import torch
from torch.autograd import Variable
from torchvision import transforms#, utils
# import torch.optim as optim
import numpy as np
from u_2_net.data_loader import RescaleT
from u_2_net.data_loader import ToTensorLab
from u_2_net.model import U2NET # full size version 173.6 MB
from PIL import Image
import os

# normalize the predicted SOD probability map
def norm_pred(d):
    ma = torch.max(d)
    mi = torch.min(d)
    dn = (d-mi)/(ma-mi)
    return dn


def preprocess(image):
    label_3 = np.zeros(image.shape)
    label = np.zeros(label_3.shape[0:2])

    if (3 == len(label_3.shape)):
        label = label_3[:, :, 0]
    elif (2 == len(label_3.shape)):
        label = label_3
    if (3 == len(image.shape) and 2 == len(label.shape)):
        label = label[:, :, np.newaxis]
    elif (2 == len(image.shape) and 2 == len(label.shape)):
        image = image[:, :, np.newaxis]
        label = label[:, :, np.newaxis]

    transform = transforms.Compose([RescaleT(320), ToTensorLab(flag=0)])
    sample = transform({
        'imidx': np.array([0]),
        'image': image,
        'label': label
    })

    return sample


def pre_net():
    # 采用n2net 模型数据
    model_name = 'u2net'
    path = os.path.dirname(__file__)
    model_dir = path+'/saved_models/'+ model_name + '/' + model_name + '.pth'
    net = U2NET(3,1)
    net.load_state_dict(torch.load(model_dir, map_location=torch.device('cpu')))
    if torch.cuda.is_available():
        net.cuda()
    net.eval()
    return net


def pre_test_data(img):
    torch.cuda.empty_cache()
    sample = preprocess(img)
    with torch.no_grad():
        inputs_test = torch.FloatTensor(sample["image"].unsqueeze(0).float())
    #inputs_test = sample['image'].unsqueeze(0)
    #inputs_test = inputs_test.type(torch.FloatTensor)
    #if torch.cuda.is_available():
    #    inputs_test = Variable(inputs_test.cuda())
    #else:
    #    inputs_test = Variable(inputs_test)
    return inputs_test


def get_im(pred):
    predict = pred
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy()
    im = Image.fromarray(predict_np*255).convert('RGB')
    return im

def test_seg_trimap(org,alpha, alpha_resize):
    # 将原始图片转换成 Alpha图
    # org：原始图片
    # org_trimap:
    # resize_trimap: 调整尺寸的trimap
    image = Image.open(org)
    sample = preprocess(np.array(image))
    #model_name = 'u2net'
    #path = os.path.dirname(__file__)
    #model_dir = path+'/saved_models/'+ model_name + '/' + model_name + '.pth'
    #net = U2NET(3,1)
    #net.load_state_dict(torch.load(model_dir, map_location=torch.device('cpu')))
    #if torch.cuda.is_available():
    #    net.cuda()
    #net.eval()
    
    net = pre_net()
    with torch.no_grad():
        inputs_test = torch.FloatTensor(sample["image"].unsqueeze(0).float())
        d1, _, _, _, _, _, _ = net(inputs_test)
        # normalization
        pred = d1[:, 0, :, :]
        predict = norm_pred(pred).squeeze().cpu().data.numpy()
        # 将数据转换成图片
        im =  Image.fromarray(predict*255).convert('RGB')
        #im.save(alpha)
        # 根据原始图片调整尺寸
        imo = im.resize((image.size), resample=Image.BILINEAR)
        imo.save(alpha_resize)
        del d1, pred, predict, inputs_test, sample, net 


# if __name__ == "__main__":
#     test_seg_trimap("..\\img\\meinv.jpg","..\\img\\trimap\\meinv_alpha.png","..\\img\\trimap\\meinv_alpha_resize.png")
#     #pil_wait_blue()

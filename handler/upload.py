import os
import tornado.web
import shortuuid
from u_2_net import my_u2net_test
from to_background import to_background
from to_background import to_standard_trimap
from resize import resize_image
from utils import date_util
import handler.base as base
import re
class UploadHandler(base.BaseHandler):

    def post(self, *args, **kwargs):

        
        
        filePath =""
        # 查看上传文件的完整格式，files以字典形式返回
        # {'file1':
        # [{'filename': '新建文本文档.txt', 'body': b'61 60 -83\r\n-445 64 -259', 'content_type': 'text/plain'}],
        # 'file2':
        filesDict = self.request.files
        config_path = self.get_file_path()
        width = self.get_body_argument('width')
        height = self.get_body_argument('height')
        num_re = r'^\d+$';
        if width and not re.match(num_re,width):
            self.write_fail('width参数不正确')
        elif height and not re.match(num_re,height):
            self.write_fail('height参数不正确')
        else:
            color = self.get_body_argument('color')
            self.handler_image(filesDict, width, height, color, config_path)
 
    def handler_image(self, filesDict, width, height, color, config_path ):
        today = date_util.todaystr()
        parent_folder = config_path['root_folder']
        static_folder = config_path['static']
        parent_path = os.path.join(parent_folder, static_folder, today)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        filename=shortuuid.uuid()
        for inputname in filesDict:
            # 第一层循环取出最外层信息，即input标签传回的name值
            # 用过filename键值对对应，取出对应的上传文件的真实属性
            http_file = filesDict[inputname]
            for fileObj in http_file:
                upload_name = fileObj.filename
                upload_name_suffix = upload_name.split('.')[1]
                upload_name_suffix = '.' + upload_name_suffix 
                # 第二层循环取出完整的对象
                # 取得当前路径下的 upfiles 文件夹+上fileObj.filename属性(即真实文件名)
                filePath = os.path.join(parent_path, filename+upload_name_suffix)
                
                with open(filePath, 'wb') as f:
                    f.write(fileObj.body)



        org_img = filePath
        self.resize_image(org_img, width, height, color, filename, upload_name_suffix, config_path)

    def resize_image(self, org_img, width, height, color, filename, suffix, config_path):
        today = date_util.todaystr()
        parent_folder = config_path['root_folder']
        static_folder = config_path['static']
        temp_folder = config_path['temp']
        parent_path = os.path.join(parent_folder, static_folder, today)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        temp_path = os.path.join(parent_folder, temp_folder)
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        #id_image = os.path.join(parent_path, filename+"id.png")
        # 20200719
        # 通过识别人脸关键点，裁剪图像
        #ai_crop.crop_photo(org_img,id_image, width, height )


        
        alpha_img = os.path.join(temp_path, filename+"_alpha.png")
        
        alpha_resize_img = os.path.join(temp_path, filename+"_alpha_resize.png")
        
        #
        # 通过u_2_net 获取 alpha 先不裁剪
        my_u2net_test.test_seg_trimap(org_img, alpha_img, alpha_resize_img)
        #
        # # 通过alpha 获取 trimap
        trimap = os.path.join(temp_path, filename+"_trimap_resize.png")
        to_standard_trimap.to_standard_trimap(alpha_resize_img, trimap)
        
        #原图
        id_image_org = os.path.join(parent_path, filename+"id_2in.jpg")
        #原图经过u_2_net 匹配不含背景图
        cutout_image = os.path.join(parent_path, filename+"_cutout.png")
        back_image = os.path.join(temp_path, filename+"_bj.png")
        to_background.to_background(org_img, trimap, id_image_org, color,back_image, cutout_image)
        info = {}
        if width   and height:
            width = int(width)
            height = int(height)
         
            target_image = os.path.join(parent_path, filename+'_finally.jpg')
            resize_image.resize_image(id_image_org, width, height, target_image)
            target_iamge_cut = os.path.join(static_folder, today, filename+'_finally.jpg')
            info['targetImageCut'] = target_iamge_cut
        #最终图包含背景且切图
        source_image = os.path.join(static_folder, today, filename+suffix)
        source_image_not_back = os.path.join(static_folder, today, filename+"_cutout.png")
        info['sourceImage'] = source_image
        info['sourceImageNotBack'] = source_image_not_back
        info['targetWidth']=width
        info['targetHeight']=height
        source_height,source_width = resize_image.image_shape(org_img)
        info['sourceWidth']=source_width
        info['sourceHeight']=source_height
        image_path = self.get_image_path()
        info['imageDomain']=image_path['image_domain']
        self.write_success_data(info)


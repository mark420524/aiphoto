import m_dlib.face_marks as fmarks
from PIL import Image


def crop_photo(path, target, width, height):
    path = path
    shape, d = fmarks.predictor_face(path)
    print('pred',d)
    WIDTH_2IN = width/2
    HEIGHT_2IN = height/2
    print(WIDTH_2IN,HEIGHT_2IN)
    # 人像中心点
    X_CENTRE = d.left()+(d.right()-d.left()) / 2
    Y_CENTER = d.top()+(d.bottom()-d.top()) / 2
    print(X_CENTRE,Y_CENTER)
    im = Image.open(path)
    im = im.crop((X_CENTRE-WIDTH_2IN, Y_CENTER-HEIGHT_2IN, X_CENTRE+WIDTH_2IN, Y_CENTER+HEIGHT_2IN))
    im.save(target)


# 通过识别人脸关键点，裁剪图像
# crop_photo("..//img//meinv_id.png","..//img//2in.jpg")

from pymatting import *
from PIL import Image,ImageColor
color_dict = {
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "blue": (67, 142, 219)
}


def to_background(org, resize_trimap, id_image, color,back_image, cutout_image=''):
    """
        org：原始图片
        resize_trimap：trimap
        id_image：新图片
        colour: 背景颜色
    """
    scale = 1.0
    image = load_image(org, "RGB", scale, "box")
    trimap = load_image(resize_trimap, "GRAY", scale, "nearest")
    im = Image.open(org)
    # estimate alpha from image and trimap
    alpha = estimate_alpha_cf(image, trimap)



    # estimate foreground from image and alpha
    foreground, background = estimate_foreground_ml(image, alpha, return_background=True)
    if cutout_image:
        cutout = stack_images(foreground, alpha)
        save_image(cutout_image, cutout)
    if not color:
       return -1
    try:
        new_background = Image.new('RGB', im.size, color_dict[color])
    except KeyError :
        #此时自定义颜色
        try:
            image_color = ImageColor.getrgb(color)
        except ValueError:
            #自定义颜色值不对,默认白色
            image_color = color_dict['white']
        new_background = Image.new('RGB', im.size, image_color)
        
    new_background.save(back_image)
    # load new background
    new_background = load_image(back_image, "RGB", scale, "box")
    # blend foreground with background and alpha
    new_image = blend(foreground, new_background, alpha)
    save_image(id_image, new_image)


def to_background_grid(org, resize_trimap, id_image):
    """
        org：原始图片
        resize_trimap：trimap
        id_image：新图片
        colour: 背景颜色
    """
    scale = 1.0
    image = load_image(org, "RGB", scale, "box")
    trimap = load_image(resize_trimap, "GRAY", scale, "nearest")
    im = Image.open(org)
    # estimate alpha from image and trimap
    alpha = estimate_alpha_cf(image, trimap)

    # estimate foreground from image and alpha
    foreground, background = estimate_foreground_ml(image, alpha, return_background=True)
    images = [image]
    for k,v in colour_dict.items():
        new_background = Image.new('RGB', im.size, v)
        new_background.save("bj.png")
        new_background = load_image("bj.png", "RGB", scale, "box")
        new_image = blend(foreground, new_background, alpha)
        images.append(new_image)

    grid = make_grid(images)
    save_image(id_image, grid)


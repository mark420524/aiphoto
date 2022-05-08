import os
import shortuuid
from to_background import to_background
from to_background import to_standard_trimap
from utils import date_util
import handler.base as base
from cloud import cloud_cos

class ComposeHandler(base.BaseHandler):

    def post(self, *args, **kwargs):
        config_path = self.get_file_path()
        color = self.get_body_argument('color')
        source_image  = self.get_body_argument('sourceImage')
        if not source_image or not color:
            self.write_fail('参数不正确')
        else:
            self.compose_image(source_image, color, config_path)
 
    def compose_image(self, source_image,  color, config_path):
        filename=source_image.split('.')[0]
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
        #alpha_resize_img = os.path.join(temp_path, filename+"_alpha_resize.png")
        
        #
        # 通过u_2_net 获取 alpha 先不裁剪
        #my_u2net_test.test_seg_trimap(org_img, alpha_img, alpha_resize_img)
        #
        # # 通过alpha 获取 trimap
        trimap = os.path.join(temp_path, filename+"_trimap_resize.png")
        #to_standard_trimap.to_standard_trimap(alpha_resize_img, trimap)
        
        #原图
        #原图经过u_2_net 匹配不含背景图
        origin_image = os.path.join(parent_path, source_image)
        compose_name = shortuuid.uuid()
        image_absolute_path = os.path.join(parent_path, compose_name+"_compose.jpg") 
        back_image = os.path.join(temp_path, filename+"_bj.png")
        to_background.to_background(origin_image, trimap, image_absolute_path, color, back_image)
        info = {}
        self.delete_temp_file(origin_image)
        self.delete_temp_file(trimap)
        self.delete_temp_file(back_image)
        #最终图包含背景且切图
        image_src = os.path.join(static_folder,today,compose_name+"_compose.jpg")
        info['imageSrc']=image_src
        info['imageDomain'] = cloud_cos.get_default_domain()
        cloud_cos.upload_default_bucket( image_absolute_path , image_src)
        self.delete_temp_file(image_absolute_path)
        self.write_success_data(info)


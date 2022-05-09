import tornado.web
import os
import handler.base as base
import re
from utils import date_util
import config.config as config

class DeleteHandler(base.BaseHandler):
    def post(self, *args, **kwargs):
        source_image  = self.get_body_argument('sourceImage')
        if not source_image :
            self.write_fail('参数不正确')
        else:
            filename=source_image.split('.')[0]
            words_re = r'^\w+$'
            if not re.match(words_re, filename):
                self.write_fail('参数不正确')
            else:
                self.delete_history_file(source_image)
    def delete_history_file(self, source_image):
        config_path = self.get_file_path()
        today = date_util.todaystr()
        parent_folder = config_path['root_folder']
        static_folder = config_path['static']
        temp_folder = config_path['temp']
        filename=source_image.split('.')[0]
        parent_path = os.path.join(parent_folder, static_folder, today)
        temp_path = os.path.join(parent_folder, temp_folder)
        origin_image = os.path.join(parent_path, source_image)
        trimap = os.path.join(temp_path, filename+"_trimap_resize.png")
        self.delete_temp_file(origin_image)
        self.delete_temp_file(trimap)
        self.write_success()

import handler.base as base

class OtherAppHandler(base.BaseHandler):
    def get(self, *args, **kwargs):
        other_app_info = [{"appId":"wx7cd1c3802bbb34fa","icon":"coupon-o","iconColor":"red","path":"/pages/index/index","text":"早晚券"},{"appId":"wx09293d6036709520","icon":"checked","iconColor":"green","path":"/pages/index/index","text":"早晚答"}]
        self.write_success_data(other_app_info)

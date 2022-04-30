import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def write_success(self):
        self.set_header('Content-Type', 'application/json')
        ret_result = {}
        ret_result['code'] = 0
        ret_result['message'] = ''
        self.write(tornado.escape.json_encode(ret_result))

    def write_success_data(self,data):
        self.set_header('Content-Type', 'application/json')
        ret_result = {}
        ret_result['code'] = 0; 
        ret_result['message'] = ''
        ret_result['data']=data
        self.write(tornado.escape.json_encode(ret_result))
    def write_fail(self, message):
        self.set_header('Content-Type', 'application/json')
        ret_result = {}
        ret_result['code'] = -1
        ret_result['message'] = message
        self.write(tornado.escape.json_encode(ret_result))

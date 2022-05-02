import tornado.ioloop
import tornado.web
import handler.upload as upload
import handler.compose as compose
import os



def make_app():
    static_path = os.path.dirname(os.path.dirname(__file__))   
    static_path = os.path.join(static_path, 'static')
    return tornado.web.Application([
        
        (r"/upload",    upload.UploadHandler),
        (r"/compose",    compose.ComposeHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path})
    ]
    )


if __name__ == "__main__":
    app = make_app()
    port = 9000
    print('app service listen %d' % port)
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()

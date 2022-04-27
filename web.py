import tornado.ioloop
import tornado.web
import handler.upload as upload
import os



def make_app():
    static_path = os.path.dirname(os.path.dirname(__file__))   
    static_path = os.path.join(static_path, 'static')
    return tornado.web.Application([
        
        (r"/upload",    upload.UploadHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path})
    ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8013)
    tornado.ioloop.IOLoop.current().start()

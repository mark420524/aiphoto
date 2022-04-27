import tornado.ioloop
import tornado.web
import handler.upload as upload
import os



def make_app():
    return tornado.web.Application([
        
        (r"/upload",    upload.UploadHandler)
    ]
    )


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = make_app()
    app.listen(8013)
    tornado.ioloop.IOLoop.current().start()

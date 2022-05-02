import tornado.ioloop
import tornado.web
import handler.upload as upload
import handler.compose as compose
import os
import config.config as config



def make_app():
    config_path = config.get_config('file_path')
    root_folder = config_path['root_folder']
    static_folder = config_path['static']
    static_path = os.path.join(root_folder, static_folder)
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

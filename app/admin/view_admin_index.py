import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1 style='color:green' > 这是后台管理系统</h1>")
        # self.redirect()

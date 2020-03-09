"""
    tornado web app对于网页模板的处理和静态文件的操作
    网页模板：html页面
    处理：定义html页面、渲染html页面，响应html页面[浏览器]
    静态资源：图片/js/css/字体...
    操作：配置静态资源、查询静态资源[html]、响应数据
"""

# 引入需要的模块
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer
import os.path
from concurrent.futures import ThreadPoolExecutor
# 定义变量
define("port", default=8000, help="默认端口8000")
class CommonHandler(RequestHandler):
    #定义线程池
    executor = ThreadPoolExecutor(50)

    #前缀地址
    @property
    def site_url(self):
        return 'http://127.0.0.1:8003'

    @property
    def md(self):
        return self.application.md

    #客户端向服务端发送给请求并处理
    @property
    def params(self):
        data = self.request.body
        #包含字节型类型，转化为python数据类型
        data = {
            k:v
            for k,v in json.loads(data.decode('utf-8')).items()
        }
        return data

    #时间属性
    @property
    def dt(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #公共参数
    @property
    def common_params(self):
        data = dict(
            createAt = self.dt,
            ip = self.request.remote_ip, #获取IP地址
            # addr = ip2addr(self.request.remote_ip)['region'].decode('utf-8'),
            headers = dict(self.request.headers)
        )
        return data
    def html(self, template_name, **kwargs):
        """Renders the template with the given arguments as the response."""
        if self._finished:
            raise RuntimeError("Cannot render() after finish()")
        html = self.render_string(template_name, **kwargs)

        # Insert the additional JS and CSS added by the modules on the page
        js_embed = []
        js_files = []
        css_embed = []
        css_files = []
        html_heads = []
        html_bodies = []
        for module in getattr(self, "_active_modules", {}).values():
            embed_part = module.embedded_javascript()
            if embed_part:
                js_embed.append(utf8(embed_part))
            file_part = module.javascript_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    js_files.append(file_part)
                else:
                    js_files.extend(file_part)
            embed_part = module.embedded_css()
            if embed_part:
                css_embed.append(utf8(embed_part))
            file_part = module.css_files()
            if file_part:
                if isinstance(file_part, (unicode_type, bytes)):
                    css_files.append(file_part)
                else:
                    css_files.extend(file_part)
            head_part = module.html_head()
            if head_part:
                html_heads.append(utf8(head_part))
            body_part = module.html_body()
            if body_part:
                html_bodies.append(utf8(body_part))

        if js_files:
            # Maintain order of JavaScript files given by modules
            js = self.render_linked_js(js_files)
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + utf8(js) + b'\n' + html[sloc:]
        if js_embed:
            js = self.render_embed_js(js_embed)
            sloc = html.rindex(b'</body>')
            html = html[:sloc] + js + b'\n' + html[sloc:]
        if css_files:
            css = self.render_linked_css(css_files)
            hloc = html.index(b'</head>')
            html = html[:hloc] + utf8(css) + b'\n' + html[hloc:]
        if css_embed:
            css = self.render_embed_css(css_embed)
            hloc = html.index(b'</head>')
            html = html[:hloc] + css + b'\n' + html[hloc:]
        if html_heads:
            hloc = html.index(b'</head>')
            html = html[:hloc] + b''.join(html_heads) + b'\n' + html[hloc:]
        if html_bodies:
            hloc = html.index(b'</body>')
            html = html[:hloc] + b''.join(html_bodies) + b'\n' + html[hloc:]
        self.write(html)


# 创建视图类
import time
class IndexHandler(CommonHandler):
    # @tornado.concurrent
    def get(self):
        print("进入")
        msg = "hello,零"
        time.sleep(5)
        self.html("index.html", info=msg)
    
# class CustomApplication(Application):
#     def __int__(self):
#         # static_handlers = configs
#         # handlers = urls
#         handlers = [
#             (r'/',IndexHandler),

#         ]
#         settings = dict(
#             static_path = os.path.join(root_path,"static"),
#             templates_path = os.path.join(root_path,"templates"),
#             debug = True
#             )
#         super(CustomApplication,self).__init__(handlers=handlers,  **settings)





# 程序入口
if __name__ == '__main__':
    # 开始监听
    parse_command_line()
    app = Application(
        [
            (r'/', IndexHandler)
        ],

        # 项目配置信息
        # 网页模板
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # 静态文件
        static_path=os.path.join(os.path.dirname(__file__), "static"),

        debug=True
    )
    # app = CustomApplication()
    print(app.settings)
    # 部署
    server = HTTPServer(app)
    server.listen(options.port)

    # 轮询监听
    IOLoop.current().start()
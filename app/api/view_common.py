# _*_ coding: utf-8 _*_
import os
import datetime
import json
import tornado.web
from concurrent.futures import ThreadPoolExecutor
from app.common.ip2Addr import ip2addr
from werkzeug.datastructures import MultiDict


class CommonHandler(tornado.web.RequestHandler):
    # 定义线程池
    executor = ThreadPoolExecutor(50)

    # 定义root_path
    @property
    def root_path(self):
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # 定义上传文件保存位置
    @property
    def upload_path(self):
        return os.path.join(self.root_path, "static/upload/")
    # 定义上传文件保存位置
    @property
    def file_db_path(self):
        return "/static/upload/"
    # 前缀地址
    @property
    def site_url(self):
        return 'http://127.0.0.1:8003'

    @property
    def md(self):
        return self.application.md

    # 客户端向服务端发送给请求并处理
    @property
    def params(self):
        data = self.request.body
        # 包含字节型类型，转化为python数据类型
        data = {
            k: v
            for k, v in json.loads(data.decode('utf-8')).items()
        }
        return data

    # 时间属性
    @property
    def dt(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 公共参数
    @property
    def common_params(self):
        data = dict(
            createAt=self.dt,
            ip=self.request.remote_ip,  # 获取IP地址
            # addr = ip2addr(self.request.remote_ip)['region'].decode('utf-8'),
            headers=dict(self.request.headers)
        )
        return data
    # 获取HTML传过来的表单数据,ajax异步提交数据的方法
    @property
    def ajax_params(self):
        data = self.request.arguments
        data = {
            k: list(
                map(
                    lambda val: str(
                        val, encoding='utf-8'
                    ),
                    v
                )
            )
            for k, v in data.items()
        }
        return data
    # 表单数据
    @property
    def form_params(self):
        # print("self.ajax_params",self.ajax_params)
        return MultiDict(self.ajax_params)

    def html(self, template_name, **kwargs):

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
        return self.write(html)


if __name__ == "__main__":
    print(
        CommonHandler.common_params
    )

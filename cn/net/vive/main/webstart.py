# file:
# coding:utf-8

__author__ = 'robin'

import web

urls = ("/.*", "hello")
app = web.application(urls, globals())


class hello:
    def GET(self):
        return "helo world"


if __name__ == "__main__":
    app.run()

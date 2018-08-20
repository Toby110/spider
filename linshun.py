from tornado import web,ioloop,httpserver
from download import *
import time
import requests
import re
import urllib.request
import json
import pymysql
import os
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("toby.html")
    def post(self, *args, **kwargs):
        weather=self.get_argument("weather")
        mood=self.get_argument("mood")
        content=self.get_argument("content")
        data=time.localtime()
        self.render("linshun.html")
        dir_path="C:\\Users\\pc\\Desktop\\music\\"
        lin.mkdir(dir_path)
        for m in range(1,4):
            tom=lin("https://www.ximalaya.com/revision/play/album?albumId=14450950&pageNum={}&sort=-1&pageSize=30".format(m),dir_path)
            tom

class linshun(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("linshun.html")


if __name__=="__main__":
    app=web.Application([
              ( r"/",IndexHandler),
              ( r"/creat",linshun),
            ])
    http_server=httpserver.HTTPServer(app)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()
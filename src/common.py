#coding:UTF-8
import web
from settings import render
#class Redirect:
#    def GET(self,path):
#        web.seeother('/' + path + '/')
        
class Error:
    def GET(self,error_msg):
        return render.error(error_msg=error_msg)
        

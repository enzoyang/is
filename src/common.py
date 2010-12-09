#coding:UTF-8
import web
import random
from settings import render
from models import User
class Redirect:
    def GET(self):
        web.seeother('/admin/login/')
        
class Error:
    def GET(self,error_msg):
        return render.error(error_msg=error_msg)
        
def generalIdentity():
    result = ''
    for i in range(10):
        result += str(random.randint(0,9))
            
    return result

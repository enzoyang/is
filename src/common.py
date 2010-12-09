#coding:UTF-8
import web
import random
from settings import render
from models import User
#class Redirect:
#    def GET(self,path):
#        web.seeother('/' + path + '/')
        
class Error:
    def GET(self,error_msg):
        return render.error(error_msg=error_msg)
        
def generalIdentity(identity=None):
    def general():
        result = ''
        for i in range(10):
            result += str(random.randint(0,9))
            
    def check():
        result = general()
        if web.ctx.orm.query(User).filter(identity=result) == None and result != identity:
            return result
        else:
            return generalIdentity(identity)
    return check()    

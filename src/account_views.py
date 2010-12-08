#coding:UTF-8
import web
from models import Account
from settings import account_render,render,Errors
##region
##end region
class Error:
    def GET(self,error_msg):
        return render.error(error_msg=error_msg)
        
class Redirect:
    def GET(self,path):
        web.seeother('/' + path)

class AddUser:
    def GET(self):
        return account_render.new()
    
    def POST(self):
        i = web.input(username=None,password=None)
        if i.username and i.password:
            u = Account(_name=i.username,_password=i.password)
            web.ctx.orm.add(u)
            return "added: %s " % str(u)
        else:
            error_msg = Errors.usernameOrPasswordNotBeNull
            web.seeother('/error/' + error_msg)

class Login:
    def GET(self):
        return account_render.login()
    
    def POST(self):
        i = web.input(username=None,password=None)
        if i.username and i.password:
            u = web.ctx.orm.query(Account).filter_by(name=i.username,password=i.password).first()
            if u:
                #pass # 验证成功，转向。
                return '登录成功'
            else:#验证失败
                return account_render.login(errors=Errors.usernameAndPasswordVerifyFailure)
        else:
            return account_render.login(errors=Errors.usernameOrPasswordNotBeNull)
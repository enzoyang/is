#coding:UTF-8
import web
from models import Account
from settings import account_render,render,Errors

#decorators
def admin_required(func):
    def function(*args):
        if web.ctx.session.isLogin == 0:
            web.seeother('/login')
        else:
            return func(*args)
    return function

#views
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
        isLogin = web.ctx.session.get('isLogin',0)
    
        return account_render.login(isLogin=isLogin)
    
    def POST(self):
        i = web.input(username=None,password=None)
        if i.username and i.password:
            u = web.ctx.orm.query(Account).filter_by(name=i.username,password=i.password).first()
            if u:
                #pass # 验证成功，转向。
                web.ctx.session.isLogin = 1;
                return '登录成功'
            else:#验证失败
                return account_render.login(errors=Errors.usernameAndPasswordVerifyFailure)
        else:
            return account_render.login(errors=Errors.usernameOrPasswordNotBeNull)

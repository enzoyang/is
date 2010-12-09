#coding:UTF-8
import web
from models import Account
from settings import account_render,render,Errors
#用于传递变量
d = {}
d['links'] = [('/admin/login/',u'系统登录'),('/admin/entry/',u'管理入口'),('/admin/logout/',u'退出系统')]
#decorators
#def admin_required(func):
#    def Function(*args,**kargs):
#        isLogin = web.ctx.session.get('isLogin',0)
#        if isLogin == 0:
#            web.seeother('/admin/login/',absolute=True)
#        else:
#            return func(*args,**kargs)
#    return Function

#需要验证的action的基类
class AuthBase:
    def __init__(self):
        isLogin = web.ctx.session.get('isLogin',0)
        if isLogin == 0:
            raise web.seeother('/admin/login/',absolute=True)
#显示登录用户的基类
class AccountBase:
    def __init__(self):
        d['admin'] = u'未登录' if web.ctx.session.get('currentUser',None) == None else web.ctx.session.get('currentUser')

class Login(AccountBase):
    def GET(self):
        
        return account_render.login(**d)
    
    def POST(self):
        i = web.input(username=None,password=None)
        if i.username and i.password:
            u = web.ctx.orm.query(Account).filter_by(name=i.username,password=i.password).first()
            if u:
                #pass # 验证成功，转向。
                web.ctx.session.isLogin = 1;
                web.ctx.session.currentUser = i.username
                return web.seeother('/admin/entry/',absolute=True)
            else:#验证失败
                d['errors'] = Errors.usernameAndPasswordVerifyFailure
                return account_render.login(**d)
        else:
            d['errors'] = Errors.usernameOrPasswordNotBeNull
            return account_render.login(**d)
            
class Logout:
    def GET(self):
        web.ctx.session.kill()
        web.seeother('/admin/login/',absolute=True)

class Entry(AuthBase,AccountBase):
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        
    def GET(self):
        return account_render.entry(**d)

#urls

account_urls = (
    '/',Login,
    '/login/',Login,
    '/logout/',Logout,
    '/entry/',Entry,
)

#app
account_app = web.application(account_urls,locals())
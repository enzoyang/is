#coding:UTF-8
import web
import user
from common import generalIdentity
from account import AuthBase
from settings import expense_render,user_render,Errors,Infos
from models import Water,Electric,User
d={}
d['links'] = []
#global

class AccountBase:
    
    def __init__(self):
        d['admin'] = u'未登录' if web.ctx.session.get('currentUser',None) == None else web.ctx.session.get('currentUser')
        
class Index(AuthBase,AccountBase):
    
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/admin/entry/',u'返回管理入口')]
        
    def GET(self):
        return expense_render.entry(**d)

    
#用户管理
class IndexUser(AuthBase,AccountBase):
    
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/expense/',u'返回水电管理系统首页'),('/expense/user/add/',u'添加用户'),]
        
    def GET(self):
        totalUserCount = web.ctx.orm.query(User).count()
        d['totalUserCount'] = totalUserCount
        d['totalUser'] = web.ctx.orm.query(User).all()
        return user_render.index(**d)
    
class AddUser(AuthBase,AccountBase):
    
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/expense/',u'返回水电管理系统首页'),('/expense/user/',u'返回用户管理首页'),]
        
    def GET(self):
        return user_render.add(**d)
    
    def POST(self):
        i = web.input(realName=None)
        if i.realName:
            u = User(generalIdentity(),i.realName)
            web.ctx.orm.add(u)
            d['infos'] = Infos.userAddSuccess
        else:
            d['errors'] = Errors.realNameNotBeNull
        return user_render.add(**d)
        
class EditUser(AuthBase,AccountBase):
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/expense/',u'返回水电管理系统首页'),('/expense/user/',u'返回用户管理首页'),]
        
    def GET(self,identity):
        d['identity'] = identity
        d['user'] = web.ctx.orm.query(User).filter_by(identity=identity).first()
        d['infos'] = Infos.identityNotBeModify
        return user_render.edit(**d)
        
    def POST(self,identity):
        i = web.input(realName = None , identity = None)
        if i.realName and i.identity:
            u = web.ctx.orm.query(User).filter_by(identity=identity).first()
            u.realName = i.realName
            u.identity = i.identity
            d['infos'] = Infos.userinfoUpdateSuccess
            d['user'] = u
        else:
            d['user'] = u
            d['errors'] = Errors.userinfoNotBeNull
            
        return user_render.edit(**d)    
        
    
class ListUser(AuthBase):
    def GET(self,pageCount):
        return 'user list'
    
class DeleteUser(AuthBase):
    def GET(self,identity):
        return 'user delete : no.%s' % identity
    
#水费管理
#电费管理

urls=(
    '/',Index,
    '/index/',Index,
    
    '/user/',IndexUser,
    '/user/add/',AddUser,
    '/user/(\d+)/edit/',EditUser,
    '/user/list/(.*)/',ListUser,
    '/user/(\d+)/delete/',DeleteUser,
)

expense_app = web.application(urls,locals())
#coding:UTF-8
import web
import user
from common import generalIdentity
from account import AuthBase
from settings import expense_render,user_render,water_render,Errors,Infos
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
        d['links'] = [
            ('/admin/entry/',u'返回管理入口'),
            ('/expense/user/',u'水电用户管理'),
            ('/expense/manager/',u'水电管理'),
            ('/expense/report/',u'报表系统'),
            ]
        
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
        d['infos'] = Infos.inputRealName
        return user_render.add(**d)
    
    def POST(self):
        i = web.input(realName=None,water=0,electric=0)
        if i.realName and i.water and i.electric:
            u = User(_identity=generalIdentity(),_realName=i.realName,
                     _water=i.water,_electric=i.electric,
                     _nowWater=i.water,_nowElectric=i.electric)
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
        i = web.input(realName = None , identity = None , water = 0 ,electric = 0)
        if i.realName and i.identity and i.water and i.electric:
            u = web.ctx.orm.query(User).filter_by(identity=identity).first()
            u.realName = i.realName
            u.identity = i.identity
            u.water = i.water
            u.electric = i.electric
            d['infos'] = Infos.userinfoUpdateSuccess
            d['user'] = u
        else:
            d['user'] = u
            d['errors'] = Errors.userinfoNotBeNull
            
        return user_render.edit(**d)    
        
    
class ListUser(AuthBase):
    def GET(self,pageCount):
        return '未实现'

class ComfirmDeleteUser(AuthBase):
    def GET(self,identity):
        d['user'] = web.ctx.orm.query(User).filter_by(identity=identity).first()
        return user_render.yamade(**d)
        
class DeleteUser(AuthBase):
    def POST(self,identity):
        u = web.ctx.orm.query(User).filter_by(identity=identity).first()
        web.ctx.orm.delete(u)
        web.seeother('/expense/user/',absolute=True)
        
#用户管理结束

#水电费管理
class IndexManager(AuthBase,AccountBase):
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/expense/',u'返回水电管理系统首页'),]
    
    def GET(self):
        d['totalUser'] = web.ctx.orm.query(User).all()
        return water_render.index(**d)
        
class AddManager(AuthBase,AccountBase):
    def __init__(self):
        AuthBase.__init__(self)
        AccountBase.__init__(self)
        d['links'] = [('/expense/',u'返回水电管理系统首页'),]


urls=(
    '/',Index,
    '/index/',Index,
    
    '/user/',IndexUser,
    '/user/add/',AddUser,
    '/user/(\d+)/edit/',EditUser,
    '/user/list/(.*)/',ListUser,
    '/user/(\d+)/yamade/',ComfirmDeleteUser,
    '/user/(\d+)/delete/',DeleteUser,
    
    '/manager/',IndexManager,
    
)

expense_app = web.application(urls,locals())
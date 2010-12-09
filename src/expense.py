#coding:UTF-8
import web
import user
from account import AuthBase
from settings import expense_render
from models import Water,Electric,User

#global
class Index(AuthBase):
    def GET(self):
        return expense_render.index()

    
#用户管理
class AddUser(AuthBase):
    def GET(self):
        return 'user add'
    
class EditUser(AuthBase):
    def GET(self,identity):
        return 'user edit'
    
class ListUser(AuthBase):
    def GET(self,pageCount):
        return 'user list'
    
class DeleteUser(AuthBase):
    def GET(self,identity):
        return 'user delete'
    
#水费管理
#电费管理

urls=(
    '/index/',Index,
    
    '/user/add/',AddUser,
    '/user/(.*)/edit/',EditUser,
    '/user/list/(.*)/',ListUser,
    '/user/(.*)/delete/',DeleteUser,
)

expense_app = web.application(urls,locals())
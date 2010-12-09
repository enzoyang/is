#coding:UTF-8
import web
from account import AuthBase

class AddUser(AuthBase):
    def GET(self):
        pass
    
class EditUser(AuthBase):
    def GET(self,identity):
        pass
    
class ListUser(AuthBase):
    def GET(self,pageCount):
        pass
    
class DeleteUser(AuthBase):
    def GET(self,identity):
        pass
    
    
urls = (
    '/add',AddUser,
    '/(.*)/edit',EditUser,
    '/list/(.*)',ListUser,
    '/(.*)/delete',DeleteUser,
)

user_app = web.application(urls,locals())
#coding:UTF-8
import web
from account import AuthBase
from settings import expense_render
from models import Water,Electric
from user import user_app
class Index(AuthBase):
    def GET(self):
        return expense_render.index()

class New(AuthBase):
    def GET(self):
        return 'newer'
    
    
urls=(
    '/index/',Index,
    '/user/',user_app,
)

expense_app = web.application(urls,locals())
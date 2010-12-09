#coding:UTF-8
import web
from account import AuthBase
from settings import expense_render
from models import Water,Electric

class Index(AuthBase):
    def GET(self):
        return expense_render.index()

class New(AuthBase):
    def GET(self):
        return 'newer'
    
    
urls=(
    '/index/',Index,
    '/new/',New,
)

expense_app = web.application(urls,locals())
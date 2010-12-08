#coding:UTF-8
import web
from settings import load_sqlalchemy

urls=(
    '/(.*)/','acount_views.Redirect',
    '/login','acount_views.Login',
    '/error/(.*)','acount_views.Error',
    '/adduser','acount_views.AddUser',
)

app = web.application(urls,globals())
app.add_processor(load_sqlalchemy)
if __name__ == '__main__':
    app.run()
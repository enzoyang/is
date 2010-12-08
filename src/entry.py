#coding:UTF-8
import web
from settings import load_sqlalchemy

urls=(
    '/(.*)/','views.Redirect',
    '/login','views.Login',
    '/error/(.*)','views.Error',
    '/adduser','views.AddUser',
)

app = web.application(urls,globals())
app.add_processor(load_sqlalchemy)
if __name__ == '__main__':
    app.run()
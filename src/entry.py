#coding:UTF-8
import web
from settings import load_sqlalchemy

web.config.debug = False

urls=(
    #global
    '/(.*)/','acount_views.Redirect',
    #account
    '/login','acount_views.Login',
    '/error/(.*)','acount_views.Error',
    '/adduser','acount_views.AddUser',
    #expense
    
)
#app
app = web.application(urls,globals())
#钩子
app.add_processor(load_sqlalchemy)

#session
db = web.database(dbn="sqlite",db="data/infosys.db")
store = web.session.DBStore(db,'sessions')
session = web.session.Session(app, store)


if __name__ == '__main__':
    app.run()
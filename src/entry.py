#coding:UTF-8
import web
from settings import load_sqlalchemy,load_session

web.config.debug = False

urls=(
    #global
    '/(.*)/','account_views.Redirect',
    #account
    '/login','account_views.Login',
    '/error/(.*)','account_views.Error',
    '/adduser','account_views.AddUser',
    #expense
    
)
#app
app = web.application(urls,globals())

#钩子
app.add_processor(load_sqlalchemy)
app.add_processor(load_session)

#session
db = web.database(dbn="sqlite",db="data/infosys.db")
store = web.session.DBStore(db,'sessions')
session = web.session.Session(app, store)
web.config._session = session

if __name__ == '__main__':
    app.run()
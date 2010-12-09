#coding:UTF-8
import web
from settings import load_sqlalchemy,load_session,session_engine
import account
import expense
web.config.debug = False

urls=(
    #global
    '/error/(.*)/','common.Error',
    #apps
    '/admin',account.account_app,
    '/expense',expense.expense_app,
    #expense
    
)
#app
app = web.application(urls,globals())

#钩子
app.add_processor(load_sqlalchemy)
app.add_processor(load_session)

#session
store = web.session.DBStore(session_engine,'sessions')
session = web.session.Session(app, store)
web.config._session = session

if __name__ == '__main__':
    app.run()
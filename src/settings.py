#coding:UTF-8
import os
import web
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from web.contrib.template import render_jinja

#数据库驱动
infosys_engine = create_engine('sqlite:///data/infosys.db')
session_engine = web.database(dbn="sqlite",db="data/session.db")
#渲染器
render = render_jinja(os.getcwd() + '/templates',encoding = 'utf-8')
account_render = render_jinja(os.getcwd() + '/templates/account',encoding = 'utf-8')
expense_render = render_jinja(os.getcwd() + '/templates/expense',encoding = 'utf-8')
    
    
#钩子
def load_sqlalchemy(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=infosys_engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()

def load_session(handler):
    web.ctx.session = web.config._session
    return handler()

#错误信息
class Errors:
    usernameOrPasswordNotBeNull = u'用户名和密码不能为空'
    usernameAndPasswordVerifyFailure = u'用户名和密码验证失败'
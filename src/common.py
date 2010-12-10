#coding:UTF-8
import web
import os
import random
import datetime
from pyExcelerator import *
from settings import render
from models import User
class Redirect:
    def GET(self):
        web.seeother('/admin/login/')
        
class Error:
    def GET(self, error_msg):
        return render.error(error_msg=error_msg)

def generalRange():
    result = ''
    for i in range(10):
        result += str(random.randint(0, 9))
            
    return result

def generalIdentity():
    result = generalRange()
    if web.ctx.orm.query(User).filter_by(identity=result).first():
        return generalIdentity()
    else:
        return result
    
def generateWorkbook():
    path = os.getcwd() + '/static/workbooks/'
    wb = Workbook()
    setting = wb.add_sheet(u'信息设置')
    detail = wb.add_sheet(u'抄表明细')
    setting.write(0, 0, u'年份：')
    setting.write(0, 1, 2010)
    setting.write(1, 0, u'月份：')
    setting.write(1, 1, 12)
    setting.write(2, 0, u'水费单价：')
    setting.write(2, 1, 0.0)
    setting.write(3, 0, u'电费单价：')
    setting.write(3, 1, 0.0)
    wb.save(path + '201012.xls')
    return 'static/workbooks/' + '201012.xls'
    

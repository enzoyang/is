#coding:UTF-8
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from settings import infosys_engine

Base = declarative_base()

#account
class Account(Base):
    __tablename__ = 'account'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    password = Column(String(40))
    
    def __init__(self, _name, _password):
        self.name = _name
        self.password = _password
        
    def __repr__(self):
        return "Account(%s,%s)" % (self.name, self.password)
        
        

#expense
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    identity = Column(String(20))
    realName = Column(String(20))
    water = Column(Integer)
    electric = Column(Integer)
    nowWater = Column(Integer)
    nowElectric = Column(Integer)
    
    def __init__(self, _identity, _realName, _water, _electric, _nowWater, _nowElectric):
        self.identity = _identity
        self.realName = _realName
        self.water = _water
        self.electric = _electric
        self.nowWater = _nowWater
        self.nowElectric = _nowElectric
        
    def __repr__(self):
        return "User(%s,%s)" % (self.identity, self.realName)
        
class Water(Base):
    __tablename__ = 'waters'
    
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'))
    totalDegrees = Column(Integer)
    monthlyDegrees = Column(Integer)
    monthlyExpense = Column(Numeric)
    isPayed = Column(Boolean)
    year = Column(Integer)
    month = Column(Integer)
    
    def __init__(self, _totalDegrees, _monthlyDegrees, _monthlyExpense, _isPayed, _year, _month):
        self.userId = _userId
        self.totalDegrees = _totalDegrees
        self.monthlyDegrees = _monthlyDegrees
        self.monthlyExpense = _monthlyExpense
        self.isPayed = _isPayed
        self.year = _year
        self.month = _month
        
    def __repr__(self):
        return "Water(%d,%d,%d,%d)" % (self.userId, self.totalDegrees, self.monthlyDegrees, self.monthlyExpense)
    
class Electric(Base):
    __tablename__ = 'electrics'
    
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'))
    totalDegrees = Column(Integer)
    monthlyDegrees = Column(Integer)
    monthlyExpense = Column(Numeric)
    isPayed = Column(Boolean)
    year = Column(Integer)
    month = Column(Integer)

    
    def __init__(self, _totalDegrees, _monthlyDegrees, _monthlyExpense, _year, _month):
        self.userId = _userId
        self.totalDegrees = _totalDegrees
        self.monthlyDegrees = _monthlyDegrees
        self.monthlyExpense = _monthlyExpense
        self.isPayed = _isPayed
        self.year = _year
        self.month = _month
        
    def __repr__(self):
        return "Electric(%d,%d,%d,%d)" % (self.userId, self.totalDegrees, self.monthlyDegrees, self.monthlyExpense)
        
        
#初始化数据库
metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(infosys_engine)

#coding:UTF-8
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Numeric
from sqlalchemy.ext.declarative import declarative_base
from settings import engine

Base = declarative_base()

#account
class Account(Base):
    __tablename__ = 'account'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    password = Column(String(40))
    
    def __init__(self,_name,_password):
        self.name = _name
        self.password = _password
        
    def __repr__(self):
        return "Account(%s,%s)"%(self.name,self.password)
        
        

#expense
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key=True)
    identity = Column(String(20))
    realName = Column(String(20))
    
    def __init__(self,_identity,_realName):
        self.identity = _identity
        self.realName = _realName
        
    def __repr__(self):
        return "User(%s,%s)" % (self.identity,self.realName)
        
class Water(Base):
    __tablename__ = 'waters'
    
    id = Column(Integer,primary_key=True)
    userId = Column(Integer,ForeignKey('users.id'))
    totalDegrees = Column(Integer)
    monthlyDegrees = Column(Integer)
    monthlyExpense = Column(Numeric)
    
    def __init__(self,_totalDegrees,_monthlyDegrees,_monthlyExpense):
        self.userId = _userId
        self.totalDegrees = _totalDegrees
        self.monthlyDegrees = _monthlyDegrees
        self.monthlyExpense = _monthlyExpense
    
    def __repr__(self):
        return "Water(%d,%d,%d,%d)" % (self.userId,self.totalDegrees,self.monthlyDegrees,self.monthlyExpense)
    
class Electric(Base):
    __tablename__ = 'electrics'
    
    id = Column(Integer,primary_key)
    userId = Column(Integer,ForeignKey('users.id'))
    totalDegrees = Column(Integer)
    monthlyDegrees = Column(Integer)
    monthlyExpense = Column(Numeric)
    
    def __init__(self,_totalDegrees,_monthlyDegrees,_monthlyExpense):
        self.userId = _userId
        self.totalDegrees = _totalDegrees
        self.monthlyDegrees = _monthlyDegrees
        self.monthlyExpense = _monthlyExpense
    
    def __repr__(self):
        return "Electric(%d,%d,%d,%d)" % (self.userId,self.totalDegrees,self.monthlyDegrees,self.monthlyExpense)
        
        
#初始化数据库
metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
#coding:UTF-8
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from settings import engine

Base = declarative_base()

#account
class Account(Base):
    __tablename__ ='account'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    password = Column(String(40))
    
    def __init__(self,_name,_password):
        self.name = _name
        self.password = _password
        
    def __repr__(self):
        return "Account(%s,%s)"%(self.name,self.password)
        
        

#初始化数据库
metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)
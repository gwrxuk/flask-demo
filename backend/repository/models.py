from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return "(%s, %s)"%(self.name, self.email)

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    custid = Column(Integer)
    price = Column(Float)

    def __init__(self, name=None, custid=None, price=None):
        self.name = name
        self.custid = custid
        self.price = price

    def __repr__(self):
        return "(%s, %s, %s)"%(self.name, self.custid, self.price)

class Stock(Base):
    __tablename__="stocks"
    id=Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    price = Column(Float)
    def __init__(self, name=None, price=None):
        self.name=name
        self.price=price
    
    def __repr__(self):
        return '<Stock {self.name!r}>'

class HistoryStock(Base):
    __tablename__="history_stocks"
    id=Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    price = Column(Float)
    updated_at=Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())

    def __init__(self, name=None, price=None):
        self.name=name
        self.price=price
    
    def __repr__(self):
        return '<Stock {self.name!r}>'
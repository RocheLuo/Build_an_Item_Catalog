import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    title = Column(String(100), nullable = False, index = True)
    price = Column(Integer, nullable = False)
    id = Column(Integer, primary_key = True)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable = False)
    pic = Column(String(200),nullable = True)
    brand = relationship('Brand', backref = 'item')
    discount = relationship('Discount', backref='item')

class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer,primary_key = True)
    name = Column(String(50), nullable = False, index = True)
    logo = Column(String(200), nullable = True)
    shop = relationship('Shop', backref='brand')

class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer,primary_key=True)
    name = Column(String(20), nullable = False, index = True)
    url = Column(String(100), nullable = False)
    logo = Column(String(200), nullable = True)

class Discount(Base):
    __tablename__ = 'discount'
    item_id = Column(Integer,ForeignKey('item.id'),nullable = False)
    shop_id = Column(Integer,ForeignKey('shop.id'),nullable = False)
    discount_price = Column(Integer,nullable = False)
    start_time = Column(DateTime,nullable = False)
    end_time = Column(DateTime,nullable = True)
    id = Column(Integer,primary_key = True)


engine = create_engine('sqlite:///discount.db')

Base.metadata.create_all(engine)
# this script is used to create a tables
from sqlalchemy import Column, String, Integer,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

# creating table, in sql alchemy we use class to create a table rather than query
class Product(Base):
    __tablename__ = "products"
    ##__table_args__ = {"schema": "Test"}
    id = Column(Integer, primary_key=True,index = True)
    name= Column(String)
    description = Column(String)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey("seller.id"))
    seller = relationship("Seller",back_populates="products")

class Seller(Base):
    __tablename__ = "seller"
    ##__table_args__ = {"schema": "Test"}
    id = Column(Integer, primary_key=True,index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    products = relationship("Product",back_populates="seller")

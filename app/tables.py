from app.database import Base
from sqlalchemy import Boolean, Column, Integer, String ,Float,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
class Product(Base):
    __tablename__ = "products"
    name = Column(String,nullable=False)
    id = Column(Integer, primary_key=True,nullable=False)
    price = Column(Float,nullable=False)
    is_sale = Column(Boolean,nullable=False,server_default="False")
    time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    user_id = Column(Integer,ForeignKey("user.id",ondelete="CASCADE"),nullable=False)
    user = relationship("User")
class User(Base):
    __tablename__ = "user"
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password= Column(String,nullable=False)
    time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    id = Column(Integer, primary_key=True,nullable=False)
class Vote(Base):
    __tablename__ = "vote"
    user_id = Column(Integer,ForeignKey("user.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    item_id = Column(Integer,ForeignKey("products.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    
    
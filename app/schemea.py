from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import time ,datetime
from pydantic.types import conint

class Item(BaseModel):
    name:str
    price:float
    is_sale:Optional[bool] =False

    class Config:
        orm_mode = True
    
class create_Item(Item):
    pass



class User_base (BaseModel):
    name:str
    email : EmailStr
    password:str
    class Config:
        orm_mode = True

class create_user(User_base):
    pass
    

class view_user(User_base):
    id:int
    time:datetime
    
class view_Item(Item):
    id:int
    time:datetime
    user : view_user

class user_login(BaseModel):
    email:EmailStr
    password:str

class Token_data(BaseModel):
    id :Optional[int]=None 


class Token_response (BaseModel):
    token: str
    token_type:str
    
    class Config:
        orm_mode = True

class vote_response(BaseModel):
    item_id:int
    dir: int
    class Config:
        orm_mode = True
class item_out(BaseModel):
    Product:view_Item
    votes:int
    class Config:
        orm_mode = True
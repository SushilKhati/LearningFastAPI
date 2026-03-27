from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: str
    price: int

class DisplaySeller(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes = True

class DisplayProduct(BaseModel):
    name: str
    description: str
    #sellers: DisplaySeller
    class Config:
        from_attributes = True

class Seller(BaseModel):
    name: str
    email: str
    password: str

class DisplaySeller(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username:Optional[str] = None
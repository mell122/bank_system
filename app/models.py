from pydantic import BaseModel
from mongoengine import *

# data structure for mongoDB
class User(Document):
    username: str
    password: int

class registerRequest(BaseModel):
    name: str
    lastname: str
    email: str
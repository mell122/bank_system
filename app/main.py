import sentry_sdk, uvicorn, uuid
from mongoengine import *
from fastapi import FastAPI
from config import config
from models import registerRequest, User

cnf = config()

#monitoring 
sentry_sdk.init(
    dsn = cnf.sentry_sdk,
    traces_sample_rate = 1.0,

)

#MongoDB URI Connection
mongoUri = cnf.mongo_uri

#FastAPI
app = FastAPI()

@app.post('/register')
def create_user(reg: registerRequest):
    name = reg.name
    lastname: reg.lastname
    email: reg.email
    return {"message": f"User {email} registered successfully"} 
    

@app.post('/login')
def login(user: User):
    username = user.username
    password = user.password
    return{"message": f"User {username} registered successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=5000, log_level="info" , reload=True)

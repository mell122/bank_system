import sentry_sdk, uvicorn, uuid
from mongoengine import *
from fastapi import FastAPI
from config import config
import models

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

@app.get('/register')
def create_user:
    

@app.get('/login')
def login():
    


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=5000, log_level="info" , reload=True)

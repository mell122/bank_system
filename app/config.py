import os
from dotenv import load_dotenv

class config():

    def __init__(self) -> None:
        load_dotenv(dotenv_path = "env/config.env")

    sentry_sdk = os.getenv("SENTRY_DSN")
    mongo_uri = os.getenv("MONGO_URI")    
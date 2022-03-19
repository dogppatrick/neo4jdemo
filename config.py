import os

class MongodbConfig:
    URL = os.environ.get("MONGODB_URL")
    USERNAME = os.environ.get("MONGODB_USERNAME")
    PASSWORD = os.environ.get("MONGODB_PASSWORD")
    AUTH_DB = os.environ.get("MONGODB_AUTH_DB")
    DB_NAME = os.environ.get("MONGODB_DB_NAME")
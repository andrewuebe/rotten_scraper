from pymongo import MongoClient

MONGO_CONNECTION_STRING = "mongodb://127.0.0.1:27017/rotten_data"
client = MongoClient(MONGO_CONNECTION_STRING)
db = client.rotten_data

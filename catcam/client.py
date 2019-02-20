from pymongo import MongoClient

client = MongoClient('localhost', 27020)

db = client['machine']

collection = db['posts']
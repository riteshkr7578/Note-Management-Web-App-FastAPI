from pymongo import MongoClient
MONGO_URI="process.env.MONGO_URI"

conn=MongoClient(MONGO_URI)

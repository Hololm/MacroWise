import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Create a collection called "customers"
users = db["users"]
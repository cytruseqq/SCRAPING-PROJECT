from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["scraper_db"]
collection = db["scraped_data"]

def save_data(data):
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

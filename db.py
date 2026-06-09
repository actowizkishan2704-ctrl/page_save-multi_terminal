import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["only_db"]
collection = db["product_urls"]

# with open("urls.json", "r", encoding="utf-8") as f:
#     urls = json.load(f)

# data = [{"url": url} for url in urls]

# collection.insert_many(data)

# print("Data inserted successfully")


for url_dict in collection.find({},{"_id":0, "url":1}):
    url = url_dict.get('url')
    print(url)
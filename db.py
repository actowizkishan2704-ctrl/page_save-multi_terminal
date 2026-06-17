import json
from pymongo import MongoClient
import sys

client = MongoClient("mongodb://localhost:27017/")

db = client["only_db"]
collection = db["product_urls"]

# with open("urls.json", "r", encoding="utf-8") as f:
#     urls = json.load(f)

# data = [{"url": url} for url in urls]

# collection.insert_many(data)

# print("Data inserted successfully")
all_urls = []
# collections=collection.find({}, {"_id":0}).skip(int(sys.argv[1])).limit(int(sys.argv[2]))
for url_dict in collection.find({}, {"_id":0}).skip(int(sys.argv[1])).limit(int(sys.argv[2])):   
    # all_urls.append(url_dict)
    print(url_dict)
# for url in all_urls[int(sys.argv[1]):int(sys.argv[2])]:
#     print(url)
 
# result = collection.update_many(
#     {},
#     {"$set": {"status": 0}}
# )

# print(result.modified_count)
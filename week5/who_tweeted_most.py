from pymongo import MongoClient

client = MongoClient("mongodb: // localhost:27017")
db = client.examples

def most_tweets():
    result = db.tweet.aggregate([
        {"$group" : {"_id" : "$user.screen_name",
                     "count": {"$sum" : 1}}},
        {"$sort" : {"count" : -1}}])
    return result

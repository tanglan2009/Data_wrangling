from pymongo import MongoClient

client = MongoClient("mongodb: // localhost:27017")
db = client.examples

def hashtag_retweet_avg():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.hashtags"},
        {"$group" : {"_id" : "$entities.hashtags.text",
                     "retweet_ave" : {"$avg" : "$retweet_count"}}},
        {"$sort" : {"retweet_avg" : -1}}
    ])

    return result

def unique_hashtags_by_user():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.hashtags"},
        {"$group" : {"_id" : "$user.screen_name",
                     "unigue_hashtags" : {"$addToSet" : "$entities.hashtags.text"}}},
        {"$sort" : {"_id" : -1}}])

    return result

#exercise

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$unwind" : "$entities.hashtags"},
        {"$group" : {"_id" : "$user.screen_name",
                     "count":{ "$sum" : 1},
                     "tweet_texts" : {"$push" : "$entities.hashtags.text"}}},
        {"$sort" : {"count": -1}},
        {"$limit" :5}

    ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]
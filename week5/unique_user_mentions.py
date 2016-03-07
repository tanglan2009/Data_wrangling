import pprint
from pymongo import MongoClient

client = MongoClient("mongodb: // localhost:27017")
db = client.examples
def user_mentions():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.user_mentions"},
        {"$group" : { "_id" :"$user.screen_name",
                      "mset" : {"$addToSet" : "$entities.user_mentions.screen_name"}}},
        {"$unwind" : "$mset"},
        {"$group" : {"_id" : "$_id", "count" : {"$sum" : 1}}},
        {"$sort" : {"count" : -1}},
        {"$limit" : 10}
    ])

    return result


# exercise

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
    {"$match" : {"country" : "India"}},
        {"$unwind" : "$isPartOf"},
        {"$group" : {"_id" : "$isPartOf",
                     "avgCityPopulation" : { "$avg" : "$population"}}},
        {"$group" : {"_id" : "$_id",
                     "avg" : {"$avg" : "$avgCityPopulation"}
                     }},
        {"$sort" : {"count" : -1}},
        {"$limit" : 1}
    ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    assert abs(result[0]["avg"] - 196025.97814809752) < 10 ** -8
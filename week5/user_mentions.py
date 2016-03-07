from pymongo import MongoClient

client = MongoClient("mongodb: // localhost:27017")
db = client.examples

def user_mentions():
    result = db.tweets.aggregate([
        {"$unwind" : "$entities.user_mentions"},
        {"#group" : {"_id" : "$user.screen_name",
                     "count" : { "$sum" : 1}}},
        {"$sort" : {"count" : -1}},
        {"$limit" : 1}])


#execise
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
                     "count" : { "$sum" : 1}}},
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
    print "Printing the first result:"
    import pprint
    pprint.pprint(result[0])
    assert result[0]["_id"] == "Uttar Pradesh"
    assert result[0]["count"] == 623

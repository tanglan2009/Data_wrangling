def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
        {"$match" : {"country" : {"$exists" : "true"}}},
        {"$unwind" : "$isPartOf"},
        {"$group" : {"_id" : "$isPartOf",
                     "avgCityPopulation" : { "$avg" : "$population"}}},
        {"$group" :{ "_id" : "$_id",
                     "avgRegionalPopulation" : {"$avg" : "$avgCityPopulation"}}},
        {"$group" : {"country" : "$country",
                     "avgRegionalPopulation" : {"$avg" :"$avgRegionalPopulation"}}}


                ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result) < 150:
        pprint.pprint(result)
    else:
        pprint.pprint(result[:100])
    key_pop = 0
    for country in result:
        if country["_id"] == 'Lithuania':
            assert country["_id"] == 'Lithuania'
            assert abs(country["avgRegionalPopulation"] - 14750.784447977203) < 1e-10
            key_pop = country["avgRegionalPopulation"]
    assert {'_id': 'Lithuania', 'avgRegionalPopulation': key_pop} in result
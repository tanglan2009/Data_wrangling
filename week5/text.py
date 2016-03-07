def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [  # {"$match" : {"country" : {"$exists" : "true"}}},
                  {"$project": {"country": 1, "population": 1, "isPartOf": 1}},
                  {"$unwind": "$isPartOf"},
                  {"$group": {"_id":
                                  {"reg": "$isPartOf", "country": "$country"}
                  },
                   "avgCityPopulation":
                       {"$avg": "$population"}
                  }
                  #{"$group" :{ "_id" : "$_id",
                  #            "avgRegionalPopulation" : {"$avg" : "$avgCityPopulation"}}},
                  #{"$group" : {"country" :{"$_id" : "$country"},
                  #"avgRegionalPopulation" : {"$avg" :"$avgRegionalPopulation"}}}
    ]
    return pipeline
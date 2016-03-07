## Inequality operators
## $gt
## $lt
## $gte
## $lte
## $ ne

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.examples
print "__________"
def find():

    query = {"population" : {"$gt" : 250000}}
    #
    query2 = {"foundingDate" : { "$gt" : datetime(1837, 1, 1), "$lte" : datetime(1837, 12, 31)}}
    cities = db.cities.find(query)

    num_cities = 0
    for c in cities:
        pprint.pprint(c)
        num_cities += 1

    print "\nNumber of cities matching: %d\n" % num_cities
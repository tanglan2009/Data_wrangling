from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

tesla_s = {
    "manufacturer" : "Tesla Motors",
    "class" : "full-size",
    "body style" : "5-door liftback",
    "production" : [2012, 2013],
    "model years" : [2013],
    "layout" : ["Rear-motor", "rear-whell drive"],
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holzhausen"
    },
    "assembly" : [
        {
            "country" : "United States",
            "city" : "Fremont",
            "state" : "California"
        },
        {
            "country" : "The Netherlands",
            "city" : "Tilburg"
        }
    ]
}


db.autos.insert(tesla_s)

for a in db.autos.find():
    pprint.pprint(a)

def find():
    autos = db.autos.find({"manufacturer" :"Toyata"})
    for a in autos:
        pprint.pprint(a)
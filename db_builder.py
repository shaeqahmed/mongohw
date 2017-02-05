from pymongo import MongoClient
import csv

def add():
    server = MongoClient("149.89.150.100") #homer ip address, we need to ssh and clone to see if it works or substitute with our own ip address

    dataBase = server.Patriots_AhmedS_OstlundW
    
    a = open("peeps.csv")
    b = open("courses.csv")
    peeps = csv.DictReader(a)
    courses = csv.DictReader(b)
    for info in peeps:
        id  = info["id"]
        dict = {"id": id,
                "age": info["age"],
                "name": info["name"],
                "courses": []
        }
        for i in courses:
            if i["id"] == id:
                dict["courses"].append([ i["code"], i["mark"] ] )
        dataBase.students.insert_one(dict)

add()
from pymongo import MongoClient
import csv

def add():
    server = MongoClient("127.0.0.1") #homer ip address, we need to ssh and clone to see if it works or substitute with our own ip address

    dataBase = server.Patriots_AhmedS_OstlundW
    
    a = open("peeps.csv")
    b = open("courses.csv")
    peeps = csv.DictReader(a)
    courses = csv.DictReader(b)
    for info in peeps:
        #rint info
        id  = info["id"]
        dict = {"id": id,
                "age": info["age"],
                "name": info["name"],
                "courses": []
        }
        for i in courses:
            #rint i["id"]
            #rint id
            if i["id"] == id:
                dict["courses"].append([ i["code"], i["mark"] ] )
        j = open("courses.csv")
        courses = csv.DictReader(j)
        dataBase.students.insert_one(dict)
    c = dataBase.students.find()
    #print c.count()
    #for x in c:
        #print x
add()

from pymongo import MongoClient
import csv

def getIds(students, course):
    ans = []
    for i in students:
        for a in i["courses"]:
            if a[0] == course:
                ans.append(i["id"])
    return ans

def main():
    a = open("teachers.csv")
    read = csv.DictReader(a)
    server = MongoClient("127.0.0.1")
    db = server.Patriots_AhmedS_OstlundW
    col = db.teachers
    students = db.students
    for i in read:
        dict = {
            "name": i["teacher"],
            "class": i["code"],
            "period": i["period"]
            }
        c = students.find()
        dict["students"] = getIds(c, i["code"])
        col.insert_one(dict)

main()
#server = MongoClient("149.89.150.100")
#col = server.Patriots_AhmedS_OstlundW.teachers
#a = col.find()
#for i in a:
    #print i

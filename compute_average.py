from pymongo import MongoClient

def compute(x):
    i = 0.0
    ans = 0.0
    for a in x:
        i += 1.0
        ans += a[1]
    return ans/i

    
def computeAverage():
    server = MongoClient("149.89.150.100")
    col = server.Patriots_AhmedS_OstlundW.students
    c = col.find()
    averages = []
    ids = []
    names = []
    for a in c:
        averages.append([compute(a["courses"])])
        ids.append([a["id"])
        names.append([a["name"]])
    for i in range(len(averages)):
        print "Name: "+names[i]+" ID: "+ids[i]+" Average: "+averages[i]


    

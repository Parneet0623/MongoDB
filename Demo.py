import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Employee']

information = mydb.employeeinformation

record = [{"firstname" : "Parneet1", "lastname" : "Kaur1"}, {"firstname" : "Parneet2", "lastname" : "Kaur2", "age" : "25"}]

information.insert_many(record)
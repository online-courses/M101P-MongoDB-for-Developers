import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
users = db.users

doc = {'firstname':'Francisco', 'lastname':'Albarran'}
print doc
print "about to insert the document"

try:
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]

doc = {'firstname':'Francisco', 'lastname':'Albarran'}

print doc
print "inserting again"

try:
    users.insert(doc)
except:
    print "second insert failed:", sys.exc_info()[0]

print doc


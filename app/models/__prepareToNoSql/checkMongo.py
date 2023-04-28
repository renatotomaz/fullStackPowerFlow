'''This script is used to check if the data
was correctly inserted into the MongoDB.
It is not part of the application itself.'''

import pymongo

DATABASE_NAME = 'network'
COLLECTION_NAME = 'buses'

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

cursor = collection.find({'name': '38'})
for document in cursor:
    print(document)
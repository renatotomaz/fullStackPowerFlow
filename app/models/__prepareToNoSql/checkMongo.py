'''This script is used to check if the data
was correctly inserted into the MongoDB.
It is not part of the application itself.'''

import pymongo
import pickle as pkl

DATABASE_NAME = 'network'
BUS_COLLECTION_NAME = 'buses'
CIRCUIT_COLLECTION_NAME = 'circuits'

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[DATABASE_NAME]
collection = db[BUS_COLLECTION_NAME]

cursor = collection.find({'name': '38'})
for document in cursor:
    print(document)

# busesIdDict = {}
# cursor = collection.find({})
# for document in cursor:
#     busesIdDict[document['name']] = document['_id']

# with open('app/models/__prepareToNoSql/busesIdDict.pkl', 'wb') as f:
#     pkl.dump(busesIdDict, f)

collection = db[CIRCUIT_COLLECTION_NAME]

cursor = collection.find({})
for document in cursor:
    print(document)

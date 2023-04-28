"""This script reads the pkl file
with the Network data and insert it
into the MongoDB database."""

import pymongo
import pickle as pkl

DATABASE_NAME = 'network'
BUS_COLLECTION_NAME = 'buses'
CIRCUIT_COLLECTION_NAME = 'circuits'

# Get the bus documents from the pkl file
with open('app/models/__prepareToNoSql/networkToBson.pkl', 'rb') as f:
    busDocs = pkl.load(f)

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[DATABASE_NAME]

# Get the desired collection
#collection = db[BUS_COLLECTION_NAME]

# Insert the documents into the collection
#collection.insert_many(busDocs)

# Get the circuit documents from the pkl file
with open('app/models/__prepareToNoSql/circuitsToBson.pkl', 'rb') as f:
    circuitDocs = pkl.load(f)

# Get the desired collection
collection = db[CIRCUIT_COLLECTION_NAME]

# Insert the documents into the collection
collection.insert_many(circuitDocs)


#
#client = pymongo.MongoClient("mongodb://localhost:27017/")
#db = client["mydatabase"]
#col = db["mycollection"]
#col.drop()
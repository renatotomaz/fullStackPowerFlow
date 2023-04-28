"""This script reads the pkl file
with the Network data and insert it
into the MongoDB database."""

import pymongo
import pickle as pkl

DATABASE_NAME = 'network'
COLLECTION_NAME = 'buses'

with open('app/models/__prepareToNoSql/networkToBson.pkl', 'rb') as f:
    busDocs = pkl.load(f)

# Connect to MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[DATABASE_NAME]

# Get the desired collection
collection = db[COLLECTION_NAME]

# Insert the documents into the collection
bus_docs = [...]  # your list of BSON documents
collection.insert_many(busDocs)
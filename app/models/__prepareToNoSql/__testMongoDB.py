from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['network']
circuits_col = db['circuits']

# Find a circuit document
circuit_doc = circuits_col.find_one({'name': "'From_14_To_15'"})

# Retrieve the related "from_bus" document from the "buses" collection
from_bus_ref = circuit_doc['from_bus']
from_bus_doc = db.dereference(from_bus_ref['_id'])

# Print the related "from_bus" document
print(from_bus_doc)
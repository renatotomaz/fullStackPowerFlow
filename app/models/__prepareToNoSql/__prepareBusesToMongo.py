"""This is just a script to collect data from
the CSV files and prepare it to be inserted
into the MongoDB database, saving the result
as a piclke file to be used by another script.
It is not part of the application itself."""

import csv
import bson
from bson import ObjectId
import sys, os
import pickle as pkl

sys.path.append(os.getcwd())

# Create an empty list to store bus documents
busDocs = []

# Open and read bus.csv file
with open('networkData/bus.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and create bus documents
    for row in reader:
        doc = {}
        doc['_id'] = ObjectId()
        doc['name'] = row['name']
        doc['vn_kv'] = float(row['vn_kv'])
        doc['type'] = row['type']
        doc['zone'] = row['zone']
        doc['in_service'] = bool(row['in_service'])
        doc['max_vm_pu'] = float(row['max_vm_pu'])
        doc['min_vm_pu'] = float(row['min_vm_pu'])
        doc['x_pos'] = float(row['x_pos'])
        doc['y_pos'] = float(row['y_pos'])
        # Add the bus document to the list
        busDocs.append(doc)

# Open and read load.csv file
with open('networkData/load.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and add load data to bus documents
    for row in reader:
        # Find the bus document that matches the load bus
        bus_doc = next((doc for doc in busDocs if doc['name'] == row['bus']), None)
        if bus_doc:
            # Add the load data to the bus document
            bus_doc.setdefault('loads', []).append({
                'id': ObjectId(),
                'name': row['name'],
                'p_mw': float(row['p_mw']),
                'q_mvar': float(row['q_mvar']),
                'const_z_percent': float(row['const_z_percent']),
                'const_i_percent': float(row['const_i_percent']),
                'sn_mva': float(row['sn_mva']),
                'scaling': float(row['scaling']),
                'in_service': bool(row['in_service']),
                'type': row['type'],
                'controllable': bool(row['controllable'])
            })

# Open and read generator.csv file
with open('networkData/generator.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and add generator data to bus documents
    for row in reader:
        # Find the bus document that matches the generator bus
        bus_doc = next((doc for doc in busDocs if doc['name'] == row['bus']), None)
        if bus_doc:
            # Add the generator data to the bus document
            bus_doc.setdefault('generators', []).append({
                'id': ObjectId(),
                'name': row['name'],
                'p_mw': float(row['p_mw']),
                'vm_pu': float(row['vm_pu']),
                'sn_mva': float(row['sn_mva']),
                'min_q_mvar': float(row['min_q_mvar']),
                'max_q_mvar': float(row['max_q_mvar']),
                'scaling': float(row['scaling']),
                'slack': bool(row['slack']),
                'in_service': bool(row['in_service']),
                'slack_weight': float(row['slack_weight']),
                'type': row['type'],
                'controllable': bool(row['controllable']),
                'max_p_mw': float(row['max_p_mw']),
                'min_p_mw': float(row['min_p_mw'])
            })

# Open and read externalGrid.csv file
with open('networkData/externalGrid.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and add external grid data to bus documents

    for row in reader:
        # Find the bus document that matches the external grid bus
        bus_doc = next((doc for doc in busDocs if doc['name'] == row['bus']), None)
        if bus_doc:
            # Add the external grid data to the bus document
            bus_doc.setdefault('external_grids', []).append({
                'id': ObjectId(),
                'name': row['name'],
                'vm_pu': float(row['vm_pu']),
                'va_degree': float(row['va_degree']),
                'slack_weight': float(row['slack_weight']),
                'in_service': bool(row['in_service']),
                'max_p_mw': float(row['max_p_mw']),
                'min_p_mw': float(row['min_p_mw']),
                'max_q_mvar': float(row['max_q_mvar']),
                'min_q_mvar': float(row['min_q_mvar'])
            })

# Save pickle file
with open('app/models/__prepareToNoSql/networkToBson.pkl', 'wb') as f:
    pkl.dump(busDocs, f)
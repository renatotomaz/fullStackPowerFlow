"""This script prepares the branches
and transformers data to be inserted
into the MongoDB database, saving the
result as a piclke file to be used by
another script. It depends on the
busesIdDict.pkl file generated by
__prepareBusesToMongo.py script."""

import csv
import bson 
from bson import ObjectId
import sys, os
import pickle as pkl
from pymongo.database import DBRef

sys.path.append(os.getcwd())

# Create an empty list to store branch documents
circuitDocs = []

# name;std_type;from_bus;to_bus;length_km;r_ohm_per_km;x_ohm_per_km;c_nf_per_km;g_us_per_km;max_i_ka;df;parallel;type;in_service;max_loading_percent

with open('app/models/__prepareToNoSql/busesIdDict.pkl', 'rb') as f:
    busesIdDict = pkl.load(f)

with open('networkData/branch.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and create branch documents
    for row in reader:
        refFrom = DBRef('buses', busesIdDict[str(int(row['from_bus'])+1)])
        refTo = DBRef('buses', busesIdDict[str(int(row['to_bus'])+1)])
        doc = {}
        doc['_id'] = ObjectId()
        doc['name'] = row['name']
        doc['circuit_type'] = 'TL'
        doc['std_type'] = row['std_type']
        doc['from_bus'] = {
            '_id': refFrom,
            'name': row['from_bus'],
            'in_service': bool(row['in_service']),
        }
        doc['to_bus'] = {
            '_id': refTo,
            'name': row['to_bus'],
            'in_service': bool(row['in_service']),
        }
        doc['length_km'] = float(row['length_km'])
        doc['r_ohm_per_km'] = float(row['r_ohm_per_km'])
        doc['x_ohm_per_km'] = float(row['x_ohm_per_km'])
        doc['c_nf_per_km'] = float(row['c_nf_per_km'])
        doc['g_us_per_km'] = float(row['g_us_per_km'])
        doc['max_i_ka'] = float(row['max_i_ka'])
        doc['df'] = float(row['df'])
        doc['parallel'] = int(row['parallel'])
        doc['type'] = row['type']
        doc['in_service'] = bool(row['in_service'])
        doc['max_loading_percent'] = float(row['max_loading_percent'])
        # Add the branch document to the list
        circuitDocs.append(doc)



# Open and read transformer.csv file
with open('networkData/transformer.csv', 'r') as csvfile:  
    reader = csv.DictReader(csvfile, delimiter=';')
    # Iterate over the rows and create transformer documents
    for row in reader:
        refHv = DBRef('buses', busesIdDict[str(int(row['hv_bus'])+1)])
        refLv = DBRef('buses', busesIdDict[str(int(row['lv_bus'])+1)])
        doc = {}
        doc['_id'] = ObjectId()
        doc['name'] = row['name']
        doc['circuit_type'] = 'Trafo'
        doc['std_type'] = row['std_type']
        doc['hv_bus'] = {
            '_id': refHv,
            'name': row['hv_bus'],
            'in_service': bool(row['in_service']),
        }
        doc['lv_bus'] = {
            '_id': refLv,
            'name': row['lv_bus'],
            'in_service': bool(row['in_service']),
        }
        doc['sn_mva'] = float(row['sn_mva'])
        doc['vn_hv_kv'] = float(row['vn_hv_kv'])
        doc['vn_lv_kv'] = float(row['vn_lv_kv'])
        doc['vk_percent'] = float(row['vk_percent'])
        doc['vkr_percent'] = float(row['vkr_percent'])
        doc['pfe_kw'] = float(row['pfe_kw'])
        doc['i0_percent'] = float(row['i0_percent'])
        doc['shift_degree'] = float(row['shift_degree'])
        doc['tap_side'] = row['tap_side']
        doc['tap_neutral'] = float(row['tap_neutral'])
        doc['tap_min'] = float(row['tap_min'])
        doc['tap_max'] = float(row['tap_max'])
        doc['tap_step_percent'] = float(row['tap_step_percent'])
        doc['tap_step_degree'] = float(row['tap_step_degree'])
        doc['tap_pos'] = float(row['tap_pos'])
        doc['tap_phase_shifter'] = bool(row['tap_phase_shifter'])
        doc['parallel'] = int(row['parallel'])
        doc['df'] = float(row['df'])
        doc['in_service'] = bool(row['in_service'])
        doc['max_loading_percent'] = float(row['max_loading_percent'])
        # Add the transformer document to the list
        circuitDocs.append(doc)

with open('app/models/__prepareToNoSql/circuitsToBson.pkl', 'wb') as f:
    pkl.dump(circuitDocs, f)
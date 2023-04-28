import os
from pandapower.plotting.plotly import simple_plotly

import Network

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NETWORK_DATA_FOLDER = os.path.join(PROJECT_ROOT, 'networkData')


net = Network.Network(os.path.join(NETWORK_DATA_FOLDER, 'bus.csv'),
                        os.path.join(NETWORK_DATA_FOLDER, 'branch.csv'),
                        os.path.join(NETWORK_DATA_FOLDER, 'generator.csv'),
                        os.path.join(NETWORK_DATA_FOLDER, 'load.csv'),
                        os.path.join(NETWORK_DATA_FOLDER, 'transformer.csv'),
                        os.path.join(NETWORK_DATA_FOLDER, 'externalGrid.csv')) 
    

completeNet = net.getNetwork()

simple_plotly(completeNet, use_line_geodata=None)
import sys, os
import unittest

sys.path.append(os.getcwd())

from app.models.Network import Network
class TestNetworkCreation(unittest.TestCase):

    def setUp(self):
        self.network = Network('tests/benchmarkFiles/bus.csv',
                               'tests/benchmarkFiles/branch.csv', 
                               'tests/benchmarkFiles/generator.csv', 
                               'tests/benchmarkFiles/load.csv', 
                               'tests/benchmarkFiles/transformer.csv', 
                               'tests/benchmarkFiles/externalGrid.csv')
        # Arrange
        self.network.createBuses()
        
    def testBusCreation(self):
        # Act
        buses = self.network.getBuses()
        
        # Assert
        self.assertEqual(len(buses), 39)

    def testBusInfo(self):
        # Act
        buses = self.network.getBuses()
        tgtBus = buses.iloc[7]
        
        # Assert
        self.assertEqual(tgtBus['name'], 8)
        self.assertEqual(tgtBus['vn_kv'], 345.0)
        self.assertEqual(tgtBus['type'], 'b')
        self.assertEqual(tgtBus['zone'], 1.0)
        self.assertEqual(tgtBus['in_service'], True)
        self.assertEqual(tgtBus['max_vm_pu'], 1.06)
        self.assertEqual(tgtBus['min_vm_pu'], 0.94)

    def testBranchCreation(self):
        # Arrange
        self.network.createBranches()

        # Act
        branches = self.network.getBranches()
        
        # Assert
        self.assertEqual(len(branches), 35)

    def testBranchInfo(self):
        # Arrange
        self.network.createBranches()

        # Act
        branches = self.network.getBranches()
        tgtBranch = branches.iloc[34]
        
        # Assert
        self.assertEqual(tgtBranch['name'], "'From_27_To_28'")
        self.assertEqual(tgtBranch['from_bus'], 27)
        self.assertEqual(tgtBranch['to_bus'], 28)
        self.assertEqual(tgtBranch['length_km'], 1.0)
        self.assertEqual(tgtBranch['r_ohm_per_km'], 1.666350)
        self.assertEqual(tgtBranch['x_ohm_per_km'], 17.972775)
        self.assertEqual(tgtBranch['c_nf_per_km'], 554.919566)
        self.assertEqual(tgtBranch['g_us_per_km'], 0.0)
        self.assertEqual(tgtBranch['max_i_ka'],  1.004087)
        self.assertEqual(tgtBranch['df'], 1.0)
        self.assertEqual(tgtBranch['parallel'], 1)
        self.assertEqual(tgtBranch['type'], 'ol')
        self.assertEqual(tgtBranch['in_service'], True)
        self.assertEqual(tgtBranch['max_loading_percent'], 100.0)


if __name__ == '__main__':
    unittest.main()

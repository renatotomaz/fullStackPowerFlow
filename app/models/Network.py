import pandas as pd
import pandapower as pp
import os

class Network:
    def __init__(self, busFile, branchFile, generatorFile, loadFile, transformerFile, extGridFile):
        self.net = pp.create_empty_network()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.busData = pd.read_csv(busFile, sep=';')
        self.branchData = pd.read_csv(branchFile, sep=';')
        self.generatorData = pd.read_csv(generatorFile, sep=';')
        self.loadData = pd.read_csv(loadFile, sep=';')
        self.transformerData = pd.read_csv(transformerFile, sep=';')
        self.extGridData = pd.read_csv(extGridFile, sep=';')
        self.__completeNetwork = False

    def createBuses(self):
        for _, row in self.busData.iterrows():
            pp.create_bus(self.net, 
                          name=row['name'], 
                          vn_kv=row['vn_kv'], 
                          type=row['type'], 
                          zone=row['zone'], 
                          in_service=row['in_service'], 
                          max_vm_pu=row['max_vm_pu'], 
                          min_vm_pu=row['min_vm_pu'],
                          geodata=(row['x_pos'], row['y_pos']))

    def createBranches(self): 
        for _, row in self.branchData.iterrows():
            pp.create_line_from_parameters(self.net, 
                                            name=row["name"], 
                                            from_bus=row["from_bus"], 
                                            to_bus=row["to_bus"], 
                                            length_km=row["length_km"], 
                                            r_ohm_per_km=row["r_ohm_per_km"], 
                                            x_ohm_per_km=row["x_ohm_per_km"], 
                                            c_nf_per_km=row["c_nf_per_km"], 
                                            g_us_per_km=row["g_us_per_km"], 
                                            max_i_ka=row["max_i_ka"], 
                                            df=row["df"], 
                                            parallel=row["parallel"], 
                                            type=row["type"], 
                                            in_service=row["in_service"], 
                                            max_loading_percent=row["max_loading_percent"])
            
    def createGenerators(self):
        for _, row in self.generatorData.iterrows():
            pp.create_sgen(self.net, 
                            name=row["name"],
                            bus=row["bus"],
                            p_mw=row["p_mw"],
                            vm_pu=row["vm_pu"],
                            sn_mva=row["sn_mva"],
                            min_q_mvar=row["min_q_mvar"],
                            max_q_mvar=row["max_q_mvar"],
                            scaling=row["scaling"],
                            slack=row["slack"],
                            in_service=row["in_service"],
                            slack_weight=row["slack_weight"],
                            type=row["type"],
                            controllable=row["controllable"],
                            max_p_mw=row["max_p_mw"],
                            min_p_mw=row["min_p_mw"])



    def createLoads(self): 
        for _, row in self.loadData.iterrows():
            pp.create_load(self.net, 
                            name=row["name"],
                            bus=row["bus"],
                            p_mw=row["p_mw"],
                            q_mvar=row["q_mvar"],
                            const_z_percent=row["const_z_percent"],
                            const_i_percent=row["const_i_percent"],
                            sn_mva=row["sn_mva"],
                            scaling=row["scaling"],
                            in_service=row["in_service"],
                            type=row["type"],
                            controllable=row["controllable"])
                  

    def createTransformers(self):
        for _, row in self.transformerData.iterrows():
            pp.create_transformer_from_parameters(self.net,
                                                  std_type=row["std_type"],
                                                    hv_bus=row["hv_bus"],
                                                    lv_bus=row["lv_bus"],
                                                    sn_mva=row["sn_mva"],
                                                    vn_hv_kv=row["vn_hv_kv"],
                                                    vn_lv_kv=row["vn_lv_kv"],
                                                    vk_percent=row["vk_percent"],
                                                    vkr_percent=row["vkr_percent"],
                                                    pfe_kw=row["pfe_kw"],
                                                    i0_percent=row["i0_percent"],
                                                    shift_degree=row["shift_degree"],
                                                    tap_side=row["tap_side"],
                                                    tap_neutral=row["tap_neutral"],
                                                    tap_min=row["tap_min"],
                                                    tap_max=row["tap_max"],
                                                    tap_step_percent=row["tap_step_percent"],
                                                    tap_step_degree=row["tap_step_degree"],
                                                    tap_pos=row["tap_pos"],
                                                    tap_phase_shifter=row["tap_phase_shifter"],
                                                    parallel=row["parallel"],
                                                    df=row["df"],
                                                    in_service=row["in_service"],
                                                    max_loading_percent=row["max_loading_percent"])
                 

    def createExtGrids(self): 
        for _, row in self.extGridData.iterrows():
            pp.create_ext_grid(self.net,
                               name=row["name"],
                                bus=row["bus"],
                                vm_pu=row["vm_pu"],
                                va_degree=row["va_degree"], 
                                slack_weight=row["slack_weight"],
                                in_service=row["in_service"],
                                max_p_mw=row["max_p_mw"],
                                min_p_mw=row["min_p_mw"],
                                max_q_mvar=row["max_q_mvar"],
                                min_q_mvar=row["min_q_mvar"])

    def createNetwork(self):
        self.createBuses()
        self.createBranches()
        self.createGenerators()
        self.createLoads()
        self.createTransformers()
        self.createExtGrids()
        self.__completeNetwork = True

    def getNetwork(self):
        if not self.__completeNetwork:
            self.createNetwork()
            self.__completeNetwork = True
        return self.net
    
    def getBuses(self):
        return self.busData
    
    def getBranches(self):
        return self.branchData
    
    def getGenerators(self):
        return self.generatorData
    
    def getLoads(self):
        return self.loadData
    
    def getTransformers(self):
        return self.transformerData
    
    def getExtGrids(self):
        return self.extGridData
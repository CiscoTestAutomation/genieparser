expected_output = {
        "power_stack": {
            "Powerstack-1": {
                "mode": "SP-PS",
                "topology": "Stndaln",
                "total_power": 1100,
                "reserved_power": 0,
                "allocated_power": 243,
                "available_power": 857,
                "switch_num": 1,
                "power_supply_num": 1,
                'power_stack_detail': {
                    "stack_mode": "Power sharing",
                    "stack_topology": "Standalone",
                    "switch": {
                        1: {
                            "power_budget": 1100,
                            "power_allocated": 243,
                            "low_port_priority_value": 22,
                            "high_port_priority_value": 13,
                            "switch_priority_value": 4,
                            "port_1_status": "Not connected",
                            "port_2_status": "Not connected",
                            "neighbor_on_port_1": "0000.0000.0000",
                            "neighbor_on_port_2": "0000.0000.0000"
                        }
                    }              
                }  
            },
            "Powerstack-2": {
                "mode": "SP-PS",
                "topology": "Stndaln",
                "total_power": 1100,
                "reserved_power": 0,
                "allocated_power": 510,
                "available_power": 590,
                "switch_num": 1,
                "power_supply_num": 1,
                "power_stack_detail":{
                    "stack_mode": "Power sharing",
                    "stack_topology": "Standalone",
                    "switch": {
                        2 : {
                            "power_budget": 1100,
                            "power_allocated": 510,
                            "low_port_priority_value": 22,
                            "high_port_priority_value": 13,
                            "switch_priority_value": 4,
                            "port_1_status": "Not connected",
                            "port_2_status": "Not connected",
                            "neighbor_on_port_1": "0000.0000.0000",
                            "neighbor_on_port_2": "0000.0000.0000"
                        }
                    }
                }           
            },
            "Powerstack-3": {
                "mode": "SP-PS",
                "topology": "Stndaln",
                "total_power": 1100,
                "reserved_power": 0,
                "allocated_power": 510,
                "available_power": 590,
                "switch_num": 1,
                "power_supply_num": 1,
                "power_stack_detail":{
                    "stack_mode": "Power sharing",
                    "stack_topology": "Standalone",
                    "switch": {
                        3 : {
                            "power_budget": 1100,
                            "power_allocated": 510,
                            "low_port_priority_value": 22,
                            "high_port_priority_value": 13,
                            "switch_priority_value": 4,
                            "port_1_status": "Not connected",
                            "port_2_status": "Not connected",
                            "neighbor_on_port_1": "0000.0000.0000",
                            "neighbor_on_port_2": "0000.0000.0000"
                        }
                    }     
                }    
            }
        }   
    }
expected_output = {
    "interfaces": {
        "Bundle-Ether13": {
            "name": "Bundle-Ether13",
            "bundle_id": 13,
            "iccp_group": 13,
            "port": {
                "TenGigabitEthernet0/1/0/6": {
                    "interface": "TenGigabitEthernet0/1/0/6",
                    "bundle_id": 13,
                    "rate": 30,
                    "state": "ascdAF--",
                    "port_id": "0x8002,0xa001",
                    "key": "0x000d",
                    "system_id": "0x0001,40-55-39-63-6c-e5",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 1,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0003",
                        "key": "0x000d",
                        "system_id": "0x8000,19-23-19-23-19-23",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True
                    },
                    "receive": "Current",
                    "period": "Slow",
                    "selection": "Selected",
                    "mux": "Distrib",
                    "a_churn": "None",
                    "p_churn": "None"
                },
                "TenGigabitEthernet0/1/0/8": {
                    "interface": "TenGigabitEthernet0/1/0/8",
                    "bundle_id": 13,
                    "state": "a---AF--",
                    "port_id": "0x8003,0x9001",
                    "key": "0x000d",
                    "system_id": "0x0001,40-55-39-63-6c-e5",
                    "aggregatable": True,
                    "synchronization": "out_sync",
                    "collecting": False,
                    "distributing": False,
                    "partner": {
                        "state": "as--A---",
                        "port_id": "0x8000,0x0002",
                        "key": "0x000d",
                        "system_id": "0x8000,19-23-19-23-19-23",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": False,
                        "distributing": False
                    },
                    "receive": "Current",
                    "period": "Slow",
                    "selection": "Standby",
                    "mux": "Waiting",
                    "a_churn": "Churn",
                    "p_churn": "None"
                }
            },
            "lacp_mode": "active"
        },
        "Bundle-Ether15": {
            "name": "Bundle-Ether15",
            "bundle_id": 15,
            "port": {
                "TenGigabitEthernet0/1/0/10": {
                    "interface": "TenGigabitEthernet0/1/0/10",
                    "bundle_id": 15,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x8000,0x0004",
                    "key": "0x000f",
                    "system_id": "0x8000,10-f3-11-02-f8-3e",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0002",
                        "key": "0x000f",
                        "system_id": "0x8000,a8-0c-0d-3a-ae-55",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True
                    },
                    "receive": "Current",
                    "period": "Slow",
                    "selection": "Selected",
                    "mux": "Distrib",
                    "a_churn": "None",
                    "p_churn": "None"
                }
            },
            "lacp_mode": "active"
        },
        "Bundle-Ether20": {
            "name": "Bundle-Ether20",
            "bundle_id": 20,
            "port": {
                "TenGigabitEthernet0/1/0/0": {
                    "interface": "TenGigabitEthernet0/1/0/0",
                    "bundle_id": 20,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x8000,0x0003",
                    "key": "0x0014",
                    "system_id": "0x8000,10-f3-11-02-f8-3e",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0001",
                        "key": "0x0014",
                        "system_id": "0x8000,00-c1-64-61-f9-61",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True
                    },
                    "receive": "Current",
                    "period": "Slow",
                    "selection": "Selected",
                    "mux": "Distrib",
                    "a_churn": "None",
                    "p_churn": "None"
                }
            },
            "lacp_mode": "active"
        },
        "Bundle-Ether1905": {
            "name": "Bundle-Ether1905",
            "bundle_id": 1905,
            "port": {
                "TenGigabitEthernet0/1/0/18": {
                    "interface": "TenGigabitEthernet0/1/0/18",
                    "bundle_id": 1905,
                    "rate": 1,
                    "state": "a---A-D-",
                    "port_id": "0x8000,0x0002",
                    "key": "0x0771",
                    "system_id": "0x8000,10-f3-11-02-f8-3e",
                    "aggregatable": True,
                    "synchronization": "out_sync",
                    "collecting": False,
                    "distributing": False,
                    "partner": {
                        "rate": 30,
                        "state": "-----FD-",
                        "port_id": "0x0000,0x0000",
                        "key": "0x0000",
                        "system_id": "0x0000,00-00-00-00-00-00",
                        "aggregatable": False,
                        "synchronization": "out_sync",
                        "collecting": False,
                        "distributing": False
                    },
                    "receive": "Disabled",
                    "period": "None",
                    "selection": "Unselect",
                    "mux": "Detached",
                    "a_churn": "Monitor",
                    "p_churn": "Monitor"
                },
                "TenGigabitEthernet0/1/0/19": {
                    "interface": "TenGigabitEthernet0/1/0/19",
                    "bundle_id": 1905,
                    "rate": 1,
                    "state": "a---A-D-",
                    "port_id": "0x8000,0x0001",
                    "key": "0x0771",
                    "system_id": "0x8000,10-f3-11-02-f8-3e",
                    "aggregatable": True,
                    "synchronization": "out_sync",
                    "collecting": False,
                    "distributing": False,
                    "partner": {
                        "rate": 30,
                        "state": "-----FD-",
                        "port_id": "0x0000,0x0000",
                        "key": "0x0000",
                        "system_id": "0x0000,00-00-00-00-00-00",
                        "aggregatable": False,
                        "synchronization": "out_sync",
                        "collecting": False,
                        "distributing": False
                    },
                    "receive": "Disabled",
                    "period": "None",
                    "selection": "Unselect",
                    "mux": "Detached",
                    "a_churn": "Monitor",
                    "p_churn": "Monitor"
                }
            },
            "lacp_mode": "active"
        }
    }
}

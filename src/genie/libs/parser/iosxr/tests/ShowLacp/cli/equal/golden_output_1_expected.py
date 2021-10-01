

expected_output = {
    "interfaces": {
        "Bundle-Ether1": {
            "name": "Bundle-Ether1",
            "bundle_id": 1,
            "lacp_mode": "active",
            "port": {
                "GigabitEthernet0/0/0/0": {
                    "interface": "GigabitEthernet0/0/0/0",
                    "bundle_id": 1,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x000a,0x0001",
                    "key": "0x0001",
                    "system_id": "0x0064,00-1b-0c-ff-6a-36",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x000a,0x0001",
                        "key": "0x0001",
                        "system_id": "0x8000,00-0c-86-ff-c6-81",
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
                "GigabitEthernet0/0/0/1": {
                    "interface": "GigabitEthernet0/0/0/1",
                    "bundle_id": 1,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x8000,0x0002",
                    "key": "0x0001",
                    "system_id": "0x0064,00-1b-0c-ff-6a-36",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0005",
                        "key": "0x0001",
                        "system_id": "0x8000,00-0c-86-ff-c6-81",
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
            }
        },
        "Bundle-Ether2": {
            "name": "Bundle-Ether2",
            "bundle_id": 2,
            "lacp_mode": "active",
            "port": {
                "GigabitEthernet0/0/0/2": {
                    "interface": "GigabitEthernet0/0/0/2",
                    "bundle_id": 2,
                    "rate": 30,
                    "state": "a---A---",
                    "port_id": "0x8000,0x0005",
                    "key": "0x0002",
                    "system_id": "0x0064,00-1b-0c-ff-6a-36",
                    "aggregatable": True,
                    "synchronization": "out_sync",
                    "collecting": False,
                    "distributing": False,
                    "partner": {
                        "rate": 30,
                        "state": "as--A---",
                        "port_id": "0x8000,0x0004",
                        "key": "0x0002",
                        "system_id": "0x8000,00-0c-86-ff-c6-81",
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
                },
                "GigabitEthernet0/0/0/3": {
                    "interface": "GigabitEthernet0/0/0/3",
                    "bundle_id": 2,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x8000,0x0004",
                    "key": "0x0002",
                    "system_id": "0x0064,00-1b-0c-ff-6a-36",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0003",
                        "key": "0x0002",
                        "system_id": "0x8000,00-0c-86-ff-c6-81",
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
                "GigabitEthernet0/0/0/4": {
                    "interface": "GigabitEthernet0/0/0/4",
                    "bundle_id": 2,
                    "rate": 30,
                    "state": "ascdA---",
                    "port_id": "0x8000,0x0003",
                    "key": "0x0002",
                    "system_id": "0x0064,00-1b-0c-ff-6a-36",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0002",
                        "key": "0x0002",
                        "system_id": "0x8000,00-0c-86-ff-c6-81",
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
            }
        }
    }
}

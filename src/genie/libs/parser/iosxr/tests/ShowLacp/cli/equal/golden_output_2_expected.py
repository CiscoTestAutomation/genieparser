

expected_output =  {
    "interfaces": {
        "Bundle-Ether8": {
            "name": "Bundle-Ether8",
            "bundle_id": 8,
            "lacp_mode": "active",
            "port": {
                "TenGigabitEthernet0/0/0/0": {
                    "interface": "TenGigabitEthernet0/0/0/0",
                    "bundle_id": 8,
                    "rate": 1,
                    "state": "ascdAF--",
                    "port_id": "0x8000,0x0002",
                    "key": "0x0008",
                    "system_id": "0x8000,40-55-39-ff-6c-0f",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 1,
                        "state": "ascdAF--",
                        "port_id": "0x0001,0x0006",
                        "key": "0x0008",
                        "system_id": "0x0001,cc-ef-48-ff-23-0a",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True
                    },
                    "receive": "Current",
                    "period": "Fast",
                    "selection": "Selected",
                    "mux": "Distrib",
                    "a_churn": "None",
                    "p_churn": "None"
                },
                "TenGigabitEthernet0/1/0/0": {
                    "interface": "TenGigabitEthernet0/1/0/0",
                    "bundle_id": 8,
                    "rate": 1,
                    "state": "ascdAF--",
                    "port_id": "0x8000,0x0001",
                    "key": "0x0008",
                    "system_id": "0x8000,40-55-39-ff-6c-0f",
                    "aggregatable": True,
                    "synchronization": "in_sync",
                    "collecting": True,
                    "distributing": True,
                    "partner": {
                        "rate": 1,
                        "state": "ascdAF--",
                        "port_id": "0x8000,0x0004",
                        "key": "0x0008",
                        "system_id": "0x0001,cc-ef-48-ff-23-0a",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True
                    },
                    "receive": "Current",
                    "period": "Fast",
                    "selection": "Selected",
                    "mux": "Distrib",
                    "a_churn": "None",
                    "p_churn": "None"
                },
            },
        },
    },
}

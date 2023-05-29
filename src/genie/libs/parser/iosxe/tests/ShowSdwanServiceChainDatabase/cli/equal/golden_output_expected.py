expected_output = {
    "service_chain_db": {
            'SC1': {
                "vrf": 101,
                "label": "0x80041B",
                "state": "Up",
                "services": {
                    "IDS": {
                        "service_state": "Up",
                        "sequence": 1,
                        '1':{
                            'Active':{
                                'tx':{
                                    'interface': "GigabitEthernet3",
                                    'ip': "192.168.40.42",
                                    'status': "Down"
                                },
                                'rx':{
                                    'interface': "GigabitEthernet3",
                                    'ip': "192.168.40.42",
                                    'status': "Down"
                                }
                            }
                        },
                        '2':{
                            'Active':{
                                'tx':{
                                    'interface': "GigabitEthernet4",
                                    'ip': "192.168.140.42",
                                    'status': "Up"
                                },
                                'rx':{
                                    'interface': "GigabitEthernet4",
                                    'ip': "192.168.140.42",
                                    'status': "Up"
                                }
                            }
                        },

                    }

                }

            }

        }
}

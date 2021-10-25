expected_output = {
    "interface": {
        "Tunnel0": {
            "profile": "polaris-test",
             "session_status": "UP-ACTIVE",
             "peer": {
                 "1.1.1.1": {
                     "port": {
                         "500": {
                             "ike_sa": {
                                 "1": {
                                     "local": "2.2.2.2",
                                     "local_port": "500",
                                     "remote": "1.1.1.1",
                                     "remote_port": "500",
                                     "sa_status": "Active",
                                     "version": "IKEv2",
                                     "session_id": "3"
                                }
                            },
                            "ipsec_flow": {
                                "permit 47 host 2.2.2.2 host 1.1.1.1": {
                                    "active_sas": 2,
                                    "origin": "crypto map"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


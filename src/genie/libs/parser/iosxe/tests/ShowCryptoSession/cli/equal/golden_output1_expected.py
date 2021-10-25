expected_output= {
    "interface": {
        "Virtual-Access2": {
            "user_name": "cisco",
            "profile": "prof",
            "group": "easy",
            "assigned_address": "10.3.3.4",
            "session_status": "UP-ACTIVE",
            "peer": {
                "10.1.1.2": {
                    "port": {
                        "500": {
                            "ike_sa": {
                                "1": {
                                    "local": "10.1.1.1",
                                    "local_port": "500",
                                    "remote": "10.1.1.2",
                                    "remote_port": "500",
                                    "sa_status": "Active",
                                    "version": "IKE"
                                },
                                "2": {
                                    "local": "10.1.1.1",
                                    "local_port": "500",
                                    "remote": "10.1.1.2",
                                    "remote_port": "500",
                                    "sa_status": "Inactive",
                                    "version": "IKE"
                                }
                            },
                            "ipsec_flow": {
                                "permit ip 0.0.0.0/0.0.0.0 host 3.3.3.4": {
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
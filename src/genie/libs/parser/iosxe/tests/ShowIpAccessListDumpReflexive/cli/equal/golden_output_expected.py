expected_output = {
    "source":{
        "80.0.1.83":{
            "name":{
                "R11":{
                    "acl_type":{
                        "REFLECT":{
                            "direction":{
                                "IN ":{
                                    "sport_dport":"3083/4083",
                                    "threshold_count":0,
                                    "active":"Y",
                                    "interface_num":"181 (Vlan3110)"
                                }
                            }
                        }
                    }
                }
            },
            "reflex_error":0,
            "evaluate_error":0,
			"protocol":"udp",
			"timeleft":107
        },
        "80.0.1.19":{
            "name":{
                "R11":{
                    "acl_type":{
                        "REFLECT":{
                            "direction":{
                                "IN ":{
                                    "sport_dport":"3019/4019",
                                    "threshold_count":0,
                                    "active":"Y",
                                    "interface_num":"181 (Vlan3110)"
                                }
                            }
                        }
                    }
                }
            },
            "reflex_error":0,
            "evaluate_error":0,
			"protocol":"udp",
			"timeleft":103
        }
    }
}
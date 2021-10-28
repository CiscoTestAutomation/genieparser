expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                4099: {
                    "address_family": "IPv4",
                    "eid_table": "red",
                    "state": "Established",
                    "epoch": 0,
                    "entries": 2,
                    "eid_prefix": {
                        "0.0.0.0/0": {
                            "eid_epoch": 0,
                            "last_pub_time": "5d22h",
                            "ttl": "never",
                            "eid_state": "unknown-eid-forward",
                            "rloc_set": {
                                "203.203.203.203": {
                                    "priority": 255,
                                    "weight": 10,
                                    "rloc_state": "up",
                                    "encap_iid": "-",
                                }
                            },
                        },
                        "121.121.121.0/30": {
                            "eid_epoch": 0,
                            "last_pub_time": "5d22h",
                            "ttl": "1d00h",
                            "eid_state": "complete",
                            "rloc_set": {
                                "203.203.203.203": {
                                    "priority": 10,
                                    "weight": 10,
                                    "rloc_state": "up",
                                    "encap_iid": "-",
                                }
                            },
                        },
                    },
                }
            }
        }
    }
}

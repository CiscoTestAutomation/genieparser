expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                101: {
                    "address_family": "IPv4",
                    "eid_table": "vrf red",
                    "lsb": "0x0",
                    "all_no_route": False,
                    "entries_total": 2,
                    "no_route_entries": 2,
                    "inactive_entries": 0,
                    "do_not_register_entries": 0,
                    "eid_prefix": "192.168.1.0/24",
                    "eid_info": "locator-set RLOC *** NO ROUTE TO EID PREFIX ***",
                    "domain_id": "unset",
                    "srvc_ins_type": "N/A",
                    "srvc_ins_id": 0,
                    "locators": {
                        "100.31.31.31": {
                            "priority": 1,
                            "weight": 1,
                            "source": "cfg-addr",
                            "state": "site-self, reachable",
                            "config_missing": False,
                        },
                        "100.23.23.23": {
                            "priority": 1,
                            "weight": 1,
                            "source": "cfg-addr",
                            "state": "site-other, unknown",
                            "config_missing": False,
                        },
                        "100.44.44.44": {"config_missing": True},
                    },
                    "map_servers": {
                        "100.31.31.31": {
                            "uptime": "10:00:06",
                            "ack": "No",
                            "domain_id": "0",
                        },
                        "100.32.32.32": {
                            "uptime": "10:00:06",
                            "ack": "No",
                            "domain_id": "0",
                        },
                    },
                },
                103: {
                    "address_family": "IPv6",
                    "eid_table": "vrf green",
                    "lsb": "0x0",
                    "all_no_route": True,
                    "entries_total": 3,
                    "no_route_entries": 3,
                    "inactive_entries": 3,
                    "do_not_register_entries": 3,
                    "eid_prefix": "::/0",
                    "eid_info": "locator-set RLOC *** NO ROUTE TO EID PREFIX ***",
                    "domain_id": "101",
                    "srvc_ins_type": "firewall",
                    "srvc_ins_id": 1,
                    "locators": {
                        "E80::AEDE:48FF:FE00:1111": {"config_missing": True},
                        "E80::AEDE:48FF:FE00:1112": {
                            "priority": 10,
                            "weight": 10,
                            "source": "cfg-addr",
                            "state": "no-route",
                            "config_missing": False,
                        },
                    },
                    "map_servers": {
                        "100.31.31.31": {
                            "uptime": "never",
                            "ack": "Yes",
                            "domain_id": "101",
                        },
                        "100.32.32.32": {
                            "uptime": "never",
                            "ack": "No",
                            "domain_id": "0",
                        },
                    },
                },
            }
        },
        1: {
            "instance_id": {
                104: {
                    "address_family": "MAC",
                    "eid_table": "Vlan 101",
                    "lsb": "0x0",
                    "all_no_route": True,
                    "entries_total": 1,
                    "no_route_entries": 1,
                    "inactive_entries": 0,
                    "do_not_register_entries": 0,
                    "eid_prefix": "0000.0000.0000/0",
                    "eid_info": "locator-set RLOC3 *** NO ROUTE TO EID PREFIX ***",
                    "domain_id": "unset",
                    "srvc_ins_type": "N/A",
                    "srvc_ins_id": 0,
                    "locators": {
                        "100.44.44.44": {
                            "priority": 1,
                            "weight": 1,
                            "source": "cfg-addr",
                            "state": "no-route",
                            "config_missing": False,
                        }
                    },
                    "map_servers": {
                        "100.31.31.31": {
                            "uptime": "never",
                            "ack": "No",
                            "domain_id": "0",
                        }
                    },
                }
            }
        },
    }
}

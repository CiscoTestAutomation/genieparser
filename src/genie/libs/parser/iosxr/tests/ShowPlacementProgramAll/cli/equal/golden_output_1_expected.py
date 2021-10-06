

expected_output = {
    "program": {
        "rcp_fs": {
            "instance": {
                "default": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "central-services",
                    "jid": "1168",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
        "ospf": {
            "instance": {
                "1": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1018",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
        "bgp": {
            "instance": {
                "default": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "v4-routing",
                    "jid": "1018",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
        "statsd_manager_g": {
            "instance": {
                "default": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "netmgmt",
                    "jid": "1141",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
        "pim": {
            "instance": {
                "default": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "mcast-routing",
                    "jid": "1158",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
        "ipv6_local": {
            "instance": {
                "default": {
                    "active": "0/0/CPU0",
                    "active_state": "RUNNING",
                    "group": "v6-routing",
                    "jid": "1156",
                    "standby": "NONE",
                    "standby_state": "NOT_SPAWNED",
                }
            }
        },
    }
}

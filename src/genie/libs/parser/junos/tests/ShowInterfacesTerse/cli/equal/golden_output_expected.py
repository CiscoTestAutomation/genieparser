expected_output = {
    "em1": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "em1.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {
            "inet": {
                "10.0.0.4/8": {"local": "10.0.0.4/8"},
                "172.16.64.1/2": {"local": "172.16.64.1/2"},
                "172.16.64.4/2": {"local": "172.16.64.4/2"},
            },
            "inet6": {
                "fe80::250:56ff:fe82:ba52/64": {"local": "fe80::250:56ff:fe82:ba52/64"},
                "2001:db8:8d82:0:a::4/64": {"local": "2001:db8:8d82:0:a::4/64"},
            },
            "tnp": {"0x4": {"local": "0x4"}},
        },
    },
    "fxp0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "fxp0.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {"172.25.192.114/24": {"local": "172.25.192.114/24"}}},
    },
    "ge-0/0/0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "ge-0/0/0.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {
            "inet": {"10.0.1.1/24": {"local": "10.0.1.1/24"}},
            "multiservice": {},
        },
    },
    "ge-0/0/1": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "ge-0/0/1.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {
            "inet": {"10.0.2.1/24": {"local": "10.0.2.1/24"}},
            "multiservice": {},
        },
    },
    "ge-0/0/2": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "down",
        "oper_status": "down",
    },
    "lc-0/0/0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "lc-0/0/0.32769": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"vpls": {}},
    },
    "lo0.0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {
            "inet": {
                "10.1.1.1": {"local": "10.1.1.1", "remote": "0/0"},
                "10.11.11.11": {"local": "10.11.11.11", "remote": "0/0"},
            }
        },
    },
    "lo0.16384": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {"127.0.0.1": {"local": "127.0.0.1", "remote": "0/0"}}},
    },
    "lo0.16385": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {}},
    },
    "pfe-0/0/0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "pfe-0/0/0.16383": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {}, "inet6": {}},
    },
    "pfh-0/0/0": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
    },
    "pfh-0/0/0.16383": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {}},
    },
    "pfh-0/0/0.16384": {
        "admin_state": "up",
        "enabled": True,
        "link_state": "up",
        "oper_status": "up",
        "protocol": {"inet": {}},
    },
}

expected_output = {
    "radius": {
        "memlocks": 1,
        "server": {
            "10.106.26.213": {
                "acct_port": 1813,
                "auth_port": 1812,
                "auto_test_enabled": False,
                "keywrap_enabled": False,
                "server_name": "mgmt-rad",
                "transactions": {"acct": 0, "authen": 0, "author": 0},
            },
            "121.0.0.1": {
                "acct_port": 1813,
                "auth_port": 1812,
                "auto_test_enabled": False,
                "keywrap_enabled": False,
                "server_name": "data-rad",
                "transactions": {"acct": 0, "authen": 0, "author": 0},
            },
            "44AA::1": {
                "acct_port": 1813,
                "auth_port": 1812,
                "auto_test_enabled": False,
                "keywrap_enabled": False,
                "server_name": "ipv6-rad",
                "transactions": {"acct": 0, "authen": 0, "author": 0},
            },
        },
        "sg_unconfigured": False,
        "sharecount": 1,
        "type": "standard",
    },
    "radius-1": {
        "memlocks": 1,
        "server": {
            "10.106.26.213": {
                "acct_port": 1813,
                "auth_port": 1812,
                "auto_test_enabled": False,
                "keywrap_enabled": False,
                "server_name": "mgmt-rad",
                "transactions": {"acct": 4, "authen": 0, "author": 0},
            }
        },
        "sg_unconfigured": False,
        "sharecount": 1,
        "type": "standard",
    },
    "radius-2": {
        "memlocks": 1,
        "server": {
            "121.0.0.1": {
                "acct_port": 1813,
                "auth_port": 1812,
                "auto_test_enabled": False,
                "keywrap_enabled": False,
                "server_name": "data-rad",
                "transactions": {"acct": 0, "authen": 0, "author": 0},
            }
        },
        "sg_unconfigured": False,
        "sharecount": 1,
        "type": "standard",
    },
}

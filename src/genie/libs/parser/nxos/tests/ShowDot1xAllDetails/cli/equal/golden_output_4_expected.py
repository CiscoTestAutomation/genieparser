expected_output = {
    "system_auth_control": True,
    "version": 2,
    "interfaces": {
        "Ethernet1/1": {
            "interface": "Ethernet1/1",
            "pae": "authenticator",
            "port_control": "force_auth",
            "host_mode": "single host",
            "re_authentication": False,
            "timeout": {
                "quiet_period": 60,
                "server_timeout": 30,
                "supp_timeout": 30,
                "tx_period": 30,
                "ratelimit_period": 0,
            },
            "re_auth_max": 2,
            "max_req": 2,
            "mac-auth-bypass": False,
            "port_status": "authorized",
        },
        "Ethernet1/2": {
            "interface": "Ethernet1/2",
            "pae": "authenticator",
            "port_control": "auto",
            "host_mode": "single host",
            "re_authentication": True,
            "timeout": {
                "quiet_period": 60,
                "server_timeout": 30,
                "supp_timeout": 30,
                "tx_period": 30,
                "ratelimit_period": 0,
                "re_auth_period": 60,
                "time_to_next_reauth": 17,
            },
            "re_auth_max": 2,
            "max_req": 3,
            "mac-auth-bypass": False,
            "clients": {
                "54:be:ef:ff:e5:e5": {
                    "client": "54:be:ef:ff:e5:e5",
                    "session": {
                        "auth_sm_state": "authenticated",
                        "auth_bend_sm_state": "idle",
                        "auth_by": "remote server",
                        "reauth_action": "reauthenticate",
                    },
                    "auth_method": "eap",
                }
            },
            "port_status": "authorized",
        },
    },
}

expected_output = {
    "interfaces": {
        "FastEthernet7/1": {
            "interface": "FastEthernet7/1",
            "pae": "authenticator",
            "clients": {
                "fa16.3eff.c0c3": {
                    "session": {
                        "000000000000000E00110F79": {
                            "session_id": "000000000000000E00110F79",
                            "auth_bend_sm_state": "idle",
                            "auth_sm_state": "held",
                        }
                    },
                    "eap_method": "md5",
                    "client": "fa16.3eff.c0c3",
                },
                "fa16.3eff.40c7": {
                    "session": {
                        "000000000000000C00108250": {
                            "session_id": "000000000000000C00108250",
                            "auth_bend_sm_state": "idle",
                            "auth_sm_state": "authenticated",
                        }
                    },
                    "eap_method": "md5",
                    "client": "fa16.3eff.40c7",
                },
            },
            "host_mode": "single_host",
            "port_control": "auto",
            "max_reauth_req": 2,
            "re_authentication": False,
            "control_direction": "both",
            "max_req": 2,
            "timeout": {
                "tx_period": 30,
                "quiet_period": 60,
                "auth_period": 3600,
                "ratelimit_period": 0,
                "server_timeout": 30,
                "supp_timeout": 30,
            },
        }
    },
    "system_auth_control": True,
    "version": 3,
}

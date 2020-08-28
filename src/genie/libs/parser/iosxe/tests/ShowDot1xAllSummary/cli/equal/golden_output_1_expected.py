expected_output = {
    "interfaces": {
        "GigabitEthernet0/1": {
            "clients": {
                "fa16.3eff.4f27": {
                    "pae": "authenticator",
                    "status": "unauthorized",
                    "client": "fa16.3eff.4f27",
                },
                "fa16.3eff.0cdf": {
                    "pae": "authenticator",
                    "status": "authorized",
                    "client": "fa16.3eff.0cdf",
                },
                "fa16.3eff.0ce0": {
                    "pae": "supplicant",
                    "status": "authorized",
                    "client": "fa16.3eff.0ce0",
                },
                "fa16.3eff.4f28": {
                    "pae": "supplicant",
                    "status": "unauthorized",
                    "client": "fa16.3eff.4f28",
                },
            },
            "interface": "GigabitEthernet0/1",
        }
    }
}

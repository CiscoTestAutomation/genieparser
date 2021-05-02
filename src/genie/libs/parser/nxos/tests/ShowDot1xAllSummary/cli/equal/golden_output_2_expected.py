expected_output = {
    "interfaces": {
        "Ethernet5": {
            "interface": "Ethernet5",
            "clients": {
                "0e:be:00:4g:e0:00": {
                    "client": "0e:be:00:4g:e0:00",
                    "pae": "SUPP",
                    "status": "UNAUTHORIZED",
                }
            },
        },
        "Ethernet1/1": {
            "interface": "Ethernet1/1",
            "clients": {
                "none": {"client": "none", "pae": "AUTH", "status": "AUTHORIZED"}
            },
        },
    }
}

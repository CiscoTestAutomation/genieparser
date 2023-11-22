expected_output = {
    "snmp_notification_hosts": {
        "10.0.0.1": {
            "udp_port": 162,
            "type": "trap",
            "user": "priv_comm",
            "version": "v3",
            "v3_sec_level": "auth",
        },
        "10.0.0.2": {
            "udp_port": 162,
            "vrf": "VRFA",
            "type": "trap",
            "user": "priv_comm",
            "version": "v3",
            "v3_sec_level": "noauth",
        },
        "10.0.0.3": {
            "udp_port": 162,
            "type": "trap",
            "user": "public",
            "version": "v2c",
        },
        "10.0.0.4": {
            "udp_port": 162,
            "type": "inform",
            "user": "public2",
            "version": "v2c",
        },
        "2001:ab8::1": {
            "udp_port": 162,
            "type": "trap",
            "user": "public3",
            "version": "v3",
            "v3_sec_level": "priv",
        },
        "2001:0:ab00:1234:0:2552:7777:1313": {
            "udp_port": 162,
            "type": "trap",
            "user": "public4",
            "version": "v3",
            "v3_sec_level": "priv",
        },
    }
}

expected_output = {
    "interfaces": {
        "Tunnel1": {
            "type": "Spoke",
            "nhrp_peers": 1,
            "peers": {
                "2001:DB8:1101::222": {
                    "tunnel_addr": "FD00:192::1101",
                    "ipv6_target_network": "FD00:192::1101/128",
                    "ent": 1,
                    "status": "UP",
                    "updn_time": "3d05h",
                    "cache_attrib": "S"
                }
            }
        }
    }
}
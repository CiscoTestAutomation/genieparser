expected_output = {
    "interfaces": {
        "Tunnel1": {
            "type": "Hub",
            "nhrp_peers": 2,
            "peers": {
                "2001:DB8:1201::122": {
                    "tunnel_addr": "FD00:192::1201",
                    "ipv6_target_network": "FD00:192::1201/128",
                    "ent": 1,
                    "status": "UP",
                    "updn_time": "00:02:39",
                    "cache_attrib": "D"
                },
                "2001:DB8:1202::123": {
                    "tunnel_addr": "FD00:192::1202",
                    "ipv6_target_network": "FD00:192::1202/128",
                    "ent": 1,
                    "status": "UP",
                    "updn_time": "00:02:29",
                    "cache_attrib": "D"
                }
            }
        }
    }
}
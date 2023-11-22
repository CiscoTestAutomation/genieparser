expected_output = {
    "dns_parameters": {
        "vrf_id": {
            "0": {
                "dns_lookup": "enabled",
                "domain_name": "pm9001_201_dhcp.intranet",
                "dns_servers": ["10.10.201.132"],
            },
            "65528": {
                "dns_lookup": "enabled",
                "dns_servers": ["10.10.201.144", "10.10.201.2"],
            },
        }
    }
}

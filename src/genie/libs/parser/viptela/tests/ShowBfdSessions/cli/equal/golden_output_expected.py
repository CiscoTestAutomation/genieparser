expected_output = {
    "system_ip": {
        "172.16.241.1": {
            "source_tloc_color": {
                "mpls": {
                    "destination_public_ip": "172.16.171.2",
                    "destination_public_port": "12346",
                    "detect_multiplier": "20",
                    "encapsulation": "ipsec",
                    "remote_tloc_color": "mpls",
                    "site_id": "30001001",
                    "source_ip": "172.16.189.2",
                    "state": "up",
                    "transitions": "0",
                    "tx_interval": "1000",
                    "uptime": "0:01:46:50",
                },
                "private1": {
                    "destination_public_ip": "172.16.171.2",
                    "destination_public_port": "12346",
                    "detect_multiplier": "20",
                    "encapsulation": "ipsec",
                    "remote_tloc_color": "mpls",
                    "site_id": "30001001",
                    "source_ip": "172.16.16.2",
                    "state": "up",
                    "transitions": "0",
                    "tx_interval": "1000",
                    "uptime": "0:01:46:51",
                },
            }
        },
        "172.16.241.2": {
            "source_tloc_color": {
                "mpls": {
                    "destination_public_ip": "172.16.34.2",
                    "destination_public_port": "12346",
                    "detect_multiplier": "20",
                    "encapsulation": "ipsec",
                    "remote_tloc_color": "mpls",
                    "site_id": "30001002",
                    "source_ip": "172.16.189.2",
                    "state": "up",
                    "transitions": "2",
                    "tx_interval": "1000",
                    "uptime": "0:01:41:27",
                },
                "private1": {
                    "destination_public_ip": "172.16.34.2",
                    "destination_public_port": "12346",
                    "detect_multiplier": "20",
                    "encapsulation": "ipsec",
                    "remote_tloc_color": "mpls",
                    "site_id": "30001002",
                    "source_ip": "172.16.16.2",
                    "state": "up",
                    "transitions": "2",
                    "tx_interval": "1000",
                    "uptime": "0:01:41:28",
                },
            }
        },
    }
}

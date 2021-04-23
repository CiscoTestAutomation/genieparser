expected_output = {
    "GigabitEthernet0/0/0/1": {
        "int_status": "up",
        "ipv4": {
            "10.1.5.1/24": {"ip": "10.1.5.1", "prefix_length": "24", "route_tag": 50},
            "10.2.2.2/24": {"ip": "10.2.2.2", "prefix_length": "24", "secondary": True},
            "broadcast_forwarding": "disabled",
            "icmp_redirects": "never sent",
            "icmp_replies": "never " "sent",
            "icmp_unreachables": "always sent",
            "mtu": 1514,
            "mtu_available": 1500,
            "proxy_arp": "disabled",
            "table_id": "0xe0000010",
        },
        "multicast_groups": ["224.0.0.2", "224.0.0.1"],
        "oper_status": "up",
        "vrf": "VRF1",
        "vrf_id": "0x60000001",
    },
}

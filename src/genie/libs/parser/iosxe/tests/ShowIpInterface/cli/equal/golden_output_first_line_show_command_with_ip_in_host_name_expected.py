expected_output = {
    "GigabitEthernet1": {
        "bgp_policy_mapping": False,
        "directed_broadcast_forwarding": False,
        "enabled": False,
        "icmp": {
            "mask_replies": "never sent",
            "redirects": "always sent",
            "unreachables": "always sent",
        },
        "input_features": ["MCI Check"],
        "ip_access_violation_accounting": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_multicast_distributed_fast_switching": False,
        "ip_multicast_fast_switching": True,
        "ip_null_turbo_vector": True,
        "ip_output_packet_accounting": False,
        "ip_route_cache_flags": ["CEF", "Fast"],
        "ipv4": {
            "dhcp_negotiated": {
                "broadcast_address": "255.255.255.255",
                "ip": "dhcp_negotiated",
            }
        },
        "local_proxy_arp": False,
        "mtu": 1500,
        "network_address_translation": False,
        "oper_status": "down",
        "policy_routing": False,
        "probe_proxy_name_replies": False,
        "proxy_arp": True,
        "router_discovery": False,
        "rtp_ip_header_compression": False,
        "security_level": "default",
        "split_horizon": True,
        "tcp_ip_header_compression": False,
        "unicast_routing_topologies": {"topology": {"base": {"status": "down"}}},
        "wccp": {
            "redirect_exclude": False,
            "redirect_inbound": False,
            "redirect_outbound": False,
        },
    }
}

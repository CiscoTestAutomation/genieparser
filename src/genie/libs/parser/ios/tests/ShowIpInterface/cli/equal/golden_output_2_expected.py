expected_output = {
    "Embedded-Service-Engine0/0": {
        "enabled": False,
        "oper_status": "down"
    },
    "GigabitEthernet0/0": {
        "enabled": True,
        "oper_status": "up"
    },
    "GigabitEthernet0/0.100": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.1.10/24": {
                "ip": "10.1.1.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.1",
            "224.0.0.13",
            "224.0.0.2",
            "224.0.0.22",
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.101": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.98.10/24": {
                "ip": "10.1.98.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.300": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.6.100.10/25": {
                "ip": "10.6.100.10",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.308": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.5.101.129/25": {
                "ip": "10.5.101.129",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.324": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.2.100.129/25": {
                "ip": "10.2.100.129",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.160.124.129",
            "10.160.125.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.398": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.8.10.10/25": {
                "ip": "10.8.10.10",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "ISM0/0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.98.10": {
                "ip": "10.1.98.10",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/1": {
        "enabled": True,
        "oper_status": "down"
    },
    "GigabitEthernet0/2": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.205.34.178/29": {
                "ip": "10.205.34.178",
                "prefix_length": "29",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "proxy_arp": False,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "ISM0/1": {
        "enabled": True,
        "oper_status": "up"
    },
    "SM1/0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.99.10/24": {
                "ip": "10.1.99.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": True
        }
    },
    "SM1/1": {
        "enabled": True,
        "oper_status": "up"
    },
    "Async0/1/0": {
        "enabled": True,
        "oper_status": "down"
    },
    "Loopback0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.38.2.9/32": {
                "ip": "10.38.2.9",
                "prefix_length": "32",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "Loopback1": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "172.16.219.118/32": {
                "ip": "172.16.219.118",
                "prefix_length": "32",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "NVI0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "0.0.0.0": {
                "ip": "0.0.0.0",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": False,
        "ip_flow_switching": False,
        "ip_cef_switching": False,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "Tunnel20": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.145.24.118/30": {
                "ip": "10.145.24.118",
                "prefix_length": "30",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1420,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.1",
            "224.0.0.13",
            "224.0.0.2",
            "224.0.0.22"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "Vlan1": {
        "enabled": True,
        "oper_status": "up"
    }
}
expected_output = {
    "service_instance": {
        100: {
            "interfaces": {
                "TenGigabitEthernet0/1": {
                    "description": "Fiber Connexion to XXX-111-1111",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "efp_statistics": {
                        "bytes_in": 3955205745,
                        "bytes_out": 20480433984,
                        "pkts_in": 36279507,
                        "pkts_out": 42299716,
                    },
                    "encapsulation": "dot1q 19 vlan protocol type 0x8100 second-dot1q 149 vlan protocol type 0x8100",
                    "l2protocol_drop": True,
                    "micro_block_type": {
                        "Bridge-domain": {"bridge_domain": 129},
                        "L2Mcast": {"l2_multicast_gid": 54},
                        "dhcp_snoop": {"l2_multicast_gid": 54},
                    },
                    "rewrite": "ingress tag pop 2 symmetric",
                    "state": "Up",
                    "type": "Static",
                }
            }
        },
        2000: {
            "interfaces": {
                "TenGigabitEthernet0/1": {
                    "description": "Fiber Connexion (Layer 2) to XXX-200-2222",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "efp_statistics": {
                        "bytes_in": 51800659418,
                        "bytes_out": 229082305074,
                        "pkts_in": 356008885,
                        "pkts_out": 533687182,
                    },
                    "encapsulation": "dot1q 21 vlan protocol type 0x8100 second-dot1q 1-123,150-5000 vlan protocol type 0x8100",
                    "l2protocol_drop": True,
                    "micro_block_type": {
                        "Bridge-domain": {"bridge_domain": 200},
                        "L2Mcast": {"l2_multicast_gid": 58},
                        "dhcp_snoop": {"l2_multicast_gid": 58},
                    },
                    "rewrite": "ingress tag pop 1 symmetric",
                    "state": "Up",
                    "type": "Static",
                }
            }
        },
    }
}

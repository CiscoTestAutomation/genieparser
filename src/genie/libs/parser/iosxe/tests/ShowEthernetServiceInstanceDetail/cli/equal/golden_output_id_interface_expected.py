expected_output = {
    "service_instance": {
        4000: {
            "interfaces": {
                "GigabitEthernet0/0/0": {
                    "type": "Trunk",
                    "l2protocol_drop": True,
                    "encapsulation": "dot1q 2-21 vlan protocol type 0x8100",
                    "rewrite": "ingress tag pop 1 symmetric",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "state": "Up",
                    "efp_statistics": {
                        "pkts_in": 2810511074,
                        "bytes_in": 191114753032,
                        "pkts_out": 0,
                        "bytes_out": 0,
                    },
                    "micro_block_type": {
                        "Bridge-domain": {"bridge_domain": "2-21"},
                        "L2Mcast": {"l2_multicast_gid": 9},
                        "dhcp_snoop": {"l2_multicast_gid": 9},
                        "PPPoE IA UBLOCK": {"enable": 0, "format_type": 0},
                    },
                }
            }
        }
    }
}

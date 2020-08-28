expected_output = {
    "service_instance": {
        1: {
            "interfaces": {
                "Ethernet0/0": {
                    "control_policy": "ABC",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "efp_statistics": {
                        "bytes_in": 0,
                        "bytes_out": 0,
                        "pkts_in": 0,
                        "pkts_out": 0,
                    },
                    "encapsulation": "dot1q 200-300 vlan protocol type 0x8100",
                    "intiators": "unclassified vlan",
                    "l2protocol_drop": True,
                    "state": "Up",
                    "type": "L2Context",
                }
            }
        },
        2: {
            "interfaces": {
                "Ethernet0/0": {
                    "ce_vlans": "10-20",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "efp_statistics": {
                        "bytes_in": 0,
                        "bytes_out": 0,
                        "pkts_in": 0,
                        "pkts_out": 0,
                    },
                    "encapsulation": "dot1q 201 vlan protocol type 0x8100",
                    "l2protocol_drop": True,
                    "state": "Up",
                    "type": "Dynamic",
                }
            }
        },
        3: {
            "interfaces": {
                "Ethernet0/0": {
                    "ce_vlans": "10-20",
                    "dot1q_tunnel_ethertype": "0x8100",
                    "efp_statistics": {
                        "bytes_in": 0,
                        "bytes_out": 0,
                        "pkts_in": 0,
                        "pkts_out": 0,
                    },
                    "encapsulation": "dot1q 201 vlan protocol type 0x8100",
                    "l2protocol_drop": True,
                    "state": "Up",
                    "type": "static",
                }
            }
        },
    }
}

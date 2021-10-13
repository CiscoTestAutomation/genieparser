expected_output = {
    "lpts_policer_list": {
        "0/RP0/CPU0": {
            "lpts_policer": [
                {
                    "flow_type": "Fragment",
                    "policer": 2,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 2,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "OSPF-mc-known",
                    "policer": 3,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "OSPF-mc-default",
                    "policer": 4,
                    "type": "np",
                    "current_rate": 1017,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "OSPF-uc-known",
                    "policer": 5,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "OSPF-uc-default",
                    "policer": 6,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "BFD-default",
                    "policer": 10,
                    "type": "np",
                    "current_rate": 7864,
                    "burst": 1000,
                    "accepted": 75,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "BFD-MP-known",
                    "policer": 11,
                    "type": "np",
                    "current_rate": 7864,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "BGP-known",
                    "policer": 16,
                    "type": "np",
                    "current_rate": 16272,
                    "burst": 1000,
                    "accepted": 120267993,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "BGP-cfg-peer",
                    "policer": 17,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 294,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "BGP-default",
                    "policer": 18,
                    "type": "np",
                    "current_rate": 1017,
                    "burst": 1000,
                    "accepted": 553,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "PIM-mcast-default",
                    "policer": 19,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "PIM-mcast-known",
                    "policer": 20,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "PIM-ucast",
                    "policer": 21,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 135624,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "IGMP",
                    "policer": 22,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "ICMP-local",
                    "policer": 23,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 1165931,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "ICMP-control",
                    "policer": 25,
                    "type": "np",
                    "current_rate": 2101,
                    "burst": 1000,
                    "accepted": 145677506,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "LDP-TCP-known",
                    "policer": 28,
                    "type": "np",
                    "current_rate": 2101,
                    "burst": 1000,
                    "accepted": 186297,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "LDP-TCP-cfg-peer",
                    "policer": 29,
                    "type": "np",
                    "current_rate": 1017,
                    "burst": 1000,
                    "accepted": 8,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "LDP-TCP-default",
                    "policer": 30,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "LDP-UDP",
                    "policer": 31,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 520734,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "All-routers",
                    "policer": 32,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "RSVP-default",
                    "policer": 38,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "RSVP-known",
                    "policer": 39,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "SNMP",
                    "policer": 47,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 87256864,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "SSH-known",
                    "policer": 48,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 4775896,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "SSH-default",
                    "policer": 49,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "HTTP-known",
                    "policer": 50,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "SHTTP-known",
                    "policer": 52,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "TELNET-known",
                    "policer": 54,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "TELNET-default",
                    "policer": 55,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "UDP-known",
                    "policer": 60,
                    "type": "np",
                    "current_rate": 23865,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "UDP-default",
                    "policer": 63,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 443643,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "TCP-known",
                    "policer": 64,
                    "type": "np",
                    "current_rate": 23865,
                    "burst": 1000,
                    "accepted": 1902746,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "TCP-default",
                    "policer": 67,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 2132524,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "Raw-default",
                    "policer": 71,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 1235342,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "GRE",
                    "policer": 77,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "VRRP",
                    "policer": 78,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "DNS",
                    "policer": 83,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "NTP-known",
                    "policer": 87,
                    "type": "np",
                    "current_rate": 474,
                    "burst": 1000,
                    "accepted": 93812,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "TPA",
                    "policer": 96,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                },
                {
                    "flow_type": "PM-TWAMP",
                    "policer": 99,
                    "type": "np",
                    "current_rate": 1559,
                    "burst": 1000,
                    "accepted": 0,
                    "dropped": 0,
                    "npu": 0
                }
            ]
        }
    }
}
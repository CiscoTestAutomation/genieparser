expected_output = {
        "Vlan88": {
            "port_channel": {
                "port_channel_member": False
            },
            "link_state": "up",
            "enabled": True,
            "oper_status": "up",
            "line_protocol": "up",
            "autostate": True,
            "delay": 10,
            "mtu": 1500,
            "bandwidth": 1000000,
            "reliability": "255/255",
            "txload": "1/255",
            "rxload": "1/255",
            "encapsulations": {
                "encapsulation": "arpa"
            }
        },
        "port-channel233": {
            "port_channel": {
                "port_channel_member": False
            },
            "link_state": "down",
            "enabled": True,
            "oper_status": "down",
            "admin_state": "up",
            "dedicated_interface": True,
            "types": "10/100/1000 Ethernet",
            "mac_address": "aaaa.bbff.8888",
            "phys_address": "5254.00ff.8506",
            "description": "desc-1",
            "ipv4": {
                "10.4.4.4/24": {
                    "ip": "10.4.4.4",
                    "prefix_length": "24",
                    "secondary": True,
                    "route_tag": "10"
                }
            },
            "delay": 3330,
            "mtu": 1600,
            "bandwidth": 768,
            "reliability": "255/255",
            "txload": "1/255",
            "rxload": "1/255",
            "encapsulations": {
                "encapsulation": "arpa"
            },
            "medium": "broadcast",
            "port_mode": "routed",
            "duplex_mode": "full",
            "port_speed": "1000",
            "beacon": "off",
            "auto_negotiate": False,
            "flow_control": {
                "receive": False,
                "send": False
            },
            "auto_mdix": "off",
            "switchport_monitor": "off",
            "ethertype": "0x8100",
            "efficient_ethernet": "n/a",
            "last_link_flapped": "00:00:29",
            "interface_reset": 1,
            "counters": {
                "rate": {
                    "load_interval": 0,
                    "in_rate": 0,
                    "in_rate_pkts": 0,
                    "out_rate": 0,
                    "out_rate_pkts": 0,
                    "in_rate_bps": 0,
                    "in_rate_pps": 0,
                    "out_rate_bps": 0,
                    "out_rate_pps": 0
                },
                "rx": True,
                "in_unicast_pkts": 0,
                "in_multicast_pkts": 0,
                "in_broadcast_pkts": 0,
                "last_clear": "never",
                "in_pkts": 0,
                "in_octets": 0,
                "in_jumbo_packets": 0,
                "in_storm_suppression_packets": 0,
                "in_runts": 0,
                "in_oversize_frame": 0,
                "in_crc_errors": 0,
                "in_no_buffer": 0,
                "in_errors": 0,
                "in_short_frame": 0,
                "in_overrun": 0,
                "in_underrun": 0,
                "in_ignored": 0,
                "in_watchdog": 0,
                "in_bad_etype_drop": 0,
                "in_unknown_protos": 0,
                "in_if_down_drop": 0,
                "in_with_dribble": 0,
                "in_discard": 0,
                "in_mac_pause_frames": 0,
                "tx": True,
                "out_unicast_pkts": 0,
                "out_multicast_pkts": 0,
                "out_broadcast_pkts": 0,
                "out_pkts": 0,
                "out_octets": 0,
                "out_jumbo_packets": 0,
                "out_errors": 0,
                "out_collision": 0,
                "out_deferred": 0,
                "out_late_collision": 0,
                "out_lost_carrier": 0,
                "out_no_carrier": 0,
                "out_babble": 0,
                "out_discard": 0,
                "out_mac_pause_frames": 0
            }
        }
    }
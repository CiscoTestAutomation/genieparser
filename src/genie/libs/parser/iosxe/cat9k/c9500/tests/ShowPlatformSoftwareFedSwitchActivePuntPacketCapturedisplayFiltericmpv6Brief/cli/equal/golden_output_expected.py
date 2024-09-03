expected_output = {
    "punt_packet_number": {
        "6": {
            "ce_hdr": {
                "dest_mac": "f4bd.9eff.fff0",
                "ethertype": "0x7106",
                "src_mac": "f4bd.9eff.fff1"
            },
            "ether_hdr": {
                "dest_mac": "3333.0000.0016",
                "ether_type": "0x8100",
                "src_mac": "a0b4.39cd.70ff",
                "vlan": 100
            },
            "interface": {
                "pal": {
                    "if_id": "0x0000058a",
                    "val": "Port-channel10"
                },
                "phy": {
                    "if_id": "0x0000058a",
                    "val": "Port-channel10"
                }
            },
            "ipv6_hdr": {
                "dest_ip": "ff02::16",
                "hop_count": 1,
                "next_hdr": 0,
                "payload_len": 36,
                "src_ip": "fe80::a2b4:39ff:fecd:70ff"
            },
            "meta_hdr": {
                "dlp": "0xef",
                "dsp": "0xffff",
                "fwd_hdr": 0,
                "nxt_hdr": "0x1",
                "slp": "0x800fb",
                "ssp": "0x55f"
            },
            "misc_info": {
                "cause_desc": "Layer2 bridge domain data packet",
                "cause_number": 58,
                "link_type": "IPV6 ",
                "subcause_desc": "NONE",
                "subcause_number": 11
            },
            "timestamp": "2024/06/25 16:17:59.842"
        },
        "7": {
            "ce_hdr": {
                "dest_mac": "f4bd.9eff.fff0",
                "ethertype": "0x7106",
                "src_mac": "f4bd.9eff.fff1"
            },
            "ether_hdr": {
                "dest_mac": "3333.0000.0016",
                "ether_type": "0x8100",
                "src_mac": "a0b4.39cd.70ff",
                "vlan": 300
            },
            "interface": {
                "pal": {
                    "if_id": "0x0000058b",
                    "val": "Port-channel11"
                },
                "phy": {
                    "if_id": "0x0000058b",
                    "val": "Port-channel11"
                }
            },
            "ipv6_hdr": {
                "dest_ip": "ff02::18",
                "hop_count": 1,
                "next_hdr": 0,
                "payload_len": 18,
                "src_ip": "fe80::a2b4:39ff:fecd:30fd"
            },
            "meta_hdr": {
                "dlp": "0xef",
                "dsp": "0xffff",
                "fwd_hdr": 0,
                "nxt_hdr": "0x1",
                "slp": "0x800fb",
                "ssp": "0x55f"
            },
            "misc_info": {
                "cause_desc": "Layer2 bridge domain data packet",
                "cause_number": 58,
                "link_type": "IPV6 ",
                "subcause_desc": "NONE",
                "subcause_number": 11
            },
            "timestamp": "2024/06/25 16:17:59.832"
        }
    }
}

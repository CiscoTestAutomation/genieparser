expected_output = {
    "punt_packet_number": {
        "41,": {
            "ce_hdr": {
                "dest_mac": "4e41.5000.0111",
                "ethertype": "0x7106",
                "src_mac": "4e41.5000.0111"
            },
            "ether_hdr": {
                "dest_mac": "3c57.3104.7045",
                "ether_type": "0x8100",
                "src_mac": "a0b4.39cd.70ff",
                "vlan": 100
            },
            "icmp_hdr": {
                "code": 0,
                "icmp_type": 8
            },
            "interface": {
                "pal": {
                    "if_id": "0x00000624]",
                    "val": "Vlan100"
                },
                "phy": {
                    "if_id": "0x00000624",
                    "val": "Vlan100"
                }
            },
            "ipv4_hdr": {
                "dest_ip": "100.10.1.1",
                "packet_len": 100,
                "protocol": "1 (ICMP)",
                "src_ip": "1.0.0.3",
                "ttl": 254
            },
            "meta_hdr": {
                "dlp": "0xef",
                "dsp": "0xffff",
                "fwd_hdr": "0x2",
                "nxt_hdr": "0x1",
                "slp": "0x122",
                "ssp": "0x119"
            },
            "misc_info": {
                "cause": "For-us control]",
                "cause_number": "55",
                "link_type": "IP [1]"
            }
        },
        "51,": {
            "ce_hdr": {
                "dest_mac": "4e41.5000.0111",
                "ethertype": "0x7106",
                "src_mac": "4e41.5000.0111"
            },
            "ether_hdr": {
                "dest_mac": "3c57.3104.7045",
                "ether_type": "0x8100",
                "src_mac": "a0b4.39cd.70ff",
                "vlan": 200
            },
            "icmp_hdr": {
                "code": 0,
                "icmp_type": 9
            },
            "interface": {
                "pal": {
                    "if_id": "0x00000624]",
                    "val": "Vlan100"
                },
                "phy": {
                    "if_id": "0x00000624",
                    "val": "Vlan100"
                }
            },
            "ipv4_hdr": {
                "dest_ip": "10.10.1.1",
                "packet_len": 100,
                "protocol": "1 (ICMP)",
                "src_ip": "1.1.1.3",
                "ttl": 254
            },
            "meta_hdr": {
                "dlp": "0xef",
                "dsp": "0xffff",
                "fwd_hdr": "0x2",
                "nxt_hdr": "0x1",
                "slp": "0x122",
                "ssp": "0x119"
            },
            "misc_info": {
                "cause": "For-us control]",
                "cause_number": "55",
                "link_type": "IP [1]"
            }
        },
        "timestamp": "2024/06/25 16:07:00.656 ------"
    }
}
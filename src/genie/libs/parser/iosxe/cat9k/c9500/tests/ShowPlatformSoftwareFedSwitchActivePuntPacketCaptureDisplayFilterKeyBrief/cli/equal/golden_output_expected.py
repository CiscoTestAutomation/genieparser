expected_output = {
    'punt_packet_number': {
        '3659': {
            'arp_hdr': {
                'dest_ip': '14.0.1.2',
                'dest_mac': 'ffff.ffff.ffff',
                'opcode': {
                    'opcode_number': 2,
                    'val': '2 (ARP Reply)',
                },
                'src_ip': '14.0.1.2',
                'src_mac': '00a7.428a.7fbf',
            },
            'ce_hdr': {
                'dest_mac': '4e41.5000.0010',
                'ethertype': '0x7102',
                'src_mac': '4e41.5000.0111',
            },
            'ether_hdr': {
                'dest_mac': 'ffff.ffff.ffff',
                'ethertype': '0x8100',
                'src_mac': '00a7.428a.7fbf',
                'vlan': 101,
            },
            'interface': {
                'pal': {
                    'if_id': '0x000005ce',
                    'val': 'Port11lVlan101',
                },
                'phy': {
                    'if_id': '0x50000000b0065',
                    'val': 'Port11lVlan101',
                },
            },
            'misc_info': {
                'cause': 'ARP request or response',
                'cause_number': 7,
            },
        },
        '36906': {
            'arp_hdr': {
                'dest_ip': '14.9.1.2',
                'dest_mac': 'ffff.ffff.ffff',
                'opcode': {
                    'opcode_number': 2,
                    'val': '2 (ARP Reply)',
                },
                'src_ip': '14.0.1.3',
                'src_mac': '00a7.428a.7fbf',
            },
            'ce_hdr': {
                'dest_mac': '4e41.5000.0010',
                'ethertype': '0x7102',
                'src_mac': '4e41.5000.0111',
            },
            'ether_hdr': {
                'dest_mac': 'ffff.ffff.ffff',
                'ethertype': '0x8101',
                'src_mac': '00a7.428a.7fbf',
                'vlan': 10,
            },
            'interface': {
                'pal': {
                    'if_id': '0x000005ce',
                    'val': 'Port11lVlan101',
                },
                'phy': {
                    'if_id': '0x50000000b0065',
                    'val': 'Port11lVlan101',
                },
            },
            'misc_info': {
                'cause': 'ARP request or response',
                'cause_number': 8,
            },
        },
        'timestamp': '2024/05/13 06:54:41.280 ',
    },
    'total_captured_so_far': 4096,
}
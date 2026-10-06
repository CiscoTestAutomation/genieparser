# golden_output_1_expected.py
#
# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.

expected_output  = {
    'dhcp_server_database_count': 3,
    'entries': {
        1: {
            'link_layer_address': 'dead.beef.0008',
            'vlan_id': 20,
            'network_layer_address': '3002::30',
            'duid_length': 1,
            'duid': '10',
            'interface': 'Twe1/0/1',
            'last_pkt_recv': '6s',
            'reply_count': 1,
            'last_reply_recv': '6s',
            'last_addr_allocated': '2001:DB8::105',
            'preferred_lifetime': '60s',
            'valid_lifetime': '60s'
        },
        2: {
            'link_layer_address': 'dead.beef.0008',
            'vlan_id': 20,
            'network_layer_address': '3002::30',
            'duid_length': 1,
            'duid': '10',
            'interface': 'Twe1/0/1',
            'last_pkt_recv': '6s',
            'reply_count': 0,
            'last_reply_recv': 'n/a',
            'last_addr_allocated': 'none',
            'preferred_lifetime': '0s',
            'valid_lifetime': '0s'
        },
        3: {
            'link_layer_address': '0102.0304.0506',
            'vlan_id': 100,
            'network_layer_address': 'FF01::1234:5678',
            'duid_length': 99,
            'duid': '565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656565656',
            'interface': 'Twe1/0/2',
            'last_pkt_recv': '1m 1s',
            'reply_count': 1,
            'last_reply_recv': '1m 1s',
            'last_addr_allocated': '3002::30',
            'preferred_lifetime': '60s',
            'valid_lifetime': '60s'
        }
    }
}

# golden_output_expected.py
#
# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.

expected_output  = {
    'dhcp_server_database_count': 1,
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
        }
    }
}

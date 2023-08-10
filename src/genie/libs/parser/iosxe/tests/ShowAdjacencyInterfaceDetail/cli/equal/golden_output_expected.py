# golden_output_expected.py
#
# Copyright (c) 2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'protocol': 'IPV6',
    'interface': 'Tunnel0',
    'address': 'ABCD:2::2(4)',
    'connectionid': 1,
    'traffic_data': {
        'packets': 56,
        'bytes':7494
    },
    'epoch': 0,
    'sourced_in_sev_epoch': 1,
    'encap_length': 48,
    'encap_str': '60000000000011FFABCD0001000000000000000000000002ABCD000200000000000000000000000212B512B500000000',
    'adjacency_source': 'Tun endpt',
    'next_chain_elem': {
        'protocol': 'IPV6',
        'outgoing_interface': 'Ethernet1/0',
        'outgoing_address': 'FE80::A8BB:CCFF:FE02:5710'
    }
}

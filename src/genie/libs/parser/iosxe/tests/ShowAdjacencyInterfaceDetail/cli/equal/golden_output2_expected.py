# golden_output2_expected.py
#
# Copyright (c) 2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'protocol': 'IPV6',
    'interface': 'Ethernet1/0',
    'address': 'FE80::A8BB:CCFF:FE02:5710(16)',
    'traffic_data': {
        'packets': 7856,
        'bytes': 1156536
    },
    'epoch': 0,
    'sourced_in_sev_epoch': 1,
    'encap_length': 14,
    'encap_str': 'AABBCC025710AABBCC01F50186DD',
    'L2_destination_address': {
        'byte_offset': 0,
        'byte_length': 6
    },
    'link_type_after_encap': 'ipv6',
    'adjacency_source': 'IPv6 ND'
}

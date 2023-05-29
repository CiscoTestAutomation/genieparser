# golden_output_expected.py
#
# Copyright (c) 2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'protocol': 'IP',
    'interface': 'Vlan3',
    'address': 'ABCD:2::2(6)',
    'traffic_data': {
        'packets': 0,
        'bytes':0
    },
    'epoch': 0,
    'sourced_in_sev_epoch': 4,
    'encap_length': 14,
    'encap_str': 'AABBCC81F600AABBCC81F5000800',
    'adjacency_source': 'VXLAN Transport tunnel',
}

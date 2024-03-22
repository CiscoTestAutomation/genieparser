# golden_output_expected.py
#
# Copyright (c) 2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'admin_state': 'Up',
    'bgp_host_reachability': 'Enabled',
    'encap': 'Vxlan IPv4',
    'interface': 'nve1',
    'mcast_encap': 'Vxlan IPv4',
    'num_l2vni_cp': 12,
    'num_l2vni_dp': 0,
    'num_l3vni_cp': 2,
    'oper_state': 'Up',
    'src_intf': {
        'Loopback2': {
            'primary_ip': '1.1.1.3',
            'vrf': '0',
        },
    },
    'tunnel_intf': {
        'Tunnel1': {
            'counters': {
                'bytes_in': 0,
                'bytes_out': 0,
                'pkts_in': 0,
                'pkts_out': 0,
            },
        },
    },
    'tunnel_primary': 'Tunnel1',
    'vxlan_dport': 4789,
}

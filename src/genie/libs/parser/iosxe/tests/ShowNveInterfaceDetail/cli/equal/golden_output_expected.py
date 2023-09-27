expected_output = {
    'admin_state': 'Up',
    'bgp_host_reachability': 'Enabled',
    'encap': 'Vxlan',
    'interface': 'nve1',
    'num_l2vni_cp': 2,
    'num_l2vni_dp': 0,
    'num_l3vni_cp': 30,
    'oper_state': 'Down',
    'src_intf': {
        'Loopback1': {
            'primary_ip': '1.1.1.2',
            'vrf': '0',
        },
    },
    'tunnel_intf': {
        'Tunnel0': {
            'counters': {
                'bytes_in': 11,
                'bytes_out': 0,
                'pkts_in': 1,
                'pkts_out': 0
            },
        }
    },
    'tunnel_primary': 'Tunnel0',
    'vxlan_dport': 4789,
}

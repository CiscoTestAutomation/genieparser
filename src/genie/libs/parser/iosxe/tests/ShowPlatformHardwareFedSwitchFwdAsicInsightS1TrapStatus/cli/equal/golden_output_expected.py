expected_output = {
    'trap_status': {
        'ETHERNET_ACCEPTABLE_FORMAT': {
            'direction': 'NONE',
        },
        'ETHERNET_ACL_DROP': {
            'direction': 'EGRESS',
            'overwrite_phb': True,
            'priority': 1,
            'skip_inject_up': False,
            'skip_p2p': False,
            'traffic_class': 0,
        },
        'ETHERNET_ACL_FORCE_PUNT': {
            'direction': 'EGRESS',
            'overwrite_phb': True,
            'priority': 21,
            'skip_inject_up': False,
            'skip_p2p': False,
            'traffic_class': 0,
        },
        'ETHERNET_ARP': {
            'direction': 'NONE',
        },
        'ETHERNET_CISCO_PROTOCOLS': {
            'direction': 'INGRESS',
            'l2_punt_oid': 375,
            'overwrite_phb': True,
            'priority': 3,
            'skip_inject_up': True,
            'skip_p2p': True,
            'traffic_class': 5,
        },
        'ETHERNET_DA_ERROR': {
            'direction': 'INGRESS',
            'overwrite_phb': True,
            'priority': 10,
            'skip_inject_up': True,
            'skip_p2p': False,
            'traffic_class': 0,
        },
    },
}
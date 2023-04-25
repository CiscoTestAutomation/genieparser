# golden_output_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'reptype': 'ingress',
    'floodsup_ar_disable': True,
    'floodsup_dhcprelay_disable': True,
    'mh_alias_disable': True,
    'dgw_advertise': True,
    'mcast_advertise': True,
    'evis': {
        '1': {
            'srvinst': 'vlan-based',
            'encaptype': 'vxlan',
            'reptype': 'static',
            'dgw_advertise': False,
            'mcast_advertise': True,
        },
        '2': {
            'srvinst': 'vlan-based',
            'reptype': 'ingress',
            'dgw_advertise': True,
            'mcast_advertise': True,
        },
    },
}

# golden_output_1_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
        'adv_def_gateway': False,
        'adv_mcast': True,
        'arp_flood_suppression': True,
        'auto_rt': 'evi-id based',
        'bgp': {'asn': 1, 'evpn_af_configured': True},
        'bridge_domains': 1,
        'core_connected': True,
        'def_gateway_addresses': {'local': 1, 'remote': 0, 'total': 1},
        'evis': {'total': 1, 'vlan_based': 1},
        'glb_ip_local_learn': True,
        'glb_rep_type': 'Static',
        'ip_addresses': {'duplicate': 3, 'local': 5, 'remote': 6, 'total': 14},
        'ip_dup': {'limit': 5, 'seconds': 180},
        'ip_local_learn_limit': {'ipv4': 4, 'ipv6': 12},
        'ip_local_learn_timer': {'down': 10, 'poll': 1, 'reachable': 5, 'stale': 30},
        'mac_addresses': {'duplicate': 2, 'local': 11, 'remote': 12, 'total': 25},
        'mac_dup': {'limit': 100, 'seconds': 10},
        'max_rt_per_ead_es': 200,
        'mh_aliasing': True,
        'router_id': '20.20.20.20'
}

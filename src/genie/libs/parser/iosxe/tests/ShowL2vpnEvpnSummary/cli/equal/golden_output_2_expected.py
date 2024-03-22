# golden_output_2_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
        'adv_def_gateway': False,
        'adv_mcast': False,
        'arp_flood_suppression': True,
        'auto_rt': 'evi-id based',
        'bgp': {'asn': 1, 'evpn_af_configured': True},
        'bridge_domains': 10,
        'core_connected': True,
        'def_gateway_addresses': {'local': 0, 'remote': 0, 'total': 0},
        'evis': {'total': 6, 'vlan_aware': 2, 'vlan_based': 2, 'vlan_bundle': 2},
        'glb_ip_local_learn': True,
        'glb_rep_type': 'Ingress',
        'ip_addresses': {'duplicate': 0, 'local': 20, 'remote': 20, 'total': 40},
        'ip_dup': {'limit': 5, 'seconds': 180},
        'ip_local_learn_limit': {'ipv4': 4, 'ipv6': 12},
        'ip_local_learn_timer': {'down': 10, 'poll': 1, 'reachable': 5, 'stale': 30},
        'label_alloc_mode': 'Per-BD',
        'mac_addresses': {'duplicate': 0, 'local': 20, 'remote': 20, 'total': 40},
        'mac_dup': {'limit': 5, 'seconds': 180},
        'max_rt_per_ead_es': 200,
        'mh_aliasing': True,
        'router_id': '10.10.10.10'
}

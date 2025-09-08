expected_output = {
    'system_information': {
        'links_count': 4,
        'flooding_system': 'enabled',
    },
    'igp_areas': {
        'ospf 100  area 0': {
            'flooding_protocol': 'OSPF',
            'flooding_status': 'data flooded',
            'periodic_flooding': 'enabled (every 60 seconds, next in 12 seconds)',
            'flooded_links': 3,
            'igp_system_id': '10.2.1.1',
            'mpls_te_router_id': '10.2.1.1',
            'neighbors': 3,
        }
    },
    'links': {
        'Gi0/1/2_172.2.5.2': {
            'interface': 'Gi0/1/2',
            'remote_ip': '172.2.5.2',
            'local_intfc_id': 13,
            'srlgs': 'None',
            'intfc_switching_capability_descriptors': {
                'default': 'Intfc Switching Cap psc1, Encoding ethernet',
            },
            'link_label_type': 'Packet',
            'physical_bandwidth': '1000000 kbits/sec',
            'max_res_global_bw': '750000 kbits/sec (reserved: 0% in, 0% out)',
            'max_res_sub_bw': '0 kbits/sec (reserved: 100% in, 100% out)',
            'mpls_te_link_state': 'MPLS TE on, RSVP on, admin-up, flooded',
            'inbound_admission': 'reject-huge',
            'outbound_admission': 'allow-if-room',
            'link_mtu': {
                'ip': 1500,
                'mpls': 1500
            }
        }
    }
}

expected_output = {
    'group_members_registered': 12,
    'bw6000': {
        'group_name': 'bw6000',
        're_auth_on_new_crl': 'Disabled',
        'group_identity': 6000,
        'group_type': 'ISAKMP',
        'group_members': 2,
        'rekey_acknowledgement_cfg': 'Cisco',
        'ipsec_sa_direction': 'Both',
        'ip_d3p_window': 'Disabled',
        'split_resiliency_factor': 0,
        'ckm_status': 'Disabled',
        'acl_configured': {
            'access_list': 'bw600-crypto-policy',
        },
        'redundancy': {
            'redundancy_mode': 'Configured',
            'local_address': '15.15.15.1',
            'local_priority': 245,
            'local_ks_status': 'Alive',
            'local_ks_role': 'Primary',
            'local_ks_version': '1.0.27',
            'local_coop_version': '1.0.8',
        },
    },
    'bw600-IPV6': {
        'group_name': 'bw600-IPV6',
        're_auth_on_new_crl': 'Disabled',
        'group_identity': 6600,
        'group_type': 'ISAKMP',
        'group_members': 2,
        'rekey_acknowledgement_cfg': 'Cisco',
        'ipsec_sa_direction': 'Both',
        'ip_d3p_window': 'Disabled',
        'split_resiliency_factor': 0,
        'ckm_status': 'Disabled',
        'acl_configured': {
            'access_list': 'bw600-v6-crypto-policy',
        },
        'redundancy': {
            'redundancy_mode': 'Configured',
            'local_address': '15.15.15.1',
            'local_priority': 245,
            'local_ks_status': 'Alive',
            'local_ks_role': 'Primary',
            'local_ks_version': '1.0.27',
            'local_coop_version': '1.0.8'
        }
    }

}


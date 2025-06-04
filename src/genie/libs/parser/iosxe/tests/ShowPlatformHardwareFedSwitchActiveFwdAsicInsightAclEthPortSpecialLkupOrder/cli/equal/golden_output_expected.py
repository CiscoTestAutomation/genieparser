expected_output = {
    'acl_eth_port_special_lkup_order': {
        813: {
            'acl_direction': 'INGRESS',
            'acl_packet_format': 'ETHERNET',
            'entries': [
                {'acl_plkp_oid': 557, 'acl_kp_oid': 492, 'acl_interface': 'E_0', 'acl_stage': 'TERMINATION', 'acl_label_type': 'CLIENT_LABEL'},
                {'acl_plkp_oid': 557, 'acl_kp_oid': 497, 'acl_interface': 'E_0', 'acl_stage': 'TERMINATION', 'acl_label_type': 'PORT_LABEL'},
                {'acl_plkp_oid': 557, 'acl_kp_oid': 500, 'acl_interface': 'E_0', 'acl_stage': 'TERMINATION', 'acl_label_type': 'LIF_LABEL'}
            ],
            'eth_port_oid': 813,
            'eth_port_underlay_type': 'sysport-gid',
            'underlay_port_gid': 47,
        },
    },
}
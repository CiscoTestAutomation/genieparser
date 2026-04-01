expected_output = {
    'cef_capabilities': {
        'supported_address_families': ['IPv4', 'IPv6', 'Binding-Label'],
        'active_address_families': ['IPv4', 'IPv6', 'Binding-Label'],
        'distributed_platform': True,
        'warm_or_hot_standby_supported': True,
        'cef_nsf_capable': True,
        'hardware_forwarding': False,
        'checker_auto_repair_supported': True,
        'crashdump_on_memory_failure': False,
        'blocking_standby_hot_until_synced': True
    },
    'label_fib_cef_status': {
        'load_sharing_algorithm': 'universal per-destination load sharing algorithm',
        'algorithm_id': '5808CE4A'
    },
    'ipv4_cef_capabilities': {
        'default_cef_switching': True,
        'always_fib_switching': True,
        'default_dcef_switching': True,
        'always_dcef_switching': True,
        'drop_multicast_packets': False,
        'ok_to_punt_packets': True,
        'nvgen_cef_state': False,
        'fastsend_used': True,
        'support_per_packet_load_sharing': False,
        'multicast_groups_in_cef': False,
        'install_local_entries_from_rib': False
    },
    'ipv6_cef_capabilities': {
        'default_cef_switching': True,
        'always_fib_switching': True,
        'default_dcef_switching': True,
        'always_dfib_switching': True,
        'drop_multicast_packets': False,
        'ok_to_punt_packets': True,
        'nvgen_cef_state': False,
        'fastsend_used': True
    },
    'cef_issu_status': {
        'fibhwidb_broker': {
            'status': 'No slots are ISSU capable'
        },
        'fibidb_broker': {
            'status': 'No slots are ISSU capable'
        },
        'fibhwidb_subblock_broker': {
            'status': 'No slots are ISSU capable'
        },
        'fibidb_subblock_broker': {
            'status': 'No slots are ISSU capable'
        },
        'adjacency_update': {
            'status': 'No slots are ISSU capable'
        },
        'ipv4_table_broker': {
            'status': 'No slots are ISSU capable'
        },
        'ipv6_table_broker': {
            'status': 'No slots are ISSU capable'
        },
        'cef_push': {
            'status': 'No slots are ISSU capable'
        },
        'label_fib_table_broker': {
            'status': 'No slots are ISSU capable'
        }
    }
}

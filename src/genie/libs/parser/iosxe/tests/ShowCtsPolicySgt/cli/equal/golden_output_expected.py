expected_output = {
    'cts_sgt_policy': {
        'rbacl_monitor_all': False,
        'rbacl_ip_version_supported': 'IPv4 & IPv6',
        'sgt': '30-01:SGT_030  (address=0x750E40477850)',
        'sgt_policy_flag': '0x41400001',
        'rbacl_source_list': {
            1: {
                'source_sgt': '25-00:SGT_025-0',
                'destination_sgt': '30-01:SGT_030-0',
                'rbacl_type': 80,
                'rbacl_index': 1,
                'name': 'PERMIT_IP-01',
                'ip_protocol_version': 'IPV4',
                'refcnt': 2,
                'flag': '0x41000000',
                'stale': False,
                'rbacl_aces': ['permit ip log', 'deny ip']
            }
        },
        'rbacl_destination_list': 'Not exist',
        'rbacl_multicast_list': 'Not exist',
        'rbacl_policy_lifetime': 86400,
        'rbacl_policy_last_update_time': '12:55:59 IST Wed Jan 15 2025',
        'policy_expires_in': '0:22:10:38',
        'policy_refreshes_in': '0:22:10:38',
        'cache_data_applied': 'NONE'
    }
}

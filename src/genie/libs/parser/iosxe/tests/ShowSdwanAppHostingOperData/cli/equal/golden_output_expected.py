expected_output = {
    'app_hosting_oper_data_app': {
        'utd': {
            'state': 'RUNNING',
            'pkg_info_name': 'UTD-Snort-Feature',
            'pkg_info_path': '/bootflash/.UTD_IMAGES/iox-utd_1.0.4_SV2.9.16.1_XE17.7.tar',
            'app_name': 'utd',
            'pkg_version': '1.0.4_SV2.9.16.1_XE17.7',
            'pkg_desc_name': '"Unified Threat Defense"',
            'pkg_app_type': 'LXC',
            'pkg_app_owner': 'ioxm',
            'app_act_allowed': 'true',
            'pkg_app_author': '""',
            'pkg_info_key_type': '""',
            'pkg_info_method': '""',
            'pkg_lic_name': '""',
            'pkg_lic_version': '""',
            'processes_name': '""',
            'processes_status': '""',
            'processes_pid': '""',
            'processes_uptime': '""',
            'processes_memory': '""',
            'profile_name': 'cloud-medium',
            'disk': '1111',
            'memory': '3072',
            'cpu': '0',
            'vcpu': '0',
            'cpu_percent': '50',
            'guest_intf': '""',
            'res_add_state': '""',
            'res_add_disk_space': '""',
            'res_add_memory': '""',
            'res_add_cpu': '0',
            'res_add_vcpu': '""',
            'res_doc_run_opts': '""',
            'details_command': '""',
            'details_entry_point': '""',
            'details_health_stats': '0',
            'details_probe_error': '""',
            'details_probe_output': '""',
            'details_pkg_run_opt': '""',
            'ieobc_mac_address': '33:33:3a:33:33:3a',
            'utilization_name': 'utd',
            'req_app_util': '0',
            'actual_app_util': '3',
            'cpu_state': '""',
            'mem_allocation': '3072',
            'mem_used': '335636'
        }
    },
    'name': {
        'dp_1_0': {
            'alias': 'net2',
            'rx_packets': '0',
            'rx_bytes': '0',
            'rx_errors': '0',
            'tx_packets': '30',
            'tx_bytes': '1260',
            'tx_errors': '0'
        },
        'dp_1_1': {
            'alias': 'net3',
            'rx_packets': '0',
            'rx_bytes': '0',
            'rx_errors': '0',
            'tx_packets': '0',
            'tx_bytes': '0',
            'tx_errors': '0'
        },
        'ieobc_1': {
            'alias': 'ieobc',
            'rx_packets': '190',
            'rx_bytes': '11175',
            'rx_errors': '0',
            'tx_packets': '190',
            'tx_bytes': '12303',
            'tx_errors': '0'
        }
    },
    'storage_utils_storage_util_disk': {
        'alias': '""',
        'rd_bytes': '0',
        'rd_requests': '0',
        'errors': '0',
        'wr_bytes': '0',
        'wr_requests': '0',
        'capacity': '1137664',
        'available': '255382',
        'used': '882282',
        'usage': '""',
        'pkg_policy': 'iox-pkg-policy-invalid'
    },
    'mac_address': {
        '54:0e:00:0b:0c:02 ': {
            'attached_intf': 'eth0',
            'ipv4_address': '0.0.0.0',
            'network_name': 'ieobc_1',
            'ipv6_address': '::'
        },
        'f8:6b:d9:c0:cc:5e ': {
            'attached_intf': 'eth2',
            'ipv4_address': '0.0.0.0',
            'network_name': 'dp_1_0',
            'ipv6_address': '::'
        },
        'f8:6b:d9:c0:cc:5f ': {
            'attached_intf': 'eth1',
            'ipv4_address': '192.0.2.2',
            'network_name': 'dp_1_1',
            'ipv6_address': '::'
        }
    },
    'app_hosting_oper_data_app_resources_global': {
        'cpu_details': {
            'quota': '98',
            'available': '48',
            'quota_unit': '48608',
            'available_unit': '23808'
        },
        'memory_details': {
            'quota': '4096',
            'available': '1024'
        },
        'storage_device_harddisk': {
            'quota': '512000',
            'available': '13516'
        },
        'storage_device_bootflash': {
            'quota': '1000',
            'available': '1000'
        },
        'storage_device_volume_group': {
            'quota': '14896',
            'available': '0'
        },
        'storage_device_caf_persist_disk': {
            'quota': '14534',
            'available': '12840'
        }
    },
    'app_notifications_event': {
        'timestamp': '2022-04-25T18:08:36.189866+00:00',
        'severity_level': 'minor',
        'host_name': 'pm9005',
        'vrf_name': '""',
        'app_id': 'utd',
        'ev_type': 'im-iox-enable',
        'status': 'im-app-pass',
        'app_state': 'im-state-running',
        'is_enabled': 'true'
    }
}

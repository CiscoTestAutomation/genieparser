expected_output = {
    'fib': {
        'notifications': {
            'received': 35669,
            'processed': 35669
            },
        'invalid': {
            'received': 0,
            'processed': 0
            },
        'data_packet': {
            'received': 35669,
            'processed': 35669
            },
        'l2_data_packet': {
            'received': 0,
            'processed': 0
            },
        'status_report': {
            'received': 0,
            'processed': 0
            },
        'dyn_eid_detected': {
            'received': 0,
            'processed': 0
            },
        'dyn_eid_decap_statle': {
            'received': 0,
            'processed': 0
            },
        'l2_dyn_eid_decap_statle': {
            'received': 0,
            'processed': 0
            },
        'dyn_eid_adjacency': {
            'received': 0,
            'processed': 0
            },
        'delete_map_cache': {
            'received': 0,
            'processed': 0
            }
        },
    'l2_rib': {
        'remote_update_requests': 0,
        'local_update_requests': 5,
        'delete_requests': 1,
        'update_test': 0,
        'delete_test': 0,
        'message_sent': 6,
        'message_received': 6,
        'unknown_message_received': 0,
        'send_errors': 0,
        'flow_control': 0
	},
	'cef': {
		'dropped_notifications': 0,
		'total_notifications': 35669,
		'dropped_control_packets': 0,
		'high_priority_queue': 0,
		'normal_priority_queue': 0
    },
    'deffered': {
        'ddt_referral': {
            'deferred': 0,
            'dropped': 0
            },
        'ddt_request': {
            'deferred': 0,
            'dropped': 0
            },
        'ddt_query': {
            'deferred': 0,
            'dropped': 0
            },
        'map_request': {
            'deferred': 0,
            'dropped': 0
            },
        'map_register': {
            'deferred': 0,
            'dropped': 0
            },
        'map_reply': {
            'deferred': 0,
            'dropped': 0
            },
        'mr_negative_map_reply': {
            'deferred': 0,
            'dropped': 0
            },
        'mr_map_request_fwd': {
            'deferred': 0,
            'dropped': 0
            },
        'ms_map_request_fwd': {
            'deferred': 0,
            'dropped': 0
            },
        'ms_proxy_map_reply': {
            'deferred': 0,
            'dropped': 0
            },
        'xtr_mcast_map_notify': {
            'deferred': 0,
            'dropped': 0
            },
        'ms_info_reply': {
            'deferred': 0,
            'dropped': 0
            },
        'ms_map_notify': {
            'deferred': 0,
            'dropped': 0
            },
        'rtr_map_register_fwd': {
            'deferred': 0,
            'dropped': 0
            },
        'rtr_map_notify_fwd': {
            'deferred': 0,
            'dropped': 0
            },
        'etr_info_request': {
            'deferred': 0,
            'dropped': 0
            }
        },
    'errors': {
        'invalid_ip_version_drops': 0
        },
    'udp_control_packets': {
        'ipv4': {
            'received_total_packets': 0,
            'received_invalid_vrf': 0,
            'received_invalid_ip_header': 0,
            'received_invalid_protocol': 0,
            'received_invalid_size': 0,
            'received_invalid_port': 0,
            'received_invalid_checksum': 0,
            'received_unsupported_lisp': 0,
            'received_not_lisp_control': 0,
            'received_unknown_lisp_control': 0,
            'sent_total': 0,
            'sent_flow_controlled': 0
            },
        'ipv6': {
            'received_total_packets': 0,
            'received_invalid_vrf': 0,
            'received_invalid_ip_header': 0,
            'received_invalid_protocol': 0,
            'received_invalid_size': 0,
            'received_invalid_port': 0,
            'received_invalid_checksum': 0,
            'received_unsupported_lisp': 0,
            'received_not_lisp_control': 0,
            'received_unknown_lisp_control': 0,
            'sent_total': 0,
            'sent_flow_controlled': 0
            }
        }
    }
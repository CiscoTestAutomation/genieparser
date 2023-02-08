expected_output={
        'vmi1_neighbors': 1, 
        'vmi1_1': {
            'ipv6_address': 'FE80::21E:7AFF:FEC6:7900', 
            'ipv6_global_addr': '::', 
            'ipv4_address': '121.0.0.1', 
            'uptime': '03:00:14', 
            'output_pkts': 0, 
            'input_pkts': 0, 
            'transport_pppoe': {
                'session_id': 1
            }, 
            'interface_stats': {
                'vmi_interface': {
                    'vmi1': {
                        'input_qcount': 0, 
                        'input_drops': 0, 
                        'output_qcount': 0, 
                        'output_drops': 0
                    }
                }, 
                'v_access_intf': {
                    'virtual_access1.1': {
                        'input_qcount': 0, 
                        'input_drops': 0, 
                        'output_qcount': 0, 
                        'output_drops': 0
                    }
                }, 
                'physical_intf': {
                    'gigabitethernet0/0/0': {
                        'input_qcount': 0, 
                        'input_drops': 0, 
                        'output_qcount': 0, 
                        'output_drops': 0
                    }
                }
            }, 
            'pppoe_flow_control_stats': {
                'local_credits': 65534, 
                'peer_credits': 65535, 
                'local_scaling_value': '65534 bytes', 
                'credit_grant_threshold': 28000, 
                'max_credits_per_grant': 65535, 
                'credit_starved_packets': 0, 
                'padg_xmit_seq_num': 10817, 
                'padg_timer_index': 12784, 
                'padg_last_rcvd_seq_num': 0, 
                'padg_last_nonzero_seq_num': 12784, 
                'padg_last_nonzero_rcvd_amount': 0, 
                'padg_timers_in_milliseconds': {
                    '0': 1000, 
                    '1': 2000, 
                    '2': 3000, 
                    '3': 4000, 
                    '4': 5000
                    }, 
                'padg_xmit': 10815, 
                'padg_rcvd': 0, 
                'padc_xmit': 4294770688, 
                'padc_rcvd': 10815, 
                'in_band_credit_pkt_xmit': 0, 
                'in_band_rcvd': 0, 
                'last_credit_packet_snapshot': {
                    'padg_xmit': {
                        'seq_num': 10817, 
                        'fcn': 65535, 
                        'bcn': 1
                    }, 
                    'padc_rcvd': {
                        'seq_num': 10817, 
                        'fcn': 65534, 
                        'bcn': 65535
                    }, 
                    'padg_rcvd': {
                        'seq_num': 0, 
                        'fcn': 0, 
                        'bcn': 3352
                    }, 
                    'padc_xmit': {
                        'seq_num': 3307, 
                        'fcn': 1952, 
                        'bcn': 0
                    }, 
                    'in_band_credit_pkt_xmit': {
                        'fcn': 0, 
                        'bcn': 0
                    }, 
                    'in_band_credit_pkt_rcvd': {
                        'fcn': 0, 
                        'bcn': 0
                    }, 
                    'padq_statistics': {
                        'padq_xmit': 0, 
                        'rcvd': 1
                    }
                }
            }
        }
    }

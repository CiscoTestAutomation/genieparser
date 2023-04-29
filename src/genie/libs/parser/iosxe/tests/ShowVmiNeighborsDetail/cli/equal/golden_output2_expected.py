expected_output={
        'vmi1_neighbors': 2, 
        'vmi1_1': {
            'ipv6_address': 'FE80::21E:E5FF:FE26:E700', 
            'ipv6_global_addr': '::', 
            'ipv4_address': '211.0.0.1', 
            'uptime': '2w5d', 
            'output_pkts': 0, 
            'input_pkts': 0, 
            'transport_pppoe': {
                'session_id': 49
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
                    'virtual_access2.9': {
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
                'local_credits': 65486, 
                'peer_credits': 65535, 
                'local_scaling_value': '65534 bytes', 
                'credit_grant_threshold': 28000, 
                'max_credits_per_grant': 65535, 
                'credit_starved_packets': 0, 
                'padg_xmit_seq_num': 16393, 
                'padg_timer_index': 1654622, 
                'padg_last_rcvd_seq_num': 0, 
                'padg_last_nonzero_seq_num': 16222, 
                'padg_last_nonzero_rcvd_amount': 25, 
                'padg_timers_in_milliseconds': {
                    '0': 1000, 
                    '1': 2000, 
                    '2': 3000, 
                    '3': 4000, 
                    '4': 5000
                }, 
                'padg_xmit': 1654791, 
                'padg_rcvd': 0, 
                'padc_xmit': 4291690496, 
                'padc_rcvd': 1654791, 
                'in_band_credit_pkt_xmit': 0, 
                'in_band_rcvd': 0, 
                'last_credit_packet_snapshot': {
                    'padg_xmit': {
                        'seq_num': 16393, 
                        'fcn': 65535, 
                        'bcn': 0
                    }, 
                    'padc_rcvd': {
                        'seq_num': 16393, 
                        'fcn': 65486, 
                        'bcn': 65535
                    }, 
                    'padg_rcvd': {
                        'seq_num': 0, 
                        'fcn': 7, 
                        'bcn': 45148
                    }, 
                    'padc_xmit': {
                        'seq_num': 508153, 
                        'fcn': 65534, 
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
                        'rcvd': 0
                    }
                }
            }
        }, 
        'vmi1_2': {
                'ipv6_address': 'FE80::21E:BDFF:FEF0:3A00', 
                'ipv6_global_addr': '::', 
                'ipv4_address': '221.0.0.1', 
                'uptime': '2w5d', 
                'output_pkts': 0, 
                'input_pkts': 0, 
                'transport_pppoe': {
                    'session_id': 50
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
                        'virtual_access2.10': {
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
                    'local_credits': 65495, 
                    'peer_credits': 65533, 
                    'local_scaling_value': '65534 bytes', 
                    'credit_grant_threshold': 28000, 
                    'max_credits_per_grant': 65535, 
                    'credit_starved_packets': 0, 
                    'padg_xmit_seq_num': 16383, 
                    'padg_timer_index': 1654612, 
                    'padg_last_rcvd_seq_num': 0, 
                    'padg_last_nonzero_seq_num': 16212, 
                    'padg_last_nonzero_rcvd_amount': 25, 
                    'padg_timers_in_milliseconds': {
                        '0': 1000, 
                        '1': 2000, 
                        '2': 3000, 
                        '3': 4000, 
                        '4': 5000
                    }, 
                    'padg_xmit': 1654781, 
                    'padg_rcvd': 0, 
                    'padc_xmit': 4292280320, 
                    'padc_rcvd': 1654781, 
                    'in_band_credit_pkt_xmit': 0, 
                    'in_band_rcvd': 0, 
                    'last_credit_packet_snapshot': {
                        'padg_xmit': {
                            'seq_num': 16383, 
                            'fcn': 65535, 
                            'bcn': 0
                        }, 
                        'padc_rcvd': {
                            'seq_num': 16383, 
                            'fcn': 65495, 
                            'bcn': 65535
                        }, 
                        'padg_rcvd': {
                            'seq_num': 0, 
                            'fcn': 7, 
                            'bcn': 16657
                        }, 
                        'padc_xmit': {
                            'seq_num': 494276, 
                            'fcn': 65533, 
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
                            'rcvd': 0
                        }
                    }
                }
            }
        }

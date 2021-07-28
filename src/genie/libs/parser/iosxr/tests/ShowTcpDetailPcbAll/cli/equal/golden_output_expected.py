expected_output = {
    'pcb_address': {
        '0x00007f553800d8f8': {
            'connection_state': 'ESTAB',
            'io_status': 0,
            'socket_status': 0,
            'established_datetime': 'Mon Jul 12 09:44:25 2021',
            'tcp_connection_data': {
                'pcb': '0x00007f553800d8f8',
                'so': '0x7f5538008698',
                'tcpcb': '0x7f5538008b58',
                'vrfid': '0x60000000',
                'pak_prio': 'Medium',
                'tos': 192,
                'ttl': 1,
                'hash_index': 26,
                'local_host': '2000:108:10::1',
                'local_port': 179,
                'local_app_pid': 11298,
                'foreign_host': '2000:108:10::2',
                'foreign_port': 56357,
                'local_app': {
                    'pid': 11298,
                    'instance': 1,
                    'spl_id': 0
                }
            },
            'current_queue': {
                'send': {
                    'send_size_bytes': 0,
                    'max_send_size_bytes': 24576
                },
                'receive': {
                    'receive_size_bytes': 0,
                    'max_receive_size_bytes': 32768,
                    'mis_ordered_bytes': 0,
                    'receive_size_packages': 0,
                    'max_receive_size_packages': 0
                }
            },
            'event_timers': {
                'retrans': {
                    'starts': 3,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'sendWnd': {
                    'starts': 0,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'timewait': {
                    'starts': 0,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'ackhold': {
                    'starts': 4,
                    'wakeups': 3,
                    'next_msec': 0
                },
                'keepalive': {
                    'starts': 1,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'pmtuager': {
                    'starts': 0,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'giveup': {
                    'starts': 0,
                    'wakeups': 0,
                    'next_msec': 0
                },
                'throttle': {
                    'starts': 0,
                    'wakeups': 0,
                    'next_msec': 0
                }
            },
            'sequences': {
                'iss': 2552699488,
                'snduna': 2552699622,
                'sndnxt': 2552699622,
                'sndmax': 2552699622,
                'sndwnd': 32739,
                'sndcwnd': 2880,
                'irs': 3293391238,
                'rcvnxt': 3293391391,
                'rcvwnd': 32701,
                'rcvadv': 3293424092
            },
            'round_trip_delay': {
                'srtt_ms': 34,
                'rtto_ms': 300,
                'rtv_ms': 208,
                'krtt_ms': 0,
                'min_rtt_ms': 11,
                'max_rtt_ms': 202
            },
            'times': {
                'ack_hold_ms': 200,
                'keepalive_sec': 0,
                'syn_waittime_sec': 30,
                'giveup_ms': 0,
                'retransmission_retries': 0,
                'retransmit_forever': 'FALSE',
                'connect_retries_remaining': 0,
                'connect_retry_interval_sec': 0
            },
            'flags': {
                'state': 'none',
                'feature': 'Win Scale, Nagle',
                'request': 'Win Scale'
            },
            'datagrams': {
                'mss_bytes': 1440,
                'peer_mss_bytes': 1440,
                'min_mss_bytes': 1440,
                'max_mss_bytes': 1440
            },
            'window_scales': {
                'rcv': 0,
                'snd': 0,
                'request_rcv': 0,
                'request_snd': 0
            },
            'timestamp_option': {
                'recent': 0,
                'recent_age': 0,
                'last_ack_sent': 0
            },
            'sack_blocks': {
                'start': 'none',
                'end': 'none'
            },
            'sack_holes': {
                'start': 'none',
                'end': 'none',
                'dups': 'none',
                'rxmit': 'none'
            },
            'socket_options': 'SO_REUSEADDR, SO_REUSEPORT, SO_NBIO',
            'socket_states': 'SS_ISCONNECTED, SS_PRIV',
            'socket_receive_buffer_states': 'SB_DEL_WAKEUP',
            'socket_send_buffer_states': 'SB_DEL_WAKEUP',
            'socket_receive_buffer': {
                'watermarks': {
                    'low': 1,
                    'high': 32768
                }
            },
            'socket_send_buffer': {
                'watermarks': {
                    'low': 2048,
                    'high': 24576
                },
                'notify_threshold': 0
            },
            'socket_misc_info': {
                'rcv_data_size': 0,
                'so_qlen': 0,
                'so_q0len': 0,
                'so_qlimit': 0,
                'so_error': 0,
                'so_auto_rearm': 1
            },
            'pdu_information': {
                'pdu_buffer': 0,
                'fib_lookup_cache': {
                    'ifh': '0x1000058',
                    'pd_ctx': {
                        'size': 8,
                        'data': '0x0 0xa6fe66ce'
                    }
                },
                'num_label': 0,
                'num_peers_with_authentication': 0
            }
        }
    }
}

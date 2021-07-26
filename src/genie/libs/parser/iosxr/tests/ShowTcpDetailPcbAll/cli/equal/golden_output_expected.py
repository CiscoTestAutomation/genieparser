expected_output = {
    'pcb_address': {
        '0x00007f553800d8f8': {
            'connection_state': 'ESTAB',
            'io_status': 0,
            'socket_status': 0,
            'established_datetime': 'Mon Jul 12 09:44:25 2021',
            'tcp_connection_data': {
                'PCB': '0x00007f553800d8f8',
                'SO': '0x7f5538008698',
                'TCPCB': '0x7f5538008b58',
                'VRFID': '0x60000000',
                'pak_prio': 'Medium',
                'TOS': 192,
                'TTL': 1,
                'Hash_index': 26,
                'local_host': '2000:108:10::1',
                'local_port': 179,
                'local_app_pid': 11298,
                'foreign_host': '2000:108:10::2',
                'foreign_port': 56357,
                'local_api': {
                    'PID': 11298,
                    'Instance': 1,
                    'SPL_ID': 0
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
            'sequence_numbers': {
                'iss': 2552699488,
                'snduna': 2552699622,
                'sndnxt': 2552699622,
                'sndmax': 2552699622,
                'sndwnd': 32739,
                'sndcwnd': 2880,
                'irs': 3293391238,
                'rcvnxt': 3293391391,
                'rcvwnd': 32701,
                'rcvadv': 3293424092,
            },
            'round_trip_delay': {
                'SRTT_ms': 34,
                'RTTO_ms': 300,
                'RTV_ms': 208,
                'KRTT_ms': 0,
                'minRTT_ms': 11,
                'maxRTT_ms': 202
            },
            'times': {
                'ACK_hold_ms': 200,
                'Keepalive_sec': 0,
                'SYN_waittime_sec': 30,
                'Giveup_ms': 0,
                'Retransmission_retries': 0,
                'Retransmit_forever': False,
                'Connect_retries_remaining': 0,
                'connect_retry_interval_sec': 0
            },
            'flags': {
                'State': 'none',
                'Feature': 'Win Scale, Nagle',
                'Request': 'Win Scale'
            },
            'Datagrams': {
                'MSS_bytes': 1440,
                'peer_MSS_bytes': 1440,
                'min_MSS_bytes': 1440,
                'max_MSS_bytes': 1440
            },
            'Window_Scales': {
                'RCV': 0,
                'SND': 0,
                'Request_RCV': 0,
                'Request_SND': 0
            },
            'Timestamp_option': {
                'recent': 0,
                'recent_age': 0,
                'last_ACK_sent': 0
            },
            'Sack_Blocks': {
                'start': 'none',
                'end': 'none'
            },
            'Sack_Holes': {
                'start': 'none',
                'end': 'none',
                'dups': 'none',
                'rxmit': 'none'
            },
            'Socket_options': {
                'SO_REUSEADDR': True,
                'SO_REUSEPORT': True,
                'SO_NBIO': True
            },
            'Socket_States': {
                'SS_ISCONNECTED': True,
                'SS_PRIV': True
            },
            'Socket_Receive_Buffer_States': {
                'SB_DEL_WAKEUP': True
            },
            'Socket_Send_Buffer_States': {
                'SB_DEL_WAKEUP': True
            },
            'Socket_Receive_Buffer': {
                'watermarks': {
                    'low': 2048,
                    'high': '32768'
                }
            },
            'Socket_Send_Buffer': {
                'watermarks': {
                    'low': 2048,
                    'high': '24576'
                },
                'notify_threshold': 0
            },
            'Socket_Misc_Info': {
                'RCV_data_size': 0,
                'SO_QLen': 0,
                'SO_Q0Len': 0,
                'SO_QLimit': 0,
                'SO_Error': 0,
                'SO_Auto_Rearm': 1
            },
            'PDU_Information': {
                'PDU_Buffer': 0,
                'FIB_Lookup_Cache': {
                    'IFH': '0x1000058',
                    'PD_CTX': {
                        'Size': 8,
                        'Data': '0x0 0xa6fe66ce'
                    },
                    'Num_Labels': 0,
                    'Label_Stack': 0
                },
                'Num_Peers_With_Authentication': 0
            }
        }
    }
}
expected_output = {
    "vrf": {
        "local_ldp_identifier": "17.17.17.17:0",
        "vrfs": [
            {
                "vrf_name": "default",
                "interfaces": [
                    {
                        "interface": "HundredGigE0/0/0/0",
                        "xmit": 'True',
                        "recv": 'True',
                        "vrf_hex": "0x60000000",
                        "source_ip_addr": "10.10.10.1",
                        "transport_ip_addr": "17.17.17.17",
                        "hello_interval_ms": '5000',
                        "hello_due_time_ms": '563',
                        "quick_start": "enabled",
                        "ldp_id": {
                            "network_addr": "141.141.141.141:0",
                            "ldp_entries": [
                                {
                                    "source_ip_addr": "10.10.10.2",
                                    "transport_ip_addr": "141.141.141.141",
                                    "holdtime_sec": '15',
                                    "proposed_local": '15',
                                    "proposed_peer": '15',
                                    "expiring_in": '10.4',
                                    "established_date": "Mar 11 09:41:07.477",
                                    "established_elapsed": "00:33:46",
                                    "last_session_connection_failures": [
                                        {
                                            "timestamp": "Jan  4 05:20:34.814",
                                            "reason": "User cleared session manually",
                                            "last_up_for": "00:06:56"
                                        },
                                        {
                                            "timestamp": "Jan  4 05:28:48.641",
                                            "reason": "User cleared session manually",
                                            "last_up_for": "00:08:11"
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "interface": "TenGigE0/2/0/0",
                        "xmit": 'True',
                        "recv": 'False',
                        "vrf_hex": "0x60000000",
                        "source_ip_addr": "100.20.0.1",
                        "transport_ip_addr": "17.17.17.17",
                        "hello_interval_ms": '5000',
                        "hello_due_time_ms": '3400',
                        "quick_start": "enabled"
                    },
                    {
                        "interface": "TenGigE0/2/0/3",
                        "xmit": 'False',
                        "recv": 'True',
                        "vrf_hex": "0x60000000",
                        "source_ip_addr": "100.10.0.1",
                        "transport_ip_addr": "17.17.17.17",
                        "hello_interval_ms": '5000',
                        "hello_due_time_ms": '3600',
                        "quick_start": "enabled",
                        "ldp_id": {
                            "network_addr": "107.107.107.107:0",
                            "ldp_entries": [
                                {
                                    "source_ip_addr": "100.10.0.2",
                                    "transport_ip_addr": "107.107.107.107",
                                    "holdtime_sec": '15',
                                    "proposed_local": '15',
                                    "proposed_peer": '15',
                                    "expiring_in": '10.3',
                                    "established_date": "Mar 11 09:31:57.896",
                                    "established_elapsed": "00:42:55"
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
} 
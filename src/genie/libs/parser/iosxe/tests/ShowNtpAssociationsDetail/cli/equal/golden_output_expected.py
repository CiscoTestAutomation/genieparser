expected_output = {
    "vrf": {
        "default": {
            "associations": {
                "address": {
                    "192.168.255.254": {
                        "local_mode": {
                            "client": {
                                "isconfigured": {
                                    "True": {
                                        "ip_type": "ipv4",
                                        "selected": False,
                                        "unsynced": False,
                                        "address": "192.168.255.254",
                                        "isconfigured": True,
                                        "authenticated": True,
                                        "sane": False,
                                        "valid": False,
                                        "master": False,
                                        "stratum": 3,
                                        "refid": "172.16.255.254",
                                        "input_time": "DBAB02D6.9E354130 (16:08:06.618 EST Fri Oct 14 2016)",
                                        "peer_interface": "172.16.255.254",
                                        "poll": "512",
                                        "vrf": "default",
                                        "local_mode": "client",
                                        "peer": {
                                            "172.16.255.254": {
                                                "local_mode": {
                                                    "server": {
                                                        "poll": 512,
                                                        "local_mode": "server",
                                                    }
                                                }
                                            }
                                        },
                                        "root_delay_msec": "0.00",
                                        "root_disp": "14.52",
                                        "reach": "377",
                                        "sync_dist": "28.40",
                                        "delay_msec": "0.00",
                                        "offset_msec": "0.0000",
                                        "dispersion": "7.23",
                                        "jitter_msec": "0.97",
                                        "precision": "2**10",
                                        "version": 4,
                                        "assoc_name": "192.168.255.254",
                                        "assoc_id": 62758,
                                        "ntp_statistics": {
                                            "packet_received": 27,
                                            "packet_sent": 27,
                                            "packet_dropped": 0,
                                        },
                                        "originate_time": "00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)",
                                        "receive_time": "DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)",
                                        "transmit_time": "DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)",
                                        "filtdelay": "0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00",
                                        "filtoffset": "0.00    0.50    0.00    1.00    1.00    1.00    1.00    1.00",
                                        "filterror": "1.95    5.89    9.88   13.89   15.84   17.79   19.74   21.76",
                                        "minpoll": 6,
                                        "maxpoll": 10,
                                    }
                                }
                            }
                        }
                    },
                    "172.16.255.254": {
                        "local_mode": {
                            "client": {
                                "isconfigured": {
                                    "True": {
                                        "ip_type": "ipv4",
                                        "selected": False,
                                        "unsynced": False,
                                        "address": "172.16.255.254",
                                        "isconfigured": True,
                                        "authenticated": True,
                                        "sane": True,
                                        "valid": True,
                                        "master": True,
                                        "stratum": 2,
                                        "refid": "127.127.1.1",
                                        "input_time": "DBAB05B9.753F7E30 (16:20:25.458 EST Fri Oct 14 2016)",
                                        "peer_interface": "127.127.1.1",
                                        "poll": "512",
                                        "vrf": "default",
                                        "local_mode": "client",
                                        "peer": {
                                            "127.127.1.1": {
                                                "local_mode": {
                                                    "server": {
                                                        "poll": 512,
                                                        "local_mode": "server",
                                                    }
                                                }
                                            }
                                        },
                                        "root_delay_msec": "0.00",
                                        "root_disp": "2.18",
                                        "reach": "177",
                                        "sync_dist": "9.47",
                                        "delay_msec": "0.00",
                                        "offset_msec": "-1.0000",
                                        "dispersion": "5.64",
                                        "jitter_msec": "0.97",
                                        "precision": "2**10",
                                        "version": 4,
                                        "assoc_name": "172.16.255.254",
                                        "assoc_id": 62756,
                                        "ntp_statistics": {
                                            "packet_received": 38,
                                            "packet_sent": 50,
                                            "packet_dropped": 0,
                                        },
                                        "originate_time": "00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)",
                                        "receive_time": "DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)",
                                        "transmit_time": "DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)",
                                        "filtdelay": "1.00    1.00    1.00    1.00    0.00    1.00    1.00    0.00",
                                        "filtoffset": "-0.50   -0.50   -0.50   -0.50   -1.00   -0.50   -0.50   -1.00",
                                        "filterror": "1.95    2.88    3.81    4.74    5.08    5.11    7.53    8.46",
                                        "minpoll": 6,
                                        "maxpoll": 10,
                                    }
                                }
                            }
                        }
                    },
                }
            }
        }
    }
}

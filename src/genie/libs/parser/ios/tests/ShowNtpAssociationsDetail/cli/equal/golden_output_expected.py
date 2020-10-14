expected_output = {
    "vrf": {
        "default": {
            "associations": {
                "address": {
                    "172.31.32.2": {
                        "local_mode": {
                            "active": {
                                "isconfigured": {
                                    "True": {
                                        "selected": False,
                                        "unsynced": False,
                                        "address": "172.31.32.2",
                                        "isconfigured": True,
                                        "authenticated": False,
                                        "sane": False,
                                        "valid": False,
                                        "master": False,
                                        "stratum": 5,
                                        "refid": "172.31.32.1",
                                        "input_time": "AFE252C1.6DBDDFF2 (00:12:01.428 PDT Mon Jul 5 1993)",
                                        "peer_interface": "172.31.32.1",
                                        "poll": "1024",
                                        "vrf": "default",
                                        "local_mode": "active",
                                        "peer": {
                                            "172.31.32.1": {
                                                "local_mode": {
                                                    "active": {
                                                        "poll": 64,
                                                        "local_mode": "active",
                                                    }
                                                }
                                            }
                                        },
                                        "root_delay_msec": "137.77",
                                        "root_disp": "142.75",
                                        "reach": "376",
                                        "sync_dist": "215.363",
                                        "delay_msec": "4.23",
                                        "offset_msec": "-8.587",
                                        "dispersion": "1.62",
                                        "jitter_msec": "None",
                                        "precision": "2**19",
                                        "version": 4,
                                        "assoc_name": "192.168.1.55",
                                        "assoc_id": 1,
                                        "ntp_statistics": {
                                            "packet_received": 60,
                                            "packet_sent": 60,
                                            "packet_dropped": 0,
                                        },
                                        "originate_time": "AFE252E2.3AC0E887 (00:12:34.229 PDT Tue Oct 4 2011)",
                                        "receive_time": "AFE252E2.3D7E464D (00:12:34.240 PDT Mon Jan 1 1900)",
                                        "transmit_time": "AFE25301.6F83E753 (00:13:05.435 PDT Tue Oct 4 2011)",
                                        "filtdelay": "4.23    4.14    2.41    5.95    2.37    2.33    4.26    4.33",
                                        "filtoffset": "-8.59   -8.82   -9.91   -8.42  -10.51  -10.77  -10.13  -10.11",
                                        "filterror": "0.50    1.48    2.46    3.43    4.41    5.39    6.36    7.34",
                                    }
                                }
                            }
                        }
                    },
                    "192.168.13.33": {
                        "local_mode": {
                            "client": {
                                "isconfigured": {
                                    "True": {
                                        "selected": True,
                                        "unsynced": False,
                                        "address": "192.168.13.33",
                                        "isconfigured": True,
                                        "authenticated": False,
                                        "sane": True,
                                        "valid": True,
                                        "master": False,
                                        "stratum": 3,
                                        "refid": "192.168.1.111",
                                        "input_time": "AFE24F0E.14283000 (23:56:14.078 PDT Sun Jul 4 1993)",
                                        "peer_interface": "192.168.1.111",
                                        "poll": "128",
                                        "vrf": "default",
                                        "local_mode": "client",
                                        "peer": {
                                            "192.168.1.111": {
                                                "local_mode": {
                                                    "server": {
                                                        "poll": 128,
                                                        "local_mode": "server",
                                                    }
                                                }
                                            }
                                        },
                                        "root_delay_msec": "83.72",
                                        "root_disp": "217.77",
                                        "reach": "377",
                                        "sync_dist": "264.633",
                                        "delay_msec": "4.07",
                                        "offset_msec": "3.483",
                                        "dispersion": "2.33",
                                        "jitter_msec": "None",
                                        "precision": "2**6",
                                        "version": 3,
                                        "assoc_name": "myserver",
                                        "assoc_id": 2,
                                        "ntp_statistics": {
                                            "packet_received": 0,
                                            "packet_sent": 0,
                                            "packet_dropped": 0,
                                        },
                                        "originate_time": "AFE252B9.713E9000 (00:11:53.442 PDT Tue Oct 4 2011)",
                                        "receive_time": "AFE252B9.7124E14A (00:11:53.441 PDT Mon Jan 1 1900)",
                                        "transmit_time": "AFE252B9.6F625195 (00:11:53.435 PDT Mon Jan 1 1900)",
                                        "filtdelay": "6.47    4.07    3.94    3.86    7.31    7.20    9.52    8.71",
                                        "filtoffset": "3.63    3.48    3.06    2.82    4.51    4.57    4.28    4.59",
                                        "filterror": "0.00    1.95    3.91    4.88    5.84    6.82    7.80    8.77",
                                    }
                                }
                            }
                        }
                    },
                    "192.168.13.57": {
                        "local_mode": {
                            "client": {
                                "isconfigured": {
                                    "True": {
                                        "selected": False,
                                        "unsynced": False,
                                        "address": "192.168.13.57",
                                        "isconfigured": True,
                                        "authenticated": False,
                                        "sane": True,
                                        "valid": True,
                                        "master": True,
                                        "stratum": 3,
                                        "refid": "192.168.1.111",
                                        "input_time": "AFE252DC.1F2B3000 (00:12:28.121 PDT Mon Jul 5 1993)",
                                        "peer_interface": "192.168.1.111",
                                        "poll": "128",
                                        "vrf": "default",
                                        "local_mode": "client",
                                        "peer": {
                                            "192.168.1.111": {
                                                "local_mode": {
                                                    "server": {
                                                        "poll": 128,
                                                        "local_mode": "server",
                                                    }
                                                }
                                            }
                                        },
                                        "root_delay_msec": "125.50",
                                        "root_disp": "115.80",
                                        "reach": "377",
                                        "sync_dist": "186.157",
                                        "delay_msec": "7.86",
                                        "offset_msec": "11.176",
                                        "dispersion": "3.62",
                                        "jitter_msec": "None",
                                        "precision": "2**6",
                                        "version": 2,
                                        "assoc_name": "myserver",
                                        "assoc_id": 2,
                                        "ntp_statistics": {
                                            "packet_received": 0,
                                            "packet_sent": 0,
                                            "packet_dropped": 0,
                                        },
                                        "originate_time": "AFE252DE.77C29000 (00:12:30.467 PDT Tue Oct 4 2011)",
                                        "receive_time": "AFE252DE.7B2AE40B (00:12:30.481 PDT Mon Jan 1 1900)",
                                        "transmit_time": "AFE252DE.6E6D12E4 (00:12:30.431 PDT Mon Jan 1 1900)",
                                        "filtdelay": "49.21    7.86    8.18    8.80    4.30    4.24    7.58    6.42",
                                        "filtoffset": "11.30   11.18   11.13   11.28    8.91    9.09    9.27    9.57",
                                        "filterror": "0.00    1.95    3.91    4.88    5.78    6.76    7.74    8.71",
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

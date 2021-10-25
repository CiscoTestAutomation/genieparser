expected_output = {
    "tunnel": {
        "150.0.5.1": {
            "remote": {
                "150.0.0.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "20.0.0.20",
                    "local_color": "public-internet",
                    "remote_color": "bronze",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059454,
                        "tx_octets": 92817016,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059447,
                        "rx_octets": 128856766,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.2.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "22.0.0.22",
                    "local_color": "public-internet",
                    "remote_color": "private1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059024,
                        "tx_octets": 92797174,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1058998,
                        "rx_octets": 128802634,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.4.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 7988,
                    "remote_sys_ip": "24.0.0.24",
                    "local_color": "public-internet",
                    "remote_color": "private2",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 950,
                        "tx_octets": 108596,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 946,
                        "rx_octets": 137632,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.6.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "26.0.0.26",
                    "local_color": "public-internet",
                    "remote_color": "green",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1041336,
                        "tx_octets": 91400333,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1041327,
                        "rx_octets": 126685077,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.7.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "27.0.0.27",
                    "local_color": "public-internet",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1035334,
                        "tx_octets": 90884064,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1029341,
                        "rx_octets": 125244705,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.8.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "28.0.0.28",
                    "local_color": "public-internet",
                    "remote_color": "custom1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059202,
                        "tx_octets": 92812920,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059195,
                        "rx_octets": 128825798,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.10.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "30.0.0.30",
                    "local_color": "public-internet",
                    "remote_color": "mpls",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059113,
                        "tx_octets": 92803953,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059101,
                        "rx_octets": 128815148,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.40.4": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "140.0.1.140",
                    "local_color": "public-internet",
                    "remote_color": "gold",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 164808143,
                        "tx_octets": 20982793221,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 384304261,
                        "rx_octets": 408052008664,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.0.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "20.0.0.20",
                    "local_color": "public-internet",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059462,
                        "tx_octets": 92817487,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059456,
                        "rx_octets": 128858000,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.2.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "22.0.0.22",
                    "local_color": "public-internet",
                    "remote_color": "private2",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1058991,
                        "tx_octets": 92794420,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1058965,
                        "rx_octets": 128798821,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.4.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 5294,
                    "remote_sys_ip": "24.0.0.24",
                    "local_color": "public-internet",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 697,
                        "tx_octets": 85027,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 697,
                        "rx_octets": 108648,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.6.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "26.0.0.26",
                    "local_color": "public-internet",
                    "remote_color": "custom1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1041254,
                        "tx_octets": 91393239,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1041243,
                        "rx_octets": 126674556,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.7.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "27.0.0.27",
                    "local_color": "public-internet",
                    "remote_color": "blue",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1035480,
                        "tx_octets": 90896032,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1029500,
                        "rx_octets": 125264360,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.40.4": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "140.0.1.140",
                    "local_color": "public-internet",
                    "remote_color": "mpls",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 213927741,
                        "tx_octets": 27306030282,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 386543587,
                        "rx_octets": 410122221452,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                }
            }
        },
        "151.0.5.1": {
            "remote": {
                "150.0.0.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "20.0.0.20",
                    "local_color": "silver",
                    "remote_color": "bronze",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059493,
                        "tx_octets": 92820300,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059480,
                        "rx_octets": 128860565,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.2.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "22.0.0.22",
                    "local_color": "silver",
                    "remote_color": "private1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1058922,
                        "tx_octets": 92789312,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1058895,
                        "rx_octets": 128790085,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.4.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 7987,
                    "remote_sys_ip": "24.0.0.24",
                    "local_color": "silver",
                    "remote_color": "private1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 952,
                        "tx_octets": 106082,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 952,
                        "rx_octets": 138338,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.6.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "26.0.0.26",
                    "local_color": "silver",
                    "remote_color": "green",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1041144,
                        "tx_octets": 91384269,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1041132,
                        "rx_octets": 126647457,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.7.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "27.0.0.27",
                    "local_color": "silver",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1035427,
                        "tx_octets": 90891642,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1029431,
                        "rx_octets": 125257715,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.8.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "28.0.0.28",
                    "local_color": "silver",
                    "remote_color": "custom1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059168,
                        "tx_octets": 92809811,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059159,
                        "rx_octets": 128821926,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.10.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "30.0.0.30",
                    "local_color": "silver",
                    "remote_color": "mpls",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059132,
                        "tx_octets": 92805650,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059121,
                        "rx_octets": 128817345,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "150.0.40.4": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "140.0.1.140",
                    "local_color": "silver",
                    "remote_color": "gold",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 217959116,
                        "tx_octets": 27709918538,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 294464442,
                        "rx_octets": 312188658436,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.0.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "20.0.0.20",
                    "local_color": "silver",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1059460,
                        "tx_octets": 92817462,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1059451,
                        "rx_octets": 128857288,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.2.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "22.0.0.22",
                    "local_color": "silver",
                    "remote_color": "private2",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1058946,
                        "tx_octets": 92790641,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1058918,
                        "rx_octets": 128793419,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.4.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 5294,
                    "remote_sys_ip": "24.0.0.24",
                    "local_color": "silver",
                    "remote_color": "silver",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 698,
                        "tx_octets": 86006,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 697,
                        "rx_octets": 108641,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.6.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "26.0.0.26",
                    "local_color": "silver",
                    "remote_color": "custom1",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1041228,
                        "tx_octets": 91391178,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1041215,
                        "rx_octets": 126671232,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.7.1": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "27.0.0.27",
                    "local_color": "silver",
                    "remote_color": "blue",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 1035492,
                        "tx_octets": 90897043,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 1029523,
                        "rx_octets": 125265880,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                },
                "151.0.40.4": {
                    "protocol": "ipsec",
                    "src_port": 12346,
                    "dst_port": 12346,
                    "remote_sys_ip": "140.0.1.140",
                    "local_color": "silver",
                    "remote_color": "mpls",
                    "tunnel_mtu": 1438,
                    "tx": {
                        "tx_pkts": 241915244,
                        "tx_octets": 30746502240,
                        "tx_ipv4_mcast_pkts": 0,
                        "tx_ipv4_mcast_octets": 0
                    },
                    "rx": {
                        "rx_pkts": 332023413,
                        "rx_octets": 352981285350,
                        "rx_ipv4_mcast_pkts": 0,
                        "rx_ipv4_mcast_octets": 0
                    },
                    "tcp_mss_adjust": 1358,
                    "ipv6_tx": {
                        "ipv6_tx_pkts": 0,
                        "ipv6_tx_octets": 0
                    },
                    "ipv6_rx": {
                        "ipv6_rx_pkts": 0,
                        "ipv6_rx_octets": 0
                    }
                }
            }
        }
    }
}

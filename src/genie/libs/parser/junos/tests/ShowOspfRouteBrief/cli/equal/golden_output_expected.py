expected_output = {
    "ospf-route-information": {
        "ospf-topology-route-table": {
            "ospf-route": [
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.36.3.3",
                            "interface-cost": "1201",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Router",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.100.5.5",
                            "interface-cost": "1200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Router",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.19.198.239",
                            "interface-cost": "1000",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Router",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.34.2.250",
                            "interface-cost": "200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.34.2.251",
                            "interface-cost": "205",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.196.241",
                            "interface-cost": "1200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Router",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.240",
                            "interface-cost": "100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.241",
                            "interface-cost": "105",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.189.5.253",
                            "interface-cost": "5",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "192.168.36.119",
                            "interface-cost": "10100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "192.168.36.120",
                            "interface-cost": "10100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "AS BR",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "0.0.0.0/0",
                            "interface-cost": "101",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Ext1",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.1.0.0/24",
                            "interface-cost": "20",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Ext2",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.36.3.3/32",
                            "interface-cost": "1202",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.16.0.0/30",
                            "interface-cost": "1200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.100.5.5/32",
                            "interface-cost": "1201",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.100.5.5/32",
                            "interface-cost": "1201",
                            "next-hop-type": "Spring",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup SPRING",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.19.198.24/30",
                            "interface-cost": "1000",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.19.198.28/30",
                            "interface-cost": "1005",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.19.198.239/32",
                            "interface-cost": "1001",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.19.198.239/32",
                            "interface-cost": "1001",
                            "next-hop-type": "Spring",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup SPRING",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.174.132.237/32",
                            "interface-cost": "150",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Ext1",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.34.2.200/30",
                            "interface-cost": "205",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.34.2.250/32",
                            "interface-cost": "200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.34.2.250/32",
                            "interface-cost": "200",
                            "next-hop-type": "Spring",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.34.2.251/32",
                            "interface-cost": "205",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.34.2.251/32",
                            "interface-cost": "205",
                            "next-hop-type": "Spring",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.15.0.0/30",
                            "interface-cost": "1001",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.64.0.0/30",
                            "interface-cost": "1201",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.55.0.0/24",
                            "interface-cost": "100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/3.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.196.212/30",
                            "interface-cost": "1200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.196.216/30",
                            "interface-cost": "1205",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.196.241/32",
                            "interface-cost": "1201",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.169.196.241/32",
                            "interface-cost": "1201",
                            "next-hop-type": "Spring",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup SPRING",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.16/30",
                            "interface-cost": "105",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.32/30",
                            "interface-cost": "225",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.120/30",
                            "interface-cost": "100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.128/30",
                            "interface-cost": "125",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.156/30",
                            "interface-cost": "200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.240/32",
                            "interface-cost": "100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.169.14.240/32",
                            "interface-cost": "100",
                            "next-hop-type": "Spring",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup SPRING",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.241/32",
                            "interface-cost": "105",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.169.14.241/32",
                            "interface-cost": "105",
                            "next-hop-type": "Spring",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.242/32",
                            "interface-cost": "100",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.169.14.243/32",
                            "interface-cost": "105",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.189.5.92/30",
                            "interface-cost": "5",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.189.5.252/32",
                            "interface-cost": "0",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "lo0.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.189.5.252/32",
                            "interface-cost": "0",
                            "next-hop-type": "Spring",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "lo0.0"}
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "10.189.5.253/32",
                            "interface-cost": "5",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                        {
                            "address-prefix": "10.189.5.253/32",
                            "interface-cost": "5",
                            "next-hop-type": "Spring",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        },
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "192.168.220.0/30",
                            "interface-cost": "1200",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "192.168.36.119/32",
                            "interface-cost": "10101",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "192.168.36.120/32",
                            "interface-cost": "10101",
                            "next-hop-type": "IP",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "2567",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "2567 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "2568",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "2568 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "167966",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "167966 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "167967",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "167967 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "28985",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "28985 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "28986",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "28986 (S=0)",
                            "interface-cost": "0",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "17000",
                            "interface-cost": "1201",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16051",
                            "interface-cost": "100",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16051 (S=0)",
                            "interface-cost": "100",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16052",
                            "interface-cost": "105",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16061",
                            "interface-cost": "200",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16062",
                            "interface-cost": "205",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16063",
                            "interface-cost": "1201",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.169.14.121"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16072",
                            "interface-cost": "5",
                            "next-hop-type": "Mpls",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.189.5.94"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16073",
                            "interface-cost": "1001",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
                {
                    "ospf-route-entry": [
                        {
                            "address-prefix": "16073 (S=0)",
                            "interface-cost": "1001",
                            "next-hop-type": "Mpls",
                            "ospf-backup-next-hop": {
                                "ospf-backup-next-hop-address": "10.189.5.94",
                                "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                "ospf-backup-next-hop-type": "Bkup MPLS",
                            },
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.19.198.26"
                                },
                                "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                            },
                            "route-path-type": "Intra",
                            "route-type": "Network",
                        }
                    ]
                },
            ]
        }
    }
}

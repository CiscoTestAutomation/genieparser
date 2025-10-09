expected_output= {
    "zone_pair": {
        "new-trusted-untrusted": {
            "service_policy_inspect": {
                "firewall_policy": {
                    "class_map": {
                        "class_1": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol 802-11-iapp",
                                "protocol ace-svr",
                                "protocol aol",
                                "protocol appleqtc",
                                "protocol bgp",
                                "protocol biff",
                                "protocol bootpc",
                                "protocol bootps"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_2": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol cddbp",
				"protocol cifs",
				"protocol cisco-fna",
				"protocol cisco-net-mgmt",
				"protocol cisco-svcs",
				"protocol cisco-sys",
				"protocol cisco-tdp",
				"protocol cisco-tna"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_3": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol citrix",
				"protocol citriximaclient",
				"protocol clp",
				"protocol creativepartnr",
				"protocol creativeserver",
				"protocol cuseeme",
				"protocol daytime",
				"protocol dbase"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_4": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol dbcontrol_agent",
				"protocol ddns-v3",
				"protocol dhcp-failover",
				"protocol discard",
				"protocol dns",
				"protocol dnsix",
				"protocol echo",
				"protocol entrust-svc-handler"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_5": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol entrust-svcs",
				"protocol exec",
				"protocol fcip-port",
				"protocol finger",
				"protocol ftps",
				"protocol gdoi",
				"protocol giop",
				"protocol ftp"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_6": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol gopher",
				"protocol gtpv0",
				"protocol gtpv1",
				"protocol h225ras",
				"protocol h323",
				"protocol h323callsigalt",
				"protocol hp-alarm-mgr",
				"protocol hp-collector"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_7": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol hp-managed-node",
				"protocol hsrp",
				"protocol http",
				"protocol https",
				"protocol ica",
				"protocol icabrowser",
				"protocol icmp",
				"protocol ident"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_8": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol igmpv3lite",
				"protocol imap",
				"protocol imap3",
				"protocol imaps",
				"protocol ipass",
				"protocol ipsec-msft",
				"protocol ipx",
				"protocol irc"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_9": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol irc-serv",
				"protocol ircs",
				"protocol ircu",
				"protocol isakmp",
				"protocol iscsi",
				"protocol iscsi-target",
				"protocol kazaa",
				"protocol kerberos"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_10": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol kermit",
				"protocol l2tp",
				"protocol ldap",
				"protocol ldap-admin",
				"protocol ldaps",
				"protocol login",
				"protocol lotusmtap",
				"protocol lotusnote"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_11": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol mgcp",
				"protocol microsoft-ds",
				"protocol ms-cluster-net",
				"protocol ms-dotnetster",
				"protocol ms-sna",
				"protocol ms-sql",
				"protocol ms-sql-m",
				"protocol msexch-routing"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_12": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol msnmsgr",
				"protocol msrpc",
				"protocol mysql",
				"protocol n2h2server",
				"protocol ncp",
				"protocol net8-cman",
				"protocol netbios-dgm",
				"protocol netbios-ns"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_13": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol netbios-ssn",
				"protocol netshow",
				"protocol netstat",
				"protocol nfs",
				"protocol nntp",
				"protocol ntp",
				"protocol oem-agent",
				"protocol oracle"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_14": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol oracle-em-vp",
				"protocol oraclenames",
				"protocol orasrv",
				"protocol pcanywheredata",
				"protocol pcanywherestat",
				"protocol pop3",
				"protocol pop3s",
				"protocol pptp"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_15": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol pwdgen",
				"protocol qmtp",
				"protocol r-winsock",
				"protocol radius",
				"protocol rdb-dbs-disp",
				"protocol realmedia",
				"protocol realsecure",
				"protocol router"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_16": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol rsvd",
				"protocol rsvp-encap",
				"protocol rsvp_tunnel",
				"protocol rtc-pm-port",
				"protocol rtelnet",
				"protocol rtsp",
				"protocol send",
				"protocol shell"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_17": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol sip",
				"protocol sip-tls",
				"protocol skinny",
				"protocol sms",
				"protocol smtp",
				"protocol snmp",
				"protocol snmptrap",
				"protocol socks"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_18": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol sql-net",
				"protocol sqlserv",
				"protocol sqlsrv",
				"protocol ssh",
				"protocol sshell",
				"protocol ssp",
				"protocol streamworks",
				"protocol stun"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_19": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol sunrpc",
				"protocol syslog",
				"protocol syslog-conn",
				"protocol tacacs",
				"protocol tacacs-ds",
				"protocol tarantella",
				"protocol tcp",
				"protocol telnet"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_20": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol telnets",
				"protocol tftp",
				"protocol time",
				"protocol timed",
				"protocol tr-rsrb",
				"protocol ttc",
				"protocol udp",
				"protocol uucp"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class_21": {
                            "class_map_type": "match-any",
                            "class_map_match": [
				"protocol vdolive",
				"protocol vqp",
				"protocol webster",
				"protocol who",
				"protocol wins",
				"protocol x11",
				"protocol xdmcp",
				"protocol ymsgr"
                                ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any"
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

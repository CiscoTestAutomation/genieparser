expected_output = {
    'current_state': "Ready",
    'instances': {
        1: {
            'config_change_time': "2025-04-02 08:03:05",
            'xpaths_seen': 6,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect",
                    'operation': "Delete"
                },
                3: {
                    'path': "/ios:native/ios:radius/ios-aaa:server[ios-aaa:id='10.24.42.72_1812_0']/ios-aaa:tls/ios-aaa:port",
                    'operation': "Delete"
                },
                4: {
                    'path': "/ios:native/ios:aaa/ios-aaa:accounting/ios-aaa:jitter/ios-aaa:maximum",
                    'operation': "Delete"
                },
                5: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv4/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                },
                6: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv6/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                }
            }
        },
        2: {
            'config_change_time': "2025-04-01 22:22:38",
            'xpaths_seen': 59,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/1']",
                    'operation': "Create"
                },
                3: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/10']",
                    'operation': "Create"
                },
                4: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/11']",
                    'operation': "Create"
                },
                5: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/12']",
                    'operation': "Create"
                },
                6: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/13']",
                    'operation': "Create"
                },
                7: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/14']",
                    'operation': "Create"
                },
                8: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/15']",
                    'operation': "Create"
                },
                9: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/16']",
                    'operation': "Create"
                },
                10: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/17']",
                    'operation': "Create"
                }
            }
        },
        3: {
            'config_change_time': "2025-04-01 22:21:08",
            'xpaths_seen': 8,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect",
                    'operation': "Delete"
                },
                3: {
                    'path': "/ios:native/ios:radius/ios-aaa:server[ios-aaa:id='10.24.42.72_1812_0']/ios-aaa:tls/ios-aaa:port",
                    'operation': "Delete"
                },
                4: {
                    'path': "/ios:native/ios:policy/ios-policy:policy-map[ios-policy:name='qos_egress']/ios-policy:class",
                    'operation': "Replace"
                },
                5: {
                    'path': "/ios:native/ios:aaa/ios-aaa:accounting/ios-aaa:jitter/ios-aaa:maximum",
                    'operation': "Delete"
                },
                6: {
                    'path': "/ios:native/ios:flow/ios-flow:file-export/ios-flow:default/ios-flow:file/ios-flow:max-count",
                    'operation': "Delete"
                },
                7: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv4/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                },
                8: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv6/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                }
            }
        },
        4: {
            'config_change_time': "2025-04-01 17:48:33",
            'xpaths_seen': 1,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios:shutdown",
                    'operation': "Create"
                }
            }
        },
        5: {
            'config_change_time': "2025-04-01 17:48:22",
            'xpaths_seen': 4,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:line/ios:vty[ios:first='0']/ios:exec-timeout/ios:minutes",
                    'operation': "Replace"
                },
                2: {
                    'path': "/ios:native/ios:line/ios:vty[ios:first='0']/ios:exec-timeout/ios:seconds",
                    'operation': "Replace"
                },
                3: {
                    'path': "/ios:native/ios:line/ios:console[ios:first='0']/ios:exec-timeout/ios:minutes",
                    'operation': "Replace"
                },
                4: {
                    'path': "/ios:native/ios:line/ios:console[ios:first='0']/ios:exec-timeout/ios:seconds",
                    'operation': "Replace"
                }
            }
        },
        6: {
            'config_change_time': "2025-04-01 17:30:44",
            'xpaths_seen': 6,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect",
                    'operation': "Delete"
                },
                3: {
                    'path': "/ios:native/ios:radius/ios-aaa:server[ios-aaa:id='10.24.42.72_1812_0']/ios-aaa:tls/ios-aaa:port",
                    'operation': "Delete"
                },
                4: {
                    'path': "/ios:native/ios:aaa/ios-aaa:accounting/ios-aaa:jitter/ios-aaa:maximum",
                    'operation': "Delete"
                },
                5: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv4/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                },
                6: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv6/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                }
            }
        },
        7: {
            'config_change_time': "2025-04-01 17:29:41",
            'xpaths_seen': 10,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:errdisable/ios:detect/ios:cause/ios:loopdetect",
                    'operation': "Delete"
                },
                3: {
                    'path': "/ios:native/ios:logging/ios:console-config/ios:console",
                    'operation': "Replace"
                },
                4: {
                    'path': "/ios:native/ios:snmp-server/ios-snmp:community-config[ios-snmp:name='ikarem']/ios-snmp:permission",
                    'operation': "Replace"
                },
                5: {
                    'path': "/ios:native/ios:radius/ios-aaa:server[ios-aaa:id='10.24.42.72_1812_0']/ios-aaa:tls/ios-aaa:port",
                    'operation': "Delete"
                },
                6: {
                    'path': "/ios:native/ios:policy/ios-policy:policy-map[ios-policy:name='qos_egress']/ios-policy:class",
                    'operation': "Replace"
                },
                7: {
                    'path': "/ios:native/ios:aaa/ios-aaa:accounting/ios-aaa:jitter/ios-aaa:maximum",
                    'operation': "Delete"
                },
                8: {
                    'path': "/ios:native/ios:flow/ios-flow:file-export/ios-flow:default/ios-flow:file/ios-flow:max-count",
                    'operation': "Delete"
                },
                9: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv4/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                },
                10: {
                    'path': "/ios:native/ios-uac:uplink/ios-uac:ipv6/ios-uac:interface/ios-uac:vlan",
                    'operation': "Delete"
                }
            }
        }
    }
}

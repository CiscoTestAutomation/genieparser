

expected_output = {
    'vpn_id':{
        2:{
            'mac_address':{
                '0012.0001.0002':{
                    'encap':'SRv6',
                    'ip_address':'::',
                    'next_hop':'Bundle-Ether1.2',
                    'label':0,
                    'sid':'cafe:0:128:e1ab::',
                    'sid_flags':0,
                    'endpt_behavior':67,
                    'ethernet_tag':0,
                    'multipaths_resolved':'False',
                    'multipaths_internal_label':0,
                    'local_static':'Yes',
                    'remote_static':'No',
                    'local_ethernet_segment':'0012.1212.1212.1212.1212',
                    'remote_ethernet_segment':'0000.0000.0000.0000.0000',
                    'local_sequence_number':0,
                    'remote_sequence_number':0,
                    'local_encapsulation':'SRv6',
                    'remote_encapsulation':'N/A',
                    'local_e_tree':'Root',
                    'remote_e_tree':'Root',
                    'remote_matching_e_tree_rt':'No',
                    'local_ac_id':'0x2',
                    'remote_ac_id':'0x0',
                    'esi_port_key':'5dc0',
                    'source':'Local',
                    'flush_requested':0,
                    'flush_received':0,
                    'soo_nexthop':'::',
                    'ext_flags':'0x00000000',
                    'bp_xcid':'0xa0000002',
                    'mac_state':'Local',
                    'mac_producers':'0x2 (Best: 0x2)',
                    'local_router_mac':'0000.0000.0000',
                    'l3_label':0,
                    'object':{
                        'EVPN MAC':{
                            'base_info':{
                                'version':'0xdbdb0008',
                                'flags':'0x8024100',
                                'type':8,
                                'reserved':0
                            },
                            'num_events':5,
                            'event_history':{
                                1:{
                                    'time':'Feb 28 01:08:42.112',
                                    'event':'Create',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                2:{
                                    'time':'Feb 28 01:08:42.112',
                                    'event':'Got L2RIB update',
                                    'flag_1':'00024000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                3:{
                                    'time':'Feb 28 01:08:42.112',
                                    'event':'Advertise to BGP',
                                    'flag_1':'08226190',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                4:{
                                    'time':'Feb 28 01:08:42.112',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000000',
                                    'flag_2':'00010000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                5:{
                                    'time':'Feb 28 01:08:42.112',
                                    'event':'Encode NLRI',
                                    'flag_1':'08226190',
                                    'flag_2':'08000000',
                                    'code_1':'M',
                                    'code_2':'-'
                                }
                            }
                        }
                    }
                },
                '0012.0002.0002':{
                    'encap':'SRv6',
                    'ip_address':'::',
                    'next_hop':'Bundle-Ether1.2',
                    'label':0,
                    'sid':'cafe:0:128:e1ab::',
                    'sid_flags':0,
                    'endpt_behavior':67,
                    'ethernet_tag':0,
                    'multipaths_resolved':'False',
                    'multipaths_internal_label':0,
                    'local_static':'No',
                    'remote_static':'No',
                    'local_ethernet_segment':'0012.1212.1212.1212.1212',
                    'remote_ethernet_segment':'0000.0000.0000.0000.0000',
                    'local_sequence_number':1,
                    'remote_sequence_number':0,
                    'local_encapsulation':'SRv6',
                    'remote_encapsulation':'N/A',
                    'local_e_tree':'Root',
                    'remote_e_tree':'Root',
                    'remote_matching_e_tree_rt':'No',
                    'local_ac_id':'0x2',
                    'remote_ac_id':'0x2',
                    'esi_port_key':'5dc0',
                    'source':'Local',
                    'flush_requested':0,
                    'flush_received':0,
                    'soo_nexthop':'::',
                    'ext_flags':'0x00000000',
                    'bp_xcid':'0xa0000002',
                    'mac_state':'Local',
                    'mac_producers':'0x1 (Best: 0x1)',
                    'local_router_mac':'0000.0000.0000',
                    'l3_label':0,
                    'object':{
                        'EVPN MAC':{
                            'base_info':{
                                'version':'0xdbdb0008',
                                'flags':'0x8004500',
                                'type':8,
                                'reserved':0
                            },
                            'num_events':16,
                            'event_history':{
                                6:{
                                    'time':'Feb 28 01:08:59.136',
                                    'event':'Got BGP upd/del',
                                    'flag_1':'00ff0102',
                                    'flag_2':'00000001',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                7:{
                                    'time':'Feb 28 01:08:59.136',
                                    'event':'Modify Redundant',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                8:{
                                    'time':'Feb 28 01:08:59.136',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000002',
                                    'flag_2':'00030003',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                9:{
                                    'time':'Feb 28 01:08:59.136',
                                    'event':'L2RIB Download',
                                    'flag_1':'0a000005',
                                    'flag_2':'01000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                10:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Remote MAC become local',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                11:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Modify',
                                    'flag_1':'00102899',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                12:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Advertise to BGP',
                                    'flag_1':'083c6590',
                                    'flag_2':'40000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                13:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Got L2RIB update',
                                    'flag_1':'083c6590',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                14:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Advertise to BGP',
                                    'flag_1':'083c6590',
                                    'flag_2':'40000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                15:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000000',
                                    'flag_2':'00050003',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                16:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Encode NLRI',
                                    'flag_1':'083c6590',
                                    'flag_2':'08010000',
                                    'code_1':'M',
                                    'code_2':'-'
                                },
                                17:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Delete',
                                    'flag_1':'00000001',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                18:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Advertise to BGP',
                                    'flag_1':'09206590',
                                    'flag_2':'40000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                19:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000004',
                                    'flag_2':'00010005',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                20:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'L2RIB Download',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                21:{
                                    'time':'Feb 28 01:08:59.264',
                                    'event':'Encode NLRI',
                                    'flag_1':'08206590',
                                    'flag_2':'08010000',
                                    'code_1':'M',
                                    'code_2':'-'
                                }
                            }
                        }
                    }
                },
                '0034.0001.0002':{
                    'encap':'SRv6',
                    'ip_address':'::',
                    'next_hop':'3.3.3.3',
                    'label':'IMP-NULL',
                    'sid':'cafe:0:300:e002::',
                    'sid_flags':0,
                    'endpt_behavior':67,
                    'sid_struct':{
                        'block':32,
                        'node':16,
                        'func':16,
                        'arg':0
                    },
                    'transposition':{
                        'len':16,
                        'offset':48
                    },
                    'ethernet_tag':0,
                    'multipaths_resolved':'True',
                    'local_static':'No',
                    'remote_static':'Yes',
                    'local_ethernet_segment':'0000.0000.0000.0000.0000',
                    'remote_ethernet_segment':'0034.3434.3434.3434.3434',
                    'local_sequence_number':0,
                    'remote_sequence_number':0,
                    'local_encapsulation':'N/A',
                    'remote_encapsulation':'SRv6',
                    'local_e_tree':'Root',
                    'remote_e_tree':'Root',
                    'remote_matching_e_tree_rt':'No',
                    'local_ac_id':'0x0',
                    'remote_ac_id':'0x2',
                    'esi_port_key':'0',
                    'source':'Remote',
                    'flush_requested':0,
                    'flush_received':0,
                    'soo_nexthop':'3.3.3.3',
                    'ext_flags':'0x00000000',
                    'bp_xcid':'0xffffffff',
                    'stamped_xcid':'0xffffffff',
                    'mac_state':'Remote',
                    'mac_producers':'0x0 (Best: 0x0)',
                    'local_router_mac':'0000.0000.0000',
                    'l3_label':0,
                    'object':{
                        'EVPN MAC':{
                            'base_info':{
                                'version':'0xdbdb0008',
                                'flags':'0x200c0000',
                                'type':8,
                                'reserved':0
                            },
                            'num_events':3,
                            'event_history':{
                                22:{
                                    'time':'Feb 28 01:42:30.784',
                                    'event':'Create',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                23:{
                                    'time':'Feb 28 01:42:30.784',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000001',
                                    'flag_2':'00020000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                24:{
                                    'time':'Feb 28 01:42:31.040',
                                    'event':'L2RIB Download',
                                    'flag_1':'0a000048',
                                    'flag_2':'11000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                }
                            }
                        }
                    }
                },
                '0034.0002.0002':{
                    'encap':'SRv6',
                    'ip_address':'::',
                    'next_hop':'3.3.3.3',
                    'label':'IMP-NULL',
                    'sid':'cafe:0:300:e002::',
                    'sid_flags':0,
                    'endpt_behavior':67,
                    'sid_struct':{
                        'block':32,
                        'node':16,
                        'func':16,
                        'arg':0
                    },
                    'transposition':{
                        'len':16,
                        'offset':48
                    },
                    'ethernet_tag':0,
                    'multipaths_resolved':'True',
                    'local_static':'No',
                    'remote_static':'No',
                    'local_ethernet_segment':'0000.0000.0000.0000.0000',
                    'remote_ethernet_segment':'0034.3434.3434.3434.3434',
                    'local_sequence_number':0,
                    'remote_sequence_number':0,
                    'local_encapsulation':'N/A',
                    'remote_encapsulation':'SRv6',
                    'local_e_tree':'Root',
                    'remote_e_tree':'Root',
                    'remote_matching_e_tree_rt':'No',
                    'local_ac_id':'0x0',
                    'remote_ac_id':'0x2',
                    'esi_port_key':'0',
                    'source':'Remote',
                    'flush_requested':0,
                    'flush_received':0,
                    'soo_nexthop':'3.3.3.3',
                    'ext_flags':'0x00000000',
                    'bp_xcid':'0xffffffff',
                    'stamped_xcid':'0xffffffff',
                    'mac_state':'Remote',
                    'mac_producers':'0x0 (Best: 0x0)',
                    'local_router_mac':'0000.0000.0000',
                    'l3_label':0,
                    'object':{
                        'EVPN MAC':{
                            'base_info':{
                                'version':'0xdbdb0008',
                                'flags':'0xc0000',
                                'type':8,
                                'reserved':0
                            },
                            'num_events':3,
                            'event_history':{
                                25:{
                                    'time':'Feb 28 01:42:30.144',
                                    'event':'Create',
                                    'flag_1':'00000000',
                                    'flag_2':'00000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                26:{
                                    'time':'Feb 28 01:42:30.144',
                                    'event':'FSM Event (event, state)',
                                    'flag_1':'00000001',
                                    'flag_2':'00020000',
                                    'code_1':'-',
                                    'code_2':'-'
                                },
                                27:{
                                    'time':'Feb 28 01:42:31.040',
                                    'event':'L2RIB Download',
                                    'flag_1':'0a000048',
                                    'flag_2':'01000000',
                                    'code_1':'-',
                                    'code_2':'-'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
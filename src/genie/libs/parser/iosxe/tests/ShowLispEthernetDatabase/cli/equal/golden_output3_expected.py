expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                101: {
                    'eid_table': 'Vlan 101',
                    'lsb': '0x1',
                    'entries': 2,
                    'no_route': 0,
                    'inactive': 0,
                    'do_not_reg': 1,
                    'eid_prefix': {
                        'aabb.cc00.c901/48': {
                            'dyn_eid_name': 'Auto-L2-group-101',
                            'do_not_reg_flag': False,
                            'loc_set': 'RLOC',
                            'uptime': '3d01h',
                            'last_change_time': '3d01h',
                            'domain_id': 'local',
                            'serv_ins_type': 'N/A',
                            'serv_ins_id': 0,
                            'locators': {
                                '11.11.11.11': {
                                    'priority': 10,
                                    'weight': 10,
                                    'src': 'cfg-intf',
                                    'state': 'site-self, reachable'
                                    }
                                }
                            },
                        'aabb.cc80.ca00/48': {
                            'dyn_eid_name': 'Auto-L2-group-101',
                            'do_not_reg_flag': True,
                            'loc_set': 'RLOC',
                            'uptime': '3d01h',
                            'last_change_time': '3d01h',
                            'domain_id': 'local',
                            'serv_ins_type': 'N/A',
                            'serv_ins_id': 0,
                            'locators': {
                                '11.11.11.11': {
                                    'priority': 10,
                                    'weight': 10,
                                    'src': 'cfg-intf',
                                    'state': 'site-self, reachable'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
expected_output = {
    'flow_record_name':{
        'wireless avc basic':{
            'description':'Basic IPv4 Wireless AVC template',
            'no_of_users':0,
            'total_field_space':78,
            'fields':{
                'match_list':[
                    'ipv4 protocol',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'flow direction',
                    'application name',
                    'wireless ssid'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'wireless ap mac address',
                    'wireless client mac address'
                ]
            }
        },
        'wireless avc ipv6 basic':{
            'description':'Basic IPv6 Wireless AVC template',
            'no_of_users':0,
            'total_field_space':102,
            'fields':{
                'match_list':[
                    'ipv6 protocol',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'flow direction',
                    'wireless ssid'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'application name',
                    'wireless ap mac address',
                    'wireless client mac address'
                ]
            }
        },
        'netflow ipv6 app-client-server-stats':{
            'description':'Application client server statistics',
            'no_of_users':0,
            'total_field_space':102,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 protocol',
                    'application name',
                    'connection client ipv6 address',
                    'connection server transport port',
                    'connection server ipv6 address',
                    'flow observation point'
                ],
                'collect_list':[
                    'flow direction',
                    'timestamp absolute first',
                    'timestamp absolute last',
                    'connection initiator',
                    'connection new-connections',
                    'connection server counter packets long',
                    'connection client counter packets long',
                    'connection server counter bytes network long',
                    'connection client counter bytes network long'
                ]
            }
        },
        'netflow ipv6 app-client-server-trans-stats':{
            'description':'Application client-server transaction statistics',
            'no_of_users':0,
            'total_field_space':104,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 protocol',
                    'application name',
                    'connection client transport port',
                    'connection client ipv6 address',
                    'connection server transport port',
                    'connection server ipv6 address',
                    'flow observation point'
                ],
                'collect_list':[
                    'flow direction',
                    'timestamp absolute first',
                    'timestamp absolute last',
                    'connection initiator',
                    'connection new-connections',
                    'connection server counter packets long',
                    'connection client counter packets long',
                    'connection server counter bytes network long',
                    'connection client counter bytes network long'
                ]
            }
        },
        'netflow ipv6 app-stats-input':{
            'description':'Application statistics - input',
            'no_of_users':0,
            'total_field_space':97,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 protocol',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface input',
                    'application name'
                ],
                'collect_list':[
                    'datalink dot1q vlan input',
                    'datalink mac source address input',
                    'datalink mac destination address input',
                    'transport tcp flags',
                    'interface output',
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'netflow ipv6 app-stats-output':{
            'description':'Application statistics - output',
            'no_of_users':0,
            'total_field_space':97,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 protocol',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface output',
                    'application name'
                ],
                'collect_list':[
                    'datalink dot1q vlan output',
                    'datalink mac source address output',
                    'datalink mac destination address output',
                    'transport tcp flags',
                    'interface input',
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'netflow ipv4 app-client-server-stats':{
            'description':'Application client server statistics',
            'no_of_users':0,
            'total_field_space':78,
            'fields':{
                'match_list':[
                    'ipv4 version',
                    'ipv4 protocol',
                    'application name',
                    'connection client ipv4 address',
                    'connection server ipv4 address',
                    'connection server transport port',
                    'flow observation point'
                ],
                'collect_list':[
                    'flow direction',
                    'timestamp absolute first',
                    'timestamp absolute last',
                    'connection initiator',
                    'connection new-connections',
                    'connection server counter packets long',
                    'connection client counter packets long',
                    'connection server counter bytes network long',
                    'connection client counter bytes network long'
                ]
            }
        },
        'netflow ipv4 app-client-server-trans-stats':{
            'description':'Application client-server transaction statistics',
            'no_of_users':0,
            'total_field_space':80,
            'fields':{
                'match_list':[
                    'ipv4 version',
                    'ipv4 protocol',
                    'application name',
                    'connection client ipv4 address',
                    'connection client transport port',
                    'connection server ipv4 address',
                    'connection server transport port',
                    'flow observation point'
                ],
                'collect_list':[
                    'flow direction',
                    'timestamp absolute first',
                    'timestamp absolute last',
                    'connection initiator',
                    'connection new-connections',
                    'connection server counter packets long',
                    'connection client counter packets long',
                    'connection server counter bytes network long',
                    'connection client counter bytes network long'
                ]
            }
        },
        'netflow ipv4 app-stats-input':{
            'description':'Application statistics - input',
            'no_of_users':0,
            'total_field_space':73,
            'fields':{
                'match_list':[
                    'ipv4 version',
                    'ipv4 protocol',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface input',
                    'application name'
                ],
                'collect_list':[
                    'datalink dot1q vlan input',
                    'datalink mac source address input',
                    'datalink mac destination address input',
                    'transport tcp flags',
                    'interface output',
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'netflow ipv4 app-stats-output':{
            'description':'Application statistics - output',
            'no_of_users':0,
            'total_field_space':73,
            'fields':{
                'match_list':[
                    'ipv4 version',
                    'ipv4 protocol',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface output',
                    'application name'
                ],
                'collect_list':[
                    'datalink dot1q vlan output',
                    'datalink mac source address output',
                    'datalink mac destination address output',
                    'transport tcp flags',
                    'interface input',
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_l2_in':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':48,
            'fields':{
                'match_list':[
                    'datalink ethertype',
                    'datalink vlan input',
                    'datalink mac source address input',
                    'datalink mac destination address input'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_l2_out':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':48,
            'fields':{
                'match_list':[
                    'datalink ethertype',
                    'datalink mac source address input',
                    'datalink mac destination address output',
                    'datalink vlan output'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_ipv4_in':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':49,
            'fields':{
                'match_list':[
                    'ipv4 protocol',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface input'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_ipv4_out':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':49,
            'fields':{
                'match_list':[
                    'ipv4 protocol',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface output'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_ipv6_in':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':72,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 traffic-class',
                    'ipv6 protocol',
                    'ipv6 hop-limit',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'interface input'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'record_ipv6_out':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':72,
            'fields':{
                'match_list':[
                    'ipv6 version',
                    'ipv6 traffic-class',
                    'ipv6 protocol',
                    'ipv6 hop-limit',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'interface output'
                ],
                'collect_list':[
                    'counter bytes long',
                    'counter packets long',
                    'timestamp absolute first',
                    'timestamp absolute last'
                ]
            }
        },
        'fr-wdavc-in':{
            'description':'User defined',
            'no_of_users':1,
            'total_field_space':80,
            'fields':{
                'match_list':[
                    'ipv4 version',
                    'ipv4 protocol',
                    'application name',
                    'connection client ipv4 address',
                    'connection client transport port',
                    'connection server ipv4 address',
                    'connection server transport port',
                    'flow observation point'
                ],
                'collect_list':[
                    'flow direction',
                    'timestamp absolute first',
                    'timestamp absolute last',
                    'connection initiator',
                    'connection new-connections',
                    'connection server counter packets long',
                    'connection client counter packets long',
                    'connection server counter bytes network long',
                    'connection client counter bytes network long'
                ]
            }
        },
        'test':{
            'description':'User defined',
            'no_of_users':0,
            'total_field_space':0,
            'fields':{

            }
        }
    }
}

expected_output = {
    'flow_record':{
        'record_l2_in':{
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
        },
        'record_l2_out':{
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
        },
        'record_ipv4_in':{
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
    }
}

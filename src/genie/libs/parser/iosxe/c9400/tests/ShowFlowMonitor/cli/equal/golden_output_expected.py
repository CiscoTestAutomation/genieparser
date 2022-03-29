expected_output = {
    'flow_monitor_name':{
        'monitor_ipv4_in':{
            'description':'User defined',
            'record_name':'record_ipv4_out',
            'exporter_name':'export_local_nf10',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':15,
                'active_timeout':30
            }
        },
        'monitor_ipv6_in':{
            'description':'User defined',
            'record_name':'record_ipv6_in',
            'exporter_name':'export_local_nf10',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':15,
                'active_timeout':30
            }
        },
        'dnacmonitor':{
            'description':'User defined',
            'record_name':'dnacrecord',
            'exporter_name':'dnacexporter',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':10,
                'active_timeout':60
            }
        },
        'dnacmonitor_v6':{
            'description':'User defined',
            'record_name':'dnacrecord_v6',
            'exporter_name':'dnacexporter',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':10,
                'active_timeout':60
            }
        }
    }
}

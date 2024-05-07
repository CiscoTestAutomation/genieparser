expected_output = {
    'flow_monitor':{
        'FLOW_MONITOR_V4_IN':{
            'description':'User defined',
            'flow_record':'FLOWS_V4_INPUT',
            'flow_exporter':'FLOW_COLLECTOR',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':60,
                'active_timeout':180
            }
        },
        'FLOW_MONITOR_V4_OUT':{
            'description':'User defined',
            'flow_record':'FLOWS_V4_OUTPUT',
            'flow_exporter':'FLOW_COLLECTOR',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':60,
                'active_timeout':180
            }
        },
        'FLOW_MONITOR_V6_IN':{
            'description':'User defined',
            'flow_record':'FLOWS_V6_INPUT',
            'flow_exporter':'FLOW_COLLECTOR',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'allocated',
                'size':10000,
                'inactive_timeout':60,
                'active_timeout':180
            }
        },
        'FLOW_MONITOR_V6_OUT':{
            'description':'User defined',
            'flow_record':'FLOWS_V6_OUTPUT',
            'flow_exporter':'FLOW_COLLECTOR',
            'cache':{
                'type':'normal (Platform cache)',
                'status':'not allocated',
                'size':10000,
                'inactive_timeout':60,
                'active_timeout':180
            }
        }
    }
}


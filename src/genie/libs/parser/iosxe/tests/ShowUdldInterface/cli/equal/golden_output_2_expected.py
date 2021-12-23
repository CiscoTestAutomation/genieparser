expected_output = {
    'interfaces': {
        'GigabitEthernet1/0/7' : {
            'port_enable_administrative_configuration_setting' : 'Enabled / in alert mode',
            'port_enable_operational_state' : 'Enabled / in alert mode',
            'current_bidirectional_state' : 'Bidirectional',
            'current_operational_state': 'Advertisement - Single neighbor detected',
            'message_interval_ms' : 15000 ,
            'time_out_interval_ms': 5000,
            'port_fast_hello_configuration_setting': 'Disabled',
            'port_fast_hello_interval_ms': 0 ,
            'port_fast_hello_operational_state': 'Disabled',
            'neighbor_fast_hello_configuration_setting': 'Disabled',
            'neighbor_fast_hello_interval': 'Unknown',
            'entries' : { 
                1: {
                    'expiration_time_ms': 42600,
                    'cache_device_index': 1,
                    'current_neighbor_state': 'Bidirectional',
                    'device_id': 'A4B43937780',
                    'port_id': 'A4:B4:39:37:78:00/7',
                    'neighbor_echo_1_device': '70D37984690',
                    'neighbor_echo_1_port': '70:D3:79:84:69:00/7',
                    'tlv_message_interval_sec': 15,
                }
            }
        }   
    }
}

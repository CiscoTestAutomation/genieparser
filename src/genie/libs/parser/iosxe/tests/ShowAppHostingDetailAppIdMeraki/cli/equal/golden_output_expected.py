expected_output = {
    'app_id' : 'meraki',
    'owner' : 'iox',
    'state' : 'RUNNING',
    'application':{
        'type' : 'docker',
        'name' : 'cat9k-app',
        'version' : 'T-202106031655-G5c6da678-L0b29c1a9M-clouisa-creditor',
        'activated_profile_name' : 'custom'
    },
    'resource_reservation' : {
        'memory' : '512 MB',
        'disk' : '2 MB',
        'cpu' : '500 units',
        'cpu_percent' : '7 %',
        'vcpu' : 1
    },
    'attached_devices' : {
        'serial/shell': {
            'name' : 'iox_console_shell',
            'alias': 'serial0'
        },
        'serial/aux' : {
            'name' : 'iox_console_aux',
            'alias': 'serial1'
        },
        'serial/syslog' : {
            'name' : 'iox_syslog',
            'alias': 'serial2'
        },
        'serial/trace' : {
            'name' : 'iox_trace',
            'alias': 'serial3'
        }   
    },
    'network_interfaces' : {
        'eth2' : {
            'mac_address' : '52:54:dd:0c:8e:82',
            'ipv6_address' : '::',
            'network_name' : 'mgmt-bridge100'
        },
        'eth1': {
            'mac_address' : '52:54:dd:0e:5f:bd',
            'ipv6_address' : '::',
            'network_name' : 'mgmt-bridge-v4093'
        },
        'eth0' : {
            'mac_address' : '52:54:dd:e3:61:72',
            'ipv6_address' : '::',
            'network_name' : 'mgmt-bridge300'
        }
    },
    'docker' : {
        'run_time_information': {
            'entry_point' : '/sbin/init'
        },
        'application_health_information':{
            'status' : 0,
            'last_probe_output' : '[]'
        }
    }
}

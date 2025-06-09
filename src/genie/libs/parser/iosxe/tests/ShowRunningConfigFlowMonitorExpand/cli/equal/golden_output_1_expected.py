expected_output = {
    'flow_record': {
        'DreamLine-Record': {
            'matches': ['datalink mac source address input', 
                        'datalink mac destination address input', 
                        'datalink ethertype', 
                        'datalink vlan input', 
                        'datalink dot1q priority', 
                        'datalink dot1q vlan input', 
                        'ipv4 protocol', 
                        'ipv4 source address', 
                        'ipv4 destination address', 
                        'transport source-port', 
                        'transport destination-port', 
                        'interface input'], 
            'collects': ['counter bytes', 
                         'counter packets', 
                         'timestamp sys-uptime first']
            }
        }, 
        'flow_exporter': {
            'DDoS-Exporter': {
                'destination': '220.64.0.236', 
                'source': 'Loopback0', 
                'dscp': 57, 
                'ttl': 67, 
                'transport_protocol': 'udp', 
                'port': 5000
            }, 
            'Kentik_Exporter': {
                'destination': '192.186.1.1', 
                'source': 'Loopback0', 
                'dscp': 57, 
                'ttl': 67, 
                'transport_protocol': 'udp', 
                'port': 2055, 
                'match_counter_packets_long_gt': 456677, 
                'export_protocol': 'ipfix'
            }, 
            'KTOA-Exporter': {
                'destination': '192.186.1.1', 
                'source': 'Loopback0', 
                'dscp': 57, 
                'ttl': 67, 
                'transport_protocol': 'udp', 
                'port': 2055, 
                'match_counter_packets_long_gt': 456677, 
                'export_protocol': 'netflow-v9'
            }
        }, 
        'flow_monitor': {
            'DreamLine-Monitor': {
                'exporters': ['DDoS-Exporter', 
                              'Kentik_Exporter', 
                              'KTOA-Exporter'], 
                'cache_entries': 40000, 
                'record': 'DreamLine-Record'
            }
        }
    }
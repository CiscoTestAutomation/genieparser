expected_output =  {
     'zone_pair': {
         'in-out': {
             'service_policy_inspect': {
                 'pmap1': {
                     'class_map': {
                         'class-default': {
                             'bytes': 0,
                             'class_map_action': 'Drop',
                             'class_map_match': ['any'],
                             'class_map_type': 'match-any',
                             'packets': 0,
                         },
                         'cmap1': {
                             'class_map_action': 'Inspect',
                             'class_map_match': ['protocol udp', 'protocol icmp', 'protocol ftp', 'protocol tcp'],
                             'class_map_type': 'match-any',
                             'terminating_sessions': {
                                 '0x00000000': {
                                     'bytes_sent': {
                                         'initiator': '90',
                                         'responder': 332,
                                     },
                                     'created': '00:00:02',
                                     'initiator_ip': '1.1.1.1',
                                     'initiator_port': '11001',
                                     'last_heard': '00:00:01',
                                     'protocol': 'ftp',
                                     'responder_ip': '2.2.2.1',
                                     'responder_port': '21',
                                     'state': 'SIS_CLOSED',
                                 },
                             },
                         },
                     },
                 },
             },
         },
     },
 }


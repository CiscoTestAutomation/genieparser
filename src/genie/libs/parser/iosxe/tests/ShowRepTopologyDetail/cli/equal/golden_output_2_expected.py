expected_output = {
     'rep_segment': {
       'BOI-AIR-AGG-1': {
             'interfaces': {
                 'TenGigabitEthernet0/0/26': {
                     'bridge_mac': '00ea.bd0a.243f',
                     'edge': 'Primary Edge No-Neighbor',
                     'neighbor_number': '1 / [-4]',
                     'port_number': '021',
                     'port_priority': '000',
                    'role': 'Open',
                     'vlan_status': 'all vlans forwarding',
                 },
                 'TenGigabitEthernet0/0/27': {
                     'bridge_mac': '00ea.bd0a.243f',
                     'edge': 'Intermediate',
                     'neighbor_number': '2 / [-3]',
                     'port_number': '022',
                     'port_priority': '040',
                    'role': 'Alternate',
                     'vlan_status': 'some vlans blocked',
                 },
             },
         },
         'BOI-AIR-AGG-2': {
             'interfaces': {
                 'TenGigabitEthernet0/0/26': {
                     'bridge_mac': '00ea.bd0a.1dbf',
                     'edge': 'Intermediate',
                     'neighbor_number': '3 / [-2]',
                     'port_number': '021',
                     'port_priority': '000',
                     'role': 'Open',
                     'vlan_status': 'all vlans forwarding',
                 },
                 'TenGigabitEthernet0/0/27': {
                     'bridge_mac': '00ea.bd0a.1dbf',
                     'edge': 'Secondary Edge No-Neighbor',
                     'neighbor_number': '4 / [-1]',
                     'port_number': '022',
                     'port_priority': '000',
                     'role': 'Open',
                     'vlan_status': 'all vlans forwarding',
                 },
             },
         },
     },
     'rep_segment_no': 170,
 }
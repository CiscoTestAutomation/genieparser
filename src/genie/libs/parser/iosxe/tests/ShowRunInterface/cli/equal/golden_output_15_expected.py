expected_output =  {
     'interfaces': {
         'TenGigabitEthernet0/0/0.10': {
             'acl': {
                 'inbound': {
                     'acl_name': 'DELETE_ME',
                     'direction': 'in',
                 },
                 'outbound': {
                     'acl_name': 'TEST-OUT',
                     'direction': 'out',
                 },
             },
             'description': 'MPLS1',
             'encapsulation_dot1q': '10',
             'ipv4': {
                 'ip': '10.114.11.1',
                 'netmask': '255.255.255.252',
             },
             'mtu': 1500,
         },
     },
 }
expected_output =  {
     'interface': {
         'GigabitEthernet1/0/25': {
             'direction': {
                 'Ingress': {
                     'feature': {
                         'Racl': {
                             'cg_id': 17,
                             'cg_name': 'acl-1',
                             'dst_og_lkup_hdl': 0,
                             'protocol': 'IPv4',
                             'src_og_lkup_hdl': 0,
                             'status': 'Success',
                         },
                     },
                 },
             },
         },
         'GigabitEthernet1/0/26.11': {
             'direction': {
                 'Egress': {
                     'feature': {
                         'Racl': {
                             'cg_id': 13,
                             'cg_name': 'acl-2',
                             'dst_og_lkup_hdl': 0,
                             'protocol': 'IPv4',
                             'src_og_lkup_hdl': 0,
                             'status': 'Success',
                         },
                     },
                 },
             },
         },
     },
 }

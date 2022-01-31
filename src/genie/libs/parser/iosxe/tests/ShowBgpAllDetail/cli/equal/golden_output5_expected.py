expected_output = {
     'instance': {
         'default': {
             'vrf': {
                 'red': {
                     'address_family': {
                         '': {
                             'prefixes': {
                                 '11.11.11.11/32': {
                                     'available_path': '1',
                                     'best_path': '1',
                                     'index': {
                                         1: {
                                             'binding_sid': {
                                                 'color': '7',
                                                 'sid': '22',
                                                 'state': 'UP',
                                             },
                                             'cluster_list': '8.8.8.9',
                                             'ext_community': 'RT:2:2 Color:1 Color:2 Color:3 Color:4 Color:7',
                                             'gateway': '7.7.7.9',
                                             'imported_path_from': '1:1:11.11.11.11/32 (global)',
                                             'localpref': 100,
                                             'metric': 0,
                                             'mpls_labels': {
                                                 'in': 'nolabel',
                                                 'out': '19',
                                             },
                                             'next_hop': '4.4.4.4',
                                             'next_hop_igp_metric': '20',
                                             'next_hop_via': 'default',
                                             'origin_codes': '?',
                                             'originator': '8.8.8.9',
                                             'recipient_pathid': '0',
                                             'refresh_epoch': 5,
                                             'route_info': '1',
                                             'status_codes': '*>',
                                             'transfer_pathid': '0x0',
                                             'update_group': 5,
                                         },
                                     },
                                     'paths': '1 available, best #1, table red',
                                     'table_version': '17',
                                 },
                             },
                         },
                     },
                 },
             },
         },
     },
 }

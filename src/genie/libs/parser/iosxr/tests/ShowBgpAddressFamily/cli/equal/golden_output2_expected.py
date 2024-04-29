expected_output = {
     'address_family': {
         'ipv6_all': {
             'bgp_table_version': 5530,
             'generic_scan_interval': 60,
             'local_as': 1234,
             'non_stop_routing': True,
             'nsr_initial_init_ver_status': 'reached',
             'nsr_initial_initsync_version': '7',
             'nsr_issu_sync_group_versions': '5530/0',
             'route_distinguisher': {
                 '1234:1234': {
                     'prefix': {
                         '2001:0db8:85a3:0:0:0:0:1403::/48': {
                             'index': {
                                 1: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.1',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*>i',
                                     'weight': '100',
                                 },
                                 2: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.1',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*i',
                                     'weight': '100',
                                 },
                             },
                         },
                         '2001:0db8:85a3::/64': {
                             'index': {
                                 1: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.1',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*>i',
                                     'weight': '100',
                                 },
                                 2: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.1',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*i',
                                     'weight': '100',
                                 },
                             },
                         },
                     },
                 },
                 '1234:2505005': {
                     'prefix': {
                         '2001:0db8:85a3:0:0:0:0:6:10:205::/112': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*>i',
                                     'weight': '0',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*i',
                                     'weight': '0',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:6:192:168:201::/112': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*>i',
                                     'weight': '0',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*i',
                                     'weight': '0',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:6:195:113:123:128:0/112': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*>i',
                                     'weight': '0',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*i',
                                     'weight': '0',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:6:195:113:123:80/125': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*>i',
                                     'weight': '0',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*i',
                                     'weight': '0',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:6:195:113:123:96:0/112': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*>i',
                                     'weight': '0',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'metric': '4294967295',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '65031',
                                     'status_codes': '*i',
                                     'weight': '0',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:6::10/127': {
                             'index': {
                                 1: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*>i',
                                     'weight': '100',
                                 },
                                 2: {
                                     'locprf': '0',
                                     'next_hop': '192.0.2.2',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*i',
                                     'weight': '100',
                                 },
                             },
                         },
                     },
                 },
                 '1234:2505118': {
                     'prefix': {
                         '2001:0db8:85a3:0:0:0:0:18::/56': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'next_hop': '203.0.113.7',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*>i',
                                     'weight': '100',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'next_hop': '203.0.113.7',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*i',
                                     'weight': '100',
                                 },
                             },
                         },
                         '2001:0db8:85a3:0:0:0:0:1e08::/48': {
                             'index': {
                                 1: {
                                     'locprf': '100',
                                     'next_hop': '203.0.113.7',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*>i',
                                     'weight': '100',
                                 },
                                 2: {
                                     'locprf': '100',
                                     'next_hop': '203.0.113.7',
                                     'origin_codes': 'i',
                                     'path': '0',
                                     'status_codes': '*i',
                                     'weight': '100',
                                 },
                             },
                         },
                     },
                 },
             },
             'router_identifier': '192.168.1.1',
             'scan_interval': 60,
             'table_state': 'active',
         },
     },
 }


expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'vpnv4 unicast':
                    {'bgp_distance_internal_as': 33,
                    'bgp_distance_local': 55,
                    'ip':
                        {'10.121.0.0/8':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'Null0':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '5w0d',
                                                    'preference': '55',
                                                    'metric': '0',
                                                    'protocol_id': '100',
                                                    'attribute': 'discard',
                                                    'tag': '100'}}}}}}},
                        '10.205.0.1/32':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'attach': 'attached',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'10.205.0.1':
                                            {'protocol':
                                                {'local':
                                                    {'uptime': '2w6d',
                                                    'interface': 'Bdi1255',
                                                    'preference': '0',
                                                    'metric': '0'}}}}}}},
                        '10.189.1.0/24':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'10.55.130.3':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '3d10h',
                                                    'preference': '33',
                                                    'metric': '0',
                                                    'protocol_id': '1',
                                                    'attribute': 'internal',
                                                    'tag': '1',
                                                    'evpn': True,
                                                    'segid': 50051,
                                                    'route_table': 'default',
                                                    'tunnelid': '0x64008203',
                                                    'encap': 'vxlan'}}}}}}},
                        '10.21.33.33/32':
                            {'ubest_num': '1',
                            'mbest_num': '1',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'10.36.3.3':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '5w0d',
                                                    'preference': '33',
                                                    'metric': '0',
                                                    'protocol_id': '100',
                                                    'attribute': 'internal',
                                                    'route_table': 'default',
                                                    'mpls_vpn': True,
                                                    'tag': '100'}}}}},
                                'multicast':
                                    {'nexthop':
                                        {'10.36.3.3':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '5w0d',
                                                    'preference': '33',
                                                    'metric': '0',
                                                    'protocol_id': '100',
                                                    'attribute': 'internal',
                                                    'route_table': 'default',
                                                    'mpls_vpn': True,
                                                    'tag': '100'}}}}}}},
                        "10.16.2.2/32": {
                           "mbest_num": "0",
                           "ubest_num": "1",
                           "best_route": {
                                "unicast": {
                                     "nexthop": {
                                          "10.2.4.2": {
                                               "protocol": {
                                                    "ospf": {
                                                         "preference": "110",
                                                         "protocol_id": "1",
                                                         "uptime": "00:18:35",
                                                         "metric": "41",
                                                         "mpls": True,
                                                         "attribute": "intra",
                                                         "interface": "Ethernet2/4"}}}}}}},
                        "10.4.1.1/32": {
                           "mbest_num": "0",
                           "ubest_num": "2",
                           "best_route": {
                                "unicast": {
                                     "nexthop": {
                                          "10.2.4.2": {
                                               "protocol": {
                                                    "ospf": {
                                                         "preference": "110",
                                                         "protocol_id": "1",
                                                         "uptime": "00:18:35",
                                                         "metric": "81",
                                                         "mpls": True,
                                                         "attribute": "intra",
                                                         "interface": "Ethernet2/4"}}},
                                          "10.3.4.3": {
                                               "protocol": {
                                                    "ospf": {
                                                         "preference": "110",
                                                         "protocol_id": "1",
                                                         "uptime": "00:18:35",
                                                         "metric": "81",
                                                         "mpls": True,
                                                         "attribute": "intra",
                                                         "interface": "Ethernet2/1"}}}}}}},
                        '10.229.11.11/32':
                            {'ubest_num': '2',
                            'mbest_num': '0',
                            'attach': 'attached',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'10.229.11.11':
                                            {'protocol':
                                                {'local':
                                                    {'uptime': '5w4d',
                                                    'preference': '0',
                                                    'metric': '0',
                                                    'interface': 'Loopback1'},
                                                'direct':
                                                    {'uptime': '5w4d',
                                                    'preference': '0',
                                                    'metric': '0',
                                                    'interface': 'Loopback1'}}}}}}}}}}},
        'default':
            {'address_family':
                {'ipv4 unicast':
                    {'bgp_distance_extern_as': 20,
                    'bgp_distance_internal_as': 200,
                    'ip':
                        {'10.106.0.0/8':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'vrf default':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '18:11:28',
                                                    'preference': '20',
                                                    'metric': '0',
                                                    'protocol_id': '333',
                                                    'attribute': 'external',
                                                    'tag': '333',
                                                    'interface': 'Null0'}}}}}}},
                        '10.16.1.0/24':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'2001:db8:8b05::1002':
                                            {'protocol':
                                                {'bgp':
                                                    {'uptime': '15:57:39',
                                                    'preference': '200',
                                                    'metric': '4444',
                                                    'protocol_id': '333',
                                                    'attribute': 'internal',
                                                    'route_table': 'default',
                                                    'tag': '333',
                                                    'interface': 'Ethernet1/1'}}}}}}},
                        '10.106.0.5/8':
                            {'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route':
                                {'unicast':
                                    {'nexthop':
                                        {'Null0':
                                            {'protocol':
                                                {'static':
                                                    {'uptime': '18:47:42',
                                                    'preference': '1',
                                                    'metric': '0'}}}}}}}}}}}}}

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'ospfv3_l3uls':
                            {'areas':
                                {'0.0.0.0':
                                    {'interfaces':
                                        {'Ethernet1/33':
                                            {'neighbors':
                                                {'1.1.1.1':
                                                    {'address': 'fe80::2de:fbff:fed4:89c7',
                                                     'bdr_ip_addr': '1.1.1.1',
                                                     'dbd_options': '0x13',
                                                     'dead_timer': '00:00:33',
                                                     'dr_ip_addr': '2.2.2.2',
                                                     'hello_options': '0x13',
                                                     'last_non_hello_packet_received': '00:03:17',
                                                     'last_state_change': '04:06:04',
                                                     'priority': 1,
                                                     'nbr_intf_id': 37,
                                                     'neighbor_router_id': '1.1.1.1',
                                                     'state': 'full',
                                                     'statistics':
                                                        {'nbr_event_count': 5}
                                                     }
                                                 }
                                             }
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
             }
         }
}

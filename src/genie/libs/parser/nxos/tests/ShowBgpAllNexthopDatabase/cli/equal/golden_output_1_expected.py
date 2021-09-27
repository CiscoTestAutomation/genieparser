

expected_output = {
    "vrf": {
      "default": {
           "address_family": {
                "vpnv6 unicast": {
                     "nexthop_trigger_delay_non_critical": 10000,
                     "af_nexthop_trigger_enable": True,
                     "nexthop_trigger_delay_critical": 3000
                },
                "vpnv4 unicast": {
                     "nexthop_trigger_delay_non_critical": 10000,
                     "af_nexthop_trigger_enable": True,
                     "nexthop_trigger_delay_critical": 3000
                },
                "ipv4 mdt": {
                     "af_nexthop_trigger_enable": True,
                     "nexthop_trigger_delay_critical": 3000,
                     "nexthop_trigger_delay_non_critical": 10000,
                     "next_hop": {
                        "0.0.0.0": {
                             "resolve_time": "never",
                             "igp_cost": 0,
                             "rnh_epoch": 0,
                             "igp_route_type": 0,
                             "refcount": 1,
                             "metric_next_advertise": "never",
                             "rib_route": "0.0.0.0/0",
                             "igp_preference": 0,
                             'attached': False,
                             'local': True,
                             'reachable': False,
                             'labeled': False,
                             'filtered': False,
                             'pending_update': False,
                             "flags": "0x2",
                        },
                    },
                },
                "ipv4 unicast": {
                     "af_nexthop_trigger_enable": True,
                     "nexthop_trigger_delay_critical": 3000,
                     "nexthop_trigger_delay_non_critical": 10000,
                     "next_hop": {
                        "192.168.154.1": {
                             "resolve_time": "18:37:36",
                             "igp_cost": 3,
                             "attached_nexthop": {
                                  "192.168.196.2": {
                                       "attached_nexthop_interface": "port-channel2.100"
                                  },
                                  "192.168.66.2": {
                                       "attached_nexthop_interface": "port-channel2.107"
                                  }
                             },
                             "rnh_epoch": 1,
                             "igp_route_type": 0,
                             "refcount": 1,
                             "metric_next_advertise": "never",
                             "rib_route": "192.168.154.1/32",
                             "igp_preference": 110,
                             'attached': False,
                             'local': False,
                             'reachable': True,
                             'labeled': True,
                             'filtered': False,
                             'pending_update': False,
                             "flags": "0x41",
                        },
                    },
                },
                "ipv6 unicast": {
                     "af_nexthop_trigger_enable": True,
                     "nexthop_trigger_delay_critical": 3000,
                     "nexthop_trigger_delay_non_critical": 10000,
                     "next_hop": {
                        "2001:db8:400::3:1": {
                             "resolve_time": "18:37:36",
                             "igp_cost": 2,
                             "attached_nexthop": {
                                  "fe80::6e9c:edff:fe4d:ff41": {
                                       "attached_nexthop_interface": "port-channel2.100"
                                  }
                             },
                             "rnh_epoch": 1,
                             "igp_route_type": 0,
                             "refcount": 1,
                             "metric_next_advertise": "never",
                             "rib_route": "2001:db8:400::3:1/128",
                             "igp_preference": 110,
                             'attached': False,
                             'local': False,
                             'reachable': True,
                             'labeled': False,
                             'filtered': False,
                             'pending_update': False,
                             "flags": "0x1",
                        },
                    },
                }
           }
        }
    }
}

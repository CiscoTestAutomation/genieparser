

expected_output = {
    "template": {
      "PEER1": {
           "passive_only": False,
           "remove_private_as": False,
           "vrf": {
                "default": {
                     "inheriting_peer": {
                          "10.106.200.200": {
                               "inheriting_peer": "10.106.200.200"
                          }
                     }
                }
           },
           "address_family": {
                "ipv6 multicast": {
                     "send_community": True,
                     "condition_map": "PERMIT_ALL_RM",
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": True,
                     "default_originate": True,
                     "soo": "SOO:10.4.1.1:88",
                     "advertise_map_status": "advertise",
                     "allow_as_in": 4,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "third_party_nexthop": False,
                     "local_nexthop": "0.0.0.0",
                     "advertise_map": "PASS-ALL",
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "as_override": True,
                     "max_pfx": 1000000
                },
                "link-state": {
                     "as_override": False,
                     "send_community": True,
                     "in_soft_reconfig_allowed": False,
                     "third_party_nexthop": False,
                     "default_originate": False,
                     "peer_as_check_disabled": False,
                     "allow_as_in": 4,
                     "send_ext_community": True,
                     "rr_configured": False,
                     "max_pfx": 1000000
                },
                "ipv4 mvpn": {
                     "send_community": True,
                     "third_party_nexthop": False,
                     "max_pfx": 1000000,
                     "send_ext_community": True,
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": False,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "allow_as_in": 4,
                     "default_originate": False,
                     "as_override": False,
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     }
                },
                "vpnv6 unicast": {
                     "send_community": True,
                     "third_party_nexthop": False,
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": False,
                     "rr_configured": False,
                     "peer_as_check_disabled": False,
                     "local_nexthop": "0.0.0.0",
                     "allow_as_in": 4,
                     "default_originate": False,
                     "as_override": False,
                     "max_pfx": 1000000
                },
                "vpnv4 unicast": {
                     "send_community": True,
                     "third_party_nexthop": False,
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": False,
                     "rr_configured": False,
                     "peer_as_check_disabled": False,
                     "local_nexthop": "0.0.0.0",
                     "allow_as_in": 4,
                     "default_originate": False,
                     "as_override": False,
                     "max_pfx": 1000000
                },
                "ipv4 multicast": {
                     "send_community": True,
                     "condition_map": "PERMIT_ALL_RM",
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": True,
                     "default_originate": True,
                     "soo": "SOO:10.4.1.1:88",
                     "advertise_map_status": "advertise",
                     "allow_as_in": 4,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "third_party_nexthop": False,
                     "local_nexthop": "0.0.0.0",
                     "advertise_map": "PASS-ALL",
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "as_override": True,
                     "max_pfx": 1000000
                },
                "l2vpn evpn": {
                     "send_community": True,
                     "third_party_nexthop": False,
                     "max_pfx": 1000000,
                     "send_ext_community": True,
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": False,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "allow_as_in": 4,
                     "default_originate": False,
                     "as_override": True,
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     }
                },
                "ipv6 mvpn": {
                     "send_community": True,
                     "third_party_nexthop": False,
                     "max_pfx": 1000000,
                     "send_ext_community": True,
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": False,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "allow_as_in": 4,
                     "default_originate": False,
                     "as_override": False,
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     }
                },
                "ipv6 unicast": {
                     "send_community": True,
                     "condition_map": "PERMIT_ALL_RM",
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": True,
                     "default_originate": True,
                     "soo": "SOO:10.4.1.1:88",
                     "advertise_map_status": "advertise",
                     "allow_as_in": 4,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "third_party_nexthop": False,
                     "local_nexthop": "0.0.0.0",
                     "advertise_map": "PASS-ALL",
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "as_override": True,
                     "max_pfx": 1000000
                },
                "ipv4 unicast": {
                     "send_community": True,
                     "condition_map": "PERMIT_ALL_RM",
                     "weight": 222,
                     "unsuppress_map": "PERMIT_ALL_RM",
                     "in_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "in_soft_reconfig_allowed": True,
                     "default_originate": True,
                     "soo": "SOO:10.4.1.1:88",
                     "advertise_map_status": "advertise",
                     "allow_as_in": 4,
                     "rr_configured": False,
                     "peer_as_check_disabled": True,
                     "third_party_nexthop": False,
                     "local_nexthop": "0.0.0.0",
                     "advertise_map": "PASS-ALL",
                     "out_policy": {
                          "PASS-ALL": {
                               "type": "route-map",
                               "name": "PASS-ALL"
                          }
                     },
                     "send_ext_community": True,
                     "as_override": True,
                     "max_pfx": 1000000
                }
           },
           "local_as_inactive": False,
           "logging_neighbor_events": False
      }}}

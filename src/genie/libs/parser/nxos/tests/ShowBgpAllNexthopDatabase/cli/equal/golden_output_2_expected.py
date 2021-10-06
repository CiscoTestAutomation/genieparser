

expected_output = {
    "vrf": {
          "default": {
               "address_family": {
                    "ipv4 multicast": {
                         "next_hop": {
                              "10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "10.106.102.4": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "10.106.102.4": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.4/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "ipv6 multicast": {
                         "next_hop": {
                              "2001:db8:8d82::1002": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "2001:db8:8d82::1002": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "2001:db8:8d82::1002/128"
                              },
                              "2001:db8:8d82::2002": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "2001:db8:8d82::2002": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "2001:db8:8d82::2002/128"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "vpnv4 unicast": {
                         "next_hop": {
                              "10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "10.106.101.1": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.101.1": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.101.1/32"
                              },
                              "10.106.102.4": {
                                   "pending_update": False,
                                   "refcount": 4,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 1,
                                   "attached_nexthop": {
                                        "10.106.102.4": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.4/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "ipv4 unicast": {
                         "next_hop": {
                              "10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "10.106.101.1": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.101.1": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.101.1/32"
                              },
                              "10.186.101.99": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": False,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "igp_preference": 0,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": False,
                                   "flags": "0",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": -1,
                                   "rib_route": "0.0.0.0/0"
                              },
                              "10.106.102.4": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 1,
                                   "attached_nexthop": {
                                        "10.106.102.4": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.4/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "l2vpn evpn": {
                         "next_hop": {
                              "10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 4,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "10.106.101.1": {
                                   "pending_update": False,
                                   "refcount": 9,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.101.1": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.101.1/32"
                              },
                              "10.106.102.4": {
                                   "pending_update": False,
                                   "refcount": 4,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 1,
                                   "attached_nexthop": {
                                        "10.106.102.4": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.4/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "ipv4 mvpn": {
                         "next_hop": {
                              "10.106.103.20": {
                                   "pending_update": False,
                                   "refcount": 15,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 1,
                                   "attached_nexthop": {
                                        "10.106.103.20": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.103.20/32"
                              },
                              "10.106.103.10": {
                                   "pending_update": False,
                                   "refcount": 15,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 1,
                                   "attached_nexthop": {
                                        "10.106.103.10": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.103.10/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "ipv6 unicast": {
                         "next_hop": {
                              "2001:db8:8d82::1002": {
                                   "pending_update": False,
                                   "refcount": 3,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "2001:db8:8d82::1002": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "2001:db8:8d82::1002/128"
                              },
                              "2001:db8:8d82::2002": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "attached_nexthop": {
                                        "2001:db8:8d82::2002": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:19",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "2001:db8:8d82::2002/128"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "ipv6 mvpn": {
                         "next_hop": {
                              "2001:db8:4677:441::2": {
                                   "pending_update": False,
                                   "refcount": 10,
                                   "attached": False,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "igp_preference": 0,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": False,
                                   "flags": "0",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": -1,
                                   "rib_route": "0::/0"
                              },
                              "2001:db8:4677:121::2": {
                                   "pending_update": False,
                                   "refcount": 10,
                                   "attached": False,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 0,
                                   "igp_preference": 0,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": False,
                                   "flags": "0",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": -1,
                                   "rib_route": "0::/0"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "vpnv6 unicast": {
                         "next_hop": {
                              "::ffff:10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "::ffff:10.106.101.1": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.101.1": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.101.1/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    },
                    "link-state": {
                         "next_hop": {
                              "10.106.102.3": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.102.3": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.102.3/32"
                              },
                              "10.106.101.1": {
                                   "pending_update": False,
                                   "refcount": 2,
                                   "attached": True,
                                   "igp_route_type": 0,
                                   "rnh_epoch": 2,
                                   "attached_nexthop": {
                                        "10.106.101.1": {
                                             "attached_nexthop_interface": "Ethernet1/1"
                                        }
                                   },
                                   "igp_preference": 250,
                                   "filtered": False,
                                   "resolve_time": "00:52:09",
                                   "reachable": True,
                                   "flags": "0x5",
                                   "metric_next_advertise": "never",
                                   "labeled": False,
                                   "local": False,
                                   "igp_cost": 0,
                                   "rib_route": "10.106.101.1/32"
                              }
                         },
                         "af_nexthop_trigger_enable": True,
                         "nexthop_trigger_delay_non_critical": 10000,
                         "nexthop_trigger_delay_critical": 3000
                    }
               }
          }
     }
}

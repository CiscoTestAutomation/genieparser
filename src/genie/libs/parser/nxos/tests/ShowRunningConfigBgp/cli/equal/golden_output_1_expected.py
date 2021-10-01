

expected_output = {
    "bgp": {
    "instance": {
    "default": {
        "bgp_id": 333,
        "protocol_shutdown": True,
        "vrf": {
          "management": {
            "graceful_restart": True,
            "log_neighbor_changes": False,
            "enforce_first_as": True,
            "flush_routes": False,
            "fast_external_fallover": True,
            "isolate": False,
            "neighbor_id": {
              "10.100.5.5": {'nbr_disable_connected_check': False,
                          'nbr_ebgp_multihop': False,
                          'nbr_fall_over_bfd': False,
                          'nbr_local_as_dual_as': False,
                          'nbr_local_as_no_prepend': False,
                          'nbr_local_as_replace_as': False,
                          'nbr_password_text': '3 '
                                               '386c0565965f89de',
                          'nbr_remove_private_as': False,
                          'nbr_shutdown': False,
                          'nbr_suppress_four_byte_as_capability': False}}},
          "ac": {
            "log_neighbor_changes": False,
            "bestpath_cost_community_ignore": False,
            "bestpath_med_missing_at_worst": False,
            "enforce_first_as": True,
            "flush_routes": False,
            "always_compare_med": True,
            "graceful_restart": True,
            "bestpath_compare_routerid": False,
            "af_name": {
              "ipv4 unicast": {
                "af_client_to_client_reflection": True
              }
            },
            "neighbor_id": {
              "10.16.2.2": {
                "nbr_disable_connected_check": True,
                "nbr_local_as_replace_as": False,
                "nbr_local_as_no_prepend": False,
                "nbr_description": "ja",
                "nbr_af_name": {
                  "ipv4 unicast": {
                    "nbr_af_allowas_in_as_number": 3,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": True,
                    "nbr_af_maximum_prefix_max_prefix_no": 2
                  }
                },
                "nbr_shutdown": False,
                "nbr_remove_private_as": True,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_suppress_four_byte_as_capability": True,
                "nbr_fall_over_bfd": True,
                "nbr_local_as_as_no": 222
              }
            },
            "fast_external_fallover": True,
            "isolate": False
          },
          "vpn1": {
            "graceful_restart": True,
            "log_neighbor_changes": False,
            "af_name": {
              "ipv4 unicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv6 unicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv6 multicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv4 multicast": {
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_redist_static": True
              }
            },
            "enforce_first_as": True,
            "flush_routes": False,
            "fast_external_fallover": True,
            "isolate": False
          },
          "default": {
            "dynamic_med_interval": 70,
            "graceful_restart": False,
            "log_neighbor_changes": False,
            "af_name": {
               "l2vpn evpn": {
                    "af_advertise_pip": True,
                    "af_client_to_client_reflection": True
               },
              "ipv4 unicast": {
                "af_dampening_reuse_time": 10,
                "af_aggregate_address_ipv4_address": "10.4.1.0",
                "af_redist_static": True,
                "af_network_mask": 24,
                "af_network_number": "10.4.1.0",
                "af_redist_static_route_policy": "ADD_RT_400_400",
                "af_dampening": True,
                "af_client_to_client_reflection": True,
                "af_aggregate_address_ipv4_mask": 24,
                "af_dampening_suppress_time": 30,
                "af_dampening_max_suppress_time": 2,
                "af_v6_allocate_label_all": True,
                "af_dampening_half_life_time": 1
              },
              "link-state": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv4 multicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv6 unicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "vpnv6 unicast": {
                "af_dampening_reuse_time": 10,
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "vpnv4 unicast": {
                "af_dampening_route_map": "PASS-ALL",
                "af_dampening": True,
                "af_nexthop_trigger_enable": True,
                "af_nexthop_trigger_delay_critical": 4,
                "af_nexthop_trigger_delay_non_critical": 5
              },
              "ipv6 multicast": {
                "af_dampening_reuse_time": 10,
                "af_client_to_client_reflection": True,
                "af_redist_static_route_policy": "PERMIT_ALL_RM",
                "af_dampening_suppress_time": 30,
                "af_dampening": True,
                "af_redist_static": True,
                "af_dampening_max_suppress_time": 2,
                "af_dampening_half_life_time": 1
              },
              "ipv4 labeled-unicast": {}
            },
            "neighbor_id": {
              "2001:db8:8b05::2002": {
                "nbr_local_as_replace_as": False,
                "nbr_disable_connected_check": False,
                "nbr_remove_private_as": False,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_local_as_no_prepend": False,
                "nbr_shutdown": False,
                "nbr_suppress_four_byte_as_capability": False,
                "nbr_fall_over_bfd": False,
                "nbr_remote_as": 888,
                'nbr_update_source': 'loopback0',
                "nbr_af_name": {
                  "ipv4 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "link-state": {
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  }
                }
              },
              "10.186.102.1": {
                "nbr_local_as_replace_as": False,
                "nbr_peer_type" : "fabric-external",
                "nbr_af_name": {
                   "l2vpn evpn": {
                     "nbr_af_rewrite_evpn_rt_asn": True,
                     "nbr_af_allowas_in": False,
                     "nbr_af_send_community": "both",
                     'nbr_af_route_reflector_client': False
                  },
                  "ipv4 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "link-state": {
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv4 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv6 unicast": {
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv4 unicast": {
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  }
                },
                "nbr_disable_connected_check": False,
                "nbr_remove_private_as": False,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_local_as_no_prepend": False,
                "nbr_shutdown": False,
                "nbr_suppress_four_byte_as_capability": False,
                "nbr_fall_over_bfd": False,
                "nbr_remote_as": 333
              },
              "10.186.201.1": {
                "nbr_local_as_replace_as": False,
                "nbr_af_name": {
                  "ipv4 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "link-state": {
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv4 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv6 unicast": {
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv4 unicast": {
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": False,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  }
                },
                "nbr_disable_connected_check": False,
                "nbr_remove_private_as": False,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_local_as_no_prepend": False,
                "nbr_shutdown": False,
                "nbr_suppress_four_byte_as_capability": False,
                "nbr_fall_over_bfd": False,
                "nbr_remote_as": 888
              },
              "10.186.101.1": {
                "nbr_local_as_replace_as": False,
                "nbr_inherit_peer": "GENIE-BGP",
                "nbr_af_name": {
                  "ipv4 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "link-state": {
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv4 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv6 unicast": {
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "vpnv4 unicast": {
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  },
                  "ipv6 multicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  }
                },
                "nbr_disable_connected_check": False,
                "nbr_remove_private_as": False,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_local_as_no_prepend": False,
                "nbr_shutdown": False,
                "nbr_suppress_four_byte_as_capability": False,
                "nbr_fall_over_bfd": False,
                "nbr_remote_as": 333
              },
              "2001:db8:8b05::1002": {
                "nbr_local_as_replace_as": False,
                "nbr_af_name": {
                  "ipv4 unicast": {
                    "nbr_af_soft_reconfiguration": True,
                    "nbr_af_route_reflector_client": True,
                    "nbr_af_send_community": "both",
                    "nbr_af_allowas_in": False
                  }
                },
                "nbr_disable_connected_check": False,
                "nbr_remove_private_as": False,
                "nbr_local_as_dual_as": False,
                "nbr_ebgp_multihop": False,
                "nbr_local_as_no_prepend": False,
                "nbr_shutdown": False,
                "nbr_suppress_four_byte_as_capability": False,
                "nbr_fall_over_bfd": False,
                "nbr_remote_as": 333
              },
              "10.64.4.4": {}
            },
            "disable_policy_batching_ipv4": "s",
            "cluster_id": "3",
            "enforce_first_as": False,
            "flush_routes": True,
            "fast_external_fallover": True,
            "isolate": True
          }
        },
        "ps_name": {
          "PEER-SESSION": {
            "ps_ebgp_multihop": True,
            "ps_fall_over_bfd": False,
            "ps_shutdown": False,
            "ps_local_as_dual_as": False,
            "ps_local_as_replace_as": False,
            "ps_ebgp_multihop_max_hop": 3,
            "ps_suppress_four_byte_as_capability": False,
            "ps_local_as_no_prepend": False,
            "ps_disable_connected_check": False
          }
        }
      }
    }
  },
    'vxlan':{
        'evpn':{
            "evpn_vni": {
                8100: {
                    "evpn_vni_rd": "auto",
                    "evpn_vni_rt":{
                         "auto":{
                             "evpn_vni_rt": "auto",
                             "evpn_vni_rt_type": "export",
                             },
                        },
                    "evpn_vni": 8100,
                    },
                8101: {
                    "evpn_vni_rd": "auto",
                    "evpn_vni_rt": {
                        "auto": {
                            "evpn_vni_rt": "auto",
                            "evpn_vni_rt_type": "export",
                            }
                        },
                    "evpn_vni": 8101
                    },
                8103: {
                    "evpn_vni_rd": "auto",
                    "evpn_vni_rt": {
                        "auto": {
                            "evpn_vni_rt": "auto",
                            "evpn_vni_rt_type": "export",
                        }
                    },
                    "evpn_vni": 8103
                },
            },
        },
    },
}

expected_output={
  "tunnel_type": {
    "p2mp_sub_lsps": {
      "tunnel_name": {}
    },
    "p2mp_tunnels": {
      "tunnel_name": {}
    },
    "p2p_tunnels": {
      "tunnel_name": {
        "Tunnel100": {
          "active_path_option_parameters": {
            "bandwidthoverride": "disabled",
            "lockdown": "disabled",
            "state": {
              "active_path": "1",
              "path_type": "dynamic"
            },
            "verbatim": "disabled"
          },
          "config_parameters": {
            "action": "Tear",
            "affinity": "0x0/0xFFFF",
            "auto_bw": "disabled",
            "autoroute": "enabled",
            "bandwidth": 500,
            "bandwidth_type": "Global",
            "bandwidth_unit": "kbps",
            "cost_limit": "disabled",
            "fault_oam": "disabled",
            "hop_limit": "disabled",
            "load_share_type": "bw-based",
            "loadshare": 500,
            "lockdown": "disabled",
            "max_load_share": 4000000,
            "metric_type": "interface",
            "metric_used": "IGP",
            "path_invalidation_timeout": 10000,
            "path_invalidation_timeout_type": "default",
            "path_invalidation_timeout_unit": "msec",
            "path_selection_tiebreaker": {
              "effective": "min-fill",
              "effective_type": "default",
              "global": "not set",
              "tunnel_specific": "not set"
            },
            "priority": {
              "hold_priority": 7,
              "setup_priority": 7
            },
            "wrap_capable": "No",
            "wrap_protection": "disabled"
          },
          "destination": "2.2.2.2",
          "history": {
            "current_lsp_id": {
              "319": {
                "selection": "reoptimization",
                "uptime": "2 hours, 27 minutes"
              }
            },
            "prior_lsp_id": {
              "301": {
                "id": "path option unknown",
                "removal_trigger": "configuration changed "
              }
            },
            "tunnel": {
              "number_of_lsp_ids_used": 319,
              "time_since_created": "1 days, 50 minutes",
              "time_since_path_change": "20 hours, 4 minutes"
            }
          },
          "inlabel": [
            "-"
          ],
          "next_hop": [
            "192.1.1.2"
          ],
          "node_hop_count": 1,
          "outlabel": [
            "Port-channel20",
            "implicit-null"
          ],
          "rsvp_signalling_info": {
            "dst": "2.2.2.2",
            "rsvp_path_info": {
              "explicit_route": [
                "192.1.1.2",
                "2.2.2.2"
              ],
              "my_address": "192.1.1.1",
              "record_route": "NONE",
              "tspec": {
                "ave_rate": 500,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 500,
                "peak_rate_unit": "kbits"
              }
            },
            "rsvp_resv_info": {
              "fspec": {
                "ave_rate": 500,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 500,
                "peak_rate_unit": "kbits"
              },
              "record_route": "NONE"
            },
            "src": "3.3.3.3",
            "tun_id": 100,
            "tun_instance": 319
          },
          "status": {
            "admin": "up",
            "oper": "up",
            "path": "valid",
            "path_option": {
              "1": {
                "path_weight": 1,
                "type": "dynamic"
              },
              "2": {
                "type": "dynamic"
              }
            },
            "signalling": "connected"
          }
        },
        "Tunnel101": {
          "config_parameters": {
            "action": "Tear",
            "affinity": "0x0/0xFFFF",
            "auto_bw": "disabled",
            "autoroute": "enabled",
            "bandwidth": 5000,
            "bandwidth_type": "Global",
            "bandwidth_unit": "kbps",
            "cost_limit": "disabled",
            "fault_oam": "disabled",
            "hop_limit": "disabled",
            "load_share_type": "bw-based",
            "loadshare": 5000,
            "lockdown": "disabled",
            "max_load_share": 0,
            "metric_type": "default",
            "metric_used": "TE",
            "path_invalidation_timeout": 10000,
            "path_invalidation_timeout_type": "default",
            "path_invalidation_timeout_unit": "msec",
            "path_selection_tiebreaker": {
              "effective": "min-fill",
              "effective_type": "default",
              "global": "not set",
              "tunnel_specific": "not set"
            },
            "priority": {
              "hold_priority": 7,
              "setup_priority": 7
            },
            "wrap_capable": "No",
            "wrap_protection": "disabled"
          },
          "destination": "2.2.2.2",
          "history": {
            "prior_lsp_id": {
              "11": {
                "id": "path option unknown",
                "removal_trigger": "tunnel shutdown"
              }
            },
            "tunnel": {
              "number_of_lsp_ids_used": 11,
              "time_since_created": "3 hours, 11 minutes",
              "time_since_path_change": "2 hours, 52 minutes"
            }
          },
          "status": {
            "admin": "admin-down",
            "oper": "down",
            "path": "not valid",
            "path_option": {
              "1": {
                "path_name": "R3_R5_R2",
                "type": "explicit"
              },
              "2": {
                "type": "dynamic"
              }
            },
            "signalling": "down"
          }
        },
        "Tunnel102": {
          "active_path_option_parameters": {
            "bandwidthoverride": "disabled",
            "lockdown": "disabled",
            "state": {
              "active_path": "1",
              "path_type": "explicit"
            },
            "verbatim": "disabled"
          },
          "config_parameters": {
            "action": "Tear",
            "affinity": "0x0/0xFFFF",
            "auto_bw": "disabled",
            "autoroute": "enabled",
            "bandwidth": 5000,
            "bandwidth_type": "Global",
            "bandwidth_unit": "kbps",
            "cost_limit": "disabled",
            "fault_oam": "disabled",
            "hop_limit": "disabled",
            "load_share_type": "bw-based",
            "loadshare": 5000,
            "lockdown": "disabled",
            "max_load_share": 400000,
            "metric_type": "default",
            "metric_used": "TE",
            "path_invalidation_timeout": 10000,
            "path_invalidation_timeout_type": "default",
            "path_invalidation_timeout_unit": "msec",
            "path_selection_tiebreaker": {
              "effective": "min-fill",
              "effective_type": "default",
              "global": "not set",
              "tunnel_specific": "not set"
            },
            "priority": {
              "hold_priority": 7,
              "setup_priority": 7
            },
            "wrap_capable": "No",
            "wrap_protection": "disabled"
          },
          "destination": "2.2.2.2",
          "history": {
            "current_lsp_id": {
              "2": {
                "selection": "reoptimization",
                "uptime": "1 hours, 34 minutes"
              }
            },
            "prior_lsp_id": {
              "1": {
                "id": "path option unknown",
                "removal_trigger": "configuration changed "
              }
            },
            "tunnel": {
              "number_of_lsp_ids_used": 2,
              "time_since_created": "2 hours, 53 minutes",
              "time_since_path_change": "1 hours, 34 minutes"
            }
          },
          "inlabel": [
            "-"
          ],
          "next_hop": [
            "194.1.1.2"
          ],
          "node_hop_count": 2,
          "outlabel": [
            "Port-channel40",
            "23"
          ],
          "rsvp_signalling_info": {
            "dst": "2.2.2.2",
            "rsvp_path_info": {
              "explicit_route": [
                "194.1.1.2",
                "197.1.1.1",
                "197.1.1.2",
                "2.2.2.2"
              ],
              "my_address": "194.1.1.1",
              "record_route": "NONE",
              "tspec": {
                "ave_rate": 5000,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 5000,
                "peak_rate_unit": "kbits"
              }
            },
            "rsvp_resv_info": {
              "fspec": {
                "ave_rate": 5000,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 5000,
                "peak_rate_unit": "kbits"
              },
              "record_route": "NONE"
            },
            "src": "3.3.3.3",
            "tun_id": 102,
            "tun_instance": 2
          },
          "status": {
            "admin": "up",
            "oper": "up",
            "path": "valid",
            "path_option": {
              "1": {
                "path_attribute": "TU1_attrib",
                "path_name": "R3_R5_R2",
                "path_weight": 2,
                "type": "explicit"
              },
              "2": {
                "type": "dynamic"
              }
            },
            "signalling": "connected"
          }
        }
      }
    }
  }
}

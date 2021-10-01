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
              "19": {
                "id": "path option 3 ",
                "last_error": "CTRL:: Destination IP address, 2.2.2.2, not found",
                "removal_trigger": "tunnel shutdown"
              }
            },
            "tunnel": {
              "number_of_lsp_ids_used": 428,
              "time_since_created": "11 hours, 15 minutes",
              "time_since_path_change": "1 hours, 11 minutes"
            }
          },
          "status": {
            "admin": "up",
            "oper": "down",
            "path": "not valid",
            "path_option": {
              "1": {
                "type": "dynamic"
              },
              "2": {
                "type": "dynamic"
              },
              "3": {
                "path_name": "R3_R5_R2",
                "type": "explicit"
              }
            },
            "signalling": "down"
          }
        },
        "Tunnel101": {
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
            "tunnel": {
              "number_of_lsp_ids_used": 192,
              "time_since_created": "45 minutes, 2 seconds"
            }
          },
          "status": {
            "admin": "up",
            "oper": "down",
            "path": "not valid",
            "path_option": {
              "1": {
                "type": "dynamic"
              },
              "2": {
                "path_name": "R3_R5_R2",
                "type": "explicit"
              }
            },
            "signalling": "down"
          }
        },
        "Tunnel102": {
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
          "destination": "4.4.4.4",
          "history": {
            "tunnel": {
              "number_of_lsp_ids_used": 94,
              "time_since_created": "44 minutes, 16 seconds"
            }
          },
          "status": {
            "admin": "up",
            "oper": "down",
            "path": "not valid",
            "path_option": {
              "1": {
                "type": "dynamic"
              }
            },
            "signalling": "down"
          }
        }
      }
    }
  }
}

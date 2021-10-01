expected_output={
  "tunnel": {
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
            "last_error": "CTRL:: Explicit path has unknown address, 194.1.1.1",
            "removal_trigger": "tunnel shutdown"
          }
        },
        "tunnel": {
          "number_of_lsp_ids_used": 35,
          "time_since_created": "10 hours, 13 minutes",
          "time_since_path_change": "9 minutes, 22 seconds"
        }
      },
      "shortest_unconstrained_path_info": {
        "explicit_route": [
          "UNKNOWN"
        ],
        "path_weight": "UNKNOWN"
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
    }
  }
}

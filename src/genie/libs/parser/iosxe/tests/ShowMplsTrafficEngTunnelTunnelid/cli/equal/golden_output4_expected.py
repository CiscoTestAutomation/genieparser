expected_output={
  "tunnel": {
    "Tunnel100": {
      "config_parameters": {
        "action": "Tear",
        "affinity": "0x0/0xFFFF",
        "auto_bw": "disabled",
        "autoroute": "disabled",
        "autoroute_destination": "enabled",
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
          "5022": {
            "id": "path option 1 ",
            "last_error": "CTRL:: path",
            "removal_trigger": "configuration changed "
          }
        },
        "tunnel": {
          "number_of_lsp_ids_used": 5029,
          "time_since_created": "2 days, 3 hours, 48 minutes",
          "time_since_path_change": "12 minutes, 41 seconds"
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
            "lockdown": True,
            "path_name": "R4_R5_R2",
            "type": "explicit"
          },
          "2": {
            "path_attribute": "ATTR",
            "path_name": "R3_R4_R2",
            "type": "explicit"
          }
        },
        "signalling": "down"
      }
    }
  }
}

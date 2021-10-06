expected_output={
  "tunnel": {
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
          "19": {
            "selection": "reoptimization",
            "uptime": "9 hours, 52 minutes"
          }
        },
        "prior_lsp_id": {
          "18": {
            "id": "path option unknown",
            "removal_trigger": "configuration changed "
          }
        },
        "tunnel": {
          "number_of_lsp_ids_used": 19,
          "time_since_created": "9 hours, 59 minutes",
          "time_since_path_change": "9 hours, 52 minutes"
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
        " implicit-null"
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
        "tun_instance": 19
      },
      "shortest_unconstrained_path_info": {
        "explicit_route": [
          "192.1.1.1",
          "192.1.1.2",
          "2.2.2.2"
        ],
        "path_weight": "1",
        "path_weight_type": "TE"
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
          },
          "3": {
            "path_name": "R3_R5_R2",
            "type": "explicit"
          }
        },
        "signalling": "connected"
      }
    }
  }
}

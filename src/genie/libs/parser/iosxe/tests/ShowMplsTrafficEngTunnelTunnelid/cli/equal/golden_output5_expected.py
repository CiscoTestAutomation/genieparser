expected_output={
  "tunnel": {
    "Tunnel100": {
      "active_path_option_parameters": {
        "bandwidthoverride": "disabled",
        "lockdown": "enabled",
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
        "lockdown": "enabled",
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
          "5030": {
            "uptime": "1 minutes, 11 seconds"
          }
        },
        "prior_lsp_id": {
          "5022": {
            "id": "path option unknown",
            "removal_trigger": "configuration changed "
          }
        },
        "tunnel": {
          "number_of_lsp_ids_used": 5030,
          "time_since_created": "2 days, 3 hours, 58 minutes",
          "time_since_path_change": "1 minutes, 11 seconds"
        }
      },
      "inlabel": [
        "-"
      ],
      "next_hop": [
        "193.1.1.2"
      ],
      "node_hop_count": 1,
      "outlabel": [
        "Port-channel30",
        " 27"
      ],
      "rsvp_signalling_info": {
        "dst": "2.2.2.2",
        "rsvp_path_info": {
          "explicit_route": [
            "193.1.1.2",
            "4.4.4.4",
            "196.1.1.2*",
            "197.1.1.2*"
          ],
          "my_address": "193.1.1.1",
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
          "record_route": "196.1.1.1 197.1.1.1 197.1.1.2"
        },
        "src": "3.3.3.3",
        "tun_id": 100,
        "tun_instance": 5030
      },
      "shortest_unconstrained_path_info": {
        "explicit_route": [
          "UNKNOWN"
        ],
        "path_weight": "UNKNOWN"
      },
      "status": {
        "admin": "up",
        "oper": "up",
        "path": "valid",
        "path_option": {
          "1": {
            "lockdown": True,
            "path_name": "PE1_R4_R5_R2",
            "path_weight": 1,
            "type": "explicit"
          }
        },
        "signalling": "connected"
      }
    }
  }
}

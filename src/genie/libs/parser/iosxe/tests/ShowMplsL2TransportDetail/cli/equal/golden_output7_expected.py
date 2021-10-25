expected_output={
  "interface": {
    "Ethernet0/2": {
      "create_time": "00:00:16",
      "destination_address": {
        "4.4.4.4": {
          "default_path": "no route",
          "imposed_label_stack": "{}",
          "output_interface": "none",
          "preferred_path": "not configured",
          "vc_id": {
            "1": {
              "vc_status": "down"
            }
          }
        }
      },
      "ethernet_vlan": {
        1000: {
           'status': 'down',
                },
      },
      "graceful_restart": "not configured and not enabled",
      "label_state_machine": "local standby, AC-ready, LnuRnd",
      "last_label_fsm_state_change_time": "00:00:16",
      "last_status_change_time": "00:00:16",
      "last_status_name": {
        "bfd_dataplane": {
          "received": "Not sent"
        },
        "bfd_peer_monitor": {
          "received": "No fault"
        },
        "local_ac__circuit": {
          "received": "No fault",
          "sent": "Not sent"
        },
        "local_dataplane": {
          "received": "No fault"
        },
        "local_ldp_tlv": {
          "sent": "No status"
        },
        "local_pw_if_circ": {
          "received": "No fault"
        },
        "remote_ldp_adj": {
          "received": "None (no remote binding)"
        },
        "remote_ldp_tlv": {
          "received": "None (no remote binding)"
        }
      },
      "ldp_route_enabled": "enabled",
      "line_protocol_status": "up",
      "non_stop_routing": "not configured and not enabled",
      "sequencing": {
        "received": "disabled",
        "sent": "disabled"
      },
      "signaling_protocol": {
        "LDP": {
          "group_id": {
            "local": "4",
            "remote": "unknown"
          },
          "mpls_vc_labels": {
            "local": "21",
            "remote": "unassigned"
          },
          "mtu": {
            "local": "1500",
            "remote": "unknown"
          },
          "peer_id": "unknown",
        }
      },
      "status": "up",
      "statistics": {
        "bytes": {
          "received": 0,
          "sent": 0
        },
        "packets": {
          "received": 0,
          "sent": 0
        },
        "packets_drop": {
          "received": 0,
          "sent": 0,
          "seq_error": 0
        }
      },
      "status_tlv_support": "enabled/None (no remote binding"
    }
  }
}


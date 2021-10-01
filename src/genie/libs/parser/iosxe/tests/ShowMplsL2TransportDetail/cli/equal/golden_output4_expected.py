expected_output={
  "interface": {
    "Port-channel10": {
      "create_time": "04:34:36",
      "destination_address": {
        "3.3.3.3": {
          "default_path": "active",
          "imposed_label_stack": "{117}",
          "next_hop": "192.1.1.1",
          "output_interface": "Port-channel20",
          "preferred_path": "not configured",
          "vc_id": {
            "10": {
              "vc_status": "up"
            }
          }
        }
      },
      "graceful_restart": "configured and enabled",
      "label_state_machine": "established, LruRru",
      "last_label_fsm_state_change_time": "04:17:59",
      "last_status_change_time": "04:11:01",
      "last_status_name": {
        "bfd_dataplane": {
          "received": "Not sent"
        },
        "bfd_peer_monitor": {
          "received": "No fault"
        },
        "local_ac__circuit": {
          "received": "No fault",
          "sent": "No fault"
        },
        "local_dataplane": {
          "received": "No fault"
        },
        "local_ldp_tlv": {
          "sent": "No fault"
        },
        "local_pw_if_circ": {
          "received": "No fault"
        },
        "remote_ldp_adj": {
          "received": "No fault"
        },
        "remote_ldp_tlv": {
          "received": "No fault"
        }
      },
      "ldp_route_enabled": "enabled",
      "line_protocol_status": "up",
      "non_stop_routing": "not configured and not enabled",
      "protocol_status": {
        "Ethernet": "up"
      },
      "sequencing": {
        "received": "disabled",
        "sent": "disabled"
      },
      "signaling_protocol": {
        "LDP": {
          "group_id": {
            "local": "n/a",
            "remote": "0"
          },
          "id": "3.3.3.3",
          "mpls_vc_labels": {
            "local": "133",
            "remote": "117"
          },
          "mtu": {
            "local": "1500",
            "remote": "1500"
          },
          "peer_id": "3.3.3.3:0",
          "peer_state": "up",
          "status": "UP",
          "targeted_hello_ip": "2.2.2.2"
        }
      },
      "state": "up",
      "statistics": {
        "bytes": {
          "received": 2739166,
          "sent": 967768
        },
        "packets": {
          "received": 20342,
          "sent": 7194
        },
        "packets_drop": {
          "received": 0,
          "sent": 0,
          "seq_error": 0
        }
      },
      "status_tlv_support": "enabled/supported"
    }
  }
}


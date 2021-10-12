expected_output={
  "interface": {
    "Port-channel10": {
      "create_time": "00:02:03",
      "destination_address": {
        "2.2.2.2": {
          "default_path": "ready",
          "imposed_label_stack": "{133}",
          "next_hop": "point2point",
          "output_interface": "Tunnel100",
          "preferred_path": "Tunnel100",
          "preferred_path_state": "active",
          "vc_id": {
            "10": {
              "vc_status": "up"
            }
          }
        }
      },
      "graceful_restart": "configured and enabled",
      "label_state_machine": "established, LruRru",
      "last_label_fsm_state_change_time": "00:02:03",
      "last_status_change_time": "00:02:03",
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
          "id": "2.2.2.2",
          "mpls_vc_labels": {
            "local": "125",
            "remote": "133"
          },
          "mtu": {
            "local": "1500",
            "remote": "1500"
          },
          "peer_id": "2.2.2.2:0",
          "peer_state": "up",
          "status": "UP",
          "targeted_hello_ip": "3.3.3.3"
        }
      },
      "state": "up",
      "statistics": {
        "bytes": {
          "received": 1176291,
          "sent": 17970
        },
        "packets": {
          "received": 7520,
          "sent": 158
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


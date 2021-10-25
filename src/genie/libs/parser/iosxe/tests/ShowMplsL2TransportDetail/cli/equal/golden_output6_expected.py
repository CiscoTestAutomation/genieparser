expected_output={
  "interface": {
    "Ethernet0/3": {
      "create_time": "00:01:05",
      "destination_address": {
        "1.1.1.1": {
          "default_path": "active",
          "imposed_label_stack": "{24 21}",
          "next_hop": "30.1.2.1",
          "output_interface": "Ethernet0/1",
          "preferred_path": "not configured",
          "vc_id": {
            "1": {
              "vc_status": "up"
            }
          }
        }
      },
      "ethernet_vlan": {
        1000: {
           'status': 'up',
                },
      },
      "graceful_restart": "not configured and not enabled",
      "label_state_machine": "established, LruRru",
      "last_label_fsm_state_change_time": "00:01:05",
      "last_status_change_time": "00:01:05",
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
      "non_stop_routing": "configured and not enabled",
      "sequencing": {
        "received": "disabled",
        "sent": "disabled"
      },
      "signaling_protocol": {
        "LDP": {
          "group_id": {
            "local": "5",
            "remote": "4"
          },
          "id": "1.1.1.1",
          "mpls_vc_labels": {
            "local": "21",
            "remote": "21"
          },
          "mtu": {
            "local": "1500",
            "remote": "1500"
          },
          "peer_id": "1.1.1.1:0",
          "peer_state": "up",
          "status": "UP",
          "targeted_hello_ip": "4.4.4.4"
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
      "status_tlv_support": "enabled/supported"
    }
  }
}


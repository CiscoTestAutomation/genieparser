expected_output = {
  "instance": {
    "default": {
      "vrf": {
        "default": {
          "neighbor": {
            "10.10.10.107": {
              "address_family": {
                "ipv4 unicast": {
                  "accepted_prefixes": 3,
                  "additional_paths_operation": "None",
                  "best_paths": 1,
                  "cummulative_no_prefixes_denied": 0,
                  "eor_status": "was received during read-only mode",
                  "filter_group": "0.1",
                  "last_ack_version": 8,
                  "last_synced_ack_version": 0,
                  "maximum_prefix_max_prefix_no": 1048576,
                  "maximum_prefix_restart": 0,
                  "maximum_prefix_threshold": "75%",
                  "maximum_prefix_warning_only": True,
                  "neighbor_version": 8,
                  "outstanding_version_objects_current": 0,
                  "outstanding_version_objects_max": 1,
                  "prefix_advertised": 3,
                  "prefix_suppressed": 0,
                  "prefix_withdrawn": 0,
                  "refresh_request_status": "No Refresh request being processed",
                  "route_map_name_in": "route-in",
                  "route_map_name_out": "route-out",
                  "route_refresh_request_received": 0,
                  "route_refresh_request_sent": 0,
                  "soft_configuration": True,
                  "update_group": "0.2"
                }
              },
              "attempted": 19,
              "bgp_negotiated_capabilities": {
                "four_octets_asn": "advertised received",
                "ipv4_unicast": "advertised received",
                "route_refresh": "advertised received"
              },
              "bgp_neighbor_counters": {
                "messages": {
                  "received": {
                    "keepalives": 144,
                    "notifications": 0,
                    "opens": 2,
                    "updates": 2
                  },
                  "sent": {
                    "keepalives": 144,
                    "notifications": 0,
                    "opens": 1,
                    "updates": 2
                  }
                }
              },
              "bgp_session_transport": {
                "connection": {
                  "connections_dropped": 0,
                  "connections_established": 1,
                  "last_reset": "00:00:00",
                  "state": "established"
                },
                "transport": {
                  "foreign_host": "10.10.10.107",
                  "foreign_port": "179",
                  "if_handle": "0x00000060",
                  "local_host": "10.10.10.108",
                  "local_port": "36752"
                }
              },
              "enforcing_first_as": "enabled",
              "holdtime": 180,
              "inbound_message": "3",
              "keepalive_interval": 60,
              "last_full_not_set_pulse_count": 292,
              "last_ka_error_before_reset": "00:00:00",
              "last_ka_error_ka_not_sent": "00:00:00",
              "last_ka_expiry_before_reset": "00:00:00",
              "last_ka_expiry_before_second_last": "00:00:00",
              "last_ka_start_before_reset": "00:00:00",
              "last_ka_start_before_second_last": "00:00:00",
              "last_read": "00:00:55",
              "last_read_before_reset": "00:00:00",
              "last_write": "00:00:56",
              "last_write_attempted": 0,
              "last_write_before_reset": "00:00:00",
              "last_write_pulse_rcvd": "Aug 21 20:43:11.593 ",
              "last_write_pulse_rcvd_before_reset": "00:00:00",
              "last_write_thread_event_before_reset": "00:00:00",
              "last_write_thread_event_second_last": "00:00:00",
              "last_write_written": 0,
              "link_state": "external link",
              "local_as_as_no": "65108.65108",
              "local_as_dual_as": False,
              "local_as_no_prepend": False,
              "local_as_replace_as": False,
              "message_stats_input_queue": 0,
              "message_stats_output_queue": 0,
              "min_acceptable_hold_time": 3,
              "minimum_time_between_adv_runs": 30,
              "multiprotocol_capability": "received",
              "non_stop_routing": True,
              "nsr_state": "None",
              "outbound_message": "3",
              "precedence": "internet",
              "remote_as": "65107.65107",
              "router_id": "10.10.10.107",
              "second_attempted": 19,
              "second_last_write": "00:01:56",
              "second_last_write_before_attempted": 0,
              "second_last_write_before_reset": "00:00:00",
              "second_last_write_before_written": 0,
              "second_written": 19,
              "session_state": "established",
              "tcp_initial_sync": "---",
              "tcp_initial_sync_done": "---",
              "up_time": "02:23:58",
              "written": 19
            },
            "2001:2001:2001:2001:2001::7": {
              "address_family": {
                "ipv6 unicast": {
                  "accepted_prefixes": 3,
                  "additional_paths_operation": "None",
                  "best_paths": 2,
                  "cummulative_no_prefixes_denied": 0,
                  "eor_status": "was received during read-only mode",
                  "filter_group": "0.1",
                  "last_ack_version": 10,
                  "last_synced_ack_version": 0,
                  "maximum_prefix_max_prefix_no": 524288,
                  "maximum_prefix_restart": 0,
                  "maximum_prefix_threshold": "75%",
                  "maximum_prefix_warning_only": True,
                  "neighbor_version": 10,
                  "outstanding_version_objects_current": 0,
                  "outstanding_version_objects_max": 1,
                  "prefix_advertised": 3,
                  "prefix_suppressed": 0,
                  "prefix_withdrawn": 0,
                  "refresh_request_status": "No Refresh request being processed",
                  "route_map_name_in": "route-in",
                  "route_map_name_out": "route-out",
                  "route_refresh_request_received": 0,
                  "route_refresh_request_sent": 0,
                  "soft_configuration": True,
                  "update_group": "0.2"
                }
              },
              "attempted": 19,
              "bgp_negotiated_capabilities": {
                "four_octets_asn": "advertised received",
                "ipv6_unicast": "advertised received",
                "route_refresh": "advertised received"
              },
              "bgp_neighbor_counters": {
                "messages": {
                  "received": {
                    "keepalives": 144,
                    "notifications": 0,
                    "opens": 1,
                    "updates": 2
                  },
                  "sent": {
                    "keepalives": 144,
                    "notifications": 0,
                    "opens": 1,
                    "updates": 2
                  }
                }
              },
              "bgp_session_transport": {
                "connection": {
                  "connections_dropped": 0,
                  "connections_established": 1,
                  "last_reset": "00:00:00",
                  "state": "established"
                },
                "transport": {
                  "foreign_host": "2001:2001:2001:2001:2001::7",
                  "foreign_port": "26921",
                  "if_handle": "0x00000060",
                  "local_host": "2001:2001:2001:2001:2001::8",
                  "local_port": "179"
                }
              },
              "enforcing_first_as": "enabled",
              "holdtime": 180,
              "inbound_message": "3",
              "keepalive_interval": 60,
              "last_full_not_set_pulse_count": 293,
              "last_ka_error_before_reset": "00:00:00",
              "last_ka_error_ka_not_sent": "00:00:00",
              "last_ka_expiry_before_reset": "00:00:00",
              "last_ka_expiry_before_second_last": "00:00:00",
              "last_ka_start_before_reset": "00:00:00",
              "last_ka_start_before_second_last": "00:00:00",
              "last_read": "00:00:15",
              "last_read_before_reset": "00:00:00",
              "last_write": "00:00:15",
              "last_write_attempted": 0,
              "last_write_before_reset": "00:00:00",
              "last_write_pulse_rcvd": "Aug 21 20:43:51.721 ",
              "last_write_pulse_rcvd_before_reset": "00:00:00",
              "last_write_thread_event_before_reset": "00:00:00",
              "last_write_thread_event_second_last": "00:00:00",
              "last_write_written": 0,
              "link_state": "external link",
              "local_as_as_no": "65108.65108",
              "local_as_dual_as": False,
              "local_as_no_prepend": False,
              "local_as_replace_as": False,
              "message_stats_input_queue": 0,
              "message_stats_output_queue": 0,
              "min_acceptable_hold_time": 3,
              "minimum_time_between_adv_runs": 30,
              "multiprotocol_capability": "received",
              "non_stop_routing": True,
              "nsr_state": "None",
              "outbound_message": "3",
              "precedence": "internet",
              "remote_as": "65107.65107",
              "router_id": "10.10.10.107",
              "second_attempted": 19,
              "second_last_write": "00:01:15",
              "second_last_write_before_attempted": 0,
              "second_last_write_before_reset": "00:00:00",
              "second_last_write_before_written": 0,
              "second_written": 19,
              "session_state": "established",
              "tcp_initial_sync": "---",
              "tcp_initial_sync_done": "---",
              "up_time": "02:23:56",
              "written": 19
            }
          }
        }
      }
    }
  }
}
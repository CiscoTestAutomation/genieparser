expected_output = {
  "instance": {
    "default": {
      "vrf": {
        "default": {
          "active_cluster_id": "10.10.10.108",
          "address_family": {
            "ipv4 unicast": {
              "attribute_download": "Disabled",
              "bgp_table_version": "8",
              "chunk_elememt_size": "3",
              "client_to_client_reflection": True,
              "dampening": False,
              "dynamic_med": True,
              "dynamic_med_int": "10 minutes",
              "dynamic_med_periodic_timer": "Not Running",
              "dynamic_med_timer": "Not Running",
              "label_retention_timer_value": "5 mins",
              "main_table_version": "8",
              "nexthop_resolution_minimum_prefix_length": "0 (not configured)",
              "num_of_scan_segments": "1",
              "permanent_network": "unconfigured",
              "prefix_scanned_per_segment": "100000",
              "prefixes_path": {
                "prefixes": {
                  "mem_used": 368,
                  "number": 4
                }
              },
              "remote_local": {
                "prefixes": {
                  "allocated": 4,
                  "freed": 0
                }
              },
              "rib_table_prefix_limit_reached": "no",
              "rib_table_prefix_limit_ver": "0",
              "scan_interval": "60",
              "soft_reconfig_entries": "0",
              "state": "normal mode",
              "table_bit_field_size": "1 ",
              "table_version_acked_by_rib": "8",
              "table_version_synced_to_rib": "8",
              "thread": {
                "import thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 8,
                      "trig_tid": 3,
                      "ver": 8
                    }
                  }
                },
                "rib thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 8,
                      "trig_tid": 3,
                      "ver": 8
                    }
                  }
                },
                "update thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 8,
                      "trig_tid": 3,
                      "ver": 8
                    }
                  }
                }
              },
              "total_prefixes_scanned": "4"
            },
            "ipv6 unicast": {
              "attribute_download": "Disabled",
              "bgp_table_version": "10",
              "chunk_elememt_size": "3",
              "client_to_client_reflection": True,
              "dampening": False,
              "dynamic_med": False,
              "dynamic_med_int": "10 minutes",
              "dynamic_med_periodic_timer": "Not Running",
              "dynamic_med_timer": "Not Running",
              "label_retention_timer_value": "5 mins",
              "main_table_version": "10",
              "nexthop_resolution_minimum_prefix_length": "0 (not configured)",
              "num_of_scan_segments": "1",
              "permanent_network": "unconfigured",
              "prefix_scanned_per_segment": "100000",
              "prefixes_path": {
                "prefixes": {
                  "mem_used": 520,
                  "number": 5
                }
              },
              "remote_local": {
                "prefixes": {
                  "allocated": 5,
                  "freed": 0
                }
              },
              "rib_table_prefix_limit_reached": "no",
              "rib_table_prefix_limit_ver": "0",
              "scan_interval": "60",
              "soft_reconfig_entries": "0",
              "state": "normal mode",
              "table_bit_field_size": "1 ",
              "table_version_acked_by_rib": "10",
              "table_version_synced_to_rib": "10",
              "thread": {
                "import thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 10,
                      "trig_tid": 3,
                      "ver": 10
                    }
                  }
                },
                "rib thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 10,
                      "trig_tid": 3,
                      "ver": 10
                    }
                  }
                },
                "update thread": {
                  "triggers": {
                    "Aug 21 18:23:12.249": {
                      "tbl_ver": 10,
                      "trig_tid": 3,
                      "ver": 10
                    }
                  }
                }
              },
              "total_prefixes_scanned": "5"
            }
          },
          "as_number": "65108.65108",
          "as_system_number_format": "ASDOT",
          "att": {
            "as_paths": {
              "memory_used": 486,
              "number": 1
            },
            "attributes": {
              "memory_used": 496,
              "number": 2
            },
            "communities": {
              "memory_used": 0,
              "number": 0
            },
            "extended_communities": {
              "memory_used": 0,
              "number": 0
            },
            "nexthop_entries": {
              "memory_used": 10960,
              "number": 14
            },
            "paths": {
              "memory_used": 384,
              "number": 6
            },
            "pe_distinguisher_labels": {
              "memory_used": 0,
              "number": 0
            },
            "pmsi_tunnel_attr": {
              "memory_used": 0,
              "number": 0
            },
            "ppmp_attr": {
              "memory_used": 0,
              "number": 0
            },
            "ribrnh_tunnel_attr": {
              "memory_used": 0,
              "number": 0
            },
            "route_reflector_entries": {
              "memory_used": 0,
              "number": 0
            }
          },
          "bgp_speaker_process": 0,
          "default_cluster_id": "10.10.10.108",
          "default_keepalive": 60,
          "default_local_preference": 100,
          "default_value_for_bmp_buffer_size": 307,
          "enforce_first_as": True,
          "fast_external_fallover": True,
          "generic_scan_interval": 60,
          "log_neighbor_changes": True,
          "max_limit_for_bmp_buffer_size": 409,
          "message_logging_pool_summary": {
            "100": {
              "alloc": 6,
              "free": 0
            },
            "200": {
              "alloc": 2,
              "free": 0
            },
            "2200": {
              "alloc": 0,
              "free": 0
            },
            "4500": {
              "alloc": 0,
              "free": 0
            },
            "500": {
              "alloc": 0,
              "free": 0
            }
          },
          "node": "node0_0_CPU0",
          "non_stop_routing": True,
          "operation_mode": "standalone",
          "platform_rlimit_max": 2147483648,
          "pool": {
            "1200": {
              "alloc": 0,
              "free": 0
            },
            "200": {
              "alloc": 0,
              "free": 0
            },
            "20000": {
              "alloc": 0,
              "free": 0
            },
            "2200": {
              "alloc": 0,
              "free": 0
            },
            "300": {
              "alloc": 215,
              "free": 214
            },
            "3300": {
              "alloc": 0,
              "free": 0
            },
            "400": {
              "alloc": 1,
              "free": 1
            },
            "4000": {
              "alloc": 0,
              "free": 0
            },
            "4500": {
              "alloc": 0,
              "free": 0
            },
            "500": {
              "alloc": 1,
              "free": 1
            },
            "5000": {
              "alloc": 0,
              "free": 0
            },
            "600": {
              "alloc": 3,
              "free": 3
            },
            "700": {
              "alloc": 0,
              "free": 0
            },
            "800": {
              "alloc": 0,
              "free": 0
            },
            "900": {
              "alloc": 0,
              "free": 0
            }
          },
          "received_notifications": 0,
          "received_updates": 4,
          "restart_count": 1,
          "router_id": "10.10.10.108",
          "sent_notifications": 0,
          "sent_updates": 5,
          "update_delay": 120,
          "vrf_info": {
            "default": {
              "cfg": 2,
              "nbrs_estab": 2,
              "total": 1
            },
            "non-default": {
              "cfg": 0,
              "nbrs_estab": 0,
              "total": 0
            }
          }
        }
      }
    }
  }
}
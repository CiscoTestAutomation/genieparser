expected_output = {
  "instance": {
    "default": {
      "vrf": {
        "default": {
          "address_family": {
            "ipv4 unicast": {
              "generic_scan_interval": 60,
              "local_as": "65108.65108",
              "non_stop_routing": True,
              "nsr_initial_init_ver_status": "reached",
              "nsr_initial_initsync_version": "3",
              "nsr_issu_sync_group_versions": "0/0",
              "processed_paths": 3,
              "processed_prefixes": 3,
              "rd_version": 8,
              "router_identifier": "10.10.10.108",
              "routes": {
                "10.10.10.0/24": {
                  "index": {
                    1: {
                      "metric": "0",
                      "next_hop": "10.10.10.107",
                      "origin_codes": "?",
                      "path": "65107.65107",
                      "status_codes": "*",
                      "weight": "0"
                    }
                  }
                },
                "10.7.7.7/32": {
                  "index": {
                    1: {
                      "metric": "0",
                      "next_hop": "10.10.10.107",
                      "origin_codes": "?",
                      "path": "65107.65107",
                      "status_codes": "*>",
                      "weight": "0"
                    }
                  }
                },
                "192.168.52.0/24": {
                  "index": {
                    1: {
                      "metric": "0",
                      "next_hop": "10.10.10.107",
                      "origin_codes": "?",
                      "path": "65107.65107",
                      "status_codes": "*",
                      "weight": "0"
                    }
                  }
                }
              },
              "routing_table_version": 8,
              "scan_interval": 60,
              "table_id": "0xe0000000",
              "table_state": "active"
            }
          }
        }
      }
    }
  }
}
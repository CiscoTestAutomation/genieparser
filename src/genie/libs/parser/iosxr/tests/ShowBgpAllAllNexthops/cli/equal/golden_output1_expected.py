expected_output = {
  "vrf": {
    "default": {
      "address_family": {
        "VPNv4 Unicast": {
          "total_next_hop": {
            "time_spent_secs": 0.0
          },
          "maximum_next_hop": {
            "received": "00:00:00",
            "best_paths_deleted": 0,
            "best_paths_changed": 0,
            "time_spent_secs": 0.0
          },
          "last_notification": {
            "received": "00:12:06",
            "time_spent_secs": 0.0
          },
          "gateway_address_family": "IPv4 Unicast",
          "table_id": "0xe0000000",
          "next_hop_count": 2,
          "critical_trigger_delay": "0msec",
          "non_critical_trigger_delay": "10000msec",
          "next_hop_version": 1,
          "rib_version": 1,
          "epe_table_version": 1,
          "epe_label_version": 1,
          "epe_downloaded_version": 1,
          "epe_standby_version": 1,
          "next_hops": {
            "108.10.10.1": {
              "status": [
                "R",
                "NC",
                "NL"
              ],
              "metric": 2,
              "tbl_id": "e0000000",
              "notf": "1/0",
              "last_rib_event": "00:13:49 (Cri)",
              "ref_count": "0/4"
            },
            "109.10.10.1": {
              "status": [
                "R",
                "NC",
                "NL"
              ],
              "metric": 2,
              "tbl_id": "e0000000",
              "notf": "1/0",
              "last_rib_event": "00:12:08 (Cri)",
              "ref_count": "0/4"
            }
          }
        }
      }
    }
  }
}
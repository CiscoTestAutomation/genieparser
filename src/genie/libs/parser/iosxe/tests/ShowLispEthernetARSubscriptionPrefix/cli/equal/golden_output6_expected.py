expected_output = {
  "lisp_id": {
    0: {
      "instance_id": {
        4100: {
          "eid_table": "N/A",
          "entries": 2,
          "eid_prefix": {
            "192.168.1.3/32": {
              "source": "remote-eid",
              "up_time": "00:42:38",
              "last_change": "00:42:38",
              "map_server": {
                "100.44.44.44": {
                  "state": "Subs Acked",
                },
                "100.55.55.55": {
                  "state": "Subs Acked",
                }
              }
            },
            "2001:192:168:1::1/128": {
              "source": "remote-eid",
              "up_time": "00:42:18",
              "last_change": "00:42:18",
              "map_server": {
                "100.44.44.44": {
                  "state": "Subs Acked",
                },
                "100.55.55.55": {
                  "state": "Subs Acked",
                }
              }
            }
          }
        }
      }
    }
  }
}

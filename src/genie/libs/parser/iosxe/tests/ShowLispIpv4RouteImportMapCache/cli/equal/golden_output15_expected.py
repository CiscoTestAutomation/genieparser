expected_output = {
  "lisp_id": {
    0: {
      "instance_id": {
        102: {
          "eid_table": "blue",
          "config": 2,
          "entries": 1,
          "limit": 5000,
          "eids": {
            "50.1.1.0/24": {
              "source": "static",
              "cache_db": "installed",
              "uptime": "20:36:45"
            }
          }
        },
        104: {
          "eid_table": "default",
          "config": 1,
          "entries": 1,
          "limit": 5000,
          "eids": {
            "50.1.1.0/24": {
              "source": "static",
              "cache_db": "installed",
              "uptime": "16:08:02"
            }
          }
        }
      }
    },
    1: {
      "instance_id": {
        105: {
          "eid_table": "red",
          "config": 1,
          "entries": 1,
          "limit": 5000,
          "eids": {
            "50.1.0.0/16": {
              "source": "static",
              "cache_db": "installed",
              "uptime": "00:00:03"
            }
          }
        }
      }
    }
  }
}

expected_output = {
  "instance": {
    "default": {
      "vrf": {
        "default": {
          "address_family": {
            "ipv4 unicast": {
              "advertised": {
                "10.10.10.0/24": {
                  "index": {
                    1: {
                      "froms": "Local",
                      "next_hop": "10.10.10.108",
                      "origin_code": "?",
                      "path": "65108.65108"
                    }
                  }
                },
                "10.8.8.8/32": {
                  "index": {
                    1: {
                      "froms": "Local",
                      "next_hop": "10.10.10.108",
                      "origin_code": "?",
                      "path": "65108.65108"
                    }
                  }
                },
                "192.168.52.0/24": {
                  "index": {
                    1: {
                      "froms": "Local",
                      "next_hop": "10.10.10.108",
                      "origin_code": "?",
                      "path": "65108.65108"
                    }
                  }
                }
              },
              "processed_paths": "3",
              "processed_prefixes": "3"
            }
          }
        }
      }
    }
  }
}
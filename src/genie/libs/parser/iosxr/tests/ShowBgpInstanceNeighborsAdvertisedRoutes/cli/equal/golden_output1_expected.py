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
                },
                "82.102.71.0/24": {
                  "index": {
                    1: {
                      "froms": "193.22.30.151",
                      "next_hop": "213.140.196.25",
                      "origin_code": "i",
                      "path": "(64612) 8544"
                    }
                  }
                },
                "82.102.72.0/24": {
                  "index": {
                    1: {
                      "froms": "193.22.30.151",
                      "next_hop": "213.140.196.25",
                      "origin_code": "i",
                      "path": "(64612) 8544 30916"
                    }
                  }
                }
              },
              "processed_paths": "5",
              "processed_prefixes": "5"
            }
          }
        }
      }
    }
  }
}
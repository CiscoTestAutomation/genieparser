expected_output = {
  "vrf": {
    "default": {
      "address_family": {
        "ipv4 unicast": {
          "network": {
            "111.111.111.111/32": {
              "next_hops": {
                "108.10.0.2": {
                  "metric": 0,
                  "locprf": 100,
                  "weight": 65401,
                  "path": "i"
                },
                "108.11.0.2": {
                  "metric": 0,
                  "locprf": 0,
                  "weight": 65401,
                  "path": "i"
                }
              }
            }
          }
        }
      }
    }
  }
}
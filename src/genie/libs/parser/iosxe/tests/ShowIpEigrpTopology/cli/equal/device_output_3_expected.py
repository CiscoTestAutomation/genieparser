expected_output = {
  "eigrp_instance": {
    "100": {
      "vrf": {
        "1": {
          "address_family": {
            "IPv4": {
              "eigrp_id": {
                "10.114.254.5": {
                  "eigrp_routes": {
                    "10.114.11.12/30": {
                      "FD": 1310720,
                      "known_via": "Connected",
                      "outgoing_interface": "GigabitEthernet0/0/0.1",
                      "route": "10.114.11.12/30",
                      "route_code": "P",
                      "route_type": "Passive",
                      "successor_count": 1
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
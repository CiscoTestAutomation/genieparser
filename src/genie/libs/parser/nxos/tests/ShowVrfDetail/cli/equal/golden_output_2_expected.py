

expected_output = {
     "VRF1": {
          "max_routes": 20000,
          "state": "up",
          "vrf_id": 3,
          "address_family": {
               "ipv6": {
                    "table_id": "0x80000003",
                    "state": "up",
                    "fwd_id": "0x80000003"
               },
               "ipv4": {
                    "table_id": "0x00000003",
                    "state": "up",
                    "fwd_id": "0x00000003"
               }
          },
          "mid_threshold": 17000,
          "route_distinguisher": "300:1"
     }}

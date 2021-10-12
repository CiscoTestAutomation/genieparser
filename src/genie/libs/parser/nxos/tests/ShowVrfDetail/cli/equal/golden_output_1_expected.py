

expected_output = {
    "management": {
          "max_routes": 0,
          "state": "up",
          "vrf_id": 2,
          "address_family": {
               "ipv6": {
                    "table_id": "0x80000002",
                    "state": "up",
                    "fwd_id": "0x80000002"
               },
               "ipv4": {
                    "table_id": "0x00000002",
                    "state": "up",
                    "fwd_id": "0x00000002"
               }
          },
          "mid_threshold": 0,
          "route_distinguisher": "0:0"
     },
     "default": {
          "max_routes": 0,
          "state": "up",
          "vrf_id": 1,
          "address_family": {
               "ipv6": {
                    "table_id": "0x80000001",
                    "state": "up",
                    "fwd_id": "0x80000001"
               },
               "ipv4": {
                    "table_id": "0x00000001",
                    "state": "up",
                    "fwd_id": "0x00000001"
               }
          },
          "mid_threshold": 0,
          "route_distinguisher": "0:0"
     },
     "VRF2": {
          "max_routes": 0,
          "state": "up",
          "vrf_id": 4,
          "address_family": {
               "ipv6": {
                    "table_id": "0x80000004",
                    "state": "up",
                    "fwd_id": "0x80000004"
               },
               "ipv4": {
                    "table_id": "0x00000004",
                    "state": "up",
                    "fwd_id": "0x00000004"
               }
          },
          "mid_threshold": 0,
          "route_distinguisher": "400:1"
     },
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
     }
}

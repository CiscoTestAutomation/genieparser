expected_output = {
  "instance": {
    "1": {
      "areas": {
        "0.0.0.0": {
          "interfaces": {
            "GigabitEthernet3": {
              "cost": 1,
              "ip_address": "100.3.4.4/24",
              "nbrs_count": 0,
              "nbrs_full": 0,
              "state": "P2P"
            },
            "GigabitEthernet4": {
              "cost": 1,
              "ip_address": "100.2.4.4/24",
              "nbrs_count": 1,
              "nbrs_full": 1,
              "state": "P2P"
            },
            "Loopback0": {
              "cost": 1,
              "ip_address": "100.255.255.4/32",
              "nbrs_count": 0,
              "nbrs_full": 0,
              "state": "LOOP"
            }
          }
        },
        "0.0.0.2": {
          "interfaces": {
            "GigabitEthernet5": {
              "cost": 1,
              "ip_address": "100.1.4.4/24",
              "nbrs_count": 0,
              "nbrs_full": 0,
              "state": "P2P"
            }
          }
        }
      }
    },
    "200": {
      "areas": {
        "0.0.0.0": {
          "interfaces": {
            "GigabitEthernet6": {
              "cost": 1,
              "ip_address": "100.4.11.4/24",
              "nbrs_count": 0,
              "nbrs_full": 0,
              "state": "P2P"
            },
            "GigabitEthernet7": {
              "cost": 1,
              "ip_address": "100.4.12.4/24",
              "nbrs_count": 1,
              "nbrs_full": 1,
              "state": "P2P"
            }
          }
        }
      }
    }
  }
}
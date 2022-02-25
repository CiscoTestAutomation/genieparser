expected_output={
  "vrf": {
    "vrf3001": {
      "address_family": {
        "ipv4": {
          "multicast_group": {
            "229.1.0.0/16": {
              "source_address": {
                "*": {
                  "expire": "-",
                  "flags": "B",
                  "incoming_interface_list": {
                    "Lspvif2": {
                      "state": "Accepting/Sparse"
                    },
                    "Vlan3001": {
                      "state": "Accepting/Sparse"
                    }
                  },
                  "msdp_learned": False,
                  "rp": "30.0.1.1",
                  "rp_bit": False,
                  "upstream_interface": {
                    "Lspvif2": {
                      "rpf_nbr": "1.1.1.1"
                    }
                  },
                  "uptime": "00:03:58"
                }
              }
            }
          }
        }
      }
    }
  }
}

expected_output = {
    "vrf":
      {
        "red":
          {
            "address_family":
              {
                "ipv4":
                  {
                    "instance":
                      {
                        1:
                          {
                            "router_id": "100.1.1.1",
                            "network":
                              {
                                "11.1.1.0/24":
                                  {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 200,
                                    "origin": "bgp 100",
                                    "via_network": "None",
                                    "interface": "192.46.1.6",
                                  },
                                "14.1.1.0/24":
                                  {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 200,
                                    "origin": "bgp 100",
                                    "via_network": "None",
                                    "interface": "192.46.1.6",
                                  },
                                "67.1.1.0/24":
                                  {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 200,
                                    "origin": "bgp 100",
                                    "via_network": "None",
                                    "interface": "192.46.1.6",
                                  },
                                "172.168.36.0/24":
                                  {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 200,
                                    "origin": "bgp 100",
                                    "via_network": "None",
                                    "interface": "192.46.1.6",
                                  },
                                "172.168.56.0/24":
                                  {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 200,
                                    "origin": "bgp 100",
                                    "via_network": "None",
                                    "interface": "192.46.1.6",
                                  },
                                "192.46.1.0/24":
                                  {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected",
                                    "via_network": "None",
                                    "interface": "GigabitEthernet0/0/1",
                                  },
                              },
                          },
                      },
                  },
                "ipv6":
                  {
                    "instance":
                      {
                        1:
                          {
                            "router_id": "100.1.1.1",
                            "network":
                              {
                                "33::2/128":
                                  {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (connected)",
                                    "via_network": "None",
                                    "interface": "Loopback1",
                                  },
                              },
                          },
                      },
                  },
              },
          },
      },
  }
  

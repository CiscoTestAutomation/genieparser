expected_output= {
  "vrf": {
    "vrf3001": {
      "local_label": {
        21: {
          "outgoing_label_or_vc": {
            "No Label": {
              "prefix_or_tunnel_id": {
                "121.1.1.0/24[V]": {
                  "outgoing_interface": {
                    "Aggregate/vrf3001": {
                      "bytes_label_switched": 10980
                    }
                  }
                }
              }
            }
          }
        },
        23: {
          "outgoing_label_or_vc": {
            "No Label": {
              "prefix_or_tunnel_id": {
                "3001:1": {
                  "outgoing_interface": {
                    "Aggregate/vrf3001": {
                      "bytes_label_switched": 200497062836
                    }
                  },
                  "prefix_no": 0,
                  "prefix_type": "mdt"
                }
              }
            }
          }
        },
        33: {
          "outgoing_label_or_vc": {
            "Pop Label": {
              "prefix_or_tunnel_id": {
                "30.0.1.1/32[V]": {
                  "outgoing_interface": {
                    "Aggregate/vrf3001": {
                      "bytes_label_switched": 45252090
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

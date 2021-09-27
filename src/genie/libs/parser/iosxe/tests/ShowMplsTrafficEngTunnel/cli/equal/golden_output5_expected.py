expected_output={
  "tunnel_type": {
    "p2mp_sub_lsps": {
      "tunnel_name": {}
    },
    "p2mp_tunnels": {
      "tunnel_name": {}
    },
    "p2p_tunnels": {
      "tunnel_name": {
        "Tunnel100": {
          "inlabel": [
            "Port-channel20",
            "implicit-null"
          ],
          "outlabel": [
            "-"
          ],
          "prev_hop": [
            "192.1.1.1"
          ],
          "rsvp_signalling_info": {
            "dst": "2.2.2.2",
            "rsvp_path_info": {
              "explicit_route": [
                "NONE"
              ],
              "my_address": "2.2.2.2",
              "record_route": "NONE",
              "tspec": {
                "ave_rate": 500,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 500,
                "peak_rate_unit": "kbits"
              }
            },
            "rsvp_resv_info": {
              "fspec": {
                "ave_rate": 500,
                "ave_rate_unit": "kbits",
                "burst": 1000,
                "burst_unit": "bytes",
                "peak_rate": 500,
                "peak_rate_unit": "kbits"
              },
              "record_route": "NONE"
            },
            "src": "3.3.3.3",
            "tun_id": 100,
            "tun_instance": 1481
          },
          "signalled_state": True,
          "tunnel_state": "up"
        }
      }
    }
  }
}

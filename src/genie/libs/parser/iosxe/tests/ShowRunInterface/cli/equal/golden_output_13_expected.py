
expected_output={
  "interfaces": {
    "Tunnel100": {
      "autoroute_announce": "enabled",
      "src_ip": "Loopback0",
      "tunnel_bandwidth": 500,
      "tunnel_dst": "2.2.2.2",
      "tunnel_mode": "mpls traffic-eng",
      "tunnel_path_option": {
        "1": {
          "path_type": "dynamic"
        }
      },
      "tunnel_priority": [
        "7 7"
      ]
    }
  }
}

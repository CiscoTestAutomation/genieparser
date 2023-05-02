expected_output = {
   "FastEthernet0/1": {
      "model": "WS-C3560-48TS",
      "type": "10/100BaseTX",
      "speed": [
         "10",
         "100",
         "auto"
      ],
      "duplex": [
         "half",
         "full",
         "auto"
      ],
      "trunk_encap_type": "802.1Q,ISL",
      "trunk_mode": [
         "on",
         "off",
         "desirable",
         "nonegotiate"
      ],
      "channel": True,
      "broadcast_suppression": "percentage(0-100)",
      "flowcontrol": {
         "flowcontrol_rx": [
            "off",
            "on",
            "desired"
         ],
         "flowcontrol_tx": [
            "none"
         ]
      },
      "fast_start": True,
      "qos_scheduling": {
         "qos_scheduling_rx": "not configurable on per port basis",
         "qos_scheduling_tx": "4q3t"
      },
      "udld": True,
      "inline_power": False,
      "span": "source/destination",
      "portsecure": True,
      "dot1x": True
   }
}
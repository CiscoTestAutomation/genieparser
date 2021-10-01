expected_output = {
  "number_of_aggregators": 5,
  "interfaces": {
    "Port-channel1": {
      "name": "Port-channel1",
      "bundle_id": 1,
      "flags": "SD",
      "oper_status": "down"
    },
    "Port-channel2": {
      "name": "Port-channel2",
      "bundle_id": 2,
      "flags": "SD",
      "oper_status": "down"
    },
    "Port-channel3": {
      "name": "Port-channel3",
      "bundle_id": 3,
      "protocol": "lacp",
      "flags": "SU",
      "oper_status": "up",
      "members": {
        "TenGigabitEthernet2/0/1": {
          "interface": "TenGigabitEthernet2/0/1",
          "flags": "P",
          "bundled": True,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        },
        "TenGigabitEthernet2/0/2": {
          "interface": "TenGigabitEthernet2/0/2",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        },
        "TenGigabitEthernet2/0/3": {
          "interface": "TenGigabitEthernet2/0/3",
          "flags": "s",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        },
        "TenGigabitEthernet3/0/1": {
          "interface": "TenGigabitEthernet3/0/1",
          "flags": "s",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        },
        "TenGigabitEthernet3/0/2": {
          "interface": "TenGigabitEthernet3/0/2",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        },
        "TenGigabitEthernet3/0/3": {
          "interface": "TenGigabitEthernet3/0/3",
          "flags": "P",
          "bundled": True,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel3"
          }
        }
      },
      "port_channel": {
        "port_channel_member": True,
        "port_channel_member_intfs": [
          "TenGigabitEthernet2/0/1",
          "TenGigabitEthernet2/0/2",
          "TenGigabitEthernet2/0/3",
          "TenGigabitEthernet3/0/1",
          "TenGigabitEthernet3/0/2",
          "TenGigabitEthernet3/0/3"
        ]
      }
    },
    "Port-channel4": {
      "name": "Port-channel4",
      "bundle_id": 4,
      "protocol": "lacp",
      "flags": "RD",
      "oper_status": "down",
      "members": {
        "FiveGigabitEthernet1/0/5": {
          "interface": "FiveGigabitEthernet1/0/5",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel4"
          }
        },
        "GigabitEthernet4/0/5": {
          "interface": "GigabitEthernet4/0/5",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel4"
          }
        }
      },
      "port_channel": {
        "port_channel_member": True,
        "port_channel_member_intfs": [
          "FiveGigabitEthernet1/0/5",
          "GigabitEthernet4/0/5"
        ]
      }
    },
    "Port-channel5": {
      "name": "Port-channel5",
      "bundle_id": 5,
      "protocol": "lacp",
      "flags": "RD",
      "oper_status": "down",
      "members": {
        "TenGigabitEthernet2/0/4": {
          "interface": "TenGigabitEthernet2/0/4",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel5"
          }
        },
        "TenGigabitEthernet3/0/4": {
          "interface": "TenGigabitEthernet3/0/4",
          "flags": "D",
          "bundled": False,
          "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel5"
          }
        }
      },
      "port_channel": {
        "port_channel_member": True,
        "port_channel_member_intfs": [
          "TenGigabitEthernet2/0/4",
          "TenGigabitEthernet3/0/4"
        ]
      }
    }
  }
}
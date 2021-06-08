expected_output = {
    "interfaces": {
        "Ethernet1/1": {
            "port_id": {
                "TenGigE0/1/0/4/0": {
                    "neighbors": {
                        "ROUTER_Y": {
                            "chassis_id": "4321.abcd.1234",
                            "port_description": "BAR",
                            "system_name": "ROUTER_Y",
                            "system_description": "Cisco IOS XR Software, Version 5.3.4[Default]Copyright (c) 2018 by Cisco Systems, Inc., ASR9K Series\n",
                            "time_remaining": 92,
                            "capabilities": {
                                "router": {
                                    "name": "router",
                                    "system": True,
                                    "enabled": True,
                                }
                            },
                            "management_address_v4": "not advertised",
                            "management_address_v6": "not advertised",
                            "vlan_id": "not advertised",
                        }
                    }
                }
            }
        },
        "Ethernet1/5": {
            "port_id": {
                "TenGigabitEthernet0/1/0/5/0": {
                    "neighbors": {
                        "R1_xe.cisco.com": {
                            "chassis_id": "4321.abcd.1234",
                            "port_description": "GigabitEthernet6",
                            "system_name": "R1_xe.cisco.com",
                            "system_description": "Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2018 by Cisco Systems, Inc.\nCompiled Tue 17-Jul-18 16:57 by mcp",
                            "time_remaining": 95,
                            "capabilities": {
                                "bridge": {"name": "bridge", "system": True},
                                "router": {
                                    "name": "router",
                                    "system": True,
                                    "enabled": True,
                                },
                            },
                            "management_address_v4": "172.16.1.73",
                            "management_address_v6": "2001:10:12:90::1",
                            "vlan_id": "not advertised",
                        }
                    }
                }
            }
        },
        "Ethernet1/6": {
            "port_id": {
                "GigabitEthernet7": {
                    "neighbors": {
                        "R1_xe.cisco.com": {
                            "chassis_id": "4321.abcd.1234",
                            "port_description": "GigabitEthernet7",
                            "system_name": "R1_xe.cisco.com",
                            "system_description": "Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2018 by Cisco Systems, Inc.\nCompiled Tue 17-Jul-18 16:57 by mcp",
                            "time_remaining": 100,
                            "capabilities": {
                                "bridge": {"name": "bridge", "system": True},
                                "router": {
                                    "name": "router",
                                    "system": True,
                                    "enabled": True,
                                },
                            },
                            "management_address_v4": "172.16.1.73",
                            "management_address_v6": "2001:10:12:90::1",
                            "vlan_id": "not advertised",
                        }
                    }
                }
            }
        },
    },
    "total_entries": 2,
}
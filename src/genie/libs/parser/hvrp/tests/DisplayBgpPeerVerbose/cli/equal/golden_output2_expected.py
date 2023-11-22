
expected_output = {
    "vrf": {
        "default": {
            "peer": {
                "10.10.10.10": {
                    "remote_as": "65000",
                    "peer_type": "EBGP link",
                    "description": "TEST",
                    "bgp_version": 4,
                    "remote_router_id": "3.3.3.3",
                    "update_group_id": 1,
                    "current_state": "Idle(Admin)",
                    "last_state": "Established",
                    "peer_up_count": 3,
                    "messages_counters": {
                        "received": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "FROM_RRVPN",
                        "export": "KEEP_MED"
                    }
                },
                "11.11.11.11": {
                    "remote_as": "65000",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "1.1.1.1",
                    "update_group_id": 2,
                    "current_state": "Established",
                    "up_time": "26d05h20m49s",
                    "last_state": "OpenConfirm",
                    "peer_up_count": 7,
                    "prefixes_counters": {
                        "received": 40,
                        "active": 24,
                        "advertised": 16
                    },
                    "transport": {
                        "local_port": 49801,
                        "remote_port": 179
                    },
                    "capabilities": {
                        "multi-protocol extension": "",
                        "route refresh capability": "",
                        "4-byte-as capability": "",
                        "VPNv4 Unicast": "advertised and received"
                    },
                    "messages_counters": {
                        "received": {
                            "total": 238538,
                            "update": 713,
                            "open": 1,
                            "keepalive": 237824,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 272113,
                            "update": 35,
                            "open": 1,
                            "keepalive": 272077,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "FROM_RRVPN",
                        "export": "KEEP_MED"
                    }
                },
                "20.20.20.20": {
                    "remote_as": "65000",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "1.1.1.1",
                    "update_group_id": 2,
                    "current_state": "Established",
                    "up_time": "26d05h21m00s",
                    "last_state": "OpenConfirm",
                    "peer_up_count": 4,
                    "prefixes_counters": {
                        "received": 40,
                        "active": 0,
                        "advertised": 16
                    },
                    "transport": {
                        "local_port": 55630,
                        "remote_port": 179
                    },
                    "capabilities": {
                        "multi-protocol extension": "",
                        "route refresh capability": "",
                        "4-byte-as capability": "",
                        "VPNv4 Unicast": "advertised and received"
                    },
                    "messages_counters": {
                        "received": {
                            "total": 238537,
                            "update": 693,
                            "open": 1,
                            "keepalive": 237843,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 272150,
                            "update": 36,
                            "open": 1,
                            "keepalive": 272113,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "FROM_RRVPN",
                        "export": "KEEP_MED"
                    }
                }
            }
        },
        "mobile": {
            "peer": {
                "5.5.5.5": {
                    "remote_as": "64535",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "0.0.0.0",
                    "update_group_id": 4,
                    "current_state": "Idle",
                    "last_state": "Idle",
                    "peer_up_count": 0,
                    "messages_counters": {
                        "received": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "SET-WEIGHT"
                    }
                },
                "30.30.30.30": {
                    "remote_as": "64535",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "1.1.1.1",
                    "update_group_id": 5,
                    "current_state": "Established",
                    "up_time": "33d23h00m11s",
                    "last_state": "OpenConfirm",
                    "peer_up_count": 1,
                    "prefixes_counters": {
                        "received": 5,
                        "active": 4,
                        "advertised": 1
                    },
                    "transport": {
                        "local_port": 50166,
                        "remote_port": 179
                    },
                    "capabilities": {
                        "multi-protocol extension": "",
                        "route refresh capability": "",
                        "4-byte-as capability": "",
                        "IPv4 Unicast": "advertised and received"
                    },
                    "messages_counters": {
                        "received": {
                            "total": 54338,
                            "update": 982,
                            "open": 1,
                            "keepalive": 53355,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 56184,
                            "update": 2,
                            "open": 1,
                            "keepalive": 56181,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "SET-WEIGHT"
                    }
                },
                "40.40.40.40": {
                    "remote_as": "64535",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "0.0.0.0",
                    "update_group_id": 4,
                    "current_state": "Active",
                    "last_state": "Connect",
                    "peer_up_count": 0,
                    "messages_counters": {
                        "received": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "SET-WEIGHT"
                    }
                },
                "50.50.50.50": {
                    "remote_as": "64535",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "0.0.0.0",
                    "update_group_id": 4,
                    "current_state": "Idle",
                    "last_state": "Idle",
                    "peer_up_count": 0,
                    "messages_counters": {
                        "received": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "SET-WEIGHT"
                    }
                },
                "60.60.60.60": {
                    "remote_as": "64535",
                    "peer_type": "EBGP link",
                    "bgp_version": 4,
                    "remote_router_id": "1.1.1.1",
                    "update_group_id": 4,
                    "current_state": "Idle",
                    "last_state": "Established",
                    "peer_up_count": 1,
                    "messages_counters": {
                        "received": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        },
                        "sent": {
                            "total": 0,
                            "update": 0,
                            "open": 0,
                            "keepalive": 0,
                            "notification": 0,
                            "refresh": 0
                        }
                    },
                    "route_update_interval": "30",
                    "route_policies": {
                        "import": "SET-WEIGHT"
                    }
                }
            }
        }
    }
}

expected_output = {
    "pvst": {
        "vlans": {
            100: {
                "topology_from_port": "Port-channel12",
                "topology_detected_flag": False,
                "topology_change_flag": False,
                "bridge_address": "3820.56ff.76db",
                "forwarding_delay": 15,
                "topology_change_times": 35,
                "hello_timer": 0,
                "hello_time": 2,
                "bridge_sysid": 100,
                "aging_timer": 300,
                "hold_time": 1,
                "bridge_priority": 24576,
                "notification_times": 2,
                "topology_changes": 1,
                "notification_timer": 0,
                "root_of_spanning_tree": True,
                "interfaces": {
                    "Port-channel12": {
                        "designated_bridge_priority": 24676,
                        "link_type": "point-to-point",
                        "hold": 0,
                        "counters": {"bpdu_sent": 183, "bpdu_received": 0},
                        "port_num": 2388,
                        "message_age": 0,
                        "number_of_forward_transitions": 1,
                        "designated_path_cost": 0,
                        "forward_delay": 0,
                        "name": "Port-channel12",
                        "designated_root_priority": 24676,
                        "designated_bridge_address": "3820.56ff.76db",
                        "status": "designated forwarding",
                        "port_identifier": "128.2388.",
                        "designated_root_address": "3820.56ff.76db",
                        "cost": 3,
                        "port_priority": 128,
                        "designated_port_id": "128.2388",
                    }
                },
                "vlan_id": 100,
                "max_age": 20,
                "topology_change_timer": 0,
                "time_since_topology_change": "00:05:37",
            }
        },
        "hello_time": 2,
        "max_age": 20,
        "forwarding_delay": 15,
    }
}

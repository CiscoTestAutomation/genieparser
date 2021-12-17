expected_output = {
    "lisp_id": {
        0: {
            "instance_id": {
                101: {
                    "client_name": "Test 0",
                    "process_id": 871,
                    "connection_to_control_process": "DISABLED",
                    "ipc_endpoint": 1,
                    "client_notifications": "Pending",
                    "address_family": "IPv4",
                    "eid_table": "vrf default",
                    "entry_count": 1,
                    "prefix": "0.0.0.0/0",
                    "watched_entries": ["1.1.1.1", "1.1.1.2"],
                },
                102: {
                    "client_name": "Test11",
                    "process_id": 817,
                    "connection_to_control_process": "ENABLED",
                    "ipc_endpoint": 2,
                    "client_notifications": "Delivered",
                    "address_family": "IPv6",
                    "eid_table": "vrf default",
                    "entry_count": 1,
                    "prefix": "::/0",
                    "watched_entries": [
                        "E80::AEDE:48FF:FE00:1111",
                        "E80::AEDE:48FF:FE00:1112",
                    ],
                },
            }
        },
        1: {
            "instance_id": {
                102: {
                    "client_name": "Ok",
                    "process_id": 187,
                    "connection_to_control_process": "ENABLED",
                    "ipc_endpoint": 1,
                    "client_notifications": "Delivered",
                    "address_family": "MAC",
                    "eid_table": "Vlan 101",
                    "entry_count": 1,
                    "prefix": "0000.0000.0000/0",
                    "watched_entries": ["f100.a551.0501", "f100.a551.0502"],
                }
            }
        },
        2: {"instance_id": {}},
        3: {
            "instance_id": {
                103: {
                    "client_name": "Ok",
                    "process_id": 187,
                    "connection_to_control_process": "ENABLED",
                    "ipc_endpoint": 1,
                    "client_notifications": "Delivered",
                    "address_family": "MAC",
                    "eid_table": "Vlan 101",
                    "entry_count": 3,
                    "prefix": "0000.0000.0000/0",
                    "watched_entries": ["ffff.aaaa.bbbb", "ffff.aaaa.cccc"],
                }
            }
        },
        4: {"instance_id": {}},
    }
}

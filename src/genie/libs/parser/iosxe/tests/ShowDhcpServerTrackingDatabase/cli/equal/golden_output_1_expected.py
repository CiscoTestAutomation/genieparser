# golden_output_1_expected.py
#
# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    "dhcp_server_database_count": 2,
    "entries": {
        1: {
            "link_layer_address": "dead.beef.0001",
            "vlan_id": 20,
            "network_layer_address": "3002::31",
        },
        2: {
            "link_layer_address": "dead.beef.0002",
            "vlan_id": 20,
            "network_layer_address": "3002::32",
        },
    }
}

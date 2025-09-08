# golden_output_expected.py
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    "vpls_name": {
        "ce2": {
            "state": "UP",
            "interface": {
                "pw100002": {
                    "priority": 0,
                    "state": "UP",
                    "encapsulation": "ce2(VFI)",
                    "state_in_l2vpn_service": "UP",
                },
                "pw101": {
                    "priority": 0,
                    "state": "UP",
                    "encapsulation": "106.0.0.2:101(MPLS)",
                    "group": "core_pw",
                    "state_in_l2vpn_service": "UP",
                },
            },
        },
    }
}

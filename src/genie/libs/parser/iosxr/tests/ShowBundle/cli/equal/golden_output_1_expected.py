

expected_output = {
    "interfaces": {
        "Bundle-Ether1": {
            "name": "Bundle-Ether1",
            "bundle_id": 1,
            "oper_status": "up",
            "local_links": {
                "active": 2,
                "standby": 0,
                "configured": 2
            },
            "local_bandwidth_kbps": {
                "effective": 2000000,
                "available": 2000000
            },
            "mac_address": "001b.0cff.6a35",
            "mac_address_source": "Chassis pool",
            "inter_chassis_link": "No",
            "min_active_link": 1,
            "min_active_bw_kbps": 1,
            "max_active_link": 8,
            "wait_while_timer_ms": 2000,
            "load_balance": {
                "link_order_signaling": "Not configured",
                "hash_type": "Default",
                "locality_threshold": "None"
            },
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "Off",
                "cisco_extensions": "Disabled",
                "non_revertive": "Disabled"
            },
            "mlacp": {
                "mlacp": "Not configured"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not configured"
            },
            "ipv6_bfd": {
                "ipv6_bfd": "Not configured"
            },
            "port": {
                "GigabitEthernet0/0/0/0": {
                    "interface": "GigabitEthernet0/0/0/0",
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x000a, 0x0001",
                    "bw_kbps": 1000000,
                    "link_state": "Link is Active"
                },
                "GigabitEthernet0/0/0/1": {
                    "interface": "GigabitEthernet0/0/0/1",
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x8000, 0x0002",
                    "bw_kbps": 1000000,
                    "link_state": "Link is Active"
                }
            }
        },
        "Bundle-Ether2": {
            "name": "Bundle-Ether2",
            "bundle_id": 2,
            "oper_status": "up",
            "local_links": {
                "active": 2,
                "standby": 1,
                "configured": 3
            },
            "local_bandwidth_kbps": {
                "effective": 2000000,
                "available": 2000000
            },
            "mac_address": "001b.0cff.6a34",
            "mac_address_source": "Chassis pool",
            "inter_chassis_link": "No",
            "min_active_link": 2,
            "min_active_bw_kbps": 1,
            "max_active_link": 2,
            "wait_while_timer_ms": 2000,
            "load_balance": {
                "link_order_signaling": "Not configured",
                "hash_type": "Default",
                "locality_threshold": "None"
            },
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "Off",
                "cisco_extensions": "Disabled",
                "non_revertive": "Disabled"
            },
            "mlacp": {
                "mlacp": "Not configured"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not configured"
            },
            "ipv6_bfd": {
                "ipv6_bfd": "Not configured"
            },
            "port": {
                "GigabitEthernet0/0/0/2": {
                    "interface": "GigabitEthernet0/0/0/2",
                    "device": "Local",
                    "state": "Standby",
                    "port_id": "0x8000, 0x0005",
                    "bw_kbps": 1000000,
                    "link_state": "Link is Standby due to maximum-active links configuration"
                },
                "GigabitEthernet0/0/0/3": {
                    "interface": "GigabitEthernet0/0/0/3",
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x8000, 0x0004",
                    "bw_kbps": 1000000,
                    "link_state": "Link is Active"
                },
                "GigabitEthernet0/0/0/4": {
                    "interface": "GigabitEthernet0/0/0/4",
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x8000, 0x0003",
                    "bw_kbps": 1000000,
                    "link_state": "Link is Active"
                }
            }
        }
    }
}

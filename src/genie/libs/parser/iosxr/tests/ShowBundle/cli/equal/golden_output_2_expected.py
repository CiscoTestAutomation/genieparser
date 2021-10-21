

expected_output = {
    "interfaces": {
        "Bundle-Ether 2": {
            "name": "Bundle-Ether 2",
            "bundle_id": 2,
            "oper_status": "up",
            "local_links": {
                "active": 1,
                "standby": 0,
                "configured": 1
            },
            "local_bandwidth_kbps": {
                "effective": 100000,
                "available": 100000
            },
            "mac_address": "1234.43ff.3232",
            "mac_address_source": "GigabitEthernet0/0/0/1",
            "min_active_link": 1,
            "min_active_bw_kbps": 500,
            "max_active_link": 32,
            "wait_while_timer_ms": 2000,
            "load_balance": {
                "load_balance": "Default"
            },
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "2500 ms",
                "cisco_extensions": "Disabled"
            },
            "mlacp": {
                "mlacp": "Operational",
                "iccp_group": "3",
                "foreign_links_active": 1,
                "foreign_links_configured": 1,
                "switchover_type": "Revertive",
                "recovery_delay": "300 s",
                "maximize_threshold": "2 links"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not operational",
                "state": "Off",
                "fast_detect": "Enabled",
                "start_timer": "Off",
                "neighbor_unconfigured_timer": "Off",
                "preferred_min_interval_ms": 150,
                "preferred_multiple": 3,
                "destination_address": "Not Configured"
            },
            "port": {
                "GigabitEthernet0/0/0/1": {
                    "interface": "GigabitEthernet0/0/0/1",
                    "bw_kbps": 100000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x8000, 0x0001"
                },
                "MyFirstInterface": {
                    "interface": "MyFirstInterface",
                    "bw_kbps": 100000,
                    "device": "10.10.10.123",
                    "state": "Negotiating",
                    "port_id": "0x8000, 0x0032"
                }
            }
        },
        "Bundle-Ether 3": {
            "name": "Bundle-Ether 3",
            "bundle_id": 3,
            "oper_status": "up",
            "local_links": {
                "active": 1,
                "standby": 0,
                "configured": 1
            },
            "local_bandwidth_kbps": {
                "effective": 100000,
                "available": 100000
            },
            "mac_address": "1234.43ff.4343",
            "mac_address_source": "chassis pool",
            "min_active_link": 1,
            "min_active_bw_kbps": 500,
            "max_active_link": 32,
            "wait_while_timer_ms": 100,
            "load_balance": {
                "link_order_signaling": "Operational",
                "hash_type": "Src-IP"
            },
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "120 s",
                "cisco_extensions": "Enabled"
            },
            "mlacp": {
                "mlacp": "Not configured"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not operational"
            },
            "port": {
                "GigabitEthernet0/0/0/2": {
                    "interface": "GigabitEthernet0/0/0/2",
                    "bw_kbps": 100000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x8000, 0x0002"
                }
            }
        }
    }
}

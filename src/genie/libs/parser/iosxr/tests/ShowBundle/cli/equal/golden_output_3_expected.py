

expected_output = {
    "interfaces": {
        "Bundle-Ether1": {
            "name": "Bundle-Ether1",
            "bundle_id": 1,
            "oper_status": "up",
            "local_links": {
                "active": 1,
                "standby": 0,
                "configured": 1
            },
            "local_bandwidth_kbps": {
                "effective": 1000000,
                "available": 1000000
            },
            "mac_address": "0000.deff.afaf",
            "mac_address_source": "Configured",
            "min_active_link": 1,
            "min_active_bw_kbps": 1,
            "max_active_link": 64,
            "wait_while_timer_ms": 100,
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "300 ms"
            },
            "mlacp": {
                "mlacp": "Operational",
                "role": "Active",
                "foreign_links_active": 0,
                "foreign_links_configured": 1,
                "switchover_type": "Non-revertive",
                "recovery_delay": "300 s",
                "maximize_threshold": "Not configured"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not configured"
            },
            "port": {
                "GigabitEthernet0/0/0/0": {
                    "interface": "GigabitEthernet0/0/0/0",
                    "bw_kbps": 1000000,
                    "device": "10.81.3.2",
                    "state": "Standby",
                    "port_id": "0x8002, 0xa001",
                    "link_state": "Link is marked as Standby by mLACP peer"
                }
            }
        }
    }
}

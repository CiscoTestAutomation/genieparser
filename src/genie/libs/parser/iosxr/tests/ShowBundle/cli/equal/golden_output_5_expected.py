expected_output = {
    "interfaces": {
        "Bundle-Ether98": {
            "name": "Bundle-Ether98",
            "bundle_id": 98,
            "oper_status": "up",
            "local_links": {
                "active": 5,
                "standby": 0,
                "configured": 5
            },
            "local_bandwidth_kbps": {
                "effective": 50000000,
                "available": 50000000
            },
            "mac_address": "dada.dada.dada",
            "mac_address_source": "Configured",
            "inter_chassis_link": "No",
            "min_active_link": 1,
            "min_active_bw_kbps": 1,
            "max_active_link": 64,
            "wait_while_timer_ms": "Off",
            "load_balance": {
                "link_order_signaling": "Not configured",
                "hash_type": "Default",
                "locality_threshold": "None"
            },
            "lacp": {
                "lacp": "Operational",
                "flap_suppression_timer": "100 ms",
                "cisco_extensions": "Disabled",
                "non_revertive": "Disabled"
            },
            "mlacp": {
                "mlacp": "Operational",
                "role": "Active",
                "foreign_links_active": 0,
                "foreign_links_configured": 5,
                "switchover_type": "Non-revertive",
                "recovery_delay": "60 s",
                "maximize_threshold": "1 link"
            },
            "ipv4_bfd": {
                "ipv4_bfd": "Not configured"
            },
            "ipv6_bfd": {
                "ipv6_bfd": "Not configured"
            },
            "port": {
                "TenGigabitEthernet0/0/0/16": {
                    "interface": "TenGigabitEthernet0/0/0/16",
                    "bw_kbps": 10000000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x00db, 0xa001",
                    "link_state": "Link is Active"
                },
                "TenGigabitEthernet0/7/0/7": {
                    "interface": "TenGigabitEthernet0/7/0/7",
                    "bw_kbps": 10000000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x00db, 0xa005",
                    "link_state": "Link is Active"
                },
                "TenGigabitEthernet0/7/0/13": {
                    "interface": "TenGigabitEthernet0/7/0/13",
                    "bw_kbps": 10000000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x00db, 0xa004",
                    "link_state": "Link is Active"
                },
                "TenGigabitEthernet0/7/0/14": {
                    "interface": "TenGigabitEthernet0/7/0/14",
                    "bw_kbps": 10000000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x00db, 0xa002",
                    "link_state": "Link is Active"
                },
                "TenGigabitEthernet0/7/0/15": {
                    "interface": "TenGigabitEthernet0/7/0/15",
                    "bw_kbps": 10000000,
                    "device": "Local",
                    "state": "Active",
                    "port_id": "0x00db, 0xa003",
                    "link_state": "Link is Active"
                },
                "TenGigabitEthernet0/4/0/12": {
                    "interface": "TenGigabitEthernet0/4/0/12",
                    "bw_kbps": 10000000,
                    "device": "193.126.0.87",
                    "state": "Standby",
                    "port_id": "0x00dc, 0x9009",
                    "link_state": "Link is marked as Standby by mLACP peer"
                },
                "TenGigabitEthernet0/4/0/13": {
                    "interface": "TenGigabitEthernet0/4/0/13",
                    "bw_kbps": 10000000,
                    "device": "193.126.0.87",
                    "state": "Standby",
                    "port_id": "0x00dc, 0x900a",
                    "link_state": "Link is marked as Standby by mLACP peer"
                },
                "TenGigabitEthernet0/4/0/7": {
                    "interface": "TenGigabitEthernet0/4/0/7",
                    "bw_kbps": 10000000,
                    "device": "193.126.0.87",
                    "state": "Standby",
                    "port_id": "0x00dc, 0x9006",
                    "link_state": "Link is marked as Standby by mLACP peer"
                },
                "TenGigabitEthernet0/4/0/8": {
                    "interface": "TenGigabitEthernet0/4/0/8",
                    "bw_kbps": 10000000,
                    "device": "193.126.0.87",
                    "state": "Standby",
                    "port_id": "0x00dc, 0x9007",
                    "link_state": "Link is marked as Standby by mLACP peer"
                },
                "TenGigabitEthernet0/4/0/9": {
                    "interface": "TenGigabitEthernet0/4/0/9",
                    "bw_kbps": 10000000,
                    "device": "193.126.0.87",
                    "state": "Standby",
                    "port_id": "0x00dc, 0x9008",
                    "link_state": "Link is marked as Standby by mLACP peer"
                }
            }
        }
    }
}
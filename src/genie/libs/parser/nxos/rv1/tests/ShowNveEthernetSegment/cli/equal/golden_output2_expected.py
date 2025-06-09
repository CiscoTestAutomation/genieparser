expected_output = {
    "nve": {
        "nve1": {
            "ethernet_segment": {
                "esi": {
                    "0322.22aa.aa00.0000.002a": {
                        "active_vlans": ["2052", "2062"],
                        "active_vnis": ["2002052", "2002062"],
                        "config_status": "config-applied",
                        "df_list": ["10.200.200.105", "10.200.200.106"],
                        "df_timer_st": "00:00:00",
                        "df_vlans": ["2052", "2062"],
                        "ead_rt_added": True,
                        "es_rt_added": True,
                        "es_state": "up",
                        "esi": "0322.22aa.aa00.0000.002a",
                        "esi_df_election_mode": "Modulo",
                        "esi_type": "Ether-segment",
                        "host_reach_mode": "control-plane",
                        "if_name": "port-channel42",
                        "local_ordinal": 0,
                        "num_es_mem": 2,
                        "nve_if_name": "nve1",
                        "nve_state": "up",
                        "po_state": "up",
                    }
                }
            }
        }
    }
}

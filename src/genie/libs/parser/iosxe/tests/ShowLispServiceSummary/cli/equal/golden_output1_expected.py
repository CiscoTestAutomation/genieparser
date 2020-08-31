expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv4": {
                    "virtual_network_ids": {
                        "102": {
                            "cache_idle": "0%",
                            "cache_size": 1,
                            "db_no_route": 0,
                            "db_size": 1,
                            "incomplete": "0.0%",
                            "vrf": "blue",
                            "interface": "LISP0.102",
                            "lisp_role": {"itr-etr": {"lisp_role_type": "itr-etr"}},
                        },
                        "101": {
                            "cache_idle": "0.0%",
                            "cache_size": 2,
                            "db_no_route": 0,
                            "db_size": 1,
                            "incomplete": "0.0%",
                            "vrf": "red",
                            "interface": "LISP0.101",
                            "lisp_role": {"itr-etr": {"lisp_role_type": "itr-etr"}},
                        },
                    },
                    "etr": {
                        "summary": {
                            "eid_tables_incomplete_map_cache_entries": 0,
                            "eid_tables_inconsistent_locators": 0,
                            "eid_tables_pending_map_cache_update_to_fib": 0,
                            "instance_count": 2,
                            "total_db_entries": 2,
                            "total_db_entries_inactive": 0,
                            "total_eid_tables": 2,
                            "total_map_cache_entries": 3,
                        }
                    },
                }
            },
        }
    }
}

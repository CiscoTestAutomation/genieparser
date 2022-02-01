expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ethernet": {
                    "virtual_network_ids": {
                        "1": {
                            "cache_idle": "100%",
                            "cache_size": 4,
                            "db_no_route": 0,
                            "db_size": 2,
                            "incomplete": "0.0%",
                            "interface": "LISP0.1",
                            "lisp_role": {"none": {"lisp_role_type": "none"}},
                        },
                        "2": {
                            "cache_idle": "0%",
                            "cache_size": 0,
                            "db_no_route": 0,
                            "db_size": 2,
                            "incomplete": "0%",
                            "interface": "LISP0.2",
                            "lisp_role": {"none": {"lisp_role_type": "none"}},
                        },
                    },
                    "etr": {
                        "summary": {
                            "eid_tables_incomplete_map_cache_entries": 0,
                            "eid_tables_inconsistent_locators": 0,
                            "eid_tables_pending_map_cache_update_to_fib": 0,
                            "instance_count": 69,
                            "total_db_entries": 4,
                            "total_db_entries_inactive": 0,
                            "total_eid_tables": 2,
                            "total_map_cache_entries": 4,
                            "maximum_db_entries": 5120,
                            "maximum_map_cache_entries": 5120
                        }
                    },
                }
            },
        }
    }
}

expected_output = {
    "load_balance_status": "ENABLED",
    "load_balance_method": "least-outstanding",
    "batch_size": 50,
    "ignore_preferred_server": True,
    "server_group_dead_time": 20,
    "server_group_dead_time_unit": "secs",
    "global_server_liveness_automated_test": {
        "dead_time": 20,
        "dead_time_unit": "secs",
        "idle_time": 60,
        "idle_time_unit": "mins",
        "status": "ENABLED (default)",
    },
}

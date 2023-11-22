expected_output = {
    "load_balance_status": "DISABLED",
    "server_group_dead_time": 20,
    "server_group_dead_time_unit": "secs",
    "global_server_liveness_automated_test": {
        "dead_time": 20,
        "dead_time_unit": "secs",
        "idle_time": 60,
        "idle_time_unit": "mins",
        "status": "ENABLED (default)",
    },
    "installed_list": {
        "CTSServerList1-0001": {
            "10.104.187.183": {
                "server_ip": "10.104.187.183",
                "port_number": 1812,
                "a_id": "3CB545021D06087F9580164F589F76DB",
                "status": "DEAD",
                'auto_test_status': True,
                'keywrap_enable': False,
                'idle_time': 60,
                'idle_time_unit': 'mins',
                'dead_time': 20,
                'dead_time_unit': 'secs'
            }
        }
    },
}

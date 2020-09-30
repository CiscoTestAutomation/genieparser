expected_output = {
    "rm_resources": {
        "rm_global_resources": {
            "max_services_memory_kb": 6410098,
            "available_system_memory_kb": 12820196,
            "used_services_memory_kb": 0,
            "used_services_memory_percentage": 0,
            "system_memory_status": "GREEN",
            "num_sessions_status": "GREEN",
            "overall_htx_health_status": "GREEN",
        },
        "registered_service_resources": {
            "tcp_resources": {
                "max_sessions": 11000,
                "used_sessions": 0,
                "memory_per_session": 128,
            },
            "ssl_resources": {
                "max_sessions": 11000,
                "used_sessions": 0,
                "memory_per_session": 50,
            },
        },
    }
}

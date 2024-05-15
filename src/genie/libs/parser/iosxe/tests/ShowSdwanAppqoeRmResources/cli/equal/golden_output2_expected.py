expected_output = {
    "rm_resources": {
        "rm_global_resources": {
            "max_services_memory_kb": 6261122,
            "available_system_memory_kb": 0,
            "used_services_memory_kb": 12522244,
            "used_services_memory_percentage": 0,
            "system_memory_status": "GREEN",
            "num_sessions_status": "GREEN",
            "overall_htx_health_status": "GREEN",
        },
        "registered_service_resources": {
            "tcp_resources": {
                "max_sessions": 40000,
                "used_sessions": 1,
                "memory_per_session": 64,
            },
            "ssl_resources": {
                "max_sessions": 40000,
                "used_sessions": 0,
                "memory_per_session": 50,
            },
            "dre_resources": {
                "max_sessions": 36000,
                "used_sessions": 0,
                "memory_per_session": 50,
            },
            "http_resources": {
                "max_sessions": 0,
                "used_sessions": 0,
                "memory_per_session": 0,
            },
        },
    }
}
 

expected_output = {
    "sessions": {
        1: {
            "source_ip": "192.168.1.10",
            "destination_ip": "10.0.0.1",
            "source_port": 12345,
            "destination_port": 80,
            "protocol": "TCP",
            "status": "Established",
            "creation_time": "00:01:30",
            "timeout": "00:04:30",
        },
        2: {
            "source_ip": "192.168.1.11",
            "destination_ip": "10.0.0.2",
            "source_port": 12346,
            "destination_port": 443,
            "protocol": "TCP",
            "status": "Established",
            "creation_time": "00:01:15",
            "timeout": "00:04:15",
        },
        3: {
            "source_ip": "192.168.1.12",
            "destination_ip": "10.0.0.3",
            "source_port": 12347,
            "destination_port": 22,
            "protocol": "TCP",
            "status": "Established",
            "creation_time": "00:00:50",
            "timeout": "00:04:50",
        },
    }
}

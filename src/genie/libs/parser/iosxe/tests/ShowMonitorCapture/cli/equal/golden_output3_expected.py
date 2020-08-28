expected_output = {
    "status_information": {
        "mycap": {
            "target_type": {
                "interface": "GigabitEthernet1/0/3",
                "direction": "both",
                "status": "Inactive",
            },
            "filter_details": {
                "filter_details_type": "IPv4",
                "source_ip": "any",
                "destination_ip": "any",
                "protocol": "any",
            },
            "buffer_details": {"buffer_type": "LINEAR (default)"},
            "file_details": {
                "file_name": "flash:mycap.pcap",
                "file_size": 5,
                "file_number": 2,
                "size_of_buffer": 10,
            },
            "limit_details": {
                "packets_number": 0,
                "packets_capture_duaration": 0,
                "packets_size": 0,
                "packets_per_second": 0,
                "packet_sampling_rate": 0,
            },
        }
    }
}

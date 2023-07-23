expected_output = {
    "bridge_domain": 500,
    "reference_count": 6,
    "replication_ports_count": 3,
    "unicast_addr_table_size": 0,
    "ip_multicast_prefix_table_size": 0,
    "port_info": {
        "Et0/0:500": {
            "type": "BD_PORT",
            "description": "Et0/0:500",
            "description_values": {
                "interface": "Et0/0",
                "service_instance": 500,
            },
            "is_pathlist": False,
        },
        "Et0/3:500": {
            "type": "BD_PORT",
            "description": "Et0/3:500",
            "description_values": {
                "interface": "Et0/3",
                "service_instance": 500,
            },
            "is_pathlist": False,
        },
        "Et1/0:500": {
            "type": "BD_PORT",
            "description": "Et1/0:500",
            "description_values": {
                "interface": "Et1/0",
                "service_instance": 500,
            },
            "is_pathlist": False,
        },
    },
    "flood_list_info": {"olist": 61, "ports": 3},
}

expected_output = {
    "tunnel_sla_class": {
        "23.0.0.23": {
            "tunnel_count": 4,
            "150.0.5.1": {
                "remote": {
                    "150.0.3.1": {
                        "index": 0,
                        "protocol": "ipsec",
                        "src_ip": "150.0.5.1",
                        "dst_ip": "150.0.3.1",
                        "local_color": "public-internet",
                        "remote_color": "biz-internet",
                        "sla_class_name": "__all_tunnels__, aarSla"
                    },
                    "151.0.3.1": {
                        "index": 2,
                        "protocol": "ipsec",
                        "src_ip": "150.0.5.1",
                        "dst_ip": "151.0.3.1",
                        "local_color": "public-internet",
                        "remote_color": "bronze",
                        "sla_class_name": "__all_tunnels__, aarSla"
                    }
                }
            },
            "151.0.5.1": {
                "remote": {
                    "150.0.3.1": {
                        "index": 1,
                        "protocol": "ipsec",
                        "src_ip": "151.0.5.1",
                        "dst_ip": "150.0.3.1",
                        "local_color": "silver",
                        "remote_color": "biz-internet",
                        "sla_class_name": "__all_tunnels__, aarSla"
                    },
                    "151.0.3.1": {
                        "index": 3,
                        "protocol": "ipsec",
                        "src_ip": "151.0.5.1",
                        "dst_ip": "151.0.3.1",
                        "local_color": "silver",
                        "remote_color": "bronze",
                        "sla_class_name": "__all_tunnels__, aarSla"
                    }
                }
            }
        }
    }
}

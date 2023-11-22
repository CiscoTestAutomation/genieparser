expected_output = {
    "flow_exporter_name":{
        "StealthWatch_Exporter":{
            "description":"Export NetFlow to StealthWatch",
            "export_protocol":"NetFlow Version 9",
            "transport_config":{
                "destination_type":"IP",
                "destination_ip_address":"19.1.1.19",
                "source_ip_address":"4.4.1.1",
                "transport_protocol":"UDP",
                "destination_port":2055,
                "source_port":50714,
                "dscp":"0x0",
                "ttl":255,
                "output_features":"Used"
            }
        }
    }
}

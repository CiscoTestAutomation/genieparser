expected_output = {
    "flow_exporter_name":{
        "dnacexporter":{
            "destination":"10.10.0.104",
            "source":"Loopback80",
            "transport_protocol":"udp",
            "transport_protocol_port":6007,
            "export_protocol":"ipfix",
            "options":[
                "interface-table timeout 10",
                "vrf-table timeout 10",
                "sampler-table",
                "application-table timeout 10",
                "application-attributes timeout 10"
            ]
        },
        "export_local_nf10":{
            "destination":"90.90.90.90",
            "transport_protocol":"udp",
            "transport_protocol_port":4739,
            "export_protocol":"ipfix",
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "export_local_nf9":{
            "destination":"90.90.90.90",
            "transport_protocol":"udp",
            "transport_protocol_port":2055,
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "export_prime_nf9":{
            "destination":"10.5.28.188",
            "transport_protocol":"udp",
            "transport_protocol_port":9991,
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "export_prime_nf10":{
            "destination":"10.5.28.188",
            "transport_protocol":"udp",
            "transport_protocol_port":9991,
            "export_protocol":"ipfix",
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "export_prime1_nf9":{
            "destination":"10.5.28.112",
            "transport_protocol":"udp",
            "transport_protocol_port":9991,
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "export_prime1_nf10":{
            "destination":"10.5.28.112",
            "transport_protocol":"udp",
            "transport_protocol_port":9991,
            "export_protocol":"ipfix",
            "options":[
                "exporter-stats timeout 20"
            ]
        },
        "10.10.0.160":{
            "destination":"10.10.0.160",
            "transport_protocol":"udp",
            "transport_protocol_port":6007
        },
        "test":{
            "description":"test_expoter",
            "destination":"2.3.4.5",
            "source":"Loopback0",
            "dscp":5,
            "ttl":64,
            "transport_protocol":"udp",
            "transport_protocol_port":555,
            "export_protocol":"ipfix",
            "options":[
                "interface-table"
            ],
            "match_counter_packets_long_gt":128
        }
    }
}

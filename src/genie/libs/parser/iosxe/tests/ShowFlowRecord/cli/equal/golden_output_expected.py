expected_output = {
    "flow_record_name":{
        "wireless avc basic":{
            "description":"Basic IPv4 Wireless AVC template",
            "no_of_users":0,
            "total_field_space":78,
            "fields":{
                "match_list":[
                    "ipv4 protocol",
                    "ipv4 source address",
                    "ipv4 destination address",
                    "transport source-port",
                    "transport destination-port",
                    "flow direction",
                    "application name",
                    "wireless ssid"
                ],
                "collect_list":[
                    "counter bytes long",
                    "counter packets long",
                    "wireless ap mac address",
                    "wireless client mac address"
                ]
            }
        },
        "wireless avc ipv6 basic":{
            "description":"Basic IPv6 Wireless AVC template",
            "no_of_users":0,
            "total_field_space":102,
            "fields":{
                "match_list":[
                    "ipv6 protocol",
                    "ipv6 source address",
                    "ipv6 destination address",
                    "transport source-port",
                    "transport destination-port",
                    "flow direction",
                    "wireless ssid"
                ],
                "collect_list":[
                    "counter bytes long",
                    "counter packets long",
                    "application name",
                    "wireless ap mac address",
                    "wireless client mac address"
                ]
            }
        }
    }
}

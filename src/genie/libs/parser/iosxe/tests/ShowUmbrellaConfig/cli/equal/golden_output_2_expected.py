expected_output = {
    'umbrella_configuration': {
        "token_key": "FC4C18E820D29D6CFC9B5224D5EAE8020026E638",
        "api_key": "NONE",
        "org_id": "2549304",
        "local_domain_regex_parameter_map_name": "NONE",
        "dns_crypt": "Enabled",
        "public_key": "B735:1140:206F:225D:3E2B:D822:D7FD:691E:A1C3:3CC8:D666:8D0C:BE04:BFAB:CA43:FB79",
        "udp_timeout": 5,
        "resolver_address": [
            "208.67.220.220",
            "208.67.222.222",
            "2620:119:53::53",
            "2620:119:35::35"
        ],
        "umbrella_interface_config": {
            "umbrella out": {
                "number_of_interfaces": 1,
                "indexes": {
                    1: {
                        "interface": "GigabitEthernet2/0/1",
                        "mode": "OUT",
                        "vrf": "global",
                        "vrf_id": 0,
                    }
                }
            },
            "umbrella in": {
                "number_of_interfaces": 1,
                "indexes": {
                    1: {
                        "interface": "GigabitEthernet2/0/7",
                        "mode": "IN",
                        "dca": "Disabled",
                        "tag": "9200_9300_tag",
                        "device_id": "010abd2ec0dcffe3",
                        "vrf": "global",
                        "vrf_id": 0,
                    }
                }
            }
        },
        'parameter_maps': {
            1: {
                'type': 'global'
            }
        }
    }
}

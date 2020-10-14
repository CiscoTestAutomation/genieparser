expected_output = {
    "traceroute": {
        "172.16.51.1": {
            "address": "172.16.51.1",
            "hops": {
                "1": {
                    "paths": {
                        1: {"address": "*"},
                        2: {"address": "172.16.51.1", "probe_msec": ["41", "*"]},
                        3: {"address": "*"},
                    }
                },
                "2": {
                    "paths": {
                        1: {"address": "10.1.2.6", "probe_msec": ["148"]},
                        2: {"address": "10.1.1.6", "probe_msec": ["120"]},
                        3: {"address": "10.1.2.6", "probe_msec": ["132"]},
                    }
                },
            },
            "vrf": "CE1test",
        }
    }
}

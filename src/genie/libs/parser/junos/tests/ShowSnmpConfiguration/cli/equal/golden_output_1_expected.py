expected_output = {
    "configuration": {
        "snmp": {
            "location": "TH-HK2/floor_1B-002/rack_KHK1104",
            "contact": "KHK",
            "community": [
                {
                    "name": "safaripub",
                    "authorization": "read-only",
                    "clients": [
                        {"name": "10.169.5.0/25"},
                        {"name": "10.25.32.0/24"},
                        {"name": "192.168.219.128/27"},
                        {"name": "192.168.64.0/24"},
                        {"name": "192.168.154.0/24"},
                        {"name": "0.0.0.0/0", "restrict": True},
                        {"name": "2001:db8:d38a:cf16::/64"},
                        {"name": "2001:db8:d38a:d3e9::/64"},
                        {"name": "10.49.164.48/28"},
                        {"name": "192.168.21.0/24"},
                        {"name": "10.64.97.0/24"},
                    ],
                },
                {
                    "name": "SpiderSDC",
                    "authorization": "read-only",
                    "clients": [{"name": "10.64.99.0/26"}],
                },
                {
                    "name": "kitsune",
                    "authorization": "read-only",
                    "clients": [{"name": "192.168.34.0/24"}],
                },
            ],
            "trap-options": {"source-address": "lo0"},
            "trap-group": {
                "name": "safaripub",
                "version": "v1",
                "categories": [
                    {"name": "chassis"},
                    {"name": "link"},
                    {"name": "routing"},
                ],
                "targets": [{"name": "10.64.99.32"}, {"name": "10.169.249.67"}],
            },
        }
    }
}



expected_output = {
    "instance": {
        "TEST": {
            "address_family": {
                "IPv4 Unicast": {
                    "spf_log": {
                        1: {
                            "start_timestamp": "Mon Oct  7 2019 23:12:51.401",
                            "level": 2,
                            "type": "PPFRR",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "triggers": "PERPREFIXFRR",
                        },
                        2: {
                            "start_timestamp": "Mon Oct  7 2019 23:27:50.960",
                            "level": 2,
                            "type": "FSPF",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "triggers": "PERIODIC",
                        },
                        3: {
                            "start_timestamp": "Tue Oct  8 2019 00:00:17.514",
                            "level": 2,
                            "type": "PRC",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 6,
                            "first_trigger_lsp": "bla-host1.12-34",
                            "triggers": "PREFIXBAD",
                        },
                        4: {
                            "start_timestamp": "Tue Oct  8 2019 00:02:24.523",
                            "level": 2,
                            "type": "PRC",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 6,
                            "first_trigger_lsp": "bla-host2.13-34",
                            "triggers": "PREFIXGOOD",
                        },
                        5: {
                            "start_timestamp": "Tue Oct  8 2019 00:02:25.025",
                            "level": 2,
                            "type": "PPFRR",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "triggers": "PERPREFIXFRR",
                        },
                        6: {
                            "start_timestamp": "Tue Oct  8 2019 08:15:04.265",
                            "level": 2,
                            "type": "PRC",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                            "triggers": "PREFIXBAD",
                        },
                        7: {
                            "start_timestamp": "Tue Oct  8 2019 08:15:04.418",
                            "level": 2,
                            "type": "PRC",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                            "triggers": "PREFIXGOOD",
                        },
                        8: {
                            "start_timestamp": "Tue Oct  8 2019 08:17:55.366",
                            "level": 2,
                            "type": "PRC",
                            "time_ms": 0,
                            "total_nodes": 64,
                            "trigger_count": 1,
                            "first_trigger_lsp": "bla-9.blahlab-cld.12-34",
                            "triggers": "PREFIXBAD",
                        },
                    }
                }
            }
        }
    }
}

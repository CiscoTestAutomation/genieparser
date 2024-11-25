expected_output = {
    "job_id": {
        4: {
            "status": "JOB_COMPLETED",
            "request_info": {
                "vrf_name": "default",
                "host_name": "yahoo.com",
                "dns_server": "72.163.128.140"
            },
            "request_time": "Sep 19 20:20:33.776",
            "completion_time": "Sep 19 20:20:33.785",
            "error_code": "No Error",
            "dns_response": {
                1: {
                    "dns_id": 0,
                    "dns_flags": "qr-response opcode-query rd ra rcode-noerr",
                    "dns_qdcnt": 1,
                    "dns_ancnt": 6,
                    "dns_nscnt": 0,
                    "dns_arcnt": 1,
                    "dns_class": "IN",
                    "dns_type": "IPv4",
                    "dns_rtt": "9ms",
                    "dns_payload_size": 134,
                    "dns_ip": {
                        "74.6.143.26": {
                            "dns_ttl": 0
                        },
                        "74.6.143.25": {
                            "dns_ttl": 0
                        },
                        "98.137.11.164": {
                            "dns_ttl": 0
                        },
                        "98.137.11.163": {
                            "dns_ttl": 0
                        },
                        "74.6.231.20": {
                            "dns_ttl": 0
                        },
                        "74.6.231.21": {
                            "dns_ttl": 0
                        }
                    }
                }
            }
        },
        5: {
            "status": "JOB_COMPLETED",
            "request_info": {
                "vrf_name": "Mgmt-intf",
                "host_name": "yahoo.com",
                "dns_server": "72.163.128.140"
            },
            "request_time": "Sep 19 20:21:51.972",
            "completion_time": "Sep 19 20:21:51.982",
            "error_code": "No Error",
            "dns_response": {
                1: {
                    "dns_id": 0,
                    "dns_flags": "qr-response opcode-query rd ra rcode-noerr",
                    "dns_qdcnt": 1,
                    "dns_ancnt": 6,
                    "dns_nscnt": 0,
                    "dns_arcnt": 1,
                    "dns_class": "IN",
                    "dns_type": "IPv4",
                    "dns_rtt": "11ms",
                    "dns_payload_size": 134,
                    "dns_ip": {
                        "74.6.143.25": {
                            "dns_ttl": 0
                        },
                        "74.6.231.21": {
                            "dns_ttl": 0
                        },
                        "98.137.11.163": {
                            "dns_ttl": 0
                        },
                        "74.6.143.26": {
                            "dns_ttl": 0
                        },
                        "74.6.231.20": {
                            "dns_ttl": 0
                        },
                        "98.137.11.164": {
                            "dns_ttl": 0
                        }
                    }
                }
            }
        }
    },
    "total_number_of_jobs": 2
}
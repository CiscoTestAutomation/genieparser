expected_output = {
    "job_id": {
        3: {
            "status": "JOB_COMPLETED",
            "request_info": {
                "vrf_name": "default",
                "host_name": "yahoo.com",
                "dns_server": "72.163.128.140"
            },
            "request_time": "Sep 19 20:19:08.462",
            "completion_time": "Sep 19 20:19:08.474",
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
                    "dns_type": "IPv6",
                    "dns_rtt": "12ms",
                    "dns_payload_size": 206,
                    "dns_ip": {
                        "2001:4998:44:3507::8000": {
                            "dns_ttl": 0
                        },
                        "2001:4998:24:120D::1:1": {
                            "dns_ttl": 0
                        },
                        "2001:4998:124:1507::F000": {
                            "dns_ttl": 0
                        },
                        "2001:4998:124:1507::F001": {
                            "dns_ttl": 0
                        },
                        "2001:4998:24:120D::1:0": {
                            "dns_ttl": 0
                        },
                        "2001:4998:44:3507::8001": {
                            "dns_ttl": 0
                        }
                    }
                }
            }
        }
    },
    "total_number_of_jobs": 1
}
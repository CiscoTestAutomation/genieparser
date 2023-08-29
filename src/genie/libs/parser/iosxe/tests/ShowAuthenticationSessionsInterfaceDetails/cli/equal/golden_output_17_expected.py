
expected_output = {
    "interfaces": {
        "GigabitEthernet2/0/24": {
            "mac_address": {
                "000c.2911.69b9": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x3C9B9200",
                    "ipv4_address": "101.1.0.2",
                    "user_name": "webauth_user1",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "single-host",
                    "oper_control_dir": "both",
                    "session_timeout": {
                        "type": "N/A"
                    },
                    "common_session_id": "910C140B00000017F40DA338",
                    "acct_session_id": "0x00000003",
                    "handle": "0xf700000d",
                    "current_policy": "Webauth",
                    "server_policies": {
                        1: {
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Webauth_ACL-64cbe188"
                        }
                    },
                    "method_status": {
                        "webauth": {
                            "method": "webauth",
                            "state": "Authc Success"
                        }
                    }
                }
            }
        }
    }
}

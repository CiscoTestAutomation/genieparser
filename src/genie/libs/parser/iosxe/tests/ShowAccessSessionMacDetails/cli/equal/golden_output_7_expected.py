expected_output = {
    "mac": {
        "000c.2911.69b9": {
            "interface": "GigabitEthernet2/0/24",
            "iif_id": "0x312C3E39",
            "ipv6_address": "Unknown",
            "ipv4_address": "101.1.0.2",
            "user_name": "webauth_user2",
            "status": "Authorized",
            "domain": "DATA",
            "oper_host_mode": "multi-auth",
            "oper_control_dir": "both",
            "common_session_id": "910C140B000000248F52CD2F",
            "acct_session_id": "Unknown",
            "handle": "0x8600001a",
            "current_policy": "WA_logout_vip",
            "local_policies": {
                "url_redirect_acl_v4": "IP-Adm-V4-LOGOUT-ACL"
            },
            "server_policies": {
                "filter_id": "Webauth_ACL",
                "session_timeout": 70
            },
            "method_status_list": {
                "method": "webauth",
                "state": "Authc Success"
            }
        }
    }
}

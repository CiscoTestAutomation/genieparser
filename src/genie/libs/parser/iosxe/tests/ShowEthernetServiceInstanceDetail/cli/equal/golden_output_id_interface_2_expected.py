expected_output = {
    "service_instance": {
        100: {
            "interfaces": {
                "Gig3/0/1": {
                    "l2_acl": {
                        "inbound": "test-acl",
                        "permit_count": 10255,
                        "deny_count": 53,
                    },
                    "associated_evc": "test",
                    "l2protocol_drop": True,
                    "dot1q_tunnel_ethertype": "0x8100",
                    "state": "Up",
                }
            }
        }
    }
}

expected_output = {
    "peer_session": {
        "PEER-SESSION": {
            "local_policies": "0x5025FD",
            "inherited_polices": "0x0",
            "fall_over_bfd": True,
            "suppress_four_byte_as_capability": True,
            "description": "desc1!",
            "disable_connected_check": True,
            "ebgp_multihop_enable": True,
            "ebgp_multihop_max_hop": 254,
            "local_as_as_no": 255,
            "password_text": "is configured",
            "remote_as": 321,
            "shutdown": True,
            "transport_connection_mode": "passive",
            "update_source": "Loopback0",
            "index": 1,
            "inherited_session_commands": {"keepalive_interval": 10, "holdtime": 30},
        },
        "PEER-SESSION2": {
            "local_policies": "0x100000",
            "inherited_polices": "0x0",
            "fall_over_bfd": True,
            "index": 2,
        },
    }
}

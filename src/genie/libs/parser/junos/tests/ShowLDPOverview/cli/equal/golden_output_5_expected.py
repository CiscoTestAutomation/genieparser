expected_output = {
    "ldp-overview-information": {
        "ldp-overview": {
            "ldp-configuration-sequence": 1,
            "ldp-deaggregate": "disabled",
            "ldp-explicit-null": "disabled",
            "ldp-gr-overview": {
                "ldp-gr-helper": "enabled",
                "ldp-gr-max-neighbor-reconnect-time": 120000,
                "ldp-gr-max-neighbor-recovery-time": 240000,
                "ldp-gr-reconnect-time": 60000,
                "ldp-gr-recovery-time": 160000,
                "ldp-gr-restart": "enabled",
                "ldp-gr-restarting": "false",
            },
            "ldp-igp-overview": {
                "ldp-igp-sync-session-up-delay": 10,
                "ldp-tracking-igp-metric": "disabled",
            },
            "ldp-instance-capability": {"ldp-capability": "none"},
            "ldp-instance-name": "master",
            "ldp-interface-address": {"interface-address": ["10.1.2.2"]},
            "ldp-ipv6-tunneling": "disabled",
            "ldp-loopback-if-added": "no",
            "ldp-message-id": 4,
            "ldp-p2mp-transit-lsp-chaining": "disabled",
            "ldp-protocol-modes": {
                "ldp-control-mode": "ordered",
                "ldp-distribution-mode": "unsolicited",
                "ldp-retention-mode": "liberal",
            },
            "ldp-route-preference": 9,
            "ldp-router-id": "10.204.1.100",
            "ldp-session-count": {"ldp-session-connecting": 1},
            "ldp-session-protect-overview": {
                "ldp-session-protect": "disabled",
                "ldp-session-protect-timeout": 0,
            },
            "ldp-strict-targeted-hellos": "disabled",
            "ldp-te-overview": {
                "ldp-te-bgp-igp": "disabled",
                "ldp-te-both-ribs": "disabled",
                "ldp-te-mpls-forwarding": "disabled",
            },
            "ldp-timer-overview": {
                "ldp-instance-keepalive-interval": 10,
                "ldp-instance-keepalive-timeout": 30,
                "ldp-instance-label-withdraw-delay": 60,
                "ldp-instance-link-hello-hold-time": 15,
                "ldp-instance-link-hello-interval": 5,
                "ldp-instance-targeted-hello-hold-time": 45,
                "ldp-instance-targeted-hello-interval": 15,
            },
            "ldp-transit-lsp-route-stats": "disabled",
            "ldp-unicast-transit-lsp-chaining": "disabled",
        }
    }
}

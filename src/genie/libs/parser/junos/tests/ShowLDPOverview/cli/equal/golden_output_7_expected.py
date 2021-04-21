expected_output = {
    "ldp-overview-information": {
        "ldp-overview": {
            "ldp-closing-mode": "1",
            "ldp-configuration-sequence": 2,
            "ldp-control-mode": "ordered",
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
            "ldp-instance-egress-fec-capability": {
                "ldp-egress-fec-capability": "entropy-label-capability"
            },
            "ldp-instance-name": "master",
            "ldp-interface-address": {
                "interface-address": ["10.169.14.121", "10.169.14.157"]
            },
            "ldp-ipv6-tunneling": "disabled",
            "ldp-job-overview": {
                "ldp-inbound-read-job-loop-quantum": 100,
                "ldp-inbound-read-job-time-quantum": 1000,
                "ldp-outbound-read-job-loop-quantum": 100,
                "ldp-outbound-read-job-time-quantum": 1000,
                "ldp-read-job-loop-quantum": 100,
                "ldp-read-job-time-quantum": 1000,
                "ldp-write-job-loop-quantum": 100,
                "ldp-write-job-time-quantum": 1000,
            },
            "ldp-loopback-if-added": "no",
            "ldp-message-id": 10,
            "ldp-mtu-discovery": "disabled",
            "ldp-p2mp-transit-lsp-chaining": "disabled",
            "ldp-reference-count": 3,
            "ldp-retention-mode": "liberal",
            "ldp-route-acknowledgement": "enabled",
            "ldp-route-preference": 9,
            "ldp-router-id": "10.169.14.240",
            "ldp-session-count": {
                "ldp-control-mode": "ordered",
                "ldp-retention-mode": "liberal",
                "ldp-session-nonexistent": 1,
            },
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
                "ldp-instance-link-protection-timeout": 120,
                "ldp-instance-make-before-break-switchover-delay": 3,
                "ldp-instance-make-before-break-timeout": 30,
                "ldp-instance-targeted-hello-hold-time": 45,
                "ldp-instance-targeted-hello-interval": 15,
            },
            "ldp-transit-lsp-route-stats": "disabled",
            "ldp-unicast-transit-lsp-chaining": "disabled",
        }
    }
}

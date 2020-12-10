expected_output = {
    "mpls-lsp-information": {
        "rsvp-session-data": [
            {
                "count": "0",
                "display-count": "0",
                "down-count": "0",
                "session-type": "Ingress",
                "up-count": "0",
            },
            {
                "count": "0",
                "display-count": "0",
                "down-count": "0",
                "session-type": "Egress",
                "up-count": "0",
            },
            {
                "count": "30",
                "display-count": "1",
                "down-count": "0",
                "rsvp-session": {
                    "adspec": "received MTU 1500 sent MTU 1500",
                    "destination-address": "10.49.194.125",
                    "explicit-route": {
                        "explicit-route-element": [
                            {"address": "192.168.145.218"},
                            {"address": "10.49.194.65"},
                            {"address": "10.49.194.66"},
                        ]
                    },
                    "label-in": "46",
                    "label-out": "44",
                    "lsp-id": "1",
                    "lsp-path-type": "Primary",
                    "lsp-state": "Up",
                    "name": "test_lsp_01",
                    "packet-information": [
                        {
                            "heading": "PATH",
                            "count": "1",
                            "in-epoch": "385353",
                            "in-message-handle": "P-8/1",
                            "in-message-id": "23",
                            "interface-name": "ge-0/0/0.0",
                            "previous-hop": "10.169.14.157",
                        },
                        {
                            "heading": "PATH",
                            "count": "1",
                            "interface-name": "ge-0/0/1.1",
                            "next-hop": "192.168.145.218",
                            "out-epoch": "385318",
                            "out-message-id": "23",
                            "out-message-state": "refreshing",
                        },
                        {
                            "heading": "RESV",
                            "count": "1",
                            "entropy-label": "Yes",
                            "in-epoch": "385436",
                            "in-message-handle": "R-59/1",
                            "in-message-id": "74",
                            "interface-name": "ge-0/0/1.1",
                            "previous-hop": "192.168.145.218",
                        },
                        {
                            "heading": "RESV",
                            "out-epoch": "385318",
                            "out-message-id": "74",
                            "out-message-state": "refreshing",
                        },
                    ],
                    "proto-id": "0",
                    "psb-creation-time": "Tue Jun 30 07:22:02 2020",
                    "psb-lifetime": "146",
                    "record-route": {
                        "address": [
                            "10.49.194.2",
                            "10.169.14.157",
                            "192.168.145.218",
                            "10.49.194.66",
                        ]
                    },
                    "recovery-label-in": "-",
                    "recovery-label-out": "44",
                    "resv-style": "FF",
                    "route-count": "0",
                    "rsb-count": "1",
                    "rsvp-lsp-enh-local-prot-downstream": {
                        "rsvp-lsp-enh-local-prot-refresh-interval": "30 secs",
                        "rsvp-lsp-enh-lp-downstream-status": "Disabled",
                    },
                    "rsvp-lsp-enh-local-prot-upstream": {
                        "rsvp-lsp-enh-local-prot-refresh-interval": "30 secs",
                        "rsvp-lsp-enh-lp-upstream-status": "Disabled",
                    },
                    "sender-tspec": "rate 0bps size 0bps peak Infbps m 20 M 1500",
                    "source-address": "10.49.194.127",
                    "suggested-label-in": "-",
                    "suggested-label-out": "-",
                    "tunnel-id": "50088",
                },
                "session-type": "Transit",
                "up-count": "1",
            },
        ]
    }
}

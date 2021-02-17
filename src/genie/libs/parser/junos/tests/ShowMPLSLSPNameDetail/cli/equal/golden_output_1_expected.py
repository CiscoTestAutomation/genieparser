expected_output = {
    "mpls-lsp-information": {
        "rsvp-session-data": [
            {
                "session-type": "Ingress",
                "count": "0",
                "display-count": "0",
                "up-count": "0",
                "down-count": "0",
            },
            {
                "session-type": "Egress",
                "count": "0",
                "display-count": "0",
                "up-count": "0",
                "down-count": "0",
            },
            {
                "session-type": "Transit",
                "count": "30",
                "rsvp-session": {
                    "destination-address": "10.49.194.125",
                    "source-address": "10.49.194.127",
                    "lsp-state": "Up",
                    "route-count": "0",
                    "name": "test_lsp_01",
                    "lsp-path-type": "Primary",
                    "suggested-label-in": "-",
                    "suggested-label-out": "-",
                    "recovery-label-in": "-",
                    "recovery-label-out": "44",
                    "rsb-count": "1",
                    "resv-style": "FF",
                    "label-in": "46",
                    "label-out": "44",
                    "psb-lifetime": "138",
                    "psb-creation-time": "Tue Jun 30 07:22:02 2020",
                    "sender-tspec": "rate 0bps size 0bps peak Infbps m 20 M 1500",
                    "lsp-id": "1",
                    "tunnel-id": "50088",
                    "proto-id": "0",
                    "packet-information": [
                        {
                            "heading": "PATH",
                            "previous-hop": "10.169.14.157",
                            "interface-name": "(ge-0/0/0.0)",
                            "count": "1",
                        },
                        {
                            "heading": "PATH",
                            "next-hop": "192.168.145.218",
                            "interface-name": "(ge-0/0/1.1)",
                            "count": "1",
                        },
                        {
                            "heading": "RESV",
                            "previous-hop": "192.168.145.218",
                            "interface-name": "(ge-0/0/1.1)",
                            "count": "1",
                            "entropy-label": "Yes",
                        },
                    ],
                    "adspec": "received MTU 1500 sent MTU 1500",
                    "explicit-route": {
                        "explicit-route-element": [
                            {"address": "192.168.145.218"},
                            {"address": "10.49.194.65"},
                            {"address": "10.49.194.66"},
                            {"address": "10.49.194.123"},
                        ]
                    },
                    "record-route": {
                        "record-route-element": [
                            {"address": "10.49.194.2"},
                            {"address": "10.169.14.157"},
                            {"address": "<self>"},
                            {"address": "192.168.145.218"},
                            {"address": "10.49.194.66"},
                            {"address": "10.49.194.12"},
                            {"address": "255.255.255.255"},
                            {"address": "10.4.1.1"},
                            {"address": "10.1.8.8"},
                            {"address": "10.64.64.64"},
                        ]
                    },
                },
                "display-count": "1",
                "up-count": "1",
                "down-count": "0",
            },
        ]
    }
}

expected_output = {
    "bridge-domains": {
        20: {
            "bpdu-drop-enable": True,
            "bridge-domain-id": 20,
            "bridge-domain-type": "p2mp",
            "local-switching": True,
            "logical-interfaces": {
                "ethernet": {
                    "0/30.1": {"lif-bind-id": "Ethernet 0/30.1"},
                    "0/30.2": {"lif-bind-id": "Ethernet 0/30.2"},
                },
                "port-channel": {
                    "100.1": {"pc-lif-bind-id": "Port-channel 100.1"},
                    "100.2": {"pc-lif-bind-id": "Port-channel 100.2"},
                },
            },
            "mac-address": {"withdrawal": True},
            "peers": {
                "1.1.1.1": {
                    "lsps": {
                        "abc": {"lsp-name": "abc"},
                        "def": {"lsp-name": "def"},
                        "ed": {"lsp-name": "ed"},
                    },
                    "peer-ip": "1.1.1.1",
                },
                "3.3.3.3": {
                    "lsps": {
                        "1": {"lsp-name": "1"},
                        "abc": {"lsp-name": "abc"},
                        "cos": {"lsp-name": "cos"},
                    },
                    "peer-ip": "3.3.3.3",
                },
                "4.4.4.4": {
                    "control-word": True,
                    "cos": 4,
                    "flow-label": True,
                    "load-balance": True,
                    "lsps": {
                        "abc": {"lsp-name": "abc"},
                        "ds": {"lsp-name": "ds"}
                    },
                    "peer-ip": "4.4.4.4",
                },
            },
            "pw-profile-name": "default",
            "statistics": True,
            "suppress-arp": {"suppress-arp-enable": True},
            "suppress-nd": {"suppress-nd-enable": True},
            "vc-id-num": 20,
        },
        30: {
            "bridge-domain-id": 30,
            "bridge-domain-type": "p2p",
            "logical-interfaces": {
                "ethernet": {},
                "port-channel": {
                    "1.300": {
                        "pc-lif-bind-id": "Port-channel 1.300"
                    }
                },
            },
            "peers": {
                "100.1.234.6": {
                    "control-word": True,
                    "cos": 1,
                    "flow-label": True,
                    "load-balance": True,
                    "peer-ip": "100.1.234.6",
                }
            },
            "pw-profile-name": "class-fat",
            "vc-id-num": 20030,
        },
        40: {
            "bpdu-drop-enable": True,
            "bridge-domain-id": 40,
            "bridge-domain-type": "p2mp",
            "description": "test",
            "local-switching": True,
            "mac-address": {"withdrawal": True},
            "pw-profile-name": "default",
            "statistics": True,
        },
    }
}

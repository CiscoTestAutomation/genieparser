expected_output = {
    "segment_1": {
        "ac Gi0/0/0:8(Ethernet)": {
            "s1": "UP",
            "segment_2": {
                "l2tp 100.3.1.1:101": {
                    "s2": "UP",
                    "xc": "UP",
                    "st": "pri"
                }
            }
        },
        "ac Gi0/0/1:10(Ethernet)": {
            "s1": "DN",
            "segment_2": {
                "mpls 10.239.6.2:684955608": {
                    "s2": "DN",
                    "xc": "DN",
                    "st": "sec"
                }
            }
        },
        "mpls 10.16.2.2:888": {
            "s1": "UP",
            "segment_2": {
                "ac Gi3:9(Ethernet)": {
                    "s2": "UP",
                    "xc": "UP",
                    "st": "pri"
                }
            }
        },
        "bd 300": {
            "s1": "UP",
            "segment_2": {
                "vfi sample-vfi": {
                    "s2": "IA",
                    "xc": "IA",
                    "st": "pri"
                }
            }
        },
        "ac Gi0/0/2:15(Ethernet)": {
            "s1": "UP",
            "segment_2": {
                "l2tp 192.168.1.5:201": {
                    "s2": "UP",
                    "xc": "UP",
                    "st": "sec"
                }
            }
        },
        "mpls 172.16.1.1:999": {
            "s1": "AD",
            "segment_2": {
                "ac Gi1/0/1:20(Ethernet)": {
                    "s2": "AD",
                    "xc": "AD",
                    "st": "pri"
                }
            }
        },
        "bd 400": {
            "s1": "SB"
        }
    }
}
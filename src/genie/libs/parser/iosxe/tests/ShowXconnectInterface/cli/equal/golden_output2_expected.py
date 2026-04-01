expected_output = {
    "segment_1": {
        "ac Gi0/0/1:10(Ethernet)": {
            "s1": "UP",
            "segment_2": {
                "mpls 10.239.6.2:684955608": {
                    "s2": "UP",
                    "xc": "UP",
                    "st": "pri"
                }
            }
        },
        "mpls 172.16.1.1:777": {
            "s1": "DN", 
            "segment_2": {
                "ac Gi1/0/2:25(Ethernet)": {
                    "s2": "DN",
                    "xc": "DN",
                    "st": "sec"
                }
            }
        }
    }
}
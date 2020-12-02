expected_output = {
    "ospf-neighbor-information": {
        "ospf-neighbor": [
            {
                "activity-timer": "39",
                "adj-sid-list": {
                    "spring-adjacency-labels": [
                        {"adj-sid-type": "Protected", "flags": "BVL", "label": "28985"},
                        {
                            "adj-sid-type": "UnProtected",
                            "flags": "VL",
                            "label": "28986",
                        },
                    ]
                },
                "bdr-address": "0.0.0.0",
                "dr-address": "0.0.0.0",
                "interface-name": "ge-0/0/0.0",
                "neighbor-address": "10.189.5.94",
                "neighbor-adjacency-time": {"#text": "3w0d 16:50:35"},
                "neighbor-id": "10.189.5.253",
                "neighbor-priority": "128",
                "neighbor-up-time": {"#text": "3w0d 16:50:35"},
                "options": "0x52",
                "ospf-area": "0.0.0.8",
                "ospf-neighbor-state": "Full",
                "ospf-neighbor-topology": {
                    "ospf-neighbor-topology-state": "Bidirectional",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            },
            {
                "activity-timer": "31",
                "adj-sid-list": {
                    "spring-adjacency-labels": [
                        {"adj-sid-type": "Protected", "flags": "BVL", "label": "2567"},
                        {"adj-sid-type": "UnProtected", "flags": "VL", "label": "2568"},
                    ]
                },
                "bdr-address": "0.0.0.0",
                "dr-address": "0.0.0.0",
                "interface-name": "ge-0/0/1.0",
                "neighbor-address": "10.169.14.121",
                "neighbor-adjacency-time": {"#text": "3w2d 03:12:15"},
                "neighbor-id": "10.169.14.240",
                "neighbor-priority": "128",
                "neighbor-up-time": {"#text": "3w2d 03:12:20"},
                "options": "0x52",
                "ospf-area": "0.0.0.8",
                "ospf-neighbor-state": "Full",
                "ospf-neighbor-topology": {
                    "ospf-neighbor-topology-state": "Bidirectional",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            },
            {
                "activity-timer": "39",
                "adj-sid-list": {
                    "spring-adjacency-labels": [
                        {
                            "adj-sid-type": "Protected",
                            "flags": "BVL",
                            "label": "167966",
                        },
                        {
                            "adj-sid-type": "UnProtected",
                            "flags": "VL",
                            "label": "167967",
                        },
                    ]
                },
                "bdr-address": "0.0.0.0",
                "dr-address": "0.0.0.0",
                "interface-name": "ge-0/0/2.0",
                "neighbor-address": "10.19.198.26",
                "neighbor-adjacency-time": {"#text": "1w5d 20:40:14"},
                "neighbor-id": "10.19.198.239",
                "neighbor-priority": "1",
                "neighbor-up-time": {"#text": "1w5d 20:40:14"},
                "options": "0x52",
                "ospf-area": "0.0.0.8",
                "ospf-neighbor-state": "Full",
                "ospf-neighbor-topology": {
                    "ospf-neighbor-topology-state": "Bidirectional",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            },
        ]
    }
}

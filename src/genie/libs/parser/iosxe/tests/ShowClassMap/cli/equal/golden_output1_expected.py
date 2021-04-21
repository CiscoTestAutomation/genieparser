expected_output = {
    "class_maps": {
        "system-cpp-police-ewlc-control": {
            "match_criteria": "match-any",
            "cm_id": 23,
            "description": "EWLC Control",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-topology-control": {
            "match_criteria": "match-any",
            "cm_id": 2,
            "description": "Topology control",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-sw-forward": {
            "match_criteria": "match-any",
            "cm_id": 3,
            "description": "Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-default": {
            "match_criteria": "match-any",
            "cm_id": 4,
            "description": "EWLC Data, Inter FED Traffic",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-sys-data": {
            "match_criteria": "match-any",
            "cm_id": 5,
            "description": "Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-punt-webauth": {
            "match_criteria": "match-any",
            "cm_id": 6,
            "description": "Punt Webauth",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-l2lvx-control": {
            "match_criteria": "match-any",
            "cm_id": 7,
            "description": "L2 LVX control packets",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "class-default": {
            "match_criteria": "match-any",
            "cm_id": 0,
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "any"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-forus": {
            "match_criteria": "match-any",
            "cm_id": 8,
            "description": "Forus Address resolution and Forus traffic",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-multicast-end-station": {
            "match_criteria": "match-any",
            "cm_id": 9,
            "description": "MCAST END STATION",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-high-rate-app": {
            "match_criteria": "match-any",
            "cm_id": 10,
            "description": "High Rate Applications",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-multicast": {
            "match_criteria": "match-any",
            "cm_id": 11,
            "description": "MCAST Data",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-l2-control": {
            "match_criteria": "match-any",
            "cm_id": 12,
            "description": "L2 control",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-dot1x-auth": {
            "match_criteria": "match-any",
            "cm_id": 13,
            "description": "DOT1X Auth",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-data": {
            "match_criteria": "match-any",
            "cm_id": 14,
            "description": "ICMP redirect, ICMP_GEN and BROADCAST",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-stackwise-virt-control": {
            "match_criteria": "match-any",
            "cm_id": 15,
            "description": "Stackwise Virtual OOB",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-control-low-priority": {
            "match_criteria": "match-any",
            "cm_id": 16,
            "description": "General punt",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "non-client-nrt-class": {
            "match_criteria": "match-any",
            "cm_id": 1,
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "non_client_nrt"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-routing-control": {
            "match_criteria": "match-any",
            "cm_id": 17,
            "description": "Routing control and Low Latency",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-protocol-snooping": {
            "match_criteria": "match-any",
            "cm_id": 18,
            "description": "Protocol snooping",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-dhcp-snooping": {
            "match_criteria": "match-any",
            "cm_id": 19,
            "description": "DHCP snooping",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-ios-routing": {
            "match_criteria": "match-any",
            "cm_id": 21,
            "description": "L2 control, Topology control, Routing control, Low Latency",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-system-critical": {
            "match_criteria": "match-any",
            "cm_id": 20,
            "description": "System Critical and Gold Pkt",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        },
        "system-cpp-police-ios-feature": {
            "match_criteria": "match-any",
            "cm_id": 22,
            "description": "ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed",
            "index": {
                1: {
                    "match": {
                        "policy": [
                            "none"
                        ]
                    }
                }
            }
        }
    }
}
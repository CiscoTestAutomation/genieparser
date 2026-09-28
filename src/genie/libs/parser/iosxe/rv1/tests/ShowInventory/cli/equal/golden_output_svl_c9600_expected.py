expected_output = {
    "main": {
        "chassis": {
            "switch_1": {
                "name": "Switch 1 Chassis",
                "descr": "Cisco Catalyst 9600 Series 6 Slot Chassis",
                "pid": "C9606R",
                "vid": "V01",
                "sn": "FXS2346Q1SV",
            },
            "switch_2": {
                "name": "Switch 2 Chassis",
                "descr": "Cisco Catalyst 9600 Series 6 Slot Chassis",
                "pid": "C9606R",
                "vid": "V01",
                "sn": "FXS2346Q1S6",
            },
        },
        "supervisor": {
            "switch_1": {
                "name": "Switch 1 Slot 4 Supervisor",
                "descr": "Supervisor 1 Module",
                "pid": "C9600-SUP-1",
                "vid": "V01",
                "sn": "CAT2348L6PH",
            },
            "switch_2": {
                "name": "Switch 2 Slot 4 Supervisor",
                "descr": "Supervisor 1 Module",
                "pid": "C9600-SUP-1",
                "vid": "V01",
                "sn": "CAT2348L6LL",
            },
        },
    },
    "slot": {
        "Switch_1_Slot_1_Linecard": {
            "lc": {
                "C9600-LC-48YL": {
                    "name": "Switch 1 Slot 1 Linecard",
                    "descr": "48-Port 10GE / 25GE",
                    "pid": "C9600-LC-48YL",
                    "vid": "V01",
                    "sn": "CAT2346L5LH",
                }
            },
            "pluggable": {
                "TwentyFiveGigE1/1/0/9": {
                    "name": "TwentyFiveGigE1/1/0/9",
                    "descr": "SFP 25GE CU2M",
                    "pid": "SFP-H25G-CU2M",
                    "vid": "V01",
                    "sn": "LRM2112X041",
                },
                "TwentyFiveGigE1/1/0/10": {
                    "name": "TwentyFiveGigE1/1/0/10",
                    "descr": "SFP 25GE CU3M",
                    "pid": "SFP-H25G-CU3M",
                    "vid": "V01",
                    "sn": "APF2501136Y",
                },
                "TwentyFiveGigE1/1/0/12": {
                    "name": "TwentyFiveGigE1/1/0/12",
                    "descr": "SFP 25GE CU3M",
                    "pid": "SFP-H25G-CU3M",
                    "vid": "V01",
                    "sn": "APF2248008R",
                },
                "TwentyFiveGigE1/1/0/27": {
                    "name": "TwentyFiveGigE1/1/0/27",
                    "descr": "GE T",
                    "pid": "SP7041-E",
                    "vid": "",
                    "sn": "MTC150203LS",
                },
                "TwentyFiveGigE1/1/0/40": {
                    "name": "TwentyFiveGigE1/1/0/40",
                    "descr": "10GE CU1M",
                    "pid": "SFP-H10GB-CU1M",
                    "vid": "V03",
                    "sn": "TED2135A03N",
                },
            },
        },
        "Switch_1_Slot_5_Linecard": {
            "lc": {
                "C9600-LC-48TX": {
                    "name": "Switch 1 Slot 5 Linecard",
                    "descr": "48-Port 10GE and MGIG COPPER",
                    "pid": "C9600-LC-48TX",
                    "vid": "V00",
                    "sn": "CAT2324L1GW",
                }
            }
        },
        "Switch_1_Slot_4_Supervisor": {
            "other": {
                "C9600-PWR-2KWAC": {
                    "name": "Switch 1 Power Supply Module 1",
                    "descr": "Cisco Catalyst 9600 Series 2000W AC Power Supply",
                    "pid": "C9600-PWR-2KWAC",
                    "vid": "V01",
                    "sn": "POG2330D64V",
                }
            }
        },
        "Switch_2_Slot_1_Linecard": {
            "lc": {
                "C9600-LC-24C": {
                    "name": "Switch 2 Slot 1 Linecard",
                    "descr": "24-Port 40GE/12-Port 100GE",
                    "pid": "C9600-LC-24C",
                    "vid": "V02",
                    "sn": "FDO26422YJL",
                }
            },
            "pluggable": {
                "FortyGigabitEthernet2/1/0/7-qsa": {
                    "name": "FortyGigabitEthernet2/1/0/7-qsa",
                    "descr": "CVR 10GE SFP",
                    "pid": "CVR-QSFP-SFP10G",
                    "vid": "V02",
                    "sn": "DTY2352008J",
                },
                "FortyGigabitEthernet2/1/0/7": {
                    "name": "FortyGigabitEthernet2/1/0/7",
                    "descr": "GE T",
                    "pid": "GLC-TE",
                    "vid": "V01",
                    "sn": "AVC224922YG",
                },
            },
        },
        "Switch_2_Slot_2_Linecard": {
            "lc": {
                "C9600-LC-48TX": {
                    "name": "Switch 2 Slot 2 Linecard",
                    "descr": "48-Port 10GE and MGIG COPPER",
                    "pid": "C9600-LC-48TX",
                    "vid": "V01",
                    "sn": "CAT2343L135",
                }
            }
        },
        "Switch_2_Slot_6_Linecard": {
            "lc": {
                "C9600-LC-48YL": {
                    "name": "Switch 2 Slot 6 Linecard",
                    "descr": "48-Port 10GE / 25GE",
                    "pid": "C9600-LC-48YL",
                    "vid": "V01",
                    "sn": "CAT2348L010",
                }
            },
            "pluggable": {
                "TwentyFiveGigE2/6/0/9": {
                    "name": "TwentyFiveGigE2/6/0/9",
                    "descr": "SFP 25GE CU2M",
                    "pid": "SFP-H25G-CU2M",
                    "vid": "V01",
                    "sn": "LRM2112X041",
                },
                "TwentyFiveGigE2/6/0/10": {
                    "name": "TwentyFiveGigE2/6/0/10",
                    "descr": "SFP 25GE CU3M",
                    "pid": "SFP-H25G-CU3M",
                    "vid": "V01",
                    "sn": "APF2501136Y",
                },
                "TwentyFiveGigE2/6/0/11": {
                    "name": "TwentyFiveGigE2/6/0/11",
                    "descr": "SFP 25GE CU3M",
                    "pid": "SFP-H25G-CU3M",
                    "vid": "V01",
                    "sn": "APF21170228",
                },
                "TwentyFiveGigE2/6/0/40": {
                    "name": "TwentyFiveGigE2/6/0/40",
                    "descr": "10GE CU3M",
                    "pid": "SFP-H10GB-CU3M",
                    "vid": "V03",
                    "sn": "JPC2051094J",
                },
            },
        },
        "Switch_2_Slot_4_Supervisor": {
            "other": {
                "C9600-PWR-2KWAC": {
                    "name": "Switch 2 Power Supply Module 1",
                    "descr": "Cisco Catalyst 9600 Series 2000W AC Power Supply",
                    "pid": "C9600-PWR-2KWAC",
                    "vid": "V01",
                    "sn": "QCS23344ZLZ",
                }
            }
        },
    },
}

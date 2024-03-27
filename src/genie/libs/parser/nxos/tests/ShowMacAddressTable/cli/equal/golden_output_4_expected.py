expected_output = {
    "mac_table": {
        "vlans": {
            "-": {
                "vlan": "-",
                "mac_addresses": {
                    "0000.eeef.f113": {
                        "mac_address": "0000.eeef.f113",
                        "entry": "G",
                        "interfaces": {
                            "Sup-eth1(R)(Po90.275)": {
                                "interface": "Sup-eth1(R)(Po90.275)",
                                "mac_type": "static",
                                "age": "-"
                            }
                        },
                        "secure": "F",
                        "ntfy": "F"
                    },
                    "0000.eeef.f118": {
                        "mac_address": "0000.eeef.f118",
                        "entry": "*",
                        "drop": {
                            "drop": True,
                            "mac_type": "static",
                            "age": "-"
                        },
                        "interfaces": {
                            "Ethernet17/3.280": {
                                "interface": "Ethernet17/3.280",
                                "mac_type": "static",
                                "age": "-"
                            }
                        },
                        "secure": "F",
                        "ntfy": "F"
                    }
                }
            },
            "301": {
                "vlan": "301",
                "mac_addresses": {
                    "0000.eeef.f12d": {
                        "mac_address": "0000.eeef.f12d",
                        "entry": "G",
                        "interfaces": {
                            "Sup-eth1(R)": {
                                "interface": "Sup-eth1(R)",
                                "mac_type": "static",
                                "age": "-"
                            }
                        },
                        "secure": "F",
                        "ntfy": "F"
                    }
                }
            },
            "440": {
                "vlan": "440",
                "mac_addresses": {
                    "0000.eeef.f1b8": {
                        "mac_address": "0000.eeef.f1b8",
                        "entry": "G",
                        "interfaces": {
                            "vPC Peer-Link(R)": {
                                "interface": "vPC Peer-Link(R)",
                                "mac_type": "static",
                                "age": "-"
                            }
                        },
                        "secure": "F",
                        "ntfy": "F"
                    }
                }
            }
        }
    }
}


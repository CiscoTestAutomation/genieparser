expected_output={
    "asic": {
        "0": {
            "table": {
                "Mac Address Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "32768",
                                    "used": "21",
                                    "used_percent": "0.06%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "21"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "22",
                                    "used_percent": "2.15%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "22"
                                }
                            }
                        }
                    }
                },
                "L3 Multicast": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "10",
                                    "used_percent": "0.12%",
                                    "v4": "10",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "10",
                                    "used_percent": "1.95%",
                                    "v4": "4",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "L2 Multicast": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "11",
                                    "used_percent": "2.15%",
                                    "v4": "3",
                                    "v6": "8",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "IP Route Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "24576",
                                    "used": "14",
                                    "used_percent": "0.06%",
                                    "v4": "13",
                                    "v6": "0",
                                    "mpls": "1",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "24",
                                    "used_percent": "0.29%",
                                    "v4": "11",
                                    "v6": "10",
                                    "mpls": "2",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "QOS ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "5120",
                                    "used": "85",
                                    "used_percent": "1.66%",
                                    "v4": "28",
                                    "v6": "38",
                                    "mpls": "0",
                                    "other": "19"
                                }
                            }
                        }
                    }
                },
                "Security ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "5120",
                                    "used": "131",
                                    "used_percent": "2.56%",
                                    "v4": "26",
                                    "v6": "60",
                                    "mpls": "0",
                                    "other": "45"
                                }
                            }
                        }
                    }
                },
                "Netflow ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "6",
                                    "used_percent": "2.34%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2"
                                },
                                "O": {
                                    "max": "768",
                                    "used": "6",
                                    "used_percent": "0.78%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2"
                                }
                            }
                        }
                    }
                },
                "PBR ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "36",
                                    "used_percent": "3.52%",
                                    "v4": "30",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Flow SPAN ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "1024",
                                    "used": "13",
                                    "used_percent": "1.27%",
                                    "v4": "3",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "4"
                                }
                            }
                        }
                    }
                },
                "Control Plane": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "290",
                                    "used_percent": "56.64%",
                                    "v4": "138",
                                    "v6": "106",
                                    "mpls": "0",
                                    "other": "46"
                                }
                            }
                        }
                    }
                },
                "Tunnel Termination": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "20",
                                    "used_percent": "3.91%",
                                    "v4": "8",
                                    "v6": "12",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Lisp Inst Mapping": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "2048",
                                    "used": "1",
                                    "used_percent": "0.05%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "Security Association": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "4",
                                    "used_percent": "1.56%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "CTS Cell Matrix/VPN Label": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "O": {
                                    "max": "8192",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "O": {
                                    "max": "512",
                                    "used": "1",
                                    "used_percent": "0.20%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "Client Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "4096",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Input Group LE": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Output Group LE": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "O": {
                                    "max": "1024",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Macsec SPD": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "2",
                                    "used_percent": "0.78%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "2"
                                }
                            }
                        }
                    }
                }
            }
        },
        "1": {
            "table": {
                "Mac Address Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "32768",
                                    "used": "21",
                                    "used_percent": "0.06%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "21"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "22",
                                    "used_percent": "2.15%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "22"
                                }
                            }
                        }
                    }
                },
                "L3 Multicast": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "10",
                                    "used_percent": "0.12%",
                                    "v4": "10",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "10",
                                    "used_percent": "1.95%",
                                    "v4": "4",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "L2 Multicast": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "11",
                                    "used_percent": "2.15%",
                                    "v4": "3",
                                    "v6": "8",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "IP Route Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "24576",
                                    "used": "14",
                                    "used_percent": "0.06%",
                                    "v4": "13",
                                    "v6": "0",
                                    "mpls": "1",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "8192",
                                    "used": "24",
                                    "used_percent": "0.29%",
                                    "v4": "11",
                                    "v6": "10",
                                    "mpls": "2",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "QOS ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "5120",
                                    "used": "81",
                                    "used_percent": "1.58%",
                                    "v4": "27",
                                    "v6": "36",
                                    "mpls": "0",
                                    "other": "18"
                                }
                            }
                        }
                    }
                },
                "Security ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "5120",
                                    "used": "131",
                                    "used_percent": "2.56%",
                                    "v4": "26",
                                    "v6": "60",
                                    "mpls": "0",
                                    "other": "45"
                                }
                            }
                        }
                    }
                },
                "Netflow ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "6",
                                    "used_percent": "2.34%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2"
                                },
                                "O": {
                                    "max": "768",
                                    "used": "6",
                                    "used_percent": "0.78%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2"
                                }
                            }
                        }
                    }
                },
                "PBR ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "36",
                                    "used_percent": "3.52%",
                                    "v4": "30",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Flow SPAN ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "1024",
                                    "used": "13",
                                    "used_percent": "1.27%",
                                    "v4": "3",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "4"
                                }
                            }
                        }
                    }
                },
                "Control Plane": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "290",
                                    "used_percent": "56.64%",
                                    "v4": "138",
                                    "v6": "106",
                                    "mpls": "0",
                                    "other": "46"
                                }
                            }
                        }
                    }
                },
                "Tunnel Termination": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "512",
                                    "used": "20",
                                    "used_percent": "3.91%",
                                    "v4": "8",
                                    "v6": "12",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Lisp Inst Mapping": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "2048",
                                    "used": "1",
                                    "used_percent": "0.05%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "Security Association": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "3",
                                    "used_percent": "1.17%",
                                    "v4": "1",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "CTS Cell Matrix/VPN Label": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "O": {
                                    "max": "8192",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "O": {
                                    "max": "512",
                                    "used": "1",
                                    "used_percent": "0.20%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "1"
                                }
                            }
                        }
                    }
                },
                "Client Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "4096",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Input Group LE": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Output Group LE": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "O": {
                                    "max": "1024",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "Macsec SPD": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "256",
                                    "used": "2",
                                    "used_percent": "0.78%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "2"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
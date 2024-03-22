expected_output = {
    "asic": {
        "0": {
            "table": {
                "Mac Address Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "32768",
                                    "used": "53",
                                    "used_percent": "0.16%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "53"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "768",
                                    "used": "22",
                                    "used_percent": "2.86%",
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
                                    "max": "32768",
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
                                    "max": "768",
                                    "used": "6",
                                    "used_percent": "0.78%",
                                    "v4": "3",
                                    "v6": "3",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "L2 Multicast": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "2304",
                                    "used": "7",
                                    "used_percent": "0.30%",
                                    "v4": "3",
                                    "v6": "4",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "IP Route Table": {
                    "subtype": {
                        "EM/LPM": {
                            "dir": {
                                "I": {
                                    "max": "212992",
                                    "used": "17",
                                    "used_percent": "0.01%",
                                    "v4": "17",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0"
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1536",
                                    "used": "16",
                                    "used_percent": "1.04%",
                                    "v4": "10",
                                    "v6": "3",
                                    "mpls": "3",
                                    "other": "0"
                                }
                            }
                        }
                    }
                },
                "QOS ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "45",
                                    "used_percent": "4.39%",
                                    "v4": "15",
                                    "v6": "20",
                                    "mpls": "0",
                                    "other": "10"
                                },
                                "O": {
                                    "max": "1024",
                                    "used": "40",
                                    "used_percent": "3.91%",
                                    "v4": "13",
                                    "v6": "18",
                                    "mpls": "0",
                                    "other": "9"
                                }
                            }
                        }
                    }
                },
                "Security ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "4096",
                                    "used": "88",
                                    "used_percent": "2.15%",
                                    "v4": "12",
                                    "v6": "36",
                                    "mpls": "0",
                                    "other": "40"
                                },
                                "O": {
                                    "max": "4096",
                                    "used": "43",
                                    "used_percent": "1.05%",
                                    "v4": "14",
                                    "v6": "24",
                                    "mpls": "0",
                                    "other": "5"
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
                                    "max": "512",
                                    "used": "6",
                                    "used_percent": "1.17%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2"
                                },
                                "O": {
                                    "max": "512",
                                    "used": "6",
                                    "used_percent": "1.17%",
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
                                    "max": "27648",
                                    "used": "53",
                                    "used_percent": "0.19%",
                                    "v4": "37",
                                    "v6": "16",
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
                                "I": {
                                    "max": "512",
                                    "used": "4",
                                    "used_percent": "0.78%",
                                    "v4": "1",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "1"
                                },
                                "O": {
                                    "max": "512",
                                    "used": "4",
                                    "used_percent": "0.78%",
                                    "v4": "1",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "1"
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
                                    "used": "283",
                                    "used_percent": "55.27%",
                                    "v4": "130",
                                    "v6": "106",
                                    "mpls": "0",
                                    "other": "47"
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
                                    "max": "768",
                                    "used": "33",
                                    "used_percent": "4.30%",
                                    "v4": "12",
                                    "v6": "20",
                                    "mpls": "0",
                                    "other": "1"
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
                                    "max": "1024",
                                    "used": "1",
                                    "used_percent": "0.10%",
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
                                    "max": "512",
                                    "used": "4",
                                    "used_percent": "0.78%",
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
                                    "max": "32768",
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
                                    "max": "768",
                                    "used": "1",
                                    "used_percent": "0.13%",
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

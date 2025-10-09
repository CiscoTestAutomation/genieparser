expected_output = {
    "asic": {
        "0": {
            "table": {
                "Mac Address Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "16384",
                                    "used": "45",
                                    "used_percent": "0.27%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "45",
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
                                    "other": "22",
                                }
                            }
                        },
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
                                    "other": "0",
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "67",
                                    "used_percent": "6.54%",
                                    "v4": "3",
                                    "v6": "64",
                                    "mpls": "0",
                                    "other": "0",
                                }
                            }
                        },
                    }
                },
                "L2 Multicast": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "16384",
                                    "used": "0",
                                    "used_percent": "0.00%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "0",
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "1024",
                                    "used": "11",
                                    "used_percent": "1.07%",
                                    "v4": "3",
                                    "v6": "8",
                                    "mpls": "0",
                                    "other": "0",
                                }
                            }
                        },
                    }
                },
                "IP Route Table": {
                    "subtype": {
                        "EM": {
                            "dir": {
                                "I": {
                                    "max": "49152",
                                    "used": "8",
                                    "used_percent": "0.02%",
                                    "v4": "7",
                                    "v6": "0",
                                    "mpls": "1",
                                    "other": "0",
                                }
                            }
                        },
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "65536",
                                    "used": "20",
                                    "used_percent": "0.03%",
                                    "v4": "7",
                                    "v6": "10",
                                    "mpls": "2",
                                    "other": "1",
                                }
                            }
                        },
                    }
                },
                "QOS ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "IO": {
                                    "max": "3072",
                                    "used": "85",
                                    "used_percent": "2.77%",
                                    "v4": "28",
                                    "v6": "38",
                                    "mpls": "0",
                                    "other": "19",
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
                                    "max": "18432",
                                    "used": "131",
                                    "used_percent": "0.71%",
                                    "v4": "26",
                                    "v6": "60",
                                    "mpls": "0",
                                    "other": "45",
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
                                    "max": "1024",
                                    "used": "6",
                                    "used_percent": "0.59%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2",
                                },
                                "O": {
                                    "max": "2048",
                                    "used": "6",
                                    "used_percent": "0.29%",
                                    "v4": "2",
                                    "v6": "2",
                                    "mpls": "0",
                                    "other": "2",
                                },
                            }
                        }
                    }
                },
                "PBR ACL": {
                    "subtype": {
                        "TCAM": {
                            "dir": {
                                "I": {
                                    "max": "16384",
                                    "used": "36",
                                    "used_percent": "0.22%",
                                    "v4": "30",
                                    "v6": "6",
                                    "mpls": "0",
                                    "other": "0",
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
                                    "other": "4",
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
                                    "max": "1024",
                                    "used": "320",
                                    "used_percent": "31.25%",
                                    "v4": "168",
                                    "v6": "106",
                                    "mpls": "0",
                                    "other": "46",
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
                                    "max": "1024",
                                    "used": "20",
                                    "used_percent": "1.95%",
                                    "v4": "8",
                                    "v6": "12",
                                    "mpls": "0",
                                    "other": "0",
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
                                    "other": "1",
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
                                    "other": "0",
                                },
                                "O": {
                                    "max": "512",
                                    "used": "6",
                                    "used_percent": "1.17%",
                                    "v4": "0",
                                    "v6": "0",
                                    "mpls": "0",
                                    "other": "6",
                                },
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
                                    "other": "0",
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
                                    "other": "1",
                                }
                            }
                        },
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
                                    "other": "0",
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
                                    "other": "0",
                                }
                            }
                        },
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
                                    "other": "0",
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
                                    "other": "0",
                                }
                            }
                        }
                    }
                },
            }
        }
    }
}

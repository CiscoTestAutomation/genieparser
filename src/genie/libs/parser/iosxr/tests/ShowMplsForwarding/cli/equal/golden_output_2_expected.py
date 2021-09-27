

expected_output = {
    "local_label": {
        "24000": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.4.1.1/32": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.90": {
                                    "next_hop": "10.12.90.1",
                                    "bytes_switched": 9321675
                                }
                            }
                        }
                    }
                }
            }
        },
        "24002": {
            "outgoing_label": {
                "Pop": {
                    "prefix_or_id": {
                        "10.13.110.0/24": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.110": {
                                    "next_hop": "10.12.110.1",
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "24003": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.13.115.0/24": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.115": {
                                    "next_hop": "10.12.115.1",
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "24004": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.13.90.0/24": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.90": {
                                    "next_hop": "10.12.90.1",
                                    "bytes_switched": 0
                                },
                                "GigabitEthernet0/0/0/1.90": {
                                    "next_hop": "10.23.90.3",
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "24005": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "2001:1:1:1::1/128[V]": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.390": {
                                    "next_hop": "fe80::f816:3eff:fe53:2cc7",
                                    "bytes_switched": 3928399
                                }
                            }
                        }
                    }
                }
            }
        },
        "24006": {
            "outgoing_label": {
                "Aggregate": {
                    "prefix_or_id": {
                        "VRF1: Per-VRF Aggr[V]": {
                            "outgoing_interface": {
                                "VRF1": {
                                    "bytes_switched": 832
                                }
                            }
                        }
                    }
                }
            }
        },
        "24007": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "2001:3:3:3::3/128[V]": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/1.390": {
                                    "next_hop": "fe80::5c00:ff:fe02:7",
                                    "bytes_switched": 3762357
                                }
                            }
                        }
                    }
                }
            }
        },
        "24008": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.4.1.1/32[V]": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.390": {
                                    "next_hop": "10.12.90.1",
                                    "bytes_switched": 6281421
                                }
                            }
                        }
                    }
                }
            }
        },
        "24009": {
            "outgoing_label": {
                "Aggregate": {
                    "prefix_or_id": {
                        "VRF1: Per-VRF Aggr[V]": {
                            "outgoing_interface": {
                                "VRF1": {
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "24010": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.36.3.3/32[V]": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/1.390": {
                                    "next_hop": "10.23.90.3",
                                    "bytes_switched": 7608898
                                }
                            }
                        }
                    }
                }
            }
        },
        "24011": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.1.0.0/8": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.120": {
                                    "next_hop": "10.12.120.1",
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "24012": {
            "outgoing_label": {
                "Unlabelled": {
                    "prefix_or_id": {
                        "10.13.120.0/24": {
                            "outgoing_interface": {
                                "GigabitEthernet0/0/0/0.120": {
                                    "next_hop": "10.12.120.1",
                                    "bytes_switched": 0
                                },
                                "GigabitEthernet0/0/0/1.120": {
                                    "next_hop": "10.23.120.3",
                                    "bytes_switched": 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

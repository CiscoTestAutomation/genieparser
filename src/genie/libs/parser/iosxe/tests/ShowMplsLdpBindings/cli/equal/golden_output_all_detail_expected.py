expected_output = {
    "vrf": {
        "default": {
            "lib_entry": {
                "10.169.197.92/30": {
                    "rev": "4",
                    "label_binding": {
                        "label": {
                            "imp-null": {
                                "owner": "LDP",
                                "advertised_to": [
                                    "10.169.197.252:0",
                                    "10.169.197.253:0",
                                ],
                            }
                        }
                    },
                    "checkpoint": "none",
                    "remote_binding": {
                        "label": {
                            "126": {
                                "lsr_id": {
                                    "10.169.197.252": {
                                        "label_space_id": {0: {"checkpointed": True}}
                                    }
                                }
                            }
                        }
                    },
                },
                "10.120.202.64/32": {
                    "rev": "12",
                    "label_binding": {
                        "label": {
                            "2027": {
                                "owner": "LDP",
                                "advertised_to": [
                                    "10.169.197.252:0",
                                    "10.169.197.253:0",
                                ],
                            }
                        }
                    },
                    "checkpoint": "none",
                    "remote_binding": {
                        "label": {
                            "308016": {
                                "lsr_id": {
                                    "10.169.197.253": {
                                        "label_space_id": {0: {"checkpointed": True}}
                                    }
                                }
                            },
                            "516": {
                                "lsr_id": {
                                    "10.169.197.252": {
                                        "label_space_id": {0: {"checkpointed": True}}
                                    }
                                }
                            },
                        }
                    },
                },
                "10.120.202.56/30": {
                    "rev": "1085",
                    "label_binding": {
                        "label": {
                            "6589": {
                                "owner": "LDP",
                                "advertised_to": [
                                    "10.169.197.252:0",
                                    "10.169.197.253:0",
                                ],
                            }
                        }
                    },
                    "checkpoint": "none",
                    "remote_binding": {
                        "label": {
                            "1014": {
                                "lsr_id": {
                                    "10.169.197.252": {
                                        "label_space_id": {0: {"checkpointed": True}}
                                    }
                                }
                            }
                        }
                    },
                },
                "10.120.202.48/30": {
                    "rev": "18",
                    "label_binding": {
                        "label": {
                            "2030": {
                                "owner": "LDP",
                                "advertised_to": [
                                    "10.169.197.252:0",
                                    "10.169.197.253:0",
                                ],
                            }
                        }
                    },
                    "checkpoint": "none",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.169.197.252": {
                                        "label_space_id": {0: {"checkpointed": True}}
                                    }
                                }
                            }
                        }
                    },
                },
            }
        }
    }
}

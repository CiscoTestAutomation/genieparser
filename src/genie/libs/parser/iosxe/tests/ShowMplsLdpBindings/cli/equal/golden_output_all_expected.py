expected_output = {
    "vrf": {
        "vrf1": {
            "lib_entry": {
                "10.11.0.0/24": {
                    "rev": "7",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {"10.132.0.1": {"label_space_id": {0: {}}}}
                            }
                        }
                    },
                },
                "10.12.0.0/24": {
                    "label_binding": {"label": {"17": {}}},
                    "rev": "8",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {"10.132.0.1": {"label_space_id": {0: {}}}}
                            }
                        }
                    },
                },
                "10.0.0.0/24": {
                    "rev": "6",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {"10.132.0.1": {"label_space_id": {0: {}}}}
                            }
                        }
                    },
                },
            }
        },
        "default": {
            "lib_entry": {
                "10.11.0.0/24": {
                    "label_binding": {"label": {"imp-null": {}}},
                    "rev": "15",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {"10.131.0.1": {"label_space_id": {0: {}}}}
                            }
                        }
                    },
                },
                "10.0.0.0/24": {
                    "label_binding": {"label": {"imp-null": {}}},
                    "rev": "4",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {"10.131.0.1": {"label_space_id": {0: {}}}}
                            }
                        }
                    },
                },
            }
        },
    }
}

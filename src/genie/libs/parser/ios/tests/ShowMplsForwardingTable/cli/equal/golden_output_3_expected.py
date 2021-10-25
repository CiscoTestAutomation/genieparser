expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                16: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '192.168.154.2-A': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/1/2': {
                                            'next_hop': '192.168.154.2',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                17: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '192.168.4.2-A': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/1/1': {
                                            'next_hop': '192.168.4.2',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                18: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '192.168.111.2-A': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/1/0': {
                                            'next_hop': '192.168.111.2',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                19: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '192.168.220.2-A': {
                                    'outgoing_interface': {
                                        'TenGigabitEthernet0/0/0': {
                                            'next_hop': '192.168.220.2',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16002: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '10.16.2.2/32': {
                                    'outgoing_interface': {
                                        'TenGigabitEthernet0/0/0': {
                                            'next_hop': '192.168.220.2',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet0/1/0': {
                                            'next_hop': '192.168.111.2',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet0/1/1': {
                                            'next_hop': '192.168.4.2',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet0/1/2': {
                                            'next_hop': '192.168.154.2',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

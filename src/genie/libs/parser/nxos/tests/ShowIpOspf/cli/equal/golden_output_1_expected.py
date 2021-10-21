

expected_output = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'areas': {
                                '0.0.0.1': {
                                    'area_id': '0.0.0.1',
                                    'area_type': 'stub',
                                    'authentication': 'none',
                                    'default_cost': 1,
                                    'existed': '08:30:42',
                                    'numbers': {
                                        'active_interfaces': 3,
                                        'interfaces': 3,
                                        'loopback_interfaces': 0,
                                        'passive_interfaces': 0
                                    },
                                    'ranges': {
                                        '10.4.0.0/16': {
                                            'advertise': False,
                                            'cost': 31,
                                            'net': 1,
                                            'prefix': '10.4.0.0/16'
                                        }
                                    },
                                    'statistics': {
                                        'area_scope_lsa_cksum_sum': '11',
                                        'area_scope_lsa_count': 11,
                                        'spf_last_run_time': 0.000464,
                                        'spf_runs_count': 33
                                    }
                                }
                            },
                            'auto_cost': {
                                'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 40000
                            },
                            'enable': True,
                            'discard_route_external': True,
                            'discard_route_internal': True,
                            'graceful_restart': {
                                'ietf': {
                                    'enable': True,
                                    'exist_status': 'none',
                                    'restart_interval': 60,
                                    'state': 'Inactive',
                                    'type': 'ietf'
                                }
                            },
                            'instance': 1,
                            'nsr': {
                                'enable': True
                            },
                            'numbers': {
                                'active_areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                },
                                'areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                }
                            },
                            'opaque_lsa_enable': True,
                            'this_router_is': 'an area border and '
                            'autonomous system boundary',
                            'preference': {
                                'single_value': {
                                    'all': 110
                                }
                            },
                            'router_id': '10.151.22.22',
                            'single_tos_routes_enable': True,
                            'redistribution': {
                                'bgp': {
                                    'bgp_id': 100
                                }
                            },
                            'spf_control': {
                                'paths': 8,
                                'throttle': {
                                    'lsa': {
                                        'group_pacing': 10,
                                        'hold': 5000,
                                        'maximum': 5000,
                                        'minimum': 1000,
                                        'numbers': {
                                            'external_lsas': {
                                                'checksum': '0',
                                                'total': 0
                                            },
                                            'opaque_as_lsas': {
                                                'checksum': '0',
                                                'total': 0
                                            }
                                        },
                                        'start': 0
                                    },
                                    'spf': {
                                        'hold': 1000,
                                        'maximum': 5000,
                                        'start': 200
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'areas': {
                                '0.0.0.0': {
                                    'area_id': '0.0.0.0',
                                    'area_type': 'normal',
                                    'authentication': 'none',
                                    'existed': '08:30:42',
                                    'numbers': {
                                        'active_interfaces': 4,
                                        'interfaces': 4,
                                        'loopback_interfaces': 1,
                                        'passive_interfaces': 0
                                    },
                                    'ranges': {
                                        '10.4.1.0/24': {
                                            'advertise': True,
                                            'cost': 33,
                                            'net': 0,
                                            'prefix': '10.4.1.0/24'
                                        }
                                    },
                                    'statistics': {
                                        'area_scope_lsa_cksum_sum': '19',
                                        'area_scope_lsa_count': 19,
                                        'spf_last_run_time': 0.001386,
                                        'spf_runs_count': 8
                                    }
                                }
                            },
                            'auto_cost': {
                                'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 40000
                            },
                            'bfd': {
                                'enable': True
                            },
                            'database_control': {
                                'max_lsa': 123
                            },
                            'enable': True,
                            'discard_route_external': True,
                            'discard_route_internal': True,
                            'graceful_restart': {
                                'ietf': {
                                    'enable': True,
                                    'exist_status': 'none',
                                    'restart_interval': 60,
                                    'state': 'Inactive',
                                    'type': 'ietf'
                                }
                            },
                            'instance': 1,
                            'nsr': {
                                'enable': True
                            },
                            'numbers': {
                                'active_areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                },
                                'areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                }
                            },
                            'opaque_lsa_enable': True,
                            'preference': {
                                'single_value': {
                                    'all': 110
                                }
                            },
                            'router_id': '10.100.2.2',
                            'single_tos_routes_enable': True,
                            'spf_control': {
                                'paths': 8,
                                'throttle': {
                                    'lsa': {
                                        'group_pacing': 10,
                                        'hold': 5000,
                                        'maximum': 5000,
                                        'minimum': 1000,
                                        'numbers': {
                                            'external_lsas': {
                                                'checksum': '0x7d61',
                                                'total': 1
                                            },
                                            'opaque_as_lsas': {
                                                'checksum': '0',
                                                'total': 0
                                            }
                                        },
                                        'start': 0
                                    },
                                    'spf': {
                                        'hold': 1000,
                                        'maximum': 5000,
                                        'start': 200
                                    }
                                }
                            },
                            'stub_router': {
                                'always': {
                                    'always': True
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

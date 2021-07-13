expected_output = {
    'NO-EXPORT': {
        'statements': {
            10: {
                'actions': {
                    'actions': 'pass',
                    'set_community_list': 'no-export'
                },
                'conditions': {
                    'match_prefix_list': 'NO-EXPORT'
                }
            }
        }
    },
    'all-pass':
        {'statements': {
            1: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {

                }
            }
        }
    },
    'allpass': {
        'statements': {
            10: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {

                }
            }
        }
    },
    'as-path': {
        'statements': {
            10: {
                'actions': {

                },
                'conditions': {

                }
            }
        }
    },
    'aspath': {
        'statements': {
            10: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {
                    'match_as_path_list': 'test'
                }
            },
            20: {
                'actions': {
                    'actions': 'drop'
                },
                'conditions': {

                }
            }
        }
    },
    'test': {
        'statements': {
            1: {
                'actions': {

                },
                'conditions': {

                }
            },
            10: {
                'actions': {
                    'set_route_origin': 'incomplete'
                },
                'conditions': {
                    'match_local_pref_eq': '123'
                }
            },
            20: {
                'actions': {
                    'set_weight': '44'
                },
                'conditions': {
                    'match_med_eq': 100
                }
            }
        }
    },
    'test-community': {
        'statements': {
            10: {
                'actions': {
                    'set_community': ['100:1',
                                      '200:1',
                                      '300:1'],
                    'set_community_no_advertise': True,
                    'set_community_no_export': True
                },
                'conditions': {
                    'match_med_eq': 90
                }
            },
            20: {
                'actions': {
                    'set_community': ['111:1',
                                      '222:1'],
                    'set_community_additive': True,
                    'set_community_no_advertise': True,
                    'set_ext_community_rt': ['100:1',
                                             '200:1'],
                    'set_ext_community_rt_additive': True
                },
                'conditions': {
                    'match_local_pref_eq': '30'
                }
            }
        }
    },
    'test2': {
        'statements': {
            10: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {
                    'match_med_eq': 100,
                    'match_origin_eq': 'egp'
                }
            },
            20: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {
                    'match_nexthop_in': 'prefix-set1'
                }
            },
            30: {
                'actions': {
                    'actions': 'pass'
                },
                'conditions': {
                    'match_ext_community_list': ['test'],
                    'match_local_pref_eq': '130'
                }
            }
        }
    },
        'test3': {
            'statements': {
                10: {
                    'actions': {
                        'actions': 'pass'
                    },
                    'conditions': {

                    }
                },
                20: {
                    'actions': {
                        'actions': 'pass'
                    },
                    'conditions': {
                        'match_area_eq': '10.4.1.1',
                        'match_level_eq': 'level-2'
                    }
                },
                30: {
                    'actions': {
                        'actions': 'pass'
                    },
                    'conditions': {
                        'match_as_path_list': 'test',
                        'match_prefix_list': 'prefix-set1'
                    }
                },
                40: {
                    'actions': {
                        'actions': 'pass'
                    },
                    'conditions': {

                    }
                },
                50: {
                    'actions': {
                        'set_as_path_prepend': 100,
                        'set_as_path_prepend_repeat_n': 10,
                        'set_community': ['100:100'],
                        'set_community_additive': True,
                        'set_community_delete': 'test',
                        'set_community_list': 'test',
                        'set_community_no_advertise': True,
                        'set_community_no_export': True,
                        'set_ext_community_delete': 'test',
                        'set_ext_community_rt': ['300:1',
                                                 '300:2'],
                        'set_ext_community_rt_additive': True,
                        'set_ext_community_soo': '100:100',
                        'set_ext_community_soo_additive': True,
                        'set_level': 'level-1-2',
                        'set_local_pref': 100,
                        'set_med': 113,
                        'set_metric': '100',
                        'set_metric_type': 'type-2',
                        'set_next_hop': '10.4.1.1',
                        'set_ospf_metric': '100',
                        'set_route_origin': 'egp',
                        'set_tag': '111'
                    },
                    'conditions': {

                    }
                }
            }
        },
    'testtest': {
        'statements': {
            10: {
                'actions': {
                    'set_local_pref': 120,
                    'set_med': 111, 'set_metric_type': 'type-1',
                    'set_next_hop': '192.168.1.1'
                },
                'conditions': {
                    'match_area_eq': '0',
                    'match_local_pref_eq': '100',
                    'match_med_eq': 100
                }
            }
        }
    },
    'testtest2': {
        'statements': {
            10: {
                'actions': {
                    'set_community_additive': True,
                    'set_community_list': 'no-export',
                    'set_med': 222
                },
                'conditions': {
                    'match_local_pref_eq': '99',
                    'match_med_eq': 88}
            }
        }
    }
}

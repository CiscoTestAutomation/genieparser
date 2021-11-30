expected_output = {'access-list': {
                        'acl1_default': {
                                  'elements': 5,
                                  'name_hash': '0xf6e3360c'
                                  'entry': {
                                      '1.0': {'remark': '-------------------------------------------------------------------------'},
                                      '2.0': {
                                          'controls_flows': 'false',
                                          'has_children': 'true',
                                          'is_child': 'false',
                                          'source': {
                                              'object_group': {
                                                  'BGP-Peers-In': {
                                                      'destination': {
                                                          'object_group': {
                                                              'BGP-Peers-Out': {
                                                                  'action': 'permit',
                                                                  'protocol': 'tcp',
                                                                  'port': 'bgp',
                                                                  'log': 'false',
                                                                  'hitcnt': '0',
                                                                  'acl_hash': '0xee513685'
                                                              }
                                                            }
                                                          }
                                                      }
                                                  }
                                              }
                                          },
                                      '2.1': {
                                          'controls_flows': 'true',
                                          'has_children': 'false',
                                          'is_child': 'true',
                                          'source': {
                                              'host': {
                                                  '172.16.132.3' : {
                                                      'destination': {
                                                          'host' : {
                                                              '172.16.141.107' : {
                                                                  'action': 'permit',
                                                                  'protocol': 'tcp',
                                                                  'port': 'bgp',
                                                                  'log': 'false',
                                                                  'hitcnt': '0',
                                                                  'acl_hash': '0x666ea2e1'
                                                               }     
                                      '2.2': {
                                          'controls_flows': 'true',
                                          'has_children': 'false',
                                          'is_child': 'true',
                                          'source': {
                                              'host': {
                                                  '172.16.132.3' : {
                                                      'destination': {
                                                          'host' : {
                                                               '172.16.141.108' : {
                                                                   'action': 'permit',
                                                                   'protocol': 'tcp',
                                                                   'port': 'bgp',
                                                                   'log': 'false',
                                                                   'hitcnt': '0',
                                                                   'acl_hash': '0x26750fac'
                                                               }     
                                                          }
                                                      }
                                                  }
                                              }
                                          }
                                      },
                                      '2.3': {
                                          'controls_flows': 'true',
                                          'has_children': 'false',
                                          'is_child': 'true',
                                          'source': {
                                              'host':{
                                                '172.16.132.4' : {
                                                    'destination': {
                                                        'host' : {
                                                            '172.16.141.107' : {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x173720dc'
                                                            }     
                                      '2.4': {
                                          'controls_flows': 'true',
                                          'has_children': 'false',
                                          'is_child': 'true',
                                          'source': {
                                              'host':{
                                                '172.16.132.4' : {
                                                    'destination': {
                                                        'host' : {
                                                            '172.16.141.108' : {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x47628544'
                                                            }     
                                                        }
                                                    }
                                                }
                                            }
                                        }   
                                      },
                                      '3.0': {
                                          'controls_flows': 'true',
                                          'has_children': 'false',
                                          'is_child': 'false',
                                          'source': {
                                              'any': {
                                                  'any': {
                                                      'destination': {
                                                          'any': {
                                                              'any': {
                                                                  'action': 'deny',
                                                                  'protocol': 'ip',
                                                                  'informational_interval': 300
                                                                  'hitcnt': '60',
                                                                  'acl_hash': '0x2296c901'
                                                              }
                                                          }
                                                      }
                                                  }
                                              }
                                          }
                                      },
                                      '4.0': {'remark': '-------------------------------------------------------------------------'}
                                  }
                              },
                             'acl2_default': {
                                 'elements': 5,
                                 'name_hash': '0x7dcb06e2',       
                                 'entry': {
                                    '1.0': {'remark': '-------------------------------------------------------------------------'},
                                    '2.0': {
                                        'controls_flows': 'false',
                                        'has_children': 'true',
                                        'is_child': 'false',
                                        'source': {
                                            'object_group': {
                                                'BGP-Peers-Out': {
                                                    'destination': {
                                                        'object_group': {
                                                            'BGP-Peers-In': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x98b0c6a5'
                                                            }
                                                        }
                                                    }
                                                }
                                            },

                                    '2.1': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x69f5e48c'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '2.2': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x08e9769f'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '2.3': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x01404b2b'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '2.4': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x00e2f9ae'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '3.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'any': {
                                                'any': {
                                                    'destination': {
                                                        'any': {
                                                            'any': {
                                                                'action': 'deny',
                                                                'protocol': 'ip',
                                                                'informational_interval': '300',
                                                                'log', 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x6d1cc2e1'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '4.0': { 'remark': '-------------------------------------------------------------------------' }
                                 }
                             },
                             'TEST': {
                                'entry': {
                                    '1.0': { 'remark': 'test1' },
                                    '2.0': { 'remark': 'test2' },
                                    '3.0': { 'remark': 'test3' },
                                    '4.0': { 'remark': 'test4' },
                                    '5.0': { 'remark': 'test5' },
                                }
                             }

                            'acl2': {
                                'elements': 14,
                                'name_hash': '0x8caa425b',
                                'entry': {
                                    '1.0': {
                                        'controls_flows': 'false',
                                        'has_children': 'true',
                                        'is_child': 'false',
                                        'source': {
                                            'object_group': {
                                                'BGP-Peers-Out': {
                                                    'destination': {
                                                        'object_group': {
                                                            'BGP-Peers-In': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x65c3b335'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.1': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x9f489d59'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.2': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x16c843c4'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.3': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x20b3cece'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.4': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'bgp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x6ec8a21c'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '2.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.45': {
                                                    'destination': {
                                                        'host': {
                                                            '9.17.186.253': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'ldap',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x07859be7'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '3.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.51': {
                                                    'destination': {
                                                        'host': {
                                                            '9.17.186.253': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'https',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x991e76ce'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '4.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.45': {
                                                    'destination': {
                                                        'host': {
                                                            '9.57.182.78': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'https',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x60d91668'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '5.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.50': {
                                                    'destination': {
                                                        'host': {
                                                            '9.17.186.253': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'https',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xb61112e7'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '6.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.51': {
                                                    'destination': {
                                                        'host': {
                                                            '9.17.186.253': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'ldap',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x064fabd6'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '7.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.50': {
                                                    'destination': {
                                                        'host': {
                                                            '9.57.182.78': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'https',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x7fe2a4d1'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '8.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.51': {
                                                    'destination': {
                                                        'host': {
                                                            ''9.17.186.253: {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'ldaps',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xdfc19219'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '9.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'host': {
                                                '10.38.193.51': {
                                                    'destination': {
                                                        'host': {
                                                            '9.57.182.78': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'port': 'ldap',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xa68455fb'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '10.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'any': {
                                                'any4': {
                                                    'destination': {
                                                        'any': {
                                                            'any4': {
                                                                'action': 'deny',
                                                                'protocol': 'ip',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x07bca870'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '11.0': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'false',
                                        'source': {
                                            'any': {
                                                'any6': {
                                                    'destination': {
                                                        'any': {
                                                            'any6': {
                                                                'action': 'deny',
                                                                'protocol': 'ip',
                                                                'informational_interval': 300,
                                                                'log': 'true',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x40c8b102'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            'acl3': {
                                'elements': 8,
                                'name_hash': '0x1b62e350'
                                'entry': {
                                    '1.0': {
                                        'controls_flows': 'false',
                                        'has_children': 'true',
                                        'is_child': 'false',
                                        'source': {
                                            'object_group': {
                                                'BGP-Peers-Out': {
                                                    'destination': {
                                                        'object_group': {
                                                            'BGP-Peers-In': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x128539ce'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.1': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xb9af5448'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '1.2': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.107': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xb70d09a2'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '1.3': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.3': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0xe95a626b'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '1.4': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.141.108': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.132.4': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0',
                                                                'acl_hash': '0x59b21cbd'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    '2.0': {
                                        'controls_flows': 'false',
                                        'has_children': 'true',
                                        'is_child': 'false',
                                        'source': {
                                            'object_group': {
                                                'BGP-Peers-In': {
                                                    'destination': {
                                                        'object_group': {
                                                            'BGP-Peers-Out': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '2',
                                                                'acl_hash': '0x99171bd1'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '2.1': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.132.3': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.141.107': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0xf3c06b2b',
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '2.2': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.132.3': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.141.108': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0xf4eeda64'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '2.3': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.132.4': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.141.107': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '0x76ca927c'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    '2.4': {
                                        'controls_flows': 'true',
                                        'has_children': 'false',
                                        'is_child': 'true',
                                        'source': {
                                            'host': {
                                                '172.16.132.4': {
                                                    'destination': {
                                                        'host': {
                                                            '172.16.141.108': {
                                                                'action': 'permit',
                                                                'protocol': 'tcp',
                                                                'log': 'false',
                                                                'hitcnt': '1',
                                                                'acl_hash': '0x0e95724d'
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
                        'alert_interval': 300,
                        'cached_acl_log_flows': {
                             'denied': 0, 
                             'deny_flow_max': 4096, 
                             'total': 0
                         }
                    }

expected_output={
  'asic': {
    '0': {
      'table': {
        'Mac Address Table': {
          'subtype': {
            'EM': {
              'dir': {
                'I': {
                  'max': '32768',
                  'used': '795',
                  'used_percent': '2.43%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '795'
                }
              }
            },
            'TCAM': {
              'dir': {
                'I': {
                  'max': '768',
                  'used': '21',
                  'used_percent': '2.73%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '21'
                }
              }
            }
          }
        },
        'L3 Multicast': {
          'subtype': {
            'EM': {
              'dir': {
                'I': {
                  'max': '32768',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'TCAM': {
              'dir': {
                'I': {
                  'max': '768',
                  'used': '6',
                  'used_percent': '0.78%',
                  'v4': '3',
                  'v6': '3',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'L2 Multicast': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '2304',
                  'used': '7',
                  'used_percent': '0.30%',
                  'v4': '3',
                  'v6': '4',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'IP Route Table': {
          'subtype': {
            'EM/LPM': {
              'dir': {
                'I': {
                  'max': '212992',
                  'used': '648',
                  'used_percent': '0.30%',
                  'v4': '647',
                  'v6': '0',
                  'mpls': '1',
                  'other': '0'
                }
              }
            },
            'TCAM': {
              'dir': {
                'I': {
                  'max': '1536',
                  'used': '11',
                  'used_percent': '0.72%',
                  'v4': '6',
                  'v6': '3',
                  'mpls': '2',
                  'other': '0'
                }
              }
            }
          }
        },
        'QOS ACL Ipv4': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '5632',
                  'used': '15',
                  'used_percent': '0.27%',
                  'v4': '15',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                },
                'O': {
                  'max': '6144',
                  'used': '13',
                  'used_percent': '0.21%',
                  'v4': '13',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'QOS ACL Non Ipv4': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '2560',
                  'used': '30',
                  'used_percent': '1.17%',
                  'v4': '0',
                  'v6': '20',
                  'mpls': '0',
                  'other': '10'
                },
                'O': {
                  'max': '2048',
                  'used': '27',
                  'used_percent': '1.32%',
                  'v4': '0',
                  'v6': '18',
                  'mpls': '0',
                  'other': '9'
                }
              }
            }
          }
        },
        'Security ACL Ipv4': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '7168',
                  'used': '12',
                  'used_percent': '0.17%',
                  'v4': '12',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                },
                'O': {
                  'max': '7168',
                  'used': '14',
                  'used_percent': '0.20%',
                  'v4': '14',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Security ACL Non Ipv4': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '5120',
                  'used': '76',
                  'used_percent': '1.48%',
                  'v4': '0',
                  'v6': '36',
                  'mpls': '0',
                  'other': '40'
                },
                'O': {
                  'max': '8192',
                  'used': '29',
                  'used_percent': '0.35%',
                  'v4': '0',
                  'v6': '24',
                  'mpls': '0',
                  'other': '5'
                }
              }
            }
          }
        },
        'Netflow ACL': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '512',
                  'used': '6',
                  'used_percent': '1.17%',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                },
                'O': {
                  'max': '512',
                  'used': '6',
                  'used_percent': '1.17%',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                }
              }
            }
          }
        },
        'PBR ACL': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '3072',
                  'used': '22',
                  'used_percent': '0.72%',
                  'v4': '16',
                  'v6': '6',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Flow SPAN ACL': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '512',
                  'used': '4',
                  'used_percent': '0.78%',
                  'v4': '1',
                  'v6': '2',
                  'mpls': '0',
                  'other': '1'
                },
                'O': {
                  'max': '512',
                  'used': '4',
                  'used_percent': '0.78%',
                  'v4': '1',
                  'v6': '2',
                  'mpls': '0',
                  'other': '1'
                }
              }
            }
          }
        },
        'Control Plane': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '512',
                  'used': '260',
                  'used_percent': '50.78%',
                  'v4': '110',
                  'v6': '106',
                  'mpls': '0',
                  'other': '44'
                }
              }
            }
          }
        },
        'Tunnel Termination': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '2816',
                  'used': '27',
                  'used_percent': '0.96%',
                  'v4': '11',
                  'v6': '16',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Lisp Inst Mapping': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '2048',
                  'used': '1',
                  'used_percent': '0.05%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            }
          }
        },
        'Security Association': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '512',
                  'used': '4',
                  'used_percent': '0.78%',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'CTS Cell Matrix/VPN Label': {
          'subtype': {
            'EM': {
              'dir': {
                'O': {
                  'max': '32768',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'TCAM': {
              'dir': {
                'O': {
                  'max': '768',
                  'used': '1',
                  'used_percent': '0.13%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            }
          }
        },
        'Client Table': {
          'subtype': {
            'EM': {
              'dir': {
                'I': {
                  'max': '8192',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'TCAM': {
              'dir': {
                'I': {
                  'max': '512',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Input Group LE': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '1024',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Output Group LE': {
          'subtype': {
            'TCAM': {
              'dir': {
                'O': {
                  'max': '1024',
                  'used': '0',
                  'used_percent': '0.00%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            }
          }
        },
        'Macsec SPD': {
          'subtype': {
            'TCAM': {
              'dir': {
                'I': {
                  'max': '256',
                  'used': '2',
                  'used_percent': '0.78%',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '2'
                }
              }
            }
          }
        }
      }
    }
  }
}

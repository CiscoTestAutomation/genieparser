expected_output = {
  'zp_name': {
    'ZP_lanZone_lanZone_Is_-902685811': {
      'src-zone-name': 'lanZone',
      'dst-zone-name': 'lanZone',
      'policy-name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect',
          'pkts-counter': 3500756201,
          'bytes-counter': 2474964323709,
          'attempted-conn': 17942922,
          'current-active-conn': 0,
          'max-active-conn': 818,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 178,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 13568,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'proto_entry': {
            '1': {
              'protocol-name': 'tcp',
              'byte-counters': 1063161213,
              'pkt-counters': 3500756201
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'class-default': {
          'zonepair-name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class-action': 'Inspect Pass',
          'pkts-counter': 1991519754,
          'bytes-counter': 845205210769,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'l7-policy-name': 'NONE'
        }
      }
    },
    'ZP_lanZone_wanZone_I_-1639760094': {
      'src-zone-name': 'lanZone',
      'dst-zone-name': 'wanZone',
      'policy-name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect',
          'pkts-counter': 11613822,
          'bytes-counter': 11980287348,
          'attempted-conn': 62347,
          'current-active-conn': 65,
          'max-active-conn': 181,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 19,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 16,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'proto_entry': {
            '1': {
              'protocol-name': 'tcp',
              'byte-counters': 3390354167,
              'pkt-counters': 11613838
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'class-default': {
          'zonepair-name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class-action': 'Inspect Pass',
          'pkts-counter': 79392,
          'bytes-counter': 12475089,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'l7-policy-name': 'NONE'
        }
      }
    },
    'ZP_wanZone_lanZone_I_-1538991582': {
      'src-zone-name': 'wanZone',
      'dst-zone-name': 'lanZone',
      'policy-name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect',
          'pkts-counter': 0,
          'bytes-counter': 0,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match-type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match-type': 'access-group name'
            }
          },
          'l7-policy-name': 'NONE'
        },
        'class-default': {
          'zonepair-name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class-action': 'Inspect Pass',
          'pkts-counter': 50660,
          'bytes-counter': 7353043,
          'attempted-conn': 0,
          'current-active-conn': 0,
          'max-active-conn': 0,
          'current-halfopen-conn': 0,
          'max-halfopen-conn': 0,
          'current-terminating-conn': 0,
          'max-terminating-conn': 0,
          'time-since-last-session-create': 0,
          'l7-policy-name': 'NONE'
        }
      }
    }
  }
}
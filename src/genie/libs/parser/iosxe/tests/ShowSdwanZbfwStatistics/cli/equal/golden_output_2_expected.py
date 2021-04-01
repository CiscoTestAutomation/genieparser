expected_output = {
  'zonepair_name': {
    'ZP_lanZone_lanZone_Is_-902685811': {
      'src_zone_name': 'lanZone',
      'dst_zone_name': 'lanZone',
      'policy_name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect',
          'pkts_counter': 3500756201,
          'bytes_counter': 2474964323709,
          'attempted_conn': 17942922,
          'current_active_conn': 0,
          'max_active_conn': 818,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 178,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 13568,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'proto_entry': {
            1: {
              'protocol_name': 'tcp',
              'byte_counters': 1063161213,
              'pkt_counters': 3500756201
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'class-default': {
          'zonepair_name': 'ZP_lanZone_lanZone_Is_-902685811',
          'class_action': 'Inspect Pass',
          'pkts_counter': 1991519754,
          'bytes_counter': 845205210769,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'l7_policy_name': 'NONE'
        }
      }
    },
    'ZP_lanZone_wanZone_I_-1639760094': {
      'src_zone_name': 'lanZone',
      'dst_zone_name': 'wanZone',
      'policy_name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect',
          'pkts_counter': 11613822,
          'bytes_counter': 11980287348,
          'attempted_conn': 62347,
          'current_active_conn': 65,
          'max_active_conn': 181,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 19,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 16,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'proto_entry': {
            1: {
              'protocol_name': 'tcp',
              'byte_counters': 3390354167,
              'pkt_counters': 11613838
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'class-default': {
          'zonepair_name': 'ZP_lanZone_wanZone_I_-1639760094',
          'class_action': 'Inspect Pass',
          'pkts_counter': 79392,
          'bytes_counter': 12475089,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'l7_policy_name': 'NONE'
        }
      }
    },
    'ZP_wanZone_lanZone_I_-1538991582': {
      'src_zone_name': 'wanZone',
      'dst_zone_name': 'lanZone',
      'policy_name': 'Isn4451ZbfPolicy',
      'class_entry': {
        'Isn4451ZbfPolicy-seq-1-cm_': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf1-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf1-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-11-cm_': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svr2-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vr2-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-21-cm_': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf3-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf3-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-31-cm_': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf4-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf4-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'Isn4451ZbfPolicy-seq-41-cm_': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect',
          'pkts_counter': 0,
          'bytes_counter': 0,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'match_entry': {
            'Isn4451ZbfPolicy-svrf5-l4-cm_': {
              'seq_num': 11,
              'match_crit': 'match-any',
              'match_type': 'class-map'
            },
            'Isn4451ZbfPolicy-seq-vrf5-acl_': {
              'seq_num': 3,
              'match_type': 'access-group name'
            }
          },
          'l7_policy_name': 'NONE'
        },
        'class-default': {
          'zonepair_name': 'ZP_wanZone_lanZone_I_-1538991582',
          'class_action': 'Inspect Pass',
          'pkts_counter': 50660,
          'bytes_counter': 7353043,
          'attempted_conn': 0,
          'current_active_conn': 0,
          'max_active_conn': 0,
          'current_halfopen_conn': 0,
          'max_halfopen_conn': 0,
          'current_terminating_conn': 0,
          'max_terminating_conn': 0,
          'time_since_last_session_create': 0,
          'l7_policy_name': 'NONE'
        }
      }
    }
  }
}
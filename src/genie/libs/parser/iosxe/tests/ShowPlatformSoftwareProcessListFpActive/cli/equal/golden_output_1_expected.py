expected_output = {
    "processes": {
        "systemd": {
            "pids": {
                1: {
                    "ppid": 0,
                    "group_id": 1,
                    "status": "S",
                    "priority": "20",
                    "size": 13844,
                }
            }
        },
        "kthreadd": {
            "pids": {
                2: {
                    "ppid": 0,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "rcu_gp": {
            "pids": {
                3: {"ppid": 2, "group_id": 0, "status": "I", "priority": "0", "size": 0}
            }
        },
        "rcu_par_gp": {
            "pids": {
                4: {"ppid": 2, "group_id": 0, "status": "I", "priority": "0", "size": 0}
            }
        },
        "slub_flushwq": {
            "pids": {
                5: {"ppid": 2, "group_id": 0, "status": "I", "priority": "0", "size": 0}
            }
        },
        "netns": {
            "pids": {
                6: {"ppid": 2, "group_id": 0, "status": "I", "priority": "0", "size": 0}
            }
        },
        "kworker/0:0H-events_": {
            "pids": {
                8: {"ppid": 2, "group_id": 0, "status": "I", "priority": "0", "size": 0}
            }
        },
        "mm_percpu_wq": {
            "pids": {
                10: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "rcu_tasks_rude_kthre": {
            "pids": {
                11: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "rcu_tasks_trace_kthr": {
            "pids": {
                12: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/0": {
            "pids": {
                13: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "rcu_sched": {
            "pids": {
                14: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/0": {
            "pids": {
                15: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "cpuhp/0": {
            "pids": {
                16: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "cpuhp/1": {
            "pids": {
                17: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/1": {
            "pids": {
                18: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/1": {
            "pids": {
                19: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/1:0H-events_": {
            "pids": {
                21: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/2": {
            "pids": {
                22: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/2": {
            "pids": {
                23: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/2": {
            "pids": {
                24: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/2:0H-events_": {
            "pids": {
                26: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/3": {
            "pids": {
                27: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/3": {
            "pids": {
                28: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/3": {
            "pids": {
                29: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/3:0H-events_": {
            "pids": {
                31: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/4": {
            "pids": {
                32: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/4": {
            "pids": {
                33: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/4": {
            "pids": {
                34: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/4:0H-events_": {
            "pids": {
                36: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/5": {
            "pids": {
                37: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/5": {
            "pids": {
                38: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/5": {
            "pids": {
                39: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/5:0H-events_": {
            "pids": {
                41: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/6": {
            "pids": {
                42: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/6": {
            "pids": {
                43: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/6": {
            "pids": {
                44: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/6:0H-events_": {
            "pids": {
                46: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/7": {
            "pids": {
                47: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/7": {
            "pids": {
                48: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/7": {
            "pids": {
                49: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/7:0H-events_": {
            "pids": {
                51: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/8": {
            "pids": {
                52: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/8": {
            "pids": {
                53: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/8": {
            "pids": {
                54: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/8:0H-events_": {
            "pids": {
                56: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/9": {
            "pids": {
                57: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/9": {
            "pids": {
                58: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/9": {
            "pids": {
                59: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/9:0H-events_": {
            "pids": {
                61: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/10": {
            "pids": {
                62: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/10": {
            "pids": {
                63: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/10": {
            "pids": {
                64: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/10:0-rcu_gp": {
            "pids": {
                65: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/10:0H-events": {
            "pids": {
                66: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/11": {
            "pids": {
                67: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/11": {
            "pids": {
                68: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/11": {
            "pids": {
                69: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/11:0H-events": {
            "pids": {
                71: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/12": {
            "pids": {
                72: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/12": {
            "pids": {
                73: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/12": {
            "pids": {
                74: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/12:0H-events": {
            "pids": {
                76: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/13": {
            "pids": {
                77: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/13": {
            "pids": {
                78: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/13": {
            "pids": {
                79: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/13:0H-events": {
            "pids": {
                81: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/14": {
            "pids": {
                82: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/14": {
            "pids": {
                83: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/14": {
            "pids": {
                84: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/14:0H-events": {
            "pids": {
                86: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cpuhp/15": {
            "pids": {
                87: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "migration/15": {
            "pids": {
                88: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "4294967196",
                    "size": 0,
                }
            }
        },
        "ksoftirqd/15": {
            "pids": {
                89: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "T",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/15:0H-events": {
            "pids": {
                91: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdevtmpfs": {
            "pids": {
                92: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "inet_frag_wq": {
            "pids": {
                93: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kauditd": {
            "pids": {
                94: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/1:1-mm_percp": {
            "pids": {
                96: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "khungtaskd": {
            "pids": {
                97: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "oom_reaper": {
            "pids": {
                98: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "writeback": {
            "pids": {
                100: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kcompactd0": {
            "pids": {
                102: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "ksmd": {
            "pids": {
                103: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "25",
                    "size": 0,
                }
            }
        },
        "kblockd": {
            "pids": {
                104: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "blkcg_punt_bio": {
            "pids": {
                105: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "tpm_dev_wq": {
            "pids": {
                106: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "md": {
            "pids": {
                107: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "edac-poller": {
            "pids": {
                108: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "watchdogd": {
            "pids": {
                109: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "rpciod": {
            "pids": {
                110: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/2:1-mm_percp": {
            "pids": {
                111: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/2:1H-kblockd": {
            "pids": {
                112: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "xprtiod": {
            "pids": {
                113: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/12:1-rcu_gp": {
            "pids": {
                114: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kswapd0": {
            "pids": {
                116: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "nfsiod": {
            "pids": {
                117: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kthrotld": {
            "pids": {
                118: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "irq/25-aerdrv": {
            "pids": {
                120: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/27-aerdrv": {
            "pids": {
                121: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/28-aerdrv": {
            "pids": {
                122: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/29-aerdrv": {
            "pids": {
                123: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/31-aerdrv": {
            "pids": {
                124: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/32-aerdrv": {
            "pids": {
                125: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/32-pciehp": {
            "pids": {
                126: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/33-aerdrv": {
            "pids": {
                127: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/33-pciehp": {
            "pids": {
                128: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/34-aerdrv": {
            "pids": {
                129: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/34-pciehp": {
            "pids": {
                130: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/35-pciehp": {
            "pids": {
                131: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/36-pciehp": {
            "pids": {
                132: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "irq/37-pciehp": {
            "pids": {
                133: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "4294967245",
                    "size": 0,
                }
            }
        },
        "kworker/3:1-mm_percp": {
            "pids": {
                134: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/4:1-mm_percp": {
            "pids": {
                135: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/5:1-events": {
            "pids": {
                136: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/6:1-mm_percp": {
            "pids": {
                137: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/7:1-mm_percp": {
            "pids": {
                138: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/9:1-events": {
            "pids": {
                140: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/11:1-mm_perc": {
            "pids": {
                141: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/13:1-rcu_gp": {
            "pids": {
                142: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/14:1-events": {
            "pids": {
                143: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/15:1-events": {
            "pids": {
                144: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "acpi_thermal_pm": {
            "pids": {
                145: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "tpm-vtpm": {
            "pids": {
                146: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/u33:0": {
            "pids": {
                147: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd0-recv": {
            "pids": {
                148: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd1-recv": {
            "pids": {
                149: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd2-recv": {
            "pids": {
                150: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd3-recv": {
            "pids": {
                151: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd4-recv": {
            "pids": {
                152: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd5-recv": {
            "pids": {
                153: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd6-recv": {
            "pids": {
                154: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd7-recv": {
            "pids": {
                155: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd8-recv": {
            "pids": {
                156: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd9-recv": {
            "pids": {
                157: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd10-recv": {
            "pids": {
                158: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd11-recv": {
            "pids": {
                159: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd12-recv": {
            "pids": {
                160: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd13-recv": {
            "pids": {
                161: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd14-recv": {
            "pids": {
                162: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nbd15-recv": {
            "pids": {
                163: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_0": {
            "pids": {
                164: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_0": {
            "pids": {
                165: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_1": {
            "pids": {
                166: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_1": {
            "pids": {
                167: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_2": {
            "pids": {
                168: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_2": {
            "pids": {
                169: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_3": {
            "pids": {
                170: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_3": {
            "pids": {
                171: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_4": {
            "pids": {
                172: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_4": {
            "pids": {
                173: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_5": {
            "pids": {
                174: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_5": {
            "pids": {
                175: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "dm_bufio_cache": {
            "pids": {
                178: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kvub300c": {
            "pids": {
                179: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kvub300p": {
            "pids": {
                180: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kvub300d": {
            "pids": {
                181: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "mld": {
            "pids": {
                182: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/12:1H-kblock": {
            "pids": {
                183: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "ipv6_addrconf": {
            "pids": {
                184: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/14:1H-kblock": {
            "pids": {
                220: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/13:1H-kblock": {
            "pids": {
                223: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "scsi_eh_6": {
            "pids": {
                227: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "scsi_tmf_6": {
            "pids": {
                228: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "usb-storage": {
            "pids": {
                229: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/15:1H-kblock": {
            "pids": {
                232: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/8:1H-kblockd": {
            "pids": {
                234: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/10:1H-kblock": {
            "pids": {
                246: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/14:2-kdmflus": {
            "pids": {
                253: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/3:1H-kblockd": {
            "pids": {
                255: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/12:2-events": {
            "pids": {
                257: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/0:1H-kblockd": {
            "pids": {
                259: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/4:1H-kblockd": {
            "pids": {
                261: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/11:1H-kblock": {
            "pids": {
                263: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/1:1H-kblockd": {
            "pids": {
                265: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/9:1H-kblockd": {
            "pids": {
                285: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/15:2-events": {
            "pids": {
                286: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/5:1H-kblockd": {
            "pids": {
                290: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/7:1H-kblockd": {
            "pids": {
                294: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/6:1H-kblockd": {
            "pids": {
                303: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kworker/11:2-rcu_gp": {
            "pids": {
                305: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/13:2-ipv6_ad": {
            "pids": {
                308: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/1:2-rcu_gp": {
            "pids": {
                342: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/5:2-events": {
            "pids": {
                370: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/3:2-rcu_gp": {
            "pids": {
                371: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/10:2-mm_perc": {
            "pids": {
                394: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/9:2-events": {
            "pids": {
                429: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/7:2-events": {
            "pids": {
                440: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/2:2-events_p": {
            "pids": {
                463: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/6:2-inet_fra": {
            "pids": {
                471: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "bnxt_pf_wq": {
            "pids": {
                488: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "i40e": {
            "pids": {
                512: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "ixgbe": {
            "pids": {
                514: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:0": {
            "pids": {
                650: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kverityd": {
            "pids": {
                651: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                656: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                660: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                664: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                668: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                672: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                676: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                680: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                684: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                688: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                692: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                696: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                700: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                704: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                708: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                712: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                716: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
            }
        },
        "kdmflush/253:1": {
            "pids": {
                655: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:2": {
            "pids": {
                659: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:3": {
            "pids": {
                663: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:4": {
            "pids": {
                667: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:5": {
            "pids": {
                671: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:6": {
            "pids": {
                675: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:7": {
            "pids": {
                679: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:8": {
            "pids": {
                683: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:9": {
            "pids": {
                687: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:10": {
            "pids": {
                691: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:11": {
            "pids": {
                695: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:12": {
            "pids": {
                699: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:13": {
            "pids": {
                703: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:14": {
            "pids": {
                707: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:15": {
            "pids": {
                711: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "kdmflush/253:16": {
            "pids": {
                715: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "pman": {
            "pids": {
                778: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2732,
                },
                908: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2808,
                },
                2344: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                3096: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                3368: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2760,
                },
                3613: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2824,
                },
                3743: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                3863: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                3994: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2760,
                },
                4125: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                4441: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                4788: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2764,
                },
                5045: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                5111: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                5324: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                5436: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                5578: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                5725: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                5766: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                5912: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                6031: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2764,
                },
                6149: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                6283: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                6404: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                6528: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2764,
                },
                6532: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                6660: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                10489: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2776,
                },
                11351: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                11472: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2764,
                },
                11605: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2764,
                },
                11726: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                11852: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                12352: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2768,
                },
                14411: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 3592,
                },
                15419: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                15785: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                16294: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2740,
                },
                17549: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 3644,
                },
                17932: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 3124,
                },
                18675: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2736,
                },
                18888: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                19869: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2772,
                },
                20129: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                20400: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                20757: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                21075: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2756,
                },
                21273: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                21508: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2752,
                },
                21568: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                21674: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                21782: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                21978: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2744,
                },
                22086: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                22198: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                22307: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                22413: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                22533: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                23265: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2744,
                },
                23857: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2744,
                },
                23877: {
                    "ppid": 23101,
                    "group_id": 23100,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                24469: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                24491: {
                    "ppid": 23101,
                    "group_id": 23100,
                    "status": "S",
                    "priority": "20",
                    "size": 2740,
                },
                25032: {
                    "ppid": 23101,
                    "group_id": 23100,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                25660: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                25933: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                26219: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                26939: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2760,
                },
                32256: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2748,
                },
                32383: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 2808,
                },
            }
        },
        "systemd-journal": {
            "pids": {
                780: {
                    "ppid": 1,
                    "group_id": 780,
                    "status": "S",
                    "priority": "20",
                    "size": 11604,
                }
            }
        },
        "autodns.py": {
            "pids": {
                787: {
                    "ppid": 778,
                    "group_id": 787,
                    "status": "S",
                    "priority": "20",
                    "size": 9136,
                }
            }
        },
        "auditd": {
            "pids": {
                838: {
                    "ppid": 1,
                    "group_id": 838,
                    "status": "S",
                    "priority": "16",
                    "size": 2824,
                }
            }
        },
        "kworker/u32:4-loop20": {
            "pids": {
                842: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "audisp-syslog": {
            "pids": {
                852: {
                    "ppid": 838,
                    "group_id": 838,
                    "status": "S",
                    "priority": "16",
                    "size": 460,
                }
            }
        },
        "rpc.idmapd": {
            "pids": {
                855: {
                    "ppid": 1,
                    "group_id": 855,
                    "status": "S",
                    "priority": "20",
                    "size": 2252,
                }
            }
        },
        "lsmpi-refill": {
            "pids": {
                878: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "15",
                    "size": 0,
                }
            }
        },
        "lsmpi-xmit": {
            "pids": {
                879: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "15",
                    "size": 0,
                }
            }
        },
        "lsmpi-rx": {
            "pids": {
                880: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "15",
                    "size": 0,
                }
            }
        },
        "nfsdcld": {
            "pids": {
                897: {
                    "ppid": 1,
                    "group_id": 897,
                    "status": "S",
                    "priority": "20",
                    "size": 3044,
                }
            }
        },
        "systemd-udevd": {
            "pids": {
                907: {
                    "ppid": 1,
                    "group_id": 907,
                    "status": "S",
                    "priority": "20",
                    "size": 9644,
                }
            }
        },
        "run_ioxn_caf.sh": {
            "pids": {
                914: {
                    "ppid": 908,
                    "group_id": 914,
                    "status": "S",
                    "priority": "20",
                    "size": 7640,
                },
                2378: {
                    "ppid": 2377,
                    "group_id": 914,
                    "status": "S",
                    "priority": "20",
                    "size": 6456,
                },
            }
        },
        "qat_device_rese": {
            "pids": {
                1031: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "qat_fatal_error": {
            "pids": {
                1032: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nvme-wq": {
            "pids": {
                1212: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nvme-reset-wq": {
            "pids": {
                1213: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "nvme-delete-wq": {
            "pids": {
                1214: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "cron": {
            "pids": {
                2165: {
                    "ppid": 4690,
                    "group_id": 2165,
                    "status": "S",
                    "priority": "27",
                    "size": 764,
                }
            }
        },
        "ioxman": {
            "pids": {
                2350: {
                    "ppid": 2344,
                    "group_id": 2350,
                    "status": "S",
                    "priority": "20",
                    "size": 30148,
                }
            }
        },
        "python3": {
            "pids": {
                2377: {
                    "ppid": 914,
                    "group_id": 914,
                    "status": "S",
                    "priority": "20",
                    "size": 58764,
                }
            }
        },
        "sed": {
            "pids": {
                2379: {
                    "ppid": 2378,
                    "group_id": 914,
                    "status": "S",
                    "priority": "20",
                    "size": 768,
                }
            }
        },
        "logger": {
            "pids": {
                2380: {
                    "ppid": 2378,
                    "group_id": 914,
                    "status": "S",
                    "priority": "20",
                    "size": 724,
                }
            }
        },
        "kworker/4:2-rcu_gp": {
            "pids": {
                2550: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/u32:10-kveri": {
            "pids": {
                2670: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "jbd2/loop18-8": {
            "pids": {
                2728: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "ext4-rsv-conver": {
            "pids": {
                2729: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                2767: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                3890: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
                6690: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                },
            }
        },
        "psvp.sh": {
            "pids": {
                2745: {
                    "ppid": 1,
                    "group_id": 2744,
                    "status": "S",
                    "priority": "20",
                    "size": 13088,
                }
            }
        },
        "jbd2/loop19-8": {
            "pids": {
                2766: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "rotee": {
            "pids": {
                2811: {
                    "ppid": 1,
                    "group_id": 2810,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
                2875: {
                    "ppid": 1,
                    "group_id": 2874,
                    "status": "S",
                    "priority": "20",
                    "size": 2388,
                },
                4939: {
                    "ppid": 1,
                    "group_id": 4938,
                    "status": "S",
                    "priority": "20",
                    "size": 2248,
                },
                6907: {
                    "ppid": 1,
                    "group_id": 6906,
                    "status": "S",
                    "priority": "20",
                    "size": 2432,
                },
                7161: {
                    "ppid": 1,
                    "group_id": 7160,
                    "status": "S",
                    "priority": "20",
                    "size": 2380,
                },
                7363: {
                    "ppid": 1,
                    "group_id": 7362,
                    "status": "S",
                    "priority": "20",
                    "size": 2252,
                },
                7560: {
                    "ppid": 1,
                    "group_id": 7559,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
                13245: {
                    "ppid": 1,
                    "group_id": 13243,
                    "status": "S",
                    "priority": "20",
                    "size": 2256,
                },
                13267: {
                    "ppid": 1,
                    "group_id": 13266,
                    "status": "S",
                    "priority": "20",
                    "size": 2256,
                },
                13286: {
                    "ppid": 1,
                    "group_id": 13285,
                    "status": "S",
                    "priority": "20",
                    "size": 2256,
                },
                13332: {
                    "ppid": 1,
                    "group_id": 13331,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
                21261: {
                    "ppid": 1,
                    "group_id": 21260,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
                22802: {
                    "ppid": 1,
                    "group_id": 22801,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
                23199: {
                    "ppid": 1,
                    "group_id": 23198,
                    "status": "S",
                    "priority": "20",
                    "size": 2260,
                },
            }
        },
        "inotifywait": {
            "pids": {
                2816: {
                    "ppid": 2745,
                    "group_id": 2744,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                },
                6927: {
                    "ppid": 4729,
                    "group_id": 4729,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                7221: {
                    "ppid": 7025,
                    "group_id": 7025,
                    "status": "S",
                    "priority": "20",
                    "size": 828,
                },
                7519: {
                    "ppid": 7231,
                    "group_id": 7231,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                },
                13361: {
                    "ppid": 12992,
                    "group_id": 12992,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                13371: {
                    "ppid": 12939,
                    "group_id": 13371,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                },
                13378: {
                    "ppid": 12996,
                    "group_id": 12996,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                13389: {
                    "ppid": 12991,
                    "group_id": 12991,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                13417: {
                    "ppid": 2821,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                21423: {
                    "ppid": 21105,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 740,
                },
                22857: {
                    "ppid": 22742,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                },
                23366: {
                    "ppid": 23101,
                    "group_id": 23100,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                },
                27151: {
                    "ppid": 26960,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 748,
                },
                27155: {
                    "ppid": 26960,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 744,
                },
            }
        },
        "pvp.sh": {
            "pids": {
                2821: {
                    "ppid": 1,
                    "group_id": 2820,
                    "status": "S",
                    "priority": "20",
                    "size": 9840,
                },
                21105: {
                    "ppid": 1,
                    "group_id": 21104,
                    "status": "S",
                    "priority": "20",
                    "size": 8712,
                },
                22742: {
                    "ppid": 1,
                    "group_id": 22741,
                    "status": "S",
                    "priority": "20",
                    "size": 8708,
                },
                23101: {
                    "ppid": 1,
                    "group_id": 23100,
                    "status": "S",
                    "priority": "20",
                    "size": 8700,
                },
            }
        },
        "libvirt_lxc": {
            "pids": {
                2995: {
                    "ppid": 1,
                    "group_id": 2994,
                    "status": "S",
                    "priority": "20",
                    "size": 9256,
                },
                4688: {
                    "ppid": 1,
                    "group_id": 4687,
                    "status": "S",
                    "priority": "20",
                    "size": 9224,
                },
            }
        },
        "sysmgr": {
            "pids": {
                2997: {
                    "ppid": 2995,
                    "group_id": 2994,
                    "status": "S",
                    "priority": "20",
                    "size": 224,
                }
            }
        },
        "so_dre": {
            "pids": {
                3031: {
                    "ppid": 2997,
                    "group_id": 2994,
                    "status": "S",
                    "priority": "20",
                    "size": 571040,
                }
            }
        },
        "psd": {
            "pids": {
                3290: {
                    "ppid": 3096,
                    "group_id": 3290,
                    "status": "S",
                    "priority": "20",
                    "size": 28184,
                }
            }
        },
        "linux_iosd-imag": {
            "pids": {
                3526: {
                    "ppid": 3368,
                    "group_id": 3526,
                    "status": "S",
                    "priority": "20",
                    "size": 794408,
                }
            }
        },
        "vman": {
            "pids": {
                3656: {
                    "ppid": 3613,
                    "group_id": 3656,
                    "status": "S",
                    "priority": "20",
                    "size": 25412,
                }
            }
        },
        "sessmgrd": {
            "pids": {
                3750: {
                    "ppid": 3743,
                    "group_id": 3750,
                    "status": "S",
                    "priority": "20",
                    "size": 69840,
                }
            }
        },
        "smand": {
            "pids": {
                3874: {
                    "ppid": 3863,
                    "group_id": 3874,
                    "status": "S",
                    "priority": "20",
                    "size": 85204,
                }
            }
        },
        "jbd2/loop20-8": {
            "pids": {
                3889: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "repm": {
            "pids": {
                4027: {
                    "ppid": 3994,
                    "group_id": 4027,
                    "status": "S",
                    "priority": "20",
                    "size": 20736,
                }
            }
        },
        "plogd": {
            "pids": {
                4183: {
                    "ppid": 4125,
                    "group_id": 4183,
                    "status": "S",
                    "priority": "20",
                    "size": 9740,
                }
            }
        },
        "keyman": {
            "pids": {
                4449: {
                    "ppid": 4441,
                    "group_id": 4449,
                    "status": "S",
                    "priority": "20",
                    "size": 13396,
                }
            }
        },
        "SarIosdMond": {
            "pids": {
                4546: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "sleep": {
            "pids": {
                4683: {
                    "ppid": 16316,
                    "group_id": 16316,
                    "status": "S",
                    "priority": "20",
                    "size": 464,
                },
                4944: {
                    "ppid": 4740,
                    "group_id": 4740,
                    "status": "S",
                    "priority": "20",
                    "size": 460,
                },
                5007: {
                    "ppid": 26789,
                    "group_id": 26788,
                    "status": "S",
                    "priority": "20",
                    "size": 460,
                },
                5014: {
                    "ppid": 5346,
                    "group_id": 5346,
                    "status": "S",
                    "priority": "20",
                    "size": 464,
                },
                5110: {
                    "ppid": 17942,
                    "group_id": 17942,
                    "status": "S",
                    "priority": "20",
                    "size": 464,
                },
                5154: {
                    "ppid": 17593,
                    "group_id": 17593,
                    "status": "S",
                    "priority": "20",
                    "size": 468,
                },
                5604: {
                    "ppid": 14428,
                    "group_id": 14428,
                    "status": "S",
                    "priority": "20",
                    "size": 464,
                },
                15782: {
                    "ppid": 7000,
                    "group_id": 6549,
                    "status": "S",
                    "priority": "20",
                    "size": 460,
                },
                31761: {
                    "ppid": 12002,
                    "group_id": 12002,
                    "status": "S",
                    "priority": "20",
                    "size": 460,
                },
            }
        },
        "init": {
            "pids": {
                4690: {
                    "ppid": 4688,
                    "group_id": 4690,
                    "status": "S",
                    "priority": "20",
                    "size": 896,
                }
            }
        },
        "agetty": {
            "pids": {
                4728: {
                    "ppid": 4690,
                    "group_id": 4728,
                    "status": "S",
                    "priority": "20",
                    "size": 868,
                },
                4730: {
                    "ppid": 4690,
                    "group_id": 4730,
                    "status": "S",
                    "priority": "20",
                    "size": 872,
                },
            }
        },
        "droputil.sh": {
            "pids": {
                4729: {
                    "ppid": 1,
                    "group_id": 4729,
                    "status": "S",
                    "priority": "20",
                    "size": 9336,
                }
            }
        },
        "oom.sh": {
            "pids": {
                4740: {
                    "ppid": 1,
                    "group_id": 4740,
                    "status": "S",
                    "priority": "20",
                    "size": 3036,
                }
            }
        },
        "ds": {
            "pids": {
                4766: {
                    "ppid": 4690,
                    "group_id": 4766,
                    "status": "S",
                    "priority": "20",
                    "size": 2108,
                }
            }
        },
        "nodemgr": {
            "pids": {
                4767: {
                    "ppid": 4690,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "20",
                    "size": 1584,
                }
            }
        },
        "libvirtd": {
            "pids": {
                4785: {
                    "ppid": 1,
                    "group_id": 4736,
                    "status": "S",
                    "priority": "20",
                    "size": 19184,
                }
            }
        },
        "hman": {
            "pids": {
                4795: {
                    "ppid": 4788,
                    "group_id": 4795,
                    "status": "S",
                    "priority": "20",
                    "size": 23624,
                },
                21576: {
                    "ppid": 21568,
                    "group_id": 21576,
                    "status": "R",
                    "priority": "20",
                    "size": 17544,
                },
                23284: {
                    "ppid": 23265,
                    "group_id": 23284,
                    "status": "S",
                    "priority": "20",
                    "size": 16836,
                },
                24028: {
                    "ppid": 23877,
                    "group_id": 24028,
                    "status": "S",
                    "priority": "20",
                    "size": 16828,
                },
            }
        },
        "sntp": {
            "pids": {
                4887: {
                    "ppid": 1,
                    "group_id": 4887,
                    "status": "S",
                    "priority": "20",
                    "size": 736,
                }
            }
        },
        "rpcbind": {
            "pids": {
                4889: {
                    "ppid": 1,
                    "group_id": 4889,
                    "status": "S",
                    "priority": "20",
                    "size": 684,
                }
            }
        },
        "virtlogd": {
            "pids": {
                4905: {
                    "ppid": 1,
                    "group_id": 4905,
                    "status": "S",
                    "priority": "20",
                    "size": 6352,
                }
            }
        },
        "xinetd": {
            "pids": {
                4949: {
                    "ppid": 1,
                    "group_id": 4949,
                    "status": "S",
                    "priority": "20",
                    "size": 908,
                },
                11829: {
                    "ppid": 1,
                    "group_id": 11829,
                    "status": "S",
                    "priority": "20",
                    "size": 1184,
                },
                11831: {
                    "ppid": 1,
                    "group_id": 11831,
                    "status": "S",
                    "priority": "20",
                    "size": 936,
                },
                12940: {
                    "ppid": 1,
                    "group_id": 12940,
                    "status": "S",
                    "priority": "20",
                    "size": 1140,
                },
                12941: {
                    "ppid": 1,
                    "group_id": 12941,
                    "status": "S",
                    "priority": "20",
                    "size": 1132,
                },
            }
        },
        "rpc.mountd": {
            "pids": {
                4996: {
                    "ppid": 1,
                    "group_id": 4996,
                    "status": "S",
                    "priority": "20",
                    "size": 1328,
                }
            }
        },
        "lockd": {
            "pids": {
                5032: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "nfsd": {
            "pids": {
                5033: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5034: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5035: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5036: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5037: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5038: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5039: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
                5040: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                },
            }
        },
        "rpc.statd": {
            "pids": {
                5043: {
                    "ppid": 1,
                    "group_id": 5043,
                    "status": "S",
                    "priority": "20",
                    "size": 580,
                }
            }
        },
        "htx": {
            "pids": {
                5052: {
                    "ppid": 5045,
                    "group_id": 5052,
                    "status": "S",
                    "priority": "20",
                    "size": 1145796,
                }
            }
        },
        "fman_rp": {
            "pids": {
                5222: {
                    "ppid": 5111,
                    "group_id": 5222,
                    "status": "S",
                    "priority": "20",
                    "size": 91976,
                }
            }
        },
        "iox_restart.sh": {
            "pids": {
                5346: {
                    "ppid": 5324,
                    "group_id": 5346,
                    "status": "S",
                    "priority": "20",
                    "size": 2468,
                }
            }
        },
        "climgr": {
            "pids": {
                5427: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 55488,
                }
            }
        },
        "dbm": {
            "pids": {
                5443: {
                    "ppid": 5436,
                    "group_id": 5443,
                    "status": "S",
                    "priority": "20",
                    "size": 102224,
                }
            }
        },
        "sshd": {
            "pids": {
                5524: {
                    "ppid": 1,
                    "group_id": 5524,
                    "status": "S",
                    "priority": "20",
                    "size": 1108,
                }
            }
        },
        "cmand": {
            "pids": {
                5599: {
                    "ppid": 5578,
                    "group_id": 5599,
                    "status": "S",
                    "priority": "20",
                    "size": 60452,
                }
            }
        },
        "sort_files_by_i": {
            "pids": {
                5638: {
                    "ppid": 18686,
                    "group_id": 18686,
                    "status": "S",
                    "priority": "20",
                    "size": 848,
                },
                18686: {
                    "ppid": 18675,
                    "group_id": 18686,
                    "status": "S",
                    "priority": "20",
                    "size": 1696,
                },
            }
        },
        "cli_agent": {
            "pids": {
                5751: {
                    "ppid": 5725,
                    "group_id": 5751,
                    "status": "S",
                    "priority": "20",
                    "size": 33968,
                }
            }
        },
        "ngiolite": {
            "pids": {
                5780: {
                    "ppid": 5766,
                    "group_id": 5780,
                    "status": "S",
                    "priority": "20",
                    "size": 14316,
                },
                6039: {
                    "ppid": 6031,
                    "group_id": 6039,
                    "status": "S",
                    "priority": "20",
                    "size": 38924,
                },
                6549: {
                    "ppid": 6528,
                    "group_id": 6549,
                    "status": "S",
                    "priority": "20",
                    "size": 13988,
                },
            }
        },
        "cck_qat": {
            "pids": {
                5956: {
                    "ppid": 5912,
                    "group_id": 5956,
                    "status": "S",
                    "priority": "20",
                    "size": 12440,
                }
            }
        },
        "btman": {
            "pids": {
                6165: {
                    "ppid": 6149,
                    "group_id": 6165,
                    "status": "S",
                    "priority": "20",
                    "size": 39148,
                },
                22554: {
                    "ppid": 22533,
                    "group_id": 22554,
                    "status": "S",
                    "priority": "20",
                    "size": 19460,
                },
                24555: {
                    "ppid": 24469,
                    "group_id": 24555,
                    "status": "S",
                    "priority": "20",
                    "size": 19744,
                },
                25045: {
                    "ppid": 25032,
                    "group_id": 25045,
                    "status": "S",
                    "priority": "20",
                    "size": 17020,
                },
            }
        },
        "tams_proc": {
            "pids": {
                6293: {
                    "ppid": 6283,
                    "group_id": 6293,
                    "status": "S",
                    "priority": "20",
                    "size": 8424,
                }
            }
        },
        "kdmflush/253:17": {
            "pids": {
                6363: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "0",
                    "size": 0,
                }
            }
        },
        "tamd_proc": {
            "pids": {
                6418: {
                    "ppid": 6404,
                    "group_id": 6418,
                    "status": "S",
                    "priority": "20",
                    "size": 8748,
                }
            }
        },
        "tam_svcs_esg_cf": {
            "pids": {
                6541: {
                    "ppid": 6532,
                    "group_id": 6541,
                    "status": "S",
                    "priority": "20",
                    "size": 7232,
                }
            }
        },
        "autodns": {
            "pids": {
                6666: {
                    "ppid": 6660,
                    "group_id": 6666,
                    "status": "S",
                    "priority": "20",
                    "size": 5360,
                }
            }
        },
        "jbd2/dm-17-8": {
            "pids": {
                6689: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/8:2-rcu_gp": {
            "pids": {
                6721: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "mcp_smartctl_cm": {
            "pids": {
                7000: {
                    "ppid": 1,
                    "group_id": 6549,
                    "status": "S",
                    "priority": "20",
                    "size": 1100,
                }
            }
        },
        "reflector.sh": {
            "pids": {
                7025: {
                    "ppid": 1,
                    "group_id": 7025,
                    "status": "S",
                    "priority": "20",
                    "size": 9292,
                }
            }
        },
        "iptbl.sh": {
            "pids": {
                7231: {
                    "ppid": 1,
                    "group_id": 7231,
                    "status": "S",
                    "priority": "20",
                    "size": 5872,
                }
            }
        },
        "lfts_sar_aux": {
            "pids": {
                7672: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "S",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/u32:13-kveri": {
            "pids": {
                9812: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/8:1-events": {
            "pids": {
                9852: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "nginx": {
            "pids": {
                10497: {
                    "ppid": 10489,
                    "group_id": 10497,
                    "status": "S",
                    "priority": "20",
                    "size": 14648,
                },
                10527: {
                    "ppid": 10497,
                    "group_id": 10497,
                    "status": "S",
                    "priority": "20",
                    "size": 9624,
                },
                10528: {
                    "ppid": 10497,
                    "group_id": 10497,
                    "status": "S",
                    "priority": "20",
                    "size": 7684,
                },
            }
        },
        "dhcpd": {
            "pids": {
                11248: {
                    "ppid": 1,
                    "group_id": 11248,
                    "status": "S",
                    "priority": "20",
                    "size": 5944,
                }
            }
        },
        "cxpd": {
            "pids": {
                11358: {
                    "ppid": 11351,
                    "group_id": 11358,
                    "status": "S",
                    "priority": "20",
                    "size": 25020,
                }
            }
        },
        "fpmd": {
            "pids": {
                11480: {
                    "ppid": 11472,
                    "group_id": 11480,
                    "status": "S",
                    "priority": "20",
                    "size": 31356,
                }
            }
        },
        "ftmd": {
            "pids": {
                11613: {
                    "ppid": 11605,
                    "group_id": 11613,
                    "status": "S",
                    "priority": "20",
                    "size": 122652,
                }
            }
        },
        "ompd": {
            "pids": {
                11733: {
                    "ppid": 11726,
                    "group_id": 11733,
                    "status": "S",
                    "priority": "20",
                    "size": 62716,
                }
            }
        },
        "ttmd": {
            "pids": {
                11858: {
                    "ppid": 11852,
                    "group_id": 11858,
                    "status": "S",
                    "priority": "20",
                    "size": 22208,
                }
            }
        },
        "memory_monitor.": {
            "pids": {
                12002: {
                    "ppid": 1,
                    "group_id": 12002,
                    "status": "S",
                    "priority": "20",
                    "size": 2172,
                }
            }
        },
        "dbgd": {
            "pids": {
                12396: {
                    "ppid": 12352,
                    "group_id": 12396,
                    "status": "S",
                    "priority": "20",
                    "size": 19756,
                }
            }
        },
        "kworker/u32:3-kverit": {
            "pids": {
                12497: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "auxinit.sh": {
            "pids": {
                12937: {
                    "ppid": 1,
                    "group_id": 12937,
                    "status": "S",
                    "priority": "20",
                    "size": 2020,
                }
            }
        },
        "rollback_timer.": {
            "pids": {
                12939: {
                    "ppid": 1,
                    "group_id": 12939,
                    "status": "S",
                    "priority": "20",
                    "size": 13872,
                }
            }
        },
        "kernel_ftrace.s": {
            "pids": {
                12991: {
                    "ppid": 1,
                    "group_id": 12991,
                    "status": "S",
                    "priority": "20",
                    "size": 12396,
                }
            }
        },
        "kernel_smu.sh": {
            "pids": {
                12992: {
                    "ppid": 1,
                    "group_id": 12992,
                    "status": "S",
                    "priority": "20",
                    "size": 10452,
                }
            }
        },
        "selinux_smu.sh": {
            "pids": {
                12996: {
                    "ppid": 1,
                    "group_id": 12996,
                    "status": "S",
                    "priority": "20",
                    "size": 10456,
                }
            }
        },
        "bcti": {
            "pids": {
                13541: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 15616,
                }
            }
        },
        "beakerd": {
            "pids": {
                13568: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 11144,
                }
            }
        },
        "utd_tg_client": {
            "pids": {
                13573: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 3304,
                }
            }
        },
        "stats-zipper.sh": {
            "pids": {
                14428: {
                    "ppid": 14411,
                    "group_id": 14428,
                    "status": "S",
                    "priority": "20",
                    "size": 2724,
                }
            }
        },
        "kworker/u32:9-loop17": {
            "pids": {
                14730: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "snort3": {
            "pids": {
                14816: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 814816,
                }
            }
        },
        "journalctl": {
            "pids": {
                15283: {
                    "ppid": 4183,
                    "group_id": 4183,
                    "status": "S",
                    "priority": "20",
                    "size": 5888,
                }
            }
        },
        "kworker/u32:5-kverit": {
            "pids": {
                15365: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "lman": {
            "pids": {
                15426: {
                    "ppid": 15419,
                    "group_id": 15426,
                    "status": "S",
                    "priority": "20",
                    "size": 13592,
                }
            }
        },
        "utd_logger.py": {
            "pids": {
                15652: {
                    "ppid": 4767,
                    "group_id": 4767,
                    "status": "S",
                    "priority": "27",
                    "size": 31308,
                }
            }
        },
        "install_mgr": {
            "pids": {
                15792: {
                    "ppid": 15785,
                    "group_id": 15792,
                    "status": "S",
                    "priority": "20",
                    "size": 25932,
                }
            }
        },
        "flash_check.sh": {
            "pids": {
                16316: {
                    "ppid": 16294,
                    "group_id": 16316,
                    "status": "S",
                    "priority": "20",
                    "size": 4448,
                }
            }
        },
        "cedge-tanman.sh": {
            "pids": {
                17593: {
                    "ppid": 17549,
                    "group_id": 17593,
                    "status": "S",
                    "priority": "20",
                    "size": 8112,
                }
            }
        },
        "kworker/u32:12-loop1": {
            "pids": {
                17745: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "cedge-data-stre": {
            "pids": {
                17942: {
                    "ppid": 17932,
                    "group_id": 17942,
                    "status": "S",
                    "priority": "20",
                    "size": 3240,
                }
            }
        },
        "kworker/u32:2-kverit": {
            "pids": {
                18248: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "pistisd": {
            "pids": {
                18900: {
                    "ppid": 18888,
                    "group_id": 18900,
                    "status": "S",
                    "priority": "20",
                    "size": 23500,
                }
            }
        },
        "sdavc_proxy": {
            "pids": {
                19878: {
                    "ppid": 19869,
                    "group_id": 19878,
                    "status": "S",
                    "priority": "20",
                    "size": 7384,
                }
            }
        },
        "pubd": {
            "pids": {
                20143: {
                    "ppid": 20129,
                    "group_id": 20143,
                    "status": "S",
                    "priority": "20",
                    "size": 100200,
                }
            }
        },
        "pttcd": {
            "pids": {
                20412: {
                    "ppid": 20400,
                    "group_id": 20412,
                    "status": "S",
                    "priority": "20",
                    "size": 5912,
                }
            }
        },
        "ndbmand": {
            "pids": {
                20778: {
                    "ppid": 20757,
                    "group_id": 20778,
                    "status": "S",
                    "priority": "20",
                    "size": 112740,
                }
            }
        },
        "kworker/u32:7-kverit": {
            "pids": {
                20931: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "dmiauthd": {
            "pids": {
                21086: {
                    "ppid": 21075,
                    "group_id": 21086,
                    "status": "S",
                    "priority": "20",
                    "size": 39104,
                }
            }
        },
        "ncsshd_bp": {
            "pids": {
                21280: {
                    "ppid": 21273,
                    "group_id": 21280,
                    "status": "R",
                    "priority": "20",
                    "size": 9748,
                }
            }
        },
        "ncsshd": {
            "pids": {
                21527: {
                    "ppid": 21508,
                    "group_id": 21527,
                    "status": "S",
                    "priority": "20",
                    "size": 10520,
                },
                31582: {
                    "ppid": 21527,
                    "group_id": 31582,
                    "status": "S",
                    "priority": "20",
                    "size": 10540,
                },
                31598: {
                    "ppid": 31582,
                    "group_id": 31582,
                    "status": "S",
                    "priority": "20",
                    "size": 4356,
                },
            }
        },
        "fman_fp_image": {
            "pids": {
                21707: {
                    "ppid": 21674,
                    "group_id": 21707,
                    "status": "S",
                    "priority": "20",
                    "size": 204612,
                }
            }
        },
        "ucode_pkt_PPE0": {
            "pids": {
                21808: {
                    "ppid": 21782,
                    "group_id": 21808,
                    "status": "S",
                    "priority": "20",
                    "size": 714688,
                }
            }
        },
        "cpp_sp_svr": {
            "pids": {
                22006: {
                    "ppid": 21978,
                    "group_id": 22006,
                    "status": "S",
                    "priority": "20",
                    "size": 105148,
                }
            }
        },
        "cpp_ha_top_leve": {
            "pids": {
                22095: {
                    "ppid": 22086,
                    "group_id": 22095,
                    "status": "S",
                    "priority": "20",
                    "size": 76804,
                }
            }
        },
        "cpp_driver": {
            "pids": {
                22227: {
                    "ppid": 22198,
                    "group_id": 22227,
                    "status": "S",
                    "priority": "20",
                    "size": 66380,
                }
            }
        },
        "cpp_cp_svr": {
            "pids": {
                22336: {
                    "ppid": 22307,
                    "group_id": 22336,
                    "status": "S",
                    "priority": "20",
                    "size": 385264,
                }
            }
        },
        "cman_fp": {
            "pids": {
                22440: {
                    "ppid": 22413,
                    "group_id": 22440,
                    "status": "S",
                    "priority": "20",
                    "size": 31816,
                }
            }
        },
        "cmcc": {
            "pids": {
                24027: {
                    "ppid": 23857,
                    "group_id": 24027,
                    "status": "S",
                    "priority": "20",
                    "size": 22736,
                },
                24554: {
                    "ppid": 24491,
                    "group_id": 24554,
                    "status": "S",
                    "priority": "20",
                    "size": 20340,
                },
            }
        },
        "kworker/u32:6-loop12": {
            "pids": {
                24658: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/0:2": {
            "pids": {
                24680: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "iomd": {
            "pids": {
                25689: {
                    "ppid": 25660,
                    "group_id": 25689,
                    "status": "S",
                    "priority": "20",
                    "size": 63712,
                },
                25948: {
                    "ppid": 25933,
                    "group_id": 25948,
                    "status": "S",
                    "priority": "20",
                    "size": 63164,
                },
                26230: {
                    "ppid": 26219,
                    "group_id": 26230,
                    "status": "S",
                    "priority": "20",
                    "size": 61140,
                },
            }
        },
        "viptela-logrota": {
            "pids": {
                26789: {
                    "ppid": 1,
                    "group_id": 26788,
                    "status": "S",
                    "priority": "20",
                    "size": 1712,
                }
            }
        },
        "vip-confd-start": {
            "pids": {
                26960: {
                    "ppid": 26939,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 8940,
                },
                32130: {
                    "ppid": 26960,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 8184,
                },
                32132: {
                    "ppid": 26960,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 8280,
                },
            }
        },
        "kworker/0:1-events": {
            "pids": {
                27111: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "confd.smp": {
            "pids": {
                27158: {
                    "ppid": 26960,
                    "group_id": 26960,
                    "status": "S",
                    "priority": "20",
                    "size": 189012,
                }
            }
        },
        "erl_child_setup": {
            "pids": {
                27176: {
                    "ppid": 27158,
                    "group_id": 27176,
                    "status": "S",
                    "priority": "20",
                    "size": 620,
                }
            }
        },
        "kworker/u32:0-loop18": {
            "pids": {
                29863: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/u32:1-loop21": {
            "pids": {
                30032: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/8:0-rcu_gp": {
            "pids": {
                30120: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "netconf-subsys": {
            "pids": {
                31599: {
                    "ppid": 31598,
                    "group_id": 31582,
                    "status": "S",
                    "priority": "20",
                    "size": 3032,
                }
            }
        },
        "cfgmgr": {
            "pids": {
                32264: {
                    "ppid": 32256,
                    "group_id": 32264,
                    "status": "S",
                    "priority": "20",
                    "size": 36180,
                }
            }
        },
        "vdaemon": {
            "pids": {
                32389: {
                    "ppid": 32383,
                    "group_id": 32389,
                    "status": "S",
                    "priority": "20",
                    "size": 44708,
                }
            }
        },
        "kworker/0:0-rcu_gp": {
            "pids": {
                32457: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
        "kworker/u32:8-kverit": {
            "pids": {
                32489: {
                    "ppid": 2,
                    "group_id": 0,
                    "status": "I",
                    "priority": "20",
                    "size": 0,
                }
            }
        },
    }
}

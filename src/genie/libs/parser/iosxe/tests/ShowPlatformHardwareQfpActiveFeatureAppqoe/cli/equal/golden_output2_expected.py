expected_output = {
    "feature": {
        "appqoe": {
            "global": {
                "ip_non_tcp_pkts": 314759,
                "not_enabled": 0,
                "cft_handle_pkt": 0,
                "sdvt_divert_req_fail": 399829,
                "appqoe_sn_data_pkts_processed": 0,
                "appqoe_alloc_empty_ht_entry": 16,
                "appqoe_cvla_alloc_failure": 1,
                "appqoe_bulk_upd_mem_bm_no_sng": 0,
                "appqoe_srv_chain_transit_dre_bypass": 0,
                "appqoe_srv_chain_sn_unhealthy_bypass": 0,
                "appqoe_srv_chain_tcp_mid_flow_bypass": 0,
                "appqoe_srv_chain_non_tcp_bypass": 0,
                "appqoe_srv_chain_frag_bypass": 0,
                "appqoe_lb_without_dre": 0,
                "appqoe_svc_on_appqoe_vpn_drop": 0,
                "appqoe_sng_not_configured": 0,
                "appqoe_unknown_tlv_type": 0,
                "appqoe_sn_data_pkts_dropped": 0,
                "appqoe_reset_appnav_fo_data": 499911,
                "appqoe_lb_without_caching": 0,
                "sdvt_global_stats": {
                    "remarking_persistent_for_htx_inj_flows": 1,
                    "appnav_registration": 64,
                    "control_decaps_could_not_find_flow_from_tuple": 5982,
                    "within_sdvt_syn_policer_limit": 3441777,
                },
            },
            "sng": {
                "1": {
                    "sn_index": {
                        "0 (Green)": {
                            "ip": "140.140.0.5",
                            "oce_id": 2173591328,
                            "ocev6_id": 2173591392,
                            "appnav_stats": {
                                "to_sn": {
                                    "packets": 2311028380,
                                    "bytes": 1153888628632,
                                },
                                "from_sn": {
                                    "packets": 2527681444,
                                    "bytes": 1044707959405,
                                },
                            },
                            "sdvt_count_stats": {
                                "active_connections": 465,
                                "decaps": 2526833671,
                                "encaps": 2311028384,
                                "expired_connections": 848018,
                                "idle_timed_out_persistent_connections": 2353,
                                "decap_messages": {
                                    "processed_control_messages": 845665,
                                    "delete_requests_recieved": 845665,
                                    "deleted_protocol_decision": 845665,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {
                                    "packets": 2311028386,
                                    "bytes": 1015226926144,
                                },
                                "reinject": {
                                    "packets": 2526833672,
                                    "bytes": 856747757207,
                                },
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 6853
                            },
                            "sdvt_errors_stats": {},
                        },
                        "1 (Green)": {
                            "ip": "140.140.0.6",
                            "oce_id": 2173590944,
                            "ocev6_id": 2173591008,
                            "appnav_stats": {
                                "to_sn": {
                                    "packets": 1532425869,
                                    "bytes": 1031152755261,
                                },
                                "from_sn": {
                                    "packets": 1716481004,
                                    "bytes": 933320679322,
                                },
                            },
                            "sdvt_count_stats": {
                                "active_connections": 536,
                                "decaps": 1715653948,
                                "encaps": 1532425870,
                                "expired_connections": 826739,
                                "idle_timed_out_persistent_connections": 1800,
                                "decap_messages": {
                                    "processed_control_messages": 824939,
                                    "delete_requests_recieved": 824939,
                                    "deleted_protocol_decision": 824939,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {
                                    "packets": 1532425871,
                                    "bytes": 939207203225,
                                },
                                "reinject": {
                                    "packets": 1715653948,
                                    "bytes": 805326828294,
                                },
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 2135
                            },
                            "sdvt_errors_stats": {},
                        },
                        "2 (Green)": {
                            "ip": "140.140.0.7",
                            "oce_id": 2173591424,
                            "ocev6_id": 2173591488,
                            "appnav_stats": {
                                "to_sn": {
                                    "packets": 1622980630,
                                    "bytes": 1053155876806,
                                },
                                "from_sn": {
                                    "packets": 1798004782,
                                    "bytes": 929759501435,
                                },
                            },
                            "sdvt_count_stats": {
                                "active_connections": 518,
                                "decaps": 1797174459,
                                "encaps": 1622980631,
                                "expired_connections": 830178,
                                "idle_timed_out_persistent_connections": 2641,
                                "decap_messages": {
                                    "processed_control_messages": 827537,
                                    "delete_requests_recieved": 827537,
                                    "deleted_protocol_decision": 827537,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {
                                    "packets": 1622980631,
                                    "bytes": 955777039058,
                                },
                                "reinject": {
                                    "packets": 1797174459,
                                    "bytes": 795754934749,
                                },
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 3955
                            },
                            "sdvt_errors_stats": {},
                        },
                    }
                },
                "2": {
                    "sn_index": {
                        "3 (Down)": {
                            "ip": "140.140.0.2",
                            "oce_id": 2173591424,
                            "ocev6_id": 2173591488,
                            "appnav_stats": {
                                "to_sn": {"packets": 0, "bytes": 0},
                                "from_sn": {"packets": 0, "bytes": 0},
                            },
                            "sdvt_count_stats": {},
                            "sdvt_packet_stats": {},
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                        "4 (Green)": {
                            "ip": "140.140.0.3",
                            "oce_id": 2173591040,
                            "ocev6_id": 2173591104,
                            "appnav_stats": {
                                "to_sn": {"packets": 0, "bytes": 0},
                                "from_sn": {"packets": 0, "bytes": 0},
                            },
                            "sdvt_count_stats": {},
                            "sdvt_packet_stats": {},
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                        "5 (Green)": {
                            "ip": "140.140.0.4",
                            "oce_id": 2173590656,
                            "ocev6_id": 2173590720,
                            "appnav_stats": {
                                "to_sn": {"packets": 0, "bytes": 0},
                                "from_sn": {"packets": 0, "bytes": 0},
                            },
                            "sdvt_count_stats": {},
                            "sdvt_packet_stats": {},
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                    }
                },
                "3": {
                    "sn_index": {
                        "6 (Green)": {
                            "ip": "140.140.0.18",
                            "oce_id": 2173589104,
                            "ocev6_id": 2173590528,
                            "appnav_stats": {
                                "to_sn": {"packets": 81093914, "bytes": 62150892582},
                                "from_sn": {"packets": 75404208, "bytes": 42147444289},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4234,
                                "decaps": 75379416,
                                "encaps": 81093927,
                                "packets_unclassified_by_ingress_policy": 1,
                                "expired_connections": 27246,
                                "idle_timed_out_persistent_connections": 2446,
                                "decap_messages": {
                                    "processed_control_messages": 24807,
                                    "delete_requests_recieved": 24807,
                                    "deleted_protocol_decision": 24807,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 81093935, "bytes": 57285264066},
                                "reinject": {"packets": 75379425, "bytes": 36547522685},
                            },
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                        "7 (Green)": {
                            "ip": "140.140.0.19",
                            "oce_id": 2173590752,
                            "ocev6_id": 2173590816,
                            "appnav_stats": {
                                "to_sn": {"packets": 76940120, "bytes": 56971636336},
                                "from_sn": {"packets": 71775419, "bytes": 38608351136},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4352,
                                "decaps": 71750476,
                                "encaps": 76940136,
                                "expired_connections": 27431,
                                "idle_timed_out_persistent_connections": 2493,
                                "decap_messages": {
                                    "processed_control_messages": 24945,
                                    "delete_requests_recieved": 24945,
                                    "deleted_protocol_decision": 24945,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 76940140, "bytes": 52355238024},
                                "reinject": {"packets": 71750490, "bytes": 33276862842},
                            },
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                        "8 (Green)": {
                            "ip": "140.140.0.20",
                            "oce_id": 2173590560,
                            "ocev6_id": 2173590624,
                            "appnav_stats": {
                                "to_sn": {"packets": 82078389, "bytes": 63136586190},
                                "from_sn": {"packets": 76266746, "bytes": 42683514877},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4287,
                                "decaps": 76241655,
                                "encaps": 82078392,
                                "packets_unclassified_by_ingress_policy": 34,
                                "expired_connections": 27618,
                                "idle_timed_out_persistent_connections": 2531,
                                "decap_messages": {
                                    "processed_control_messages": 25093,
                                    "delete_requests_recieved": 25093,
                                    "deleted_protocol_decision": 25093,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 82078404, "bytes": 58211883630},
                                "reinject": {"packets": 76241662, "bytes": 37019796641},
                            },
                            "sdvt_drop_cause_stats": {},
                            "sdvt_errors_stats": {},
                        },
                        "9 (Green)": {
                            "ip": "140.140.0.22",
                            "oce_id": 2173590848,
                            "ocev6_id": 2173590912,
                            "appnav_stats": {
                                "to_sn": {"packets": 75634349, "bytes": 55482208206},
                                "from_sn": {"packets": 70649639, "bytes": 37839121675},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4403,
                                "decaps": 70624930,
                                "encaps": 75634357,
                                "packets_unclassified_by_ingress_policy": 4,
                                "expired_connections": 27263,
                                "idle_timed_out_persistent_connections": 2557,
                                "decap_messages": {
                                    "processed_control_messages": 24710,
                                    "delete_requests_recieved": 24710,
                                    "deleted_protocol_decision": 24710,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 75634369, "bytes": 50944150922},
                                "reinject": {"packets": 70624933, "bytes": 32591696781},
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 17
                            },
                            "sdvt_errors_stats": {},
                        },
                        "10 (Green)": {
                            "ip": "140.140.0.23",
                            "oce_id": 2173591136,
                            "ocev6_id": 2173591200,
                            "appnav_stats": {
                                "to_sn": {"packets": 82420748, "bytes": 63291957117},
                                "from_sn": {"packets": 76638027, "bytes": 42838665301},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4351,
                                "decaps": 76613114,
                                "encaps": 82420751,
                                "expired_connections": 27380,
                                "idle_timed_out_persistent_connections": 2475,
                                "decap_messages": {
                                    "processed_control_messages": 24910,
                                    "delete_requests_recieved": 24910,
                                    "deleted_protocol_decision": 24910,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 82420765, "bytes": 58346715737},
                                "reinject": {"packets": 76613115, "bytes": 37147214795},
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 3
                            },
                            "sdvt_errors_stats": {},
                        },
                        "11 (Green)": {
                            "ip": "140.140.0.24",
                            "oce_id": 2173591232,
                            "ocev6_id": 2173591296,
                            "appnav_stats": {
                                "to_sn": {"packets": 75845968, "bytes": 55687675125},
                                "from_sn": {"packets": 70792831, "bytes": 37770306532},
                            },
                            "sdvt_count_stats": {
                                "active_connections": 4338,
                                "decaps": 70768258,
                                "encaps": 75845970,
                                "expired_connections": 27072,
                                "idle_timed_out_persistent_connections": 2503,
                                "decap_messages": {
                                    "processed_control_messages": 24575,
                                    "delete_requests_recieved": 24575,
                                    "deleted_protocol_decision": 24575,
                                },
                            },
                            "sdvt_packet_stats": {
                                "divert": {"packets": 75845971, "bytes": 51136917201},
                                "reinject": {"packets": 70768263, "bytes": 32511874270},
                            },
                            "sdvt_drop_cause_stats": {
                                "packets_dropped_as_sn_unhealthy": 57
                            },
                            "sdvt_errors_stats": {},
                        },
                    }
                },
            },
            "sn_index": {
                "Default": {
                    "sdvt_count_stats": {
                        "decaps": 2,
                        "packets_unclassified_by_ingress_policy": 90,
                        "expired_connections": 51439,
                        "non_syn_divert_requests": 399829,
                        "decap_messages": {
                            "processed_control_messages": 1,
                            "delete_requests_recieved": 1,
                            "deleted_protocol_decision": 1,
                        },
                    },
                    "sdvt_packet_stats": {},
                    "sdvt_drop_cause_stats": {},
                    "sdvt_errors_stats": {"flows_bypassed_as_sn_unhealthy": 51439},
                }
            },
        }
    }
}


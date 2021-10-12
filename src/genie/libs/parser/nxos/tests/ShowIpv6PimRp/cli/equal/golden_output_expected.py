

expected_output = {
    "vrf": {
        "VRF1": {
             "address_family": {
                  "ipv6": {
                       "rp": {
                            "rp_list": {
                                 "2001:db8:1:1::1 SM bootstrap": {
                                      "df_ordinal": 0,
                                      "info_source_address": "2001:db8:1:1::1",
                                      "info_source_type": "bootstrap",
                                      "mode": "SM",
                                      "group_ranges": "ff05::1/8",
                                      "expiration": "00:02:20",
                                      "priority": 192,
                                      "up_time": "03:29:13",
                                      "address": "2001:db8:1:1::1"
                                 }
                            },
                            "rp_mappings": {
                                 "ff05::1/8 2001:db8:1:1::1 bootstrap": {
                                      "group": "ff05::1/8",
                                      "rp_address": "2001:db8:1:1::1",
                                      "expiration": "00:02:20",
                                      "protocol": "bootstrap",
                                      "up_time": "03:29:13"
                                 }
                            },
                            "bsr": {
                                 "bsr_address": {
                                      "2001:db8:1:1::1": {
                                           "mode": "SM",
                                           "policy": "ff05::1/8",
                                           "priority": 192,
                                           "address": "2001:db8:1:1::1"
                                      }
                                 },
                                 "bsr": {
                                      "priority": 99,
                                      "hash_mask_length": 128,
                                      "expires": "00:01:37",
                                      "address": "2001:db8:1:1::1",
                                      "up_time": "00:09:14"
                                 },
                                 "bsr_candidate": {
                                      "hash_mask_length": 128,
                                      "priority": 99,
                                      "address": "2001:db8:1:1::1"
                                 },
                                 "rp": {
                                      "rp_address": "2001:db8:1:1::1",
                                      "group_policy": "ff05::1/8",
                                      "up_time": "03:29:13"
                                 },
                                 "rp_candidate_next_advertisement": "00:02:20"
                            }
                       },
                       "sm": {
                            "asm": {
                                 "anycast_rp": {
                                      "2001:db8:111:111::111 2001:db8:3:4::5": {
                                           "anycast_address": "2001:db8:111:111::111"
                                      },
                                      "2001:db8:111:111::111 2001:db8:1:2::2": {
                                           "anycast_address": "2001:db8:111:111::111"
                                      }
                                 }
                            }
                       }
                  }
             }
        },
        "default": {
             "address_family": {
                  "ipv6": {
                       "rp": {
                            "rp_list": {
                                 "2001:db8:1:1::1 SM bootstrap": {
                                      "df_ordinal": 0,
                                      "info_source_address": "2001:db8:1:1::1",
                                      "info_source_type": "bootstrap",
                                      "mode": "SM",
                                      "group_ranges": "ff05::1/8",
                                      "expiration": "00:02:20",
                                      "priority": 192,
                                      "up_time": "03:29:13",
                                      "address": "2001:db8:1:1::1"
                                 },
                                 "2001:db8:504::1 SM static": {
                                      "expiration": "0.000000",
                                      "info_source_type": "static",
                                      "mode": "SM",
                                      "group_ranges": "ff1e::3002/128 ff1e::3001/128",
                                      "df_ordinal": 0,
                                      "up_time": "00:00:02",
                                      "address": "2001:db8:504::1"
                                 },
                                 "2001:db8:12:12::12 BIDIR static": {
                                      "expiration": "0.000000",
                                      "info_source_type": "static",
                                      "mode": "BIDIR",
                                      "group_ranges": "ff08::/16",
                                      "df_ordinal": 7,
                                      "up_time": "00:58:17",
                                      "address": "2001:db8:12:12::12"
                                 },
                                 "2001:db8:111:111::111 SM static": {
                                      "expiration": "0.000000",
                                      "info_source_type": "static",
                                      "mode": "SM",
                                      "group_ranges": "ff09::/16",
                                      "df_ordinal": 0,
                                      "up_time": "00:00:52",
                                      "address": "2001:db8:111:111::111"
                                 }
                            },
                            "rp_mappings": {
                                 "ff09::/16 2001:db8:111:111::111 static": {
                                      "group": "ff09::/16",
                                      "rp_address": "2001:db8:111:111::111",
                                      "expiration": "0.000000",
                                      "protocol": "static",
                                      "up_time": "00:00:52"
                                 },
                                 "ff05::1/8 2001:db8:1:1::1 bootstrap": {
                                      "group": "ff05::1/8",
                                      "rp_address": "2001:db8:1:1::1",
                                      "expiration": "00:02:20",
                                      "protocol": "bootstrap",
                                      "up_time": "03:29:13"
                                 },
                                 "ff08::/16 2001:db8:12:12::12 static": {
                                      "group": "ff08::/16",
                                      "rp_address": "2001:db8:12:12::12",
                                      "expiration": "0.000000",
                                      "protocol": "static",
                                      "up_time": "00:58:17"
                                 },
                                 "ff1e::3002/128 ff1e::3001/128 2001:db8:504::1 static": {
                                      "group": "ff1e::3002/128 ff1e::3001/128",
                                      "rp_address": "2001:db8:504::1",
                                      "expiration": "0.000000",
                                      "protocol": "static",
                                      "up_time": "00:00:02"
                                 }
                            },
                            "static_rp": {
                                 "2001:db8:111:111::111": {
                                      "sm": {
                                           "policy_name": "ff09::/16"
                                      }
                                 },
                                 "2001:db8:504::1": {
                                      "sm": {
                                           "route_map": "PIM6-STATIC-RP",
                                           "policy_name": "ff1e::3002/128 ff1e::3001/128"
                                      }
                                 },
                                 "2001:db8:12:12::12": {
                                      "bidir": {
                                           "policy_name": "ff08::/16"
                                      }
                                 }
                            },
                            "bsr": {
                                 "bsr_address": {
                                      "2001:db8:1:1::1": {
                                           "mode": "SM",
                                           "policy": "ff05::1/8",
                                           "priority": 192,
                                           "address": "2001:db8:1:1::1"
                                      }
                                 },
                                 "bsr": {
                                      "hash_mask_length": 128,
                                      "priority": 99,
                                      "address": "2001:db8:1:1::1"
                                 },
                                 "bsr_candidate": {
                                      "hash_mask_length": 128,
                                      "priority": 99,
                                      "address": "2001:db8:1:1::1"
                                 },
                                 "rp": {
                                      "rp_address": "2001:db8:1:1::1",
                                      "group_policy": "ff05::1/8",
                                      "up_time": "03:29:13"
                                 },
                                 "bsr_next_bootstrap": "00:00:15",
                                 "rp_candidate_next_advertisement": "00:02:20"
                            }
                       },
                       "sm": {
                            "asm": {
                                 "anycast_rp": {
                                      "2001:db8:111:111::111 2001:db8:3:4::5": {
                                           "anycast_address": "2001:db8:111:111::111"
                                      },
                                      "2001:db8:111:111::111 2001:db8:1:2::2": {
                                           "anycast_address": "2001:db8:111:111::111"
                                      }
                                 }
                            }
                       }
                  }
             }
        }
   }
}

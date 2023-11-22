expected_output = {
    "primary_load_time_percent":0,
    "secondary_load_time_percent":0,
    "one_minute_load_percent":1,
    "five_minute_load_percent":1,
    "ntp_time":"14:48:32.688 UTC Tue Mar 22 2022",
    "smart_licensing_status":{
        "export_authorization_key":{
            "features_authorized":"none"
        },
        "utility":{
            "status":"DISABLED"
        },
        "smart_licensing_using_policy":{
            "status":"ENABLED"
        },
        "data_privacy":{
            "sending_hostname":"yes",
            "callhome_hostname_privacy":"DISABLED",
            "smart_licensing_hostname_privacy":"DISABLED",
            "version_privacy":"DISABLED"
        },
        "transport":{
            "type":"Smart",
            "url":"https://smartreceiver.cisco.com/licservice/license",
            "proxy":{
                "address":"<empty>",
                "port":"<empty>",
                "username":"<empty>",
                "password":"<empty>"
            },
            "server_identity_check":"True"
        },
        "miscellaneous":{
            "custom_id":"<empty>"
        },
        "policy":{
            "policy_in_use":"Installed On Mar 22 11:19:35 2022 UTC",
            "policy_name":"SLE Policy",
            "reporting_ack_required":"yes (Customer Policy)",
            "unenforced_non_export_perpetual_attributes":{
                "first_report_requirement_days":"30 (Customer Policy)",
                "reporting_frequency_days":"60 (Customer Policy)",
                "report_on_change_days":"60 (Customer Policy)"
            },
            "unenforced_non_export_subscription_attributes":{
                "first_report_requirement_days":"120 (Customer Policy)",
                "reporting_frequency_days":"111 (Customer Policy)",
                "report_on_change_days":"111 (Customer Policy)"
            },
            "enforced_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"0 (CISCO default)",
                "reporting_frequency_days":"90 (Customer Policy)",
                "report_on_change_days":"60 (Customer Policy)"
            },
            "export_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"0 (CISCO default)",
                "reporting_frequency_days":"30 (Customer Policy)",
                "report_on_change_days":"30 (Customer Policy)"
            }
        },
        "usage_reporting":{
            "last_ack_received":"Mar 22 12:19:01 2022 UTC",
            "next_ack_deadline":"May 21 12:19:01 2022 UTC",
            "reporting_push_interval":"30  days State(4) InPolicy(60)",
            "next_ack_push_check":"<none>",
            "next_report_push":"Apr 21 12:14:02 2022 UTC",
            "last_report_push":"Mar 22 12:14:02 2022 UTC",
            "last_report_file_write":"<none>"
        }
    },
    "license_usage":{
        "handle":{
            1:{
                "license":"network-advantage",
                "entitlement_tag":"regid.2017-03.com.cisco.advantagek9,1.0_bd1da96e-ec1d-412b-a50e-53846b347d53",
                "description":"C9300-24 Network Advantage",
                "count":3,
                "version":"1.0",
                "status":"IN USE(15)",
                "status_time":"Mar 22 11:13:23 2022 UTC",
                "request_time":"Mar 22 11:13:34 2022 UTC",
                "export_status":"NOT RESTRICTED",
                "feature_name":"network-advantage",
                "feature_description":"C9300-24 Network Advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual",
                "measurements":{
                    "entitlement":{
                        "interval":"00:01:00",
                        "current_value":3
                    }
                },
                "soft_enforced":"True"
            },
            2:{
                "license":"dna-advantage",
                "entitlement_tag":"regid.2017-05.com.cisco.c9300_dna_advantage,1.0_411773c3-2116-4c10-94a4-5d357fe6ff18",
                "description":"C9300-24 DNA Advantage",
                "count":3,
                "version":"1.0",
                "status":"IN USE(15)",
                "status_time":"Mar 22 11:13:23 2022 UTC",
                "request_time":"Mar 22 11:13:34 2022 UTC",
                "export_status":"NOT RESTRICTED",
                "feature_name":"dna-advantage",
                "feature_description":"C9300-24 DNA Advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Subscription",
                "measurements":{
                    "entitlement":{
                        "interval":"00:01:00",
                        "current_value":3
                    }
                },
                "soft_enforced":"True"
            },
            9:{
                "license":"air-network-advantage",
                "entitlement_tag":"regid.2018-06.com.cisco.DNA_NWStack,1.0_e7244e71-3ad5-4608-8bf0-d12f67c80896",
                "description":"air-network-advantage",
                "count":0,
                "version":"1.0",
                "status":"IN USE(15)",
                "status_time":"Mar 22 12:13:29 2022 UTC",
                "request_time":"None",
                "export_status":"NOT RESTRICTED",
                "feature_name":"air-network-advantage",
                "feature_description":"air-network-advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":0
                    }
                },
                "soft_enforced":"True"
            },
            10:{
                "license":"air-dna-advantage",
                "entitlement_tag":"regid.2017-08.com.cisco.AIR-DNA-A,1.0_b6308627-3ab0-4a11-a3d9-586911a0d790",
                "description":"air-dna-advantage",
                "count":0,
                "version":"1.0",
                "status":"IN USE(15)",
                "status_time":"Mar 22 12:13:29 2022 UTC",
                "request_time":"None",
                "export_status":"NOT RESTRICTED",
                "feature_name":"air-dna-advantage",
                "feature_description":"air-dna-advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Subscription",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":0
                    }
                },
                "soft_enforced":"True"
            }
        }
    },
    "product_information":{
        "udi":{
            "pid":"C9300-24UX",
            "sn":"FCW2134L00C"
        },
        "ha_udi_list":{
            "active":{
                "pid":"C9300-24UX",
                "sn":"FCW2134L00C"
            },
            "standby":{
                "pid":"C9300-24U",
                "sn":"FOC2129Z02H"
            },
            "member":{
                "pid":"C9300-24T",
                "sn":"FCW2125L07Y"
            }
        }
    },
    "agent_version":{
        "smart_agent_for_licensing":"5.1.26_rel/120"
    },
    "upcoming_scheduled_jobs":{
        "current_time":"Mar 22 14:48:32 2022 UTC",
        "daily":"Mar 23 11:13:25 2022 UTC (20 hours, 24 minutes, 53 seconds remaining)",
        "authorization_renewal":"Mar 23 11:15:05 2022 UTC (20 hours, 26 minutes, 33 seconds remaining)",
        "init_flag_check":"Expired Not Rescheduled",
        "register_period_expiration_check":"Expired Not Rescheduled",
        "ack_expiration_check":"Expired Not Rescheduled",
        "reservation_configuration_mismatch_between_nodes_in_ha_mode":"Expired Not Rescheduled",
        "retrieve_data_processing_result":"Expired Not Rescheduled",
        "start_utility_measurements":"Mar 22 14:49:00 2022 UTC (28 seconds remaining)",
        "send_utility_rum_reports":"Apr 21 12:14:01 2022 UTC (29 days, 21 hours, 25 minutes, 29 seconds remaining)",
        "save_unreported_rum_reports":"Mar 22 15:48:10 2022 UTC (59 minutes, 38 seconds remaining)",
        "process_utility_rum_reports":"Mar 23 11:14:05 2022 UTC (20 hours, 25 minutes, 33 seconds remaining)",
        "data_synchronization":"Expired Not Rescheduled",
        "external_event":"May 21 11:14:04 2022 UTC (59 days, 20 hours, 25 minutes, 32 seconds remaining)",
        "operational_model":"Expired Not Rescheduled"
    },
    "communication_statistics":{
        "communication_level_allowed":"DIRECT",
        "overall_state":"<empty>",
        "trust_establishment":{
            "attempts":"Total=1, Success=1, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK on Mar 22 11:19:35 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Mar 22 11:19:35 2022 UTC",
            "last_failure_time":"<none>"
        },
        "trust_acknowledgement":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "usage_reporting":{
            "attempts":"Total=4, Success=4, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK_POLL on Mar 22 12:14:01 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Mar 22 12:14:01 2022 UTC",
            "last_failure_time":"<none>"
        },
        "result_polling":{
            "attempts":"Total=4, Success=4, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK on Mar 22 12:19:01 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Mar 22 12:19:01 2022 UTC",
            "last_failure_time":"<none>"
        },
        "authorization_request":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "authorization_confirmation":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "authorization_return":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "trust_sync":{
            "attempts":"Total=2, Success=2, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK on Mar 22 11:28:22 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Mar 22 11:28:22 2022 UTC",
            "last_failure_time":"<none>"
        },
        "hello_message":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        }
    },
    "license_certificates":{
        "production_cert":"True"
    },
    "ha_info":{
        "rp_role":"Active",
        "chassis_role":"Active",
        "behavior_role":"Active",
        "rmf":"True",
        "cf":"True",
        "cf_state":"Stateless",
        "message_flow_allowed":"False"
    },
    "reservation_info":{
        "license_reservation":"DISABLED",
        "overall_status":{
            "active":{
                "pid":"C9300-24UX",
                "sn":"FCW2134L00C",
                "reservation_status":"NOT INSTALLED",
                "request_code":"<none>",
                "last_return_code":"<none>",
                "last_confirmation_code":"<none>",
                "reservation_authorization_code":"<none>"
            },
            "standby":{
                "pid":"C9300-24U",
                "sn":"FOC2129Z02H",
                "reservation_status":"NOT INSTALLED",
                "request_code":"<none>",
                "last_return_code":"<none>",
                "last_confirmation_code":"<none>",
                "reservation_authorization_code":"<none>"
            },
            "member":{
                "pid":"C9300-24T",
                "sn":"FCW2125L07Y",
                "reservation_status":"NOT INSTALLED",
                "request_code":"<none>",
                "last_return_code":"<none>",
                "last_confirmation_code":"<none>",
                "reservation_authorization_code":"<none>"
            }
        },
        "purchased_licenses":"No Purchase Information Available"
    },
    "other_info":{
        "software_id":"regid.2017-05.com.cisco.C9300,v1_727af1d9-6c39-4444-b301-863f81445b72",
        "agent_state":"authorized",
        "ts_enable":"True",
        "transport":"Smart",
        "default_url":"https://smartreceiver.cisco.com/licservice/license",
        "locale":"en_US.UTF-8",
        "debug_flags":"0x7",
        "privacy_send_hostname":"True",
        "privacy_send_ip":"True",
        "build_type":"Production",
        "sizeof_char":1,
        "sizeof_int":4,
        "sizeof_long":4,
        "sizeof_char_*":8,
        "sizeof_time_t":4,
        "sizeof_size_t":8,
        "endian":"Big",
        "write_erase_occurred":"False",
        "xos_version":"0.12.0.0",
        "config_persist_received":"True",
        "message_version":"1.3",
        "connect_info_name":"SSM",
        "connect_info_version":"1.3",
        "connect_info_prod":"True",
        "connect_info_capabilities":"DLC, AppHA, EXPORT_2, POLICY_USAGE, UTILITY",
        "agent_capabilities":"UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE",
        "check_point_interface":"True",
        "config_management_interface":"False",
        "license_map_interface":"True",
        "ha_interface":"True",
        "trusted_store_interface":"True",
        "platform_data_interface":"True",
        "crypto_version_2_interface":"False",
        "sapluginmgmtinterfacemutex":"True",
        "sapluginmgmtipdomainname":"True",
        "smartagentclientwaitforserver":2000,
        "smartagentcmretrysend":"True",
        "smartagentclientisunified":"True",
        "smartagentcmclient":"True",
        "smartagentclientname":"UnifiedClient",
        "builtinencryption":"True",
        "enableoninit":"True",
        "routingreadybyevent":"True",
        "systeminitbyevent":"True",
        "smarttransportserveridcheck":"True",
        "smarttransportproxysupport":"True",
        "smartagentreportonupgrade":"False",
        "smartagentusagestatisticsenable":"False",
        "smartagentmaxrummemory":50,
        "smartagentconcurrentthreadmax":10,
        "smartagentpolicycontrollermodel":"False",
        "smartagentpolicymodel":"True",
        "smartagentfederallicense":"True",
        "smartagentmultitenant":"False",
        "attr365dayevalsyslog":"True",
        "checkpointwriteonly":"False",
        "smartagentdelaycertvalidation":"False",
        "enablebydefault":"False",
        "conversionautomatic":"False",
        "conversionallowed":"False",
        "storageencryptdisable":"False",
        "storageloadunencrypteddisable":"False",
        "tsplugindisable":"False",
        "bypassudicheck":"False",
        "loggingaddtstamp":"False",
        "loggingaddtid":"True",
        "highavailabilityoverrideevent":"UnknownPlatformEvent",
        "platformindependentoverrideevent":"UnknownPlatformEvent",
        "platformoverrideevent":"SmartAgentSystemDataListChanged",
        "waitforharole":"False",
        "standbyishot":"True",
        "chkpttype":2,
        "delaycomminit":"False",
        "rolebyevent":"True",
        "maxtracelength":150,
        "tracealwayson":"True",
        "debugflags":0,
        "event_log_max_size":"5120 KB",
        "event_log_current_size":"CALCULATING",
        "trust_data":{
            "fcw2134l00c:":{
                "p":"C9300-24UX",
                "trustvalue":"Trust Data INSTALLED"
            },
            "foc2129z02h:":{
                "p":"C9300-24U",
                "trustvalue":"Trust Data INSTALLED"
            },
            "fcw2125l07y:":{
                "p":"C9300-24T",
                "trustvalue":"Trust Data INSTALLED"
            }
        },
        "overall_trust":"INSTALLED (2)",
        "clock_synced_with_ntp":"True"
    },
    "platform_provided_mapping_table":{
        "pid":"C9300-24UX",
        "total_licenses_found":194,
        "enforced_licenses":{
            "fcw2134l00c":{
                "pid":"C9300-24UX"
            },
            "foc2129z02h":{
                "pid":"C9300-24U"
            },
            "fcw2125l07y":{
                "pid":"C9300-24T"
            }
        }
    } 
}
expected_output = {
    "primary_load_time_percent":0,
    "secondary_load_time_percent":0,
    "one_minute_load_percent":0,
    "five_minute_load_percent":0,
    "ntp_time":"14:10:53.416 UTC Sat May 21 2022",
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
        "account_information":{
            "smart_account":"<none>",
            "virtual_account":"<none>"
        },
        "data_privacy":{
            "sending_hostname":"yes",
            "callhome_hostname_privacy":"DISABLED",
            "smart_licensing_hostname_privacy":"DISABLED",
            "version_privacy":"DISABLED"
        },
        "transport":{
            "type":"cslu",
            "cslu_address":"http://172.19.180.22:8182/cslu/v1/pi",
            "proxy":{
                "address":"<empty>",
                "port":"<empty>",
                "username":"<empty>",
                "password":"<empty>"
            },
            "server_identity_check":"True",
            "vrf":"<empty>"
        },
        "miscellaneous":{
            "custom_id":"<empty>"
        },
        "policy":{
            "policy_in_use":"Merged from multiple sources.",
            "reporting_ack_required":"yes (CISCO default)",
            "unenforced_non_export_perpetual_attributes":{
                "first_report_requirement_days":"365 (CISCO default)",
                "reporting_frequency_days":"0 (CISCO default)",
                "report_on_change_days":"90 (CISCO default)"
            },
            "unenforced_non_export_subscription_attributes":{
                "first_report_requirement_days":"90 (CISCO default)",
                "reporting_frequency_days":"90 (CISCO default)",
                "report_on_change_days":"90 (CISCO default)"
            },
            "enforced_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"0 (CISCO default)",
                "reporting_frequency_days":"0 (CISCO default)",
                "report_on_change_days":"0 (CISCO default)"
            },
            "export_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"0 (CISCO default)",
                "reporting_frequency_days":"0 (CISCO default)",
                "report_on_change_days":"0 (CISCO default)"
            }
        },
        "usage_reporting":{
            "last_ack_received":"<none>",
            "next_ack_deadline":"Apr 06 13:28:03 2023 UTC",
            "reporting_push_interval":"30  days State(2) InPolicy(365)",
            "next_ack_push_check":"<none>",
            "next_report_push":"May 21 07:54:06 2022 UTC",
            "last_report_push":"<none>",
            "last_report_file_write":"<none>"
        }
    },
    "license_usage":{
        "handle":{
            1:{
                "license":"network-essentials",
                "entitlement_tag":"regid.2017-03.com.cisco.essentialsk9,1.0_90406ae8-385e-43aa-ac98-91da0ea270e2",
                "description":"C9300-24 Network Essentials",
                "count":3,
                "version":"1.0",
                "status":"IN USE(15)",
                "status_time":"May 21 06:53:32 2022 UTC",
                "request_time":"May 21 06:53:42 2022 UTC",
                "export_status":"NOT RESTRICTED",
                "feature_name":"network-essentials",
                "feature_description":"C9300-24 Network Essentials",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":3,
                        "current_report":1649251641,
                        "previous":1649251640
                    }
                },
                "soft_enforced":"True"
            },
            5:{
                "license":"air-network-advantage",
                "entitlement_tag":"regid.2018-06.com.cisco.DNA_NWStack,1.0_e7244e71-3ad5-4608-8bf0-d12f67c80896",
                "description":"air-network-advantage",
                "count":0,
                "version":"1.0",
                "status":"NOT IN USE(1)",
                "status_time":"May 21 07:53:36 2022 UTC",
                "request_time":"None",
                "export_status":"NOT RESTRICTED",
                "feature_name":"air-network-advantage",
                "feature_description":"air-network-advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":0,
                        "current_report":0,
                        "previous":0
                    }
                },
                "soft_enforced":"True"
            },
            6:{
                "license":"air-dna-advantage",
                "entitlement_tag":"regid.2017-08.com.cisco.AIR-DNA-A,1.0_b6308627-3ab0-4a11-a3d9-586911a0d790",
                "description":"air-dna-advantage",
                "count":0,
                "version":"1.0",
                "status":"NOT IN USE(1)",
                "status_time":"May 21 07:53:36 2022 UTC",
                "request_time":"None",
                "export_status":"NOT RESTRICTED",
                "feature_name":"air-dna-advantage",
                "feature_description":"air-dna-advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Subscription",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":0,
                        "current_report":0,
                        "previous":0
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
        "smart_agent_for_licensing":"5.5.11_rel/31"
    },
    "upcoming_scheduled_jobs":{
        "current_time":"May 21 14:10:53 2022 UTC",
        "daily":"May 22 06:53:34 2022 UTC (16 hours, 42 minutes, 41 seconds remaining)",
        "authorization_renewal":"Expired Not Rescheduled",
        "init_flag_check":"Expired Not Rescheduled",
        "reservation_configuration_mismatch_between_nodes_in_ha_mode":"Expired Not Rescheduled",
        "start_utility_measurements":"May 21 14:23:36 2022 UTC (12 minutes, 43 seconds remaining)",
        "send_utility_rum_reports":"May 22 07:54:06 2022 UTC (17 hours, 43 minutes, 13 seconds remaining)",
        "save_unreported_rum_reports":"May 21 15:08:46 2022 UTC (57 minutes, 53 seconds remaining)",
        "data_synchronization":"May 21 14:56:35 2022 UTC (45 minutes, 42 seconds remaining)",
        "external_event":"Feb 05 13:28:02 2023 UTC (259 days, 23 hours, 17 minutes, 9 seconds remaining)",
        "operational_model":"Expired Not Rescheduled"
    },
    "communication_statistics":{
        "communication_level_allowed":"INDIRECT",
        "overall_state":"<empty>",
        "trust_establishment":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
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
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "result_polling":{
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
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
            "attempts":"Total=0, Success=0, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"<none>",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"<none>"
        },
        "hello_message":{
            "attempts":"Total=11, Success=0, Fail=11",
            "ongoing_failure":"Overall=11 Communication=11",
            "last_response":"NO REPLY on May 21 13:56:36 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"<none>",
            "last_failure_time":"May 21 13:56:36 2022 UTC"
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
    "usage_report_summary":{
        "total":3,
        "purged":"0(0)",
        "total_acknowledged_received":0,
        "waiting_for_ack":"0(3)",
        "available_to_report":3,
        "collecting_data":1,
        "maximum_display":3,
        "in_storage":3,
        "mia":"0(0)",
        "report_module_status":"Ready"
    },
    "other_info":{
        "software_id":"regid.2017-05.com.cisco.C9300,v1_727af1d9-6c39-4444-b301-863f81445b72",
        "agent_state":"authorized",
        "ts_enable":"True",
        "transport":"cslu",
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
        "config_persist_received":"False",
        "message_version":"1.3",
        "connect_info_name":"<empty>",
        "connect_info_version":"<empty>",
        "connect_info_additional":"<empty>",
        "connect_info_prod":"False",
        "connect_info_capabilities":"<empty>",
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
        "smarttransportvrfsupport":"True",
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
        "smartagenttelemetryrumreportmax":1000,
        "smartagentrumtelemetryrumstoremin":500,
        "smartagentpolicydisplayformat":0,
        "smartagentreportonupgrade":"False",
        "smartagentindividualrumencrypt":2,
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
        "event_log_current_size":"90 KB",
        "trust_data":{
            "fcw2134l00c":{
                "p":"C9300-24UX",
                "trustvalue":"No Trust Data"
            },
            "foc2129z02h":{
                "p":"C9300-24U",
                "trustvalue":"No Trust Data"
            },
            "fcw2125l07y":{
                "p":"C9300-24T",
                "trustvalue":"No Trust Data"
            }
        },
        "overall_trust":"No ID",
        "clock_synced_with_ntp":"True"
    },
    "platform_provided_mapping_table":{
        "pid":"C9300-24UX",
        "total_licenses_found":215,
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
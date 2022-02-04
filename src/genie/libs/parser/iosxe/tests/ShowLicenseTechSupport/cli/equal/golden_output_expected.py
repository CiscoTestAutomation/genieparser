expected_output = {
    "primary_load_time_percent":1,
    "secondary_load_time_percent":0,
    "one_minute_load_percent":0,
    "five_minute_load_percent":0,
    "ntp_time":".13:28:08.565 UTC Tue Jan 11 2022",
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
            "smart_account":"SA-Switching-Polaris As of Jan 10 20:31:32 2022 UTC",
            "virtual_account":"SLE_Test"
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
            "server_identity_check":"False",
            "vrf":"<empty>"
        },
        "miscellaneous":{
            "custom_id":"<empty>"
        },
        "policy":{
            "policy_in_use":"Installed On Jan 10 17:18:01 2022 UTC",
            "policy_name":"Custom Policy",
            "reporting_ack_required":"yes (Customer Policy)",
            "unenforced_non_export_perpetual_attributes":{
                "first_report_requirement_days":"365 (Customer Policy)",
                "reporting_frequency_days":"0 (Customer Policy)",
                "report_on_change_days":"90 (Customer Policy)"
            },
            "unenforced_non_export_subscription_attributes":{
                "first_report_requirement_days":"90 (Customer Policy)",
                "reporting_frequency_days":"90 (Customer Policy)",
                "report_on_change_days":"90 (Customer Policy)"
            },
            "enforced_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"365 (Customer Policy)",
                "reporting_frequency_days":"90 (Customer Policy)",
                "report_on_change_days":"90 (Customer Policy)"
            },
            "export_perpetual_subscription_license_attributes":{
                "first_report_requirement_days":"365 (Customer Policy)",
                "reporting_frequency_days":"90 (Customer Policy)",
                "report_on_change_days":"90 (Customer Policy)"
            }
        },
        "usage_reporting":{
            "last_ack_received":"Jan 10 20:32:26 2022 UTC",
            "next_ack_deadline":"Apr 10 20:32:26 2022 UTC",
            "reporting_push_interval":"30  days State(4) InPolicy(90)",
            "next_ack_push_check":"<none>",
            "next_report_push":"Jan 11 13:21:47 2022 UTC",
            "last_report_push":"Jan 10 20:31:25 2022 UTC",
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
                "status_time":"Jan 10 20:21:10 2022 UTC",
                "request_time":"Jan 10 20:21:24 2022 UTC",
                "export_status":"NOT RESTRICTED",
                "feature_name":"network-advantage",
                "feature_description":"C9300-24 Network Advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":3,
                        "current_report":1641834470,
                        "previous":1641834468
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
                "status_time":"Jan 10 20:21:10 2022 UTC",
                "request_time":"Jan 10 20:21:24 2022 UTC",
                "export_status":"NOT RESTRICTED",
                "feature_name":"dna-advantage",
                "feature_description":"C9300-24 DNA Advantage",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Subscription",
                "measurements":{
                    "entitlement":{
                        "interval":"00:15:00",
                        "current_value":3,
                        "current_report":1641834471,
                        "previous":1641834469
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
                "status":"NOT IN USE(1)",
                "status_time":"Jan 11 13:21:17 2022 UTC",
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
            10:{
                "license":"air-dna-advantage",
                "entitlement_tag":"regid.2017-08.com.cisco.AIR-DNA-A,1.0_b6308627-3ab0-4a11-a3d9-586911a0d790",
                "description":"air-dna-advantage",
                "count":0,
                "version":"1.0",
                "status":"NOT IN USE(1)",
                "status_time":"Jan 11 13:21:17 2022 UTC",
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
        "smart_agent_for_licensing":"5.3.16_rel/55"
    },
    "upcoming_scheduled_jobs":{
        "current_time":"Jan 11 13:28:08 2022 UTC",
        "daily":"Jan 11 20:21:12 2022 UTC (6 hours, 53 minutes, 4 seconds remaining)",
        "authorization_renewal":"Jan 11 20:22:55 2022 UTC (6 hours, 54 minutes, 47 seconds remaining)",
        "init_flag_check":"Expired Not Rescheduled",
        "reservation_configuration_mismatch_between_nodes_in_ha_mode":"Expired Not Rescheduled",
        "retrieve_data_processing_result":"Expired Not Rescheduled",
        "start_utility_measurements":"Jan 11 13:36:18 2022 UTC (8 minutes, 10 seconds remaining)",
        "send_utility_rum_reports":"Jan 12 13:21:47 2022 UTC (23 hours, 53 minutes, 39 seconds remaining)",
        "save_unreported_rum_reports":"Jan 11 14:21:28 2022 UTC (53 minutes, 20 seconds remaining)",
        "process_utility_rum_reports":"Jan 11 20:37:26 2022 UTC (7 hours, 9 minutes, 18 seconds remaining)",
        "data_synchronization":"Expired Not Rescheduled",
        "external_event":"Apr 10 20:32:26 2022 UTC (89 days, 7 hours, 4 minutes, 18 seconds remaining)",
        "operational_model":"Expired Not Rescheduled",
        "hello_message":"Expired Not Rescheduled"
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
            "attempts":"Total=3, Success=3, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK_POLL on Jan 10 20:31:24 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Jan 10 20:31:24 2022 UTC",
            "last_failure_time":"<none>"
        },
        "result_polling":{
            "attempts":"Total=3, Success=3, Fail=0",
            "ongoing_failure":"Overall=0 Communication=0",
            "last_response":"OK on Jan 10 20:32:26 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Jan 10 20:32:26 2022 UTC",
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
            "last_response":"OK on Jan 10 20:31:12 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Jan 10 20:31:12 2022 UTC",
            "last_failure_time":"<none>"
        },
        "hello_message":{
            "attempts":"Total=12, Success=9, Fail=3",
            "ongoing_failure":"Overall=3 Communication=3",
            "last_response":"NO REPLY on Jan 11 13:21:47 2022 UTC",
            "failure_reason":"<none>",
            "last_success_time":"Jan 10 20:32:25 2022 UTC",
            "last_failure_time":"Jan 11 13:21:47 2022 UTC"
        }
    },
    "license_certificates":{
        "production_cert":"False"
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
        "purchased_licenses":"No Purchase Information Available",
        "last_reporting_not_required":{
            "entitlement_tag":"regid.2017-03.com.cisco.essentialsk9,1.0_90406ae8-385e-43aa-ac98-91da0ea270e2"
        }
    },
    "usage_report_summary":{
        "total":86,
        "purged":"0(0)",
        "total_acknowledged_received":76,
        "waiting_for_ack":"0(10)",
        "available_to_report":3,
        "collecting_data":2,
        "maximum_display":86,
        "in_storage":22,
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
        "event_log_current_size":"56 KB",
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
        "total_licenses_found":198,
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
expected_output = {
   "smart_licensing_status":{
      "license_conversion":{
         "automatic_conversion_enabled":"False"
      },
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
         "cslu_address":"<empty>",
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
         "next_ack_deadline":"Feb 22 22:52:03 2024 PDT",
         "reporting_push_interval":"30  days State(2) InPolicy(0)",
         "next_ack_push_check":"<none>",
         "next_report_push":"Nov 24 02:04:02 2023 PDT",
         "last_report_push":"<none>",
         "last_report_file_write":"<none>"
      }
   },
   "license_usage":{
      "handle":{
         1:{
            "license":"network-advantage",
            "entitlement_tag":"regid.2017-05.com.cisco.C9300_48P_NW_Advantagek9,1.0_6a224fe3-c92e-4440-a9c1-5d0e53a54015",
            "description":"C9300-48 Network Advantage",
            "count":2,
            "version":"1.0",
            "status":"IN USE(15)",
            "status_time":"Nov 24 02:01:48 2023 PDT",
            "request_time":"Nov 24 02:02:02 2023 PDT",
            "export_status":"NOT RESTRICTED",
            "feature_name":"network-advantage",
            "feature_description":"C9300-48 Network Advantage",
            "enforcement_type":"NOT ENFORCED",
            "license_type":"Perpetual",
            "measurements":{
               "entitlement":{
                  "interval":"00:15:00",
                  "current_value":2,
                  "current_report":1676661933,
                  "previous":1676661931
               }
            },
            "soft_enforced":"True"
         },
         4:{
            "license":"network-advantage",
            "entitlement_tag":"regid.2017-03.com.cisco.advantagek9,1.0_bd1da96e-ec1d-412b-a50e-53846b347d53",
            "description":"C9300-24 Network Advantage",
            "count":1,
            "version":"1.0",
            "status":"IN USE(15)",
            "status_time":"Nov 24 02:02:02 2023 PDT",
            "request_time":"Nov 24 02:02:02 2023 PDT",
            "export_status":"NOT RESTRICTED",
            "feature_name":"network-advantage",
            "feature_description":"C9300-24 Network Advantage",
            "enforcement_type":"NOT ENFORCED",
            "license_type":"Perpetual",
            "measurements":{
               "entitlement":{
                  "interval":"00:15:00",
                  "current_value":1,
                  "current_report":1676661934,
                  "previous":1676661932
               }
            },
            "soft_enforced":"True"
         }
      }
   },
   "product_information":{
      "udi":{
         "pid":"C9300-48UXM",
         "sn":"FOC2617YTXX"
      },
      "ha_udi_list":{
         "active":{
            "pid":"C9300-48UXM",
            "sn":"FOC2617YTXX"
         },
         "standby":{
            "pid":"C9300-48U",
            "sn":"FOC2618YCVZ"
         },
         "member":{
            "pid":"C9300-24U",
            "sn":"FOC2617YMQU"
         }
      }
   },
   "agent_version":{
      "smart_agent_for_licensing":"5.10.1_rel/5"
   },
   "upcoming_scheduled_jobs":{
      "current_time":"Dec 02 10:15:21 2023 PDT",
      "daily":"Dec 03 02:01:57 2023 PDT (15 hours, 46 minutes, 36 seconds remaining)",
      "init_flag_check":"Expired Not Rescheduled",
      "reservation_configuration_mismatch_between_nodes_in_ha_mode":"Expired Not Rescheduled",
      "start_utility_measurements":"Dec 02 10:20:24 2023 PDT (5 minutes, 3 seconds remaining)",
      "send_utility_rum_reports":"Dec 03 02:06:52 2023 PDT (15 hours, 51 minutes, 31 seconds remaining)",
      "save_unreported_rum_reports":"Dec 02 11:05:35 2023 PDT (50 minutes, 14 seconds remaining)",
      "process_utility_rum_reports":"Dec 03 02:02:36 2023 PDT (15 hours, 47 minutes, 15 seconds remaining)",
      "data_synchronization":"Dec 02 11:12:30 2023 PDT (57 minutes, 9 seconds remaining)",
      "external_event":"Dec 24 22:52:02 2023 PDT (22 days, 12 hours, 36 minutes, 41 seconds remaining)",
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
            "pid":"C9300-48UXM",
            "sn":"FOC2617YTXX",
            "reservation_status":"NOT INSTALLED",
            "request_code":"<none>",
            "last_return_code":"<none>",
            "last_confirmation_code":"<none>",
            "reservation_authorization_code":"<none>"
         },
         "standby":{
            "pid":"C9300-48U",
            "sn":"FOC2618YCVZ",
            "reservation_status":"NOT INSTALLED",
            "request_code":"<none>",
            "last_return_code":"<none>",
            "last_confirmation_code":"<none>",
            "reservation_authorization_code":"<none>"
         },
         "member":{
            "pid":"C9300-24U",
            "sn":"FOC2617YMQU",
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
      "total":810,
      "purged":"902(902)",
      "total_acknowledged_received":0,
      "waiting_for_ack":"0(349)",
      "available_to_report":349,
      "collecting_data":2,
      "maximum_display":349,
      "in_storage":0,
      "mia":"105(105)",
      "report_module_status":"Ready"
   },
   "device_telemetry_report_summary":{
      "data_channel":"AVAILABLE",
      "reports_on_disk":0,
      "trust_code_installed": "<none>",
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
      "config_persist_received":"True",
      "message_version":"1.3",
      "connect_info_name":"<empty>",
      "connect_info_version":"<empty>",
      "connect_info_additional":"<empty>",
      "connect_info_prod":"False",
      "connect_info_capabilities":"<empty>",
      "agent_capabilities":"UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE, TELEMETRY, TELEMETRY_POLICY",
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
      "smartagentcompliancestatus":"False",
      "smartagenttelemetryrumreportmax":600,
      "smartagentrumtelemetryrumstoremin":500,
      "smartagentpolicydisplayformat":0,
      "smartagentreportonupgrade":"False",
      "smartagentindividualrumencrypt":2,
      "smartagentmaxrummemory":50,
      "smartagentconcurrentthreadmax":10,
      "smartagentpolicycontrollermodel":"False",
      "smartagentdisablecacheswid":"False",
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
      "event_log_current_size":"6393 KB",
      "trust_data":{
         "foc2617ytxx":{
            "p":"C9300-48UXM",
            "trustvalue":"No Trust Data"
         },
         "foc2618ycvz":{
            "p":"C9300-48U",
            "trustvalue":"No Trust Data"
         },
         "foc2617ymqu":{
            "p":"C9300-24U",
            "trustvalue":"No Trust Data"
         }
      },
      "overall_trust":"No ID",
      "clock_synced_with_ntp":"False"
   },
   "platform_provided_mapping_table":{
      "pid":"C9300-48UXM",
      "total_licenses_found":213,
      "enforced_licenses":{
         "foc2617ytxx":{
            "pid":"C9300-48UXM",
            "hseck9_entitlement_tag":"regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2",
            "hseck9_no":3
         },
         "foc2618ycvz":{
            "pid":"C9300-48U",
            "hseck9_entitlement_tag":"regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2",
            "hseck9_no":3
         },
         "foc2617ymqu":{
            "pid":"C9300-24U",
            "hseck9_entitlement_tag":"regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2",
            "hseck9_no":3
         }
      }
   }
}


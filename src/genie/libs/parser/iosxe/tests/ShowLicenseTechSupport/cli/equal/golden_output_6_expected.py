expected_output = {   
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
         "type":"Smart",
         "url":"https://smartreceiver-dev.cisco.com/licservice/license",
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
         "next_ack_deadline":"Mar 19 19:51:37 2023 UTC",
         "reporting_push_interval":"30  days State(2) InPolicy(90)",
         "next_ack_push_check":"<none>",
         "next_report_push":"Jan 09 10:43:20 2023 UTC",
         "last_report_push":"<none>",
         "last_report_file_write":"<none>"
      }
   },
   "license_usage":{
      "handle":{
         1:{
            "license":"network-advantage",
            "entitlement_tag":"regid.2021-03.com.cisco.C9500X_NW_A,1.0_9cff48db-3555-4bf0-ae49-edfbb0a8327d",
            "description":"Network Advantage License for Catalyst 9500X Switches",
            "count":1,
            "version":"1.0",
            "status":"IN USE(15)",
            "status_time":"Jan 09 10:41:20 2023 UTC",
            "request_time":"Jan 09 10:41:20 2023 UTC",
            "export_status":"NOT RESTRICTED",
            "feature_name":"network-advantage",
            "feature_description":"Network Advantage License for Catalyst 9500X Switches",
            "enforcement_type":"NOT ENFORCED",
            "license_type":"Perpetual",
            "measurements":{
               "entitlement":{
                  "interval":"00:15:00",
                  "current_value":1,
                  "current_report":1671479454,
                  "previous":1671479452
               }
            },
            "soft_enforced":"True"
         },
         2:{
            "license":"dna-advantage",
            "entitlement_tag":"regid.2021-03.com.cisco.C9500X_DNA_A,1.0_ed879e7f-f17e-4a9e-a7c1-aee91e5d6ec3",
            "description":"DNA Advantage License for Catalyst 9500X Switches",
            "count":1,
            "version":"1.0",
            "status":"IN USE(15)",
            "status_time":"Jan 09 10:41:20 2023 UTC",
            "request_time":"Jan 09 10:41:20 2023 UTC",
            "export_status":"NOT RESTRICTED",
            "feature_name":"dna-advantage",
            "feature_description":"DNA Advantage License for Catalyst 9500X Switches",
            "enforcement_type":"NOT ENFORCED",
            "license_type":"Subscription",
            "measurements":{
               "entitlement":{
                  "interval":"00:15:00",
                  "current_value":1,
                  "current_report":1671479455,
                  "previous":1671479453
               }
            },
            "soft_enforced":"True"
         }
      }
   },
   "product_information":{
      "udi":{
         "pid":"C9500X-28C8D",
         "sn":"FDO2446000P"
      },
      "ha_udi_list":{
         "active":{
            "pid":"C9500X-28C8D",
            "sn":"FDO2446000P"
         },
         "standby":{
            "pid":"C9500X-28C8D",
            "sn":"FDO25200FUB"
         }
      }
   },
   "agent_version":{
      "smart_agent_for_licensing":"5.7.15_rel/44"
   },
   "upcoming_scheduled_jobs":{
      "current_time":"Jan 09 15:08:53 2023 UTC",
      "daily":"Jan 10 10:41:22 2023 UTC (19 hours, 32 minutes, 29 seconds remaining)",
      "authorization_renewal":"Expired Not Rescheduled",
      "init_flag_check":"Expired Not Rescheduled",
      "reservation_configuration_mismatch_between_nodes_in_ha_mode":"Expired Not Rescheduled",
      "start_utility_measurements":"Jan 09 15:08:59 2023 UTC (6 seconds remaining)",
      "send_utility_rum_reports":"Jan 10 10:54:54 2023 UTC (19 hours, 46 minutes, 1 seconds remaining)",
      "save_unreported_rum_reports":"Jan 09 15:54:09 2023 UTC (45 minutes, 16 seconds remaining)",
      "process_utility_rum_reports":"Jan 10 10:42:04 2023 UTC (19 hours, 33 minutes, 11 seconds remaining)",
      "authorization_code_process":"Jan 09 15:08:59 2023 UTC (6 seconds remaining)",
      "data_synchronization":"Expired Not Rescheduled",
      "external_event":"Jan 18 19:51:37 2023 UTC (9 days, 4 hours, 42 minutes, 44 seconds remaining)",
      "operational_model":"Expired Not Rescheduled"
   },
   "communication_statistics":{
      "communication_level_allowed":"INDIRECT",
      "overall_state":"Insufficient trust for direct communication",
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
            "pid":"C9500X-28C8D",
            "sn":"FDO2446000P",
            "reservation_status":"NOT INSTALLED",
            "request_code":"<none>",
            "last_return_code":"<none>",
            "last_confirmation_code":"<none>",
            "reservation_authorization_code":"<none>"
         },
         "standby":{
            "pid":"C9500X-28C8D",
            "sn":"FDO25200FUB",
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
      "total":10,
      "purged":"0(0)",
      "total_acknowledged_received":0,
      "waiting_for_ack":"0(12)",
      "available_to_report":12,
      "collecting_data":2,
      "maximum_display":12,
      "in_storage":10,
      "mia":"0(0)",
      "report_module_status":"Ready"
   },
   "device_telemetry_report_summary":{
      "data_channel":"NOT AVAILABLE",
      "reports_on_disk":0
   },
   "other_info":{
      "software_id":"regid.2017-05.com.cisco.C9500,v1_7435cf27-0075-4bfb-b67c-b42f3054e82a",
      "agent_state":"authorized",
      "ts_enable":"True",
      "transport":"Smart",
      "default_url":"https://smartreceiver-dev.cisco.com/licservice/license",
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
      "agent_capabilities":"UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE, TELEMETRY",
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
      "smartagenttelemetryrumreportmax":600,
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
      "event_log_current_size":"59 KB",
      "trust_data":{
         "fdo2446000p":{
            "p":"C9500X-28C8D",
            "trustvalue":"No Trust Data"
         },
         "fdo25200fub":{
            "p":"C9500X-28C8D",
            "trustvalue":"No Trust Data"
         }
      },
      "overall_trust":"No ID",
      "clock_synced_with_ntp":"False"
   },
   "platform_provided_mapping_table":{
      "pid":"C9500X-28C8D",
      "total_licenses_found":205,
      "enforced_licenses":{
         "fdo2446000p":{
            "pid":"C9500X-28C8D",
            "hseck9_entitlement_tag":"regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2",
            "hseck9_no":3
         },
         "fdo25200fub":{
            "pid":"C9500X-28C8D",
            "hseck9_entitlement_tag":"regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2",
            "hseck9_no":3
         }
      }
   }
}
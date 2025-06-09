expected_output = {
    "primary_load_time_percent": 2,
    "secondary_load_time_percent": 0,
    "one_minute_load_percent": 2,
    "five_minute_load_percent": 1,
    "ntp_time": "15:08:49.347 IST Wed Mar 19 2025",
    "smart_licensing_status": {
        "license_conversion": {
            "automatic_conversion_enabled": "False",
            "last_data_push": "<none>",
            "last_file_export": "<none>"
        },
        "export_authorization_key": {
            "features_authorized": "none"
        },
        "utility": {
            "status": "DISABLED"
        },
        "smart_licensing_using_policy": {
            "status": "ENABLED",
            "reporting_mode": "STANDARD"
        },
        "account_information": {
            "smart_account": "<none>",
            "virtual_account": "<none>"
        },
        "data_privacy": {
            "sending_hostname": "yes",
            "callhome_hostname_privacy": "DISABLED",
            "smart_licensing_hostname_privacy": "DISABLED",
            "version_privacy": "DISABLED"
        },
        "transport": {
            "type": "Smart",
            "url": "https://smartreceiver.cisco.com/licservice/license",
            "proxy": {
                "address": "173.36.224.108",
                "port": 80,
                "username": "<empty>",
                "password": "<empty>"
            },
            "server_identity_check": "True",
            "vrf": "<empty>",
            "ip_mode": "IPv4 ONLY",
            "trust_point": "SLA-TrustPoint"
        },
        "miscellaneous": {
            "custom_id": "<empty>"
        },
        "policy": {
            "policy_in_use": "Merged from multiple sources.",
            "reporting_ack_required": "yes (CISCO default)",
            "unenforced_non_export_perpetual_attributes": {
                "first_report_requirement_days": "365 (CISCO default)",
                "reporting_frequency_days": "0 (CISCO default)",
                "report_on_change_days": "90 (CISCO default)"
            },
            "unenforced_non_export_subscription_attributes": {
                "first_report_requirement_days": "90 (CISCO default)",
                "reporting_frequency_days": "90 (CISCO default)",
                "report_on_change_days": "90 (CISCO default)"
            },
            "enforced_perpetual_subscription_license_attributes": {
                "first_report_requirement_days": "0 (CISCO default)",
                "reporting_frequency_days": "0 (CISCO default)",
                "report_on_change_days": "0 (CISCO default)"
            },
            "export_perpetual_subscription_license_attributes": {
                "first_report_requirement_days": "0 (CISCO default)",
                "reporting_frequency_days": "0 (CISCO default)",
                "report_on_change_days": "0 (CISCO default)"
            }
        },
        "usage_reporting": {
            "last_ack_received": "<none>",
            "next_ack_deadline": "Jun 17 15:04:29 2025 IST",
            "reporting_push_interval": "30  days State(2) InPolicy(90)",
            "next_ack_push_check": "<none>",
            "next_report_push": "Mar 19 15:06:29 2025 IST",
            "last_report_push": "<none>",
            "last_report_file_write": "<none>"
        },
        "trust_code_installed": "<none>"
    },
    "license_usage": {
        "handle": {
            2: {
                "license": "network-advantage",
                "entitlement_tag": "regid.2017-03.com.cisco.advantagek9-Nyquist-C9500,1.0_f1563759-2e03-4a4c-bec5-5feec525a12c",
                "description": "C9500 Network Advantage",
                "count": 2,
                "version": "1.0",
                "status": "IN USE(15)",
                "authorized_count": 0,
                "outofcompliance_count": 0,
                "insufficient_count": 0,
                "no_license": 0,
                "status_time": "Mar 19 15:03:39 2025 IST",
                "request_time": "Mar 19 15:04:26 2025 IST",
                "export_status": "NOT RESTRICTED",
                "feature_name": "network-advantage",
                "feature_description": "C9500 Network Advantage",
                "enforcement_type": "NOT ENFORCED",
                "day0_verification": "NO",
                "license_type": "Perpetual",
                "measurements": {
                    "entitlement": {
                        "interval": "00:15:00",
                        "current_value": 2,
                        "current_report": 1742378619,
                        "previous": 1742378617
                    }
                },
                "soft_enforced": "True"
            },
            3: {
                "license": "dna-advantage",
                "entitlement_tag": "regid.2018-01.com.cisco.C9500-DNA-32QC-A,1.0_1fd2bf73-201e-472b-a287-65f23ec80f3e",
                "description": "C9500-32QC DNA Advantage",
                "count": 2,
                "version": "1.0",
                "status": "IN USE(15)",
                "authorized_count": 0,
                "outofcompliance_count": 0,
                "insufficient_count": 0,
                "no_license": 0,
                "status_time": "Mar 19 15:03:39 2025 IST",
                "request_time": "Mar 19 15:04:26 2025 IST",
                "export_status": "NOT RESTRICTED",
                "feature_name": "dna-advantage",
                "feature_description": "C9500-32QC DNA Advantage",
                "enforcement_type": "NOT ENFORCED",
                "day0_verification": "NO",
                "license_type": "Subscription",
                "measurements": {
                    "entitlement": {
                        "interval": "00:15:00",
                        "current_value": 2,
                        "current_report": 1742378620,
                        "previous": 1742378618
                    }
                },
                "soft_enforced": "True"
            },
            4: {
                "license": "cisco-wireless-advantage",
                "entitlement_tag": "regid.2024-08.com.cisco.CNS_CW_A,1.0_5c973b43-3728-4489-9c45-42197a411835",
                "description": "cisco-wireless-advantage",
                "count": 0,
                "version": "1.0",
                "status": "NOT IN USE(1)",
                "status_time": "Mar 19 15:03:45 2025 IST",
                "request_time": "None",
                "export_status": "NOT RESTRICTED",
                "feature_name": "cisco-wireless-advantage",
                "feature_description": "cisco-wireless-advantage",
                "enforcement_type": "NOT ENFORCED",
                "day0_verification": "NO",
                "license_type": "Subscription",
                "measurements": {
                    "entitlement": {
                        "interval": "00:15:00",
                        "current_value": 0,
                        "current_report": 0,
                        "previous": 0
                    }
                },
                "soft_enforced": "True"
            }
        }
    },
    "product_information": {
        "udi": {
            "pid": "C9500-32QC",
            "sn": "CAT2209L0KS"
        },
        "ha_udi_list": {
            "active": {
                "pid": "C9500-32QC",
                "sn": "CAT2209L0KS"
            },
            "standby": {
                "pid": "C9500-32QC",
                "sn": "CAT2210L3GH"
            }
        }
    },
    "agent_version": {
        "smart_agent_for_licensing": "6.3.7/b37215cd0"
    },
    "upcoming_scheduled_jobs": {
        "current_time": "Mar 19 15:08:49 2025 IST",
        "daily": "Mar 20 15:03:41 2025 IST (23 hours, 54 minutes, 52 seconds remaining)",
        "init_flag_check": "Expired Not Rescheduled",
        "reservation_configuration_mismatch_between_nodes_in_ha_mode": "Expired Not Rescheduled",
        "start_utility_measurements": "Mar 19 15:22:41 2025 IST (13 minutes, 52 seconds remaining)",
        "send_utility_rum_reports": "Mar 20 15:05:38 2025 IST (23 hours, 56 minutes, 49 seconds remaining)",
        "save_unreported_rum_reports": "Mar 19 16:08:11 2025 IST (59 minutes, 22 seconds remaining)",
        "process_utility_rum_reports": "Mar 20 15:04:29 2025 IST (23 hours, 55 minutes, 40 seconds remaining)",
        "data_synchronization": "Expired Not Rescheduled",
        "external_event": "Mar 19 15:09:18 2025 IST (29 seconds remaining)",
        "operational_model": "Expired Not Rescheduled"
    },
    "communication_statistics": {
        "communication_level_allowed": "INDIRECT",
        "overall_state": "Device configured for Offline transport",
        "trust_establishment": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "trust_acknowledgement": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "usage_reporting": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "result_polling": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "authorization_request": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "authorization_confirmation": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "authorization_return": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "trust_sync": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        },
        "hello_message": {
            "attempts": "Total=0, Success=0, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "<none>",
            "failure_reason": "<none>",
            "last_success_time": "<none>",
            "last_failure_time": "<none>"
        }
    },
    "license_certificates": {
        "production_cert": "True"
    },
    "ha_info": {
        "rp_role": "Active",
        "chassis_role": "Active",
        "behavior_role": "Active",
        "rmf": "True",
        "cf": "True",
        "cf_state": "Stateless",
        "message_flow_allowed": "False"
    },
    "reservation_info": {
        "license_reservation": "DISABLED",
        "last_data_push": "<none>",
        "last_file_export": "<none>",
        "overall_status": {
            "active": {
                "pid": "C9500-32QC",
                "sn": "CAT2209L0KS",
                "reservation_status": "NOT INSTALLED",
                "request_code": "<none>",
                "last_return_code": "<none>",
                "last_confirmation_code": "<none>",
                "reservation_authorization_code": "<none>"
            },
            "standby": {
                "pid": "C9500-32QC",
                "sn": "CAT2210L3GH",
                "reservation_status": "NOT INSTALLED",
                "request_code": "<none>",
                "last_return_code": "<none>",
                "last_confirmation_code": "<none>",
                "reservation_authorization_code": "<none>"
            }
        },
        "purchased_licenses": "No Purchase Information Available"
    },
    "usage_report_summary": {
        "total": 6,
        "purged": "0(0)",
        "total_acknowledged_received": 0,
        "waiting_for_ack": "0(6)",
        "available_to_report": 6,
        "collecting_data": 2,
        "maximum_display": 6,
        "in_storage": 6,
        "mia": "0(0)",
        "report_module_status": "Ready"
    },
    "product_analytics_report_summary": {
        "product_analytics": "AVAILABLE",
        "not_available_reason": "<empty>",
        "total_current_product_analytics_reports": 0
    },
    "other_info": {
        "software_id": "regid.2017-05.com.cisco.C9500,v1_7435cf27-0075-4bfb-b67c-b42f3054e82a",
        "agent_state": "authorized",
        "ts_enable": "True",
        "transport": "Smart",
        "default_url": "https://smartreceiver.cisco.com/licservice/license",
        "locale": "en_US.UTF-8",
        "debug_flags": "0x7",
        "privacy_send_hostname": "True",
        "privacy_send_ip": "True",
        "build_type": "Production",
        "sizeof_char": 1,
        "sizeof_int": 4,
        "sizeof_long": 4,
        "sizeof_char_*": 8,
        "sizeof_time_t": 4,
        "sizeof_size_t": 8,
        "endian": "Big",
        "write_erase_occurred": "False",
        "xos_version": "0.12.0.0",
        "config_persist_received": "False",
        "message_version": "1.3",
        "connect_info_name": "<empty>",
        "connect_info_version": "<empty>",
        "connect_info_additional": "<empty>",
        "connect_info_prod": "False",
        "connect_info_capabilities": "<empty>",
        "agent_capabilities": "UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE, TELEMETRY, PRODUCT-ANALYTICS, TELEMETRY_POLICY",
        "check_point_interface": "True",
        "config_management_interface": "False",
        "license_map_interface": "True",
        "ha_interface": "True",
        "trusted_store_interface": "True",
        "platform_data_interface": "True",
        "crypto_version_2_interface": "False",
        "sapluginmgmtinterfacemutex": "True",
        "sapluginmgmtipdomainname": "True",
        "smarttransportvrfsupport": "True",
        "smartagentclientwaitforserver": 2000,
        "smartagentcmretrysend": "True",
        "smartagentclientisunified": "True",
        "smartagentcmclient": "True",
        "smartagentclientname": "UnifiedClient",
        "builtinencryption": "True",
        "enableoninit": "True",
        "routingreadybyevent": "True",
        "systeminitbyevent": "True",
        "smarttransportserveridcheck": "True",
        "smarttransportproxysupport": "True",
        "smartagentmaxermnotifylistsize": 6000,
        "smartagentday0enforcement": "False",
        "smartagentunifiedlicensing": "False",
        "smartagentslpenhanced": "False",
        "smartagentpurgeallreports": "False",
        "trustpointenrollmentonboot": "False",
        "smartagentmaxsinglereportsize": 0,
        "smartagentslacreturnforcedallowed": "False",
        "smartagentcompliancestatus": "False",
        "smartagenttelemetryrumreportmax": 600,
        "smartagentrumtelemetryrumstoremin": 500,
        "smartagentpolicydisplayformat": 0,
        "smartagentreportonupgrade": "False",
        "smartagentindividualrumencrypt": 2,
        "smartagentmaxrummemory": 50,
        "smartagentconcurrentthreadmax": 10,
        "smartagentpolicycontrollermodel": "False",
        "smartagentdisablecacheswid": "False",
        "smartagentpolicymodel": "True",
        "smartagentfederallicense": "True",
        "smartagentmultitenant": "False",
        "attr365dayevalsyslog": "True",
        "checkpointwriteonly": "False",
        "smartagentdelaycertvalidation": "False",
        "enablebydefault": "False",
        "conversionautomatic": "False",
        "conversionallowed": "False",
        "storageencryptdisable": "False",
        "storageloadunencrypteddisable": "False",
        "tsplugindisable": "False",
        "bypassudicheck": "False",
        "loggingaddtstamp": "False",
        "loggingaddtid": "True",
        "highavailabilityoverrideevent": "UnknownPlatformEvent",
        "platformindependentoverrideevent": "UnknownPlatformEvent",
        "platformoverrideevent": "SmartAgentSystemDataListChanged",
        "waitforharole": "False",
        "standbyishot": "True",
        "chkpttype": 2,
        "delaycomminit": "False",
        "rolebyevent": "True",
        "maxtracelength": 150,
        "tracealwayson": "True",
        "debugflags": 0,
        "event_log_max_size": "5120 KB",
        "event_log_current_size": "1 KB",
        "trust_data": {
            "cat2209l0ks": {
                "p": "C9500-32QC",
                "trustvalue": "No Trust Data"
            },
            "cat2210l3gh": {
                "p": "C9500-32QC",
                "trustvalue": "No Trust Data"
            }
        },
        "overall_trust": "No ID",
        "clock_synced_with_ntp": "True"
    },
    "platform_provided_mapping_table": {
        "pid": "C9500-32QC",
        "total_licenses_found": 224,
        "enforced_licenses": {
            "cat2209l0ks": {
                "pid": "C9500-32QC"
            },
            "cat2210l3gh": {
                "pid": "C9500-32QC"
            }
        }
    }
}
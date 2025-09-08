expected_output = {
    "primary_load_time_percent": 1,
    "secondary_load_time_percent": 0,
    "one_minute_load_percent": 4,
    "five_minute_load_percent": 3,
    "ntp_time": "05:02:23.993 UTC Tue Apr 22 2025",
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
            "smart_account": "BU Production Test As of Apr 22 05:02:11 2025 UTC",
            "virtual_account": "Starfleet"
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
            "policy_in_use": "Installed On Apr 22 05:01:33 2025 UTC",
            "policy_name": "SLE Policy",
            "reporting_ack_required": "yes (Customer Policy)",
            "unenforced_non_export_perpetual_attributes": {
                "first_report_requirement_days": "30 (Customer Policy)",
                "reporting_frequency_days": "60 (Customer Policy)",
                "report_on_change_days": "60 (Customer Policy)"
            },
            "unenforced_non_export_subscription_attributes": {
                "first_report_requirement_days": "120 (Customer Policy)",
                "reporting_frequency_days": "111 (Customer Policy)",
                "report_on_change_days": "111 (Customer Policy)"
            },
            "enforced_perpetual_subscription_license_attributes": {
                "first_report_requirement_days": "30 (Customer Policy)",
                "reporting_frequency_days": "90 (Customer Policy)",
                "report_on_change_days": "60 (Customer Policy)"
            },
            "export_perpetual_subscription_license_attributes": {
                "first_report_requirement_days": "30 (Customer Policy)",
                "reporting_frequency_days": "30 (Customer Policy)",
                "report_on_change_days": "30 (Customer Policy)"
            }
        },
        "usage_reporting": {
            "last_ack_received": "Apr 22 05:01:33 2025 UTC",
            "next_ack_deadline": "May 22 05:01:34 2025 UTC",
            "reporting_push_interval": "30  days State(2) InPolicy(30)",
            "next_ack_push_check": "<none>",
            "next_report_push": "Apr 22 05:02:02 2025 UTC",
            "last_report_push": "<none>",
            "last_report_file_write": "<none>"
        },
        "trust_code_installed": {
            "attributes": "<none>",
            "active": {
                "pid": "C9500-32QC",
                "sn": "CAT2209L0KS",
                "info": "INSTALLED on Apr 22 05:01:33 2025 UTC    Valid on Apr 22 04:56:31 2025 UTC",
                "expired_on_jan_01_00": "00:00 1970 UTC",
                "trust_code_type": "CSSM",
                "attributes": "<none>"
            },
            "standby": {
                "pid": "C9500-32QC",
                "sn": "CAT2210L3GH",
                "info": "INSTALLED on Apr 22 05:01:33 2025 UTC    Valid on Apr 22 04:56:32 2025 UTC",
                "expired_on_jan_01_00": "00:00 1970 UTC",
                "trust_code_type": "CSSM",
                "attributes": "<none>"
            }
        }
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
                "status_time": "Apr 22 04:53:59 2025 UTC",
                "request_time": "Apr 22 04:54:41 2025 UTC",
                "export_status": "NOT RESTRICTED",
                "feature_name": "network-advantage",
                "feature_description": "C9500 Network Advantage",
                "enforcement_type": "NOT ENFORCED",
                "license_type": "Perpetual",
                "measurements": {
                    "entitlement": {
                        "interval": "00:15:00",
                        "current_value": 2,
                        "current_report": 1745297635,
                        "previous": 0
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
                "status_time": "Apr 22 04:53:59 2025 UTC",
                "request_time": "Apr 22 04:54:41 2025 UTC",
                "export_status": "NOT RESTRICTED",
                "feature_name": "dna-advantage",
                "feature_description": "C9500-32QC DNA Advantage",
                "enforcement_type": "NOT ENFORCED",
                "license_type": "Subscription",
                "measurements": {
                    "entitlement": {
                        "interval": "00:15:00",
                        "current_value": 2,
                        "current_report": 1745297636,
                        "previous": 0
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
                "status_time": "Apr 22 04:54:06 2025 UTC",
                "request_time": "None",
                "export_status": "NOT RESTRICTED",
                "feature_name": "cisco-wireless-advantage",
                "feature_description": "cisco-wireless-advantage",
                "enforcement_type": "NOT ENFORCED",
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
        "smart_agent_for_licensing": "6.3.10/58086906e"
    },
    "upcoming_scheduled_jobs": {
        "current_time": "Apr 22 05:02:24 2025 UTC",
        "daily": "Apr 23 04:54:02 2025 UTC (23 hours, 51 minutes, 38 seconds remaining)",
        "init_flag_check": "Not Available",
        "register_period_expiration_check": "Expired Not Rescheduled",
        "ack_expiration_check": "Expired Not Rescheduled",
        "reservation_configuration_mismatch_between_nodes_in_ha_mode": "Expired Not Rescheduled",
        "start_utility_measurements": "Apr 22 05:15:03 2025 UTC (12 minutes, 39 seconds remaining)",
        "send_utility_rum_reports": "Apr 22 05:03:01 2025 UTC (37 seconds remaining)",
        "save_unreported_rum_reports": "Apr 22 06:00:35 2025 UTC (58 minutes, 11 seconds remaining)",
        "process_utility_rum_reports": "Apr 23 05:00:02 2025 UTC (23 hours, 57 minutes, 38 seconds remaining)",
        "authorization_code_process": "Apr 22 05:02:42 2025 UTC (18 seconds remaining)",
        "data_synchronization": "Expired Not Rescheduled",
        "external_event": "Apr 22 05:03:12 2025 UTC (48 seconds remaining)",
        "operational_model": "Expired Not Rescheduled"
    },
    "communication_statistics": {
        "communication_level_allowed": "DIRECT",
        "overall_state": "<empty>",
        "trust_establishment": {
            "attempts": "Total=1, Success=1, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "OK on Apr 22 05:01:33 2025 UTC",
            "failure_reason": "<none>",
            "last_success_time": "Apr 22 05:01:33 2025 UTC",
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
            "attempts": "Total=1, Success=1, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "NO DATA TO PROCESS",
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
            "attempts": "Total=1, Success=1, Fail=0",
            "ongoing_failure": "Overall=0 Communication=0",
            "last_response": "OK on Apr 22 05:02:12 2025 UTC",
            "failure_reason": "<none>",
            "last_success_time": "Apr 22 05:02:12 2025 UTC",
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
        "total": 2,
        "purged": "0(0)",
        "total_acknowledged_received": 0,
        "waiting_for_ack": "0(2)",
        "available_to_report": 2,
        "collecting_data": 2,
        "maximum_display": 2,
        "in_storage": 2,
        "mia": "0(0)",
        "report_module_status": "Ready"
    },
    "product_analytics_report_summary": {
        "product_analytics": "NOT AVAILABLE",
        "not_available_reason": "Smart license channel not established",
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
        "config_persist_received": "True",
        "message_version": "1.3",
        "connect_info_name": "SSM",
        "connect_info_version": "1.3",
        "connect_info_prod": "True",
        "connect_info_capabilities": "DLC, AppHA, EXPORT_2, POLICY_USAGE, UTILITY, TELEMETRY_POLICY",
        "agent_capabilities": "UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE, PRODUCT-ANALYTICS, TELEMETRY_POLICY",
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
        "smartagentdelaycertvalidation": "True",
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
                "trustid": 552
            },
            "cat2210l3gh": {
                "p": "C9500-32QC",
                "trustid": 582
            }
        },
        "overall_trust": "INSTALLED (2)",
        "clock_synced_with_ntp": "True"
    },
    "platform_provided_mapping_table": {
        "pid": "C9500-32QC",
        "total_licenses_found": 221,
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

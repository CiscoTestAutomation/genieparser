expected_output = {
    'smart_licensing_status': {
        'license_conversion': {
            'automatic_conversion_enabled': 'False',
            'last_data_push': '<none>',
            'last_file_export': '<none>'
        },
        'export_authorization_key': {
            'features_authorized': 'none'
        },
        'utility': {
            'status': 'DISABLED'
        },
        'smart_licensing_using_policy': {
            'status': 'ENABLED',
            'reporting_mode': 'STANDARD'
        },
        'account_information': {
            'smart_account': 'BU Production Test As of Mar 15 21:01:33 2024 UTC',
            'virtual_account': 'Cat9K-FranklinDT'
        },
        'data_privacy': {
            'sending_hostname': 'yes',
            'callhome_hostname_privacy': 'DISABLED',
            'smart_licensing_hostname_privacy': 'DISABLED',
            'version_privacy': 'DISABLED'
        },
        'transport': {
            'type': 'Smart',
            'url': 'https://smartreceiver.cisco.com/licservice/license',
            'proxy': {
                'address': '173.36.224.109',
                'port': 80,
                'username': '<empty>',
                'password': '<empty>'
            },
            'server_identity_check': 'True',
            'vrf': '<empty>'
        },
        'miscellaneous': {
            'custom_id': '<empty>'
        },
        'policy': {
            'policy_in_use': 'Installed On Mar 13 21:32:51 2024 UTC',
            'policy_name': 'SLE Policy',
            'reporting_ack_required': 'yes (Customer Policy)',
            'unenforced_non_export_perpetual_attributes': {
                'first_report_requirement_days': '30 (Customer Policy)',
                'reporting_frequency_days': '60 (Customer Policy)',
                'report_on_change_days': '60 (Customer Policy)'
            },
            'unenforced_non_export_subscription_attributes': {
                'first_report_requirement_days': '120 (Customer Policy)',
                'reporting_frequency_days': '111 (Customer Policy)',
                'report_on_change_days': '111 (Customer Policy)'
            },
            'enforced_perpetual_subscription_license_attributes': {
                'first_report_requirement_days': '30 (Customer Policy)',
                'reporting_frequency_days': '90 (Customer Policy)',
                'report_on_change_days': '60 (Customer Policy)'
            },
            'export_perpetual_subscription_license_attributes': {
                'first_report_requirement_days': '30 (Customer Policy)',
                'reporting_frequency_days': '30 (Customer Policy)',
                'report_on_change_days': '30 (Customer Policy)'
            }
        },
        'usage_reporting': {
            'last_ack_received': 'Mar 15 21:01:43 2024 UTC',
            'next_ack_deadline': 'May 14 21:01:43 2024 UTC',
            'reporting_push_interval': '30  days State(4) InPolicy(60)',
            'next_ack_push_check': 'Mar 15 22:32:55 2024 UTC',
            'next_report_push': 'Apr 13 22:27:41 2024 UTC',
            'last_report_push': 'Mar 14 22:27:41 2024 UTC',
            'last_report_file_write': '<none>'
        },
        'trust_code_installed': {
            'active': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8X0',
                'info': 'INSTALLED on Mar 13 21:32:51 2024 UTC'
            },
            'standby': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8XF',
                'info': 'INSTALLED on Mar 13 21:32:52 2024 UTC'
            },
            'member': {
                'pid': 'C9350-24U',
                'sn': 'FOC2718Y66X',
                'info': 'INSTALLED on Mar 13 21:32:52 2024 UTC'
            },
            'member2': {
                'pid': 'C9350-24U',
                'sn': 'FOC2719YOHR',
                'info': 'INSTALLED on Mar 13 21:32:52 2024 UTC'
            }
        }
    },
    'license_usage': {
        'handle': {
            1: {
                'license': 'network-advantage',
                'entitlement_tag': 'regid.2023-08.com.cisco.C9350_24P_NW_A,1.0_bf84bdef-3f01-416a-a619-4d98efbbede1',
                    'description': 'C9350-24 Catalyst Network Advantage',
                    'count': 4,
                    'version': '1.0',
                    'status': 'IN USE(15)',
                    'status_time': 'Mar 13 22:26:20 2024 UTC',
                    'request_time': 'Mar 13 22:26:40 2024 UTC',
                    'export_status': 'NOT RESTRICTED',
                    'feature_name': 'network-advantage',
                    'feature_description': 'C9350-24 Catalyst Network Advantage',
                    'enforcement_type': 'NOT ENFORCED',
                    'license_type': 'Perpetual',
                    'measurements': {
                        'entitlement': {
                            'interval': '00:15:00',
                            'current_value': 4,
                            'current_report': 1710279003,
                            'previous': 1710279001
                    }
                },
                'soft_enforced': 'True'
            },
            2: {
                'license': 'dna-advantage',
                'entitlement_tag': 'regid.2023-08.com.cisco.C9350_24P_DNX_A,1.0_e0fef355-0393-4db8-ae2e-2013b1ff759c',
                 'description': 'C9350-24 Catalyst Software Subscription Advantage',
                 'count': 4, 'version': '1.0', 'status': 'IN USE(15)',
                 'status_time': 'Mar 13 22:26:20 2024 UTC',
                 'request_time': 'Mar 13 22:26:40 2024 UTC',
                 'export_status': 'NOT RESTRICTED',
                 'feature_name': 'dna-advantage',
                 'feature_description': 'C9350-24 Catalyst Software Subscription Advantage',
                 'enforcement_type': 'NOT ENFORCED',
                 'license_type': 'Subscription',
                 'measurements': {
                     'entitlement': {
                        'interval': '00:15:00',
                        'current_value': 4,
                        'current_report': 1710279004,
                        'previous': 1710279002
                    }
                },
                'soft_enforced': 'True'
            }
        }
    },
    'product_information': {
        'udi': {
            'pid': 'C9350-24U',
            'sn': 'FOC2705Y8X0'
        },
        'ha_udi_list': {
            'active': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8X0'
            },
            'standby': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8XF'
            },
            'member': {
                'pid': 'C9350-24U',
                'sn': 'FOC2718Y66X'
            },
            'member2': {
                'pid': 'C9350-24U',
                'sn': 'FOC2719YOHR'
            }
        }
    },
    'agent_version': {
        'smart_agent_for_licensing': '5.11.4_rel/20'
    },
    'upcoming_scheduled_jobs': {
        'current_time': 'Mar 15 21:13:41 2024 UTC',
        'daily': 'Mar 15 22:26:22 2024 UTC (1 hours, 12 minutes, 41 seconds remaining)',
        'init_flag_check': 'Expired Not Rescheduled',
        'reservation_configuration_mismatch_between_nodes_in_ha_mode': 'Mar 15 21:14:04 2024 UTC (23 seconds remaining)',
        'retrieve_data_processing_result': 'Mar 15 22:32:55 2024 UTC (1 hours, 19 minutes, 14 seconds remaining)',
        'start_utility_measurements': 'Mar 15 21:28:35 2024 UTC (14 minutes, 54 seconds remaining)',
        'send_utility_rum_reports': 'Apr 13 22:27:40 2024 UTC (29 days, 1 hours, 13 minutes, 59 seconds remaining)',
        'save_unreported_rum_reports': 'Mar 15 21:13:46 2024 UTC (5 seconds remaining)',
        'process_utility_rum_reports': 'Mar 15 22:37:13 2024 UTC (1 hours, 23 minutes, 32 seconds remaining)',
        'telemetry_reporting': 'Expired Not Rescheduled',
        'authorization_code_process': 'Expired Not Rescheduled',
        'data_synchronization': 'Expired Not Rescheduled',
        'external_event': 'Mar 15 21:13:49 2024 UTC (8 seconds remaining)',
        'operational_model': 'Mar 15 21:13:41 2024 UTC  (Expired)'
    },
    'communication_statistics': {
        'communication_level_allowed': 'DIRECT', 'overall_state': '<empty>',
        'trust_establishment': {
            'attempts': 'Total=0, Success=0, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': '<none>',
            'failure_reason': '<none>',
            'last_success_time': '<none>',
            'last_failure_time': '<none>'
        },
        'trust_acknowledgement': {
            'attempts': 'Total=0, Success=0, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': '<none>',
            'failure_reason': '<none>',
            'last_success_time': '<none>',
            'last_failure_time': '<none>'
        }, 'usage_reporting': {
            'attempts': 'Total=2, Success=2, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': 'OK_POLL on Mar 14 22:27:35 2024 UTC',
            'failure_reason': '<none>',
            'last_success_time': 'Mar 14 22:27:35 2024 UTC',
            'last_failure_time': '<none>'
        }, 'result_polling': {
            'attempts': 'Total=4, Success=3, Fail=1',
            'ongoing_failure': 'Overall=1 Communication=1',
            'last_response': 'NO REPLY on Mar 14 22:32:55 2024 UTC',
            'failure_reason': '<none>',
            'last_success_time': 'Mar 13 22:32:13 2024 UTC',
            'last_failure_time': 'Mar 14 22:32:55 2024 UTC'
        },
        'authorization_request': {
            'attempts': 'Total=236, Success=236, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': 'NO DATA TO PROCESS',
            'failure_reason': '<none>',
            'last_success_time': '<none>',
            'last_failure_time': '<none>'
        }, 'authorization_confirmation': {
                'attempts': 'Total=0, Success=0, Fail=0',
                'ongoing_failure': 'Overall=0 Communication=0',
                'last_response': '<none>',
                'failure_reason': '<none>',
                'last_success_time': '<none>',
                'last_failure_time': '<none>'
        },
        'authorization_return': {
            'attempts': 'Total=0, Success=0, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': '<none>',
            'failure_reason': '<none>',
            'last_success_time': '<none>',
            'last_failure_time': '<none>'
        },
        'trust_sync': {
            'attempts': 'Total=344, Success=154, Fail=190',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': 'OK on Mar 15 21:01:43 2024 UTC',
            'failure_reason': '<none>',
            'last_success_time': 'Mar 15 21:01:43 2024 UTC',
            'last_failure_time': 'Mar 15 20:48:32 2024 UTC'
        },
        'hello_message': {
            'attempts': 'Total=0, Success=0, Fail=0',
            'ongoing_failure': 'Overall=0 Communication=0',
            'last_response': '<none>',
            'failure_reason': '<none>',
            'last_success_time': '<none>',
            'last_failure_time': '<none>'
        }
    },
    'license_certificates': {
        'production_cert': 'True'
    },
    'ha_info': {
        'rp_role': 'Active',
        'chassis_role': 'Active',
        'behavior_role': 'Active',
        'rmf': 'True',
        'cf': 'True',
        'cf_state': 'Stateless',
        'message_flow_allowed': 'False'
    },
    'reservation_info': {
        'license_reservation': 'DISABLED',
        'last_data_push': '<none>',
        'last_file_export': '<none>',
        'overall_status': {
            'active': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8X0',
                'reservation_status': 'NOT INSTALLED',
                'request_code': '<none>',
                'last_return_code': '<none>',
                'last_confirmation_code': '<none>',
                'reservation_authorization_code': '<none>'
            },
            'standby': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8XF',
                'reservation_status': 'NOT INSTALLED',
                'request_code': '<none>',
                'last_return_code': '<none>',
                'last_confirmation_code': '<none>',
                'reservation_authorization_code': '<none>'
            },
            'member': {
                'pid': 'C9350-24U',
                'sn': 'FOC2718Y66X',
                'reservation_status': 'NOT INSTALLED',
                'request_code': '<none>',
                'last_return_code': '<none>',
                'last_confirmation_code': '<none>',
                'reservation_authorization_code': '<none>'
            },
            'member2': {
                'pid': 'C9350-24U',
                'sn': 'FOC2719YOHR',
                'reservation_status': 'NOT INSTALLED',
                'request_code': '<none>',
                'last_return_code': '<none>',
                'last_confirmation_code': '<none>',
                'reservation_authorization_code': '<none>'
            }
        },
        'purchased_licenses': 'No Purchase Information Available'
    },
    'usage_report_summary': {
        'total': 707,
        'purged': '390(390)',
        'total_acknowledged_received': 0,
        'waiting_for_ack': '0(300)',
        'available_to_report': 300,
        'collecting_data': 2,
        'maximum_display': 300,
        'in_storage': 300,
        'mia': '0(0)',
        'report_module_status': 'Ready'
    },
    'device_telemetry_report_summary': {
        'data_channel': 'AVAILABLE',
        'reports_on_disk': 0
    },
    'other_info': {
        'software_id': 'regid.2023-08.com.cisco.C9350,1.0_e4e8bce9-f207-473c-a7c1-7091d8c83b9f',
        'agent_state': 'authorized',
        'ts_enable': 'True',
        'transport': 'Smart',
        'default_url': 'https://smartreceiver.cisco.com/licservice/license',
        'locale': 'en_US.UTF-8',
        'debug_flags': '0x7',
        'privacy_send_hostname': 'True',
        'privacy_send_ip': 'True',
        'build_type': 'Production',
        'sizeof_char': 1,
        'sizeof_int': 4,
        'sizeof_long': 4,
        'sizeof_char_*': 8,
        'sizeof_time_t': 4,
        'sizeof_size_t': 8,
        'endian': 'Big',
        'write_erase_occurred': 'False',
        'xos_version': '0.12.0.0',
        'config_persist_received': 'False',
        'message_version': '1.3',
        'connect_info_name': 'SSM',
        'connect_info_version': '1.3',
        'connect_info_prod': 'True',
        'connect_info_capabilities': 'DLC, AppHA, EXPORT_2, POLICY_USAGE, UTILITY, TELEMETRY, TELEMETRY_POLICY',
        'agent_capabilities': 'UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE, TELEMETRY, TELEMETRY_POLICY',
        'check_point_interface': 'True',
        'config_management_interface': 'False',
        'license_map_interface': 'True',
        'ha_interface': 'True',
        'trusted_store_interface': 'True',
        'platform_data_interface': 'True',
        'crypto_version_2_interface': 'False',
        'sapluginmgmtinterfacemutex': 'True',
        'sapluginmgmtipdomainname': 'True',
        'smarttransportvrfsupport': 'True',
        'smartagentclientwaitforserver': 2000,
        'smartagentcmretrysend': 'True',
        'smartagentclientisunified': 'True',
        'smartagentcmclient': 'True',
        'smartagentclientname': 'UnifiedClient',
        'builtinencryption': 'True',
        'enableoninit': 'True',
        'routingreadybyevent': 'True',
        'systeminitbyevent': 'True',
        'smarttransportserveridcheck': 'True',
        'smarttransportproxysupport': 'True',
        'smartagentmaxsinglereportsize': 40,
        'smartagentslacreturnforcedallowed': 'False',
        'smartagentcompliancestatus': 'False',
        'smartagenttelemetryrumreportmax': 600,
        'smartagentrumtelemetryrumstoremin': 500,
        'smartagentpolicydisplayformat': 0,
        'smartagentreportonupgrade': 'False',
        'smartagentindividualrumencrypt': 2,
        'smartagentmaxrummemory': 50,
        'smartagentconcurrentthreadmax': 10,
        'smartagentpolicycontrollermodel': 'False',
        'smartagentdisablecacheswid': 'False',
        'smartagentpolicymodel': 'True',
        'smartagentfederallicense': 'True',
        'smartagentmultitenant': 'False',
        'attr365dayevalsyslog': 'True',
        'checkpointwriteonly': 'False',
        'smartagentdelaycertvalidation': 'False',
        'enablebydefault': 'False',
        'conversionautomatic': 'False',
        'conversionallowed': 'False',
        'storageencryptdisable': 'False',
        'storageloadunencrypteddisable': 'False',
        'tsplugindisable': 'False',
        'bypassudicheck': 'False',
        'loggingaddtstamp': 'False',
        'loggingaddtid': 'True',
        'highavailabilityoverrideevent': 'UnknownPlatformEvent',
        'platformindependentoverrideevent': 'UnknownPlatformEvent',
        'platformoverrideevent': 'SmartAgentSystemDataListChanged',
        'waitforharole': 'False',
        'standbyishot': 'True',
        'chkpttype': 2,
        'delaycomminit': 'False',
        'rolebyevent': 'True',
        'maxtracelength': 150,
        'tracealwayson': 'True',
        'debugflags': 0,
        'event_log_max_size': '5120 KB',
        'event_log_current_size': '3489 KB',
        'trust_data': {
            'foc2705y8x0': {
                'p': 'C9350-24U',
                'trustid': 318
            },
            'foc2705y8xf': {
                'p': 'C9350-24U',
                'trustid': 929
            },
            'foc2718y66x': {
                'p': 'C9350-24U',
                'trustid': 996
            },
            'foc2719yohr': {
                'p': 'C9350-24U',
                'trustid': 19
            }
        },
        'overall_trust': 'INSTALLED (2)',
        'clock_synced_with_ntp': 'False'
    },
    'platform_provided_mapping_table': {
        'pid': 'C9350-24U',
        'total_licenses_found': 213,
        'enforced_licenses': {
            'foc2705y8x0': {
                'pid': 'C9350-24U',
                'hseck9_entitlement_tag': 'regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2',
                'hseck9_no': 3
            },
            'foc2705y8xf': {
                'pid': 'C9350-24U',
                'hseck9_entitlement_tag': 'regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2',
                'hseck9_no': 3
            },
            'foc2718y66x': {
                'pid': 'C9350-24U',
                'hseck9_entitlement_tag': 'regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2',
                'hseck9_no': 3
            },
            'foc2719yohr': {
                'pid': 'C9350-24U',
                'hseck9_entitlement_tag': 'regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2',
                'hseck9_no': 3
            }
        }
    }
}
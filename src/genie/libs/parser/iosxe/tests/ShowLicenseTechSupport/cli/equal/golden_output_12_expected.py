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
      'smart_account': 'BU Production Test As of Dec 18 11:02:51 2023 PDT',
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
      'policy_in_use': 'Installed On Oct 24 15:07:43 2023 PDT',
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
      'last_ack_received': 'Dec 18 11:05:11 2023 PDT',
      'next_ack_deadline': 'Feb 16 11:05:11 2024 PDT',
      'reporting_push_interval': '30  days State(4) InPolicy(60)',
      'next_ack_push_check': '<none>',
      'next_report_push': 'Jan 17 11:00:18 2024 PDT',
      'last_report_push': 'Dec 18 11:00:18 2023 PDT',
      'last_report_file_write': '<none>'
    },
    'trust_code_installed': {
      'active': {
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7',
        'info': 'INSTALLED on Nov 22 11:34:47 2023 PDT'
      },
      'standby': {
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7',
        'info': 'INSTALLED on Nov 22 11:34:47 2023 PDT'
      }
    }
  },
  'license_usage': {
    'handle': {
      1: {
        'license': 'network-advantage',
        'entitlement_tag': 'regid.2017-05.com.cisco.advantagek9-C9400,1.0_61a546cd-1037-47cb-bbe6-7cad3217a7b3',
        'description': 'C9400 Network Advantage',
        'count': 2,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Dec 18 10:58:10 2023 PDT',
        'request_time': 'Dec 18 10:58:49 2023 PDT',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'network-advantage',
        'feature_description': 'C9400 Network Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Perpetual',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 2,
            'current_report': 1698184615,
            'previous': 1698184613
          }
        },
        'soft_enforced': 'True'
      },
      2: {
        'license': 'dna-advantage',
        'entitlement_tag': 'regid.2017-05.com.cisco.dna_advantage-C9400,1.0_6e77dbc1-0da3-466c-8414-97c8ee4d48ce',
        'description': 'C9400 DNA Advantage',
        'count': 1,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Dec 18 10:58:10 2023 PDT',
        'request_time': 'Dec 18 10:58:10 2023 PDT',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'dna-advantage',
        'feature_description': 'C9400 DNA Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Subscription',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 1,
            'current_report': 1698184616,
            'previous': 1698184614
          }
        },
        'soft_enforced': 'True'
      }
    }
  },
  'product_information': {
    'udi': {
      'pid': 'C9407R',
      'sn': 'FXS2119Q2U7'
    },
    'ha_udi_list': {
      'active': {
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7'
      },
      'standby': {
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7'
      }
    }
  },
  'agent_version': {
    'smart_agent_for_licensing': '5.11.2_rel/6'
  },
  'upcoming_scheduled_jobs': {
    'current_time': 'Dec 19 03:05:28 2023 PDT',
    'daily': 'Dec 19 10:58:12 2023 PDT (7 hours, 52 minutes, 44 seconds remaining)',
    'init_flag_check': 'Expired Not Rescheduled',
    'reservation_configuration_mismatch_between_nodes_in_ha_mode': 'Expired Not Rescheduled',
    'retrieve_data_processing_result': 'Expired Not Rescheduled',
    'start_utility_measurements': 'Dec 19 03:17:53 2023 PDT (12 minutes, 25 seconds remaining)',
    'send_utility_rum_reports': 'Dec 19 11:00:10 2023 PDT (7 hours, 54 minutes, 42 seconds remaining)',
    'save_unreported_rum_reports': 'Dec 19 04:03:03 2023 PDT (57 minutes, 35 seconds remaining)',
    'process_utility_rum_reports': 'Dec 19 11:10:10 2023 PDT (8 hours, 4 minutes, 42 seconds remaining)',
    'telemetry_reporting': 'Expired Not Rescheduled',
    'authorization_code_process': 'Expired Not Rescheduled',
    'data_synchronization': 'Expired Not Rescheduled',
    'external_event': 'Dec 23 14:57:23 2023 PDT (4 days, 11 hours, 51 minutes, 55 seconds remaining)',
    'operational_model': 'Expired Not Rescheduled'
  },
  'communication_statistics': {
    'communication_level_allowed': 'DIRECT',
    'overall_state': '<empty>',
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
    },
    'usage_reporting': {
      'attempts': 'Total=1, Success=1, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': 'OK_POLL on Dec 18 11:00:12 2023 PDT',
      'failure_reason': '<none>',
      'last_success_time': 'Dec 18 11:00:12 2023 PDT',
      'last_failure_time': '<none>'
    },
    'result_polling': {
      'attempts': 'Total=2, Success=2, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': 'OK on Dec 18 11:05:11 2023 PDT',
      'failure_reason': '<none>',
      'last_success_time': 'Dec 18 11:05:11 2023 PDT',
      'last_failure_time': '<none>'
    },
    'authorization_request': {
      'attempts': 'Total=2, Success=2, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': 'NO DATA TO PROCESS',
      'failure_reason': '<none>',
      'last_success_time': '<none>',
      'last_failure_time': '<none>'
    },
    'authorization_confirmation': {
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
      'attempts': 'Total=2, Success=2, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': 'OK on Dec 18 11:02:51 2023 PDT',
      'failure_reason': '<none>',
      'last_success_time': 'Dec 18 11:02:51 2023 PDT',
      'last_failure_time': '<none>'
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
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7',
        'reservation_status': 'NOT INSTALLED',
        'request_code': '<none>',
        'last_return_code': '<none>',
        'last_confirmation_code': '<none>',
        'reservation_authorization_code': '<none>'
      },
      'standby': {
        'pid': 'C9407R',
        'sn': 'FXS2119Q2U7',
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
    'total': 70,
    'purged': '0(0)',
    'total_acknowledged_received': 64,
    'waiting_for_ack': '0(6)',
    'available_to_report': 6,
    'collecting_data': 2,
    'maximum_display': 70,
    'in_storage': 30,
    'mia': '0(0)',
    'report_module_status': 'Ready'
  },
  'device_telemetry_report_summary': {
    'data_channel': 'AVAILABLE',
    'reports_on_disk': 0
  },
  'other_info': {
    'software_id': 'regid.2017-05.com.cisco.C9400,v1_ad928212-d182-407e-ac85-29e213602efa',
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
    'event_log_current_size': '62 KB',
    'trust_data': {
      'fxs2119q2u7': {
        'p': 'C9407R',
        'trustid': 693
      }
    },
    'overall_trust': 'INSTALLED (2)',
    'clock_synced_with_ntp': 'True'
  },
  'platform_provided_mapping_table': {
    'pid': 'C9407R',
    'total_licenses_found': 213,
    'enforced_licenses': {
      'fxs2119q2u7': {
        'pid': 'C9407R',
        'hseck9_entitlement_tag': 'regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2',
        'hseck9_no': 3
      }
    }
  }
}
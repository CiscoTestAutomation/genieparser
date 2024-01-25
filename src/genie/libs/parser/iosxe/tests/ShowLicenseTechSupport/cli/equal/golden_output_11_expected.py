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
      'status': 'ENABLED'
    },
    'account_information': {
      'smart_account': '<none>',
      'virtual_account': '<none>'
    },
    'data_privacy': {
      'sending_hostname': 'yes',
      'callhome_hostname_privacy': 'DISABLED',
      'smart_licensing_hostname_privacy': 'DISABLED',
      'version_privacy': 'DISABLED'
    },
    'transport': {
      'type': 'cslu',
      'cslu_address': '<empty>',
      'proxy': {
        'address': '<empty>',
        'port': '<empty>',
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
      'policy_in_use': 'Merged from multiple sources.',
      'reporting_ack_required': 'yes (CISCO default)',
      'unenforced_non_export_perpetual_attributes': {
        'first_report_requirement_days': '365 (CISCO default)',
        'reporting_frequency_days': '0 (CISCO default)',
        'report_on_change_days': '90 (CISCO default)'
      },
      'unenforced_non_export_subscription_attributes': {
        'first_report_requirement_days': '90 (CISCO default)',
        'reporting_frequency_days': '90 (CISCO default)',
        'report_on_change_days': '90 (CISCO default)'
      },
      'enforced_perpetual_subscription_license_attributes': {
        'first_report_requirement_days': '0 (CISCO default)',
        'reporting_frequency_days': '0 (CISCO default)',
        'report_on_change_days': '0 (CISCO default)'
      },
      'export_perpetual_subscription_license_attributes': {
        'first_report_requirement_days': '0 (CISCO default)',
        'reporting_frequency_days': '0 (CISCO default)',
        'report_on_change_days': '0 (CISCO default)'
      }
    },
    'usage_reporting': {
      'last_ack_received': '<none>',
      'next_ack_deadline': 'Mar 07 00:33:56 2024 PST',
      'reporting_push_interval': '30  days State(2) InPolicy(90)',
      'next_ack_push_check': '<none>',
      'next_report_push': 'Dec 10 20:55:17 2023 PST',
      'last_report_push': '<none>',
      'last_report_file_write': '<none>'
    },
    'trust_code_installed': '<none>'
  },
  'license_usage': {
    'handle': {
      1: {
        'license': 'network-advantage',
        'entitlement_tag': 'regid.2018-06.com.cisco.C9300L_48P_NW_Advantage,1.0_6422d51b-5580-4c05-9269-e4f4c23728b9',
        'description': 'C9300L 48P Network Advantage',
        'count': 1,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Dec 10 20:53:17 2023 PST',
        'request_time': 'Dec 10 20:53:17 2023 PST',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'network-advantage',
        'feature_description': 'C9300L 48P Network Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Perpetual',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 1,
            'current_report': 1696346452,
            'previous': 0
          }
        },
        'soft_enforced': 'True'
      },
      2: {
        'license': 'dna-advantage',
        'entitlement_tag': 'regid.2018-06.com.cisco.C9300L_48P_DNA_Advantage,1.0_ecb0e901-a493-434c-b502-5b96f690eab3',
        'description': 'C9300L 48P DNA Advantage',
        'count': 1,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Dec 10 20:53:17 2023 PST',
        'request_time': 'Dec 10 20:53:17 2023 PST',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'dna-advantage',
        'feature_description': 'C9300L 48P DNA Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Subscription',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 1,
            'current_report': 1696346453,
            'previous': 0
          }
        },
        'soft_enforced': 'True'
      }
    }
  },
  'product_information': {
    'udi': {
      'pid': 'C9300L-48PF-4X',
      'sn': 'FOC2732Y0JF'
    }
  },
  'agent_version': {
    'smart_agent_for_licensing': '5.10.3_rel/9'
  },
  'upcoming_scheduled_jobs': {
    'current_time': 'Dec 19 01:41:45 2023 PST',
    'daily': 'Dec 19 20:53:21 2023 PST (19 hours, 11 minutes, 36 seconds remaining)',
    'init_flag_check': 'Expired Not Rescheduled',
    'reservation_configuration_mismatch_between_nodes_in_ha_mode': 'Expired Not Rescheduled',
    'start_utility_measurements': 'Dec 19 01:54:26 2023 PST (12 minutes, 41 seconds remaining)',
    'send_utility_rum_reports': 'Dec 19 20:58:21 2023 PST (19 hours, 16 minutes, 36 seconds remaining)',
    'save_unreported_rum_reports': 'Dec 19 02:39:36 2023 PST (57 minutes, 51 seconds remaining)',
    'process_utility_rum_reports': 'Dec 19 20:54:14 2023 PST (19 hours, 12 minutes, 29 seconds remaining)',
    'data_synchronization': 'Dec 19 02:00:13 2023 PST (18 minutes, 28 seconds remaining)',
    'external_event': 'Jan 07 00:33:56 2024 PST (18 days, 22 hours, 52 minutes, 11 seconds remaining)',
    'operational_model': 'Expired Not Rescheduled'
  },
  'communication_statistics': {
    'communication_level_allowed': 'INDIRECT',
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
      'attempts': 'Total=0, Success=0, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': '<none>',
      'failure_reason': '<none>',
      'last_success_time': '<none>',
      'last_failure_time': '<none>'
    },
    'result_polling': {
      'attempts': 'Total=0, Success=0, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': '<none>',
      'failure_reason': '<none>',
      'last_success_time': '<none>',
      'last_failure_time': '<none>'
    },
    'authorization_request': {
      'attempts': 'Total=0, Success=0, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': '<none>',
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
      'attempts': 'Total=0, Success=0, Fail=0',
      'ongoing_failure': 'Overall=0 Communication=0',
      'last_response': '<none>',
      'failure_reason': '<none>',
      'last_success_time': '<none>',
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
    'message_flow_allowed': 'True'
  },
  'reservation_info': {
    'license_reservation': 'DISABLED',
    'last_data_push': '<none>',
    'last_file_export': '<none>',
    'overall_status': {
      'active': {
        'pid': 'C9300L-48PF-4X',
        'sn': 'FOC2732Y0JF',
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
    'total': 0,
    'purged': '0(0)',
    'total_acknowledged_received': 0,
    'waiting_for_ack': '0(205)',
    'available_to_report': 205,
    'collecting_data': 2,
    'maximum_display': 205,
    'in_storage': 0,
    'mia': '0(0)',
    'report_module_status': 'Ready'
  },
  'device_telemetry_report_summary': {
    'data_channel': 'AVAILABLE',
    'reports_on_disk': 0
  },
  'other_info': {
    'software_id': 'regid.2018-06.com.cisco.C9300L,1.0_03ebc7a2-6465-4dce-b28e-1f37001db25b',
    'agent_state': 'authorized',
    'ts_enable': 'True',
    'transport': 'cslu',
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
    'connect_info_name': '<empty>',
    'connect_info_version': '<empty>',
    'connect_info_additional': '<empty>',
    'connect_info_prod': 'False',
    'connect_info_capabilities': '<empty>',
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
    'event_log_current_size': '4282 KB',
    'local_device': 'No Trust Data',
    'overall_trust': 'No ID',
    'clock_synced_with_ntp': 'False'
  },
  'platform_provided_mapping_table': {
    'pid': 'C9300L-48PF-4X',
    'total_licenses_found': 213,
    'enforced_licenses': {
      'foc2732y0jf': {
        'pid': 'C9300L-48PF-4X'
      }
    }
  }
}

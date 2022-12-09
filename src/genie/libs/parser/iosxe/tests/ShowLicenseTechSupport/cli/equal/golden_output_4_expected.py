expected_output = {
  'primary_load_time_percent': 1,
  'secondary_load_time_percent': 0,
  'one_minute_load_percent': 7,
  'five_minute_load_percent': 3,
  'ntp_time': '09:59:10.353 UTC Mon Aug 29 2022',
  'smart_licensing_status': {
    'export_authorization_key': {
      'features_authorized': 'none'
    },
    'utility': {
      'status': 'DISABLED'
    },
    'smart_licensing_using_policy': {
      'status': 'ENABLED'
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
        'address': '<empty>',
        'port': '<empty>',
        'username': '<empty>',
        'password': '<empty>'
      },
      'server_identity_check': 'True'
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
      'next_ack_deadline': 'Nov 27 09:47:56 2022 UTC',
      'reporting_push_interval': '30  days State(2) InPolicy(90)',
      'next_ack_push_check': '<none>',
      'next_report_push': 'Aug 29 09:49:56 2022 UTC',
      'last_report_push': '<none>',
      'last_report_file_write': '<none>'
    }
  },
  'license_usage': {
    'handle': {
      1: {
        'license': 'network-advantage',
        'entitlement_tag': 'regid.2017-05.com.cisco.C9300_48P_NW_Advantagek9,1.0_6a224fe3-c92e-4440-a9c1-5d0e53a54015',
        'description': 'C9300-48 Network Advantage',
        'count': 2,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Aug 29 09:47:13 2022 UTC',
        'request_time': 'Aug 29 09:47:23 2022 UTC',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'network-advantage',
        'feature_description': 'C9300-48 Network Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Perpetual',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 2
          }
        },
        'soft_enforced': 'True'
      },
      2: {
        'license': 'dna-advantage',
        'entitlement_tag': 'regid.2017-05.com.cisco.C9300_48P_Dna_Advantage,1.0_60783b06-53ee-484c-b21e-615d3cf6837a',
        'description': 'C9300-48 DNA Advantage',
        'count': 2,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Aug 29 09:47:13 2022 UTC',
        'request_time': 'Aug 29 09:47:23 2022 UTC',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'dna-advantage',
        'feature_description': 'C9300-48 DNA Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Subscription',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 2
          }
        },
        'soft_enforced': 'True'
      },
      9: {
        'license': 'network-advantage',
        'entitlement_tag': 'regid.2017-03.com.cisco.advantagek9,1.0_bd1da96e-ec1d-412b-a50e-53846b347d53',
        'description': 'C9300-24 Network Advantage',
        'count': 1,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Aug 29 09:47:49 2022 UTC',
        'request_time': 'Aug 29 09:47:49 2022 UTC',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'network-advantage',
        'feature_description': 'C9300-24 Network Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Perpetual',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 1
          }
        },
        'soft_enforced': 'True'
      },
      12: {
        'license': 'dna-advantage',
        'entitlement_tag': 'regid.2017-05.com.cisco.c9300_dna_advantage,1.0_411773c3-2116-4c10-94a4-5d357fe6ff18',
        'description': 'C9300-24 DNA Advantage',
        'count': 1,
        'version': '1.0',
        'status': 'IN USE(15)',
        'status_time': 'Aug 29 09:47:49 2022 UTC',
        'request_time': 'Aug 29 09:47:49 2022 UTC',
        'export_status': 'NOT RESTRICTED',
        'feature_name': 'dna-advantage',
        'feature_description': 'C9300-24 DNA Advantage',
        'enforcement_type': 'NOT ENFORCED',
        'license_type': 'Subscription',
        'measurements': {
          'entitlement': {
            'interval': '00:15:00',
            'current_value': 1
          }
        },
        'soft_enforced': 'True'
      }
    }
  },
  'product_information': {
    'udi': {
      'pid': 'C9300-48U',
      'sn': 'FCW2133G09T'
    },
    'ha_udi_list': {
      'active': {
        'pid': 'C9300-48U',
        'sn': 'FCW2133G09T'
      },
      'standby': {
        'pid': 'C9300-48P',
        'sn': 'FCW2132L0WA'
      },
      'member': {
        'pid': 'C9300-24UX',
        'sn': 'FOC2537Y0HL'
      }
    }
  },
  'agent_version': {
    'smart_agent_for_licensing': '5.1.29_rel/134'
  },
  'upcoming_scheduled_jobs': {
    'current_time': 'Aug 29 09:59:10 2022 UTC',
    'daily': 'Aug 30 09:47:15 2022 UTC (23 hours, 48 minutes, 5 seconds remaining)',
    'authorization_renewal': 'Aug 30 09:48:55 2022 UTC (23 hours, 49 minutes, 45 seconds remaining)',
    'init_flag_check': 'Expired Not Rescheduled',
    'register_period_expiration_check': 'Aug 29 10:03:50 2022 UTC (4 minutes, 40 seconds remaining)',
    'reservation_configuration_mismatch_between_nodes_in_ha_mode': 'Expired Not Rescheduled',
    'start_utility_measurements': 'Aug 29 10:05:43 2022 UTC (6 minutes, 33 seconds remaining)',
    'send_utility_rum_reports': 'Aug 30 09:49:12 2022 UTC (23 hours, 50 minutes, 2 seconds remaining)',
    'save_unreported_rum_reports': 'Aug 29 10:51:13 2022 UTC (52 minutes, 3 seconds remaining)',
    'process_utility_rum_reports': 'Aug 30 09:47:56 2022 UTC (23 hours, 48 minutes, 46 seconds remaining)',
    'data_synchronization': 'Expired Not Rescheduled',
    'external_event': 'Aug 29 10:47:53 2022 UTC (48 minutes, 43 seconds remaining)',
    'operational_model': 'Expired Not Rescheduled'
  },
  'communication_statistics': {
    'communication_level_allowed': 'INDIRECT',
    'overall_state': '<empty>',
    'trust_establishment': {
      'attempts': 'Total=2, Success=0, Fail=2',
      'ongoing_failure': 'Overall=2 Communication=2',
      'last_response': 'NO REPLY on Aug 29 09:58:51 2022 UTC',
      'failure_reason': '<none>',
      'last_success_time': '<none>',
      'last_failure_time': 'Aug 29 09:58:51 2022 UTC'
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
    'message_flow_allowed': 'False'
  },
  'reservation_info': {
    'license_reservation': 'DISABLED',
    'overall_status': {
      'active': {
        'pid': 'C9300-48U',
        'sn': 'FCW2133G09T',
        'reservation_status': 'NOT INSTALLED',
        'request_code': '<none>',
        'last_return_code': '<none>',
        'last_confirmation_code': '<none>',
        'reservation_authorization_code': '<none>'
      },
      'standby': {
        'pid': 'C9300-48P',
        'sn': 'FCW2132L0WA',
        'reservation_status': 'NOT INSTALLED',
        'request_code': '<none>',
        'last_return_code': '<none>',
        'last_confirmation_code': '<none>',
        'reservation_authorization_code': '<none>'
      },
      'member': {
        'pid': 'C9300-24UX',
        'sn': 'FOC2537Y0HL',
        'reservation_status': 'NOT INSTALLED',
        'request_code': '<none>',
        'last_return_code': '<none>',
        'last_confirmation_code': '<none>',
        'reservation_authorization_code': '<none>'
      }
    },
    'purchased_licenses': 'No Purchase Information Available'
  },
  'other_info': {
    'software_id': 'regid.2017-05.com.cisco.C9300,v1_727af1d9-6c39-4444-b301-863f81445b72',
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
    'config_persist_received': 'True',
    'message_version': '1.3',
    'connect_info_name': '<empty>',
    'connect_info_version': '<empty>',
    'connect_info_additional': '<empty>',
    'connect_info_prod': 'False',
    'connect_info_capabilities': '<empty>',
    'agent_capabilities': 'UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE',
    'check_point_interface': 'True',
    'config_management_interface': 'False',
    'license_map_interface': 'True',
    'ha_interface': 'True',
    'trusted_store_interface': 'True',
    'platform_data_interface': 'True',
    'crypto_version_2_interface': 'False',
    'sapluginmgmtinterfacemutex': 'True',
    'sapluginmgmtipdomainname': 'True',
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
    'smartagentreportonupgrade': 'False',
    'smartagentusagestatisticsenable': 'False',
    'smartagentmaxrummemory': 50,
    'smartagentconcurrentthreadmax': 10,
    'smartagentpolicycontrollermodel': 'False',
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
    'event_log_current_size': '21 KB',
    'trust_data': {
      'fcw2133g09t:': {
        'p': 'C9300-48U',
        'trustvalue': 'NOT INSTALLED'
      },
      'fcw2132l0wa:': {
        'p': 'C9300-48P',
        'trustvalue': 'NOT INSTALLED'
      },
      'foc2537y0hl:': {
        'p': 'C9300-24UX',
        'trustvalue': 'NOT INSTALLED'
      }
    },
    'overall_trust': 'No ID',
    'clock_synced_with_ntp': 'True'
  },
  'platform_provided_mapping_table': {
    'pid': 'C9300-48U',
    'total_licenses_found': 194,
    'enforced_licenses': {
      'fcw2133g09t': {
        'pid': 'C9300-48U'
      },
      'fcw2132l0wa': {
        'pid': 'C9300-48P'
      },
      'foc2537y0hl': {
        'pid': 'C9300-24UX'
      }
    }
  }
}
import pprint

expected_output = {
    'smart_licensing_status': {
        'license_conversion': {
            'automatic_conversion_enabled': 'False'
        },
        'export_authorization_key': {
            'features_authorized': '<none>'
        },
        'utility': {
            'status': 'DISABLED'
        },
        'smart_licensing_using_policy': {
            'status': 'ENABLED'
        },
        'account_information': {
            'smart_account': 'BU Production Test As of Mar 15 20:10:30 2024 UTC',
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
            'proxy': ''
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
            'last_ack_received': 'Mar 15 20:10:40 2024 UTC',
            'next_ack_deadline': 'May 14 20:10:40 2024 UTC',
            'reporting_push_interval': '30  days',
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
        'license_name': {
            'network-advantage (C9350-24 Catalyst Network Advantage):': {
                'description': 'C9350-24 Catalyst Network Advantage',
                'count': 4,
                'version': '1.0',
                'status': 'IN USE',
                'export_status': 'NOT RESTRICTED',
                'feature_name': 'network-advantage',
                'feature_description': 'C9350-24 Catalyst Network Advantage',
                'enforcement_type': 'NOT ENFORCED',
                'license_type': 'Perpetual'
            },
            'dna-advantage (C9350-24 Catalyst Software Subscription Advantage):': {
                'description': 'C9350-24 Catalyst Software Subscription Advantage',
                'count': 4,
                'version': '1.0',
                'status': 'IN USE',
                'export_status': 'NOT RESTRICTED',
                'feature_name': 'dna-advantage',
                'feature_description': 'C9350-24 Catalyst Software Subscription Advantage',
                'enforcement_type': 'NOT ENFORCED',
                'license_type': 'Subscription'
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
    'license_authorizations': {
        'overall_status': {
            'active': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8X0',
                'status': 'NOT INSTALLED'
            },
            'standby': {
                'pid': 'C9350-24U',
                'sn': 'FOC2705Y8XF',
                'status': 'NOT INSTALLED'
            },
            'member': {
                'pid': 'C9350-24U',
                'sn': 'FOC2718Y66X',
                'status': 'NOT INSTALLED'
            },
            'member2': {
                'pid': 'C9350-24U',
                'sn': 'FOC2719YOHR',
                'status': 'NOT INSTALLED'
            }
        },
        'purchased_licenses': 'No Purchase Information Available'
    },
    'usage_report_summary': {
        'total': '703',
        'purged': '288',
        'total_acknowledged_received': '0',
        'waiting_for_ack': '86',
        'available_to_report': '312',
        'collecting_data': '2'
    }
}
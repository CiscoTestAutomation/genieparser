expected_output = {
    "smart_licensing_status":{
        "license_conversion":{
            "automatic_conversion_enabled":"False"
        },
        "export_authorization_key":{
            "features_authorized":"<none>"
        },
        "utility":{
            "status":"DISABLED"
        },
        "smart_licensing_using_policy":{
            "status":"ENABLED"
        },
        "account_information":{
            "smart_account":"SA-Switching-Polaris As of Apr 23 15:29:19 2025 IST",
            "virtual_account":"stratocaster_test"
        },
        "data_privacy":{
            "sending_hostname":"yes",
            "callhome_hostname_privacy":"DISABLED",
            "smart_licensing_hostname_privacy":"DISABLED",
            "version_privacy":"DISABLED"
        },
        "transport":{
            "type":"Smart",
            "url":"https://smartreceiver-stage.cisco.com/licservice/license",
            "proxy":"Not Configured"
        },
        "miscellaneous":{
            "custom_id":"<empty>"
        },
        "policy":{
            "policy_in_use":"Installed On Apr 23 15:28:43 2025 IST",
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
            "last_ack_received":"Apr 23 15:28:43 2025 IST",
            "next_ack_deadline":"<none>",
            "reporting_push_interval":"0 (no reporting)",
            "next_ack_push_check":"Apr 23 15:33:15 2025 IST",
            "next_report_push":"<none>",
            "last_report_push":"Apr 23 15:29:20 2025 IST",
            "last_report_file_write":"<none>"
        },
        "trust_code_installed":{
            "active":{
                "pid":"C9350-48T",
                "sn":"FOC2820Y07F",
                "info":"INSTALLED on Apr 23 15:28:43 2025 IST    Valid on Apr 23 15:23:40 2025 IST"
            },
            "standby":{
                "pid":"C9350-48P",
                "sn":"FOC2823Y0QC",
                "info":"INSTALLED on Apr 23 15:28:43 2025 IST    Valid on Apr 23 15:23:41 2025 IST"
            },
            "member":{
                "pid":"C9350-24T",
                "sn":"FOC2823Y1LN",
                "info":"INSTALLED on Apr 23 15:28:43 2025 IST    Valid on Apr 23 15:23:42 2025 IST"
            }
        }
    },
    "license_usage":{
        "license_name":{
            "essentials (Switching OS Essentials):":{
                "description":"Cisco C9350 Switching IOS-XE Essentials",
                "count":3,
                "version":"1.0",
                "status":"IN USE",
                "export_status":"NOT RESTRICTED",
                "feature_name":"essentials",
                "feature_description":"Cisco C9350 Switching IOS-XE Essentials",
                "enforcement_type":"NOT ENFORCED",
                "license_type":"Perpetual"
            }
        }
    },
    "product_information":{
        "udi":{
            "pid":"C9350-48T",
            "sn":"FOC2820Y07F"
        },
        "ha_udi_list":{
            "active":{
                "pid":"C9350-48T",
                "sn":"FOC2820Y07F"
            },
            "standby":{
                "pid":"C9350-48P",
                "sn":"FOC2823Y0QC"
            },
            "member":{
                "pid":"C9350-24T",
                "sn":"FOC2823Y1LN"
            }
        }
    },
    "agent_version":{
        "smart_agent_for_licensing":"6.3.10/58086906e"
    },
    "license_authorizations":{
        "overall_status":{
            "active":{
                "pid":"C9350-48T",
                "sn":"FOC2820Y07F",
                "status":"NOT INSTALLED"
            },
            "standby":{
                "pid":"C9350-48P",
                "sn":"FOC2823Y0QC",
                "status":"NOT INSTALLED"
            },
            "member":{
                "pid":"C9350-24T",
                "sn":"FOC2823Y1LN",
                "status":"NOT INSTALLED"
            }
        },
        "purchased_licenses":"No Purchase Information Available"
    },
    "usage_report_summary":{
        "total":"4",
        "purged":"0",
        "total_acknowledged_received":"0",
        "waiting_for_ack":"3",
        "available_to_report":"1",
        "collecting_data":"1"
    }
}
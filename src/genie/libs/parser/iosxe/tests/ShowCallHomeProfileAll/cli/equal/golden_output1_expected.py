expected_output = {
    "profile":{
        "name":{
            "CiscoTAC-1":{
                "status":"ACTIVE",
                "mode":"Full Reporting",
                "reporting_data":"Smart Call Home, Smart Licensing",
                "preferred_message_format":"xml",
                "message_size_limit_in_bytes":3145728,
                "transport_method":"http",
                "http_address":"http://www.test1.com",
                "other_address":"default",
                "periodic_info":{
                    "configuration":{
                        "scheduled":"every 1 day of the month",
                        "time":"09:15"
                    },
                    "inventory":{
                        "scheduled":"every 1 day of the month",
                        "time":"09:00"
                    }
                },
                "group_pattern":{
                    "Alert-group":{
                        "severity":"Severity"
                    },
                    "crash":{
                        "severity":"debugging"
                    },
                    "diagnostic":{
                        "severity":"minor"
                    },
                    "environment":{
                        "severity":"warning"
                    },
                    "inventory":{
                        "severity":"normal"
                    },
                    "Syslog-Pattern":{
                        "severity":"Severity"
                    },
                    "APF-.-WLC_.*":{
                        "severity":"warning"
                    },
                    ".*":{
                        "severity":"major"
                    }
                }
            },
            "sds":{
                "status":"ACTIVE",
                "mode":"Full Reporting",
                "reporting_data":"Smart Call Home",
                "preferred_message_format":"xml",
                "message_size_limit_in_bytes":3145728,
                "transport_method":"http and email",
                "http_address":"http://www.test1.com",
                "email_address":"Not yet set up",
                "group_pattern":{
                    "Alert-group":{
                        "severity":"Severity"
                    },
                    "N/A":{
                        "severity":"N/A"
                    },
                    "Syslog-Pattern":{
                        "severity":"Severity"
                    }
                }
            }
        }
    }
}
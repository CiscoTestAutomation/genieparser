expected_output = {
    'ids': {
        '1': {
            'probe_id': 1,
            'start_time': {
                '03:21:11 UTC Mon Nov 22 2021': {
                    'dns_rtt': 0,
                    'http_transaction_rtt': 343,
                    'no_of_failures': 0,
                    'no_of_success': 60,
                    'tcp_connection_rtt': 61
                    },
                '04:21:11 UTC Mon Nov 22 2021': {
                    'dns_rtt': 0,
                    'http_transaction_rtt': 160,
                    'no_of_failures': 0,
                    'no_of_success': 25,
                    'tcp_connection_rtt': 19
                    }
                },
            'type_of_operation': 'http'
        },
        '2': {
            'probe_id': 2,
            'start_time': {
                '00:13:17 UTC Mon Nov 22 2021': {
                    'delay': '795993/902821/1057999',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 120,
                    'oper_id': 60988531,
                    'status': 'OK'
                    },
                '01:13:17 UTC Mon Nov 22 2021': {
                    'delay': '795993/902821/1057999',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 120,
                    'oper_id': 60988531,
                    'status': 'OK'
                    },
                '02:13:17 UTC Mon Nov 22 2021': {
                    'delay': '795993/902821/1057999',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 120,
                    'oper_id': 60988531,
                    'status': 'OK'
                    },
                '03:13:17 UTC Mon Nov 22 2021': {
                    'delay': '795993/902821/1057999',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 120,
                    'oper_id': 60988531,
                    'status': 'OK'
                    },
                '04:13:17 UTC Mon Nov 22 2021': {
                    'delay': '795993/902821/1057999',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 66,
                    'oper_id': 60988531,
                    'status': 'OK'
                    }
                },
            'type_of_operation': 'mcast'
        },
        '3': {
            'probe_id': 3,
            'start_time': {
                '03:12:47 UTC Mon Nov 22 2021': {
                    'delay': '796/901/1016',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 60,
                    'oper_id': 393146530,
                    'status': 'OK'
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'delay': '796/901/1016',
                    'destination': '10.50.10.100',
                    'loss_sd': 0,
                    'no_of_failures': 0,
                    'no_of_success': 34,
                    'oper_id': 393146530,
                    'status': 'OK'
                    }
                },
            'type_of_operation': 'mcast'
        },
        '50': {
            'probe_id': 50,
            'start_time': {
                '03:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 60
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 34
                    }
                },
            'type_of_operation': 'tcp-connect'
        },
        '51': {
            'probe_id': 51,
            'start_time': {
                '00:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 120
                    },
                '01:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 120
                    },
                '02:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 120
                    },
                '03:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 120
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 67
                    }
                },
            'type_of_operation': 'tcp-connect'
        },
        '52': {
            'probe_id': 52,
            'start_time': {
                '03:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 60
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 34
                    }
                },
            'type_of_operation': 'tcp-connect'
        },
        '53': {
            'probe_id': 53,
            'start_time': {
                '03:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 60,
                    'no_of_success': 0
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 33,
                    'no_of_success': 0
                    }
                },
            'type_of_operation': 'tcp-connect'
        },
        '54': {
            'probe_id': 54,
            'start_time': {
                '03:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 60,
                    'no_of_success': 0
                    },
                '04:12:47 UTC Mon Nov 22 2021': {
                    'no_of_failures': 34,
                    'no_of_success': 0
                    }
                },
            'type_of_operation': 'tcp-connect'
        },
        '100': {
            'probe_id': 100,
            'start_time': {
                '00:13:23 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    },
                '01:13:22 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    },
                '02:13:21 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    },
                '03:13:20 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    },
                '04:13:19 UTC Mon Nov 22 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 33
                    },
                '22:13:25 UTC Sun Nov 21 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    },
                '23:13:24 UTC Sun Nov 21 2021': {
                    'no_of_failures': 0,
                    'no_of_success': 59
                    }
                },
            'type_of_operation': 'dns'
        }
    }
}
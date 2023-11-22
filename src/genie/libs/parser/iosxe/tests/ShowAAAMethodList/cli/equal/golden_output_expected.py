expected_output = {
    'acct': {
        'permanent_list': {
            'Permanent_None': {
                'action': 'ALIVE',
                'id': 0,
                'method_list': '',
                'name': 'Permanent None',
                'state': 'ALIVE',
                'valid': True
            }
        },
        'queue': {
            'AAA_ML_ACCT_AUTH_PROXY': {},
            'AAA_ML_ACCT_COMMAND': {},
            'AAA_ML_ACCT_CONN': {},
            'AAA_ML_ACCT_CONNECTEDAPPS': {},
            'AAA_ML_ACCT_DOT1X': {},
            'AAA_ML_ACCT_IDENTITY': {},
            'AAA_ML_ACCT_NET': {},
            'AAA_ML_ACCT_RESOURCE': {},
            'AAA_ML_ACCT_RM': {},
            'AAA_ML_ACCT_SHELL': {},
            'AAA_ML_ACCT_SYSTEM': {}
        }
    },
    'authen': {
        'permanent_list': {
            'Permanent_Enable': {
                'id': 0,
                'method_list': 'ENABLE',
                'name': 'Permanent Enable',
                'state': 'ALIVE',
                'valid': True
            },
            'Permanent_Enable_None': {
                'id': 0,
                'method_list': 'ENABLE  NONE',
                'name': 'Permanent '
                        'Enable None',
                'state': 'ALIVE',
                'valid': True
            },
            'Permanent_Local': {
                'id': 0,
                'method_list': 'LOCAL',
                'name': 'Permanent Local',
                'state': 'ALIVE',
                'valid': True
            },
            'Permanent_None': {
                'id': 0,
                'method_list': 'NONE',
                'name': 'Permanent None',
                'state': 'ALIVE',
                'valid': True
            },
            'Permanent_rcmd': {
                'id': 0,
                'method_list': 'RCMD',
                'name': 'Permanent rcmd',
                'state': 'ALIVE',
                'valid': True
            }
        },
        'queue': {
            'AAA_ML_AUTHEN_8021X': {},
            'AAA_ML_AUTHEN_ARAP': {},
            'AAA_ML_AUTHEN_CONNECTEDAPPS': {},
            'AAA_ML_AUTHEN_DOT1X': {
                'id': 97000002,
                'method_list': 'SERVER_GROUP  private_sg-0',
                'name': 'pvt_authen_0',
                'state': 'DEAD',
                'valid': True
            },
            'AAA_ML_AUTHEN_EAPOUDP': {},
            'AAA_ML_AUTHEN_ENABLE': {
                'id': 0,
                'method_list': 'ENABLE  SERVER_GROUP radius SERVER_GROUP tacacs+',
                'name': 'default',
                'state': 'ALIVE',
                'valid': True
            },
            'AAA_ML_AUTHEN_LOGIN': {
                'id': 0,
                'method_list': 'SERVER_GROUP radius SERVER_GROUP radius SERVER_GROUP radius SERVER_GROUP radius',
                'name': 'default',
                'state': 'ALIVE',
                'valid': True
            },
            'AAA_ML_AUTHEN_PPP': {},
            'AAA_ML_AUTHEN_SGBP': {},
            'AAA_ML_AUTHEN_WEBAUTH': {}
        }
    },
    'author': {
        'permanent_list': {
            'local-list': {
                'id': 0,
                'method_list': 'LOCAL',
                'name': 'local-list',
                'state': 'ALIVE',
                'valid': True
            }
        },
        'queue': {
            'AAA_ML_AUTHOR_AUTH_PROXY': {},
            'AAA_ML_AUTHOR_COMMAND': {},
            'AAA_ML_AUTHOR_CONFIG': {},
            'AAA_ML_AUTHOR_CONN': {},
            'AAA_ML_AUTHOR_CONNECTEDAPPS': {},
            'AAA_ML_AUTHOR_CREDENTIAL_DOWNLOAD': {},
            'AAA_ML_AUTHOR_FLTSV': {},
            'AAA_ML_AUTHOR_IPMOBILE': {},
            'AAA_ML_AUTHOR_NET': {},
            'AAA_ML_AUTHOR_POLICY_IF': {},
            'AAA_ML_AUTHOR_PREAUTH': {},
            'AAA_ML_AUTHOR_PREPAID': {},
            'AAA_ML_AUTHOR_RM': {},
            'AAA_ML_AUTHOR_SHELL': {
                'id': 0,
                'method_list': 'LOCAL',
                'name': 'default',
                'state': 'ALIVE',
                'valid': True
            },
            'AAA_ML_AUTHOR_SUBSCRIBER_SERVICE': {}
        }
    }
}


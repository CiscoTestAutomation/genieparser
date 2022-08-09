expected_output = {
    'ikev2_stats': {
        'aaa_operation': {
            'receive_pskey': {
                'passed': 0,
                'failed': 0
           },
            'eap_auth': {
                'passed': 0,
                'failed': 0
           },
           'start_acc': {
                'passed': 0,
                'failed': 0
            },
            'stop_acc': {
                'passed': 0,
                'failed': 0
            },
            'authorization': {
                'passed': 0,
                'failed': 0
            }
        },
        'ipsec_operation': {
            'ipsec_policy_verify': {
                'passed': 27308,
                'failed': 7
            },
            'sa_creation': {
                'passed': 12279,
                'failed': 14970
            },
            'sa_deletion': {
                'passed': 87418,
                'failed': 7
            }
        },
        'crypto_engine_operation': {
            'dh_key_generated': {
                'passed': 136093,
                'failed': 654
            },
            'secret_generated': {
                'passed': 30624,
                'failed': 105366
            },
            'signature_sign': {
                'passed': 30271,
                'failed': 0
            },
            'signature_verify': {
                'passed': 30271,
                'failed': 0
            }
        },
        'pki_operation': {
            'verify_cert': {
                'passed': 30271,
                'failed': 3
            },
            'cert_using_http': {
                'passed': 0,
                'failed': 0
            },
            'peer_cert_using_http': {
                'passed': 0,
                'failed': 0
            },
            'get_issuers': {
                'passed': 158799,
                'failed': 0
            },
            'get_cert_from_issuers': {
                'passed': 36300,
                'failed': 0
            },
            'get_dn_from_cert': {
                'passed': 0,
                'failed': 0
            }
        },
        'gkm_operation': {
            'get_policy': {
                'passed': 0,
                'failed': 0
            },
            'set_policy': {
                'passed': 0,
                'failed': 0
            }
        },
        'ppk_sks_operation': {
            'ppk_get_cap': {
                'passed': 0,
                'failed': 0
            },
            'ppk_get_key': {
                'passed': 0,
                'failed': 0
            }
        },
    },
}

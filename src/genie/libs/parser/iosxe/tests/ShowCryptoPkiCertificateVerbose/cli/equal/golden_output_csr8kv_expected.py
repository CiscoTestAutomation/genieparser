expected_output = {
        'certificates': {
            'certificate': {
                'status': 'Available', 
                'serial': '03', 
                'usage': 'General Purpose', 
                'issuer': {
                    'common_name': 'RSA-CA', 
                    'organization': 'cisco'
                }, 
                'subject': {
                    'name': 'ROUTER', 
                    'common_name': 'ROUTER', 
                    'organizational_unit': 'PKI', 
                    'organization': 'cisco'
                }, 
                'validity_date': {
                    'start_date': '23:09:23 IST Nov 17 2021', 
                    'end_date': '23:09:23 IST Nov 16 2026'
                }, 
                'subject_key_info': {
                    'key_algorithm': 'rsaEncryption', 
                    'key_length': '2048'
                }, 
                'signature_algorithm': 'SHA256 with RSA Encryption', 
                'fingerprint_md5': '63B03B57 6ADB6EB8 A525E53A F8478A34', 
                'fingerprint_sha1': '8C78B5ED 59B6EC2E 645DB494 998657E6 290DA64C', 
                'key_usage_hex': 'B0000000', 
                'key_usage': {
                    'key_usage_1': 'Digital Signature', 
                    'key_usage_2': 'Key Encipherment', 
                    'key_usage_3': 'Data Encipherment'
                }, 
                'cert_install_time': '23:09:51 IST Nov 17 2021', 
                'trustpoints': 'openssl_test', 
                'key_label': 'openssl_test'
            }, 
            'ca_certificate': {
                'status': 'Available', 
                'serial': '4BE62C7CF3A30DDB6F133B50B2CFDCCD4F84D0B0', 
                'usage': 'Signature', 
                'issuer': {
                    'common_name': 'RSA-CA', 
                    'organization': 'cisco'
                }, 
                'subject': {
                    'common_name': 'RSA-CA', 
                    'organization': 'cisco'
                }, 
                'validity_date': {
                    'start_date': '23:08:44 IST Nov 17 2021', 
                    'end_date': '23:08:44 IST Nov 15 2031'
                }, 
                'subject_key_info': {
                    'key_algorithm': 'rsaEncryption', 
                    'key_length': '2048'
                }, 
                'signature_algorithm': 'SHA256 with RSA Encryption', 
                'fingerprint_md5': '1E534C29 1DC463F6 90544209 26C218F6', 
                'fingerprint_sha1': '0A21682B 2C484AC6 1CE09935 2132CA62 686ACA1D', 
                'key_usage_hex': '86000000', 
                'key_usage': {
                    'key_usage_1': 'Digital Signature', 
                    'key_usage_2': 'Key Cert Sign', 
                    'key_usage_3': 'CRL Signature'
                }, 
                'cert_install_time': '23:09:50 IST Nov 17 2021', 
                'trustpoints': 'openssl_test'
            }
        }
    } 

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
                    'ip_address': '100.100.100.1', 
                    'common_name': 'ROUTER', 
                    'organizational_unit': 'PKI', 
                    'organization': 'cisco'
                }, 
                'validity_date': {
                    'start_date': '15:33:15 IST Nov 20 2021', 
                    'end_date': '15:33:15 IST Nov 19 2026'
                }, 
                'subject_key_info': {
                    'key_algorithm': 'rsaEncryption', 
                    'key_length': '2048'
                }, 
                'signature_algorithm': 'SHA256 with RSA Encryption', 
                'fingerprint_md5': 'DE8CC8FA B9E41665 31DDED4A 1A2A6191', 
                'fingerprint_sha1': '9E349A47 A2227F86 E87336CE 3D260431 D4F11472', 
                'key_usage_hex': 'B0000000', 
                'key_usage': {
                    'key_usage_1': 'Digital Signature', 
                    'key_usage_2': 'Key Encipherment', 
                    'key_usage_3': 'Data Encipherment'
                }, 
                'subj_alt_name': {
                    'subj_alt_ip_addr': '100.100.100.1'
                }, 
                'cert_install_time': '15:33:42 IST Nov 20 2021', 
                'trustpoints': 'openssl_test', 
                'key_label': 'openssl_test'
            }, 
            'ca_certificate': {
                'status': 'Available', 
                'serial': '55722CE2042FD3DD40C3013FF430616170845853', 
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
                    'start_date': '15:32:34 IST Nov 20 2021', 
                    'end_date': '15:32:34 IST Nov 18 2031'
                }, 
                'subject_key_info': {
                    'key_algorithm': 'rsaEncryption', 
                    'key_length': '2048'
                }, 
                'signature_algorithm': 'SHA256 with RSA Encryption', 
                'fingerprint_md5': '1CFCED12 50E0E6DB 7DA87BE5 926ECDE3', 
                'fingerprint_sha1': 'EF28E980 73B28C7F 41F80804 73B446EF 5B1BE3D4', 
                'key_usage_hex': '86000000', 
                'key_usage': {
                    'key_usage_1': 'Digital Signature', 
                    'key_usage_2': 'Key Cert Sign', 
                    'key_usage_3': 'CRL Signature'
                }, 
                'cert_install_time': '15:33:42 IST Nov 20 2021', 
                'trustpoints': 'openssl_test'
                }
            }
        }

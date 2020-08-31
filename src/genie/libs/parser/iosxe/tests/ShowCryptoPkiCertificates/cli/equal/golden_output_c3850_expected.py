expected_output = {
    "trustpoints": {
        "CISCO_IDEVID_SUDI": {
            "associated_trustpoints": {
                "certificate": {
                    "status": "Available",
                    "serial_number_in_hex": "793B572700000003750B",
                    "subject": {
                        "name": "WS-C3850-24P-0057D21BC800",
                        "pid": "WS-C3850-24P",
                        "cn": "WS-C3850-24P-0057D21BC800",
                        "serial_number": "FCW1947C0GF",
                    },
                    "issuer": {"cn": "Cisco Manufacturing CA SHA2", "o": "Cisco"},
                    "crl_distribution_points": "http://www.cisco.com/security/pki/crl/cmca2.crl",
                    "usage": "General Purpose",
                    "validity_date": {
                        "start_date": "00:34:52 UTC Nov 20 2015",
                        "end_date": "00:44:52 UTC Nov 20 2025",
                    },
                },
                "ca_certificate": {
                    "status": "Available",
                    "serial_number_in_hex": "02",
                    "subject": {"cn": "Cisco Manufacturing CA SHA2", "o": "Cisco"},
                    "issuer": {"cn": "Cisco Root CA M2", "o": "Cisco"},
                    "crl_distribution_points": "http://www.cisco.com/security/pki/crl/crcam2.crl",
                    "usage": "Signature",
                    "validity_date": {
                        "start_date": "13:50:58 UTC Nov 12 2012",
                        "end_date": "13:00:17 UTC Nov 12 2037",
                    },
                },
            }
        }
    }
}

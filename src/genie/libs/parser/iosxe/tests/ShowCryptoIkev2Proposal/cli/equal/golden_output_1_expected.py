expected_output = {
    "proposal_name": {
        "default": {
            "encryption": "AES-CBC-256",
            "integrity": "SHA512 SHA384",
            "prf": "SHA512 SHA384",
            "dh_group": [
                "DH_GROUP_256_ECP/Group 19",
                "DH_GROUP_2048_MODP/Group 14",
                "DH_GROUP_521_ECP/Group 21"
            ],
            "pqc": "ML-KEM-768 ML-KEM-1024 Optional"
        },
        "ikev2proposal": {
            "encryption": "AES-CBC-256",
            "integrity": "SHA512",
            "prf": "SHA512",
            "dh_group": [
                "DH_GROUP_521_ECP/Group 21"
            ],
            "pqc": "ML-KEM-1024 Optional"
        }
    }
}
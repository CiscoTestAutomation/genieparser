expected_output = {
    "ipsec_profile_name": {
        "default": {
            "security_association_lifetime": "3600 seconds",
            "responder_only": "N",
            "psf": "N",
            "mixed_mode": "Disabled",
            "tranform_sets": {
                "default": {
                    "transform_set_name": "esp-aes",
                    "transform_set_method": "esp-sha-hmac"
                }
            }
        },
        "dmvpn-hub": {
            "ikev2_profile_name": "ikev2profile",
            "security_association_lifetime": "3600 seconds",
            "responder_only": "N",
            "psf": "Y",
            "pfs_inherit": "N",
            "dh_group": "group21",
            "pqc": "ML-KEM-1024",
            "mixed_mode": "Disabled",
            "tranform_sets": {
                "tset1": {
                    "transform_set_name": "esp-256-aes",
                    "transform_set_method": "esp-sha256-hmac"
                }
            }
        }
    }
}
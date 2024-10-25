expected_output = {
    "ipsec_profile_name": {
        "DCCRT1012-IPSEC-PROFILE": {
            "security_association_lifetime": "102400000 kilobytes/27000 seconds",
            "responder_only": "Y",
            "psf": "N",
            "mixed_mode": "Disabled",
            "tranform_sets": {
                "RSITE-ipsec-proposal-set": {
                    "transform_set_name": "esp-gcm",
                    "transform_set_method": "256"
                }
            }
        },
        "FRCRT1012-IPSEC-PROFILE": {
            "security_association_lifetime": "102400000 kilobytes/27000 seconds",
            "responder_only": "Y",
            "psf": "N",
            "mixed_mode": "Disabled",
            "tranform_sets": {
                "RSITE-ipsec-proposal-set": {
                    "transform_set_name": "esp-gcm",
                    "transform_set_method": "256"
                }
            }
        },
        "default": {
            "security_association_lifetime": "4608000 kilobytes/3600 seconds",
            "responder_only": "N",
            "psf": "N",
            "mixed_mode": "Disabled",
            "tranform_sets": {
                "default": {
                    "transform_set_name": "esp-aes",
                    "transform_set_method": "esp-sha-hmac"
                }
            }
        }
    }
}

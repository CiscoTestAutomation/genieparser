expected_output = {
    "ipsec_profile_name": {
        "default": {
            "security_association_lifetime": "4608000 kilobytes/3600 seconds",
            "responder_only": "N",
            "psf": "N",
            "ml-kem_only": "N",
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
            "security_association_lifetime": "4608000 kilobytes/3600 seconds",
            "responder_only": "N",
            "psf": "Y",
            "ml-kem_only": "N",
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
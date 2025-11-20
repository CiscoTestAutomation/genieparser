expected_output = {
    "ikev2_session": {
        "IPv6": {
            1: {
                "session_id": 17,
                "status": "UP-ACTIVE",
                "ike_count": 1,
                "child_count": 1,
                "tunnel_id": 3,
                "fvrf": "none",
                "ivrf": "none",
                "session_status": "READY",
                "local_ip": "2001:DB8:1101::222",
                "local_port": 500,
                "remote_ip": "2001:DB8:1201::222",
                "remote_port": 500,
                "encryption": "AES-CBC",
                "key_length": 256,
                "prf": "SHA512",
                "hash_algo": "SHA512",
                "dh_group": 21,
                "auth_sign": "PSK",
                "auth_verify": "PSK",
                "ake": {
                    "AKE1": "MLKEM1024"
                },
                "lifetime": 86400,
                "activetime": 19908,
                "ce_id": 0,
                "id": 17,
                "local_spi": "697FEC72CFA6D976",
                "remote_spi": "5F539F4D2F15DC30",
                "child_sa": {
                    1: {
                        "local_selectors": [],
                        "remote_selectors": [],
                        "traffic_selectors": [
                            "2001:DB8:1101::222/0 - 2001:DB8:1101::222/65535    ->    2001:DB8:1201::222/0 - 2001:DB8:1201::222/65535"
                        ],
                        "esp_spi_in": "0xC9CF4E92",
                        "esp_spi_out": "0xCA9B3063"
                    }
                }
            },
            2: {
                "session_id": 18,
                "status": "UP-ACTIVE",
                "ike_count": 1,
                "child_count": 1,
                "tunnel_id": 4,
                "fvrf": "none",
                "ivrf": "none",
                "session_status": "READY",
                "local_ip": "2001:DB8:1101::222",
                "local_port": 500,
                "remote_ip": "2001:DB8:1202::222",
                "remote_port": 500,
                "encryption": "AES-CBC",
                "key_length": 256,
                "prf": "SHA512",
                "hash_algo": "SHA512",
                "dh_group": 21,
                "auth_sign": "PSK",
                "auth_verify": "PSK",
                "ake": {
                    "AKE1": "MLKEM1024"
                },
                "lifetime": 86400,
                "activetime": 19896,
                "ce_id": 0,
                "id": 18,
                "local_spi": "F26D83233C693382",
                "remote_spi": "C804F614076EB601",
                "child_sa": {
                    1: {
                        "local_selectors": [],
                        "remote_selectors": [],
                        "traffic_selectors": [
                            "2001:DB8:1101::222/0 - 2001:DB8:1101::222/65535    ->    2001:DB8:1202::222/0 - 2001:DB8:1202::222/65535"
                        ],
                        "esp_spi_in": "0x88EBB220",
                        "esp_spi_out": "0xDCE88BD6"
                    }
                }
            }
        }
    }
}

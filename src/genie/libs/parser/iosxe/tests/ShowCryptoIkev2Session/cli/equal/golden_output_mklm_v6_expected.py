expected_output = {
    "ikev2_session": {
        "IPv6": {
            1: {
                "session_id": 3,
                "status": "UP-ACTIVE",
                "ike_count": 1,
                "child_count": 1,
                "tunnel_id": 1,
                "fvrf": "none",
                "ivrf": "none",
                "session_status": "READY",
                "local_ip": "2001:DB8:1101::131",
                "local_port": 500,
                "remote_ip": "2001:DB8:1201::122",
                "remote_port": 500,
                "encryption": "AES-CBC",
                "key_length": 256,
                "prf": "SHA512",
                "hash_algo": "SHA512",
                "dh_group": 21,
                "auth_sign": "PSK",
                "auth_verify": "PSK",
                "pqc": "ML-KEM-1024",
                "lifetime": 86400,
                "activetime": 223,
                "ce_id": 0,
                "id": 3,
                "local_spi": "4CF87E32B25302C0",
                "remote_spi": "96254131FD306002",
                "child_sa": {
                    1: {
                        "local_selectors": [],
                        "remote_selectors": [],
                        "traffic_selectors": [
                            "2001:DB8:1101::131/0 - 2001:DB8:1101::131/65535    ->    2001:DB8:1201::122/0 - 2001:DB8:1201::122/65535"
                        ],
                        "esp_spi_in": "0x5CFCE807",
                        "esp_spi_out": "0x34A549BD"
                    }
                }
            },
            2: {
                "session_id": 4,
                "status": "UP-ACTIVE",
                "ike_count": 1,
                "child_count": 1,
                "tunnel_id": 2,
                "fvrf": "none",
                "ivrf": "none",
                "session_status": "READY",
                "local_ip": "2001:DB8:1101::131",
                "local_port": 500,
                "remote_ip": "2001:DB8:1202::123",
                "remote_port": 500,
                "encryption": "AES-CBC",
                "key_length": 256,
                "prf": "SHA512",
                "hash_algo": "SHA512",
                "dh_group": 21,
                "auth_sign": "PSK",
                "auth_verify": "PSK",
                "pqc": "ML-KEM-1024",
                "lifetime": 86400,
                "activetime": 212,
                "ce_id": 0,
                "id": 4,
                "local_spi": "DE66CA8E9F3AB6BD",
                "remote_spi": "DB3CED85555E739D",
                "child_sa": {
                    1: {
                        "local_selectors": [],
                        "remote_selectors": [],
                        "traffic_selectors": [
                            "2001:DB8:1101::131/0 - 2001:DB8:1101::131/65535    ->    2001:DB8:1202::123/0 - 2001:DB8:1202::123/65535"
                        ],
                        "esp_spi_in": "0x33125863",
                        "esp_spi_out": "0x6728BF4E"
                    }
                }
            }
        }
    }
}
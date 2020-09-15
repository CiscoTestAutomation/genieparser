expected_output = {
    "user_name": {
        "SNMPv3-alfa": {
            "engine_id": "800000090300002790FBCF00",
            "storage_type": "nonvolatile",
            "auth_protocol": "SHA",
            "priv_protocol": "AES128",
            "group_name": "ALFA"
        },
        "bob": {
            "engine_id": "800000090300001B53CEDC01",
            "storage_type": "nonvolatile",
            "auth_protocol": "SHA",
            "priv_protocol": "AES256",
            "group_name": "group1"
        },
        "bad2": {
            "engine_id": "800000090300001B53CEDC01",
            "storage_type": "nonvolatile",
            "auth_protocol": "MD5",
            "priv_protocol": "AES128",
            "group_name": "group1"
        },
        "bad3": {
            "engine_id": "800000090300001B53CEDC01",
            "storage_type": "nonvolatile",
            "auth_protocol": "MD5",
            "priv_protocol": "3DES",
            "group_name": "group1"
        },
        "bad4": {
            "engine_id": "800000090300001B53CEDC01",
            "storage_type": "nonvolatile",
            "auth_protocol": "SHA",
            "priv_protocol": "DES",
            "group_name": "group1"
        },
        "user1": {
            "engine_id": "800000090300001B53CEDC01",
            "storage_type": "nonvolatile",
            "auth_protocol": "SHA",
            "priv_protocol": "AES128",
            "group_name": "group1"
        },
        "nmsops": {
            "engine_id": "00000063000100A20A101B3E",
            "storage_type": "nonvolatile",
            "access_list": "69",
            "auth_protocol": "MD5",
            "priv_protocol": "DES",
            "group_name": "nmcigroup"
        }
    }
}
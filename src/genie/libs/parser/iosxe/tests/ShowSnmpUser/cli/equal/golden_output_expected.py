expected_output = {
    "SNMPv3-alfa": {
        "engine-id": "800000090300002790FBCF00",
        "storage-type": "nonvolatile",
        "auth-protocol": "SHA",
        "priv-protocol": "AES128",
        "group-name": "ALFA"
    },
    "bob": {
        "engine-id": "800000090300001B53CEDC01",
        "storage-type": "nonvolatile",
        "auth-protocol": "SHA",
        "priv-protocol": "AES256",
        "group-name": "group1"
    },
    "bad2": {
        "engine-id": "800000090300001B53CEDC01",
        "storage-type": "nonvolatile",
        "auth-protocol": "MD5",
        "priv-protocol": "AES128",
        "group-name": "group1"
    },
    "bad3": {
        "engine-id": "800000090300001B53CEDC01",
        "storage-type": "nonvolatile",
        "auth-protocol": "MD5",
        "priv-protocol": "3DES",
        "group-name": "group1"
    },
    "bad4": {
        "engine-id": "800000090300001B53CEDC01",
        "storage-type": "nonvolatile",
        "auth-protocol": "SHA",
        "priv-protocol": "DES",
        "group-name": "group1"
    },
    "user1": {
        "engine-id": "800000090300001B53CEDC01",
        "storage-type": "nonvolatile",
        "auth-protocol": "SHA",
        "priv-protocol": "AES128",
        "group-name": "group1"
    },
    "nmsops": {
        "engine-id": "00000063000100A20A101B3E",
        "storage-type": "nonvolatile",
        "access-list": "69",
        "auth-protocol": "MD5",
        "priv-protocol": "DES",
        "group-name": "nmcigroup"
    }
}
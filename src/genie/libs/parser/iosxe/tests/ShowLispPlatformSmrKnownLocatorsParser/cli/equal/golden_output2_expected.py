expected_output = {
    "vrf": "default",
    "address_family": "IPv6",
    "bits": 32,
    "locators": {
        "100:11:11::11": {
            "known_from": ["MS 100:44:44::44", "MS 100:55:55::55"]
        },
        "100:22:22::22": {
            "known_from": ["MS 100:44:44::44", "MS 100:55:55::55"]
        },
        "100:33:33::33": {
            "known_from": ["MS 100:44:44::44", "MS 100:55:55::55"]
        }
    }
}

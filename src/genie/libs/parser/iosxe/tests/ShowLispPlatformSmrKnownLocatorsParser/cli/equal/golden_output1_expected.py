expected_output = {
    "vrf": "default",
    "address_family": "IPv6",
    "bits": 32,
    "locators": {
        "2::2": {
            "known_from": ["MS 3::3"]
        },
        "4::4": {
            "known_from": ["MS 3::3"]
        },
        "6::6": {
            "known_from": ["MS 3::3"]
        }
    }
}

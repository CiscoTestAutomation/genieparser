expected_output = {
    "protocols": {
        "isis": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "default": {
                                    "outgoing_filter_list": "not set",
                                    "incoming_filter_list": "not set",
                                    "redistributing": "isis",
                                    "configured_interfaces": ["Serial0"],
                                    "preference": {"single_value": {"all": 115}},
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

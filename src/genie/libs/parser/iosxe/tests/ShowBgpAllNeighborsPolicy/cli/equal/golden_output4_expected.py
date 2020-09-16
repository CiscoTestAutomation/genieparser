expected_output = {
    "vrf": {
        "LABDR_HoC_AZS_Transit": {
            "neighbor": {
                "10.251.15.5": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "nbr_af_route_map_name_in": "HoC_AZSPREFIXES_in",
                            "nbr_af_route_map_name_out": "HoC_LOCALPREFIXES_out",
                        }
                    }
                }
            }
        }
    }
}

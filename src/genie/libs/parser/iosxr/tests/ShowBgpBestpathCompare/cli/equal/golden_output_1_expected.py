expected_output = {
	"vrf": {
		"default": {
			"address_family": {
				"ipv4 unicast": {
					"network": {
						"111.111.111.111/32": {
							"versions": {
								"process": "Speaker",
								"brib/rib": 5,
								"send_tbl_ver": 5
							},
							"paths": {
								"available_paths": 2,
								"best_path": 1,
								"Path 1": {
									"update_groups": [
										"0.1",
										"0.3"
									],
									"next_hop": "108.10.0.2",
									"gateway": "108.10.0.2",
									"originator": "192.68.33.108",
									"metric": 0,
									"localpref": 100,
									"weight": 100,
									"origin_codes": "i",
									"status_codes": "*>",
									"received_path_id": 0,
									"local_path_id": 1,
									"version": 5,
									"origin_as_validity": "disabled"
								},
								"Path 2": {
									"next_hop": "108.11.0.2",
									"gateway": "108.11.0.2",
									"originator": "192.68.33.108",
									"metric": 0,
									"localpref": 100,
									"origin_codes": "i",
									"status_codes": "*",
									"received_path_id": 0,
									"local_path_id": 0,
									"version": 0,
									"origin_as_validity": "disabled"
								}
							}
						}
					}
				}
			}
		}
	}
}
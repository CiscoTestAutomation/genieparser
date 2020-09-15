expected_output = {
    "qfp_tcam_usage_information": {
        "80_bit_region_information": {
            "name": "Leaf Region #0",
            "number_of_cells_per_entry": 1,
            "current_80_bit_entries_used": 0,
            "current_used_cell_entries": 0,
            "current_free_cell_entries": 0,
        },
        "160_bit_region_information": {
            "name": "Leaf Region #1",
            "number_of_cells_per_entry": 2,
            "current_160_bits_entries_used": 19,
            "current_used_cell_entries": 38,
            "current_free_cell_entries": 4058,
        },
        "320_bit_region_information": {
            "name": "Leaf Region #2",
            "number_of_cells_per_entry": 4,
            "current_320_bits_entries_used": 0,
            "current_used_cell_entries": 0,
            "current_free_cell_entries": 0,
        },
        "total_tcam_cell_usage_information": {
            "name": "TCAM #0 on CPP #0",
            "total_number_of_regions": 3,
            "total_tcam_used_cell_entries": 38,
            "total_tcam_free_cell_entries": 1048538,
            "threshold_status": "below critical limit",
        },
    }
}

expected_output = { 
    "power_stack": {
        "Powerstack-1": {
            "allocated_power": 575,
            "mode": "SP-PS",
            "power_supply_num": 1,
            "reserved_power": 0,
            "switch_num": 1,
            "switches": {
                1: {
                    "allocated_power": 575,
                    "available_power": 525,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 155,
                    "power_budget": 1100,
                    "power_supply_a": 1100,
                    "power_supply_b": 0
                }
            },
            "topology": "Stndaln",
            "total_power": 1100,
            "unused_power": 525
        },
        "Powerstack-2": {
            "allocated_power": 575,
            "mode": "SP-PS",
            "power_supply_num": 1,
            "reserved_power": 0,
            "switch_num": 1,
            "switches": {
                2: {
                    "allocated_power": 575,
                    "available_power": 525,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 155,
                    "power_budget": 1100,
                    "power_supply_a": 1100,
                    "power_supply_b": 0
                }
            },
            "topology": "Stndaln",
            "total_power": 1100,
            "unused_power": 525
        }
    },
    "totals": {
        "total_allocated_power": 1150,
        "total_available_power": 1050,
        "total_consumed_power_poe": 0,
        "total_consumed_power_sys": 310
    }
}

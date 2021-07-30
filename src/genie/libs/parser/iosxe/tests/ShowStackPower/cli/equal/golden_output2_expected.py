expected_output = {
    "power_stack": {
        "Powerstack-1": {
            "allocated_power": 1180,
            "mode": "SP-PS",
            "power_supply_num": 5,
            "reserved_power": 35,
            "switch_num": 4,
            "switches": {
                1: {
                    "allocated_power": 240,
                    "available_power": 960,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 129,
                    "power_budget": 1200,
                    "power_supply_a": 0,
                    "power_supply_b": 0
                },
                2: {
                    "allocated_power": 240,
                    "available_power": 990,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 131,
                    "power_budget": 1230,
                    "power_supply_a": 1100,
                    "power_supply_b": 715
                },
                3: {
                    "allocated_power": 240,
                    "available_power": 990,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 127,
                    "power_budget": 1230,
                    "power_supply_a": 1100,
                    "power_supply_b": 1100
                },
                4: {
                    "allocated_power": 460,
                    "available_power": 960,
                    "consumed_power_poe": 0,
                    "consumed_power_sys": 143,
                    "power_budget": 1420,
                    "power_supply_a": 1100,
                    "power_supply_b": 0
                }
            },
            "topology": "Ring",
            "total_power": 5115,
            "unused_power": 3900
        }
    },
    "totals": {
        "total_allocated_power": 1180,
        "total_available_power": 3900,
        "total_consumed_power_poe": 0,
        "total_consumed_power_sys": 530
    }
}
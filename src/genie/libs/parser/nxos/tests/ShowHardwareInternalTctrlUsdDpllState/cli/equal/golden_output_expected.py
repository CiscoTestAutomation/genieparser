expected_output = {
    "dpll_hw_state": {
        "inst": {
            0: {
                "dpll": {
                    0: {
                        "dpll_mon_status": "(0x0118): 0x02: in Holdover",
                        "lock": "No",
                        "ho": "Yes",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            0: {
                                "mode": "Automatic",
                                "refId": "INVALID"
                            }
                        },
                        "nco_assist_pair_hw_lock_status": "Ref Failed(4)",
                        "psl": {
                            885: {
                                "bandwidth": 7,
                                "var_bw": 79,
                                "pullinrange": 0
                            }
                        }
                    },
                    1: {
                        "dpll_mon_status": "(0x0119): 0x02: in Holdover",
                        "lock": "No",
                        "ho": "Yes",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            1: {
                                "mode": "Automatic",
                                "refId": "INVALID"
                            }
                        },
                        "psl": {
                            7500: {
                                "bandwidth": 7,
                                "var_bw": 135,
                                "pullinrange": 0
                            }
                        }
                    },
                    3: {
                        "dpll_mon_status": "(0x011b): 0x02: in Holdover",
                        "lock": "No",
                        "ho": "Yes",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            3: {
                                "mode": "Automatic",
                                "refId": "INVALID"
                            }
                        },
                        "psl": {
                            7500: {
                                "bandwidth": 7,
                                "var_bw": 135,
                                "pullinrange": 0
                            }
                        }
                    }
                }
            }
        },
        "refclk": {
            "ZL30XXX_REF0P(0)": {
                "measured_freq": 7743,
                "freq_err": "NA"
            },
            "ZL30XXX_REF0N(1)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF1P(2)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF1N(3)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF2P(4)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF2N(5)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF3P(6)": {
                "measured_freq": 6,
                "freq_err": "NA"
            },
            "ZL30XXX_REF3N(7)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF4P(8)": {
                "measured_freq": 24575988,
                "freq_err": "-0.488"
            },
            "ZL30XXX_REF4N(9)": {
                "measured_freq": 0,
                "freq_err": "NA"
            }
        }
    }
}
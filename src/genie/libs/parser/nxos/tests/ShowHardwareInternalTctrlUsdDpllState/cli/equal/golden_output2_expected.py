expected_output = {
    "dpll_hw_state": {
        "inst": {
            0: {
                "dpll": {
                    0: {
                        "dpll_mon_status": "(0x0110): 0x02: in Holdover",
                        "lock": "No",
                        "ho": "Yes",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            0: {
                                "mode": "Automatic",
                                "refId": "ZL30XXX_REF0P"
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
                    1: {
                        "dpll_mon_status": "(0x0111): 0x04: Check the status below",
                        "lock": "No",
                        "ho": "No",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            1: {
                                "mode": "NCO",
                                "refId": "INVALID"
                            }
                        },
                        "nco_assist_pair_hw_lock_status": "Ref Failed(4)",
                        "psl": {
                            0: {
                                "bandwidth": 0,
                                "var_bw": 0,
                                "pullinrange": 0
                            }
                        }
                    },
                    5: {
                        "dpll_mon_status": "(0x0115): 0x02: in Holdover",
                        "lock": "No",
                        "ho": "Yes",
                        "step_time_in_progress": "No",
                        "flhit": "No",
                        "pslhit": "No",
                        "dpll": {
                            5: {
                                "mode": "Automatic",
                                "refId": "ZL30XXX_REF0P"
                            }
                        },
                        "psl": {
                            0: {
                                "bandwidth": 7,
                                "var_bw": 141,
                                "pullinrange": 0
                            }
                        }
                    }
                }
            }
        },
        "refclk": {
            "ZL30XXX_REF0P(0)": {
                "measured_freq": 0,
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
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF3N(7)": {
                "measured_freq": 0,
                "freq_err": "NA"
            },
            "ZL30XXX_REF4P(8)": {
                "measured_freq": 12800042,
                "freq_err": "3.281"
            },
            "ZL30XXX_REF4N(9)": {
                "measured_freq": 0,
                "freq_err": "NA"
            }
        }
    }
}
expected_output ={
        'interface':{
            'FiftyGigE2/0/45.2': {
                'Interface_Scheduler': {
                    'CIR': {
                        'Credit': 20000000000,
                        'Transmit': 20000000000,
                        'Weight': 1
                        },
                    'PIR': {
                        'Credit': 20000000000,
                        'Transmit': 20000000000,
                        'Weight': 1
                        }
                    },
                'Interface_Scheduler_OQPG': {
                    'PG_TYPE': {
                        'Credit Burst': {
                            'OQPG_0': '0',
                            'OQPG_1': '0',
                            'OQPG_2': '0',
                            'OQPG_3': '0',
                            'OQPG_4': '0',
                            'OQPG_5': '0',
                            'OQPG_6': '0',
                            'OQPG_7': 'SDK ''Default'
                                },
                        'Credit CIR': {
                            'OQPG_0': '0',
                            'OQPG_1': '0',
                            'OQPG_2': '0',
                            'OQPG_3': '0',
                            'OQPG_4': '0',
                            'OQPG_5': '0',
                            'OQPG_6': '0',
                            'OQPG_7': '60000000000'
                            },
                        'OQ List': {
                            'OQPG_0': '0',
                            'OQPG_1': '1',
                            'OQPG_3': '3',
                            'OQPG_4': '4',
                            'OQPG_5': '5',
                            'OQPG_6': '6',
                            'OQPG_7': '2 7'
                                      },
                        'Transmit CIR': {
                            'OQPG_0': '0',
                            'OQPG_1': '0',
                            'OQPG_2': '0',
                            'OQPG_3': '0',
                            'OQPG_4': '0',
                            'OQPG_5': '0',
                            'OQPG_6': '0',
                            'OQPG_7': '60000000000'
                            }
                        }
                    },
                'LPSE_CIR_Burst': 'SDK ''Default',
                'LPSE_CIR_Rate': 2000000000,
                'LPSE_OID': 3138,
                'LPSE_PIR_Rate': 2000000000,
                'OQPG': {
                        'Credit Burst': {
                            'LPSE_OQ_0': 'SDK ''Default',
                            'LPSE_OQ_1': 'SDK ''Default'
                            },
                        'Credit PIR': {
                            'LPSE_OQ_0': '20000000000',
                            'LPSE_OQ_1': '20000000000'
                            },
                        'Transmit Burst': {
                            'LPSE_OQ_0': 'SDK ''Default',
                            'LPSE_OQ_1': 'SDK ''Default'
                            },
                        'Transmit PIR': {
                            'LPSE_OQ_0': '20000000000',
                            'LPSE_OQ_1': '20000000000'
                            }
                        },
                'port_Scheduler': {
                        'Interface_SCH_OID': 3125,
                        'Logical_Port': 'Enabled',
                        'Priority_Propagation': 'Disabled',
                        'Sub_interface_Q_Mode': 'Enabled',
                        'System_Port_SCH_OID': 3129,
                        'TC_Profile': {
                            'SDK_OID': 110,
                            'TC': {
                                'TC0': 0,
                                'TC1': 0,
                                'TC2': 0,
                                'TC3': 0,
                                'TC4': 0,
                                'TC5': 0,
                                'TC6': 0,
                                'TC7': 2
                                }
                            }
                        },
                'oq_credit_cir': 2000000000,
                'oq_credit_pir': 2000000000,
                'oq_credit_pir_burst': 'SDK',
                'oq_id': 0,
                'oq_scheduling_mode': 'Logical',
                'oqse_oid': 4234
                }
                }
                } 

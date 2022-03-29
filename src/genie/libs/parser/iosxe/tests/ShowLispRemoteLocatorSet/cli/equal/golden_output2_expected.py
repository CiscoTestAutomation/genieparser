expected_output = {
    'lisp_id': {
        0: {
            'remote_locator_name': {
                'default-etr-locator-set-ipv4': {
                    'rloc': {
                        '10.0.1.2':{
                            'instance_id':{
                                4098:{
                                    'priority': '255',
                                    'weight': '1 ',
                                    'metric': '-',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Service',
					                'srvc_ins_id': 'SS/1'
                                },
                                4099:{
                                    'priority': '1',
                                    'weight': '1 ',
                                    'metric': '-',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Service',
					                'srvc_ins_id': 'SS/1'
                                }
                            }
                        },
                        '10.0.1.5':{
                            'instance_id':{
                                4098:{
                                    'priority': '1',
                                    'weight': '1 ',
                                    'metric': '0',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Default',
                                    'srvc_ins_id': 'P',
									'srvc_ins_type': '-'
                                },
                                4099:{
                                    'priority': '1',
                                    'weight': '1 ',
                                    'metric': '0',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Default',
                                    'srvc_ins_id': 'P',
									'srvc_ins_type': '-'
                                }
                            }
                        },
                        '10.0.11.2':{
                            'instance_id':{
                                4098:{
                                    'priority': '255',
                                    'weight': '1 ',
                                    'metric': '-',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Service',
					                'srvc_ins_id': 'SS/1'
                                },
                                4099:{
                                    'priority': '255',
                                    'weight': '1 ',
                                    'metric': '-',
                                    'domain_id': '0',
                                    'multihome_id': '0',
                                    'etr_type': 'Service',
					                'srvc_ins_id': 'SS/1'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
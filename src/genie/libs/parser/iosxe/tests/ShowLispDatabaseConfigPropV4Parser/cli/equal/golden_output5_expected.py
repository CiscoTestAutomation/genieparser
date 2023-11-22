expected_output = {
    'lisp_id':{
        0:{
            'instance_id':{
                7000:{
                    'eid_table':'vrf test7000',
                    'lsb':'0x1',
                    'entries':1,
                    'no_route':0,
                    'inactive':0,
                    'do_not_register':0,
                    'eid_prefix':{
                        '70.70.0.0/16':{
                            'eid':'70.70.0.0',
                            'mask':'16',
                            'import_from':'publication cfg prop',
                            'inherited_from':'default locator-set RLOC',
                            'auto_disc_rloc':True,
                            'proxy':True,
                            'up_time':'06:30:26',
                            'last_change':'06:30:26',
                            'service_insertion':'N/A',
                            'extranet_iid':7000,
                            'locators':{
                                '100:88:88:88::':{
                                    'priority':10,
                                    'weight':50,
                                    'source':'cfg-intf',
                                    'state':'site-self, reachable'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

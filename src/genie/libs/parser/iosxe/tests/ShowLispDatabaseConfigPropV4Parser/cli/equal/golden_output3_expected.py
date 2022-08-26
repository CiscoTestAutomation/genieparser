expected_output ={
   'lisp_id':{
      0:{
         'instance_id':{
            5000:{
               'eid_table':'vrf internet',
               'lsb':'0x3',
               'entries':7,
               'no_route':0,
               'inactive':0,
               'do_not_register':0,
               'eid_prefix':{
                  '51.51.0.0/16':{
                     'eid':'51.51.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':5000,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '88.88.0.0/16':{
                     'eid':'88.88.0.0',
                     'mask':'16',
                     'import_from':'publication',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:24:54',
                     'last_change':'06:24:54',
                     'service_insertion':'N/A',
                     'extranet_iid':5000,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        },
                        '100.99.99.99':{
                           'priority':10,
                           'weight':50,
                           'source':'auto-disc',
                           'state':'site-other, report-reachable'
                        }
                     }
                  },
                  '172.168.0.0/16':{
                     'eid':'172.168.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':4100,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '173.168.0.0/16':{
                     'eid':'173.168.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':4101,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '182.168.0.0/16':{
                     'eid':'182.168.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':4100,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '192.168.0.0/16':{
                     'eid':'192.168.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':4100,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '193.168.0.0/16':{
                     'eid':'193.168.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':4101,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  }
               }
            },
            6000:{
               'eid_table':'vrf test6000',
               'lsb':'0x1',
               'entries':2,
               'no_route':0,
               'inactive':0,
               'do_not_register':0,
               'eid_prefix':{
                  '60.60.0.0/16':{
                     'eid':'60.60.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':6000,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '61.61.0.0/16':{
                     'eid':'61.61.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':6100,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  }
               }
            },
            7000:{
               'eid_table':'vrf test7000',
               'lsb':'0x1',
               'entries':2,
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
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':7000,
                     'locators':{
                        '100.88.88.88':{
                           'priority':10,
                           'weight':50,
                           'source':'cfg-intf',
                           'state':'site-self, reachable'
                        }
                     }
                  },
                  '71.71.0.0/16':{
                     'eid':'71.71.0.0',
                     'mask':'16',
                     'import_from':'publication cfg prop',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'06:28:39',
                     'last_change':'06:28:39',
                     'service_insertion':'N/A',
                     'extranet_iid':7100,
                     'locators':{
                        '100.88.88.88':{
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
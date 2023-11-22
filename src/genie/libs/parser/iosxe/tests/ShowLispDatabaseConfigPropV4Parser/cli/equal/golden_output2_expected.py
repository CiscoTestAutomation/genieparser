expected_output ={
   'lisp_id':{
      0:{
         'instance_id':{
            5000:{
               'eid_table':'vrf internet',
               'lsb':'0x3',
               'entries':1,
               'no_route':0,
               'inactive':0,
               'do_not_register':0,
               'eid_prefix':{
                  '88.88.0.0/16':{
                     'eid':'88.88.0.0',
                     'mask':'16',
                     'import_from':'publication',
                     'inherited_from':'default locator-set RLOC',
                     'auto_disc_rloc':True,
                     'proxy':True,
                     'up_time':'04:29:46',
                     'last_change':'04:29:46',
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
                     },
                     'map_servers':{
                        '100.77.77.77':{
                           'uptime':'04:29:46',
                           'ack':'Yes',
                           'domain_id':'4'
                        },
                        '100.78.78.78':{
                           'uptime':'04:29:46',
                           'ack':'Yes',
                           'domain_id':'4'
                        }
                     }
                  }
               }
            }
         }
      }
   }
}
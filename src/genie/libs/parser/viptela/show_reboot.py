'''
* 'show reboot history'
'''
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show reboot history'
# ===========================================


class ShowRebootHistorySchema(MetaParser):
    """ Schema for "show reboot history" """

    schema = {
        'reboot_date_time': {
            str: {
                'reboot_reason': str,
            }
        }
    }
# ===========================================
# Parser for 'show reboot history'
# ===========================================

class ShowRebootHistory(ShowRebootHistorySchema):
    """ Parser for "show reboot history" """

    cli_command = "show reboot history"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # REBOOT DATE TIME           REBOOT REASON                                 
        # -------------------------------------------------------------------------
        # 2020-06-04T04:54:36+00:00  Initiated by user                             
        # 2020-06-16T09:19:57+00:00  Initiated by user                             
        # 2020-06-18T13:28:53+00:00  Initiated by user - activate 99.99.999-4542   
        # 2020-06-18T13:46:43+00:00  Software initiated - activate 99.99.999-4499  
        # 2020-06-18T14:03:24+00:00  Initiated by user - activate 99.99.999-4542   
        # 2020-06-18T14:20:11+00:00  Software initiated - activate 99.99.999-4499  
        # 2020-07-06T08:49:18+00:00  Initiated by user - activate 99.99.999-4567
        if out:
            out = pg.oper_fill_tabular(device_output=out,
                                    header_fields=["REBOOT DATE TIME", "REBOOT REASON"],
                                    index=[0])
            return_dict = out.entries
            reboot_date_time ={}
            for keys in return_dict.keys() :
                dict1={}
                dict1['reboot_reason'] = return_dict[keys]['REBOOT REASON']
                reboot_date_time[keys] = dict1
            parsed_dict['reboot_date_time'] = reboot_date_time
        return parsed_dict
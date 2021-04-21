# Metaparser
from genie.metaparser import MetaParser
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show app-hosting list'
# ===========================================

class ShowApphostingListSchema(MetaParser):
    """ Schema for show app-hosting list """
    schema = {
        'app_id': {
            str: {
                'state': str,
                }
            }
         }
# ===========================================
# Parser for 'show app-hosting list'
# ===========================================
class ShowApphostingList(ShowApphostingListSchema):
    """ Parser for "show app-hosting list" """

    cli_command = "show app-hosting list"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # App id                                   State                                                                                                            
        # ---------------------------------------------------------                                                                                                 
        # utd                                      RUNNING   
        if out:
            out = pg.oper_fill_tabular(device_output=out,
                                    header_fields=["App id", "State"],
                                    index=[0])
            return_dict = out.entries
            app_id ={}
            for keys in return_dict.keys() :
                app_dict={}
                app_dict['state'] = return_dict[keys]['State']
                app_id[keys] = app_dict
            parsed_dict['app_id'] = app_id
        return parsed_dict
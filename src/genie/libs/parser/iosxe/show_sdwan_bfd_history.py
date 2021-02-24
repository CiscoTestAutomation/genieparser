'''
show sdwan bfd history'''

#Genie Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,Or,And,Default,Use
import genie.parsergen as pg
#Python
import re

class ShowSdwanBfdHistorySchema(MetaParser):
    
    """schema for show sdwan bfd history"""

    schema={
        'site_id':
        {
            Any():
            {
                'system_ip':
                {
                    Any():
                    {
                        'dst_public_ip':
                        {
                            Any():
                            {
                                'time':
                                {
                                    Any():
                                    {
                                        'color': str,
                                        'state': str,
                                        'dst_public_port': str,
                                        'encap': str,
                                        'rx_pkts': str,
                                        'tx_pkts' : str,
                                        'del': str
                                    },   
                                }
                            },
                        }
                    },               
                }
            },
        }
    }
            
class ShowSdwanBfdHistory(ShowSdwanBfdHistorySchema):
    """parser for show sdwan bfd history"""

    cli_command= 'show sdwan bfd history'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Removing unneccessary header
        try:
            strout= re.findall(r'\s+[DST PUBLIC \s]+RX+\s+TX+\s',out)
            out=out.replace(strout[0],"")
        except:
            out=out


        #parsed output using parsergen
        parsed_out = pg.oper_fill_tabular(device_output=out,  
                                    header_fields=["SYSTEM IP", "SITE ID", "COLOR", "STATE", "IP", "PORT", "ENCAP","TIME","PKTS","PKTS","DEL"],
                                    label_fields=["system_ip", "site_id", "color", "state", "dst_public_ip", "dst_public_port","encap","time","rx_pkts","tx_pkts","del"], 
                                    index= [1,0,4,7]
                                    )

        #creating a parsed dict using the output
        parsed_dict = parsed_out.entries

        #Parsing the dict according to the schema
        out_dict={}
        out_dict['site_id']={}
        cur_dict=out_dict['site_id']



        for key in parsed_dict.keys():
            cur_dict[key]={}
            cur_dict[key]['system_ip']={}
            for subkey in parsed_dict[key].keys():
                cur_dict[key]['system_ip'][subkey]={}
                cur_dict[key]['system_ip'][subkey]['dst_public_ip']={}
                for subsubkey in parsed_dict[key][subkey].keys():
                    cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]={}
                    cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time']={}
                    for subsubsubkey in parsed_dict[key][subkey][subsubkey].keys():
                        cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time'][subsubsubkey]={}
                        for valuekey in parsed_dict[key][subkey][subsubkey][subsubsubkey].keys():
                            if valuekey not in ['site_id','system_ip','dst_public_ip','time']:
                                cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time'][subsubsubkey][valuekey]=parsed_dict[key][subkey][subsubkey][subsubsubkey][valuekey]


        return out_dict


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
        Any():
        {
            Any():
            {
                Any():
                {
                    Any():
                    {
                        Any():
                        {
                            Any():
                            {
                                'system_ip': str,
                                'site_id': str,
                                'color': str,
                                'state': str,
                                'dst_public_ip': str,
                                'dst_public_port': str,
                                'encap': str,
                                'time': str,
                                'rx_pkts': str,
                                'tx_pkts' : str,
                                'del': str
                            },
                        },
                    },               
                },
            },
        },
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
                                    index= [0,1,2,3,4,7]
                                    )

        #creating a parsed dict using the output
        parsed_dict = parsed_out.entries

        return parsed_dict


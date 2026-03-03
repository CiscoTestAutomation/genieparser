"""show_stackwise.py
   supported commands:
     * 'show stackwise-virtual link'

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional



class ShowStackwiseVirtualLinkSchema(MetaParser):
    """Schema for show stackwise-virtual link"""

    schema = {
        'switch':{
                int:{
                    'svl':{
                        int:{
                            Optional('ports'):{
                                Any():{
                                    'link_status':str,
                                    'protocol_status':str,
                                }
                            }
                        }
                    }    
                }
            }
        }

class ShowStackwiseVirtualLink(ShowStackwiseVirtualLinkSchema):
    """Parser for show stackwise-virtual link"""
 
    cli_command = 'show stackwise-virtual link'
   
    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output
       
        ret_dict = {}
        link_status_map = {
            'U': 'Up',
            'D': 'Down',
        }
        protocol_status_map = {
            'S': 'Suspended',
            's': 'Suspended',
            'P': 'Pending',
            'p': 'Pending',
            'E': 'Error',
            'e': 'Error',
            'T': 'Timeout',
            't': 'Timeout',
            'R': 'Ready',
            'r': 'Ready',
        }

        #    Switch	SVL	  Ports                  Link-Status	Protocol-Status

        #    ------	---	  -----                  -----------	---------------
        #      1    1     HundredGigE1/0/1          U             P
        #                 HundredGigE1/0/6          U             P        
        p1 = re.compile(r'^(?P<switch>\d+) +(?P<svl>\d+) +(?P<ports>\S+) +(?P<link_status>\S+) +(?P<protocol_status>\S+)$')
        p2 = re.compile(r'^(?P<ports>\S+) +(?P<link_status>\S+) +(?P<protocol_status>\S+)$')

        for line in out.splitlines():
            line = re.sub(r'\t', '   ', line)
            line = line.strip()

            #                       1       1       HundredGigE1/0/1                U               P
            m =  p1.match(line)
            if m:
               group = m.groupdict()
               #svl_port_dict = ret_dict.setdefault('svl_port', {})
               switches_dict = ret_dict.setdefault('switch',{})  
               switch_id_dict = switches_dict.setdefault(int(group['switch']),{})
               svl_dict = switch_id_dict.setdefault('svl',{})
               svl_id_dict = svl_dict.setdefault(int(group['svl']),{})
               port_dict = svl_id_dict.setdefault('ports',{})
               port_id_dict = port_dict.setdefault(str(group['ports']),{})
               port_id_dict.update({  
                'link_status' : link_status_map.get(str(group['link_status']), str(group['link_status'])),
                'protocol_status' : protocol_status_map.get(str(group['protocol_status']), str(group['protocol_status']))
                })
               continue

            #  HundredGigE1/0/6                U               P
            m =  p2.match(line)
            if m:
                group = m.groupdict()
                port_id_dict = port_dict.setdefault(str(group['ports']),{})
                port_id_dict.update({  
                    'link_status' : link_status_map.get(str(group['link_status']), str(group['link_status'])),
                    'protocol_status' : protocol_status_map.get(str(group['protocol_status']), str(group['protocol_status']))
                    })
                continue
        return ret_dict

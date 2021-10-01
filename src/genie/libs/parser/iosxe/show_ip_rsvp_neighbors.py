''' show_ip_rsvp_neighbors.py

IOSXE parsers for the following show commands:

    * 'show ip rsvp neighbors'
    * 'show ip rsvp neighbors inactive'
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

log = logging.getLogger(__name__)

class ShowIpRsvpNeihborsSchema(MetaParser):
    """Schema for show ip rsvp neighbors"""

    schema = {
        'neighbors':{
	        Any(): {
                'encapsulation':str,
                'time_since_msg_rcvd':str,
                'time_since_msg_sent':str
            }
        }
    }
        
class ShowIpRsvpNeihbor(ShowIpRsvpNeihborsSchema):
    """show ip rsvp neighbors
    """

    cli_command = [
                'show ip rsvp neighbor'
                ]

    def cli(self, output=None):
        if not output:
            cmd = self.cli_command[0]            
            output = self.device.execute(cmd)
    
        res={}

        if not output.strip():
            return res
            
        res['neighbors']={}
        result=1
            
        ###192.1.1.2       Raw IP         00:35:18   00:34:58  
        p1=re.compile(r"(?P<neighbor>\d+\.\d+\.\d+\.\d+)\s+(?P<encapsulation>[a-zA-Z ]+)\s+(?P<time_since_msg_rcvd>\S+)\s+(?P<time_since_msg_sent>\S+)")

        for line in output.splitlines():
            line=line.strip()
            m1=p1.match(line)
            if m1:
                res1=m1.groupdict()
                neigh=res1['neighbor']
                del res1['neighbor']
                res['neighbors'][neigh]={}
                for key,value in res1.items():
                    res['neighbors'][neigh][key]=value.strip()
        return res

class ShowIpRsvpNeihborinactive(ShowIpRsvpNeihbor):
    """show ip rsvp neighbors
    """

    cli_command = [
                'show ip rsvp neighbor inactive'
                ]
                
    def cli(self, output=None):
        if not output:
            cmd = self.cli_command[0]            
            output = self.device.execute(cmd)
            
        return super().cli(output=output)
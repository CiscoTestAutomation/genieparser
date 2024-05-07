"""
IOSXE C9300 parsers for the following show commands:
     * show post
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowPostSchema(MetaParser):
    """
    Schema for show post
    """

    schema = {
        'switch':{
            Any():{
                'test':{
                    Any():{
                        'status': bool,
                    }
                }
            }
        }
    }             


class ShowPost(ShowPostSchema):
    """ Parser for show post """

    # Parser for 'show post'
    cli_command = 'show post' 

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
       
        # initial variables
        ret_dict={}

        # Switch 1
        p1 = re.compile('^Switch\s+(?P<switch_num>\S+)$')

        # POST: PHY Loopback: loopback Test : End, Status Passed
        # POST: Thermal, Temperature Tests : End, Status Passed
        # POST: CRYPTO Tests : End, Status Passed
        p2 = re.compile('^POST.*:(?P<test>.+Tests*)\s+:\s+End, Status (?P<status>Passed|Failed)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Switch 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch',{}).setdefault(group['switch_num'],{}).setdefault('test',{})
                continue
                
            # POST: PHY Loopback: loopback Test : End, Status Passed
            # POST: Thermal, Temperature Tests : End, Status Passed
            # POST: CRYPTO Tests : End, Status Passed
            m = p2.match(line)
            if m:
                group=m.groupdict()
                test_key = group['test'].strip().lower().replace(',', '').replace(' ', '_')
                status = True if group['status'] == 'Passed' else False
                root_dict.setdefault(test_key, {}).setdefault('status', status)
                continue
                
        return ret_dict

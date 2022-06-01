"""show_post.py
   supported commands:
     * show post
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show parser encrypt file status'
# =============================================

class ShowPostSchema(MetaParser):
    """
    Schema for show post
    """

    schema = {
        Optional('switch'):{
            Any():{
                'test':{
                    Any():{
                        'status':bool,
                        },
                    },
                },
            },
        }
                    


class ShowPost(ShowPostSchema):
    """ Parser for show post """

    # Parser for 'show post'
    cli_command = 'show post' 

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
       
        # initial variables
        ret_dict={}

        # Switch 1
        p1 = re.compile('^Switch\s+(?P<switch_num>\S+)$')

        # Wed Feb 23 23:06:58 2022 POST: Module: 1 Mac Loopback: loopback Test: End, Status Passed
        p2 = re.compile('^[\w: ]+POST:\s+Module:[\w ]+: (?P<test>\w+\sTest):\s+End,\s+Status\s+(?P<status>Passed|Failed)$')

        for line in output.splitlines():
            line = line.strip()
            # Switch 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch',{}).setdefault(group['switch_num'],{}).setdefault('test',{})
                continue
                
            # Wed Feb 23 23:06:58 2022 POST: Module: 1 Mac Loopback: loopback Test: End, Status Passed
            m = p2.match(line)
            if m:
                group=m.groupdict()
                status = True if \
                    group['status'] == 'Passed' else\
                    False
               
                root_dict.update({group['test']:{'status':status}})
                continue
                
        return ret_dict


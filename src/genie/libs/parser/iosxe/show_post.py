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
        'test':{
            Any():{
            'status':bool,
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
        
        #Sun Oct  6 01:29:58 2019 POST: Module: 1 Mac Loopback: loopback Test: End, Status Passed
        p1=re.compile('^\w+\s+\w+.*POST: Module:\s\d\s\w+\s\S+: (?P<test>\w+\sTest): \w+\,\s+Status (?P<status>Passed|Failed)$')

        for line in output.splitlines():
            line=line.strip()
            
            #Sun Oct  6 01:29:58 2019 POST: Module: 1 Mac Loopback: loopback Test: End, Status Passed
            m=p1.match(line)
            if m:
                group=m.groupdict()
                root_dict=ret_dict.setdefault('test',{})
                status = True if \
                    group['status'] == 'Passed' else\
                    False
               
                root_dict.setdefault(group['test'],{'status':status})
                continue
                
        return ret_dict
"""show_spanning_tree_instances.py
   supported commands:
     *  show spanning-tree instances

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowSpanningTreeInstancesSchema(MetaParser):
    """Schema for show spanning-tree instances"""
    schema = {
        'vlan_count': int
    }

class ShowSpanningTreeInstances(ShowSpanningTreeInstancesSchema):
    """Parser for show spanning-tree instances"""

    cli_command = 'show spanning-tree instances'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern for
        # "MAX STP instances supported is 4093"
        p = re.compile(r'^(?P<summary>[^.]+)\s+(?P<vlan_count>[\d]+)$')

        for line in out.splitlines():
            line = line.strip()
            # MAX STP instances supported is 4093
            m = p.match(line)
            if m:
                ret_dict['vlan_count'] = int(m.groupdict()['vlan_count'])

        # {'vlan_count': 4093}   
        return ret_dict

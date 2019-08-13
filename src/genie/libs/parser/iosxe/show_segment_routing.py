'''
show_segment_routing.py
IOSXE parsers for the following show commands:
	* 'show segment-routing mpls lb lock'
'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ==============================================
# Parser for 'show segment-routing mpls lb lock'
# ==============================================

class ShowSegmentRoutingMplsLbLockSchema(MetaParser):
    """Schema for show segment-routing mpls lb lock
    """

    schema = {
        'label_min': int,
        'label_max': int
    }

class ShowSegmentRoutingMplsLbLock(ShowSegmentRoutingMplsLbLockSchema):
    """ Parser for show segment-routing mpls lb lock"""
    
    cli_command = 'show segment-routing mpls lb lock'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # SR LB (15000, 15999) Lock Users :
        p1 = re.compile(r'^SR +LB +\((?P<label_min>\d+)\, +'
            '(?P<label_max>\d+)\) +Lock +Users +:')
        
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # SR LB (15000, 15999) Lock Users :
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_min = int(group['label_min'])
                label_max = int(group['label_max'])

                ret_dict.update({'label_min': label_min})
                ret_dict.update({'label_max': label_max})
                
                continue

        return ret_dict
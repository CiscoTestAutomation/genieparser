'''
show_segment_routing.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional
                                         
# =============================================
# Parser for 'show segment-routing mpls state'
# =============================================

class ShowSegmentRoutingMplsStateSchema(MetaParser):
    """Schema for show segment-routing mpls state
    """

    schema = {
        'sr_mpls_state': str
    }

class ShowSegmentRoutingMplsState(ShowSegmentRoutingMplsStateSchema):
    """ Parser for show segment-routing mpls state"""
    
    cli_command = 'show segment-routing mpls state'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        
        # Segment Routing MPLS State : ENABLED
        p1 = re.compile(r'^Segment +Routing +MPLS +State +: +(?P<state>\S+)$')
        
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Segment Routing MPLS State : ENABLED
            m = p1.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                ret_dict.update({'sr_mpls_state': state})
                continue
        
        return ret_dict
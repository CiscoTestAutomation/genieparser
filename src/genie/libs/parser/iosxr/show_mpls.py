''' show_mpls.py

IOSXR parsers for the following show commands:
    * 'show mpls ldp neighbor brief'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# ======================================================
# Parser for 'show mpls ldp neighbor brief'
# ======================================================

class ShowMplsLdpNeighborBriefSchema(MetaParser):
    
    """Schema for show mpls ldp neighbor brief"""

    schema = {
        'peer': { 
            Any(): { 
                'gr': str,
                'nsr': str,
                'up_time': str,
                'discovery': { 
                    'ipv4': int,
                    'ipv6': int,
                },
                'addresses': { 
                    'ipv4': int,
                    'ipv6': int,
                },
                'labels': { 
                    'ipv4': int,
                    'ipv6': int,
                },
            },
        },
    }

class ShowMplsLdpNeighborBrief(ShowMplsLdpNeighborBriefSchema):

    """Parser for show mpls ldp neighbor brief"""

    cli_command = 'show mpls ldp neighbor brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Init vars
        mpls_dict = {}
        peer = ''
        
        for line in out.splitlines():
            line = line.rstrip()

            # Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
            #                                         ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
            # -----------------  --  ---  ----------  ----------  ----------  ------------
            # 10.205.2.254:0     Y   Y    31w0d       2     0     10    0     77     0
            p1 = re.compile(r'^\s*(?P<peer>[\d\.:]+)\s+(?P<gr>[\w]+)\s+(?P<nsr>[\w]+)\s+(?P<up_time>[\w\d]+)\s+(?P<discovery_ipv4>[\d]+)\s+(?P<discovery_ipv6>[\d]+)\s+(?P<addresses_ipv4>[\d]+)\s+(?P<addresses_ipv6>[\d]+)\s+(?P<labels_ipv4>[\d]+)\s+(?P<labels_ipv6>[\d]+)\s*$')
            m = p1.match(line)
            if m:
                peer = m.groupdict()['peer']
                mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                mpls_dict['peer'][peer]['gr'] = m.groupdict()['gr']
                mpls_dict['peer'][peer]['nsr'] = m.groupdict()['nsr']
                mpls_dict['peer'][peer]['up_time'] = m.groupdict()['up_time']

                mpls_dict['peer'][peer]['discovery'] = {}
                mpls_dict['peer'][peer]['discovery']['ipv4'] = int(m.groupdict()['discovery_ipv4'])
                mpls_dict['peer'][peer]['discovery']['ipv6'] = int(m.groupdict()['discovery_ipv6'])

                mpls_dict['peer'][peer]['addresses'] = {}
                mpls_dict['peer'][peer]['addresses']['ipv4'] = int(m.groupdict()['addresses_ipv4'])
                mpls_dict['peer'][peer]['addresses']['ipv6'] = int(m.groupdict()['addresses_ipv6'])

                mpls_dict['peer'][peer]['labels'] = {}
                mpls_dict['peer'][peer]['labels']['ipv4'] = int(m.groupdict()['labels_ipv4'])
                mpls_dict['peer'][peer]['labels']['ipv6'] = int(m.groupdict()['labels_ipv6'])
                continue
        
        return mpls_dict
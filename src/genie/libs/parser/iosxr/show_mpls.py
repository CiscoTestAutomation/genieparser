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
                Optional('nsr'): str,
                'up_time': str,
                Optional('discovery'): {
                    Optional('discovery'): int,
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
                },
                Optional('addresses'): {
                    Optional('address'): int,
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
                },
                Optional('labels'): {
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
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

        # Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
        #                                         ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
        # -----------------  --  ---  ----------  ----------  ----------  ------------
        # 10.205.2.254:0     Y   Y    31w0d       2     0     10    0     77     0
        p1 = re.compile(r'^(?P<peer>[\d\.:]+)\s+(?P<gr>[\w]+)\s+'
                         '(?P<nsr>[\w]+)\s+(?P<up_time>[\w\d\:]+)\s+'
                         '(?P<discovery_ipv4>[\d]+)\s+(?P<discovery_ipv6>[\d]+)\s+'
                         '(?P<addresses_ipv4>[\d]+)\s+(?P<addresses_ipv6>[\d]+)\s+'
                         '(?P<labels_ipv4>[\d]+)\s+(?P<labels_ipv6>[\d]+)$')

        # Peer              GR Up Time         Discovery Address
        # ----------------- -- --------------- --------- -------
        # 3.3.3.3:0         Y  00:01:04                3       8
        # 2.2.2.2:0         N  00:01:02                2       5
        p2 = re.compile(r'^(?P<peer>[\d\.:]+) +(?P<gr>[\w]+) +(?P<up_time>[\d\:]+) +'
                         '(?P<discovery>(\d+)) +(?P<address>(\d+))$')

        # Peer               GR  NSR  Up Time     Discovery  Address  IPv4 Label
        # -----------------  --  ---  ----------  ---------  -------  ----------
        # 2.2.2.2:0          N   Y    01:39:50            1        4          19
        # 3.3.3.3:0          N   N    01:38:04            1        3           5
        p3 = re.compile(r'^(?P<peer>[\d\.:]+) +(?P<gr>(\w+)) +(?P<nsr>(\w+)) +(?P<up_time>[\d\:]+) +'
                         '(?P<discovery>(\d+)) +(?P<address>(\d+)) +(?P<labels_ipv4>(\d+))$')

        for line in out.splitlines():
            line = line.strip()

            # Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
            #                                         ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
            # -----------------  --  ---  ----------  ----------  ----------  ------------
            # 10.205.2.254:0     Y   Y    31w0d       2     0     10    0     77     0
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

            # Peer              GR Up Time         Discovery Address
            # ----------------- -- --------------- --------- -------
            # 3.3.3.3:0         Y  00:01:04                3       8
            # 2.2.2.2:0         N  00:01:02                2       5
            m = p2.match(line)
            if m:
                peer = m.groupdict()['peer']
                gr = m.groupdict()['gr']
                up_time = m.groupdict()['up_time']
                discovery = int(m.groupdict()['discovery'])
                address = int(m.groupdict()['address'])

                peer_dict = mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                peer_dict['gr'] = gr
                peer_dict['up_time'] = up_time

                discovery_dict = peer_dict.setdefault('discovery', {})
                discovery_dict['discovery'] = discovery

                address_dict = peer_dict.setdefault('addresses', {})
                address_dict['address'] = address

                continue

            # Peer               GR  NSR  Up Time     Discovery  Address  IPv4 Label
            # -----------------  --  ---  ----------  ---------  -------  ----------
            # 2.2.2.2:0          N   Y    01:39:50            1        4          19
            # 3.3.3.3:0          N   N    01:38:04            1        3           5
            m = p3.match(line)
            if m:
                peer = m.groupdict()['peer']
                gr = m.groupdict()['gr']
                nsr = m.groupdict()['nsr']
                up_time = m.groupdict()['up_time']
                discovery = int(m.groupdict()['discovery'])
                address = int(m.groupdict()['address'])
                labels_ipv4 = int(m.groupdict()['labels_ipv4'])

                peer_dict = mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                peer_dict['gr'] = gr
                peer_dict['up_time'] = up_time
                peer_dict['nsr'] = nsr

                discovery_dict = peer_dict.setdefault('discovery', {})
                discovery_dict['discovery'] = discovery

                address_dict = peer_dict.setdefault('addresses', {})
                address_dict['address'] = address

                label_dict = peer_dict.setdefault('labels', {})
                label_dict['ipv4'] = labels_ipv4

                continue

        return mpls_dict

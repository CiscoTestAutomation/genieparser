''' show_mpls.py

IOSXR parsers for the following show commands:
    * 'show mpls ldp neighbor brief'
    * 'show mpls label table detail'
    * 'show mpls interfaces'
    * 'show mpls interfaces {interface}'
    * 'show mpls forwarding'
    * 'show mpls forwarding vrf {vrf}'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use
# import parser utils
from genie.libs.parser.utils.common import Common

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
        # 10.36.3.3:0         Y  00:01:04                3       8
        # 10.16.2.2:0         N  00:01:02                2       5
        p2 = re.compile(r'^(?P<peer>[\d\.:]+) +(?P<gr>[\w]+) +(?P<up_time>[\d\:]+) +'
                         '(?P<discovery>(\d+)) +(?P<address>(\d+))$')

        # Peer               GR  NSR  Up Time     Discovery  Address  IPv4 Label
        # -----------------  --  ---  ----------  ---------  -------  ----------
        # 10.16.2.2:0          N   Y    01:39:50            1        4          19
        # 10.36.3.3:0          N   N    01:38:04            1        3           5
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
            # 10.36.3.3:0         Y  00:01:04                3       8
            # 10.16.2.2:0         N  00:01:02                2       5
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
            # 10.16.2.2:0          N   Y    01:39:50            1        4          19
            # 10.36.3.3:0          N   N    01:38:04            1        3           5
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


# ======================================================
# Parser for 'show mpls label table detail'
# ======================================================
class ShowMplsLabelTableDetailSchema(MetaParser):
    
    """Schema for show mpls label table detail"""

    schema = {
        'table': {
            Any(): {
                'label': {
                    Any(): {
                        'owner': str,
                        'state': str,
                        'rewrite': str,
                        Optional('label_type'): {
                            Any(): {
                                Optional('vers'): int,
                                Optional('start_label'): int,
                                Optional('size'): int,
                                Optional('app_notify'): int,
                                Optional('index'): int,
                                Optional('type'): int,
                                Optional('interface'): str,
                                Optional('nh'): str,
                            },
                        }
                    },
                }
            },
        }
    }


class ShowMplsLabelTableDetail(ShowMplsLabelTableDetailSchema):

    """Parser for show mpls label table detail"""

    cli_command = ['show mpls label table detail']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        # Init vars
        mpls_dict = {}
        table = ''

        # Table Label   Owner                           State  Rewrite
        # ----- ------- ------------------------------- ------ -------
        # 0     0       LSD(A)                          InUse  Yes
        # 0     16000   ISIS(A):SR                      InUse  No
        p1 = re.compile(r'^(?P<table>\d+)\s+(?P<label>\d+)\s+(?P<owner>[\S]+)\s+(?P<state>\S+)'
            '\s+(?P<rewrite>\S+)$')

        # (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
        # (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
        p2 = re.compile(r'^\((?P<label_type>[\S\s]+),\s+vers:(?P<vers>\d+),'
            '\s+\(start_label=(?P<start_label>\d+),\s+size=(?P<size>\d+)'
            '(,\s+app_notify=(?P<app_notify>\d+))?\)$')

        # (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        p3 = re.compile(r'^\((?P<sr_label_type>[\S\s]+),\s+vers:(?P<vers>\d+),'
            '\s+index=(?P<index>\d+),\s+type=(?P<type>\d+),\s+intf=(?P<interface>\S+),'
            '\s+nh=(?P<nh>\S+)\)$')

        for line in out.splitlines():
            line = line.strip()

            # Table Label   Owner                           State  Rewrite
            # ----- ------- ------------------------------- ------ -------
            # 0     0       LSD(A)                          InUse  Yes
            # 0     16000   ISIS(A):SR                      InUse  No
            m = p1.match(line)
            if m:
                table = int(m.groupdict()['table'])
                label = int(m.groupdict()['label'])
                final_dict = mpls_dict.setdefault('table', {}).setdefault(table, {}).\
                    setdefault('label', {}).setdefault(label, {})
                label_list = ['owner', 'state', 'rewrite']
                for key in label_list:
                    final_dict.update({key:m.groupdict()[key]})
                continue

            # (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
            # (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
            m = p2.match(line)
            if m:
                label_type = m.groupdict()['label_type']
                latest_dict = final_dict.setdefault('label_type', {}).setdefault(label_type, {})
                label_list = ['vers', 'start_label', 'size']
                for key in label_list:
                    latest_dict.update({key:int(m.groupdict()[key])})
                if m.groupdict()['app_notify']:
                    latest_dict.update({'app_notify':int(m.groupdict()['app_notify'])})
                continue

            # (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
            m = p3.match(line)
            if m:
                label_type = m.groupdict()['sr_label_type']
                latest_dict = final_dict.setdefault('label_type', {}).setdefault(label_type, {})
                label_list = ['vers', 'index', 'type']
                for key in label_list:
                    latest_dict.update({key:int(m.groupdict()[key])})
                latest_dict.update({'interface':m.groupdict()['interface']})
                latest_dict.update({'nh':m.groupdict()['nh']})
                continue

        return mpls_dict


# ======================================================
# Schema for 'show mpls interfaces'
# ======================================================
class ShowMplsInterfacesSchema(MetaParser):
    schema = {
        'interfaces': {
            Any(): {
                'ldp': str,
                'tunnel': str,
                'static': str,
                'enabled': str,
            }
        },
    }


# ======================================================
# Parser for 'show mpls interfaces'
# ======================================================
class ShowMplsInterfaces(ShowMplsInterfacesSchema):
    cli_command = ['show mpls interfaces',
        'show mpls interfaces {interface}']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(
                                          interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # GigabitEthernet0/0/0/0     No       No       No       Yes
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<ldp>No|Yes) +'
                r'(?P<tunnel>No|Yes) +(?P<static>No|Yes) +'
                r'(?P<enabled>No|Yes)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0     No       No       No       Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.get('interface'))
                ldp = group.get('ldp')
                tunnel = group.get('tunnel')
                static = group.get('static')
                enabled = group.get('enabled')
                interface_dict = ret_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'ldp' : ldp})
                interface_dict.update({'tunnel': tunnel})
                interface_dict.update({'static': static})
                interface_dict.update({'enabled': enabled})
                continue

        return ret_dict


# ======================================================
# Schema for
#   * 'show mpls forwarding vrf {vrf}'
# ======================================================
class ShowMplsForwardingVrfSchema(MetaParser):
    schema = {
        'vrf': {
            Any(): {
                'local_label': {
                    Any(): {
                        'outgoing_label': {
                            Any(): {
                                'prefix_or_id': {
                                    Any(): {
                                        'outgoing_interface': {
                                            Any(): {
                                                Optional('next_hop'): str,
                                                'bytes_switched': int,
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================================
# Parser for
#   * 'show mpls forwarding vrf {vrf}'
# ======================================================
class ShowMplsForwardingVrf(ShowMplsForwardingVrfSchema):

    cli_command = ['show mpls forwarding vrf {vrf}']

    def cli(self, vrf, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0].format(vrf=vrf))
        else:
            out = output

        ret_dict = {}

        # 16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0
        p1 = re.compile(r'^((?P<local_label>\d+) +)?(?P<outgoing_label>\S+) '
                        r'+(?P<prefix_or_id>.+?) +(?P<outgoing_interface>\S+) '
                        r'+(?P<next_hop>\S+) +(?P<bytes_switched>\d+)$')

        # 24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
        p2 = re.compile(r'^(?P<local_label>\d+) +(?P<outgoing_label>\S+) '
                        r'+(?P<prefix_or_id>.+?) +\\$')

        # VRF1                         832
        p3 = re.compile(r'^(?P<outgoing_interface>\S+) +((?P<next_hop>\S+) +)?'
                        r'(?P<bytes_switched>\d+)$')

        # Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
        p4 = re.compile(r'^(?P<outgoing_interface>\S+) +(?P<next_hop>\S+) +\\$')

        # 3747484
        p5 = re.compile(r'^(?P<bytes_switched>\d+)$')

        pre_label = ''
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # 16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0
            #        Unlabelled  10.13.90.0/24      Gi0/0/0/1.90 10.23.90.3      0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                local_label = group.get('local_label') or pre_label
                outgoing_label = group.get('outgoing_label')
                prefix_or_id = group.get('prefix_or_id').strip()
                outgoing_interface = Common.convert_intf_name(group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})

                pre_label = local_label or pre_label
                continue

            # 24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
            m = p2.match(line)
            if m:
                group = m.groupdict()
                local_label = group.get('local_label') or pre_label
                outgoing_label = group.get('outgoing_label')
                prefix_or_id = group.get('prefix_or_id').strip()
                pre_label = local_label or pre_label
                continue

            # VRF1                         832
            m = p3.match(line)
            if m:
                group = m.groupdict()
                outgoing_interface = Common.convert_intf_name(
                    group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})
                continue

            # Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
            m = p4.match(line)
            if m:
                group = m.groupdict()
                outgoing_interface = Common.convert_intf_name(group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                continue

            # 3747484
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})
                continue

        return ret_dict


# ======================================================
# Schema for
#   * 'show mpls forwarding'
# ======================================================
class ShowMplsForwardingSchema(MetaParser):
    schema = {
        'local_label': {
            Any(): {
                'outgoing_label': {
                    Any(): {
                        'prefix_or_id': {
                            Any(): {
                                'outgoing_interface': {
                                    Any(): {
                                        Optional('next_hop'): str,
                                        'bytes_switched': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================================
# Parser for 
#   * 'show mpls forwarding'
# ======================================================
class ShowMplsForwarding(ShowMplsForwardingSchema, ShowMplsForwardingVrf):

    cli_command = ['show mpls forwarding']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        vrf = 'default'
        ret_dict = super().cli(vrf=vrf, output=out).get(
                    'vrf', {}).get('default', {})

        return ret_dict

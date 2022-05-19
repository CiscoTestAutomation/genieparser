"""show_vlan.py

"""
import re
import logging

from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Any, Optional


logger = logging.getLogger(__name__)


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match

# ====================================================
#  schema for show vlan
# ====================================================
class ShowVlanSchema(MetaParser):
    """Schema for show vlan"""
    schema = {
        'vlans':{
            Any():{
                Optional('vlan_id'): str,
                Optional('name'): str,
                Optional('state'): str,
                Optional('shutdown'): bool,
                Optional('interfaces'): list,
                Optional('type'): str,
                Optional('said'): int,
                Optional('mtu'): int,
                Optional('parent'): str,
                Optional('ring_no'): str,
                Optional('bridge_no'): str,
                Optional('stp'): str,
                Optional('bridge_mode'): str,
                Optional('trans1'): int,
                Optional('trans2'): int,
                Optional('remote_span_vlan'): bool,
                Optional('private_vlan'):
                    {
                        Optional('primary'): bool,
                        Optional('association'): list,
                        Optional('type'): str,
                        Optional('ports'): list,
                    },
                Optional('token_ring'):
                    {
                        Optional('are_hops'): int,
                        Optional('ste_hops'): int,
                        Optional('backup_crf'): str,
                    }
                },
            },
        }

# ====================================================
#  parser for show vlan
# ====================================================
class ShowVlan(ShowVlanSchema):
    """Parser for show vlan"""
    cli_command = 'show vlan'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # This pattern is for when the Name field is so long that it causes the
        # line to wrap around. For example:
        # 1832 blablablablablablablablablablablablablabla
        #                                       active
        p0 = re.compile(r'^\s*(active|suspended|\w+/lshut|\w+/unsup)+.*$')

        # VLAN Name                             Status    Ports
        # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
        # 2    VLAN_0002                        active
        # 20   VLAN-0020                        active
        # 100  V100                             suspended
        # 105  Misc. Name                       active    Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/19
        p1 = re.compile(r'^(?P<vlan_id>[0-9]+)\s+(?P<name>(?=\S).*(?<=\S))'
                         '\s+(?P<status>(active|suspended|(.*)lshut|(.*)unsup)+)'
                         '(?P<interfaces>[\s\S]+)?$')

        #                                                Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22
        p2 = re.compile(r'^\s*(?P<space>\s{48})(?P<interfaces>[\w\s\/\,]+)?$')

        # VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
        # ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
        # 1    enet  100001     1500  -      -      -        -    -        0      0
        p3 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<type>[a-zA-Z]+)'
                        ' +(?P<said>\d+) +(?P<mtu>[\d\-]+) +(?P<parent>[\w\-]+)?'
                        ' +(?P<ring_no>[\w\-]+)? +(?P<bridge_no>[\w\-]+)? +(?P<stp>[\w\-]+)?'
                        ' +(?P<bridge_mode>[\w\-]+)? +(?P<trans1>[\d\-]+) +(?P<trans2>[\d\-]+)$')

        # Remote SPAN VLANs
        # -------------------------------------
        # 201-202
        # 201,202
        # 201,202-205
        p4 = re.compile(r'^\s*(?P<remote_span_vlans>[^--][0-9\-\,]+)?$')

        # Primary Secondary Type              Ports
        # ------- --------- ----------------- ------------------------------------------
        # 2       301       community         Fa5/3, Fa5/25
        #  2       302       community
        #          10        community
        #  none    20        community
        # 20      105       isolated
        # 100     151       non-operational
        # none    202       community
        #         303       community
        # 101     402       non-operational
        p5 = re.compile(r'^\s*(?P<primary>[0-9a-zA-Z]+)? +(?P<secondary>\d+)'
                        ' +(?P<type>[\w\-]+)( +(?P<interfaces>[\s\S]+))?')

        # VLAN AREHops STEHops Backup CRF
        # ---- ------- ------- ----------
        # 1003 7       7       off
        p6 = re.compile(r'^\s*(?P<vlan_id>\d+)\s+'
                         '(?P<are_hops>\d+)\s+'
                         '(?P<ste_hops>\d+)\s+'
                         '(?P<backup_crf>\S+)\s*$')

        vlan_dict = {}
        primary = prev_line = ""
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            # active
            # suspended
            m = p0.match(line)
            if m:
                line = prev_line + ' ' + line

            # VLAN Name                             Status    Ports
            # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            # 2    VLAN_0002                        active
            # 20   VLAN-0020                        active
            # 100  V100                             suspended
            # 101  VLAN-0101                        active
            # 102  VLAN_0102                        active
            # 103  VLAN-0103                        act/unsup
            # 104  VLAN_0104                        act/lshut
            m = p1.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict:
                    vlan_dict['vlans'][vlan_id] = {}

                vlan_dict['vlans'][vlan_id]['vlan_id'] = vlan_id
                vlan_dict['vlans'][vlan_id]['name'] = m.groupdict()['name']
                vlan_dict['vlans'][vlan_id]['shutdown'] = False
                if 'act/unsup' in m.groupdict()['status']:
                    status = 'unsupport'
                elif 'suspend' in m.groupdict()['status']:
                    status = 'suspend'

                elif 'shut' in m.groupdict()['status']:
                    status = 'shutdown'
                    vlan_dict['vlans'][vlan_id]['shutdown'] = True
                else:
                    status = m.groupdict()['status']
                vlan_dict['vlans'][vlan_id]['state'] = status
                if m.groupdict()['interfaces']:
                    vlan_dict['vlans'][vlan_id]['interfaces'] = \
                        [Common.convert_intf_name(i) for i in m.groupdict()['interfaces'].split(',')]

                continue

            #                                                Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22
            m = p2.match(line)
            if m:
                vlan_dict['vlans'][vlan_id]['interfaces'] = vlan_dict['vlans'][vlan_id]['interfaces']+\
                    [Common.convert_intf_name(i) for i in m.groupdict()['interfaces'].split(',')]
                continue

            # VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
            # ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
            # 1    enet  100001     1500  -      -      -        -    -        0      0
            m = p3.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                type_ = m.groupdict()['type']
                said = m.groupdict()['said']
                mtu = m.groupdict()['mtu']
                parent = m.groupdict()['parent']
                ring_no = m.groupdict()['ring_no']
                bridge_no = m.groupdict()['bridge_no']
                stp = m.groupdict()['stp']
                bridge_mode = m.groupdict()['bridge_mode']
                trans1 = m.groupdict()['trans1']
                trans2 = m.groupdict()['trans2']

                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict['vlans']:
                    vlan_dict['vlans'][vlan_id] = {}

                vlan_dict['vlans'][vlan_id]['type'] = type_
                vlan_dict['vlans'][vlan_id]['said'] = int(said)
                vlan_dict['vlans'][vlan_id]['mtu'] = int(mtu)
                if '-' not in parent.strip():
                    vlan_dict['vlans'][vlan_id]['parent'] = parent
                if '-' not in ring_no.strip():
                    vlan_dict['vlans'][vlan_id]['ring_no'] = ring_no
                if '-' not in bridge_no.strip():
                    vlan_dict['vlans'][vlan_id]['bridge_no'] = bridge_no
                if '-' not in stp.strip():
                    vlan_dict['vlans'][vlan_id]['stp'] = stp
                if '-' not in bridge_mode.strip():
                    vlan_dict['vlans'][vlan_id]['bridge_mode'] = bridge_mode
                vlan_dict['vlans'][vlan_id]['trans1'] = int(trans1)
                vlan_dict['vlans'][vlan_id]['trans2'] = int(trans2)

                continue

            # VLAN AREHops STEHops Backup CRF
            # ---- ------- ------- ----------
            # 1003 7       7       off
            m = p6.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                are_hops = m.groupdict()['are_hops']
                ste_hops = m.groupdict()['ste_hops']
                backup_crf = m.groupdict()['backup_crf']

                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict['vlans']:
                    vlan_dict['vlans'][vlan_id] = {}

                if 'token_ring' not in vlan_dict['vlans'][vlan_id]:
                    vlan_dict['vlans'][vlan_id]['token_ring'] = {}

                vlan_dict['vlans'][vlan_id]['token_ring']['are_hops'] = int(are_hops)
                vlan_dict['vlans'][vlan_id]['token_ring']['ste_hops'] = int(ste_hops)
                vlan_dict['vlans'][vlan_id]['token_ring']['backup_crf'] = backup_crf

                continue

            # Remote SPAN VLANs
            # -------------------------------------
            # 201-202
            # 201,202
            # 201,202-205
            m = p4.match(line)
            if m:
                if m.groupdict()['remote_span_vlans']:
                    remote_span_vlans = m.groupdict()['remote_span_vlans'].split(',')

                    if 'vlans' not in vlan_dict:
                        vlan_dict['vlans'] = {}
                    for remote_vlan in remote_span_vlans:
                        if '-' in remote_vlan:
                            remote_span_list = remote_vlan.split('-')
                            initial = remote_span_list[0]
                            end = remote_span_list[1]
                            value = int(initial)
                            while (value <= int(end)):
                                if str(value) not in vlan_dict['vlans']:
                                    vlan_dict['vlans'][str(value)] = {}
                                vlan_dict['vlans'][str(value)]['remote_span_vlan'] = True
                                value += 1

                        else:
                            if remote_vlan not in vlan_dict['vlans']:
                                vlan_dict['vlans'][remote_vlan] = {}
                            vlan_dict['vlans'][remote_vlan]['remote_span_vlan'] = True

                continue

            # Primary Secondary Type              Ports
            # ------- --------- ----------------- ------------------------------------------
            # 2       301       community         Fa5/3, Fa5/25
            #  2       302       community
            #          10        community
            #  none    20        community
            # 20      105       isolated
            # 100     151       non-operational
            # none    202       community
            #         303       community
            # 101     402       non-operational
            m = p5.match(line)
            if m:
                if m.groupdict()['primary'] and m.groupdict()['primary'].lower() != "none":
                    primary = m.groupdict()['primary']
                else:
                    primary = ""
                secondary = m.groupdict()['secondary']

                private_vlan_type = m.groupdict()['type']
                if m.groupdict()['interfaces']:
                    private_vlan_interfaces = \
                        [Common.convert_intf_name(i) for i in m.groupdict()['interfaces'].split(',')]

                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}
                if m.groupdict()['primary'] and m.groupdict()['primary'].lower() != "none":
                    if primary not in vlan_dict['vlans']:
                        vlan_dict['vlans'][primary] = {}
                    if 'private_vlan' not in vlan_dict['vlans'][primary]:
                        vlan_dict['vlans'][primary]['private_vlan'] = {}
                if primary:
                    vlan_dict['vlans'][primary]['private_vlan']['primary'] = True
                    if 'association' in vlan_dict['vlans'][primary]['private_vlan']:
                        vlan_dict['vlans'][primary]['private_vlan']['association'] = \
                            vlan_dict['vlans'][primary]['private_vlan']['association'] + [secondary]
                    else:
                        vlan_dict['vlans'][primary]['private_vlan']['association'] = secondary.split()

                if secondary not in vlan_dict['vlans']:
                    vlan_dict['vlans'][secondary] = {}

                if 'private_vlan' not in vlan_dict['vlans'][secondary]:
                    vlan_dict['vlans'][secondary]['private_vlan'] = {}
                vlan_dict['vlans'][secondary]['private_vlan']['primary'] = False
                vlan_dict['vlans'][secondary]['private_vlan']['type'] = private_vlan_type
                if m.groupdict()['interfaces']:
                    vlan_dict['vlans'][secondary]['private_vlan']['ports'] = private_vlan_interfaces

                continue

            """
            Save previous line in case lines like
            1832 blablablabla blablablablabla blablablabla bla
                                                 active
            need to be combined into
            1832 blablablabla blablablablabla blablablabla bla active
            """
            prev_line = line

        return vlan_dict

#================================================================
#old  parsers with old schema
#=================================================================

class ShowVlanMtuSchema(MetaParser):
    """Schema for show vlan mtu"""
    schema = {'vlan_id':
                {Any():
                     {'vlan_mtu': str,
                      'vlan_min_mtu': str,
                      'vlan_max_mtu': str,
                      'mtu_mismatch': str}
                },
            }


class ShowVlanMtu(ShowVlanMtuSchema):
    """Parser for show vlan mtu"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show vlan mtu'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        vlan_list = []
        vlan_mtu_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*VLAN\s +SVI_MTU\s +interface\s +MinMTU(port)\s +MaxMTU(port)\s +MTU_Mismatch$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<vlan_mtu>[0-9\-]+) +(?P<vlan_min_mtu>[0-9]+) +(?P<vlan_max_mtu>[0-9]+) +(?P<mtu_mismatch>[a-zA-Z]+)$')
            m = p2.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if 'vlan_id' not in vlan_mtu_dict:
                    vlan_mtu_dict['vlan_id'] = {}
                if vlan_id not in vlan_mtu_dict['vlan_id']:
                    vlan_mtu_dict['vlan_id'][vlan_id] = {}
                vlan_mtu_dict['vlan_id'][vlan_id]['vlan_mtu'] = \
                    m.groupdict()['vlan_mtu']
                vlan_mtu_dict['vlan_id'][vlan_id]['vlan_min_mtu'] = \
                    m.groupdict()['vlan_min_mtu']
                vlan_mtu_dict['vlan_id'][vlan_id]['vlan_max_mtu'] = \
                    m.groupdict()['vlan_max_mtu']
                vlan_mtu_dict['vlan_id'][vlan_id]['mtu_mismatch'] = \
                    m.groupdict()['mtu_mismatch']
                continue

        return vlan_mtu_dict


class ShowVlanAccessMapSchema(MetaParser):
    """Schema for show vlan access map"""
    schema = {'access_map_id':
                {Any():
                    {'access_map_sequence':
                        {Any():
                            {Optional('access_map_match_protocol'): str,
                             Optional('access_map_match_protocol_value'): str,
                             Optional('access_map_action_value'): str}
                        },
                    }
                },
            }

class ShowVlanAccessMap(ShowVlanAccessMapSchema):
    """Parser for show vlan access-map"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show vlan access-map'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        access_map_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Vlan\s+access-map\s+\"(?P<access_map_id>\S+)\"\s+(?P<access_map_sequence>[0-9]+)$')
            m = p1.match(line)
            if m:
                access_map_id = m.groupdict()['access_map_id']
                map_id = m.groupdict()['access_map_id']
                if 'access_map_id' not in access_map_dict:
                   access_map_dict['access_map_id'] = {}
                if map_id not in access_map_dict['access_map_id']:
                    access_map_dict['access_map_id'][map_id] = {}
                access_map_sequence = m.groupdict()['access_map_sequence']
                if 'access_map_sequence' not in access_map_dict['access_map_id'][map_id]:
                    access_map_dict['access_map_id'][map_id]['access_map_sequence'] = {}
                if access_map_sequence not in access_map_dict['access_map_id'][map_id]['access_map_sequence']:
                    access_map_dict['access_map_id'][map_id]['access_map_sequence'][access_map_sequence] = {}
                continue

            p2 = re.compile(r'^\s*(?P<access_map_match_protocol>\S+)\s+address:\s+(?P<access_map_match_protocol_value>\S+)$')
            m = p2.match(line)
            if m:
                access_map_dict['access_map_id'][map_id]\
                    ['access_map_sequence'][access_map_sequence]['access_map_match_protocol'] = \
                        m.groupdict()['access_map_match_protocol']
                access_map_dict['access_map_id'][map_id]\
                    ['access_map_sequence'][access_map_sequence]['access_map_match_protocol_value'] = \
                        m.groupdict()['access_map_match_protocol_value']
                continue

            p3 = re.compile(r'^\s*(?P<access_map_action_value>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:
                access_map_dict['access_map_id'][map_id]\
                    ['access_map_sequence'][access_map_sequence]['access_map_action_value'] = \
                        m.groupdict()['access_map_action_value']
                continue

        return access_map_dict


class ShowVlanRemoteSpanSchema(MetaParser):
    """Schema for show vlan remote-span"""
    schema = {'vlan_id':
                {Any():
                    {'vlan_is_remote_span':bool}
                },
            }

class ShowVlanRemoteSpan(ShowVlanRemoteSpanSchema):
    """Parser for show vlan remote-span"""
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show vlan remote-span'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        remote_span_vlan_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Remote +SPAN +VLANs$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*(?P<remote_span_vlan_ids>[0-9\,]+)$')
            m = p2.match(line)
            if m:
                if 'vlan_id' not in remote_span_vlan_dict:
                    remote_span_vlan_dict['vlan_id'] = {}
                remote_span_vlans = m.groupdict()['remote_span_vlan_ids']
                for vlid in remote_span_vlans.split(","):
                    if vlid not in remote_span_vlan_dict['vlan_id']:
                        remote_span_vlan_dict['vlan_id'][vlid] = {}
                    remote_span_vlan_dict['vlan_id'][vlid]['vlan_is_remote_span'] = True
                continue

        return remote_span_vlan_dict


class ShowVlanFilterSchema(MetaParser):
    """Schema for show vlan filter"""
    schema = {'vlan_id':
                {Any():
                    {'access_map_tag':str}
                },
            }

class ShowVlanFilter(ShowVlanFilterSchema):
    """Parser for show vlan filter"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show vlan filter'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*VLAN\s+Map\s+(?P<vlan_access_map_tag>\S+)\s+is\s+filtering\s+VLANs:$')
            m = p1.match(line)
            if m:
                if 'vlan_id' not in vlan_dict:
                    vlan_dict['vlan_id'] = {}
                tag = m.groupdict()['vlan_access_map_tag']
                continue

            p2 = re.compile(r'^\s*(?P<access_map_vlan_ids>[0-9\,\-]+)$')
            m = p2.match(line)
            if m:
                access_map_vlan_ids = m.groupdict()['access_map_vlan_ids']
                vlans = re.split(r'[,-]', access_map_vlan_ids)
                for vlid in vlans:
                    if vlid not in vlan_dict['vlan_id']:
                        vlan_dict['vlan_id'][vlid] = {}
                    vlan_dict['vlan_id'][vlid]['access_map_tag'] = tag
                continue

        return vlan_dict


class ShowVlanIdSchema(MetaParser):
    """Schema for show vlan id"""
    schema = {'brdg-mode': str,
              'bridge-no': str,
              'mtu': str,
              'parent': str,
              Optional('ports'): list,
              'ring-no': str,
              'said': str,
              'status': str,
              'stp': str,
              'trans1': str,
              'trans2': str,
              'type': str,
              'vlan-id': int,
              'vlan-name': str
            }


class ShowVlanId(ShowVlanIdSchema):
    """Parser for show vlan id {vlan_id}"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show vlan id {vlan_id}'
    def cli(self, vlan_id=None, output=None):
        cmd = self.cli_command.format(vlan_id=vlan_id)
        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary

        vlan_dict = {}
        p1 = re.compile(r'(?P<vlan_id>\d+) +(?P<vlan_name>\S+|\S+.*\S+) +'
                        r'(?P<status>active|suspended|act/lshut|sus/lshut)'
                        r'(?:\s+(?P<ports>([A-Za-z\-]+[\/\d\-\:\.]+\d+)(.*)))?')
        p2 = re.compile(r'(?P<ports>([A-Za-z\-]+[\/\d\-\:\.]+\d+)(.*))')
        p3 = re.compile(r'\d+ +'
                    '(?P<type>\w+) +'
                    '(?P<said>\d+) +'
                    '(?P<mtu>\d+) +'
                    '(?P<parent>\S+) +'
                    '(?P<ring_no>\S+) +'
                    '(?P<bridge_no>\S+) +'
                    '(?P<stp>\S+) +'
                    '(?P<brdg_mode>\S+) +'
                    '(?P<trans1>\d+) +'
                    '(?P<trans2>\d+)')

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                port_list = []
                vlan_dict['vlan-id'] = int(group['vlan_id'])
                vlan_dict['vlan-name'] = group['vlan_name']
                vlan_dict['status'] = group['status']
                if group['ports']:
                    port_list.extend(group['ports'].replace(' ','').split(','))
                    vlan_dict['ports'] = port_list
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                vlan_dict['ports'].extend(group['ports'].replace(' ','').split(','))
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                vlan_dict['type'] = group['type']
                vlan_dict['said'] = group['said']
                vlan_dict['mtu'] = group['mtu']
                vlan_dict['parent'] = group['parent']
                vlan_dict['ring-no'] = group['ring_no']
                vlan_dict['bridge-no'] = group['bridge_no']
                vlan_dict['stp'] = group['stp']
                vlan_dict['brdg-mode'] = group['brdg_mode']
                vlan_dict['trans1'] = group['trans1']
                vlan_dict['trans2'] = group['trans2']
        return vlan_dict


class ShowVlanVirtualportSchema(MetaParser):
    """Schema for show vlan virtual-port"""
    schema = {
        Optional('slots'): {
             Any(): {
                 'virtual-ports': int
             }
        },
        Optional('total'): int
    }


class ShowVlanVirtualport(ShowVlanVirtualportSchema):
    """ Parser for show vlan virtual-port"""
    cli_command = "show vlan virtual-port"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Slot 1
        p1 = re.compile(r'^Slot +(?P<slot>\d+)$')

        # Total slot virtual ports 4796
        p2 = re.compile(r'^Total +slot +virtual +ports +(?P<ports>\d+)$')

        # Total chassis virtual ports 14254
        p3 = re.compile(r'^Total +chassis +virtual +ports +(?P<ports>\d+)$')

        ret_dict = {}
        slot = None

        for line in output.splitlines():
            line = line.strip()
            # Slot 1
            m = p1.match(line)
            if m:
                ret_dict.setdefault('slots', {})
                slot = int(m.groupdict()['slot'])
                ret_dict['slots'].setdefault(slot, {})
                continue

            # Total slot virtual ports 4796
            m = p2.match(line)
            if m:
                ports = int(m.groupdict()['ports'])
                if slot:
                    ret_dict['slots'][slot]['virtual-ports'] = ports
                slot = None

            # Total chassis virtual ports 14254
            m = p3.match(line)
            if m:
                ports = int(m.groupdict()['ports'])
                ret_dict['total'] = ports

        return ret_dict


class ShowVlansDot1qVlanIdSecondDot1qVlanIdSchema(MetaParser):
     """Schema for show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}"""
     schema = {
                'stat_for_vlan': {
                    str: {
                       'in_pkts': int,         # These counters are incremented for both
                       'in_octets': int,       # first_vlan_id case and also first_vlan_id
                       'out_pkts': int,        # and second_vlan_id case.
                       'out_octets': int
                    }
                }
            }

class ShowVlansDot1qVlanIdSecondDot1qVlanId(ShowVlansDot1qVlanIdSecondDot1qVlanIdSchema):
     """Parser for
         * show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}
         * show vlans dot1q {first_vlan_id}
     """

     #*************************
     # schema - class variable
     #
     # Purpose is to make sure the parser always return the output
     # (nested dict) that has the same data structure across all supported
     # parsing mechanisms (cli(), yang(), xml()).
     cli_command = [
               'show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}',
               'show vlans dot1q {first_vlan_id}'
    ]
     def cli(self, first_vlan_id=None, second_vlan_id=None, output=None):

         if not output:
            cmd = []
            if second_vlan_id:
                cmd.append('show vlans dot1q {first_vlan_id} second-dot1q {second_vlan_id}'.format(first_vlan_id=first_vlan_id, second_vlan_id=second_vlan_id))
            else:
                cmd.append('show vlans dot1q {first_vlan_id}'.         format(first_vlan_id=first_vlan_id))
            cmd = ' '.join(cmd)
            out = self.device.execute(cmd)
         else:
            out = output

         #initial return dictionary
         ret_dict = {}
         vlan = None
         #Total statistics for Outer/Inner VLAN 2/3:        ---> Outer/Inner VLAN case
         p0 = re.compile(r'^Total statistics for (?P<vlan>[a-zA-Z]+\/[a-zA-Z]+\s+VLAN\s+[0-9]\/[0-9]):$')
         #Total statistics for 802.1Q VLAN 1:               ---> Outer VLAN case
         p0_1 = re.compile(r'^Total statistics for (?P<vlan>[0-9]+.[0-9][A-Z]\s+VLAN\s+[0-9]):$')
         #105331037 packets, 147884775948 bytes input
         p1 = re.compile(r'^(?P<in_pkts>\d+)\s+packets,\s+(?P<in_octets>\d+)\s+bytes\s+input$')
         #105334310 packets, 148310655960 bytes output
         p2 = re.compile(r'^(?P<out_pkts>\d+)\s+packets,\s+(?P<out_octets>\d+)\s+bytes\s+output$')

         #Total statistics for Outer/Inner VLAN 2/3:
         #   105331037 packets, 147884775948 bytes input
         #   105334310 packets, 148310655960 bytes output

         for line in out.splitlines():
             line = line.strip()
             #Total statistics for Outer/Inner VLAN 2/3:        ---> Outer/Inner VLAN case
             m0 = p0.match(line)
             #Total statistics for 802.1Q VLAN 2:               ---> Outer VLAN case
             m0_1 = p0_1.match(line)
             if m0:
                ret_dict.setdefault('stat_for_vlan', {})
                vlan = str(m0.groupdict()['vlan'])
                ret_dict['stat_for_vlan'].setdefault(vlan, {})
                continue
             if m0_1:
                ret_dict.setdefault('stat_for_vlan', {})
                vlan = str(m0_1.groupdict()['vlan'])
                ret_dict['stat_for_vlan'].setdefault(vlan, {})
                continue

             #105331037 packets, 147884775948 bytes input
             m1 = p1.match(line)
             if m1:
                 group = m1.groupdict()
                 ret_dict['stat_for_vlan'][vlan]['in_pkts'] = int(group['in_pkts'])
                 ret_dict['stat_for_vlan'][vlan]['in_octets'] = int(group['in_octets'])
                 continue
             #105334310 packets, 148310655960 bytes output
             m2 = p2.match(line)
             if m2:
                 group = m2.groupdict()
                 ret_dict['stat_for_vlan'][vlan]['out_pkts'] = int(group['out_pkts'])
                 ret_dict['stat_for_vlan'][vlan]['out_octets'] = int(group['out_octets'])
                 continue

         return ret_dict


class ShowVlanSummarySchema(MetaParser):
    schema = {
        'vlan_summary': {
            'existing_vlans': int,
            'existing_vtp_vlans': int,
            'existing_extend_vlans': int
        }
    }

class ShowVlanSummary(ShowVlanSummarySchema):
    cli_command = 'show vlan summary'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #Number of existing VLANs               : 1009
        p1 = re.compile(r'Number\sof\sexisting\sVLANs\s+\:\s+(?P<existing_vlans>\d+)')

        #Number of existing VTP VLANs          : 1005
        p2 = re.compile(r'Number\sof\sexisting\sVTP\sVLANs\s+\:\s+(?P<existing_vtp_vlans>\d+)')

        #Number of existing extended VLANS     : 4
        p3 = re.compile(r'Number\sof\sexisting\sextended\sVLANS\s+\:\s+(?P<existing_extend_vlans>\d+)')

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'vlan_summary' not in ret_dict:
                    vlan_summary = ret_dict.setdefault('vlan_summary', {})

                vlan_summary['existing_vlans'] = int(group['existing_vlans'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vlan_summary['existing_vtp_vlans'] = int(group['existing_vtp_vlans'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                vlan_summary['existing_extend_vlans'] = int(group['existing_extend_vlans'])
                continue

        return ret_dict


"""show_vlan.py

"""
import xmltodict
import re
import logging

from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

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
                },
            },
        }

# ====================================================
#  parser for show vlan
# ====================================================
class ShowVlan(ShowVlanSchema):
    """Parser for show vlan"""
    def cli(self):
        cmd = 'show vlan'
        out = self.device.execute(cmd)

        vlan_dict = {}
        primary = ""
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            # VLAN Name                             Status    Ports
            # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            p1 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<name>[a-zA-Z0-9\-]+)'
                            ' +(?P<status>(active|suspended|act/unsup|(.*)lshut)+) *(?P<interfaces>[\w\s\/\,]+)?$')
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
            p2 = re.compile(r'^\s*(?P<space>\s{48})(?P<interfaces>[\w\s\/\,]+)?$')
            m = p2.match(line)
            if m:
                vlan_dict['vlans'][vlan_id]['interfaces'] = vlan_dict['vlans'][vlan_id]['interfaces']+\
                    [Common.convert_intf_name(i) for i in m.groupdict()['interfaces'].split(',')]
                continue

            # VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
            # ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
            # 1    enet  100001     1500  -      -      -        -    -        0      0
            p3 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<type>[a-zA-Z]+)'
                            ' +(?P<said>\d+) +(?P<mtu>[\d\-]+) +(?P<parent>[\w\-]+)?'
                            ' +(?P<ring_no>[\w\-]+)? +(?P<bridge_no>[\w\-]+)? +(?P<stp>[\w\-]+)?'
                            ' +(?P<bridge_mode>[\w\-]+)? +(?P<trans1>[\d\-]+) +(?P<trans2>[\d\-]+)$')
            m = p3.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                type = m.groupdict()['type']
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

                vlan_dict['vlans'][vlan_id]['type'] = type
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

            # Remote SPAN VLANs
            # -------------------------------------
            # 201-202
            # 201,202
            # 201,202-205
            p4 = re.compile(r'^\s*(?P<remote_span_vlans>[^--][0-9\-\,]+)?$')
            m = p4.match(line)
            if m:
                if m.groupdict()['remote_span_vlans']:
                    remote_span_vlans = m.groupdict()['remote_span_vlans'].split(',')

                if remote_span_vlans:
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

            p5 = re.compile(r'^\s*(?P<primary>[0-9a-zA-Z]+)? +(?P<secondary>\d+)'
                            ' +(?P<type>[\w\-]+)( +(?P<interfaces>[\w\s\,\/]+))?$')
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

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show vlan mtu'.format()
        out = self.device.execute(cmd)
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

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show vlan access-map'.format()
        out = self.device.execute(cmd)
        access_map_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Vlan +access-map +\"(?P<access_map_id>[a-zA-Z0-9]+)\" +(?P<access_map_sequence>[0-9]+)$')
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

            p2 = re.compile(r'^\s*(?P<access_map_match_protocol>[a-zA-Z0-9]+) +address: +(?P<access_map_match_protocol_value>[a-zA-Z0-9\s]+)$')
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

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        cmd = 'show vlan remote-span'.format()
        out = self.device.execute(cmd)
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

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """

        cmd = 'show vlan filter'.format()
        out = self.device.execute(cmd)
        vlan_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*VLAN +Map +(?P<vlan_access_map_tag>[a-zA-Z0-9]+) +is +filtering +VLANs:$')
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
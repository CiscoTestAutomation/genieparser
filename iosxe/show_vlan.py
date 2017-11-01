''' show_vlan.py

Example parser class

'''
import xmltodict
import re
import logging

from metaparser import MetaParser
from parser.utils.common import Common
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional \

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
    schema = {
        'vlans':{
            Any():{
                Optional('vlan_id'): int,
                Optional('name'): str,
                Optional('state'): str,
                Optional('interfaces'): list,
                },
            },
        }

# ====================================================
#  parser for show vlan
# ====================================================
class ShowVlan(ShowVlanSchema):
    '''
       show vlan
    '''
    def cli(self):
        cmd = 'show vlan'
        out = self.device.execute(cmd)

        vlan_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            # VLAN Name                             Status    Ports
            # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            p1 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<name>[a-zA-Z0-9\-]+)'
                            ' +(?P<status>[a-zA-Z\/]+) *(?P<interfaces>[\w\s\/\,]+)?$')
            m = p1.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict:
                    vlan_dict['vlans'][vlan_id] = {}

                vlan_dict['vlans'][vlan_id]['vlan_id'] = int(vlan_id)
                vlan_dict['vlans'][vlan_id]['name'] = m.groupdict()['name']
                vlan_dict['vlans'][vlan_id]['state'] = m.groupdict()['status']
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

        return vlan_dict

#================================================================
#old  parsers with old schema
#=================================================================


class ShowVlanMtuSchema(MetaParser):
    schema = {'vlan_id':
                {Any():
                     {'vlan_mtu': str,
                      'vlan_min_mtu': str,
                      'vlan_max_mtu': str,
                      'mtu_mismatch': str}
                },
            }


class ShowVlanMtu(ShowVlanMtuSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
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
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
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
    schema = {'vlan_id':
                {Any():
                    {'vlan_is_remote_span':bool}
                },
            }

class ShowVlanRemoteSpan(ShowVlanRemoteSpanSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
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
    schema = {'vlan_id':
                {Any():
                    {'access_map_tag':str}
                },
            }

class ShowVlanFilter(ShowVlanFilterSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
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
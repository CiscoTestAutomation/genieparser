"""show_vlan.py

NXOS parsers for the following show commands:
    * show vlan
    * show vlan id 1-3967 vn-segment
    * show vlan internal info
    * show vlan filter
    * show vlan access-map
    * show vxlan
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
from genie.libs.parser.utils.common import Common

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
                Optional('mode'): str,
                Optional('type'): str,
                Optional('state'): str,
                Optional('shutdown'): bool,
                Optional('interfaces'): list,
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

    cli_command = 'show vlan'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # VLAN Name                             Status    Ports
            # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            # 105  VLAN0105                         act/lshut Po333
            # 1    default                          active
            p1 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<name>[a-zA-Z0-9\-]+)'
                            ' +(?P<status>[active|suspended|act/unsup|sus|(.*)/lshut]+)( *(?P<interfaces>[\w\s\/\,]+))?$')
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
            p2 = re.compile(r'^\s*(?P<space>\s{48})(?P<interfaces>[\w\s\/\,]+)$')
            m = p2.match(line)
            if m:
                vlan_dict['vlans'][vlan_id]['interfaces'] = vlan_dict['vlans'][vlan_id]['interfaces']+\
                [Common.convert_intf_name(i) for i in m.groupdict()['interfaces'].split(',')]
                continue

            # VLAN Type         Vlan-mode
            # 1    enet         CE
            p3 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<vlan_type>[\w]+)'
                            ' +(?P<vlan_mode>[\w]+)?$')
            m = p3.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if vlan_id in vlan_dict['vlans']:
                    vlan_dict['vlans'][vlan_id]['mode'] = m.groupdict()['vlan_mode'].lower()
                    vlan_dict['vlans'][vlan_id]['type'] = m.groupdict()['vlan_type']
                continue


            # Remote SPAN VLANs
            # -------------------------------------
            # 201-202
            # 201,202
            # 201,204,201-220
            p4 = re.compile(r'^\s*(?P<remote_span_vlans>[^--][0-9\-\,]+)?$')
            m = p4.match(line)
            if m:
                remote_span_vlans = ""
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

            p5 = re.compile(r'^\s*(?P<primary>\d+)? +(?P<secondary>\d+)'
                            ' +(?P<type>[\w\-]+)( +(?P<interfaces>[\w\s\,\/]+))?$')
            m = p5.match(line)

            if m:
                if m.groupdict()['primary']:
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
                if m.groupdict()['primary']:
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

# ====================================================
#  schema for show vlan id 1-3967 vn_segment
# ====================================================
class ShowVlanIdVnSegmentSchema(MetaParser):
    """Schema for show vlan id 1-3967 vn_segment"""
    schema = {
        'vlans': {
            Any(): {
                Optional('vlan_id'): str,
                Optional('vn_segment_id'): int,
            },
        },
    }

# ====================================================
#  parser for show vlan id 1-3967 vn-segment
# ====================================================
class ShowVlanIdVnSegment(ShowVlanIdVnSegmentSchema):
    """Parser for show vlan id 1-3967 vn_segment"""

    cli_command = 'show vlan id 1-3967 vn-segment'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # VLAN Segment-id
            # ---- -----------
            # 10   5010
            p1 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<segment_id>[0-9]+)$')
            m = p1.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict:
                    vlan_dict['vlans'][vlan_id] = {}

                vlan_dict['vlans'][vlan_id]['vlan_id'] = vlan_id
                vlan_dict['vlans'][vlan_id]['vn_segment_id'] = int(m.groupdict()['segment_id'])
                continue

        return vlan_dict


############################################################
#  Old Parsers are below
#  may be in feature we need to delete or improve them
#############################################################
def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match

class ShowVlanOldSchema(MetaParser):
    schema = {'vlan_id':
                {Any():
                    {'name': str,
                     'status': str,
                     Optional('ports'): Or(str, None),
                     Optional('type'): str,
                     Optional('said'): str,
                     Optional('mtu'): str,
                     Optional('parent'): str,
                     Optional('RingNo'): str,
                     Optional('BridgeNo'): str,
                     Optional('stp'): str,
                     Optional('BrdgMode'): str,
                     Optional('Trans1'): str,
                     Optional('Trans2'): str,
                     'vlan_type': str,
                     'vl_mode': str,
                     Optional('remote_span_vlan'): bool,
                     Optional('private_secondary_vlan'): str,
                     Optional('private_vlan_type'): str}
                },
            }

class ShowVlanOld(ShowVlanOldSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show vlan'
    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        vlan_dict = {}
        main_section = False
        mtu_section = False
        vlan_mode_section = False
        remote_span_section = False
        private_vlan_section = False
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*VLAN +Name +Status +Ports$')
            m = p1.match(line)
            if m:
                main_section = True
                continue

            p2 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<name>[a-zA-Z0-9\-]+) +(?P<status>[a-zA-Z\/]+) *(?P<ports>[a-zA-Z0-9\s\/\,]+)?$')
            m = p2.match(line)
            if m:
                if main_section:
                    vlan_id = m.groupdict()['vlan_id']
                    if 'vlan_id' not in vlan_dict:
                        vlan_dict['vlan_id'] = {}
                    if vlan_id not in vlan_dict['vlan_id']:
                        vlan_dict['vlan_id'][vlan_id] = {}
                    vlan_dict['vlan_id'][vlan_id]['name'] = m.groupdict()['name']
                    vlan_dict['vlan_id'][vlan_id]['status'] = m.groupdict()['status']
                    vlan_dict['vlan_id'][vlan_id]['ports'] = m.groupdict()['ports']
                    continue

            p8 = re.compile(r'^\s*(?P<ports>[a-zA-Z0-9\s\/\,]+)$')
            m = p8.match(line)
            if m:
                if main_section:
                    vlan_ports = vlan_dict['vlan_id'][vlan_id]['ports']
                    if vlan_ports:
                        added_ports = m.groupdict()['ports']
                        vlan_dict['vlan_id'][vlan_id]['ports'] = \
                            vlan_dict['vlan_id'][vlan_id]['ports'] + ', ' + added_ports

            p3 = re.compile(r'^\s*VLAN +Type +SAID +MTU +Parent +RingNo +BridgeNo +Stp +BrdgMode +Trans1 +Trans2$')
            m = p3.match(line)
            if m:
                mtu_section = True
                main_section = False
                continue

            p4 = re.compile(r'^\s*(?P<vid>[0-9]+) +(?P<type>[a-zA-Z]+) +(?P<said>[0-9]+) +(?P<mtu>[0-9]+) +(?P<parent>[a-zA-Z0-9\-]+) +(?P<RingNo>[a-zA-Z0-9\-]+) +(?P<BridgeNo>[a-zA-Z0-9\-]+) +(?P<stp>[a-zA-Z\-]+) +(?P<BrdgMode>[a-zA-Z0-9\-]+) +(?P<Trans1>[a-zA-Z0-9\-]+) +(?P<Trans2>[a-zA-Z0-9\-]+)$')
            m = p4.match(line)
            if m:
                if mtu_section:
                    vid = m.groupdict()['vid']
                    if vid not in vlan_dict['vlan_id']:
                        vlan_dict['vlan_id'][vid] = {}
                    vlan_dict['vlan_id'][vid]['type'] = m.groupdict()['type']
                    vlan_dict['vlan_id'][vid]['said'] = m.groupdict()['said']
                    vlan_dict['vlan_id'][vid]['mtu'] = m.groupdict()['mtu']
                    vlan_dict['vlan_id'][vid]['parent'] = m.groupdict()['parent']
                    vlan_dict['vlan_id'][vid]['RingNo'] = m.groupdict()['RingNo']
                    vlan_dict['vlan_id'][vid]['BridgeNo'] = m.groupdict()['BridgeNo']
                    vlan_dict['vlan_id'][vid]['stp'] = m.groupdict()['stp']
                    vlan_dict['vlan_id'][vid]['BrdgMode'] = m.groupdict()['BrdgMode']
                    vlan_dict['vlan_id'][vid]['Trans1'] = m.groupdict()['Trans1']
                    vlan_dict['vlan_id'][vid]['Trans2'] = m.groupdict()['Trans2']
                    continue

            p5 = re.compile(r'^\s*VLAN +Type +Vlan-mode$')
            m = p5.match(line)
            if m:
                vlan_mode_section = True
                main_section = False
                continue

            p6 = re.compile(r'^\s*(?P<vl_id>[0-9]+) +(?P<vlan_type>[a-z]+) +(?P<vl_mode>[A-Z]+)$')
            m = p6.match(line)
            if m:
                if vlan_mode_section:
                    vl_id = m.groupdict()['vl_id']
                    if vl_id not in vlan_dict['vlan_id']:
                        vlan_dict['vlan_id'][vl_id] = {}
                    vlan_dict['vlan_id'][vl_id]['vlan_type'] = m.groupdict()['vlan_type']
                    vlan_dict['vlan_id'][vl_id]['vl_mode'] = m.groupdict()['vl_mode']

            p7 = re.compile(r'^\s*Remote +SPAN +VLANs$')
            m = p7.match(line)
            if m:
                remote_span_section = True
                mtu_section = False
                continue

            p8 = re.compile(r'^\s*(?P<remote_span_vlans>[0-9\,]+)$')
            m = p8.match(line)
            if m:
                if remote_span_section:
                    remote_span_vlans = m.groupdict()['remote_span_vlans']
                    for vlid in remote_span_vlans.split(","): 
                        if vlid not in vlan_dict['vlan_id']:
                            vlan_dict['vlan_id'][vlid] = {}
                        vlan_dict['vlan_id'][vlid]['remote_span_vlan'] = True
                    continue

            p9 = re.compile(r'^\s*Primary +Secondary +Type +Ports$')
            m = p9.match(line)
            if m:
                private_vlan_section = True
                remote_span_section = False
                continue

            p10 = re.compile(r'^\s*(?P<private_primary_vlan>[0-9]+) +(?P<private_secondary_vlan>[a-z0-9]+) +(?P<private_vlan_type>[a-z0-9\-]+)$')
            m = p10.match(line)
            if m:
                if private_vlan_section:
                    vlanid = m.groupdict()['private_primary_vlan']
                    if vlanid not in vlan_dict['vlan_id']:
                        vlan_dict['vlan_id'][vlanid] = {}
                    vlan_dict['vlan_id'][vlanid]['private_secondary_vlan'] = \
                        m.groupdict()['private_secondary_vlan']
                    vlan_dict['vlan_id'][vlanid]['private_vlan_type'] = \
                        m.groupdict()['private_vlan_type']
                    continue

        return vlan_dict


#Incomplete parser - to be completed 
class ShowVlanInternalInfoSchema(MetaParser):
    """Schema for show vlan internal info"""
    schema = {'vlan_id':
                {Any():
                     {'vlan_configuration': bool}
                },
            }


class ShowVlanInternalInfo(ShowVlanInternalInfoSchema):
    """Parser for show vlan internal info"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show vlan internal info'

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_list = []
        vlan_configuration_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*VLAN_INFO_GLOBAL$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*vlan +configuration +(?P<vlan_ids>[0-9\-\,]+)$')
            m = p2.match(line)
            if m:
                vlan_ids = m.groupdict()['vlan_ids']
                for vlanid in re.split(r'[-,]+', vlan_ids): 
                    if 'vlan_id' not in vlan_configuration_dict:
                        vlan_configuration_dict['vlan_id'] = {}
                    if vlanid not in vlan_configuration_dict['vlan_id']:
                        vlan_configuration_dict['vlan_id'][vlanid] = {}
                    vlan_configuration_dict['vlan_id'][vlanid]['vlan_configuration'] = True
                continue

        return vlan_configuration_dict


class ShowVlanFilterSchema(MetaParser):
    """Schema show vlan filter"""
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

        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*vlan +map +(?P<vlan_access_map_tag>[a-zA-Z0-9]+):$')
            m = p1.match(line)
            if m:
                if 'vlan_id' not in vlan_dict:
                    vlan_dict['vlan_id'] = {}
                tag = m.groupdict()['vlan_access_map_tag']
                continue

            p2 = re.compile(r'^\s*Configured +on +VLANs: +(?P<access_map_vlan_ids>[0-9\,\-]+)$')
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


class ShowVlanAccessMapSchema(MetaParser):
    """Schema for show vlan access-map"""
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
        ''' parsing mechanism: cli

           Function cli() defines the cli type output parsing mechanism which
           typically contains 3 steps: exe
           cuting, transforming, returning
           '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        access_map_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Vlan +access-map +(?P<access_map_id>[a-zA-Z0-9\"]+) +(?P<access_map_sequence>[0-9]+)$')
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

            p2 = re.compile(r'^\s*match +(?P<access_map_match_protocol>[a-zA-Z0-9]+): +(?P<access_map_match_protocol_value>[a-zA-Z0-9\s]+)$')
            m = p2.match(line)
            if m:
                access_map_dict['access_map_id'][map_id]['access_map_sequence']\
                    [access_map_sequence]['access_map_match_protocol'] = m.groupdict()['access_map_match_protocol']
                access_map_dict['access_map_id'][map_id]['access_map_sequence']\
                    [access_map_sequence]['access_map_match_protocol_value'] = m.groupdict()['access_map_match_protocol_value']
                continue

            p3 = re.compile(r'^\s*action: +(?P<access_map_action_value>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:
                access_map_dict['access_map_id'][map_id]['access_map_sequence']\
                    [access_map_sequence]['access_map_action_value'] = m.groupdict()['access_map_action_value']
                continue

        return access_map_dict

# ====================================================================
# Schema for 'show vxlan'
# ====================================================================
class ShowVxlanSchema(MetaParser):    
    """Schema for show vxlan"""

    schema = {'vlan':
                {Any():
                    {'vni': str}
                },
            }

# ====================================================================
# Parser for 'show vxlan'
# ====================================================================
class ShowVxlan(ShowVxlanSchema):
    """Parser for show vxlan"""

    cli_command = 'show vxlan'

    def cli(self, output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 100             8100
            p1 = re.compile(r'^\s*(?P<vlan>[0-9]+) +(?P<vn_segment>[0-9]+)$')
            m = p1.match(line)
            if m:

                vlan = str(m.groupdict()['vlan'])
                vn_segment = str(m.groupdict()['vn_segment'])

                if 'vlan' not in ret_dict:
                    ret_dict['vlan'] = {}

                ret_dict['vlan'][vlan] = {}
                ret_dict['vlan'][vlan]['vni'] = vn_segment

                continue

        return ret_dict
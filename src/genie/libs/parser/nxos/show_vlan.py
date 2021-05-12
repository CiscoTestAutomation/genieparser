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

        # VLAN Name                             Status    Ports
        # 1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
        # 105  VLAN0105                         act/lshut Po333
        # 25   PV-VLAN25-SEC-ISO                sus/ishut Eth1/21, Eth1/22
        # 1    default                          active
        # 1   1_192.168.0.0/1                   active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
        p1 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<name>\S+) +'
                        r'(?P<status>active|suspended|act/unsup|.*/lshut|.*/ishut|sus|act)'
                        r'( *(?P<interfaces>[\w \/\,]+))?$')

        #                                                Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22
        p2 = re.compile(r'^\s*(?P<space>\s{48})(?P<interfaces>[\w\s\/\,]+)$')

        # VLAN Type         Vlan-mode
        # 1    enet         CE
        p3 = re.compile(r'^\s*(?P<vlan_id>[0-9]+) +(?P<vlan_type>[a-zA-Z]+)'
                        r' +(?P<vlan_mode>[a-zA-Z]+)?$')

        # Remote SPAN VLANs
        # -------------------------------------
        # 201-202
        # 201,202
        # 201,204,201-220
        p4 = re.compile(r'^\s*(?P<remote_span_vlans>[^--][0-9\-\,]+)?$')

        # Primary Secondary Type              Ports
        # ------- --------- ----------------- ------------------------------------------
        # 2       301       community         Fa5/3, Fa5/25
        #  2       302       community
        #          10        community
        # 20       25         isolated
        p5 = re.compile(r'^\s*(?P<primary>\d+)? +(?P<secondary>\d+)'
                        r' +(?P<type>[\w\-]+)( +(?P<interfaces>[\w\,\/ ]+))?$')

        vlan_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # 105  VLAN0105                         act/lshut Po333
            # 1    default                          active
            # 1   1_192.168.0.0/1                   active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12,
            # 25   PV-VLAN25-SEC-ISO                sus/ishut Eth1/21, Eth1/22
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
                if 'shut' in m.groupdict()['status']:
                    vlan_dict['vlans'][vlan_id]['shutdown'] = True

                if 'unsup' in m.groupdict()['status']:
                    status = 'unsupport'
                elif 'act' in m.groupdict()['status']:
                    status = 'active'
                elif 'sus' in m.groupdict()['status']:
                    status = 'suspend'
                elif 'shut' in m.groupdict()['status']:
                    status = 'shutdown'
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

            # VLAN Type         Vlan-mode
            # 1    enet         CE
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
            # 20       25         isolated
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

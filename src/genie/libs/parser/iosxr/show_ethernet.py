"""show_ethernet.py
    IOSXR commands:
        show ethernet cfm peer meps
        show ethernet trunk detail
        show ethernet tags

"""

import logging

from genie.metaparser import MetaParser
from genie.metaparser.util import merge_dict, keynames_convert
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from genie.libs.parser.utils.common import Common

class ShowEthernetCfmMepsSchema(MetaParser):
    schema = {
        'domain': {
            Any(): {
                'level': int,
                'service': str,
                Optional('mep_type'): {
                    Any(): {
                        'interface': {
                            Any(): {
                                'mep_id': int,
                                'id': {
                                    Any(): {
                                        'mac_address': {
                                            Any(): {
                                                'st': str,
                                                'port': str,
                                                'up_down_time': str,
                                                'ccm_rcvd': int,
                                                'seq_err': int,
                                                'rdi': int,
                                                'error': int
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

class ShowEthernetCfmMeps(ShowEthernetCfmMepsSchema):
    """Parser for show ethernet cfm peer meps"""

    cli_command = 'show ethernet cfm peer meps'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Sample Output

        # Flags:
        # > - Ok                          I - Wrong interval
        # R - Remote Defect received      V - Wrong level
        # L - Loop (our MAC received)     T - Timed out
        # C - Config (our ID received)    M - Missing (cross-check)
        # X - Cross-connect (wrong MAID)  U - Unexpected (cross-check)
        # * - Multiple errors received    S - Standby
        # 
        # Domain domain7_1 (level 7), Service service7_1
        # Down MEP on GigabitEthernet0/0/1/0.1 MEP-ID 10
        # ================================================================================
        # St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        # -- ----- -------------- ------- ----------- --------- ------ ----- -----
        #  >    40 a80c.0dff.6722 Up      13:20:10        48010      0     0     0
        # 
        # Domain domain7_2 (level 7), Service service7_2
        # Down MEP on GigabitEthernet0/0/1/0.2 MEP-ID 10
        # ================================================================================
        # St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        # -- ----- -------------- ------- ----------- --------- ------ ----- -----
        #  >    40 a80c.0dff.6722 Up      13:20:10        48010      0     0     0

        ret_dict = {}
        
        # Domain dom3 (level 5), Service ser3
        p1 = re.compile(r'^Domain +(?P<domain>\S+) +\(level +(?P<level>\d+)\), +Service +(?P<service>\S+)$')
        
        # Down MEP on GigabitEthernet0/0/0/0 MEP-ID 1
        # Up MEP on GigabitEthernet0/6/0/23.1 MEP-ID 500
        p2 = re.compile(r'^(?P<mep_type>\w+) +MEP +on +(?P<interface>\S+) +MEP-ID +(?P<mep_id>\d+)$')

        # V     10 0001.02ff.0706 Up      00:01:35            2      0     0     2
        # >    20 0001.02ff.0705 Up      00:00:03            4      1     0     0
        p3 = re.compile(r'^(?P<st>(>|R|L|C|X|\*|I|V|T|M|U)) +(?P<id>\d+) +(?P<mac_address>\S+) +'
            '(?P<port>\w+) +(?P<up_down_time>\S+) +(?P<ccm_rcvd>\d+) +(?P<seq_err>\d+) +'
            '(?P<rdi>\d+) +(?P<error>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # Domain dom3 (level 5), Service ser3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain = group['domain']
                level = int(group['level'])
                service = group['service']
                domain_dict = ret_dict.setdefault('domain', {}). \
                    setdefault(domain, {})
                domain_dict.update({'level': level})
                domain_dict.update({'service': service})
                
                continue
            
            # Down MEP on GigabitEthernet0/0/0/0 MEP-ID 1
            # Up MEP on GigabitEthernet0/6/0/23.1 MEP-ID 500
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                mep_type = group['mep_type'].lower()
                mep_id = int(group['mep_id'])

                interface_dict = domain_dict.setdefault('mep_type', {}). \
                    setdefault(mep_type, {}). \
                    setdefault('interface', {}). \
                    setdefault(interface, {})
                
                interface_dict.update({'mep_id': mep_id})

                continue
            
            # V     10 0001.02ff.0706 Up      00:01:35            2      0     0     2
            # >    20 0001.02ff.0705 Up      00:00:03            4      1     0     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                st = group['st']
                id = int(group['id'])
                mac_address = group['mac_address']
                port = group['port']
                up_down_time = group['up_down_time']
                ccm_rcvd = int(group['ccm_rcvd'])
                seq_err = int(group['seq_err'])
                rdi = int(group['rdi'])
                error = int(group['error'])

                mac_address_dict = interface_dict.setdefault('id', {}). \
                    setdefault(id, {}). \
                    setdefault('mac_address', {}). \
                    setdefault(mac_address, {})

                mac_address_dict.update({'st': st})
                mac_address_dict.update({'port': port})
                mac_address_dict.update({'up_down_time': up_down_time})
                mac_address_dict.update({'ccm_rcvd': ccm_rcvd})
                mac_address_dict.update({'seq_err': seq_err})
                mac_address_dict.update({'rdi': rdi})
                mac_address_dict.update({'error': error})
                continue
        return ret_dict

#Incomplete parser - to be completed 
class ShowEthernetTrunkDetailSchema(MetaParser):
    """Schema for show ethernet trunk detail"""
    schema = {'interface':
                {Any():
                    {Optional('dot1q_tunneling_ethertype'): str}
                },
            }


class ShowEthernetTrunkDetail(ShowEthernetTrunkDetailSchema):
    """Parser for show ethernet trunk detail
    parser class - implements detail parsing mechanisms for cli output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show ethernet trunk detail'
    def cli(self,output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        trunk_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<interface_name>[A-Z][a-z])([A-Za-z]+)(?P<interface_number>[0-9\/]+) +is +(?P<status>[a-z]+)$')
            m = p1.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                interface_number = m.groupdict()['interface_number']
                interface = interface_name + interface_number
                if 'interface' not in trunk_dict:
                    trunk_dict['interface'] = {}
                if interface not in trunk_dict['interface']:
                    trunk_dict['interface'][interface] = {}
                    continue

            p2 = re.compile(r'^\s*Dot1Q +Tunneling +Ethertype +is +(?P<dot1q_tunneling_ethertype>[a-z0-9]+)$')
            m = p2.match(line)
            if m:
                trunk_dict['interface'][interface]['dot1q_tunneling_ethertype'] = \
                    m.groupdict()['dot1q_tunneling_ethertype']
            continue

        return trunk_dict


class ShowEthernetTagsSchema(MetaParser):
    """Schema for show ethernet tags"""
    schema = {'interface':
                {Any():
                    {'sub_interface':
                        {Any():
                            {Optional('vlan_id'):
                                {Any():
                                    {Optional('status'): str,
                                     'mtu': str,
                                     Optional('layer'): str,
                                     'outer_encapsulation_type': str,
                                     Optional('inner_encapsulation_vlan_id'): str,
                                     Optional('inner_encapsulation_type'): str}
                                    },
                            }
                        },
                    }
                },
            }

class ShowEthernetTags(ShowEthernetTagsSchema):
    """Parser for show ethernet tags
    parser class - implements detail parsing mechanisms for cli and yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self,output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        intf_dict = {}
        stage = ''
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Interface\s +St\s +MTU\s +Ly\s +Outer\s +Inner\s +Xtra\s +-,+$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*(?P<sub_interface>[A-Za-z0-9\/\.]+) +(?P<status>[A-Za-z]+) +(?P<mtu>[0-9]+) +(?P<layer>[A-Z0-9]+) +(\.)(?P<outer_encapsulation_type>[A-Za-z0-9]+)(\:)(?P<outer_encapsulation_value>[0-9]+) +((\.)(?P<inner_encapsulation_type>[A-Za-z0-9]+)(\:)(?P<inner_encapsulation_value>[0-9]+))?')
            m = p2.match(line)
            if m:
                sub_interface = m.groupdict()['sub_interface']
                stage = re.search('[A-Za-z0-9\/]+',sub_interface)
                interface = stage.group()
                if 'interface' not in intf_dict:
                    intf_dict['interface'] = {}
                if interface not in intf_dict['interface']:
                    intf_dict['interface'][interface] = {}

                if 'sub_interface' not in intf_dict['interface'][interface]:
                    intf_dict['interface'][interface]['sub_interface'] = {}
                if sub_interface not in intf_dict['interface'][interface]['sub_interface']:
                    intf_dict['interface'][interface]['sub_interface'][sub_interface] = {}

                vlan_id = m.groupdict()['outer_encapsulation_value']
                if 'vlan_id' not in intf_dict['interface'][interface]['sub_interface'][sub_interface]:
                    intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'] = {}
                if vlan_id not in intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id']:
                    intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id] = {}

                intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['status'] = \
                    m.groupdict()['status']
                intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['mtu'] = \
                    m.groupdict()['mtu']
                intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['layer'] = \
                    m.groupdict()['layer']
                intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['outer_encapsulation_type'] = \
                    'dot' + m.groupdict()['outer_encapsulation_type']
                inner_encapsulation_type = m.groupdict()['inner_encapsulation_type']
                if inner_encapsulation_type:
                    intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['inner_encapsulation_type'] = \
                        'dot' + inner_encapsulation_type
                    intf_dict['interface'][interface]['sub_interface'][sub_interface]['vlan_id'][vlan_id]['inner_encapsulation_vlan_id'] = \
                        m.groupdict()['inner_encapsulation_value']
                continue

        return intf_dict

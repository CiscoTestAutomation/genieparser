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

from genie.libs.parser.base import *

def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match


class ShowEthernetCfmMeps(MetaParser):
    """Parser for show ethernet cfm peer meps"""
    # TODO schema

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def cli(self):

        cmd = 'show ethernet cfm peer meps'

        out = self.device.execute(cmd)

        result = {
            'entries' : []
        }

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
        #  >    40 a80c.0d4f.18d2 Up      13:20:10        48010      0     0     0
        # 
        # Domain domain7_2 (level 7), Service service7_2
        # Down MEP on GigabitEthernet0/0/1/0.2 MEP-ID 10
        # ================================================================================
        # St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        # -- ----- -------------- ------- ----------- --------- ------ ----- -----
        #  >    40 a80c.0d4f.18d2 Up      13:20:10        48010      0     0     0

        title_found = False
        header_processed = False
        field_indice = []

        def _retrieve_fields(line,field_indice):
            res = []
            for idx,(start,end) in enumerate(field_indice):
                if idx == len(field_indice) - 1:
                    res.append(line[start:].strip())
                else:
                    res.append(line[start:end].strip())
            return res

        lines = out.splitlines()
        for idx,line in enumerate(lines):

            m = re.match(r'Domain (\w+).+level (\w+).+Service (\w+)',line)
            if m:
                domain = m.group(1)
                level = m.group(2)
                service = m.group(3)

            m = re.match(r'.+ on (\S+) MEP-ID (\w+)',line)
            if m:
                interface = m.group(1)
                local_id = m.group(2)
                
            if idx == len(lines) - 1:
                break

            line = line.rstrip()
            if not header_processed:
                # 1. check proper title header exist
                if re.match(r"^St\s+ID\s+MAC Address\s+Port\s+Up/Downtime\s+CcmRcvd\s+SeqErr\s+RDI\s+Error",line):
                    title_found = True
                    continue
                # 2. get dash header line
                if title_found and re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line):
                    match = re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line)
                    start = 0
                    for field in match.groups():
                        if '-' in field:
                            end = start + len(field)
                            field_indice.append((start,end))
                            start = end
                        else:
                            start += len(field)
                            end += len(field)
                    header_processed = True
                    continue

            elif re.match('^\s*$',line):
                title_found = False
                header_processed = False
                field_indice = []

            else:
                status,remote_id,mac,port,time,ccm_rcvd,seq_error,rdi,error = _retrieve_fields(line,field_indice)
                result['entries'].append({
                    'domain' : domain,
                    'level' : level,
                    'service' : service,
                    'status' : status,
                    'remote_id' : remote_id,
                    'local_id' : local_id,
                    'interface' : interface,
                    'mac_address' : mac,
                    'time' : time,
                    'ccm_rcvd' : ccm_rcvd,
                    'seq_error' : seq_error,
                    'rdi' : rdi,
                    'error' : error,
                })

        return result


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

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        cmd = 'show ethernet trunk detail'.format()
        out = self.device.execute(cmd)
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

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        cmd = 'show ethernet tags'.format()
        out = self.device.execute(cmd)
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

    def yang(self):
        """parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        """

        ret = {}
        cmd = '''<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper"><interface-xr><interface/></interface-xr></interfaces>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for interfaces in data:
                for interface_xr in interfaces:
                    interface_name = None
                    encapsulation_type = None
                    sub_interface = None
                    mtu = None
                    outer_tag = None
                    second_tag = None
                    for interface in interface_xr:
                        # Remove the namespace
                        text = interface.tag[interface.tag.find('}')+1:]
                        if text == 'interface-name':
                            sub_interface = interface.text
                            continue
                        if text == 'encapsulation':
                            encapsulation_type = interface.text
                            continue
                        if text == 'parent-interface-name':
                            interface_name = interface.text
                            continue
                        if text == 'mtu':
                            mtu = interface.text
                            continue
                        if encapsulation_type:
                            for encapsulation_information in interface:
                                for dot1q_information in encapsulation_information:
                                    for encapsulation_details in dot1q_information:
                                        for stack in encapsulation_details:
                                            # Remove the namespace
                                            text = stack.tag[stack.tag.find('}')+1:]
                                            if text == 'outer-tag':
                                                outer_tag = stack.text
                                                continue
                                            if text == 'second-tag':
                                                second_tag = stack.text
                                                continue

                        # Let's build it now
                        if 'interface' not in ret:
                            ret['interface'] = {}
                        if interface_name is not None:
                            ret['interface'][interface_name] = {}
                            if sub_interface is not None:
                                if 'sub_interface' not in ret['interface'][interface_name]:
                                    ret['interface'][interface_name]['sub_interface'] = {}
                                ret['interface'][interface_name]['sub_interface'][sub_interface] = {}
                                if outer_tag is not None:
                                    if 'vlan_id' not in ret['interface'][interface_name]['sub_interface'][sub_interface]:
                                        ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'] = {}
                                    ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'][outer_tag] = {}
                                    if encapsulation_type is not None:
                                        ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'][outer_tag]['outer_encapsulation_type'] = \
                                            encapsulation_type
                                        ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'][outer_tag]['inner_encapsulation_type'] = \
                                            encapsulation_type
                                    if second_tag is not None:
                                        ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'][outer_tag]['inner_encapsulation_vlan_id'] = \
                                            second_tag
                                    if mtu is not None:
                                        ret['interface'][interface_name]['sub_interface'][sub_interface]['vlan_id'][outer_tag]['mtu'] = \
                                            mtu
        return ret

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output

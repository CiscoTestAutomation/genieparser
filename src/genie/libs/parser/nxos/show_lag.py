"""show_lag.py
    supported commands:
    * show feature
    * show lacp system-identifier
    * show lacp counters
    * show lacp neighbor
    * show port-channel summary
    * show port-channel database
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# import parser utils
from genie.libs.parser.utils.common import Common


# ============================
# parser for show feature
# ============================
class ShowFeatureSchema(MetaParser):
    """schema for: show feature"""
    schema = {
        'features': {
            Any(): {
                'instances': {
                    Any(): bool
                }
            }
        }
    }


class ShowFeature(ShowFeatureSchema):
    """parser for show feature"""
    cli_command = 'show feature'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}
        # bash-shell             1          disabled
        p1 = re.compile(
            r'^(?P<feature_name>[\w-]+)\s+(?P<instance>\d+)\s+(?P<state>('
            r'disabled|enabled))$')

        for line in out.splitlines():
            line = line.strip()
            # bash-shell             1          disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                state = True if group['state'] == 'enabled' else False
                sub_dict = parsed_dict.setdefault('features', {}).setdefault(
                    group['feature_name'], {}).setdefault('instances', {})
                sub_dict[group['instance']] = state

                continue
        return parsed_dict


# ============================
# parser for show lacp system-identifier
# ============================
class ShowLacpSystemIdentifierSchema(MetaParser):
    """Schema for show lacp system-identifier"""
    schema = {
        'system_id_mac': str,
        'system_priority': int,
    }


class ShowLacpSystemIdentifier(ShowLacpSystemIdentifierSchema):
    """Parser for :
       show lacp sys-id"""

    cli_command = 'show lacp sys-id'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        # 32768,5e-2-0-1-0-7
        p1 = re.compile(r'^\s*(?P<system_priority>[\d]+), *(?P<system_id_mac>[\w.\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'system_priority': int(group['system_priority'])})
                parsed_dict.update({'system_id_mac': group['system_id_mac']})
                continue

        return parsed_dict


# ============================
# schema for show lacp counters
# ============================
class ShowLacpCountersSchema(MetaParser):
    """schema for: show lcap counters"""
    schema = {
        'interfaces': {
            Any(): {
                'members': {
                    Any(): {
                        'interface': str,
                        'counters': {
                            'lacp_in_pkts': int,
                            'lacp_out_pkts': int,
                            'lacp_errors': int,
                            'marker_in_pkts': int,
                            'marker_out_pkts': int
                        },
                    },
                }
            },
        },
    }


# =============================
# parser for show lacp counters
# ============================
class ShowLacpCounters(ShowLacpCountersSchema):
    """Parser for: show lacp counters"""

    cli_command = 'show lacp counters'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dict
        parsed_dict = {}
        intf_dict = {}
        # port-channel1
        p1 = re.compile(r'^port-channel\d+$')
        # ------------------------------------------------------------------------------
        #                              LACPDUs                      Markers / Resp
        # LACPDUs
        # Port              Sent                Recv                  Recv
        # Sent  Pkts
        # Err
        # ------------------------------------------------------------------------------
        # port - channel1
        # Ethernet1 / 1        92                   85                     0      0   
        # 0      
        # Ethernet1 / 2        79                   87                     0      0   
        # 0      
        #
        # port - channel2
        # Ethernet1 / 3        136                  112                    0      0   
        # 0      
        # Ethernet1 / 4        95                   90                     0      0   
        # 0      
        # Ethernet1 / 5        118                  146                    0      0   
        # 0      
        p2 = re.compile(
            r'^(?P<interface>[\w\/]+) +(?P<lacp_out_pkts>[\d]+) +(?P<lacp_in_pkts>[\d]+)'
            ' +(?P<marker_in_pkts>[\d]+) +(?P<marker_out_pkts>[\d]+) +( +('
            '?P<lacp_pkts_errors>[\d]+))?$')

        for line in out.splitlines():
            if line:
                line = line.strip().replace('\xa0', ' ')
            else:
                continue

            # port-channel1
            m = p1.match(line)
            if m:
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(m.group(),
                                                                                {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"])
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface,
                                                                             {})
                member_dict.update({'interface': interface})
                counter_dict = member_dict.setdefault('counters', {})
                counter_dict.update({'lacp_in_pkts': int(group['lacp_in_pkts'])})
                counter_dict.update({'lacp_out_pkts': int(group['lacp_out_pkts'])})
                counter_dict.update({'marker_in_pkts': int(group['marker_in_pkts'])})
                counter_dict.update({'marker_out_pkts': int(group['marker_out_pkts'])})
                counter_dict.update({'lacp_errors': int(group['lacp_pkts_errors'])})
                continue

        return parsed_dict


# =============================
# schema for show lacp neighbor
# ============================
class ShowLacpNeighborSchema(MetaParser):
    """schema for: show lacp neighbor"""
    schema = {
        'interfaces': {
            Any(): {
                'members': {
                    Any(): {
                        'interface': str,
                        'activity': str,
                        'oper_key': int,
                        'port_num': int,
                        'partner_id': str,
                        'age': int,
                        'interval': str,
                        'lacp_port_priority': int,
                        'port_state': int,
                    },
                }
            },
        },
    }


# =============================
# parser for show lacp neighbor
# ============================
class ShowLacpNeighbor(ShowLacpNeighborSchema):
    """parser for: show lacp neighbor"""
    cli_command = 'show lacp neighbor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}
        intf_dict = {}
        member_dict = {}
        # port-channel1 neighbors
        p1 = re.compile(r'^(?P<port_channel>[\w-]+)[\xa0 ]+neighbors$')
        #             Partner                Partner                     Partner
        # Port        System ID              Port Number     Age         Flags
        # Eth1/1      32768,5e-2-0-1-0-7     0x101           1140        SA
        p2 = re.compile(
            r'^(?P<interface>[\w/]+)[\xa0 ]+\d+,[\xa0 ]*(?P<sys_id>[\w.\-]+)[\xa0 ]+('
            r'?P<port_num>0x[a-fA-F0-9]+)[\xa0 ]+(?P<age>\d+)[\xa0 ]+(?P<flags>[\w]+)$')
        #             LACP Partner           Partner                     Partner
        #             Port Priority          Oper Key                    Port State
        #             32768                  0x8000                      0x3d
        p3 = re.compile(
            r'^(?P<lacp_port_priority>\d+)[\xa0 ]+(?P<oper_key>0x[a-fA-F0-9]+)[\xa0 ]+('
            r'?P<port_state>0x[a-fA-F0-9]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(
                    group['port_channel'], {})
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface,
                                                                             {})
                member_dict.update({'interface': interface})
                flags = group['flags'].lower()
                if 'a' in flags:
                    activity = 'active'
                else:
                    activity = 'passive'
                if 's' in flags:
                    interval = 'slow'
                else:
                    interval = 'fast'

                member_dict.update({'interval': interval})
                member_dict.update({'activity': activity})

                member_dict.update({'port_num': int(group['port_num'], 0)})
                member_dict.update({'partner_id': group['sys_id']})
                member_dict.update({'age': int(group['age'])})
                continue
            m = p3.match(line)
            if m:
                group = m.groupdict()
                member_dict.update(
                    {'lacp_port_priority': int(group['lacp_port_priority'])})
                member_dict.update({'oper_key': int(group['oper_key'], 0)})
                member_dict.update({'port_state': int(group['port_state'], 0)})
                continue

        return parsed_dict


# =============================
# schema for show port-channel summary
# ============================
class ShowPortChannelSummarySchema(MetaParser):
    """schema for: show show port-channel summary"""
    schema = {
        'interfaces': {
            Any(): {
                'bundle_id': int,
                'oper_status': str,
                'layer': str,  # routed vs switched
                'protocol': str,
                'type': str,
                'members': {
                    Any(): {
                        'flags': str,
                    }
                },
            },
        }
    }


# =============================
# parser for show port-channel summary
# ============================
class ShowPortChannelSummary(ShowPortChannelSummarySchema):
    """parser for: show port-channel summary"""

    cli_command = 'show port-channel summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        inft_dict = {}

        # --------------------------------------------------------------------------------
        # Group Port-       Type     Protocol  Member Ports
        #       Channel
        # --------------------------------------------------------------------------------
        # 1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth1/2(P)
        # 2     Po2(SU)     Eth      LACP      Eth1/3(P)    Eth1/4(P)    Eth1/5(H)
        p1 = re.compile(
            r'(?P<bundle_id>[\d]+)[\xa0 ]+(?P<name>[\w\-]+)\((?P<flags>[\w]+)\)?[\xa0 '
            r']+(?P<type>\w+)[\xa0 ]+(?P<protocol>[\w\-]+)?[\xa0 ]+(?P<ports>[\w\-/() '
            r'\xa0]+ *)?$')
        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            # 1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth1/2(P)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = Common.convert_intf_name(group["name"])
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'bundle_id': int(group["bundle_id"])})
                intf_dict.update({'type': group['type'].lower()})
                intf_dict.update({'protocol': group['protocol'].lower()})
                flags = group['flags'].lower()
                intf_dict['layer'] = 'switched' if 's' in flags else 'routed'
                intf_dict['oper_status'] = 'up' if 'u' in flags else 'down'
                port_dict = intf_dict.setdefault('members', {})
                port_list = re.findall(r'([\w/]+)\((\w+)\)', group['ports'])
                for port in port_list:
                    intf = Common.convert_intf_name(port[0])
                    port_sub_dict = port_dict.setdefault(intf, {})
                    port_sub_dict['flags'] = port[1]

                continue

        return parsed_dict


# =====================================
# schema for show port-channel database
# =====================================
class ShowPortChannelDatabaseSchema(MetaParser):
    """show post-channel database"""
    schema = {

    }

"""show_lag.py
    supported commands:
    * show lacp system-identifier
    * show lacp counters
    * show lacp neighbor
    * show port-channel summary
    * show port-channel database
"""

# Python
import re

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
       show lacp system-identifier"""

    cli_command = 'show lacp system-identifier'

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
                            'marker_resp_in_pkts': int,
                            'marker_resp_out_pkts': int
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
    exclude = ['lacp_in_pkts' , 'lacp_out_pkts']

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
        #                              LACPDUs                      Markers / Resp
        # LACPDUs
        # Port              Sent                Recv                  Recv
        # Sent  Pkts
        # Err
        # ------------------------------------------------------------------------------
        # port - channel1
        # Ethernet1 / 1        92                   85                     0      0
        # 0
        # Ethernet1 / 2        79                   87                     0      0
        # 0
        #
        # port - channel2
        # Ethernet1 / 3        136                  112                    0      0
        # 0
        # Ethernet1 / 4        95                   90                     0      0
        # 0
        # Ethernet1 / 5        118                  146                    0      0
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
                port_channel = Common.convert_intf_name(m.group()).capitalize()
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(
                    port_channel, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"]).capitalize()
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface,
                                                                             {})
                member_dict.update({'interface': interface})
                counter_dict = member_dict.setdefault('counters', {})
                counter_dict.update({'lacp_in_pkts': int(group['lacp_in_pkts'])})
                counter_dict.update({'lacp_out_pkts': int(group['lacp_out_pkts'])})
                counter_dict.update({'marker_resp_in_pkts': int(group['marker_in_pkts'])})
                counter_dict.update(
                    {'marker_resp_out_pkts': int(group['marker_out_pkts'])})
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
    exclude = ['age']

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
        #             Partner                Partner                     Partner
        # Port        System ID              Port Number     Age         Flags
        # Eth1/1      32768,5e-2-0-1-0-7     0x101           1140        SA
        p2 = re.compile(
            r'^(?P<interface>[\w/]+)[\xa0 ]+\d+,[\xa0 ]*(?P<sys_id>[\w.\-]+)[\xa0 ]+('
            r'?P<port_num>0x[a-fA-F0-9]+)[\xa0 ]+(?P<age>\d+)[\xa0 ]+(?P<flags>[\w]+)$')
        #             LACP Partner           Partner                     Partner
        #             Port Priority          Oper Key                    Port State
        #             32768                  0x8000                      0x3d
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
                port_channel = Common.convert_intf_name(
                    group['port_channel']).capitalize()
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(
                    port_channel, {})
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface")).capitalize()
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
        # Group Port-       Type     Protocol  Member Ports
        #       Channel
        # --------------------------------------------------------------------------------
        # 1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth1/2(P)
        # 2     Po2(SU)     Eth      LACP      Eth1/3(P)    Eth1/4(P)    Eth1/5(H)
        p1 = re.compile(
            r'(?P<bundle_id>[\d]+)[\xa0 ]+(?P<name>[\w\-]+)\((?P<flags>[\w]+)\)?[\xa0 '
            r']+(?P<type>\w+)[\xa0 ]+(?P<protocol>[\w\-]+)?[\xa0 ]+(?P<ports>[\w\-/() '
            r'\xa0]+ *)?$')
        #                                      Eth1/6(P)    Eth1/7(P)    Eth1/8(H)
        p2 = re.compile(
            r'^\s*(?P<space>\s{37})(?P<ports>[\w\-\/() \xa0]+)?')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            # 1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth1/2(P)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = Common.convert_intf_name(group["name"]).capitalize()
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'bundle_id': int(group["bundle_id"])})
                intf_dict.update({'type': group['type'].lower()})
                intf_dict.update({'protocol': group['protocol'].lower()})
                flags = group['flags'].lower()
                intf_dict.update({'layer': 'switched' if 's' in flags else 'routed'})
                intf_dict.update({'oper_status': 'up' if 'u' in flags else 'down'})
                port_dict = intf_dict.setdefault('members', {})
                port_list = re.findall(r'([\w/]+)\((\w+)\)', group['ports'])
                for port in port_list:
                    intf = Common.convert_intf_name(port[0]).capitalize()
                    port_sub_dict = port_dict.setdefault(intf, {})
                    port_sub_dict.update({'flags': port[1]})

                continue

            #                               Eth1/46(P)   Eth1/47(D)   Eth1/48(P)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_list = re.findall(r'([\w/]+)\((\w+)\)', group['ports'])
                for port in port_list:
                    intf = Common.convert_intf_name(port[0]).capitalize()
                    port_sub_dict = port_dict.setdefault(intf, {})
                    port_sub_dict.update({'flags': port[1]})

                continue

        return parsed_dict


# =====================================
# schema for show port-channel database
# =====================================
class ShowPortChannelDatabaseSchema(MetaParser):
    """ schema for : show post-channel database"""
    schema = {
        'interfaces': {
            Any(): {
                'last_update_success': bool,  # successful => True, else False
                'total_ports': int,
                'up_ports': int,
                'port_channel_age': str,
                'time_last_bundle': str,
                'last_bundled_member': str,
                Optional('first_oper_port'): str,
                Optional('time_last_unbundle'): str,
                Optional('last_unbundled_member'): str,
                'members': {
                    Any(): {
                        'activity': str,
                        'status': str,
                        'is_first_oper_port': bool
                    }
                }

            }
        }

    }


# =====================================
# parser for show port-channel database
# =====================================
class ShowPortChannelDatabase(ShowPortChannelDatabaseSchema):
    """parser show port-channel database"""
    cli_command = 'show port-channel database'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        intf_dict = {}
        # port-channel1
        p1 = re.compile(r'^port-channel\d+$')
        # Last membership update is successful
        p2 = re.compile(r'^Last +membership +update +is +(?P<last_update_status>\w+)$')
        # 2 ports in total, 2 ports up
        p3 = re.compile(
            r'^(?P<total_ports>\d+) +ports +in +total, +(?P<up_ports>\d+) +ports +up$')
        # First operational port is Ethernet1/1
        p4 = re.compile(r'^First +operational +port +is +(?P<first_oper_port>[\w/]+)$')
        # Age of the port-channel is 0d:02h:31m:22s
        p5 = re.compile(
            r'^Age +of +the +port-channel +is +(?P<port_channel_age>[0-9:smhd]+)$')
        # Time since last bundle is 0d:02h:28m:30s
        p6 = re.compile(
            r'^Time +since +last +bundle +is +(?P<time_last_bundle>[0-9:smhd]+)$')
        # Last bundled member is Ethernet1/2
        p7 = re.compile(r'^Last +bundled +member +is +(?P<last_bundled_member>[\w/]+)$')
        # Time since last unbundle is 0d:00h:14m:05s
        p8 = re.compile(
            r'^Time +since +last +unbundle +is +(?P<time_last_unbundle>[0-9:smhd]+)$')
        # Last unbundled member is Ethernet1/5
        p9 = re.compile(
            r'^Last +unbundled +member +is +(?P<last_unbundled_member>[\w/]+)$')
        #     Ports:   Ethernet1/3     [passive] [up]
        #              Ethernet1/4     [passive] [up] *
        #              Ethernet1/5     [passive] [hot-standy]
        #     Ports:   Ethernet1/25    [on] [up]
        #              Ethernet1/26    [on] [up] *
        p10 = re.compile(
            r'^(Ports:)?\s*(?P<interface>[\w/]+)\s+\[(?P<activity>(passive|active|on|off)) *\] '
            r'+\['
            r'(?P<status>[\w-]+)\](?P<fop>\s+\*)*$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            # port-channel1
            m = p1.match(line)
            if m:
                name = Common.convert_intf_name(m.group()).capitalize()
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(name, {})
                continue
            # Last membership update is successful
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'last_update_success': True if group[
                                                                     'last_update_status'] == 'successful' else False})
                continue
            # 2 ports in total, 2 ports up
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'total_ports': int(group['total_ports'])})
                intf_dict.update({'up_ports': int(group['up_ports'])})
                continue
            # First operational port is Ethernet1/1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'first_oper_port': group['first_oper_port']})
                continue
            # Age of the port-channel is 0d:02h:31m:22s
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'port_channel_age': group['port_channel_age']})
                continue
            # Time since last bundle is 0d:02h:28m:30s
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'time_last_bundle': group['time_last_bundle']})
                continue
            # Last bundled member is Ethernet1/2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'last_bundled_member': group['last_bundled_member']})
                continue
            # Time since last unbundle is 0d:00h:14m:05s
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'time_last_unbundle': group['time_last_unbundle']})
                continue
            # Last unbundled member is Ethernet1/5
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'last_unbundled_member': group['last_unbundled_member']})
                continue
            #     Ports:   Ethernet1/3     [passive] [up]
            #              Ethernet1/4     [passive] [up] *
            #              Ethernet1/5     [passive] [hot-standy]
            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_dict = intf_dict.setdefault('members', {}).setdefault(
                    group['interface'], {})
                sub_dict.update({'activity': group['activity']})
                sub_dict.update({'status': group['status']})
                sub_dict.update({'is_first_oper_port': True if group['fop'] else False})
                continue
        return parsed_dict

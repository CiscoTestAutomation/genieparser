"""show_lag.py
   supported commands:
     *  show lacp sys-id
     *  show lacp counters
     *  show lacp <channel_group> counters
     *  show lacp internal
     *  show lacp <channel_group> internal
     *  show lacp neighbor
     *  show lacp <channel_group> neighbor
     *  show pagp counters
     *  show pagp <channel_group> counters
     *  show pagp neighbor
     *  show pagp <channel_group> neighbor
     *  show pagp internal
     *  show pagp <channel_group> internal
     *  show etherchannel summary
     *  show etherchannel load-balancing
     *  show lacp neighbor detail
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


# ====================================================
#  parser for show lacp sys-id
# ====================================================
class ShowLacpSysIdSchema(MetaParser):
    """Schema for:
        show lacp sys-id"""

    schema = {
            'system_id_mac': str,
            'system_priority': int,
            }

class ShowLacpSysId(ShowLacpSysIdSchema):
    """Parser for :
       show lacp sys-id"""

    cli_command = 'show lacp sys-id'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # 32768, 001e.49af.8c00
        # 32768,0014.a93d.4a00
        # 8000,AC-12-34-56-78-90
        p1 = re.compile(r'^\s*(?P<system_priority>[\d]+), *(?P<system_id_mac>[\w\.\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'system_priority': int(group.pop('system_priority'))})
                result_dict.update({'system_id_mac': group.pop('system_id_mac')})
                continue

        return result_dict

# ====================================================
#  schema for show lacp counters
# ====================================================
class ShowLacpCountersSchema(MetaParser):
    """Schema for:
        show lacp counters"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'counters': {
                            'lacp_in_pkts': int,
                            'lacp_out_pkts': int,
                            'lacp_pkts': int,
                            Optional('lacp_errors'): int,
                            'marker_in_pkts': int,
                            'marker_out_pkts': int,
                            Optional('marker_response_in_pkts'): int,
                            Optional('marker_response_out_pkts'): int,
                        },
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show lacp counters
# ====================================================
class ShowLacpCounters(ShowLacpCountersSchema):
    """Parser for :
      show lacp counters"""

    cli_command = ['show lacp {channel_group} counters', 'show lacp counters']

    def cli(self, channel_group="",output=None):
        if output is None:
            if channel_group:
                cmd = self.cli_command[0].format(channel_group=channel_group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        #              LACPDUs         Marker      Marker Response    LACPDUs
        # Port       Sent   Recv     Sent   Recv     Sent   Recv      Pkts Err
        # ---------------------------------------------------------------------
        # Channel group: 1
        # Gi2         27     22       0      0        0      0         0
        # Gi5/0/0     21     18       0      0        0      0         0    0
        #              LACPDUs         Marker       LACPDUs
        # Port       Sent   Recv     Sent   Recv     Pkts Err
        # ---------------------------------------------------
        # Channel group: 1
        #   Fa4/1    8      15       0      0         3    0
        #   Fa4/3    14     18       0      0         0

        p1 = re.compile(r'^\s*Channel +group: +(?P<channel_group>[\d]+)$')
        p2 = re.compile(r'^\s*(?P<interface>[\w\/]+) +(?P<lacp_out_pkts>[\d]+) +(?P<lacp_in_pkts>[\d]+)'
                         ' +(?P<marker_out_pkts>[\d]+) +(?P<marker_in_pkts>[\d]+)'
                         '( +(?P<marker_response_out_pkts>[\d]+) +(?P<marker_response_in_pkts>[\d]+))?'
                         ' +(?P<lacp_pkts>[\d]+)( +(?P<lacp_errors>[\d]+))?$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel'+ group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name,{})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'lacp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                counter_dict = member_dict.setdefault('counters', {})
                counter_dict.update({'lacp_in_pkts': int(group.pop('lacp_in_pkts'))})
                counter_dict.update({'lacp_out_pkts': int(group.pop('lacp_out_pkts'))})
                counter_dict.update({'marker_in_pkts': int(group.pop('marker_in_pkts'))})
                counter_dict.update({'marker_out_pkts': int(group.pop('marker_out_pkts'))})
                counter_dict.update({'lacp_pkts': int(group.pop('lacp_pkts'))})

                if group['marker_response_in_pkts']:
                    counter_dict.update({'marker_response_in_pkts': int(group.pop('marker_response_in_pkts'))})
                if group['marker_response_out_pkts']:
                    counter_dict.update({'marker_response_out_pkts': int(group.pop('marker_response_out_pkts'))})
                if group['lacp_errors']:
                    counter_dict.update({'lacp_errors': int(group.pop('lacp_errors'))})
                continue

        return result_dict

# ====================================================
#  schema for show lacp internal
# ====================================================
class ShowLacpInternalSchema(MetaParser):
    """Schema for:
        show lacp internal"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'oper_key': int,
                        'admin_key':int,
                        'port_num': int,
                        'lacp_port_priority': int,
                        'flags': str,
                        Optional('activity'): str,
                        'state': str,
                        'bundled': bool,
                        'port_state': int,
                        Optional('lacp_interval'): str,
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show lacp internal
# ====================================================
class ShowLacpInternal(ShowLacpInternalSchema):
    """Parser for :
      show lacp internal"""

    cli_command = ['show lacp {channel_group} internal', 'show lacp internal']

    def cli(self, channel_group="",output=None):
        if output is None:
            if channel_group:
                cmd = self.cli_command[0].format(channel_group=channel_group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # Channel group 1
        #                             LACP port     Admin     Oper    Port        Port
        # Port      Flags   State     Priority      Key       Key     Number      State
        # Gi2       SA      bndl      32768         0x1       0x1     0x1         0x3D
        # Gi3/2     FA      bndl-sby  32768         0x1       0x1     0xF303      0x7
        #                             LACPDUs     LACP Port    Admin   Oper    Port     Port
        # Port      Flags    State    Interval    Priority     Key     Key     Number   State
        # Fa4/1     saC      bndl     30s         32768        100     100     0xc1     0x75
        p1 = re.compile(r'^\s*Channel +group +(?P<channel_group>[\d]+)$')
        p2 = re.compile(r'^\s*(?P<interface>[\w\/]+) +(?P<flags>[\w]+)'
                        ' +(?P<state>[\S]+)( +(?P<lacp_interval>[\w]+))?'
                        ' +(?P<lacp_port_priority>[\d]+) +(?P<admin_key>[\w]+)'
                        ' +(?P<oper_key>[\w]+) +(?P<port_num>[\w]+)'
                        ' +(?P<port_state>[\w]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'lacp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                flags = group.pop('flags')
                activity = 'auto' if 'a' in flags.lower() else None
                if activity:
                    member_dict.update({'activity': activity})
                member_dict.update({'flags': flags})
                state = group.pop('state')
                if 'bndl' in state:
                    bundled = True
                else:
                    bundled = False
                member_dict.update({'state': state})
                member_dict.update({'bundled': bundled})
                member_dict.update({'lacp_port_priority': int(group.pop('lacp_port_priority'))})
                member_dict.update({'admin_key': int(group.pop('admin_key'),0)})
                member_dict.update({'oper_key': int(group.pop('oper_key'),0)})
                member_dict.update({'port_num': int(group.pop('port_num'),0)})
                member_dict.update({'port_state': int(group.pop('port_state'),0)})
                if group['lacp_interval']:
                    member_dict.update({'lacp_interval': group['lacp_interval']})
                continue

        return result_dict

# ====================================================
#  schema for show lacp neighbor
# ====================================================
class ShowLacpNeighborSchema(MetaParser):
    """Schema for:
        show lacp neighbor"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'activity': str,
                        'oper_key': int,
                        'admin_key': int,
                        'port_num': int,
                        'partner_id': str,
                        'age': int,
                        'flags': str,
                        'lacp_port_priority': int,
                        Optional('port_state'): int,
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show lacp neighbor
# ====================================================
class ShowLacpNeighbor(ShowLacpNeighborSchema):
    """Parser for :
      show lacp neighbor"""

    cli_command = ['show lacp {channel_group} neighbor', 'show lacp neighbor']

    def cli(self, channel_group="", output=None):
        if output is None:
            if channel_group:
                cmd = self.cli_command[0].format(channel_group=channel_group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # Channel group 1 neighbors
        #                   LACP port                        Admin  Oper   Port    Port
        # Port      Flags   Priority  Dev ID          Age    key    Key    Number  State
        # Gi2       SA      32768     001e.49e6.bc00  25s    0x0    0x1    0x1     0x3D
        # Gi5/0/0   SP      32768     0011.2026.7300  11s    0x1    0x14   0x3C
        p1 = re.compile(r'^\s*Channel +group +(?P<channel_group>[\d]+) +neighbors$')
        p2 = re.compile(r'^\s*(?P<interface>[\w\/]+) +(?P<flags>[\w]+)'
                        ' +(?P<lacp_port_priority>[\d]+) +(?P<partner_id>[\w\.]+) +(?P<age>[\d]+)s +(?P<admin_key>[\w]+)'
                        ' +(?P<oper_key>[\w]+) +(?P<port_num>[\w]+)'
                        '( +(?P<port_state>[\w]+))?$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'lacp'})
                continue

            m = p2.match(line)
            if m:
                activity = None
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                flags = group.pop('flags')
                if 'a' in flags.lower():
                    activity = 'active'
                else:
                    activity = 'passive'

                member_dict.update({'flags': flags})
                member_dict.update({'activity': activity})
                member_dict.update({'lacp_port_priority': int(group.pop('lacp_port_priority'))})
                member_dict.update({'admin_key': int(group.pop('admin_key'), 0)})
                member_dict.update({'oper_key': int(group.pop('oper_key'), 0)})
                member_dict.update({'port_num': int(group.pop('port_num'), 0)})
                member_dict.update({'partner_id': group.pop('partner_id')})
                member_dict.update({'age': int(group.pop('age'))})
                if group['port_state']:
                    member_dict.update({'port_state': int(group.pop('port_state'),0)})
                continue

        return result_dict

# ====================================================
#  schema for show pagp counters
# ====================================================
class ShowPagpCountersSchema(MetaParser):
    """Schema for:
        show pagp counters"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'counters': {
                            'information_in_pkts': int,
                            'information_out_pkts': int,
                            'pagp_errors': int,
                            'flush_in_pkts': int,
                            'flush_out_pkts': int,
                        },
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show pagp counters
# ====================================================
class ShowPagpCounters(ShowPagpCountersSchema):
    """Parser for :
      show pagp counters"""
    cli_command = 'show pagp {channel_group} counters'

    def cli(self, channel_group="",output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(channel_group=channel_group))
        else:
            out = output

        result_dict = {}
        #           Information         Flush        PAgP
        # Port      Sent    Recv     Sent    Recv    Err Pkts
        # ---------------------------------------------------
        # Channel group: 1
        # Gi0/1     60      52       0       0       0

        p1 = re.compile(r'^\s*Channel +group: +(?P<channel_group>[\d]+)$')
        p2 = re.compile(r'^\s*(?P<interface>[\w\/]+) +(?P<information_out_pkts>[\d]+)'
                        ' +(?P<information_in_pkts>[\d]+) +(?P<flush_out_pkts>[\d]+) +(?P<flush_in_pkts>[\d]+)'
                        ' +(?P<pagp_errors>[\d]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'pagp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                counter_dict = member_dict.setdefault('counters', {})
                counter_dict.update({'information_in_pkts': int(group.pop('information_in_pkts'))})
                counter_dict.update({'information_out_pkts': int(group.pop('information_out_pkts'))})
                counter_dict.update({'flush_out_pkts': int(group.pop('flush_out_pkts'))})
                counter_dict.update({'flush_in_pkts': int(group.pop('flush_in_pkts'))})
                counter_dict.update({'pagp_errors': int(group.pop('pagp_errors'))})
                continue
        return result_dict

# ====================================================
#  schema for show pagp neighbor
# ====================================================
class ShowPagpNeighborSchema(MetaParser):
    """Schema for:
        show pagp neighbor"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        Optional('activity'): str,
                        'partner_name': str,
                        'partner_id': str,
                        'partner_port': str,
                        'age': int,
                        'flags': str,
                        'group_cap': str,
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show pagp neighbor
# ====================================================
class ShowPagpNeighbor(ShowPagpNeighborSchema):
    """Parser for :
      show pagp neighbor"""

    cli_command = ['show pagp {channel_group} neighbor', 'show pagp neighbor']

    def cli(self, channel_group="", output=None):
        if output is None:
            if channel_group:
                cmd = self.cli_command[0].format(channel_group=channel_group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # Channel group 1 neighbors
        p1 = re.compile(r'^Channel +group +(?P<channel_group>[\d]+) +neighbors$')
        #           Partner              Partner          Partner         Partner Group
        # Port      Name                 Device ID        Port       Age  Flags   Cap.
        # Gi0/1     iosvl2-2             5e02.4001.8000   Gi0/1       11s SC      10001
        # Gi1/0/15    R5                   6c41.6ae4.7880   Gi1/0/1      5s  SC       A0001
        p2 = re.compile(r'^(?P<interface>[\w\/\.\-]+) +(?P<partner_name>[\w\-\.]+)'
                        ' +(?P<partner_id>[\w\.]+) *(?P<partner_port>[\w\/\.\-]+) +(?P<age>[\d]+)s +(?P<flags>[\w]+)'
                        ' *(?P<group_cap>[\w]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()                
                line = line.replace("\t",'    ')
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'pagp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                flags = group.pop('flags')
                activity = 'auto' if 'a'in flags.lower() else None
                if activity:
                    member_dict.update({'activity': activity})
                member_dict.update({'flags': flags})
                member_dict.update({'partner_name': group.pop('partner_name')})
                member_dict.update({'partner_id': group.pop('partner_id')})
                member_dict.update({'partner_port': Common.convert_intf_name(group.pop('partner_port'))})
                member_dict.update({'group_cap': group.pop('group_cap')})
                member_dict.update({'age': int(group.pop('age'))})
                continue

        return result_dict

# ====================================================
#  schema for show pagp internal
# ====================================================
class ShowPagpInternalSchema(MetaParser):
    """Schema for:
        show pagp internal"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'group_ifindex': int,
                        'partner_count': int,
                        'hello_interval': int,
                        Optional('timers'): str,
                        'pagp_port_priority': int,
                        'flags': str,
                        'state': str,
                        'learn_method': str,
                    },
                }
            },
        },
    }

# ====================================================
#  parser for show pagp internal
# ====================================================
class ShowPagpInternal(ShowPagpInternalSchema):
    """Parser for :
      show pagp internal
      show pagp <channel_group> internal"""

    cli_command = ['show pagp {channel_group} internal', 'show pagp internal']

    def cli(self, channel_group="", output=None):
        if output is None:
            if channel_group:
                cmd = self.cli_command[0].format(channel_group=channel_group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # Channel group 1
        #                        Hello    Partner  PAgP     Learning  Group
        # Port      Flags State   Timers  Interval Count   Priority   Method  Ifindex
        # Gi0/1     SC    U6/S7   H       30s      1        128        Any      8

        #                                   Hello    Partner  PAgP       Learning  Group
        # Port        Flags State   Timers  Interval Count    Priority   Method    Ifindex
        # Gi1/0/7     d     U1/S1           1s       0        128        Any       0
        # Gi1/0/8     d     U1/S1           1s       0        128        Any       0
        # Gi1/0/9     d     U1/S1           1s       0        128        Any       0

        p1 = re.compile(r'^\s*Channel +group +(?P<channel_group>[\d]+)$')
        p2 = re.compile(r'^\s*(?P<interface>[\w\/]+) +(?P<flags>[\w\s]+)'
                        ' +(?P<state>[\w\/]+)( +(?P<timers>[\w]+))? +(?P<hello_interval>[\d]+)[\w]'
                        ' +(?P<partner_count>[\d]+) +(?P<pagp_port_priority>[\d]+)'
                        ' +(?P<learn_method>[\w]+) +(?P<group_ifindex>[\d]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
                line = line.replace("\t",'    ')
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group.pop("channel_group")
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'pagp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop("interface"))
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                member_dict.update({'flags': group.pop('flags').strip()})
                member_dict.update({'state': group.pop('state')})
                member_dict.update({'pagp_port_priority': int(group.pop('pagp_port_priority'))})
                if group['timers']:
                    member_dict.update({'timers': group.pop('timers')})
                member_dict.update({'hello_interval': int(group.pop('hello_interval'))})
                member_dict.update({'partner_count': int(group.pop('partner_count'))})
                member_dict.update({'group_ifindex': int(group.pop('group_ifindex'))})
                member_dict.update({'learn_method': group.pop('learn_method').lower()})
                continue

        return result_dict

# ====================================================
#  schema for show etherchannel summary
# ====================================================
class ShowEtherchannelSummarySchema(MetaParser):
    """Schema for:
        show etherchannel summary"""

    schema = {
        Optional('number_of_lag_in_use'): int,
        Optional('number_of_aggregators'): int,
        Optional('interfaces'): {
            Any(): {
                Optional('name'): str,
                Optional('bundle_id'): int,
                Optional('protocol'): str,
                Optional('flags'): str,
                Optional('oper_status'): str,
                Optional('activity'): str,
                Optional('members'): {
                    Any(): {
                        Optional('interface'): str,
                        Optional('flags'): str,
                        Optional('bundled'): bool,                        
                        'port_channel': {
                            'port_channel_member': bool,
                            Optional('port_channel_int'): str,
                        },
                    }
                },
                Optional('port_channel'): {
                    'port_channel_member': bool,
                    Optional('port_channel_member_intfs'): list,
                },
            },
        }
    }

# ====================================================
#  parser for show etherchannel summary
# ====================================================
class ShowEtherchannelSummary(ShowEtherchannelSummarySchema):
    """Parser for :
      show etherchannel summary"""

    cli_command = 'show etherchannel summary'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        intf_dict = {}
        m1 = ""
        # Number of channel-groups in use: 2
        # Number of aggregators:           2
        #
        # Group  Port-channel  Protocol    Ports
        # ------+-------------+-----------+-----------------------------------------------
        # 1      Po1(SU)         PAgP      Gi0/1(P)    Gi0/2(P)

        # Group  Port-channel  Protocol    Ports
        # ------+-------------+-----------+-----------------------------------------------
        # 10     Po10(SU)        PAgP        Gi1/0/15(P)     Gi1/0/16(P)     
        #                                    Gi1/0/17(P)     
        p1 = re.compile(r'^\s*Number +of +channel-groups +in +use: +(?P<number_of_lag_in_use>[\d]+)$')
        p2 = re.compile(r'^\s*Number +of +aggregators: +(?P<number_of_aggregators>[\d]+)$')
        p3 = re.compile(r'^\s*(?P<bundle_id>[\d\s]+)(?P<name>[\w\-]+)\((?P<flags>[\w]+)\)?'
                        '( +(?P<protocol>[\w\-]+))?( +((?P<ports>[\w\-\s\/\(\)]+)))?$')
        p4 = re.compile(r'^\s*(?P<bundle_id>[\d\t]+)(?P<name>[\w\-\t]+)\((?P<flags>[\w]+)\)'
                        '(?P<protocol>[\w\-\t]+)?((?P<ports>[\w\-\s\/\(\)]+))?$')
        # Group  Port-channel  Protocol    Ports
        # ------+-------------+-----------+-----------------------------------------------
        # 10     Po10(SU)        PAgP        Gi1/0/15(P)     Gi1/0/16(P)     
        #                                    Gi1/0/17(P)     
        p5 = re.compile(r'^\s*(?P<ports>[\w\-\/\(\)]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
                line = line.replace('\t', '  ')
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'number_of_lag_in_use': int(group.pop('number_of_lag_in_use'))})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'number_of_aggregators': int(group.pop('number_of_aggregators'))})
                continue

            if p3.match(line):
                m1 = p3.match(line)
            if p4.match(line):
                m1 = p4.match(line)
            if m1:
                protocol = None
                group = m1.groupdict()
                name = Common.convert_intf_name(group.pop("name"))
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})

                intf_dict.update({'name': name})
                intf_dict.update({'bundle_id': int(group.pop("bundle_id"))})
                if group.get("protocol"):
                    if '-' in group.get("protocol"):
                        protocol = None
                    else:
                        protocol = group.pop("protocol").strip().lower()
                if protocol:
                    intf_dict.update({'protocol': protocol})

                flags = group.pop("flags")
                intf_dict.update({'flags': flags})
                activity = 'auto' if 'a' in flags.lower() else None
                if activity:
                    intf_dict.update({'activity': activity})
                oper_status = 'up' if flags in ['RU', 'SU'] else 'down'
                intf_dict.update({'oper_status': oper_status})

                if group.get('ports'):
                    ports = group.pop('ports').split()

                    # port_channel
                    eth_list = []

                    port_dict = intf_dict.setdefault('members', {})
                    for port in ports:
                        port_value = port.split('(')
                        interface = Common.convert_intf_name(port_value[0])
                        state = port_value[1].replace(')','')
                        eth_list.append(interface)

                        port_item = port_dict.setdefault(interface, {})
                        port_item.update({'interface': interface})
                        port_item.update({'flags': state})
                        port_item.update({'bundled': True if state in ['bndl','P'] else False})

                        # port_channel
                        port_item.setdefault('port_channel', {}).update({'port_channel_member': True,
                                                                         'port_channel_int': name})

                    # port_channel
                    if eth_list:
                        port_dict = intf_dict.setdefault('port_channel', {})
                        port_dict['port_channel_member'] = True
                        port_dict['port_channel_member_intfs'] = sorted(eth_list)
                m1 = ""
                continue

            m = p5.match(line)
            if m and intf_dict:
                group = m.groupdict()
                ports = group.pop('ports').split()

                for port in ports:
                    port_value = port.split('(')
                    interface = Common.convert_intf_name(port_value[0])
                    state = port_value[1].replace(')','')
                    eth_list.append(interface)
                    port_item = intf_dict['members'].setdefault(interface, {})

                    port_item.update({'interface': interface})
                    port_item.update({'flags': state})
                    port_item.update({'bundled': True if state in ['bndl','P'] else False})

                    # port_channel
                    port_item.setdefault('port_channel', {}).update({'port_channel_member': True,
                                                                     'port_channel_int': name})

                # port_channel
                if eth_list:
                    intf_dict['port_channel']['port_channel_member_intfs'] = sorted(eth_list)
                continue

        return result_dict


# ====================================================
#  schema for show etherchannel load-balancing
# ====================================================
class ShowEtherChannelLoadBalancingSchema(MetaParser):
    """Schema for:
        show etherchannel load-balancing"""

    schema = {
        'global_lb_method': str,
        Optional('lb_algo_type'): str,
        'port_channel': {
            Any(): {
                'lb_method': str,
            },
        },
    }


# ====================================================
#  parser for show etherchannel load-balancing
# ====================================================
class ShowEtherChannelLoadBalancing(ShowEtherChannelLoadBalancingSchema):
    """Parser for :
      show etherchannel load-balancing"""

    cli_command = 'show etherchannel load-balancing'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initialize result dict
        result_dict = {}
        
        # Global LB Method: flow-based
        # LB Algo type: Source Destination IP
        #   Port-Channel:                       LB Method
        #     Port-channel1                   :  flow-based (Source Destination IP)
        p1 = re.compile(r'^\s*Global +LB +Method: *(?P<global_lb_method>[\w-]*)$')
        p2 = re.compile(r'^\s*LB +Algo +type: *(?P<lb_algo_type>[\w\s]*)$')
        p3 = re.compile(r'^\s*(?P<port_channel>[\w-]+) +: *(?P<lb_method>.+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                global_lb_method = m.groupdict()['global_lb_method']
                result_dict.update({'global_lb_method': global_lb_method})
                continue

            m = p2.match(line)
            if m:
                lb_algo_type = m.groupdict()['lb_algo_type']
                result_dict.update({'lb_algo_type': lb_algo_type})
                continue

            m = p3.match(line)
            if m:
                port_channel = m.groupdict()['port_channel']
                lb_method = m.groupdict()['lb_method']
                port_dict = result_dict.setdefault('port_channel', {}).setdefault(port_channel, {})
                port_dict.update({'lb_method': lb_method})
                continue

        return result_dict


# ====================================================
#  schema for show lacp neighbor detail
# ====================================================
class ShowLacpNeighborDetailSchema(MetaParser):
    """Schema for:
        show lacp neighbor detail"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'protocol': str,
                'members': {
                    Any(): {
                        'interface': str,
                        'system_id': str,
                        'port_num': int,
                        'age': int,
                        'flags': str,
                        'lacp_port_priority': int,
                        'oper_key': int,
                        'port_state': int,
                        Optional('activity'): str,
                        'timeout': str,
                        'aggregatable': bool,
                        'synchronization': bool,
                        'collecting': bool,
                        'distributing': bool,
                        'defaulted': bool,
                        'expired': bool,
                    },
                }
            },
        },
    }


# ====================================================
#  parser for show lacp neighbor detail
# ====================================================
class ShowLacpNeighborDetail(ShowLacpNeighborDetailSchema):
    """Parser for :
        show lacp neighbor detail"""

    cli_command = 'show lacp neighbor detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initialize result dict
        result_dict = {}
        
        # Channel group 1 neighbors
        p1 = re.compile(r'^\s*Channel +group +(?P<channel_group>[\d]+)')

        # Port           System ID             Port Number     Age         Flags
        # Gi0/0/1         00127,6487.88af.b840  0x2              28s        FA
        p2 = re.compile(r'^\s*(?P<interface>[\w/]+) +(?P<system_id>[\w,.]+) +(?P<port_num>[\w]+)'
                        ' +(?P<age>[\d]+)s +(?P<flags>[\w]+)$')

        # Port Priority        Oper Key        Port State
        # 100                  0x1             0x3F
        p3 = re.compile(r'^\s*(?P<lacp_port_priority>[\d.]+) +(?P<oper_key>[\w]+) +(?P<port_state>[\w]+)$')

        # Activity:   Timeout:   Aggregation:   Synchronization:
        # Active      Short      Yes            Yes
        p4 = re.compile(r'^\s*(?P<activity>[\w]+) +(?P<timeout>Long|Short)'
                        ' +(?P<aggregatable>[\w]+) +(?P<synchronization>[\w]+)$')

        # Collecting:   Distributing:   Defaulted:   Expired:
        # Yes           Yes             No           No 
        p5 = re.compile(r'^\s*(?P<collecting>Yes|No) +(?P<distributing>[\w]+) +(?P<defaulted>[\w]+) +(?P<expired>[\w]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = 'Port-channel' + group["channel_group"]
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                intf_dict.update({'name': name})
                intf_dict.update({'protocol': 'lacp'})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"])
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface, {})
                member_dict.update({'interface': interface})
                member_dict.update({'system_id': group['system_id']})
                member_dict.update({'port_num': int(group['port_num'], 0)})
                member_dict.update({'age': int(group['age'])})
                member_dict.update({'flags': group['flags']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                member_dict.update({'lacp_port_priority': int(group['lacp_port_priority'])})
                member_dict.update({'oper_key': int(group['oper_key'], 0)})
                member_dict.update({'port_state': int(group['port_state'], 0)})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                member_dict.update({'activity': group['activity']})
                member_dict.update({'timeout': group['timeout']})
                member_dict.update({'aggregatable': group['aggregatable'] == 'Yes'})
                member_dict.update({'synchronization': group['synchronization'] == 'Yes'})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                member_dict.update({'collecting': group['collecting'] == 'Yes'})
                member_dict.update({'distributing': group['distributing'] == 'Yes'})
                member_dict.update({'defaulted': group['defaulted'] == 'Yes'})
                member_dict.update({'expired': group['expired'] == 'Yes'})
                continue

        return result_dict
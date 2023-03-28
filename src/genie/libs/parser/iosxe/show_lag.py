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
     *  show etherchannel <port_channel> summary
     *  show etherchannel load-balancing
     *  show lacp neighbor detail
     *  show etherchannel <channel_group> detail
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
        # 32768, 001e.49ff.3caf
        # 32768,0014.a9ff.873d
        # 8000,AC-12-34-FF-CE-E6
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
    exclude = ['lacp_in_pkts' , 'lacp_out_pkts']
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
    exclude = ['age']

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
        # Gi2       SA      32768     001e.49ff.a3e6  25s    0x0    0x1    0x1     0x3D
        # Gi5/0/0   SP      32768     0011.20ff.9926  11s    0x1    0x14   0x3C
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
    cli_command = ['show pagp {channel_group} counters', 'show pagp counters']

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
        # Gi0/1     iosvl2-2             5e02.40ff.8101   Gi0/1       11s SC      10001
        # Gi1/0/15    R5                   6c41.6aff.5d65   Gi1/0/1      5s  SC       A0001
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
      show etherchannel summary
      show etherchannel <port-channel> summary      
      """

    cli_command = [
                  'show etherchannel summary',
                  'show etherchannel {port_channel} summary',
                ]
    exclude = ['current_time', 'last_read', 'last_write',
        'retrans', 'keepalives', 'total', 'value', 'retransmit', 
        'total_data', 'with_data', 'krtt', 'receive_idletime', 
        'sent_idletime', 'sndnxt', 'snduna', 'sndwnd', 'uptime',
        'ackhold', 'delrcvwnd', 'rcvnxt', 'receive_idletime', 
        'rcvwnd', 'updates', 'down_time', 'last_reset', 
        'notifications', 'opens', 'route_refresh', 'total',
        'updates', 'up_time', 'rtto', 'rtv', 'srtt', 'pmtuager',
        'min_rtt', 'max_rtt', 'dropped', 'established', 
        'reset_reason', 'irs', 'iss', 'tcp_semaphore', 
        'foreign_port', 'status_flags', 'local_port', 
        'keepalive', 'out_of_order']


    def cli(self,port_channel="",output=None):
        if output is None:
            if not port_channel:
                out = self.device.execute(self.cli_command[0])
            else:
                out = self.device.execute(self.cli_command[1].format(port_channel=port_channel))            
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
        #                                  Te2/0/3(s)      Te3/0/1(s)
        #                                  Te3/0/2(D)      Te3/0/3(P)
        p6 = re.compile(r'^\s*(?P<port1>[\w\-\/\(\)]+)\s+(?P<port2>[\w\-\/\(\)]+)$')

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


            m = p6.match(line)
            if m and intf_dict:
                group = m.groupdict()
                ports = [group.pop('port1'), group.pop('port2')]

                for port in ports:
                    port_value = port.split('(')
                    interface = Common.convert_intf_name(port_value[0])
                    state = port_value[1].replace(')', '')
                    eth_list.append(interface)
                    port_item = intf_dict['members'].setdefault(interface, {})

                    port_item.update({'interface': interface})
                    port_item.update({'flags': state})
                    port_item.update({'bundled': True if state in ['bndl', 'P'] else False})

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
        Optional('port_channel'): {
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
                        'collecting': bool,
                        'distributing': bool,
                        'defaulted': bool,
                        'expired': bool,
                        Optional('activity'): str,
                        Optional('timeout'): str,
                        Optional('aggregatable'): bool,
                        Optional('synchronization'): bool,
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
        # Gi0/0/1         00127,6487.88ff.68ef  0x2              28s        FA
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


class ShowEtherChannelDetailSchema(MetaParser):
    '''Schema for show etherchannel {channel_group} detail'''
    schema = {
        'group_state': str,
        'ports': int,
        'max_ports': int,
        'port_channels': int,
        'max_port_channels': int,
        'protocol': str,
        'minimum_links': int,
        Optional('port'): {
            Any(): {
                'port_state': str,
                'channel_group': int,
                'gcchange': str,
                'mode': str,
                'port_channel': str,
                'gc': str,
                'pseudo_port_channel': str, 
                'port_index': int,
                'load': str,
                'protocol': str,
                'age': str,
                'local_information': {
                    'port': {
                        Any(): {
                            'flags': str,
                            'state': str,
                            'lacp_priority': int,
                            'admin_key': str,
                            'oper_key': str,
                            'port_number': str,
                            'port_state': str
                        }
                    }
                },
                'partner_information': {
                    'port': {
                        Any(): {
                            'flags': str,
                            'dev_id': str,
                            'age': str,
                            'lacp_priority': int,
                            'admin_key': str,
                            'oper_key': str,
                            'port_number': str,
                            'port_state': str
                        }
                    }
                }            
            }
        },
        Optional('port_channel'): {
            Any(): {
                'age': str,
                'logical_slot': str,
                'number_of_ports': int,
                'hot_standby': str,
                'state': str,
                'protocol': str,
                'port_security': str,
                'fast_switchover': str,
                'dampening': str,
                Optional('last_port_bundled'): {
                    'time': str,
                    'port': str
                },
                Optional('last_port_unbundled'): {
                    'time': str,
                    'port': str
                },             
                'port': {
                    Any(): {
                        'index': int,
                        'load': str,
                        'ec_state': str,
                        'no_of_bits': int
                    }
                } 
            }
        }
    }


class ShowEtherChannelDetail(ShowEtherChannelDetailSchema):
    '''Parser for show etherchannel {channel_group} detail'''

    cli_command = 'show etherchannel {channel_group} detail'

    def cli(self, channel_group="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(channel_group=channel_group))
        
        # Group state = L2
        p1 = re.compile(r'^Group state = (?P<group_state>\w+)$')

        # Ports: 2   Maxports = 16
        p2 = re.compile(r'^Ports:\s+(?P<ports>\d+)\s+Maxports =\s+(?P<max_ports>\d+)$')

        # Port-channels: 1 Max Port-channels = 16
        p3 = re.compile(r'^Port-channels:\s(?P<port_channels>\d+)\s+Max Port-channels =\s(?P<max_port_channels>\d+)$')

        # Protocol:   LACP
        p4 = re.compile(r'^Protocol:\s+(?P<protocol>\w+)$')

        # Minimum Links: 0
        p5 = re.compile(r'^Minimum Links:\s+(?P<minimum_links>\d+)$')

        # Port: Twe1/0/13
        p6 = re.compile(r'^Port:\s+(?P<port>[\w/\.]+)$')

        # Port state    = Up Mstr Assoc In-Bndl 
        p7 = re.compile(r'^Port state    =\s+(?P<port_state>.+)$')

        # Channel group = 1           Mode = Active          Gcchange = -
        p8 = re.compile(r'^Channel\sgroup\s=\s+(?P<channel_group>\d+)\s+Mode\s=\s(?P<mode>\w+)\s+Gcchange\s=\s(?P<gcchange>\S+)$')

        # Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
        p9 = re.compile(r'^Port-channel\s+=\s(?P<port_channel>\w+)\s+GC\s+=\s+(?P<gc>\S+)\s+Pseudo\sport-channel\s=\s(?P<pseudo_port_channel>\w+)$')

        # Port index    = 0           Load = 0x00            Protocol =   LACP
        p10 = re.compile(r'^Port\sindex\s+=\s(?P<port_index>\d+)\s+Load\s=\s(?P<load>\w+)\s+Protocol\s=\s+(?P<protocol>\S+)$')

        # Age of the port in the current state: 0d:00h:03m:14s
        p11 = re.compile(r'^Age of the port in the current state:\s(?P<age>\S+)$')

        # Twe1/0/13     SA      bndl      200          0x1       0x1     0x10E       0x3D
        p12 = re.compile(r'^(?P<port>[\w/\.]+)\s+(?P<flags>\w+)\s+(?P<state>\S+)\s+(?P<lacp_priority>\d+)\s+(?P<admin_key>\w+)\s+(?P<oper_key>\w+)\s+(?P<port_number>\w+)\s+(?P<port_state>\w+)$')

        # Twe1/0/13     SA     32768     6cb2.ae4a.54c0   6s  0x0    0x1    0x804   0x3D 
        p13 = re.compile(r'^(?P<port>[\w/\.]+)\s+(?P<flags>\w+)\s+(?P<lacp_priority>\d+)\s+(?P<dev_id>[a-f0-9\.]+)\s+(?P<age>\w+)\s+(?P<admin_key>\w+)\s+(?P<oper_key>\w+)\s+(?P<port_number>\w+)\s+(?P<port_state>\w+)$')

        # Port-channel: Po1    (Primary Aggregator)
        p14 = re.compile(r'^Port\-channel:\s(?P<port_channel>\S+).+$')

        # Age of the Port-channel   = 0d:00h:10m:38s
        p15 = re.compile(r'^Age of the Port\-channel\s+=\s(?P<age>\S+)$')

        # Logical slot/port   = 9/1          Number of ports = 1
        p16 = re.compile(r'^Logical slot/port\s+=\s(?P<logical_slot>\S+)\s+Number of ports =\s(?P<number_of_ports>\d+)$')

        # HotStandBy port = Twe1/0/15 
        p17 = re.compile(r'^HotStandBy port =\s(?P<hot_standby>[\w/\.]+)$')

        # Port state          = Port-channel Ag-Inuse 
        p18 = re.compile(r'^Port state          =\s(?P<state>.+)$')

        # Protocol            =   LACP
        p19 = re.compile(r'^Protocol\s+=\s+(?P<protocol>\S+)$')

        # Port security       = Disabled
        p20 = re.compile(r'^Port security\s+=\s(?P<port_security>\S+)$')

        # Fast-switchover     = disabled
        p21 = re.compile(r'^Fast\-switchover\s+=\s(?P<fast_switchover>\S+)$')

        # Fast-switchover Dampening = disabled
        p22 = re.compile(r'^Fast\-switchover Dampening =\s(?P<dampening>\S+)$')

        # Time since last port bundled:    0d:00h:03m:14s     Twe1/0/13
        p23 = re.compile(r'^Time since last port bundled:\s+(?P<time>\S+)\s+(?P<port>\S+)$')

        # Time since last port Un-bundled: 0d:00h:03m:16s     Twe1/0/15
        p24 = re.compile(r'^Time since last port Un\-bundled:\s+(?P<time>\S+)\s+(?P<port>\S+)$')

        #   0     00     Twe1/0/13      Active             0
        p25 = re.compile(r'^(?P<index>\d+)\s+(?P<load>\w+)\s+(?P<port>[\w/\.]+)\s+(?P<ec_state>\S+)\s+(?P<no_of_bits>\d+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # Group state = L2
            m = p1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Ports: 2   Maxports = 16
            m = p2.match(line)
            if m:
                ret_dict.setdefault('ports', int(m.groupdict()['ports']))
                ret_dict.setdefault('max_ports', int(m.groupdict()['max_ports']))
                continue
            
            # Port-channels: 1 Max Port-channels = 16
            m = p3.match(line)
            if m:
                ret_dict.setdefault('port_channels', int(m.groupdict()['port_channels']))
                ret_dict.setdefault('max_port_channels', int(m.groupdict()['max_port_channels']))
                continue
            
            # Protocol:   LACP
            m = p4.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue
            
            # Minimum Links: 0
            m = p5.match(line)
            if m:
                ret_dict.setdefault('minimum_links', int(m.groupdict()['minimum_links']))
                continue
            
            # Port: Twe1/0/13
            m = p6.match(line)
            if m:
                port_dict = ret_dict.setdefault('port', {}).setdefault(Common.convert_intf_name(m.groupdict()['port']), {})
                continue
            
            # Port state    = Up Mstr Assoc In-Bndl 
            m = p7.match(line)
            if m:
                port_dict.update(m.groupdict())
                continue
            
            # Channel group = 1           Mode = Active
            m = p8.match(line)
            if m:
                port_dict.setdefault('channel_group', int(m.groupdict()['channel_group']))
                port_dict.setdefault('mode', m.groupdict()['mode'])
                port_dict.setdefault('gcchange', m.groupdict()['gcchange'])
                continue
            
            # Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
            m = p9.match(line)
            if m:
                port_dict.update(m.groupdict())
                continue
            
            # Port index    = 0           Load = 0x00            Protocol =   LACP
            m = p10.match(line)
            if m:
                port_dict.setdefault('port_index', int(m.groupdict()['port_index']))
                port_dict.setdefault('load', m.groupdict()['load'])
                port_dict.setdefault('protocol', m.groupdict()['protocol'])
                continue
            
            # Age of the port in the current state: 0d:00h:03m:14s
            m = p11.match(line)
            if m:
                port_dict.update(m.groupdict())
                continue
            
            # Twe1/0/13     SA      bndl      200          0x1       0x1     0x10E       0x3D
            m = p12.match(line)
            if m:
                output = m.groupdict()
                local_dict = port_dict.setdefault('local_information', {}).setdefault('port', {}).setdefault(Common.convert_intf_name(output['port']), {})
                local_dict.setdefault('flags', output['flags'])
                local_dict.setdefault('state', output['state'])
                local_dict.setdefault('lacp_priority', int(output['lacp_priority']))
                local_dict.setdefault('admin_key', output['admin_key'])
                local_dict.setdefault('oper_key', output['oper_key'])
                local_dict.setdefault('port_number', output['port_number'])
                local_dict.setdefault('port_state', output['port_state'])
                continue
            
            # Twe1/0/13     SA     32768     6cb2.ae4a.54c0   6s  0x0    0x1    0x804   0x3D 
            m = p13.match(line)
            if m:
                output = m.groupdict()
                par_dict = port_dict.setdefault('partner_information', {}).setdefault('port', {}).setdefault(Common.convert_intf_name(output['port']), {})
                par_dict.setdefault('flags', output['flags'])
                par_dict.setdefault('dev_id', output['dev_id'])
                par_dict.setdefault('lacp_priority', int(output['lacp_priority']))
                par_dict.setdefault('age', output['age'])
                par_dict.setdefault('admin_key', output['admin_key'])
                par_dict.setdefault('oper_key', output['oper_key'])
                par_dict.setdefault('port_number', output['port_number'])
                par_dict.setdefault('port_state', output['port_state'])
                continue
            
            # Port-channel: Po1
            m = p14.match(line)
            if m:
                channel_dict = ret_dict.setdefault('port_channel', {}).setdefault(m.groupdict()['port_channel'], {})
                continue
            
            # Age of the Port-channel   = 0d:00h:10m:38s
            m = p15.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue
                        
            # Logical slot/port   = 9/1          Number of ports = 1
            m = p16.match(line)
            if m:
                channel_dict.setdefault('logical_slot', m.groupdict()['logical_slot'])
                channel_dict.setdefault('number_of_ports', int(m.groupdict()['number_of_ports']))
                continue
               
            # HotStandBy port = Twe1/0/15 
            m = p17.match(line)
            if m:
                channel_dict.setdefault('hot_standby', Common.convert_intf_name(m.groupdict()['hot_standby']))
                continue
                        
            # Port state          = Port-channel Ag-Inuse 
            m = p18.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue

            # Protocol            =   LACP
            m = p19.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue

            # Port security       = Disabled
            m = p20.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue

            # Fast-switchover     = disabled
            m = p21.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue

            # Fast-switchover Dampening = disabled
            m = p22.match(line)
            if m:
                channel_dict.update(m.groupdict())
                continue
            
            # Time since last port bundled:    0d:00h:03m:14s     Twe1/0/13
            m = p23.match(line)
            if m:
                last_dct = channel_dict.setdefault('last_port_bundled', {})
                last_dct.setdefault('time', m.groupdict()['time'])
                last_dct.setdefault('port', Common.convert_intf_name(m.groupdict()['port']))
                continue
                       
            # Time since last port Un-bundled: 0d:00h:03m:16s     Twe1/0/15
            m = p24.match(line)
            if m:
                unbld_dict = channel_dict.setdefault('last_port_unbundled', {})
                unbld_dict.setdefault('time', m.groupdict()['time'])
                unbld_dict.setdefault('port', Common.convert_intf_name(m.groupdict()['port']))
                continue
                       
            #   0     00     Twe1/0/13      Active             0
            m = p25.match(line)
            if m:
                output = m.groupdict()
                port_dict = channel_dict.setdefault('port', {}).setdefault(Common.convert_intf_name(output['port']), {})
                port_dict.setdefault('index', int(output['index']))
                port_dict.setdefault('ec_state', output['ec_state'])
                port_dict.setdefault('load', output['load'])
                port_dict.setdefault('no_of_bits', int(output['no_of_bits']))
                continue
        
        return ret_dict



class ShowEtherchannelPortChannelSchema(MetaParser):

    """Schema for show etherchannel port-channel"""

    schema = {
        'port_channel': {
            Any(): {
                'age': str,
                'logical_slot': str,
                'number_of_ports': int,
                Optional('gc'): str,
                'protocol': str,
                'port_security': str,
                'switchover': str,
                'dampening': str,
                'ports': {
                    Any(): {
                        'ec_state': str,
                        'bits': int,
                        'load': str,
                        'index': int
                    }
                }
            }
        }
    }


class ShowEtherchannelPortChannel(ShowEtherchannelPortChannelSchema):

    """Parser for show etherchannel port-channel"""

    cli_command = 'show etherchannel {number} port-channel'

    def cli(self, number='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(number=number))

        # Port-channel: Po1
        p1 = re.compile(r"^Port-channel:\s+(?P<port_channel>\S+).*$")

        # Age of the Port-channel   = 0d:00h:01m:16s
        p2 = re.compile(r"^Age of the Port-channel\s+=\s+(?P<age>\S+)$")

        # Logical slot/port   = 35/1          Number of ports = 2
        p3 = re.compile(r"^Logical slot/port\s+=\s+(?P<logical_slot>\S+)\s+Number\s+of\s+ports\s+=\s+("
                          r"?P<number_of_ports>\d+)$")

        # GC                  = 0x00010001      HotStandBy port = null
        p4 = re.compile(r"^GC\s+=\s+(?P<gc>\S+)\s+HotStandBy\s+port\s+=\s+null$")

        # Protocol            =   PAgP
        p5 = re.compile(r"^Protocol\s+=\s+(?P<protocol>\w+)$")

        # Port security       = Disabled
        p6 = re.compile(r"^Port security\s+=\s+(?P<port_security>\w+)$")

        # Fast-switchover     = disabled
        p7 = re.compile(r"^Fast-switchover\s+=\s+(?P<switchover>\w+)$"
                          )

        # Fast-switchover Dampening = disabled
        p8 = re.compile(r"^Fast-switchover Dampening\s+=\s+(?P<dampening>\w+)$")

        #   0     00     Tw1/0/14       Desirable-Sl       0
        p9 = re.compile(r"^(?P<index>\d+)\s+(?P<load>\d+)\s+(?P<port>\S+)\s+(?P<ec_state>\S+)\s+(?P<bits>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Port-channel: Po1
            match = p1.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_var = dict_val['port_channel']
                port_channel_dict = ret_dict.setdefault('port_channel', {}).setdefault(port_channel_var, {})
                continue

            # Age of the Port-channel   = 0d:00h:01m:16s
            match = p2.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['age'] = dict_val['age']
                continue

            # Logical slot/port   = 35/1          Number of ports = 2
            match = p3.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['logical_slot'] = dict_val['logical_slot']
                port_channel_dict['number_of_ports'] = int(dict_val['number_of_ports'])
                continue

            # GC                  = 0x00010001      HotStandBy port = null
            match = p4.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['gc'] = dict_val['gc']
                continue

            # Protocol            =   PAgP
            match = p5.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['protocol'] = dict_val['protocol']
                continue

            # Port security       = Disabled
            match = p6.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['port_security'] = dict_val['port_security']
                continue

            # Fast-switchover     = disabled
            match = p7.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['switchover'] = dict_val['switchover']
                continue

            # Fast-switchover Dampening = disabled
            match = p8.match(line)
            if match:
                dict_val = match.groupdict()
                port_channel_dict['dampening'] = dict_val['dampening']
                continue

            #   0     00     Tw1/0/14       Desirable-Sl       0
            match = p9.match(line)
            if match:
                dict_val = match.groupdict()
                ports_dict = port_channel_dict.setdefault('ports', {}).setdefault(dict_val['port'], {})
                ports_dict['ec_state'] = dict_val['ec_state']
                ports_dict['bits'] = int(dict_val['bits'])
                ports_dict['load'] = dict_val['load']
                ports_dict['index'] = int(dict_val['index'])
                continue

        return ret_dict


class ShowEtherchannelProtocolSchema(MetaParser):

    """Schema for show etherchannel protocol"""

    schema = {
        'group': {
            Any(): {
                'protocol': str
            }
        }
    }


class ShowEtherchannelProtocol(ShowEtherchannelProtocolSchema):

    """Parser for show etherchannel protocol"""

    cli_command = 'show etherchannel protocol'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Group: 1
        p1 = re.compile(r"^Group:\s+(?P<group>\d+)$")

        # Protocol:   -  (Mode ON)
        p1_1 = re.compile(r"^Protocol:\s+-\s+\(?(?P<protocol>[\w\s]+)\)?$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Group: 1
            match = p1.match(line)
            if match:
                dict_val = match.groupdict()
                group_var = dict_val['group']
                group_dict = ret_dict.setdefault('group', {}).setdefault(group_var, {})
                continue

            # Protocol:   -  (Mode ON)
            match = p1_1.match(line)
            if match:
                dict_val = match.groupdict()
                group_dict['protocol'] = dict_val['protocol']
                continue

        return ret_dict

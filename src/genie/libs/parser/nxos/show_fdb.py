""" show_fdb.py
    supported commands:
        * show mac address-table vni <WORD> | grep <WORD>
        * show mac address-table local vni <WORD>
        * show mac address-table
        * show mac address-table aging-time
        * show mac address-table limit
        * show system internal l2fwder mac
        * show mac address-table vlan {vlan}
        * show mac address-table interface {interface}
        * show mac address-table interface {interface} vlan {vlan}
        * show mac address-table address {address}
        * show mac address-table address {address} vlan {vlan}
        * show mac address-table address {address} interface {interface}
        * show mac address-table address {address} interface {interface} vlan {vlan}

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
from genie.libs.parser.utils.common import Common

class ShowMacAddressTableBaseSchema(MetaParser):
    """Schema for:
        'show mac address-table vni <WORD> | grep <WORD>'
        'show mac address-table local vni <WORD>'
        'show mac address-table'
    """

    schema = {
            'mac_table': {
                'vlans': {
                    Any(): {
                        'vlan': str,
                        'mac_addresses': {
                            Any():{
                                'mac_address': str,
                                Optional('entry'): str,
                                'secure': str,
                                'ntfy': str,
                                Optional('drop'): {
                                    'drop': bool,
                                    'age': str,
                                    'mac_type': str,
                                },
                                Optional('interfaces'): {
                                    Any(): {
                                        'interface': str,
                                        'age': str,
                                        'mac_type': str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


class ShowMacAddressTableBase(ShowMacAddressTableBaseSchema):
    """Base parser for:
        'show mac address-table vni <WORD> | grep <WORD>'
        'show mac address-table local vni <WORD>'
        'show mac address-table'
    """

    def cli(self, out):

        # initial return dictionary
        ret_dict = {}

        # C 1001     0000.04ff.b1b1   dynamic  0     F      F nve1(10.9.0.101)
        # * 1001     0000.01ff.9191   dynamic  0     F      F    Eth1/11
        # G 2000     7e00.c0ff.0007    static       -       F    F  vPC Peer-Link(R)
        # 4000     5e00.c0ff.0007   static   ~~~         F      F    sup-eth1(R)
        # +  390     000f.53ff.1f1d   dynamic  0         F      F    Po125
        # 100 0000.0000.1112 dynamic NA F F Po100
        p1 = re.compile(r'^(?P<entry>[\w\*\+] )?\s*(?P<vlan>All|[\d\-]+) '
            '+(?P<mac_address>[0-9a-z\.\:]+) +(?P<mac_type>[a-z]+) '
            '+(?P<age>[0-9\-\~]+|NA) '
            '+(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
            '+(?P<drop>(drop|Drop))?'
            '(?P<ports>[a-zA-Z0-9\/\.\(\)\-\s]+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan = str(group['vlan'])
                vlan_dict = ret_dict.setdefault('mac_table', {})\
                .setdefault('vlans', {}).setdefault(vlan, {})
                vlan_dict.update({'vlan': str(vlan)})
                mac_address = str(group['mac_address'])
                mac_dict = vlan_dict.setdefault('mac_addresses', {})\
                .setdefault(mac_address,{})
                mac_dict.update({'mac_address': mac_address})
                if group['entry']:
                    mac_dict.update({'entry': str(group['entry']).strip()})
                if not str(group['drop']) == 'None':
                    intf_dict = mac_dict.setdefault('drop',{})
                    intf_dict.update({'drop': True})
                port = str(group['ports'])
                if not port == 'None':
                    converted_port = Common.convert_intf_name(group['ports'])
                    intf_dict = mac_dict.setdefault('interfaces',{})\
                    .setdefault(converted_port,{})
                    intf_dict.update({'interface': converted_port})
                mac_type = str(group['mac_type'])
                age = str(group['age'])
                secure = str(group['secure'])
                ntfy = str(group['ntfy'])
                intf_dict.update({'mac_type': str(group['mac_type'])})
                intf_dict.update({'age': str(group['age'])})                
                mac_dict.update({'secure': str(group['secure'])})
                mac_dict.update({'ntfy': str(group['ntfy'])})
                continue
                
        return ret_dict


class ShowMacAddressTableVni(ShowMacAddressTableBase, ShowMacAddressTableBaseSchema):
    """Parser for:
        'show mac address-table vni <WORD> | grep <WORD>'
        'show mac address-table local vni <WORD>'"""

    cli_command = ['show mac address-table vni {vni} | grep {interface}',
                   'show mac address-table local vni {vni}']


    def cli(self, vni, interface=None, output=None):

        cmd = ""
        if output is None:
            if vni and interface:
                cmd = self.cli_command[0].format(vni=vni, interface=interface)
            if vni and not interface:
                cmd = self.cli_command[1].format(vni=vni)
            out = self.device.execute(cmd)
        else:
            out = output
            
        # C 1001     0000.04ff.b1b1   dynamic  0         F      F    nve1(10.9.0.101)
        # * 1001     00f1.00ff.0000   dynamic  0         F      F    Eth1/11
        # get return dictionary
        ret_dict = super().cli(out)

        return ret_dict


class ShowMacAddressTable(ShowMacAddressTableBase, ShowMacAddressTableBaseSchema):
    """Parser for show mac address-table"""

    cli_command = [
        'show mac address-table',
        'show mac address-table vlan {vlan}',
        'show mac address-table interface {interface}',
        'show mac address-table interface {interface} vlan {vlan}',
        'show mac address-table address {address}',
        'show mac address-table address {address} vlan {vlan}',
        'show mac address-table address {address} interface {interface}',
        'show mac address-table address {address} interface {interface} vlan {vlan}'
    ]

    def cli(self, address=None, interface=None, vlan=None, output=None):

        if output is None:
            if address and interface and vlan:
                cmd = self.cli_command[7].format(address=address, interface=interface, vlan=vlan)
            elif address and interface:
                cmd = self.cli_command[6].format(address=address, interface=interface)
            elif address and vlan:
                cmd = self.cli_command[5].format(address=address, vlan=vlan)
            elif address:
                cmd = self.cli_command[4].format(address=address)
            elif interface and vlan:
                cmd = self.cli_command[3].format(interface=interface, vlan=vlan)
            elif interface:
                cmd = self.cli_command[2].format(interface=interface)
            elif vlan:
                cmd = self.cli_command[1].format(vlan=vlan)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # *   10     aaaa.bbff.8888   static   -         F      F    Eth1/2
        # *   20     aaaa.bbff.8888   static   -         F      F    Drop
        # G    -     0000.deff.6c9d   static   -         F      F    sup-eth1(R)
        # G    -     5e00.c0ff.0007   static   -         F      F     (R)

        # get return dictionary
        ret_dict = super().cli(out)

        return ret_dict


class ShowMacAddressTableAgingTimeSchema(MetaParser):
    """Schema for show mac address-table aging-time"""
    schema = {
        'mac_aging_time': int
    }


class ShowMacAddressTableAgingTime(ShowMacAddressTableAgingTimeSchema):
    """Parser for show mac address-table aging-time"""

    cli_command = 'show mac address-table aging-time'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^\s*(?P<mac_aging_time>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Aging Time
            # ----------
            #     10
            m = p1.match(line)
            if m:
                ret_dict['mac_aging_time'] = \
                int(m.groupdict()['mac_aging_time'])
                continue

        return ret_dict


class ShowMacAddressTableLimitSchema(MetaParser):
    """Schema for show mac address-table limit"""
    schema = {
        'configured_system_limit': int,
        'current_system_count': int,
        'configured_system_action': str,
        'currently_system_is': str,
        'mac_table': {
            'vlans': {
                Any(): {
                    'vlan': str,
                    'conf_limit': int,
                    'curr_count': int,
                    'cfg_action': str,
                    'currently': str
                }
            }
        }
    }


class ShowMacAddressTableLimit(ShowMacAddressTableLimitSchema):
    """Parser for show mac address-table limit"""

    cli_command = 'show mac address-table limit'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Configured System Limit: 111
        # Current System Count: 3
        # Configured System Action: Flood
        # Currently System is: Flooding Unknown SA
        p1 = re.compile(r'^Configured +System +Limit: '
        	'+(?P<configured_system_limit>\d+)$')
        p2 = re.compile(r'^Current +System +Count: '
        	'+(?P<current_system_count>\d+)$')
        p3 = re.compile(r'^Configured +System +Action: '
        	'+(?P<configured_system_action>\w+)$')
        p4 = re.compile(r'^Currently +System +is: '
        	'+(?P<currently_system_is>[\w\s]+)$')
        p5 = re.compile(r'^\s*(?P<vlan>\w+) +(?P<conf_limit>\d+) '
        	'+(?P<curr_count>\d+) +(?P<cfg_action>\w+) '
        	'+(?P<currently>[\w\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict['configured_system_limit'] = \
                int(m.groupdict()['configured_system_limit'])
                continue

            m = p2.match(line)
            if m:
                ret_dict['current_system_count'] = \
                int(m.groupdict()['current_system_count'])
                continue

            m = p3.match(line)
            if m:
                ret_dict['configured_system_action'] = \
                m.groupdict()['configured_system_action']
                continue

            m = p4.match(line)
            if m:
                ret_dict['currently_system_is'] = \
                m.groupdict()['currently_system_is']
                continue

            # Vlan  Conf Limit   Curr Count  Cfg Action Currently
            # ----  ------------ ---------   ---------  --------
            # 1     196000       0           Flood      Flooding Unknown SA
            # 10    196000       1           Flood      Flooding Unknown SA
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vlan = str(group['vlan'])
                vlan_dict = ret_dict.setdefault('mac_table', {})\
                .setdefault('vlans', {}).setdefault(str(vlan), {})
                vlan_dict.update({'vlan': vlan})
                vlan_dict.update({'conf_limit': int(group['conf_limit'])})
                vlan_dict.update({'curr_count': int(group['curr_count'])})
                vlan_dict.update({'cfg_action': group['cfg_action']})
                vlan_dict.update({'currently': group['currently']})

        return ret_dict

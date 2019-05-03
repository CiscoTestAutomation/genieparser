"""show_fdb.py
   supported commands:
     *  show mac address-table vni <WORD> | grep <WORD>
     *  show mac address-table local vni <WORD>
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


class ShowMacAddressTableVniSchema(MetaParser):
    """Schema for show mac address-table vni <WORD> | grep <WORD>"""
    """Schema for show mac address-table local vni <WORD>"""

    schema = {'mac_address':
                {Any():
                    {'evi': str,
                     'mac_type': str,
                     'mac_aging_time': str,
                     'entry': str,
                     'secure': str,
                     'ntfy': str,
                     'next_hop': str,
                     'ports': str,
                    }
                },
            }

class ShowMacAddressTableVni(ShowMacAddressTableVniSchema):
    """Parser for show mac address-table vni <WORD> | grep <WORD>"""
    """Parser for show mac address-table local vni <WORD>"""

    cli_command = ['show mac address-table vni {vni} | grep {intf}', 'show mac address-table local vni {vni}']

    def cli(self, vni, intf=None, output=None):

        cmd = ""
        if output is None:
            if vni and intf:
                cmd = self.cli_command[0].format(vni=vni, intf=intf)
            if vni and not intf:
                cmd = self.cli_command[1].format(vni=vni)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # C 1001     0000.04b1.0000   dynamic  0         F      F    nve1(10.9.0.101)
        # * 1001     0000.0191.0000   dynamic  0         F      F    Eth1/11
        p1 = re.compile(r'^\s*(?P<entry>[A-Z\*\(\+\)]+) +(?P<evi>[0-9]+) '
            '+(?P<mac_address>[0-9a-z\.]+) +(?P<mac_type>[a-z]+) '
            '+(?P<age>[0-9\-\:]+) +(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
            '+([a-z0-9]+\((?P<next_hop>[0-9\.]+)\))?(?P<ports>[a-zA-Z0-9\/\.]+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                mac_address = str(m.groupdict()['mac_address'])

                if 'mac_address' not in ret_dict:
                    ret_dict['mac_address'] = {}
                if mac_address not in ret_dict['mac_address']:
                    ret_dict['mac_address'][mac_address] = {}

                ret_dict['mac_address'][mac_address]['evi'] = \
                    str(m.groupdict()['evi'])
                ret_dict['mac_address'][mac_address]['mac_type'] = \
                    str(m.groupdict()['mac_type'])
                ret_dict['mac_address'][mac_address]['mac_aging_time'] = \
                    str(m.groupdict()['age'])
                ret_dict['mac_address'][mac_address]['entry'] = \
                    str(m.groupdict()['entry'])
                ret_dict['mac_address'][mac_address]['secure'] = \
                    str(m.groupdict()['secure'])
                ret_dict['mac_address'][mac_address]['ntfy'] = \
                    str(m.groupdict()['ntfy'])
                ret_dict['mac_address'][mac_address]['next_hop'] = \
                    str(m.groupdict()['next_hop'])
                ret_dict['mac_address'][mac_address]['ports'] = \
                    str(m.groupdict()['ports'])

                continue

        return ret_dict


class ShowMacAddressTable(ShowMacAddressTableVniSchema):
    """Parser for show mac address-table"""
    """leverage existing 'ShowMacAddressTableVniSchema' """

    cli_command = ['show mac address-table']

    def cli(self, output=None):

        cmd = ""
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #   VLAN      MAC Address       Type     age     Secure NTFY  Ports
        # ---------+-----------------+--------+---------+------+----+------------------
        # * 30        aaaa.bbbb.cccc    static   -         F      F   Drop
        # G -         0000.dead.beef    static   -         F      F   sup - eth1(R)
        p1 = re.compile(r'^\s*(?P<entry>[A-Z\*\(\+\)]+) +(?P<evi>[0-9\-]+) '
                        '+(?P<mac_address>[0-9a-z\.]+) +(?P<mac_type>[a-z]+) '
                        '+(?P<age>[0-9\-\:]+) +(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
                        '+(\((?P<next_hop>[0-9\.]+)\))?(?P<ports>[a-zA-Z0-9\-\s\/\.\(\)]+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                mac_address = str(m.groupdict()['mac_address'])

                if 'mac_address' not in ret_dict:
                    ret_dict['mac_address'] = {}
                if mac_address not in ret_dict['mac_address']:
                    ret_dict['mac_address'][mac_address] = {}

                ret_dict['mac_address'][mac_address]['entry'] = \
                    str(m.groupdict()['entry'])
                ret_dict['mac_address'][mac_address]['evi'] = \
                    str(m.groupdict()['evi'])
                ret_dict['mac_address'][mac_address]['mac_type'] = \
                    str(m.groupdict()['mac_type'])
                ret_dict['mac_address'][mac_address]['mac_aging_time'] = \
                    str(m.groupdict()['age'])
                ret_dict['mac_address'][mac_address]['secure'] = \
                    str(m.groupdict()['secure'])
                ret_dict['mac_address'][mac_address]['ntfy'] = \
                    str(m.groupdict()['ntfy'])
                ret_dict['mac_address'][mac_address]['next_hop'] = \
                    str(m.groupdict()['next_hop'])
                ret_dict['mac_address'][mac_address]['ports'] = \
                    str(m.groupdict()['ports'])

                continue

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
        p1 = re.compile(r'^(?P<mac_aging_time>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Aging Time
            # ----------
            #     10
            m = p1.match(line)
            if m:
                ret_dict['mac_aging_time'] = int(m.groupdict()['mac_aging_time'])
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
                    'vlan': Or(int, str),
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
        p1 = re.compile(r'^Configured +System +Limit: +(?P<configured_system_limit>\d+)$')
        p2 = re.compile(r'^Current +System +Count: +(?P<current_system_count>\d+)$')
        p3 = re.compile(r'^Configured +System +Action: +(?P<configured_system_action>\w+)$')
        p4 = re.compile(r'^Currently +System +is: +(?P<currently_system_is>[\w\s]+)$')
        p5 = re.compile(r'^(?P<vlan>\w+) +(?P<conf_limit>\d+) +(?P<curr_count>\d+)'
                        ' +(?P<cfg_action>\w+) +(?P<currently>[\w\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict['configured_system_limit'] = int(m.groupdict()['configured_system_limit'])
                continue

            m = p2.match(line)
            if m:
                ret_dict['current_system_count'] = int(m.groupdict()['current_system_count'])
                continue

            m = p3.match(line)
            if m:
                ret_dict['configured_system_action'] = m.groupdict()['configured_system_action']
                continue

            m = p4.match(line)
            if m:
                ret_dict['currently_system_is'] = m.groupdict()['currently_system_is']
                continue

            # Vlan    Conf Limit     Curr Count    Cfg Action   Currently
            # ----    ------------   ---------     ---------    --------
            # 1       196000         0             Flood        Flooding Unknown SA
            # 10      196000         1             Flood        Flooding Unknown SA
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vlan = int(group['vlan']) if re.search('\d+', group['vlan']) else group['vlan'].lower()
                vlan_dict = ret_dict.setdefault('mac_table', {}).setdefault('vlans', {}).setdefault(str(vlan), {})
                vlan_dict['vlan'] = vlan
                vlan_dict['conf_limit'] = int(group['conf_limit'])
                vlan_dict['curr_count'] = int(group['curr_count'])
                vlan_dict['cfg_action'] = group['cfg_action']
                vlan_dict['currently'] = group['currently']

        return ret_dict


class ShowSystemInternalL2fwderMacSchema(MetaParser):
    """Schema for show system internal l2fwder mac"""

    schema = {'mac_table':
                {'vlans':
                    {Any():
                         {'entry': str,
                          'vlan': str,
                          'mac_address': str,
                          'mac_type': str,
                          'mac_aging_time': str,
                          'secure': str,
                          'ntfy': str,
                          'ports': str,
                         }
                    }
                }
            }


class ShowSystemInternalL2fwderMac(ShowSystemInternalL2fwderMacSchema):
    """Parser for show system internal l2fwder mac"""

    cli_command = ['show show system internal l2fwder mac']

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #   VLAN      MAC Address       Type     age     Secure NTFY  Ports
        # ---------+-----------------+--------+---------+------+----+------------------
        # G     -    5e00:c000:0007    static   -          F     F   sup-eth1(R)
        # *     1    fa16.3eef.6e79   dynamic   00:01:02   F     F     Eth1/4
        p1 = re.compile(r'^\s*(?P<entry>[A-Z\*\(\+\)]+) +(?P<vlan>[0-9\-]+) '
                        '+(?P<mac_address>[0-9a-z\.\:]+) +(?P<mac_type>[a-z]+) '
                        '+(?P<mac_aging_time>[0-9\-\:\.]+) +(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
                        '+(?P<ports>[a-zA-Z0-9\-\s\/\.\(\)]+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan = str(group['vlan'])
                vlan_dict = ret_dict.setdefault('mac_table', {}).setdefault('vlans', {}).setdefault(vlan, {})
                vlan_dict['entry'] = str(group['entry'])
                vlan_dict['vlan'] = str(vlan)
                vlan_dict['mac_address'] = str(group['mac_address'])
                vlan_dict['mac_type'] = str(group['mac_type'])
                vlan_dict['mac_aging_time'] = str(group['mac_aging_time'])
                vlan_dict['secure'] = str(group['secure'])
                vlan_dict['ntfy'] = str(group['ntfy'])
                vlan_dict['ports'] = str(group['ports'])

        return ret_dict
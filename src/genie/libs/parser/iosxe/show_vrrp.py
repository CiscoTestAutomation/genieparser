"""show_vrrp.py

IOSXE parsers for the following show commands:
    * 'show vrrp'
    * 'show vrrp all'
    * 'show vrrp interface {interface}'
    * 'show vrrp interface {interface} all'
    * 'show vrrp interface {interface} group {group}'
    * 'show vrrp interface {interface} group {group} all'
    * 'show vrrp brief'
    * 'show vrrp brief all'
    * 'show vrrp interface {interface} brief'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


# ========================================================
# Schema for:
#    * 'show vrrp'
#    * 'show vrrp all'
#    * 'show vrrp interface {interface}'
#    * 'show vrrp interface {interface} all'
#    * 'show vrrp interface {interface} group {group}'
#    * 'show vrrp interface {interface} group {group} all'
# ========================================================
class ShowVrrpSchema(MetaParser):
    """ Schema for:
        * 'show vrrp'
        * 'show vrrp all'
        * 'show vrrp interface {interface}'
        * 'show vrrp interface {interface} all'
        * 'show vrrp interface {interface} group {group}'
        * 'show vrrp interface {interface} group {group} all'
    """
    schema = {
        'interface': {
            Any(): {
                'group': {
                    int: {
                        Optional('description'): str,
                        'state': str,
                        'virtual_ip_address': str,
                        'virtual_mac_address': str,
                        'advertise_interval_secs': float,
                        'preemption': str,
                        Optional('vrrp_delay'): float,
                        'priority': int,
                        Optional('vrrs_name'): {
                            str: {
                                Optional('track_object'): {
                                    int: {
                                        Optional('state'): str,
                                        Optional('decrement'): int,
                                    }
                                }
                            }
                        },
                        Optional('track_object'): {
                            Any(): {
                                Optional('decrement'): int,
                                Optional('state'): str,
                            }
                        },
                        Optional('auth_text'): str,
                        'master_router_ip': str,
                        Optional('master_router'): str,
                        'master_router_priority': int,
                        'master_advertisement_interval_secs': float,
                        'master_down_interval_secs': float,
                        Optional('flags'): str
                    }
                }
            }
        }
    }


# ===================================================
# Parser for:
#   * 'show vrrp'
#   * 'show vrrp interface {interface}'
#   * 'show vrrp interface {interface} group {group}'
# ===================================================
class ShowVrrp(ShowVrrpSchema):
    """ Parser for:
        * 'show vrrp'
        * 'show vrrp interface {interface}'
        * 'show vrrp interface {interface} group {group}''
    """
    cli_command = ['show vrrp', 'show vrrp interface {interface}',
                   'show vrrp interface {interface} group {group}']

    def cli(self, interface='', group='', output=None):

        if output is None:
            if interface and group:
                cmd = self.cli_command[2].format(interface=interface,
                                                 group=group)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        result_dict = {}

        # Defines the regex for the first line of device output, which is:
        # Ethernet1/0 - Group 1
        # GigabitEthernet3.415 - Group 13
        p1 = re.compile(
            r'^(?P<interface>[\w,\.\/]+) - +Group (?P<group_number>\d+)$')

        #State is Master
        p2 = re.compile(r'State is (?P<state>(Master|UP|Init))')

        # Virtual IP address is 10.2.0.10
        p3 = re.compile(r'^Virtual +IP +address is (?P<vir_ip>[\d,\.]+)')

        # Virtual MAC address is 0000.5eff.0101
        p4 = re.compile(
            r'^Virtual +MAC +address +is (?P<vir_mac_addr>[\w,\.]+)')

        # Advertisement interval is 3.000 sec
        p5 = re.compile(
            r'^Advertisement +interval +is (?P<advrt_int>[\w,\.]+) +sec')

        #Preemption is enabled
        p6 = re.compile(r'^Preemption +is (?P<state>\w+)')

        # Preemption enabled
        p7 = re.compile(r'^Preemption (?P<state>\w+)')

        # min delay is 0.000 sec
        p8 = re.compile(r'^min +delay +is (?P<delay>[\w,\.]+) +sec')

        #Priority is 115
        p9 = re.compile(r'^Priority +is (?P<priority>\w+)')

        # Priority 100
        p10 = re.compile(r'^Priority (?P<priority>\w+)')

        # VRRS Group name DC_LAN
        p11 = re.compile(r'^VRRS +Group +name (?P<vrrs_grp_name>[\w,\_]+)')

        # Track object 1 state down decrement 15
        p12 = re.compile(
            r'Track +object (?P<obj_name>\w+) +state (?P<obj_state>(Up|Down)) +decrement (?P<value>\w+)')

        # Authentication text "hash"
        p13 = re.compile(r'Authentication +text \"(?P<type>[\w,\"]+)\"')

        # Master Router is 10.2.0.1 (local), priority is 100
        p14 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.]+) \((?P<server>\S+)\), +priority +is (?P<digit>\d+)')

        # Master Advertisement interval is 3.000 sec
        p15 = re.compile(
            r'^Master +Advertisement +interval +is (?P<mast_adv_interval>[\d,\.]+) +sec')

        # Master Down interval is 9.609 sec
        p16 = re.compile(
            r'^Master +Down +interval +is (?P<mast_down_interval>[\d,\.]+) +sec')

        # Master Router is 192.168.1.233, priority is 120
        p17 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.]+)+, +priority +is (?P<digit>\d+)')

        # FLAGS: 1/1
        p18 = re.compile(r'^FLAGS: +(?P<flags>[\d\/]+)')

        # DC-LAN Subnet
        p19 = re.compile(r'(?P<description>[\w+ \-]+)')


        for line in output.splitlines():
            line = line.strip()

            # Defines the regex for the first line of device output, which is:
            # Ethernet1/0 - Group 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                vrrp_group = int(group['group_number'])
                vrrp_dict = result_dict.setdefault('interface', {})\
                    .setdefault(interface, {})\
                    .setdefault('group', {})\
                    .setdefault(vrrp_group, {})
                continue

            #State is Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'state': str(group['state'])})
                continue

            # Virtual IP address is 10.2.0.10
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'virtual_ip_address': str(group['vir_ip'])})
                continue

            # Virtual MAC address is 0000.5eff.0101
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'virtual_mac_address': str(group['vir_mac_addr'])})
                continue

            # Advertisement interval is 3.000 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'advertise_interval_secs': float(group['advrt_int'])})
                continue

            #Preemption is enabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            # Preemption enabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            # min delay is 0.000 sec
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'vrrp_delay': float(group['delay'])})
                continue

            #Priority is 115
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            # Priority 100
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            # VRRS Group name DC_LAN
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vrf_group_name = group['vrrs_grp_name']
                vrf_dict = vrrp_dict.setdefault('vrrs_name',{})\
                    .setdefault(vrf_group_name,{})
                continue

            # Track object 1 state down decrement 15
            m = p12.match(line)
            if m:
                group = m.groupdict()
                track_object_number = int(group['obj_name'])

                if 'vrrs_name' in vrrp_dict.keys():
                    track_object_dict = vrf_dict.setdefault('track_object',{})\
                        .setdefault(track_object_number,{})
                else:
                    track_object_dict = vrrp_dict.setdefault('track_object', {})\
                        .setdefault(track_object_number,{})

                track_object_dict['decrement'] = int(group['value'])
                track_object_dict['state'] = group['obj_state']
                continue

            # Authentication text "hash"
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'auth_text': str(group['type'])})
                continue

            # Master Router is 10.2.0.1 (local), priority is 100
            m = p14.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': str(group['mast_ip_addr'])})
                vrrp_dict.update({'master_router': str(group['server'])})
                vrrp_dict.update(
                    {'master_router_priority': int(group['digit'])})
                continue

            # Master Advertisement interval is 3.000 sec
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_advertisement_interval_secs':
                        float(group['mast_adv_interval'])})
                continue

            # Master Down interval is 9.609 sec
            m = p16.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_down_interval_secs':
                        float(group['mast_down_interval'])})
                continue

            # Master Router is 192.168.1.233, priority is 120
            m = p17.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': str(group['mast_ip_addr'])})
                vrrp_dict.update(
                    {'master_router_priority': int(group['digit'])})
                continue

            # FLAGS: 1/1
            m = p18.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict['flags'] = str(group['flags'])
                continue

            # DC-LAN Subnet
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict['description'] = group['description']
                continue

        return result_dict


# ==========================
# Parser for:
#   * 'show vrrp all'
#   * 'show vrrp interface {interface} all'
#   * 'show vrrp interface {interface} group {group} all'
# ==========================
class ShowVrrpAll(ShowVrrp):
    """ Parser for:
        * 'show vrrp all'
        * 'show vrrp interface {interface} all'
        * 'show vrrp interface {interface} group {group} all
    """
    cli_command = ['show vrrp all', 'show vrrp interface {interface} all',
                    'show vrrp interface {interface} group {group} all']


    def cli(self, interface='', group='', output=None):

        if output is None:
            if interface and group:
                cmd = self.cli_command[2].format(interface=interface,
                                                 group=group)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        return super().cli(output=output)



# ==============================
# Schema for:
#   * 'show vrrp brief'
#   * 'show vrrp brief all'
#   * 'show vrrp interface {interface} brief'
# ==============================
class ShowVrrpBriefSchema(MetaParser):
    """ Schema for:
        * 'show vrrp brief'
        * 'show vrrp brief all'
        * 'show vrrp interface {interface} brief'
    """
    schema = {
        'interface':{
            Any(): {
                'group': {
                    Any(): {
                        'pri': int,
                        'time': int,
                        'pre': str,
                        'state': str,
                        'master_addr': str,
                        'group_addr': str
                    },
                }
            },
        }
    }


# ==============================
# Parser for:
#   * 'show vrrp brief'
#   * 'show vrrp interface {interface} brief'
# ==============================
class ShowVrrpBrief(ShowVrrpBriefSchema):
    """ Parser for:
        * 'show vrrp brief'
        * 'show vrrp interface {interface} brief'
    """
    cli_command = ['show vrrp brief', 'show vrrp interface {interface} brief']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        #Init vars
        parsed_dict = {}

        # Interface   Grp Pri Time  Own Pre State   Master addr  Group addr
        # Gi3.420    10  100 3609        Y Master  10.13.120.1  10.13.120.254
        p1 = re.compile(
            r'^(?P<interface_name>^\S+)\s+(?P<grp>\d+)'
            r'\s+(?P<pri>\d+)\s+(?P<time>\d+)\s+(?P<pre>\w)\s+'
            r'(?P<state>\w+)\s+(?P<master_addr>[\d\.]+)\s+'
            r'(?P<group_addr>[\d\.]+)')

        for line in output.splitlines():
            line = line.strip()

            # Gi3.420   10  100 3609     Y Master  10.13.120.1  10.13.120.254
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = \
                    Common.convert_intf_name(group['interface_name'])
                group_id =  int(group['grp'])

                interface_dict = parsed_dict.setdefault('interface', {})\
                    .setdefault(interface_name, {})\
                    .setdefault('group', {})\
                    .setdefault(group_id, {})

                interface_dict['pri'] =  int(group['pri'])
                interface_dict['time'] =  int(group['time'])
                interface_dict['pre'] =  group['pre']
                interface_dict['state'] =  group['state']
                interface_dict['master_addr'] =  group['master_addr']
                interface_dict['group_addr'] =  group['group_addr']
                continue

        return parsed_dict


# ================================
# Parser for 'show vrrp brief all'
# ================================
class ShowVrrpBriefAll(ShowVrrpBrief):
    """ Parser for:
        * 'show vrrp brief all'
    """
    cli_command = 'show vrrp brief all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


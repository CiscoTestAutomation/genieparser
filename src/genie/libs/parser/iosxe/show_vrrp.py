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
    * 'show vrrp detail'
    * 'show vrrp vpn <vpn_id>'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

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
                        Optional('state_duration'): {
                            'minutes': int,
                            'seconds': float,
                        },
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
                        'master_router_priority': Or(int, str),
                        'master_advertisement_interval_secs': Or(float, str),
                        Optional('master_advertisement_expiration_secs'): float,
                        'master_down_interval_secs': Or(float, str),
                        Optional('flags'): str,
                        Optional('address_family'): {
                            'ipv6': {
                                Optional('description'): str,
                                'state': str,
                                Optional('state_duration'): {
                                    'minutes': int,
                                    'seconds': float,
                                },
                                'virtual_ip_address': str,
                                'virtual_secondary_addresses': list,
                                'virtual_mac_address': str,
                                'advertise_interval_secs': float,
                                'preemption': str,
                                'priority': int,
                                Optional('track_object'): {
                                    Any(): {
                                        Optional('decrement'): int,
                                        Optional('state'): str,
                                    }
                                },
                                Optional('auth_text'): str,
                                'master_router_ip': str,
                                Optional('master_router'): str,
                                'master_router_priority': Or(int, str),
                                'master_advertisement_interval_secs': Or(float, str),
                                Optional('master_advertisement_expiration_secs'): float,
                                'master_down_interval_secs': Or(float, str),
                                Optional('flags'): str
                            }
                        }
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
        # Vlan33 - Group 10 - Address-Family IPv4
        # Vlan33 - Group 10 - Address-Family IPv6
        p1 = re.compile(
            r'^(?P<interface>[\w,\.\/]+)\s+-\s+Group\s(?P<group_number>\d+)(\s+-\s+Address-Family\s+(?P<address_family>IPv4|IPv6))?$')

        # State is Master
        # State is INIT (No Primary virtual IP address configured)
        p2 = re.compile(r'State is (?P<state>(Master|MASTER|Up|UP|Init|INIT)).*$')

        # State duration 8 mins 40.214 secs
        p2_1 = re.compile(r'^State\s+duration\s+(?P<minutes>\d+)\s+mins\s+(?P<seconds>[\d\.]+)\s+secs$')

        # Virtual IP address is 10.2.0.10
        # Virtual IP address is FE80::1
        # Virtual IP address is no address
        p3 = re.compile(r'^Virtual +IP +address is (?P<vir_ip>[\w\.\:]+.*)$')
    
        # Virtual secondary IP addresses:
        p4 = re.compile(r'^Virtual\ssecondary\sIP\saddresses:$')

        # 17::154/64
        p5 = re.compile(r'^(?P<virtual_secondary_address>[\d\:\/\.]+)$')

        # Virtual MAC address is 0000.5eff.0101
        p6 = re.compile(
            r'^Virtual +MAC +address +is (?P<vir_mac_addr>[\w,\.]+)$')

        # Advertisement interval is 3.000 sec
        p7 = re.compile(
            r'^Advertisement +interval +is (?P<advrt_interval>[\d,\.]+)\s+(?P<unit>\w+)$')

        #Preemption is enabled
        p8 = re.compile(r'^Preemption +is (?P<state>\w+)$')

        # Preemption enabled
        p9 = re.compile(r'^Preemption (?P<state>\w+)$')

        # min delay is 0.000 sec
        p10 = re.compile(r'^min +delay +is (?P<delay>[\d,\.]+) +sec$')

        # Priority is 115
        p11 = re.compile(r'^Priority +is +(?P<priority>\d+)$')

        # Priority 100
        p12 = re.compile(r'^Priority (?P<priority>\d+)$')

        # VRRS Group name DC_LAN
        p13 = re.compile(r'^VRRS +Group +name (?P<vrrs_grp_name>[\w,\_]+)$')

        # Track object 1 state down decrement 15
        p14 = re.compile(
            r'^Track +object (?P<obj_name>\w+) +state (?P<obj_state>(Up|UP|Down|DOWN)) +decrement (?P<value>\w+)$')

        # Authentication text "hash"
        p15 = re.compile(r'^Authentication +text \"(?P<type>[\w,\"]+)\"$')

        # Master Router is 10.2.0.1 (local), priority is 100
        # Master Router is FE80::2A3:D1FF:FE45:BEC5 (local), priority is 150
        p16 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.\:]+) \((?P<server>\S+)\), +priority +is (?P<digit>\d+)$')

        # Master Advertisement interval is 3.000 sec
        # Master Advertisement interval is 1000 msec (expires in 46 msec)
        p17 = re.compile(
            r'^Master +Advertisement +interval +is (?P<mast_adv_interval>[\d,\.]+) +(?P<interval_unit>\w+)(\s+\(expires\s+in\s+(?P<expiration>[\d\.]+)\s+(?P<expiration_unit>\w+)\))?$')

        # Master Advertisement interval is unknown
        p17_2 = re.compile(
            r'^Master +Advertisement +interval +is (?P<mast_adv_interval>[\w,\.]+)$')

        # Master Down interval is 9.609 sec
        # Master Down interval is unknown
        p18 = re.compile(
            r'^Master +Down +interval +is (?P<mast_down_interval>[\w,\.]+)( +sec)?$')

        # Master Router is 192.168.1.233, priority is 120
        # Master Router is FE80::2A3:D1FF:FE45:BEC5, priority is 150
        # Master Router is unknown, priority is unknown
        p19 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.\:]+)+, +priority +is +(?P<priority>\w+)$')

        # FLAGS: 1/1
        p20 = re.compile(r'^FLAGS:\s+(?P<flags>[\d\/]+)$')

        # Description is "WORKING-VRRP"
        p21 = re.compile(r'Description\s+is\s+(?P<description>\S+)$')

        # DC-LAN Subnet
        p21_1 = re.compile(r'^(?P<description>[\S\s]+)$')


        for line in output.splitlines():
            line = line.strip()

            # Defines the regex for the first line of device output, which is:
            # Ethernet1/0 - Group 1
            # GigabitEthernet3.415 - Group 13
            # Vlan33 - Group 10 - Address-Family IPv4
            # Vlan33 - Group 10 - Address-Family IPv6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                vrrp_group = int(group['group_number'])
                vrrp_dict = result_dict.setdefault('interface', {})\
                    .setdefault(interface, {})\
                    .setdefault('group', {})\
                    .setdefault(vrrp_group, {})
                if group['address_family'] == 'IPv6':
                    vrrp_dict = result_dict.setdefault('interface', {})\
                    .setdefault(interface, {})\
                    .setdefault('group', {})\
                    .setdefault(vrrp_group, {})\
                    .setdefault('address_family', {})\
                    .setdefault('ipv6', {})
                continue

            # State is Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'state': str(group['state'])})
                continue

            # State duration 8 mins 40.214 secs
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                dur_dict = vrrp_dict.setdefault('state_duration', {})
                dur_dict.update({'minutes': int(group['minutes']), 
                                 'seconds': float(group['seconds'])})
                continue

            # Virtual IP address is 10.2.0.10
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'virtual_ip_address': str(group['vir_ip'])})
                continue

            # Virtual secondary IP addresses:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'virtual_secondary_addresses': []})
                continue

            # 17::154/64
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if 'virtual_secondary_addresses' in vrrp_dict:
                    vrrp_dict['virtual_secondary_addresses']\
                        .append(group['virtual_secondary_address'])
                continue

            # Virtual MAC address is 0000.5eff.0101
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'virtual_mac_address': str(group['vir_mac_addr'])})
                continue

            # Advertisement interval is 3.000 sec
            # Advertisement interval is 1000 msec
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if group['unit'] == 'msec':
                    seconds = float(group['advrt_interval']) / 1000
                else:
                    seconds = float(group['advrt_interval'])
                vrrp_dict.update({'advertise_interval_secs': seconds})
                continue

            #Preemption is enabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            # Preemption enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            # min delay is 0.000 sec
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'vrrp_delay': float(group['delay'])})
                continue

            #Priority is 115
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            # Priority 100
            m = p12.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            # VRRS Group name DC_LAN
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vrf_group_name = group['vrrs_grp_name']
                vrf_dict = vrrp_dict.setdefault('vrrs_name',{})\
                    .setdefault(vrf_group_name,{})
                continue

            # Track object 1 state down decrement 15
            m = p14.match(line)
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
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'auth_text': str(group['type'])})
                continue

            # Master Router is 10.2.0.1 (local), priority is 100
            m = p16.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': str(group['mast_ip_addr'])})
                vrrp_dict.update({'master_router': str(group['server'])})
                vrrp_dict.update(
                    {'master_router_priority': int(group['digit'])})
                continue

            # Master Advertisement interval is 3.000 sec
            # Master Advertisement interval is 1000 msec (expires in 46 msec)
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if group['interval_unit'] == 'msec':
                    seconds = float(group['mast_adv_interval']) / 1000
                else:
                    seconds = float(group['mast_adv_interval'])
                vrrp_dict.update({'master_advertisement_interval_secs': 
                                  seconds})

                if group['expiration_unit']:
                    if group['expiration_unit'] == 'msec':
                        seconds = float(group['expiration']) / 1000
                    else:
                        seconds = float(group['expiration'])
                    vrrp_dict.update({'master_advertisement_expiration_secs': 
                                    seconds})

                continue

            # Master Advertisement interval is unknown
            m = p17_2.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'master_advertisement_interval_secs': 
                                  group['mast_adv_interval']})


            # Master Down interval is 9.609 sec
            # Master Down interval is unknown
            m = p18.match(line)
            if m:
                group = m.groupdict()
                try:
                    vrrp_dict.update({'master_down_interval_secs':
                                      float(group['mast_down_interval'])})
                except ValueError:
                    vrrp_dict.update({'master_down_interval_secs':
                                      group['mast_down_interval']})
                continue

            # Master Router is 192.168.1.233, priority is 120
            # Master Router is unknown, priority is unknown
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': group['mast_ip_addr']})
                try:
                    priority = int(group['priority'])
                except ValueError:
                    priority = group['priority']
                vrrp_dict.update(
                    {'master_router_priority': priority})
                continue

            # FLAGS: 1/1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict['flags'] = str(group['flags'])
                continue

            # Description is "WORKING-VRRP"
            m = p21.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict['description'] = group['description'].replace('"', '')
                continue

            # DC-LAN Subnet
            m = p21_1.match(line)
            if m:
                group = m.groupdict()
                if 'description' not in vrrp_dict:
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

# =============================================
# Parser Schema for 'show vrrp detail'
# =============================================
class ShowVrrpDetailSchema(MetaParser):
    """ Schema for "show vrrp detail" """

    schema = {
        'interface': {
            Any(): {
                'group_number': {
                    Any(): {
                        'address_family': str,
                        'state': str,
                        'state_duration': {
                            'hours': int,
                            'minutes': int,
                            'seconds': float
                        },
                        'virtual_ip_address': str,
                        'virtual_mac_address': str,
                        'advertise_interval': int,
                        'preemption_state': str,
                        'priority': int,
                        'state_change_reason': str,
                        'tloc_preference': int,
                        Optional('track_object'): {
                            Any(): {
                                'state': str
                            }
                        },
                        'master_router': str,
                        'master_router_priority': Or(int, str),
                        'master_advertisement_interval': Or(int, str),
                        'master_down_interval': Or(int, str),
                        'flags': str,
                        'vrrpv3_advertisements': {
                            'sent': int,
                            'errors': int,
                            'rcvd': int
                        },
                        'vrrpv2_advertisements': {
                            'sent': int,
                            'errors': int,
                            'rcvd': int
                        },
                        'group_discarded_packets': {
                            'total' : int,
                            'vrrpv2_incompatibility': int,
                            'ip_address_owner_conflicts': int,
                            'invalid_address_count': int,
                            'ip_address_configuration_mismatch': int,
                            'invalid_advert_interval': int,
                            'adverts_received_in_Init_state': int,
                            'invalid_group_other_reason': int,
                        },
                        'group_state_transition': {
                            'init_to_master': int,
                            'init_to_backup': int,
                            'backup_to_master': int,
                            'master_to_backup': int,
                            'master_to_init': int,
                            'backup_to_init': int
                        }
                    }
                }
            }
        }
    }


# =============================================
# Parser for 'show vrrp detail'
# =============================================

class ShowVrrpDetail(ShowVrrpDetailSchema):
    """ parser for "show vrrp detail" """

    cli_command = "show vrrp detail"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        config_dict = {}

        # GigabitEthernet0/0/2.150 - Group 2 - Address-Family IPv4
        p1 = re.compile(
            r'^(?P<interface>[\w,\.\/]+)\s+-\s+Group\s(?P<group_number>\d+)(\s+-\s+Address-Family\s+(?P<address_family>IPv4|IPv6))?$')

        # State is INIT (No layer3 interface address)
        # State is BACKUP
        p2 = re.compile(r'^State is (?P<state>(Master|MASTER|Up|UP|Init|INIT|BACKUP)).*$')

        # State duration 6 hours 40 mins 47 secs
        p3 = re.compile(
            r'^State\s+duration\s+(?P<hours>\d+)\s+hours\s(?P<minutes>\d+)\s+mins\s+(?P<seconds>[\d\.]+)\s+secs$')

        # Virtual IP address is no address
        # Virtual IP address is 192.105.105.201
        p4 = re.compile(r'^Virtual\sIP\saddress\sis\s(?P<virtual_ip_address>[\w\.\:]+.*)$')

        # Virtual MAC address is 0000.5E00.0102
        p5 = re.compile(r'^Virtual\sMAC\saddress\sis\s(?P<virtual_mac_address>[\w,\.]+)$')

        # Advertisement interval is 1000 msec
        p6 = re.compile(r'^Advertisement\sinterval\sis\s+(?P<advertise_interval>[\d,\.]+)\s+(?P<unit>\w+)$')

        # Preemption enabled
        p7 = re.compile(r'^Preemption\s+(?P<preemption_state>\w+)$')

        # Priority is 250
        p8 = re.compile(r'^Priority\sis\s+(?P<priority>\d+)$')

        # State change reason is VRRP_INIT
        p9 = re.compile(r'^State\schange\sreason\sis\s+(?P<state_change_reason>\w+)$')

        # Tloc preference not configured, value 0
        p10 = re.compile(r'^Tloc\spreference\snot\sconfigured,\svalue+\s(?P<tloc_preference>\d+)$')

        # Master Router is unknown, priority is unknown
        # Master Router is 192.105.105.91, priority is 220
        p11 = re.compile(
            r'^Master\sRouter\sis\s(((?P<master_router>(([\w,\.\:]+) \((?P<server>\S+)\))|[\w,\.\:]+)+)),\spriority\sis\s(?P<master_router_priority>\w+)$')

        # Master Advertisement interval is unknown
        # Master Advertisement interval is 1000 msec (learned)
        p12 = re.compile(
            r'^Master +Advertisement +interval +is (?P<master_advertisement_interval>([\w,\.]+)|([\d,\.]+) +(?P<interval_unit>\w+)(\s+\(expires\s+in\s+(?P<expiration>[\d\.]+)\s+(?P<expiration_unit>\w+)\)))?')

        # Master Down interval is unknown
        # Master Down interval is 3218 msec (expires in 3066 msec)
        p13 = re.compile(
            r'^Master\sDown\sinterval\sis\s(?P<master_down_interval>([\w,\.]+)|([\d,\.]+) +(?P<interval_unit>\w+)(\s+\(expires\s+in\s+(?P<expiration>[\d\.]+)\s+(?P<expiration_unit>\w+)\)))?$')

        # FLAGS: 1/0
        p14 = re.compile(r'^FLAGS:\s+(?P<flags>[\d\/]+)$')

        # VRRPv3 Advertisements: sent 0 (errors 10) - rcvd 0
        # VRRPv3 Advertisements: sent 23 (errors 0) - rcvd 26331
        p15 = re.compile(
            r'^VRRPv3\sAdvertisements:\ssent\s+(?P<sent>\d+)\s\(\S+\s+(?P<errors>\d+)\)\s+\S+\s+\w+\s+(?P<rcvd>\d+)$')

        # VRRPv2 Advertisements: sent 0 (errors 10) - rcvd 0
        # VRRPv2 Advertisements: sent 23 (errors 0) - rcvd 2
        p16 = re.compile(
            r'^VRRPv2\sAdvertisements:\ssent\s+(?P<sent>\d+)\s\(\S+\s+(?P<errors>\d+)\)\s+\S+\s+\w+\s+(?P<rcvd>\d+)$')

        # Group Discarded Packets: 0
        p17 = re.compile(r'^Group\sDiscarded\sPackets:\s+(?P<group_discarded_packets>\d+)$')

        # VRRPv2 incompatibility: 0
        p18 = re.compile(r'^VRRPv2\sincompatibility:\s+(?P<vrrpv2_incompatibility>\d+)$')

        # IP Address Owner conflicts: 0
        p19 = re.compile(r'^IP\sAddress\sOwner\sconflicts:\s+(?P<ip_address_owner_conflicts>\d+)$')

        # Invalid address count: 0
        p20 = re.compile(r'^Invalid\saddress\scount:\s+(?P<invalid_address_count>\d+)$')

        # IP address configuration mismatch : 0
        p21 = re.compile(r'^IP\saddress\sconfiguration\smismatch\s:\s+(?P<ip_address_configuration_mismatch>\d+)$')

        # Invalid Advert Interval: 0
        p22 = re.compile(r'^Invalid\sAdvert\sInterval:\s+(?P<invalid_advert_interval>\d+)$')

        # Adverts received in Init state: 0
        p23 = re.compile(r'^Adverts\sreceived\sin\sInit\sstate:\s+(?P<adverts_received_in_Init_state>\d+)$')

        # Invalid group other reason: 0
        p24 = re.compile(r'^Invalid\sgroup\sother\sreason:\s+(?P<invalid_group_other_reason>\d+)$')

        # Init to master: 0
        p25 = re.compile(r'^Init\sto\smaster:\s+(?P<init_to_master>\d+)')

        # Init to backup: 0
        # Init to backup: 2 (Last change Tue Feb 15 07:17:16.662)
        p26 = re.compile(r'^Init\sto\sbackup:\s+(?P<init_to_backup>\d+)')

        # Backup to master: 0
        # Backup to master: 2 (Last change Tue Feb 15 07:17:19.881)
        p27 = re.compile(r'^Backup\sto\smaster:\s+(?P<backup_to_master>\d+)')

        # Master to backup: 0
        # Master to backup: 1 (Last change Tue Feb 15 07:17:37.384)
        p28 = re.compile(r'^Master\sto\sbackup:\s+(?P<master_to_backup>\d+)')

        # Master to init: 0
        p29 = re.compile(r'^Master\sto\sinit:\s+(?P<master_to_init>\d+)')

        # Backup to init: 0
        # Backup to init: 1 (Last change Tue Feb 15 07:12:56.285)
        p30 = re.compile(r'^Backup\sto\sinit:\s+(?P<backup_to_init>\d+)')

        # Track object omp state UP shutdown
        p31 = re.compile(r'^Track\sobject\s(?P<obj_name>\w+)\sstate\s(?P<obj_state>(Up|UP|Down|DOWN))\s\w+$')

        for line in output.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/2.150 - Group 2 - Address-Family IPv4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                group_number = int(group['group_number'])
                address_family = group['address_family']
                interface_dict = config_dict.setdefault('interface', {}).setdefault(interface, {}).setdefault(
                    'group_number', {}).setdefault(group_number, {})
                interface_dict['address_family'] = address_family
                continue

            # State is INIT (No layer3 interface address)
            # State is BACKUP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                interface_dict['state'] = state
                continue

            # State duration 6 hours 40 mins 47 secs
            m = p3.match(line)
            if m:
                group = m.groupdict()
                hours = group['hours']
                minutes = group['minutes']
                seconds = group['seconds']
                state_duration_dict = interface_dict.setdefault('state_duration', {})
                state_duration_dict.update({'hours': int(group['hours']),
                                            'minutes': int(group['minutes']),
                                            'seconds': float(group['seconds'])})
                continue

            # Virtual IP address is no address
            # Virtual IP address is 192.105.105.201
            m = p4.match(line)
            if m:
                group = m.groupdict()
                virtual_ip_address = group['virtual_ip_address']
                interface_dict['virtual_ip_address'] = virtual_ip_address
                continue

            # Virtual MAC address is 0000.5E00.0102
            m = p5.match(line)
            if m:
                group = m.groupdict()
                virtual_mac_address = group['virtual_mac_address']
                interface_dict['virtual_mac_address'] = virtual_mac_address
                continue

            # Advertisement interval is 1000 msec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                advertise_interval = int(group['advertise_interval'])
                interface_dict['advertise_interval'] = advertise_interval
                continue

            # Preemption enabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                preemption_state = group['preemption_state']
                interface_dict['preemption_state'] = preemption_state
                continue

            # Priority is 250
            m = p8.match(line)
            if m:
                group = m.groupdict()
                priority = int(group['priority'])
                interface_dict['priority'] = priority
                continue

            # State change reason is VRRP_INIT
            m = p9.match(line)
            if m:
                group = m.groupdict()
                state_change_reason = group['state_change_reason']
                interface_dict['state_change_reason'] = state_change_reason
                continue

            # Tloc preference not configured, value 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                tloc_preference = int(group['tloc_preference'])
                interface_dict['tloc_preference'] = tloc_preference
                continue

            # Master Router is unknown, priority is unknown
            # Master Router is 192.105.105.91, priority is 220
            m = p11.match(line)
            if m:
                group = m.groupdict()
                master_router = group['master_router']
                master_router_priority = group['master_router_priority']
                interface_dict['master_router'] = master_router
                interface_dict['master_router_priority'] = master_router_priority
                continue

            # Master Advertisement interval is unknown
            # Master Advertisement interval is 1000 msec (learned)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                master_advertisement_interval = group['master_advertisement_interval']
                interface_dict['master_advertisement_interval'] = master_advertisement_interval
                continue

            # Master Down interval is unknown
            # Master Down interval is 3218 msec (expires in 3066 msec)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                master_down_interval = group['master_down_interval']
                interface_dict['master_down_interval'] = master_down_interval
                continue

            # FLAGS: 1/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                flags = group['flags']
                interface_dict['flags'] = flags
                continue

            # VRRPv3 Advertisements: sent 0 (errors 0) - rcvd 0
            # VRRPv3 Advertisements: sent 23 (errors 0) - rcvd 26331
            m = p15.match(line)
            if m:
                group = m.groupdict()
                sent = group['sent']
                errors = group['errors']
                rcvd = group['rcvd']

                vrrpv3_advertisements_dict = interface_dict.setdefault('vrrpv3_advertisements', {})
                vrrpv3_advertisements_dict.update({'sent': int(group['sent']),
                                                   'errors': int(group['errors']),
                                                   'rcvd': int(group['rcvd'])})
                continue
				
            # VRRPv2 Advertisements: sent 0 (errors 0) - rcvd 0
            # VRRPv2 Advertisements: sent 23 (errors 0) - rcvd 2
            m = p16.match(line)
            if m:
                group = m.groupdict()
                sent = group['sent']
                errors = group['errors']
                rcvd = group['rcvd']

                vrrpv2_advertisements_dict = interface_dict.setdefault('vrrpv2_advertisements', {})
                vrrpv2_advertisements_dict.update({'sent': int(group['sent']),
                                                   'errors': int(group['errors']),
                                                   'rcvd': int(group['rcvd'])})
                continue
				
            # Group Discarded Packets: 0
            # Group Discarded Packets: 26361
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group_discarded_packets = int(group['group_discarded_packets'])
                group_discarded_packets_dict = interface_dict.setdefault('group_discarded_packets', {})
                group_discarded_packets_dict["total"] = group_discarded_packets
                continue

            # VRRPv2 incompatibility: 0
            # VRRPv2 incompatibility: 26329
            m = p18.match(line)
            if m:
                group = m.groupdict()
                vrrpv2_incompatibility = int(group['vrrpv2_incompatibility'])
                group_discarded_packets_dict["vrrpv2_incompatibility"] = vrrpv2_incompatibility
                continue

            # IP Address Owner conflicts 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ip_address_owner_conflicts = int(group['ip_address_owner_conflicts'])
                group_discarded_packets_dict['ip_address_owner_conflicts'] = ip_address_owner_conflicts
                continue
				
            # Invalid address count: 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                invalid_address_count = int(group['invalid_address_count'])
                group_discarded_packets_dict['invalid_address_count'] = invalid_address_count
                continue
				
            # IP address configuration mismatch: 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ip_address_configuration_mismatch = int(group['ip_address_configuration_mismatch'])
                group_discarded_packets_dict['ip_address_configuration_mismatch'] = ip_address_configuration_mismatch
                continue
				
            # Invalid Advert Interval: 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                invalid_advert_interval = int(group['invalid_advert_interval'])
                group_discarded_packets_dict['invalid_advert_interval'] = invalid_advert_interval
                continue
				
            # Adverts received in Init state: 0
            # Adverts received in Init state: 32
            m = p23.match(line)
            if m:
                group = m.groupdict()
                adverts_received_in_Init_state = int(group['adverts_received_in_Init_state'])
                group_discarded_packets_dict['adverts_received_in_Init_state'] = adverts_received_in_Init_state
                continue
				
            # Invalid group other reason: 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                invalid_group_other_reason = int(group['invalid_group_other_reason'])
                group_discarded_packets_dict['invalid_group_other_reason'] = invalid_group_other_reason
                continue
				
            # Init to master: 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                init_to_master = int(group['init_to_master'])

                group_state_transition_dict = interface_dict.setdefault('group_state_transition', {})
                group_state_transition_dict['init_to_master'] = init_to_master
                continue
				
            # Init to backup: 0
            # Init to backup: 2 (Last change Tue Feb 15 07:17:16.662)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                init_to_backup = int(group['init_to_backup'])
                group_state_transition_dict['init_to_backup'] = init_to_backup
                continue
				
            # Backup to master: 0
            # Backup to master: 2 (Last change Tue Feb 15 07:17:19.881)
            m = p27.match(line)
            if m:
                group = m.groupdict()
                backup_to_master = int(group['backup_to_master'])
                group_state_transition_dict['backup_to_master'] = backup_to_master
                continue
				
            # Master to backup: 0
            # Master to backup: 1 (Last change Tue Feb 15 07:17:37.384)
            m = p28.match(line)
            if m:
                group = m.groupdict()
                master_to_backup = int(group['master_to_backup'])
                group_state_transition_dict['master_to_backup'] = master_to_backup
                continue
				
            # Master to init: 0
            # Master to init: 1 (Last change Tue Feb 15 07:12:56.285)
            m = p29.match(line)
            if m:
                group = m.groupdict()
                master_to_init = int(group['master_to_init'])
                group_state_transition_dict['master_to_init'] = master_to_init
                continue
				
            # Backup to init: 0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                backup_to_init = int(group['backup_to_init'])
                group_state_transition_dict['backup_to_init'] = backup_to_init
                continue
				
            # Track object omp state UP shutdown
            m = p31.match(line)
            if m:
                group = m.groupdict()
                track_object_number = group['obj_name']
                track_object_dict = interface_dict.setdefault('track_object', {}) \
                    .setdefault(track_object_number, {})
                track_object_dict['state'] = group['obj_state']
                continue
				
        return config_dict

# =============================================
# Parser Schema for 'show vrrp vpn <vpn_id>'
# =============================================

class ShowVrrpVpnSchema(MetaParser):
    '''Schema for 'show vrrp vpn <vpn_id>' '''

    schema = {
        'vrrp_vpn': int,
        'interfaces': {
            str: {
                'groups': {
                    int: {
                        'virtual_ip_address': str,
                        'virtual_mac_address': str,
                        'priority': int,
                        'real_priority': int,
                        'vrrp_state': str,
                        'omp_state': str,
                        'advertisement_timer': int,
                        'primary_down_timer': int,
                        'last_state_change_time': str
                    }
                }
            }
        }
    }

# =============================================
# Parser for 'show vrrp vpn <vpn_id>'
# =============================================

class ShowVrrpVpn(ShowVrrpVpnSchema):
    """ parser for "show vrrp vpn <vpn_id>" """

    cli_command = "show vrrp vpn {vpn_id}"

    def cli(self, vpn_id='', output=None):
        cmd = self.cli_command.format(vpn_id=vpn_id)

        if output is None:
            output = self.device.execute(self.cli_command)

        config_dict = {}

        # vrrp vpn 1
        p1 = re.compile(r'^vrrp\svpn\s(?P<vrrp_vpn>\d+)$')

        # interfaces ge2/3.101
        p2 = re.compile(r'^interfaces\s(?P<interfaces>[\w,\.\/]+)$')

        # groups 1
        p3 = re.compile(r'^groups\s(?P<groups>\d+)$')

        # virtual-ip             182.210.210.201
        p4 = re.compile(r'^virtual-ip\s+(?P<virtual_ip_address>[\w\.\:]+.*)$')

        # virtual-mac            00:00:5e:00:01:01
        p5 = re.compile(r'^virtual-mac\s+(?P<virtual_mac_address>[\w,\.:]+)$')

        # priority            115
        p6 = re.compile(r'^priority\s+(?P<priority>\d+)$')

        # real-priority          105
        p7 = re.compile(r'^real-priority\s+(?P<real_priority>\d+)$')

        # vrrp-state             primary
        p8 = re.compile(r'^vrrp-state\s+(?P<vrrp_state>\w+)$')

        #  omp-state              up
        p9 = re.compile(r'^omp-state\s+(?P<omp_state>\w+)$')

        #  advertisement-timer    1
        p10 = re.compile(r'^advertisement-timer\s+(?P<advertisement_timer>\d+)$')

        #  primary-down-timer     3
        p11 = re.compile(r'^primary-down-timer\s+(?P<primary_down_timer>\d+)$')

        #  last-state-change-time 2022-01-24T06:56:20+00:00
        p12 = re.compile(r'^last-state-change-time\s+(?P<last_state_change_time>[\w:-]+[+]+[\w:]+)$')

        for line in output.splitlines():
            line = line.strip()

            # vrrp vpn 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrrp_vpn = int(group['vrrp_vpn'])
                config_dict['vrrp_vpn'] = vrrp_vpn
                continue

            # interfaces ge2/3.101
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interfaces = group['interfaces']
                interfaces_dict = config_dict.setdefault('interfaces', {}).setdefault(interfaces, {})
                continue

            # groups 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                groups = int(group['groups'])
                groups_dict = interfaces_dict.setdefault('groups', {}).setdefault(groups, {})
                continue

            # virtual-ip             182.210.210.201
            m = p4.match(line)
            if m:
                group = m.groupdict()
                virtual_ip_address = group['virtual_ip_address']
                groups_dict['virtual_ip_address'] = virtual_ip_address
                continue

            # virtual-mac            00:00:5e:00:01:01
            m = p5.match(line)
            if m:
                group = m.groupdict()
                virtual_mac_address = group['virtual_mac_address']
                groups_dict['virtual_mac_address'] = virtual_mac_address
                continue

            # priority               115
            m = p6.match(line)
            if m:
                group = m.groupdict()
                priority = int(group['priority'])
                groups_dict['priority'] = priority
                continue

            # real-priority          105
            m = p7.match(line)
            if m:
                group = m.groupdict()
                real_priority = int(group['real_priority'])
                groups_dict['real_priority'] = real_priority
                continue

            # vrrp-state             primary
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrrp_state = group['vrrp_state']
                groups_dict['vrrp_state'] = vrrp_state
                continue

            # omp-state              up
            m = p9.match(line)
            if m:
                group = m.groupdict()
                omp_state = group['omp_state']
                groups_dict['omp_state'] = omp_state
                continue

            # advertisement-timer    1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                advertisement_timer = int(group['advertisement_timer'])
                groups_dict['advertisement_timer'] = advertisement_timer
                continue

            # primary-down-timer     3
            m = p11.match(line)
            if m:
                group = m.groupdict()
                primary_down_timer = int(group['primary_down_timer'])
                groups_dict['primary_down_timer'] = primary_down_timer
                continue

            # last-state-change-time 2022-01-24T06:56:20+00:00
            m = p12.match(line)
            if m:
                group = m.groupdict()
                last_state_change_time = group['last_state_change_time']
                groups_dict['last_state_change_time'] = last_state_change_time
                continue

        return config_dict

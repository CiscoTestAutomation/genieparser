"""show_lldp.py
    supported commands:
        *show lldp all
        *show lldp timers
        *show lldp tlv-select 
        *show lldp neighbors detail
        *show lldp traffic 
"""
import re

# metaparsers
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================
# Schema for 'show lldp all'
# ==============================
class ShowLldpAllSchema(MetaParser):
    """schema for show lldp all"""
    schema = {
        'interfaces':
            {Any():
                 {'enabled': bool,
                  'tx': bool,
                  'rx': bool,
                  'dcbx': bool
                  },
             },
    }


class ShowLldpAll(ShowLldpAllSchema):
    """parser for show lldp all"""
    cli_command = 'show lldp all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}

        # Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
        # Interface Information: mgmt0 Enable (tx/rx/dcbx): Y/Y/N  
        p1 = re.compile(
            r'^Interface Information: +(?P<interface>[\S]+) +('
            r'?P<enabled>[a-zA-Z]+) +\(tx/rx/dcbx\): +(?P<tx>[YN])/('
            r'?P<rx>[YN])/(?P<dcbx>[YN])$')

        for line in out.splitlines():
            line = line.strip()

            # Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"])
                sub_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface,
                                                                               {})

                sub_dict.update({'enabled': True if group[
                                                        'enabled'] == 'Enable' else
                False})
                sub_dict.update({'tx': True if group['tx'] == 'Y' else False})
                sub_dict.update({'rx': True if group['rx'] == 'Y' else False})
                sub_dict.update({'dcbx': True if group['dcbx'] == 'Y' else False})
                continue

        return parsed_dict


# ==============================
# Schema for 'show lldp timers'
# ==============================
class ShowLldpTimersSchema(MetaParser):
    """Schema for show lldp timers"""
    schema = {
        'hold_timer': int,
        'reinit_timer': int,
        'hello_timer': int,
        Optional('transmit_delay'): int,
        Optional('hold_multiplier'): int,
        Optional('notification_interval'): int
    }


class ShowLldpTimers(ShowLldpTimersSchema):
    """parser for show lldp timers"""
    cli_command = 'show lldp timers'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}

        '''
         LLDP Timers:
        
            Holdtime in seconds: 120
            Reinit-time in seconds: 2
            Transmit interval in seconds: 30
            Transmit delay in seconds: 2
            Hold multiplier in seconds: 4
            Notification interval in seconds: 5
         '''
        p1 = re.compile(r'^(?P<timer>[\w\s-]+) +in +seconds: +(?P<seconds>\d+)$')
        for line in out.splitlines():
            line = line.strip()

            # Holdtime in seconds: 120
            m = p1.match(line)
            if m:
                timer = m.groupdict()
                timer_name = timer['timer']
                seconds = int(timer['seconds'])
                if timer_name == 'Holdtime':
                    parsed_dict.update({'hold_timer': seconds})
                elif timer_name == 'Reinit-time':
                    parsed_dict.update({'reinit_timer': seconds})
                elif 'Transmit delay' in timer_name:
                    parsed_dict.update({'transmit_delay': seconds})
                elif 'Hold multiplier' in timer_name:
                    parsed_dict.update({'hold_multiplier': seconds})
                elif 'Notification interval' in timer_name:
                    parsed_dict.update({'notification_interval': seconds})
                else:
                    parsed_dict.update({'hello_timer': seconds})
                continue

        return parsed_dict


# =================================
# schema for 'show lldp tlv-select'
# =================================

class ShowLldpTlvSelectSchema(MetaParser):
    """Schema for show lldp tlv-select"""
    schema = {'suppress_tlv_advertisement': {
        Any(): bool
    }
    }


class ShowLldpTlvSelect(ShowLldpTlvSelectSchema):
    """parser for show lldp tlv-select"""
    cli_command = 'show lldp tlv-select'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip().lower()
            line = re.sub(r'[ -]', '_', line)
            if not line:
                continue
            sub_dict = parsed_dict.setdefault(
                'suppress_tlv_advertisement', {})

            sub_dict.update({line: False})

        return parsed_dict


# =================================
# schema for 'show lldp neighbors detail'
# =================================
class ShowLldpNeighborsDetailSchema(MetaParser):
    """Schema for show lldp neighbors detail"""
    schema = {
        'total_entries': int,
        'interfaces': {
            Any(): {
                'port_id': {
                    Any(): {
                        'neighbors': {
                            Any(): {
                                'chassis_id': str,
                                Optional('port_description'): str,
                                'system_name': str,
                                'system_description': str,
                                'time_remaining': int,
                                Optional('capabilities'): {
                                    Any(): {
                                        'name': str,
                                        Optional('system'): bool,
                                        Optional('enabled'): bool
                                    }
                                },
                                'management_address_v4': str,
                                Optional('management_address_v6'): str,
                                Optional('system_capabilities'): str,
                                Optional('enabled_capabilities'): str,
                                'vlan_id': str
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLldpNeighborsDetail(ShowLldpNeighborsDetailSchema):
    """parser for lldp show neighbors detail"""
    # Capability codes:
    #    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    #    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
    CAPABILITY_CODES = {'R': 'router',
                        'B': 'bridge',
                        'T': 'telephone',
                        'C': 'docsis_cable_device',
                        'W': 'wlan_access_point',
                        'P': 'repeater',
                        'S': 'station_only',
                        'O': 'other'}
    cli_command = 'show lldp neighbors detail'
    exclude = ['time_remaining']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # init returned dict
        parsed_dict = {}

        # init sub dicts
        sub_dict = {}
        intf_dict = {}
        port_dict = {}
        tmp_chassis_id = ''
        tmp_port_id = ''
        # Chassis id: 000d.bdff.4f04
        # Chassis id: 39373638-3935-5A43-4A37-35303036574C
        p1 = re.compile(r'^Chassis +id: +(?P<chassis_id>.+?)\s*$')
        # Port id: Gi0/0/0/1
        # Port id: PCI-E Slot 1, Port 2
        p2 = re.compile(r'^Port +id: +(?P<port_id>[\S ]+)$')
        # Local Port id: Eth1/2
        p3 = re.compile(r'^Local +Port +id: +(?P<local_port_id>\S+)$')
        # Port Description: null
        p4 = re.compile(r'^Port +Description: +(?P<port_description>(?!null).+)$')
        # System Name: R2_xrv9000
        p5 = re.compile(r'^System +Name: +(?P<system_name>.+?)\s*$')
        # System Description:  6.2.2, IOS-XRv 9000
        p6 = re.compile(r'^System +Description: +(?P<system_description>.+?)$')
        # Copyright (c) 1986-2017 by Cisco Systems, Inc.
        p6_1 = re.compile(r'^(?P<copyright>Copyright +\([c|C]\) +.+)$')
        # Compiled Sat 22-Jul-17 05:51 by
        p6_2 = re.compile(r'^(?P<compiled_by>Compiled +.+)$')
        # Technical Support: http://www.cisco.com/techsupport
        p6_3 = re.compile(r'^(?P<technical_support>(Technical|TAC) (S|s)upport: +.+)$')

        # "Cisco IOS XR Software, Version 5.3.4[Default]Copyright (c) 2018 by Cisco Systems, Inc., ASR9K Series\n"
        p6_xr_0 = re.compile(r'(?P<is_iosxr>(IOS XR))')

        # Time remaining: 95 seconds
        p7 = re.compile(r'^Time +remaining: +(?P<time_remaining>\d+) +seconds$')
        # System Capabilities: B, R
        # System Capabilities: not advertised
        p8 = re.compile(r'^System +Capabilities: +(?P<system>[\w ,]+)$')
        # Enabled Capabilities: R
        # Enabled Capabilities: not advertised
        p9 = re.compile(r'^Enabled +Capabilities: +(?P<enabled>[\w ,]+)$')
        # Management Address: 10.2.3.2
        p10 = re.compile(r'^Management +Address: +(?P<mgmt_address_ipv4>.+)$')
        # Management Address IPV6: not advertised
        p11 = re.compile(r'^Management +Address +IPV6: +(?P<mgmt_address_ipv6>.+)$')
        # Vlan ID: not advertised
        p12 = re.compile(r'^Vlan +ID: +(?P<vlan_id>.+)$')
        # Total entries displayed: 2
        p13 = re.compile(r'^Total +entries +displayed: +(?P<total_entries>\d+)$')

        # VRP (R) software, Version 8.80 (CE6850 V100R003C00SPC600)
        p14 = re.compile(r'(?P<custom_name>VRP .+)$')

        # customer devices
        p15 = re.compile(r'(?P<special_name>HUA.+)$')

        for line in out.splitlines():
            line = line.strip()

            # Chassis id: 000d.bdff.4f04
            # Chassis id: 39373638-3935-5A43-4A37-35303036574C
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tmp_chassis_id = group['chassis_id']
                continue

            # Port id: Gi0/0/0/1
            # Port id: PCI-E Slot 1, Port 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_id = group['port_id']
                continue
            # Local Port id: Eth1/2
            m = p3.match(line)
            if m:
                sub_dict = {}
                group = m.groupdict()
                intf = Common.convert_intf_name(group['local_port_id'])
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(intf, {})
                sub_dict.update({'chassis_id': tmp_chassis_id})
                port_dict = intf_dict.setdefault('port_id', {}).setdefault(port_id, {})
                continue

            # Port Description: null
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault('port_description', group['port_description'])
                continue

            # System Name: R2_xrv9000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                system_name = group['system_name']
                sub_dict.update({'system_name': system_name})

                port_dict.setdefault('neighbors', {}).setdefault(system_name, sub_dict)
                continue

            # System Description: Cisco IOS Software [Everest], Virtual XE
            # Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1,
            # RELEASE SOFTWARE (fc2)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'system_description': group['system_description']})

                # sets ports to contain the dictionary of port_ids
                # sets port equal to the first port in ports, which should be the only one.
                ports = intf_dict['port_id']
                port = list(ports.keys())[0]
                # detects if system description returns an IOS-XR device
                # changes the format of the interface to ensure compatibility
                xr_check = p6_xr_0.search(sub_dict['system_description'])
                if xr_check:
                    new_port = Common.convert_intf_name(port, os='iosxr')
                else:
                    new_port = Common.convert_intf_name(port)

                ports[new_port] = ports.pop(port)

                continue

            # Copyright (c) 1986-2011 by Cisco Systems, Inc.
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += group['copyright'] + '\n'
                continue

            # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
            m = p6_2.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += group['compiled_by']
                continue

            # Technical Support: http://www.cisco.com/techsupport
            m = p6_3.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += '\n' + group['technical_support'] + '\n'
                continue

            # Time remaining: 95 seconds
            m = p7.match(line)
            if m:
                sub_dict.update({'time_remaining': int(m.groupdict()['time_remaining'])})
                continue

            # System Capabilities: B, R
            # System Capabilities: not advertised
            m = p8.match(line)
            if m:
                cap_list = m.groupdict()['system'].split(',')

                if 'not advertised' in cap_list:
                    sub_dict.update({'system_capabilities': 'not advertised'})
                else:
                    cap_list = map(str.strip, cap_list)
                    cap = [self.CAPABILITY_CODES[n] for n in cap_list]
                    for item in cap:
                        cap_dict = sub_dict.setdefault('capabilities', {}).setdefault(item,
                                                                                      {})
                        cap_dict.update({'name': item})
                        cap_dict.update({'system': True})
                continue

            # Enabled Capabilities: R
            # Enabled Capabilities: not advertised
            m = p9.match(line)
            if m:
                cap_list = m.groupdict()['enabled'].split(',')
                if 'not advertised' in cap_list:
                    sub_dict.update({'enabled_capabilities': 'not advertised'})
                else:
                    cap_list = map(str.strip, cap_list)
                    cap = [self.CAPABILITY_CODES[n] for n in cap_list]
                    for item in cap:
                        cap_dict = sub_dict.setdefault('capabilities', {}).setdefault(item,
                                                                                      {})
                        cap_dict.update({'name': item})
                        cap_dict.update({'enabled': True})

                continue

            # Management Address: 10.2.3.2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'management_address_v4': group['mgmt_address_ipv4']})

                continue

            # Management Address IPV6: not advertised
            m = p11.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'management_address_v6': group['mgmt_address_ipv6']})

                continue

            # Vlan ID: not advertised
            m = p12.match(line)
            if m:
                sub_dict.update({'vlan_id': m.groupdict()['vlan_id']})
                continue

            # Total entries displayed: 2
            m = p13.match(line)
            if m:
                parsed_dict.update({'total_entries': int(
                    m.groupdict()['total_entries'])})

                continue

            # VRP (R) software, Version 8.80 (CE6850 V100R003C00SPC600)
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                sub_dict['system_description'] += '\n' + group['custom_name'] + '\n'

                continue

            # customer device
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                sub_dict['system_description'] += group['special_name'] + '\n'

        return parsed_dict


# =================================
# schema for 'show lldp traffic'
# =================================
class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {
        'counters': {
            "total_frames_received": int,  # Total frames received: 209
            "total_frames_transmitted": int,  # Total frames transmitted: 349
            "total_frames_received_in_error": int,  # Total frames received in error: 0
            "total_frames_discarded": int,  # Total frames discarded: 0
            'total_unrecognized_tlvs': int,  # Total unrecognized TLVs: 0
            'total_entries_aged': int,  # Total entries aged: 0
            Optional('total_flap_count'): int  # Total flap count: 1
        }
    }


class ShowLldpTraffic(ShowLldpTrafficSchema):
    """parser ofr show lldp traffic"""
    cli_command = 'show lldp traffic'
    exclude = ['total_frames_received', 'total_frames_transmitted']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dictionary
        parsed_dict = {}

        #     LLDP traffic statistics: 
        #
        #         Total frames transmitted: 349
        #         Total entries aged: 0
        #         Total frames received: 209
        #         Total frames received in error: 0
        #         Total frames discarded: 0
        #         Total unrecognized TLVs: 0
        p1 = re.compile(r'^(?P<pattern>[\w\s]+): +(?P<value>\d+)$')
        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                traffic = m.groupdict()
                traffic_dict = parsed_dict.setdefault('counters', {})
                traffic_key = traffic['pattern'].replace(' ', '_').lower()
                traffic_value = int(traffic['value'])
                traffic_dict.update({traffic_key: traffic_value})

                continue
        return parsed_dict

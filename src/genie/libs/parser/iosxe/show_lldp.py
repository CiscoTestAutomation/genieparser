"""show_lldp.py
   supported commands:
     *  show lldp
     *  show lldp entry *
     *  show lldp entry [<WORD>]
     *  show lldp interface [<WORD>]
     *  show lldp neighbors
     *  show lldp neighbors detail
     *  show lldp traffic
     *  show lldp errors
     *  show lldp custom-information
"""
import re

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


class ShowLldpSchema(MetaParser):
    """Schema for show lldp"""
    schema = {
        'status': str,
        'enabled': bool,
        'hello_timer': int,
        'hold_timer': int,
        'reinit_timer': int
    }


class ShowLldp(ShowLldpSchema):
    """Parser for show lldp"""

    cli_command = 'show lldp'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Status: +(?P<status>\w+)$')
        p2 = re.compile(r'^LLDP +(?P<pattern>[\w\s]+) +(?P<value>\d+) +seconds$')

        for line in out.splitlines():
            line = line.strip()
            
            # Status: ACTIVE
            m = p1.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                ret_dict['status'] = status
                ret_dict['enabled'] = True if 'active' in status else False
                continue

            # LLDP advertisements are sent every 30 seconds
            # LLDP hold time advertised is 120 seconds
            # LLDP interface reinitialisation delay is 2 seconds
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if re.search('(advertisements +are +sent +every)', group['pattern']):
                    key = 'hello_timer'
                elif re.search('(hold +time +advertised +is)', group['pattern']):
                    key = 'hold_timer'
                elif re.search('(interface +reinitialisation +delay +is)', group['pattern']):
                    key = 'reinit_timer'
                else:
                    continue
                ret_dict[key] = int(group['value'])
                continue
        return ret_dict


class ShowLldpEntrySchema(MetaParser):
    """Schema for show lldp entry [<WORD>|*]"""
    schema = {
        'total_entries': int,
        Optional('interfaces'): {
            Any(): {
                'if_name': str,
                'port_id': {
                    Any(): {
                        'neighbors': {
                            Any(): {                        
                                Optional('chassis_id'): str,
                                'port_id': str,
                                'neighbor_id': str,
                                Optional('port_description'): str,
                                Optional('system_description'): str,
                                Optional('system_name'): str,
                                'time_remaining': int,
                                Optional('capabilities'): {
                                    Any():{
                                        Optional('system'): bool,
                                        Optional('enabled'): bool,
                                        'name': str,
                                    }
                                },
                                Optional('management_address'): str,
                                Optional('auto_negotiation'): str,
                                Optional('physical_media_capabilities'): list,
                                Optional('unit_type'): int,
                                Optional('vlan_id'): int,
                            }
                        }
                    }
                }
            }
        },
        Optional('med_information'): {
            Optional('f/w_revision'): str,
            Optional('h/w_revision'): str,
            Optional('s/w_revision'): str,
            Optional('manufacturer'): str,
            Optional('model'): str,
            Optional('capabilities'): list,
            'device_type': str,
            Optional('network_policy'): {
                Any(): { # 'voice'; 'voice_signal'
                    'vlan': int, # 110
                    'tagged': bool,
                    'layer_2_priority': int,
                    'dscp': int,
                },
            },
            Optional('serial_number'): str,
            Optional('power_source'): str,
            Optional('power_priority'): str,
            Optional('wattage'): float,
            'location': str,
        }
    }


class ShowLldpEntry(ShowLldpEntrySchema):
    """Parser for show lldp entry {* | word}"""

    CAPABILITY_CODES = {'R': 'router',
                        'B': 'mac_bridge',
                        'T': 'telephone',
                        'C': 'docsis_cable_device',
                        'W': 'wlan_access_point',
                        'P': 'repeater',
                        'S': 'station_only',
                        'O': 'other'}

    cli_command = ['show lldp entry {entry}', 'show lldp entry *']

    def cli(self, entry='',output=None):
        if output is None:
            if entry:
                cmd = self.cli_command[0].format(entry=entry)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
        item = ''
        sub_dict = {}

        # ==== initial regexp pattern ====
        # Local Intf: Gi2/0/15
        p1 = re.compile(r'^Local\s+Intf:\s+(?P<intf>[\w\/\.\-]+)$')

        # Port id: Gi1/0/4
        p1_1 = re.compile(r'^Port\s+id:\s+(?P<port_id>[\S\s]+)$')

        # Chassis id:  843d.c6ff.f1b8
        # Chassis id: r2-rf2222-qwe
        p2 = re.compile(r'^Chassis\s+id:\s+(?P<chassis_id>.+?)\s*$')

        # Port Description: GigabitEthernet1/0/4
        p3 = re.compile(r'^Port\s+Description:\s+(?P<desc>[\w\/\.\-\s]+)$')

        # System Name: R5
        # System Name - not advertised
        p4 = re.compile(r'^System\s+Name(?: +-|:)\s+(?P<name>[\S\s]+)$')

        # System Description:
        p5 = re.compile(r'^System\s+Description:.*$')

        # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        # Technical Support: http://www.cisco.com/techsupport
        # Copyright (c) 1986-2011 by Cisco Systems, Inc.
        # Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S
        p5_1 = re.compile(r'^(?P<msg>(Cisco +IOS +Software|Technical Support|Copyright|Cisco IP Phone).*)$')

        # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
        # Avaya 1220 IP Deskphone, Firmware:06Q
        # IP Phone, Firmware:90234AP
        # {"SN":"SN-NR","Owner":"OWNER"}
        p5_2 = re.compile(r'^(?P<msg>(Compile|Avaya|IP Phone|{).*)$')

        # Time remaining: 112 seconds
        p6 = re.compile(r'^Time\s+remaining:\s+(?P<time_remaining>\w+)\s+seconds$')

        # System Capabilities: B,R
        p7 = re.compile(r'^System\s+Capabilities:\s+(?P<capab>[\w\,\s]+)$')

        # Enabled Capabilities: B,R
        p8 = re.compile(r'^Enabled\s+Capabilities:\s+(?P<capab>[\w\,\s]+)$')

        # Management Addresses:
        #     IP: 10.9.1.1
        # Management Addresses:
        #     IPV6: 0000:0000:0000:0000:0000:ffff:7f00:0001
        # Management Addresses - not advertised
        p9 = re.compile(r'^(IP|IPV6):\s+(?P<ip>[\w\.:]+)$')
        p9_1 = re.compile(r'^Management\s+Addresses\s+-\s+(?P<ip>not\sadvertised)$')

        # Auto Negotiation - supported, enabled
        p10 = re.compile(r'^Auto\s+Negotiation\s+\-\s+(?P<auto_negotiation>[\w\s\,]+)$')

        # Physical media capabilities:
        p11 = re.compile(r'^Physical\s+media\s+capabilities:$')

        # 1000baseT(FD)
        # 100base-TX(HD)
        # Symm, Asym Pause(FD)
        # Symm Pause(FD)
        p11_1 = re.compile(r'^(?P<physical_media_capabilities>[\S\(\s]+(HD|FD)[\)])$')

        # Media Attachment Unit type: 30
        p12 = re.compile(r'^Media\s+Attachment\s+Unit\s+type:\s+(?P<unit_type>\d+)$')

        # Vlan ID: 1
        # Note: not parsing 'not advertised since value type is int
        p13 = re.compile(r'^^Vlan\s+ID:\s+(?P<vlan_id>\d+)$')

        # Total entries displayed: 4
        p14 = re.compile(r'^Total\s+entries\s+displayed:\s+(?P<entry>\d+)$')

        # ==== MED Information patterns =====
        # MED Information:
        med_p0 = re.compile(r'^MED\s+Information:.*$')

        # F/W revision: 06Q
        # S/W revision: SCCP42.9-3-1ES27S
        # H/W revision: 12
        med_p1 = re.compile(r'^(?P<head>(H/W|F/W|S/W))\s+revision:\s+(?P<revision>\S+)$')

        # Manufacturer: Avaya-05
        med_p2 = re.compile(r'^Manufacturer:\s+(?P<manufacturer>[\S\s]+)$')

        # Model: 1220 IP Deskphone
        med_p3 = re.compile(r'^Model:\s+(?P<model>[\S\s]+)$')

        # Capabilities: NP, LI, PD, IN
        med_p4 = re.compile(r'^Capabilities:\s*(?P<capabilities>[\S\s]+)$')

        # Device type: Endpoint Class III
        med_p5 = re.compile(r'^Device\s+type:\s+(?P<device_type>[\S\s]+)$')

        # Network Policy(Voice): VLAN 110, tagged, Layer-2 priority: 5, DSCP: 46
        # Network Policy(Voice Signal): VLAN 110, tagged, Layer-2 priority: 0, DSCP: 0
        med_p6 = re.compile(r'^Network\s+Policy\(Voice(\s+(?P<voice_signal>Signal))?\):'
                            r'\s+VLAN\s+(?P<vlan>\d+),\s+(?P<tagged>tagged),\s+'
                            r'Layer-2 priority:\s+(?P<layer_2_priority>\d+),\s+DSCP:\s+(?P<dscp>\d+)$')

        # PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
        med_p7 = re.compile(r'^(?P<device_type>PD device),\s+Power\s+source:\s+(?P<power_source>\S+),\s+'
                            r'Power\s+Priority:\s+(?P<power_priority>\S+),\s+Wattage:\s+(?P<wattage>\S+)$')

        # Location - not advertised
        med_p8 = re.compile(r'^Location\s+-\s+(?P<location>[\S\s]+)$')

        # Serial number: FCH1610A5S5
        med_p9 = re.compile(r'^Serial\s+number:\s+(?P<serial_number>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Local Intf: Gi2/0/15
            m = p1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['if_name'] = intf
                sub_dict = {}
                continue

            # Chassis id:  843d.c6ff.f1b8
            m = p2.match(line)
            if m:
                sub_dict = {}
                chassis_id = m.groupdict()['chassis_id']
                sub_dict.setdefault('chassis_id', chassis_id)
                continue

            # Port id: Gi1/0/4
            m = p1_1.match(line)
            if m:
                if 'interfaces' not in ret_dict:
                    intf_dict = ret_dict.setdefault('interfaces', {}).setdefault('N/A', {})
                    intf_dict['if_name'] = 'N/A'
                port_id = Common.convert_intf_name(m.groupdict()['port_id'])
                port_dict = intf_dict.setdefault('port_id', {}). \
                    setdefault(port_id, {})
                sub_dict.setdefault('port_id', port_id)
                continue

            # Port Description: GigabitEthernet1/0/4
            m = p3.match(line)
            if m:
                sub_dict.setdefault('port_description', m.groupdict()['desc'])
                continue

            # System Name: R5
            # System Name - not advertised
            m = p4.match(line)
            if m:
                name = m.groupdict()['name']
                nei_dict = port_dict.setdefault('neighbors', {}).setdefault(name, {})
                sub_dict['system_name'] = name
                nei_dict['neighbor_id'] = name
                nei_dict.update(sub_dict)
                continue

            # System Description: 
            m = p5.match(line)
            if m:
                nei_dict.update({'system_description': ''})
                continue

            # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
            # Technical Support: http://www.cisco.com/techsupport
            # Copyright (c) 1986-2011 by Cisco Systems, Inc.
            # Cisco IP Phone 7962G,V12, SCCP42.9-3-1ES27S
            m = p5_1.match(line)
            if m:
                nei_dict['system_description'] += m.groupdict()['msg'] + '\n'
                continue

            # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
            # Avaya 1220 IP Deskphone, Firmware:06Q
            # IP Phone, Firmware:90234AP
            m = p5_2.match(line)
            if m:
                nei_dict['system_description'] += m.groupdict()['msg']
                continue

            # Time remaining: 112 seconds
            m = p6.match(line)
            if m:
                nei_dict['time_remaining'] = int(m.groupdict()['time_remaining'])
                continue

            # System Capabilities: B,R
            m = p7.match(line)
            if m:
                cap = [self.CAPABILITY_CODES[n] for n in m.groupdict()['capab'].split(',')]
                for item in cap:
                    cap_dict = nei_dict.setdefault('capabilities', {}).\
                        setdefault(item, {})
                    cap_dict['name'] = item
                    cap_dict['system'] = True
                continue

            # Enabled Capabilities: B,R
            m = p8.match(line)
            if m:
                cap = [self.CAPABILITY_CODES[n] for n in m.groupdict()['capab'].split(',')]
                for item in cap:
                    cap_dict = nei_dict.setdefault('capabilities', {}).\
                        setdefault(item, {})
                    cap_dict['name'] = item
                    cap_dict['enabled'] = True
                continue

            # Management Addresses:
            #     IP: 10.9.1.1
            # Management Addresses - not advertised
            m = p9.match(line) or p9_1.match(line)
            if m:
                nei_dict['management_address'] = m.groupdict()['ip']
                continue

            # Auto Negotiation - supported, enabled
            m = p10.match(line)
            if m:
                nei_dict['auto_negotiation'] = m.groupdict()['auto_negotiation']
                continue

            # Physical media capabilities:
            m = p11.match(line)
            if m:
                nei_dict['physical_media_capabilities'] = []
                continue

            # 1000baseT(FD)
            # 100base-TX(HD)
            # Symm, Asym Pause(FD)
            # Symm Pause(FD)
            m = p11_1.match(line)
            if m:                
                item = nei_dict.get('physical_media_capabilities', [])
                item.append(m.groupdict()['physical_media_capabilities'])
                nei_dict['physical_media_capabilities'] = item
                continue

            # Media Attachment Unit type: 30
            m = p12.match(line)
            if m:
                nei_dict['unit_type'] = int(m.groupdict()['unit_type'])
                continue

            # Vlan ID: 1
            # Note: not parsing 'not advertised since value type is int
            m = p13.match(line)
            if m:
                nei_dict['vlan_id'] = int(m.groupdict()['vlan_id'])
                continue

            # Total entries displayed: 4
            m = p14.match(line)
            if m:
                ret_dict['total_entries'] = int(m.groupdict()['entry'])
                continue

            # ==== Med Information ====
            # MED Information:
            m = med_p0.match(line)
            if m:
                med_dict = ret_dict.setdefault('med_information', {})
                continue

            # F/W revision: 06Q
            # S/W revision: SCCP42.9-3-1ES27S
            # H/W revision: 12
            m = med_p1.match(line)
            if m:
                group = m.groupdict()
                med_dict[group['head'].lower()+'_revision'] = m.groupdict()['revision']
                continue

            # Manufacturer: Avaya-05
            # Model: 1220 IP Deskphone
            # Device type: Endpoint Class III
            m = med_p2.match(line) or med_p3.match(line) or med_p5.match(line)
            if m:
                match_key = [*m.groupdict().keys()][0]
                med_dict[match_key] = m.groupdict()[match_key]
                continue

            # Capabilities: NP, LI, PD, IN
            # Capabilities:
            m = med_p4.match(line)
            if m:
                list_capabilities = m.groupdict()['capabilities'].split(', ')
                med_dict['capabilities'] = list_capabilities
                continue

            # Network Policy(Voice): VLAN 110, tagged, Layer-2 priority: 5, DSCP: 46
            # Network Policy(Voice Signal): VLAN 110, tagged, Layer-2 priority: 0, DSCP: 0
            m = med_p6.match(line)
            if m:
                group = m.groupdict()

                if group['voice_signal']:
                    voice = 'voice_signal'
                else:
                    voice = 'voice'
                voice_sub_dict = med_dict.setdefault('network_policy', {}).\
                                          setdefault(voice, {})
                if group['tagged'] == 'tagged':
                    voice_sub_dict['tagged'] = True
                else:
                    voice_sub_dict['tagged'] = False

                for k in ['layer_2_priority', 'dscp', 'vlan']:
                    voice_sub_dict[k] = int(group[k])

                continue

            # PD device, Power source: Unknown, Power Priority: High, Wattage: 6.0
            m = med_p7.match(line)
            if m:
                for k in ['device_type', 'power_source', 'power_priority']:
                    med_dict[k] = m.groupdict()[k]
                med_dict['wattage'] = float(m.groupdict()['wattage'])
                continue

            # Location - not advertised
            m = med_p8.match(line)
            if m:
                med_dict['location'] = m.groupdict()['location']
                continue

            # Serial number: FCH1610A5S5
            m = med_p9.match(line)
            if m:
                med_dict['serial_number'] = m.groupdict()['serial_number']
                continue

        return ret_dict


class ShowLldpNeighborsDetail(ShowLldpEntry):
    '''Parser for show lldp neighbors detail'''
    cli_command = 'show lldp neighbors detail'
    exclude = ['time_remaining']

    def cli(self,output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output=show_output)


class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {
        "frame_in": int,
        "frame_out": int,
        "frame_error_in": int,
        "frame_discard": int,
        "tlv_discard": int,
        'tlv_unknown': int,
        'entries_aged_out': int
    }


class ShowLldpTraffic(ShowLldpTrafficSchema):
    """Parser for show lldp traffic"""

    cli_command = 'show lldp traffic'
    exclude = ['frame_in' , 'frame_out', 'tlv_discard', 'tlv_unknown']

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<pattern>[\w\s]+): +(?P<value>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Total frames out: 20372
            # Total entries aged: 34
            # Total frames in: 13315
            # Total frames received in error: 0
            # Total frames discarded: 14
            # Total TLVs discarded: 0
            # Total TLVs unrecognized: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if re.search('(Total +frames +out)', group['pattern']):
                    key = 'frame_out'
                elif re.search('(Total +entries +aged)', group['pattern']):
                    key = 'entries_aged_out'
                elif re.search('(Total +frames +in)', group['pattern']):
                    key = 'frame_in'
                elif re.search('(Total +frames +received +in +error)', group['pattern']):
                    key = 'frame_error_in'
                elif re.search('(Total +frames +discarded)', group['pattern']):
                    key = 'frame_discard'
                elif re.search('(Total +TLVs +discarded)', group['pattern']):
                    key = 'tlv_discard'
                elif re.search('(Total +TLVs +unrecognized)', group['pattern']):
                    key = 'tlv_unknown'
                else:
                    continue
                ret_dict[key] = int(group['value'])
                continue
        return ret_dict


class ShowLldpInterfaceSchema(MetaParser):
    """Schema for show lldp interface [<WORD>]"""
    schema = {
        'interfaces': {
            Any(): {
                'tx': str,
                'rx': str,
                'tx_state': str,
                'rx_state': str,
            },
        }
    }


class ShowLldpInterface(ShowLldpInterfaceSchema):
    """Parser for show lldp interface [<WORD>]"""

    cli_command = ['show lldp interface {interface}','show lldp interface']

    def cli(self, interface='',output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\/\-\.]+):$')
        p2 = re.compile(r'^(?P<key>[\w\s]+): +(?P<value>[\w\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1/0/15
            m = p1.match(line)
            if m:
                intf_dict = ret_dict.setdefault('interfaces', {}).\
                    setdefault(m.groupdict()['intf'], {})
                continue
            
            # Tx: enabled
            # Rx: enabled
            # Tx state: IDLE
            # Rx state: WAIT FOR FRAME
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key = '_'.join(group['key'].lower().split())
                intf_dict[key] = group['value'].lower()
                continue
        return ret_dict


class ShowLldpNeighborsSchema(MetaParser):
    """
    Schema for show lldp neighbors
    """
    schema = {
        'total_entries': int,
        'interfaces': {
            Any(): {
                'port_id': {
                    Any(): {
                        'neighbors': {
                            Any(): {
                                'hold_time': int,
                                Optional('capabilities'): list,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLldpNeighbors(ShowLldpNeighborsSchema):
    """
    Parser for show lldp neighbors
    """
    CAPABILITY_CODES = {'R': 'router',
                        'B': 'mac_bridge',
                        'T': 'telephone',
                        'C': 'docsis_cable_device',
                        'W': 'wlan_access_point',
                        'P': 'repeater',
                        'S': 'station_only',
                        'O': 'other'}

    cli_command = ['show lldp neighbors']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_output = {}

        # Total entries displayed: 4
        p1 = re.compile(r'^Total\s+entries\s+displayed:\s+(?P<entry>\d+)$')

        # Device ID           Local Intf     Hold-time  Capability      Port ID
        # router               Gi1/0/52       117        R               Gi0/0/0
        # 10.10.191.107       Gi1/0/14       155        B,T             7038.eeff.572d
        # d89e.f3ff.58fe      Gi1/0/33       3070                       d89e.f3ff.58fe
        # Polycom Trio Visual+Gi2/0/28       120        T               6416.7fff.1e30

        p2 = re.compile(r'(?P<device_id>.{20})(?P<interfaces>\S+)'
                        r'\s+(?P<hold_time>\d+)\s+(?P<capabilities>[A-Z,]+)?'
                        r'\s+(?P<port_id>\S+)')

        for line in out.splitlines():
            line = line.strip()

            # Total entries displayed: 4
            m = p1.match(line)
            if m:
                parsed_output['total_entries'] = int(m.groupdict()['entry'])
                continue

            # Device ID           Local Intf     Hold-time  Capability      Port ID
            # router               Gi1/0/52       117        R               Gi0/0/0
            # 10.10.191.107       Gi1/0/14       155        B,T             7038.eeff.572d
            # d89e.f3ff.58fe      Gi1/0/33       3070                       d89e.f3ff.58fe
            m = p2.match(line)
            if m:
                group = m.groupdict()

                intf = Common.convert_intf_name(group['interfaces'])
                device_dict = parsed_output.setdefault('interfaces', {}). \
                                          setdefault(intf, {}). \
                                          setdefault('port_id', {}). \
                                          setdefault(group['port_id'], {}).\
                                          setdefault('neighbors', {}). \
                                          setdefault(group['device_id'], {})

                device_dict['hold_time'] = int(group['hold_time'])

                if group['capabilities']:
                    capabilities = list(map(lambda x: x.strip(), group['capabilities'].split(',')))
                    device_dict['capabilities'] = capabilities


            continue

        return parsed_output


class ShowLldpErrorsSchema(MetaParser):
    """
    Schema for show lldp errors
    """
    schema = {
        'memory': int,
        'encapsulation': int,
        'input_queue': int,
        'table': int
    }


class ShowLldpErrors(ShowLldpErrorsSchema):
    """
    Parser for show lldp errors
    """
    cli_command = 'show lldp errors'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = dict()

        # Total memory allocation failures: 0
        p0 = re.compile(r'^Total\s+memory\s+allocation\s+failures:\s+(?P<memory>\d+)$')

        # Total encapsulation failures: 0
        p1 = re.compile(r'^Total\s+encapsulation\s+failures:\s+(?P<encapsulation>\d+)$')

        # Total input queue overflows: 0
        p2 = re.compile(r'^Total\s+input\s+queue\s+overflows:\s+(?P<input_queue>\d+)$')

        # Total table overflows: 0
        p3 = re.compile(r'^Total\s+table\s+overflows:\s+(?P<table>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Total memory allocation failures: 0
            match = p0.match(line)
            if match:
                ret_dict['memory'] = int(match.groupdict()['memory'])
                continue

            # Total encapsulation failures: 0           
            match = p1.match(line)
            if match:
                ret_dict['encapsulation'] = int(match.groupdict()['encapsulation'])
                continue

            # Total input queue overflows: 0
            match = p2.match(line)
            if match:
                ret_dict['input_queue'] = int(match.groupdict()['input_queue'])
                continue
            
            # Total table overflows: 0
            match = p3.match(line)
            if match:
                ret_dict['table'] = int(match.groupdict()['table'])
                continue

        return ret_dict

class ShowLldpCustomInformationSchema(MetaParser):
    """Schema for show lldp custom-information"""
    schema = {
        Optional('management_vlan'): int,
        Optional('network_hash'): str,
        Optional('management_ip'): str,
        Optional('management_ipv6'): str,
        Optional('system_name'): {
           Any(): { 
               'name':str,
              },
           },
    }


class ShowLldpCustomInformation(ShowLldpCustomInformationSchema):
    """Parser for show lldp custom-information"""

    cli_command = 'show lldp custom-information'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern based on the output
        # Management VLAN: 100
        p1 = re.compile(r'Management\sVLAN: +(?P<vlan>\d+)$')
        
        # Custom  network hash: check
        p2 = re.compile(r'Custom\s*network\shash: +(?P<network_hash>\w+)$')
        
        # Management IPv4: 10.0.0.1  20.0.0.1
        p3 = re.compile(r'Management\sIP\S*: +(?P<ip_string>[\S*\s*]*)$')
        
        # Management IPv6: 10::1  20::1
        p4 = re.compile(r'Management\sIPv6: +(?P<ipv6_string>[\S*\s*]*)$')
        
        # Switch-id 1 system-name: check
        p5 = re.compile(r'Switch-id +(?P<switch_id>\d+) system-name: (?P<system_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Management VLAN: 100
            m = p1.match(line)
            if m:
                vlan = m.groupdict()['vlan']
                ret_dict['management_vlan'] = int(vlan)
                continue

            # Custom network hash: check
            m = p2.match(line)
            if m:
                network_hash = m.groupdict()['network_hash']
                ret_dict['network_hash'] = network_hash
                continue

            # Management IPv6
            m = p4.match(line)
            if m: 
                ipv6_string = m.groupdict()['ipv6_string']
                ret_dict['management_ipv6'] = ipv6_string
                continue

            # Management IPv4
            m = p3.match(line)
            if m:
                ipv4_string = m.groupdict()['ip_string']
                ret_dict['management_ip'] = ipv4_string
                continue

            # System name
            m = p5.match(line)
            if m:
                switch_id = int(m.groupdict()['switch_id'])
                system_name = m.groupdict()['system_name']
                sub_dict = ret_dict.setdefault('system_name', {}).setdefault(switch_id, {})
                sub_dict.update({'name':system_name})

                continue

        return ret_dict

# ==========================================================================================
# Parser Schema for 'show lldp neighbors <interface> detail'
# ==========================================================================================

class ShowLldpNeighborsInterfaceDetailSchema(MetaParser):
    """
    Schema for
        * 'show lldp neighbors <interface> detail'
    """
    schema = {
        Optional('interface'):{
            Any():{
                'port_id': {
                    Any(): {
                        'local_intf_service_instance': {
                            'chassis_id': str,
                            'port_id': str,
                            'port_description': str,
                            'system_name': str
                        },
                        'system_description': {
                            'cisco_ios_software': str,
                            'catalyst_l3_switch_software': str,
                            Optional('experimental_version'): str,
                            Optional('image_label'): str,
                            Optional('image_local_path'): str,
                            Optional('version'): str,
                            Optional('release_software'): str,
                            Optional('technical_support'): str,
                            'copyright': str,
                            'compiled': str,
                            'time_remaining_sec': int,
                            'system_capabilities': str,
                            'enabled_capabilities': str,
                            Optional('management_addresses'): {
                                'ip': str,
                            },
                            'auto_negotiation': str,
                            'physical_media_capabilities': {
                                int: str,
                            },
                            'media_attachment_unit_type': int,
                            'vlan_id': int,
                            'peer_source_mac': str,
                        }
                    }
                }
            }
        },
        'total_entries_displayed': int
    }

# ==========================================================================================
# Parser for 'show lldp neighbors <interface> detail'
# ==========================================================================================

class ShowLldpNeighborsInterfaceDetail(ShowLldpNeighborsInterfaceDetailSchema):
    """
    Parser for
        * 'show lldp neighbors <interface> detail'
    """
    cli_command = 'show lldp neighbors {interface} detail'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # initializing variables
        ret_dict = {}

        # Local Intf: Gi4/0/5
        p1 = re.compile(r'^Local Intf: (?P<local_intf>\S+)$')

        # Chassis id: 380e.4d9b.0580
        p2 = re.compile(r'^Chassis id: (?P<chassis_id>\S+)$')

        # Port id: Gi4/0/5
        p3 = re.compile(r'^Port id: (?P<port_id>\S+)$')

        # Port Description: GigabitEthernet4/0/5
        p4 = re.compile(r'^Port Description: (?P<port_description>\S+)$')

        # System Name: dut9404
        p5 = re.compile(r'^System Name: (?P<system_name>\S+)$')

        # Cisco IOS Software [Dublin], Catalyst L3 Switch Software (CAT9K_IOSXE), 
        # Experimental Version 17.12.20230309:084324 
        # [BLD_POLARIS_DEV_LATEST_20230309_082032:/nobackup/mcpre/s2c-build-ws 101]
        p6 = re.compile(r'^Cisco IOS Software \[(?P<ios_software>\S+)\], Catalyst L3 Switch Software \((?P<calatyst_software>\S+)\), Experimental Version (?P<exp_version>\S+) \[(?P<image_label>\S+):(?P<local_path>[\S\s]+)\]$')

        #Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), 
        # Version 16.12.4, RELEASE SOFTWARE (fc5)
        p7 = re.compile(r'^Cisco IOS Software \[(?P<ios_software>\S+)\], Catalyst L3 Switch Software \((?P<calatyst_software>\S+)\), Version (?P<version>\S+), RELEASE SOFTWARE \((?P<release_software>\S+)\)$')

        #Technical Support: http://www.cisco.com/techsupport
        p8 = re.compile(r'^Technical Support: (?P<technical_support>\S+)$')

        # Copyright (c) 1986-2023 by Cisco Systems, Inc.
        p9 = re.compile(r'^Copyright \(c\) (?P<copyright>[\S\s]+)$')

        # Compiled Thu 09-Mar
        p10 = re.compile(r'^Compiled (?P<compiled>[\S\s]+)$')

        # Time remaining: 109 seconds
        p11 = re.compile(r'^Time remaining: (?P<time>\d+) seconds$')
        
        # System Capabilities: B,R
        p12 = re.compile(r'^System Capabilities: (?P<system_capabilities>\S+)$')

        # Enabled Capabilities: B,R
        p13 = re.compile(r'^Enabled Capabilities: (?P<enabled_capabilities>\S+)$')

        # IP: 172.21.227.230
        p14 = re.compile(r'^IP: (?P<ip>\S+)$')

        # Auto Negotiation - supported, enabled
        p15 = re.compile(r'^Auto Negotiation - (?P<auto_negotiation>[\S\s]+)$')

        # 1000baseT(FD)
        # 100base-TX(FD)
        p16 = re.compile(r'^(?P<media_capabilities>.*base.*|.*un.*)$')

        # Media Attachment Unit type: 30
        p17 = re.compile(r'^Media Attachment Unit type: (?P<media_unit_type>\d+)$')

        # Vlan ID: 1
        p18 = re.compile(r'^Vlan ID: (?P<vlan_id>\d+)$')

        # Peer Source MAC: d477.989b.79c4
        p19 = re.compile(r'^Peer Source MAC: (?P<peer_source_mac>\S+)$')

        # Total entries displayed: 8
        p20 = re.compile(r'^Total entries displayed: (?P<total_entries>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Local Intf: Gi4/0/5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface',{}).setdefault(Common.convert_intf_name(group['local_intf']),{})
                continue

            # Chassis id: 380e.4d9b.0580
            m = p2.match(line)
            if m:
                group = m.groupdict()
                chassis_id = group['chassis_id']
                continue

            # Port id: Gi4/0/5
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_dict = root_dict.setdefault('port_id',{}).setdefault(group['port_id'],{})
                intf_dict = port_dict.setdefault('local_intf_service_instance',{})
                intf_dict['port_id'] = group['port_id']
                intf_dict['chassis_id'] = chassis_id
                counter = 1
                continue

            # Port Description: GigabitEthernet4/0/5
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict['port_description'] = group['port_description']
                continue

            # System Name: dut9404
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict['system_name'] = group['system_name']
                continue

            # Cisco IOS Software [Dublin], Catalyst L3 Switch Software (CAT9K_IOSXE), 
            # Experimental Version 17.12.20230309:084324 
            # [BLD_POLARIS_DEV_LATEST_20230309_082032:/nobackup/mcpre/s2c-build-ws 101]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                desc_dict = port_dict.setdefault('system_description',{})
                desc_dict['cisco_ios_software'] = group['ios_software']
                desc_dict['catalyst_l3_switch_software'] = group['calatyst_software']
                desc_dict['experimental_version'] = group['exp_version']
                desc_dict['image_label'] = group['image_label']
                desc_dict['image_local_path'] = group['local_path']
                continue

            # Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_IOSXE), 
            # Version 16.12.4, RELEASE SOFTWARE (fc5)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                desc_dict = port_dict.setdefault('system_description',{})
                desc_dict['cisco_ios_software'] = group['ios_software']
                desc_dict['catalyst_l3_switch_software'] = group['calatyst_software']
                desc_dict['version'] = group['version']
                desc_dict['release_software'] = group['release_software']
                continue

            # Technical Support: http://www.cisco.com/techsupport
            m = p8.match(line)
            if m:
                group = m.groupdict()
                desc_dict['technical_support'] = group['technical_support']
                continue

            # Copyright (c) 1986-2023 by Cisco Systems, Inc.
            m = p9.match(line)
            if m:
                group = m.groupdict()
                desc_dict['copyright'] = group['copyright']
                continue

            # Compiled Thu 09-Mar
            m = p10.match(line)
            if m:
                group = m.groupdict()
                desc_dict['compiled'] = group['compiled']
                continue

            # Time remaining: 109 seconds
            m = p11.match(line)
            if m:
                group = m.groupdict()
                desc_dict['time_remaining_sec'] = int(group['time'])
                continue

            # System Capabilities: B,R
            m = p12.match(line)
            if m:
                group = m.groupdict()
                desc_dict['system_capabilities'] = group['system_capabilities']
                continue

            # Enabled Capabilities: B,R
            m = p13.match(line)
            if m:
                group = m.groupdict()
                desc_dict['enabled_capabilities'] = group['enabled_capabilities']
                continue

            # IP: 172.21.227.230
            m = p14.match(line)
            if m:
                group = m.groupdict()
                mngt_dict = desc_dict.setdefault('management_addresses',{})
                mngt_dict['ip'] = group['ip']
                continue

            # Auto Negotiation - supported, enabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                desc_dict['auto_negotiation'] = group['auto_negotiation']
                continue

            # 1000baseT(FD)
            # 100base-TX(FD)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                media_dict = desc_dict.setdefault('physical_media_capabilities',{})
                media_dict[counter] = group['media_capabilities']
                counter += 1
                continue

            # Media Attachment Unit type: 30
            m = p17.match(line)
            if m:
                group = m.groupdict()
                desc_dict['media_attachment_unit_type'] = int(group['media_unit_type'])
                continue

            # Vlan ID: 1
            m = p18.match(line)
            if m:
                group = m.groupdict()
                desc_dict['vlan_id'] = int(group['vlan_id'])
                continue

            # Peer Source MAC: d477.989b.79c4
            m = p19.match(line)
            if m:
                group = m.groupdict()
                desc_dict['peer_source_mac'] = group['peer_source_mac']
                continue

            # Total entries displayed: 8
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_entries_displayed'] = int(group['total_entries'])
                continue

        return ret_dict

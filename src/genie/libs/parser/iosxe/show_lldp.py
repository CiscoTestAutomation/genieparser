"""show_lldp.py
   supported commands:
     *  show lldp
     *  show lldp entry *
     *  show lldp entry [<WORD>]
     *  show lldp interface [<WORD>]
     *  show lldp neighbors
     *  show lldp neighbors detail
     *  show lldp traffic
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
                                'chassis_id': str,
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

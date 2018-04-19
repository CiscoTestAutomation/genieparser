"""show_spanning_tree.py
   supported commands:
     *  show lldp
     *  show lldp entry [<WORD>|*]
     *  show lldp interface [<WORD>]
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

    def cli(self):
         # get output from device
        out = self.device.execute('show lldp')

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
                        Optional('vlan_id'): int
                    }
                }
            }
        }
    }


class ShowLldpEntry(ShowLldpEntrySchema):
    """Parser for show lldp entry [<WORD>|*]"""

    CAPABILITY_CODES = {'R': 'router',
                        'B': 'mac_bridge',
                        'T': 'telephone',
                        'C': 'docsis_cable_device',
                        'W': 'wlan_access_point',
                        'P': 'repeater',
                        'S': 'station_only',
                        'O': 'other'}

    def cli(self, entry='*'):
        # get output from device
        if hasattr(self, 'CMD'):
            out = self.device.execute(self.CMD)
        else:
            out = self.device.execute('show lldp entry {}'.format(entry))

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Local +Intf: +(?P<intf>[\w\/\.\-]+)$')
        p1_1 = re.compile(r'^Port +id: +(?P<port_id>[\w\/\.\-]+)$')

        p2 = re.compile(r'^Chassis +id: +(?P<chassis_id>[\w\.]+)$')

        p3 = re.compile(r'^Port +Description: +(?P<desc>[\w\/\.\-]+)$')

        p4 = re.compile(r'^System +Name: +(?P<name>\w+)$')

        p5 = re.compile(r'^System +Description:$')
        p5_1 = re.compile(r'^(?P<msg>Cisco +IOS +Software.*)$')
        p5_2 = re.compile(r'^(?P<msg>Copyright.*)$')
        p5_3 = re.compile(r'^(?P<msg>Compile.*)$')
        p5_4 = re.compile(r'^(?P<msg>Technical Support.*)$')

        p6 = re.compile(r'^Time +remaining: +(?P<time_remaining>\w+) +seconds$')

        p7 = re.compile(r'^System +Capabilities: +(?P<capab>[\w\,\s]+)$')

        p8 = re.compile(r'^Enabled +Capabilities: +(?P<capab>[\w\,\s]+)$')

        p9 = re.compile(r'^IP: +(?P<ip>[\w\.]+)$')

        p10 = re.compile(r'^Auto +Negotiation +\- +(?P<auto_negotiation>[\w\s\,]+)$')

        p11 = re.compile(r'^Physical +media +capabilities:$')
        p11_1 = re.compile(r'^(?P<physical_media_capabilities>\d+base[\w\-\(\)]+)$')

        p12 = re.compile(r'^Media +Attachment +Unit +type: +(?P<unit_type>\d+)$')

        p13 = re.compile(r'^Vlan +ID: +(?P<vlan_id>\d+)$')

        p14 = re.compile(r'^Total +entries +displayed: +(?P<entry>\d+)$')

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

            # Chassis id: 843d.c638.b980
            m = p2.match(line)
            if m:
                sub_dict = {}
                chassis_id = m.groupdict()['chassis_id']
                sub_dict.setdefault('chassis_id', chassis_id)
                continue

            # Port id: Gi1/0/4
            m = p1_1.match(line)
            if m:
                sub_dict.setdefault('port_id',
                    Common.convert_intf_name(m.groupdict()['port_id']))
                continue

            # Port Description: GigabitEthernet1/0/4
            m = p3.match(line)
            if m:
                sub_dict.setdefault('port_description', m.groupdict()['desc'])
                continue

            # System Name: R5
            m = p4.match(line)
            if m:
                name = m.groupdict()['name']
                sub_dict['system_name'] = name
                continue


            # System Description: 
            m = p5.match(line)
            if m:
                sub_dict['system_description'] = ''
                continue

            # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
            m = p5_1.match(line)
            if m:
                item = sub_dict.get('system_description', '') + m.groupdict()['msg'] + '\n'
                sub_dict['system_description'] = item
                continue

            # Technical Support: http://www.cisco.com/techsupport 
            m = p5_4.match(line)
            if m:
                item = sub_dict.get('system_description', '') + m.groupdict()['msg'] + '\n'
                sub_dict['system_description'] = item
                continue

            # Copyright (c) 1986-2011 by Cisco Systems, Inc.
            m = p5_2.match(line)
            if m:
                item = sub_dict.get('system_description', '') + m.groupdict()['msg'] + '\n'
                sub_dict['system_description'] = item
                continue

            # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
            m = p5_3.match(line)
            if m:
                item = sub_dict.get('system_description', '') + m.groupdict()['msg']
                sub_dict['system_description'] = item
                continue

            # Time remaining: 112 seconds
            m = p6.match(line)
            if m:
                nei = sub_dict.get('system_name', '') if sub_dict.get('system_name', '') else \
                    sub_dict.get('chassis_id', '')
                nei_dict = intf_dict.setdefault('neighbors', {}).setdefault(nei, {})
                nei_dict.update(sub_dict)
                nei_dict['time_remaining'] = int(m.groupdict()['time_remaining'])
                nei_dict['neighbor_id'] = nei
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
            #     IP: 1.2.1.1
            m = p9.match(line)
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

            #     1000baseT(FD)
            #     100base-TX(HD)
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
            m = p13.match(line)
            if m:
                nei_dict['vlan_id'] = int(m.groupdict()['vlan_id'])
                continue

            # Total entries displayed: 4
            m = p14.match(line)
            if m:
                ret_dict['total_entries'] = int(m.groupdict()['entry'])
                continue

        return ret_dict


class ShowLldpNeighborsDetail(ShowLldpEntry):
    '''Parser for show lldp neighbors detail'''
    CMD = 'show lldp neighbors detail'


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

    def cli(self):
         # get output from device
        out = self.device.execute('show lldp traffic')

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

    def cli(self, interface=''):
         # get output from device
        out = self.device.execute('show lldp interface') if not interface else \
              self.device.execute('show lldp interface {}'.format(interface))

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


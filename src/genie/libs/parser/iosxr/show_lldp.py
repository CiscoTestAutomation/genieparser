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
        p2 = re.compile(r'^LLDP( +advertisements +are +sent +every +'
            '(?P<hello_timer>\d+))?( +hold +time +advertised +is +'
            '(?P<hold_timer>\d+))?( +interface +reinitialisation '
            '+delay +is +(?P<reinit_timer>\d+))? +seconds$')

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
                ret_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowLldpEntrySchema(MetaParser):
    """Schema for show lldp entry [<WORD>|*]"""
    schema = {
        'total_entries': int,
        Optional('interfaces'): {
            Any(): {
                'neighbors': {
                    Any(): {                        
                        'chassis_id': str,
                        'port_id': str,
                        'port_description': str,
                        'system_name': str,
                        'system_description': str,
                        'technical_support': str,
                        'copyright': str,
                        'compiled_by': str,
                        'time_remaining': int,
                        'hold_time': int,
                        'capabilities': {
                            Any():{
                                'system': bool,
                                'enabled': bool
                            }
                        },
                        'management_address': str,
                    }
                }
            }
        }
    }

class ShowLldpEntry(ShowLldpEntrySchema):
    """Parser for show lldp entry [<WORD>|*]"""

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

    cli_command = 'show lldp entry {entry}'

    def cli(self, entry='*',output=None):
    	if output is None:
            # get output from device
            if hasattr(self, 'CMD'):
                out = self.device.execute(self.CMD)
            else:
                out = self.device.execute(self.cli_command.format(entry=entry))
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
        # Local Interface: GigabitEthernet0/0/0/0
        p1 = re.compile(r'^Local +Interface: +(?P<local_interface>[\w\/\.\-]+)$')
        # Chassis id: 001e.49f7.2c00
        p2 = re.compile(r'^Chassis +id: +(?P<chassis_id>[\w\.]+)$')
        # Port id: Gi2
        p3 = re.compile(r'^Port +id: +(?P<port_id>[\w\/\.\-]+)$')
        # Port Description: GigabitEthernet2
        p4 = re.compile(r'^Port +Description: +(?P<port_description>[\w\/\.\-]+)$')
        # System Name: R1_csr1000v.openstacklocal
        p5 = re.compile(r'System +Name: +(?P<system_name>[\w\.]+)$')
        # System Description: 
        p6 = re.compile(r'^System +Description:$')
        # Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)
        # Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)
        p7 = re.compile(r'^(?P<msg>Cisco +((IOS +Software +\[Everest\])|(Nexus +Operating +System))[\S\s]+)$')
        # Copyright (c) 1986-2017 by Cisco Systems, Inc.
        p8 = re.compile(r'^Copyright +\(c\) +(?P<copyright>)$')
        # Compiled Sat 22-Jul-17 05:51 by 
        p9 = re.compile(r'Compiled +\w{3} +\d{1,2}\-\w{3}\-\d{1,2} +\d{2}:\d{2} +by +(?P<compiled_by>[\S\s]+)$ ')
        # Technical Support: http://www.cisco.com/techsupport
        p10 = re.compile(r'^Technical Support: +(?P<technical_support>[\S\s])$')
        # Time remaining: 117 seconds
        p11 = re.compile(r'Time +remaining: +(?P<time_remaining>\d+) +seconds$')
        # Hold Time: 120 seconds
        p12 = re.compile(r'Hold +Time: +(?P<hold_time>\d+) +seconds$')
        # System Capabilities: B,R
        p13 = re.compile(r'System +Capabilities: +(?P<system>[\w+,]+)$')
        # Enabled Capabilities: R
        p14 = re.compile(r'Enabled +Capabilities: +(?P<enabled>[\w+,]+)$')
        # IPv4 address: 10.1.2.1
        p15 = re.compile(r'IPv4 +address: +(?P<address>[\d\.]+)$')
        # Total entries displayed: 2
        p16 = re.compile(r'Total +entries +displayed: +(?P<total_entries>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Local Interface: GigabitEthernet0/0/0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['local_interface'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                sub_dict = {}
                continue
            
            # Chassis id: 001e.49f7.2c00
            m = p2.match(line)
            if m:
                sub_dict = {}
                group = m.groupdict()
                sub_dict.setdefault('chassis_id', group['chassis_id'])
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
            m = p6.match(line)
            if m:
                item = m.groupdict()['msg']
                sub_dict['system_description'] = item
                continue

            # Technical Support: http://www.cisco.com/techsupport 
            m = p7.match(line)
            if m:
                item = m.groupdict()['msg']
                sub_dict['technical_support'] = item
                continue

            # Copyright (c) 1986-2011 by Cisco Systems, Inc.
            m = p8.match(line)
            if m:
                item = m.groupdict()['msg']
                sub_dict['copyright'] = item
                continue

            # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
            m = p9.match(line)
            if m:
                item = m.groupdict()['msg']
                sub_dict['compiled_by'] = item
                continue

            


class ShowLldpNeighborsDetail(ShowLldpEntry):
    '''Parser for show lldp neighbors detail'''
    CMD = 'show lldp neighbors detail'

class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {}

class ShowLldpTraffic(ShowLldpTrafficSchema):
    """Parser for show lldp traffic"""

    cli_command = 'show lldp traffic'

    def cli(self,output=None):
    	ret_dict = {}
    	return ret_dict

class ShowLldpInterfaceSchema(MetaParser):
    """Schema for show lldp interface [<WORD>]"""
    schema = {}

class ShowLldpInterface(ShowLldpInterfaceSchema):
    """Parser for show lldp interface [<WORD>]"""

    cli_command = ['show lldp interface {interface}','show lldp interface']

    def cli(self, interface='',output=None):

    	ret_dict = {}
    	return ret_dict
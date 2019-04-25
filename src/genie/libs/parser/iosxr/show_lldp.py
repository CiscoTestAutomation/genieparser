"""show_spanning_tree.py
   supported commands:
     *  show lldp
     *  show lldp entry *
     *  show lldp interface
     *  show lldp neighbors detail
     *  show lldp traffic
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowLldpSchema(MetaParser):
    """Schema for show lldp"""
    schema = {
        'status': str,
        'enabled': bool,
        'hello_timer': int,
        'hold_timer': int,
        'reinit_delay': int
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
        # Status: ACTIVE
        p1 = re.compile(r'^Status: +(?P<status>\w+)$')
        # LLDP advertisements are sent every 30 seconds
        # LLDP hold time advertised is 120 seconds
        # LLDP interface reinitialisation delay is 2 seconds
        p2 = re.compile(r'^LLDP( +advertisements +are +sent +every +'
            '(?P<hello_timer>\d+))?( +hold +time +advertised +is +'
            '(?P<hold_timer>\d+))?( +interface +reinitialisation '
            '+delay +is +(?P<reinit_delay>\d+))? +seconds$')

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
    """Schema for show lldp entry *"""
    schema = {
        'total_entries': int,
        'interfaces': {
            Any(): {
                'port_id': {
                    Any(): {
                        'neighbors': {
                            Any(): {                        
                                'chassis_id': str,
                                'port_description': str,
                                'system_name': str,
                                'system_description': str,
                                'time_remaining': int,
                                'neighbor_id': str,
                                'hold_time': int,
                                'capabilities': {
                                    Any():{
                                        Optional('system'): bool,
                                        Optional('enabled'): bool
                                    }
                                },
                                Optional('management_address'): str,
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLldpEntry(ShowLldpEntrySchema):
    """Parser for show lldp entry *"""

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

    cli_command = 'show lldp entry *'

    def cli(self, cmd='', output=None):
        if output is None:
            # get output from device
            if cmd:
                out = self.device.execute(cmd)
            else:
                out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
        description_found = False

        # Local Interface: GigabitEthernet0/0/0/0
        p1 = re.compile(r'^Local +Interface: +(?P<local_interface>\S+)$')
        # Chassis id: 001e.49f7.2c00
        p2 = re.compile(r'^Chassis +id: +(?P<chassis_id>[\w\.]+)$')
        # Port id: Gi2
        p3 = re.compile(r'^Port +id: +(?P<port_id>\S+)$')
        # Port Description: GigabitEthernet2
        p4 = re.compile(r'^Port +Description: +(?P<port_description>\S+)$')
        # System Name: R1_csr1000v.openstacklocal
        p5 = re.compile(r'System +Name: +(?P<system_name>\S+)$')
        # System Description: 
        p6 = re.compile(r'^System +Description:$')
        # Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)
        # Cisco Nexus Operating System (NX-OS) Software 7.0(3)I7(1)
        p7 = re.compile(r'^(?P<system_description>Cisco +[\S\s]+)$')
        # Copyright (c) 1986-2017 by Cisco Systems, Inc.
        p8 = re.compile(r'^(?P<copyright>Copyright +\(c\) +[\S\s]+)$')
        # Compiled Sat 22-Jul-17 05:51 by 
        p9 = re.compile(r'^(?P<compiled_by>Compiled +[\S\s]+)$')
        # Technical Support: http://www.cisco.com/techsupport
        p10 = re.compile(r'^(?P<technical_support>(Technical|TAC) (S|s)upport: +[\S\s]+)$')
        # Time remaining: 117 seconds
        p11 = re.compile(r'Time +remaining: +(?P<time_remaining>\d+) +seconds$')
        # Hold Time: 120 seconds
        p12 = re.compile(r'Hold +Time: +(?P<hold_time>\d+) +seconds$')
        # System Capabilities: B,R
        p13 = re.compile(r'System +Capabilities: +(?P<system>[\w+,]+)$')
        # Enabled Capabilities: R
        p14 = re.compile(r'Enabled +Capabilities: +(?P<enabled>[\w+,]+)$')
        # IPv4 address: 10.1.2.1
        p15 = re.compile(r'IPv4 +address: +(?P<management_address>[\d\.]+)$')
        # Total entries displayed: 2
        p16 = re.compile(r'Total +entries +displayed: +(?P<total_entries>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Local Interface: GigabitEthernet0/0/0/0
            m = p1.match(line)
            if m:
                sub_dict = {}
                group = m.groupdict()
                intf = Common.convert_intf_name(group['local_interface'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                continue
            
            # Chassis id: 001e.49f7.2c00
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'chassis_id': group['chassis_id']})
                continue
            
            # Port id: Gi1/0/4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_id = Common.convert_intf_name(group['port_id'])
                port_dict = intf_dict.setdefault('port_id', {}). \
                    setdefault(port_id, {})
                
                continue

            # Port Description: GigabitEthernet1/0/4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault('port_description', group['port_description'])
                continue

            # System Name: R5
            m = p5.match(line)
            if m:
                group = m.groupdict()
                system_name = group['system_name']
                sub_dict.update({'system_name': system_name})
                sub_dict.update({'neighbor_id' : system_name})
                nei_dict = port_dict.setdefault('neighbors', {}).setdefault(system_name, sub_dict)
                continue

            # System Description: 
            m = p6.match(line)
            if m:
                description_found = True
                sub_dict['system_description'] = ''
                continue

            # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
            m = p7.match(line)
            if m:
                if description_found:
                    group = m.groupdict()
                    sub_dict['system_description'] = group['system_description'] + '\n'
                continue

            # Copyright (c) 1986-2011 by Cisco Systems, Inc.
            m = p8.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += group['copyright'] + '\n'
                continue

            # Compiled Thu 21-Jul-11 01:23 by prod_rel_team
            m = p9.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += group['compiled_by']
                continue

            # Technical Support: http://www.cisco.com/techsupport 
            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_dict['system_description'] += group['technical_support'] + '\n'
                continue

            # Time remaining: 112 seconds
            m = p11.match(line)
            if m:
                sub_dict['time_remaining'] = int(m.groupdict()['time_remaining'])
                continue

            # Hold Time: 120 seconds
            m = p12.match(line)
            if m:
                group = m.groupdict()
                sub_dict['hold_time'] = int(group['hold_time'])
                continue

            # System Capabilities: B,R
            m = p13.match(line)
            if m:
                cap = [self.CAPABILITY_CODES[n] for n in m.groupdict()['system'].split(',')]
                for item in cap:
                    cap_dict = sub_dict.setdefault('capabilities', {}).\
                        setdefault(item, {})
                    cap_dict['system'] = True
                continue

            # Enabled Capabilities: B,R
            m = p14.match(line)
            if m:
                cap = [self.CAPABILITY_CODES[n] for n in m.groupdict()['enabled'].split(',')]
                for item in cap:
                    cap_dict = sub_dict.setdefault('capabilities', {}).\
                        setdefault(item, {})
                    cap_dict['enabled'] = True
                continue   

            # IPv4 address: 10.1.2.1
            m = p15.match(line)
            if m:
                sub_dict['management_address'] = m.groupdict()['management_address']
                continue  

            # Total entries displayed: 2
            m = p16.match(line)
            if m:
                ret_dict['total_entries'] = int(m.groupdict()['total_entries'])
                continue  
        return ret_dict     


class ShowLldpNeighborsDetail(ShowLldpEntry):
    '''Parser for show lldp neighbors detail'''
    cli_command = 'show lldp neighbors detail'

    def cli(self, output=None):
    	return super().cli(cmd=self.cli_command, output=output)

class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {
    	"counters": {
	        "frame_in": int,
	        "frame_out": int,
	        "frame_error_in": int,
	        "frame_discard": int,
	        "tlv_discard": int,
	        'tlv_unknown': int,
	        'entries_aged_out': int
        }
    }

class ShowLldpTraffic(ShowLldpTrafficSchema):
    """Parser for show lldp traffic"""

    cli_command = 'show lldp traffic'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

    	# initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Total frames out: 588
        # Total frames in: 399
        # Total frames received in error: 0
        # Total frames discarded: 0
        p1 = re.compile(r'^Total +frames +(in: +(?P<frame_in>\d+))?(out: +'
            '(?P<frame_out>\d+))?(received +in +error: +(?P<frame_error_in>'
            '\d+))?(discarded: +(?P<frame_discard>\d+))?$')

        # Total entries aged: 0
        p2 = re.compile(r'Total +entries +aged: +(?P<entries_aged_out>\d+)$')

        # Total TLVs discarded: 119
        # Total TLVs unrecognized: 119
        p3 = re.compile(r'Total +TLVs +(discarded: +(?P<tlv_discard>\d+))?'
            '(unrecognized: +(?P<tlv_unknown>\d+))?')

        for line in out.splitlines():
            line = line.strip()

            # Total frames out: 588
	        # Total frames in: 399
	        # Total frames received in error: 0
	        # Total frames discarded: 0
            m = p1.match(line)
            if m:
            	counters = ret_dict.setdefault('counters', {})
            	group = m.groupdict()
            	counters.update({k:int(v) for k, v in group.items() if v is not None})

            # Total entries aged: 0
            m = p2.match(line)
            if m:
            	counters = ret_dict.setdefault('counters', {})
            	group = m.groupdict()
            	counters.update({k:int(v) for k, v in group.items() if v is not None})

            # Total TLVs discarded: 119
        	# Total TLVs unrecognized: 119
            m = p3.match(line)
            if m:
            	counters = ret_dict.setdefault('counters', {})
            	group = m.groupdict()
            	counters.update({k:int(v) for k, v in group.items() if v is not None})
        
        return ret_dict

class ShowLldpInterfaceSchema(MetaParser):
    """Schema for show lldp interface"""
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
    """Parser for show lldp interface"""

    cli_command = 'show lldp interface'

    def cli(self, interface='',output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
    	# initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # GigabitEthernet0/0/0/0:
        p1 = re.compile(r'^(?P<interface>[\w\/\-\.]+):$')
        # Tx: enabled
        # Rx: enabled
        # Tx state: IDLE
        # Rx state: WAIT FOR FRAME
        p2 = re.compile(r'^(Tx: (?P<tx>\w+))?(Rx: (?P<rx>\w+))?(Tx +state: +'
            '(?P<tx_state>\w+))?(Rx +state: +(?P<rx_state>[\w ]+))?$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue
            # GigabitEthernet1/0/15
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})
                continue
            
            # Tx: enabled
            # Rx: enabled
            # Tx state: IDLE
            # Rx state: WAIT FOR FRAME
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({k:v.lower() for k, v in group.items() if v is not None})
                continue
        
        return ret_dict
""" show_hsrp_statistics.py

IOSXR parsers for the following show commands:
    * show hsrp statistics
    * show hsrp {interface} statistics
    * show hsrp {interface} {group_number} statistics
    * show hsrp status
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

class ShowHsrpStatisticsSchema(MetaParser):
    ''' Schema for commands:
        * show hsrp statistics
    '''
    schema = {
        'hsrp': {
            Any(): {
                'protocol': {
                    'active': int,
                    'standby': int,
                    'speak': int,
                    'listen': int,
                    'learn': int,
                    'init': int,
                },
                'packets_sent': {
                    'total_sent': int,
                    'hello': int,					
                    'resign': int,
                    'coup': int,
                    'adver': int,
                },
                'valid_packets_received': {
                    'total_received': int,
                    'hello': int,
                    'resign': int,
                    'coup': int,
                    'adver': int,
                },
                'invalid_packets_received': {
                    'total_invalid_received': int,
                    'too_long': int,
                    'too_short': int,
                    'mismatching_unsupported_versions': int,
                    'invalid_opcode': int,
                    'unknown_group': int,
                    'inoperational_group': int,
                    'conflicting_source_ip': int,
                    'failed_authentication': int,
                    'invalid_hello_time': int,
                    'mismatching_virtual_ip': int,
                },
            }
        }
    }


class ShowHsrpStatistics(ShowHsrpStatisticsSchema):
    ''' Parser for commands:
        * show hsrp statistics
    '''
    cli_command = [ 
            'show hsrp statistics',
            'show hsrp {interface} statistics',
            'show hsrp {interface} {group_number} statistics'
    ]
    def cli(self, interface=None, group_number=None, output=None):

        if output is None:
            if interface and not group_number: 
                cmd = self.cli_command[1].format(interface=interface)
            elif interface and group_number:
                cmd = self.cli_command[2].format(interface=interface,group_number=group_number)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
 
        # Protocol:
        r1 = re.compile(r'(?P<protocol>Protocol):')

        # Transitions to Active 2
        r2 = re.compile(r'Transitions +to +Active: +(?P<active>\d+)')

        # Transitions to Standby 2
        r3 = re.compile(r'Transitions +to +Standby: +(?P<standby>\d+)')

        # Transitions to Speak 0
        r4 = re.compile(r'Transitions +to +Speak: +(?P<speak>\d+)')

        # Transitions to Listen 2
        r5 = re.compile(r'Transitions +to +Listen: +(?P<listen>\d+)')


        # Transitions to Learn 0
        r6 = re.compile(r'Transitions +to +Learn: +(?P<learn>\d+)')

        # Transitions to Init 0
        r7 = re.compile(r'Transitions +to\s+Init: +(?P<init>\d+)')

        # Packets Sent: 12
        r8 = re.compile(r'(?P<packets_sent>Packets Sent): +(?P<total_sent>\d+)')

        # Hello: 7
        r9 = re.compile(r'Hello: +(?P<hello>\d+)')

        # Resign: 0 
        r10 = re.compile(r'Resign: +(?P<resign>\d+)')

        # Coup: 2
        r11 = re.compile(r'Coup: +(?P<coup>\d+)')

        # Adver: 3 
        r12 = re.compile(r'Adver: +(?P<adver>\d+)')

        # Valid Packets Received: 13
        r13 = re.compile(r'Valid Packets Received: +(?P<total_received>\d+)') 
   
        # Invalid Packets Received: 0
        r14 = re.compile(r'(?P<invalid_packets_received>Invalid Packets Received:)'
                        r' +(?P<total_invalid_received>\d+)')
        # Too long: 0
        r15 = re.compile(r'Too long: +(?P<too_long>\d+)')

        # Too short: 0 
        r16 = re.compile(r'Too short: +(?P<too_short>\d+)')

        # Mismatching/unsupported versions: 0
        r17 = re.compile(r'Mismatching\/unsupported versions:'
                        r' +(?P<mismatching_unsupported_versions>\d+)')

        # Invalid opcode: 0
        r18 = re.compile(r'Invalid opcode: +(?P<invalid_opcode>\d+)') 

        # Unknown group: 0
        r19 = re.compile(r'Unknown group: +(?P<unknown_group>\d+)')

        # Inoperational group: 0
        r20 = re.compile(r'Inoperational group: +(?P<inoperational_group>\d+)') 

        # Conflicting Source IP: 0
        r21 = re.compile(r'Conflicting Source IP: +(?P<conflicting_source_ip>\d+)') 

        # Failed Authentication: 2
        r22 = re.compile(r'Failed Authentication: +(?P<failed_authentication>\d+)') 

        # Invalid Hello Time: 0
        r23 = re.compile(r'Invalid Hello Time: +(?P<invalid_hello_time>\d+)')

        # Mismatching Virtual IP: 0
        r24 = re.compile(r'Mismatching Virtual IP: +(?P<mismatching_virtual_ip>\d+)')

        parsed_dict = {} 
        vrf = 'default' 

        for line in out.splitlines():

            line = line.strip()

            #Protocol: 
            m = r1.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = parsed_dict.setdefault('hsrp', {}).setdefault('statistics', {})
                protocol_dict = statistics_dict.setdefault('protocol', {})
                continue

            # Transitions to Active 2
            m = r2.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['active'] = int(group['active'])
                continue

            # Transitions to Standby 2				
            m = r3.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['standby'] = int(group['standby'])
                continue

            # Transitions to Speak 0
            m = r4.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['speak'] = int(group['speak'])
                continue

            # Transitions to Listen 2
            m = r5.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['listen'] = int(group['listen'])
                continue

            #Transitions to Learn 0
            m = r6.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['learn'] = int(group['learn'])
                continue

            # Transitions to Init 0
            m = r7.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['init'] = int(group['init'])
                continue

            # Packets Sent: 12
            m = r8.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict = statistics_dict.setdefault('packets_sent', {})
                packets_sent_rec_dict['total_sent'] = int(group['total_sent'])
                continue

            # Valid Packets Received: 13
            m = r13.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict = statistics_dict.setdefault('valid_packets_received', {})
                packets_sent_rec_dict['total_received'] = int(group['total_received'])
                continue

            # Transitions to Learn 0
            m = r9.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict['hello'] = int(group['hello'])
                continue

            # Resign: 0	
            m = r10.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict['resign'] = int(group['resign'])
                continue

            # Coup: 2
            m = r11.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict['coup'] = int(group['coup'])
                continue

            # Adver: 3
            m = r12.match(line)
            if m:
                group = m.groupdict()
                packets_sent_rec_dict['adver'] = int(group['adver'])
                continue

            # Invalid packets received: 0
            m = r14.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_received_dict = statistics_dict.setdefault('invalid_packets_received', {})
                invalid_packets_received_dict['total_invalid_received'] = int(group['total_invalid_received'])
                continue
        
            # Too long: 0		
            m = r15.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['too_long'] = int(group['too_long'])
                continue
        
            # Too short: 0 		
            m = r16.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['too_short'] = int(group['too_short'])
                continue
        
            # Mismatching/unsupported versions: 0
            m = r17.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_received_dict['mismatching_unsupported_versions'] = int(group['mismatching_unsupported_versions'])
                continue

            # Invalid opcode: 0
            m = r18.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_received_dict['invalid_opcode'] = int(group['invalid_opcode'])
                continue

            # Unknown group: 0
            m = r19.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_received_dict['unknown_group'] = int(group['unknown_group'])
                continue
        
            # Inoperational group: 0	
            m = r20.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['inoperational_group'] = int(group['inoperational_group'])
                continue
        
            # Conflicting Source IP: 0
            m = r21.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['conflicting_source_ip'] = int(group['conflicting_source_ip'])
                continue
        		
            # Failed Authentication: 2
            m = r22.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['failed_authentication'] = int(group['failed_authentication'])
                continue

            # Invalid Hello Time: 0
            m = r23.match(line)
            if m:
                group = m.groupdict()			
                invalid_packets_received_dict['invalid_hello_time'] = int(group['invalid_hello_time'])
                continue
        		
            # Mismatching Virtual IP: 0
            m = r24.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_received_dict['mismatching_virtual_ip'] = int(group['mismatching_virtual_ip'])
                continue

        return parsed_dict
        

class ShowHsrpStatusSchema(MetaParser):
    ''' Schema for commands:
        * show hsrp status
    '''
    schema = {
        'status': {
            'clock_time': str,
            'process_started': str,
            'checkpoint_recovered': str,
            'issu_completed': str,
            'issu_aborted': str,
            'mode': {
                Any(): {
                    'mode1_type': str,
                    'issu_state': str,
                    'big_bang_notification': str,
                },
            },				
        }
    }


class ShowHsrpStatus(ShowHsrpStatusSchema):
    ''' Parser for commands:
        * show hsrp status
    '''
	
    cli_command = 'show hsrp status'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Sun Mar 27 20:41:21.974 UTC
        r1 = re.compile(r'(?P<clock_time>\S{3}\s+\S{3}\s+\d+\s+\d+\:\d+\:\d+\.\d+\s+\S+)$')
     
        # Process started at Mar 10 20:37:22.290 UTC
        r2 = re.compile(r'^Process started at +(?P<process_started>[\w\s\.\:]+)$')
     
        # Checkpoint recovered Mar 10 20:37:22.385 UTC
        r3 = re.compile(r'^Checkpoint recovered +(?P<checkpoint_recovered>[\w\s\.\:]+)$')

        # Mode is Primary
        r4 = re.compile(r'Mode +is +(?P<mode_state>[a-zA-Z]+)$')

        #   ISSU is not in progress
        r5 = re.compile(r'ISSU is +(?P<issu_state>[a-zA-Z ]+)$')

        #   Big Bang notification received Never
        r6 = re.compile(r'Big Bang notification +(?P<big_bang_notification>[a-zA-Z ]+)$')

        # ISSU completed Never
        r7 = re.compile(r'^ISSU completed +(?P<issu_completed>[a-zA-Z ]+)$')

        # ISSU aborted Never
        r8 = re.compile(r'^ISSU aborted +(?P<issu_aborted>[a-zA-Z ]+)$')

        parsed_dict = {} 

        for line in output.splitlines():
            line = line.strip()

            # Sun Mar 27 20:41:21.974 UTC 
            m = r1.match(line)
            if m: 
                group = m.groupdict()
                status_dict = parsed_dict.setdefault('status', {})
                status_dict['clock_time'] = group['clock_time']
                continue
     		
            # Process started at Mar 10 20:37:22.290 UTC	
            m = r2.match(line)                                                
            if m:
                group = m.groupdict()
                status_dict['process_started'] = group['process_started']
                continue

            # Checkpoint recovered Mar 10 20:37:22.385 UTC
            m = r3.match(line)
            if m:
                group = m.groupdict()
                status_dict['checkpoint_recovered'] = group['checkpoint_recovered']
                continue

            # Mode is Primary
            m = r4.match(line)
            if m: 
                group = m.groupdict()
                model_type = group['mode_state'].lower()
                model_dict = status_dict.setdefault('mode', {}).setdefault(model_type, {})
                model_dict['mode1_type'] = model_type 
                continue

            # ISSU is not in progress
            m = r5.match(line)
            if m:
                group = m.groupdict()
                model_dict['issu_state'] = group['issu_state']
                continue

            #Big Bang notification received Never
            m = r6.match(line)
            if m:
                group = m.groupdict()
                model_dict['big_bang_notification'] = group['big_bang_notification']
                continue
        		
            # ISSU completed Never
            m = r7.match(line)
            if m:
                group = m.groupdict()
                status_dict['issu_completed'] = group['issu_completed']
                continue

            # ISSU aborted Never
            m = r8.match(line)
            if m:
                group = m.groupdict()
                status_dict['issu_aborted'] = group['issu_aborted']
                continue
        return parsed_dict
             

""" show_frequency_synchronization.py

IOSXR parsers for the following commands:

    * 'show frequency synchronization interfaces {interface}'
    * 'show frequency synchronization interfaces'

"""

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowFrequencySynchronizationInterfacesSchema(MetaParser):
    ''' Schema for:
            * 'show frequency synchronization interfaces'
            * 'show frequency synchronization interfaces {interface}'
    '''

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'interface_status': str,
                Optional('selection'): str,
                'wait_to_restore_time': int,
                'ssm': {
                    'status': str,
                    Optional('peer_time'): str,
                    Optional('last_ssm_received'): str,
                    Optional('esmc_ssms'): {
                        'sent': {
                            'total': int,
                            'information': int,
                            'event': int,
                            'dnu_dus': int
                        },
                        'received': {
                            'total': int,
                            'information': int,
                            'event': int,
                            'dnu_dus': int
                        }
                    }
                },
                'input': {
                    'status': str,
                    Optional('selection'): str,
                    Optional('restore'): str,
                    Optional('last_received_ql'): str,
                    Optional('effective_ql'): str,
                    Optional('priority'): int,
                    Optional('time_of_day_priority'): int
                },
                'output': {
                    'selected_source': str,
                    'selected_source_ql': str,
                    Optional('effective_ql'): str
                },
                'next_selection_points': str
            }
        }
    }


# ================================
# Parser for 'show frequency synchronization interfaces'
# Parser for 'show frequency synchronization interfaces {interface}'
# ================================
class ShowFrequencySynchronizationInterfaces(ShowFrequencySynchronizationInterfacesSchema):

    cli_command = ['show frequency synchronization interfaces {interface}',
                   'show frequency synchronization interfaces']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                command = self.cli_command[0].format(interface=interface)
            else:
                command = self.cli_command[1]
            output = self.device.execute(command)

        # initial return dictionary
        ret_dict = {}

        # Interface GigabitEthernet0/0/0/16 (up)
        # Interface TenGigE0/0/2/0 (shutdown)
        p1 = re.compile(r'^Interface\s+(?P<interface>\S+)\s+\((?P<interface_status>(up|shutdown|down))\)$')

        # Assigned as input for selection
        p2 = re.compile(r'^Assigned\s+as\s+(?P<selection>\w+)\s+for\s+selection$')

        # Wait-to-restore time 0 minutes
        p3 = re.compile(r'^Wait-to-restore\s+time\s+(?P<wait_to_restore_time>\d+)\s+minutes$')

        # SSM Enabled
        # SSM Disabled
        p4 = re.compile(r'^SSM\s+(?P<ssm_status>[Enabled|Disabled]+)$')

        # Sent:          97832        97830         2          0
        p5 = re.compile(r'^Sent+:\s+(?P<total>\d+)\s+(?P<information>\d+)\s+(?P<event>\d+)\s+(?P<dnu_dus>\d+)$')

        # Received:      97831        97830         1          0
        p6 = re.compile(r'^Received+:\s+(?P<total>\d+)\s+(?P<information>\d+)\s+(?P<event>\d+)\s+(?P<dnu_dus>\d+)$')

        # Up
        # Down
        p7 = re.compile(r'^(?P<input>[Up|Down]+)$')

        # Down - not assigned for selection
        p8 = re.compile(r'^(?P<input>[Up|Down]+)\s+-\s+(?P<selection>[\w\s]+)\s+for\s+selection$')

        # Last received QL: Failed
        # Last received QL: Opt-I/PRC
        p9 = re.compile(r'^Last\s+received\s+QL:\s(?P<last_received_ql>.*)$')

        # Effective QL: Opt-I/PRC, Priority: 15, Time-of-day Priority 101
        # Effective QL: Failed, Priority: 15, Time-of-day Priority 101
        p10 = re.compile(r'^Effective\s+QL:\s+(?P<effective_ql>.*),\s+Priority:\s+(?P<priority>\d+),'\
                         '\s+Time-of-day\s+Priority\s+(?P<time_of_day_priority>\d+)$')

        # Restore in 00:04:33
        p11 = re.compile(r'^Restore\s+in\s+(?P<restore>[\d:]+)$')

        # Selected source: TenGigE0/0/2/1
        p12 = re.compile(r'^Selected\s+source:\s+(?P<selected_source>.*)$')

        # Selected source QL: Opt-I/PRC
        p13 = re.compile(r'^Selected\s+source\s+QL:\s+(?P<selected_source_ql>\S+)$')

        # Effective QL: Opt-I/PRC
        p14 = re.compile(r'^Effective\s+QL:\s+(?P<effective_ql>\S+)$')

        # Next selection points: SPA_RX_0
        p15 = re.compile(r'^Next\s+selection\s+points:\s+(?P<next_selection_points>.*)$')

        # Peer Up for 1d02h, last SSM received 0.837s ago
        # p16 = re.compile(r'^Peer\s+Up\s+for\s+(?P<peer_up_time>\w+),\s+last\s+SSM\s+received\s+(?P<last_ssm_received>[\w.]+)\s+ago$')
        p16 = re.compile(r'^Peer\s+[Up|Timed Out]+\s+for\s+(?P<peer_time>\w+),\s+last\s+SSM\s+received\s+(?P<last_ssm_received>[\w .]+)')

        for line in output.splitlines():
            line = line.strip() # strip whitespace from beginning and end

            # Interface GigabitEthernet0/0/0/16 (up)
            # Interface TenGigE0/0/2/0 (shutdown)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interfaces_dict = ret_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                interfaces_dict.update({'interface': group['interface']})
                interfaces_dict.update({'interface_status': group['interface_status']})
                continue

            # Assigned as input for selection
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interfaces_dict.update({'selection': group['selection']})
                continue

            # Wait-to-restore time 0 minutes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interfaces_dict.update({'wait_to_restore_time': int(group['wait_to_restore_time'])})
                continue

            # SSM Enabled
            # SSM Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                # ssm_dict = interfaces_dict.setdefault('ssm', {}).setdefault(group['ssm_status'], {})
                ssm_dict = interfaces_dict.setdefault('ssm', {})
                ssm_dict.update({'status': group['ssm_status']})
                continue

            # Sent:          97832        97830         2          0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                esmc_ssms_dict = ssm_dict.setdefault('esmc_ssms', {})
                sent_dict = esmc_ssms_dict.setdefault('sent', {})

                sent_dict['total'] = int(m.groupdict()['total'])
                sent_dict['information'] = int(m.groupdict()['information'])
                sent_dict['event'] = int(m.groupdict()['event'])
                sent_dict['dnu_dus'] = int(m.groupdict()['dnu_dus'])
                continue

            # Received:      97831        97830         1          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                received_dict = esmc_ssms_dict.setdefault('received', {})

                received_dict['total'] = int(m.groupdict()['total'])
                received_dict['information'] = int(m.groupdict()['information'])
                received_dict['event'] = int(m.groupdict()['event'])
                received_dict['dnu_dus'] = int(m.groupdict()['dnu_dus'])
                continue

            # Up
            # Down
            m = p7.match(line)
            if m:
                group = m.groupdict()
                input_dict = interfaces_dict.setdefault('input', {})
                input_dict['status'] = m.groupdict()['input']
                continue

            # Down - not assigned for selection
            m = p8.match(line)
            if m:
                group = m.groupdict()
                input_dict = interfaces_dict.setdefault('input', {})
                input_dict['status'] = m.groupdict()['input']
                input_dict['selection'] = m.groupdict()['selection']
                continue

            # Last received QL: Failed
            # Last received QL: Opt-I/PRC
            m = p9.match(line)
            if m:
                group = m.groupdict()
                input_dict['last_received_ql'] = m.groupdict()['last_received_ql']
                continue

            # Effective QL: Opt-I/PRC, Priority: 15, Time-of-day Priority 101
            # Effective QL: Failed, Priority: 15, Time-of-day Priority 101
            m = p10.match(line)
            if m:
                group = m.groupdict()
                input_dict['effective_ql'] = m.groupdict()['effective_ql']
                input_dict['priority'] = int(m.groupdict()['priority'])
                input_dict['time_of_day_priority'] = int(m.groupdict()['time_of_day_priority'])
                continue

            # Restore in 00:04:33
            m = p11.match(line)
            if m:
                group = m.groupdict()
                input_dict = interfaces_dict.setdefault('input', {})
                input_dict['restore'] = m.groupdict()['restore']
                continue

            # Selected source: TenGigE0/0/2/1
            # Selected source: GigabitEthernet0/0/0/18
            m = p12.match(line)
            if m:
                group = m.groupdict()
                output_dict = interfaces_dict.setdefault('output', {})
                output_dict['selected_source'] = m.groupdict()['selected_source']
                continue

            # Selected source QL: Opt-I/PRC
            m = p13.match(line)
            if m:
                group = m.groupdict()
                output_dict['selected_source_ql'] = m.groupdict()['selected_source_ql']
                continue
            
            # Effective QL: Opt-I/PRC
            m = p14.match(line)
            if m:
                group = m.groupdict()
                output_dict['effective_ql'] = m.groupdict()['effective_ql']
                continue

            # Next selection points: SPA_RX_0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                interfaces_dict.update({'next_selection_points': group['next_selection_points']})
                continue

            # Peer Up for 1d02h, last SSM received 0.837s ago
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ssm_dict.update({'peer_time': group['peer_time']})
                ssm_dict.update({'last_ssm_received': group['last_ssm_received']})
                continue

        return ret_dict

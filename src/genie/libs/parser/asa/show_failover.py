'''show_failover.py
ASA parsers for for the following commands:
    * show failover
    * show failover interface
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie import parsergen


class ShowFailoverSchema(MetaParser):
    '''Schema for:
        * show failover
    '''
    schema = {
        'failover_enabled': bool,
        'failover_unit': str,
        'failover_lan_interface': {
            Optional('name'): str,
            Optional('interface'): str,
            'status': str,
        },
        'reconnect_timeout': str,
        'unit_poll_frequency': {
            'value': int,
            'time_unit': str
        },
        'unit_hold_time': {
            'value': int,
            'time_unit': str
        },
        'interface_poll_frequency': {
            'value': int,
            'time_unit': str
        },
        'interface_hold_time': {
            'value': int,
            'time_unit': str
        },
        'interface_policy': int,
        'monitored_interfaces': int,
        'max_monitored_interfaces': int,
        Optional('version'): {
            'ours': str,
            'mate': str,
        },
        Optional('serial_number'): {
            'ours': str,
            'mate': str,
        },
        Optional('last_failover_at'): str,
        Optional('this_host'): {
            'is_primary': bool,
            'state': str,
            Optional('active_time_secs'): int,
            'interfaces': {
                Any(): {
                    Optional('ipv4_address'): str,
                    Optional('ipv6_address'): str,
                    'state': str,
                    'monitored_state': str,
                },
            },
            Optional('slots'): {
                Any(): {
                    'model': str,
                    'version': str,
                    'status': str,
                },
            },
        },
        Optional('other_host'): {
            'is_primary': bool,
            'state': str,
            Optional('active_time_secs'): int,
            'interfaces': {
                Any(): {
                    Optional('ipv4_address'): str,
                    Optional('ipv6_address'): str,
                    'state': str,
                    'monitored_state': str,
                },
            },
            Optional('slots'): {
                Any(): {
                    'model': str,
                    'version': str,
                    'status': str,
                },
            },
        },
        Optional('stateful_failover_interface'): {
            'name': str,
            'interface': str,
            'status': str,
        },
        Optional('stateful_failover_statistics'): {
            Any(): {
                'xmit': int,
                'xerr': int,
                'rcv': int,
                'rerr': int,
            }
        },
        Optional('logical_update_queue_info'): {
            'recv_q': {
                'cur': int,
                'max': int,
                'total': int,
            },
            'xmit_q': {
                'cur': int,
                'max': int,
                'total': int,
            }
        }
    }


class ShowFailover(ShowFailoverSchema):

    cli_command = 'show failover'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Failover On
        # Failover Off
        p1 = re.compile(r'^Failover\s(?P<status>On|Off)$')

        # Failover unit Secondary
        # Failover unit Primary
        p2 = re.compile(r'^Failover +unit\s(?P<is_primary>Primary|Secondary)$')

        # Failover LAN Interface: folink GigabitEthernet0/1 (up)
        p3 = re.compile(
            r'^Failover +LAN +Interface:\s(?P<name>[A-Za-z0-9\-\_]+)\s+'
            '(?P<interface>(Lo\S*|Fa\S*|Gi\S*|Ten\S*|\S*(SL|VL)\S*|Se\S*|VoIP\S*|Configured))'
            '( +\((?P<status>[A-Za-z0-0_\-\s]+)\))?$'
        )

        # Reconnect timeout 0:00:00
        p4 = re.compile(r'^Reconnect +timeout\s+(?P<timeout>\S+)$')

        # Unit Poll frequency 1 seconds, holdtime 15 seconds
        # Unit Poll frequency 300 milliseconds, holdtime 999 milliseconds
        p5 = re.compile(
            r'^Unit +Poll +frequency\s+(?P<poll>\d+)\s+(?P<poll_unit>seconds|milliseconds),'
            ' +holdtime\s+(?P<holdtime>\d+)\s+(?P<holdtime_unit>seconds|milliseconds)$'
        )

        # Interface Poll frequency 800 milliseconds, holdtime 5 seconds
        # Interface Poll frequency 5 seconds, holdtime 25 seconds
        p6 = re.compile(
            r'^Interface +Poll +frequency\s+(?P<poll>\d+)\s+(?P<poll_unit>seconds|milliseconds),'
            ' +holdtime\s+(?P<holdtime>\d+)\s+(?P<holdtime_unit>seconds|milliseconds)$'
        )

        # Interface Policy 1
        p7 = re.compile(r'^Interface +Policy\s+(?P<policy>\d+)$')

        # Monitored Interfaces 1 of 311 maximum
        p8 = re.compile(
            r'^Monitored +Interfaces\s+(?P<monitored>\d+) +of\s+(?P<max>\d+) +maximum$'
        )

        # Version: Ours 9.14(1), Mate 9.14(1)
        p9 = re.compile(
            r'^Version: +Ours\s+(?P<ours>[A-Za-z0-9\.\(\)]+),'
            ' +Mate\s+(?P<mate>[A-Za-z0-9\.\(\)]+)$'
        )

        # Serial Number: Ours 9AW2PSRETDT, Mate 9ASGGBEE416
        p10 = re.compile(
            r'^Serial +Number: +Ours\s+(?P<ours>[A-Za-z0-9]+),'
            ' +Mate\s+(?P<mate>[A-Za-z0-9]+)$'
        )

        # Last Failover at: 20:37:30 UTC Apr 11 2021
        p11 = re.compile(r'^Last +Failover +at:\s+(?P<failover>.*)$')

        # This host: Primary - Active
        # Other host: Secondary - Standby Ready
        # Other host: Secondary - Failed
        p12 = re.compile(
            r'^(?P<which>This|Other) +host:\s+(?P<is_primary>\w+)\s+\-\s+(?P<state>.*)$'
        )

        # Active time: 1106 (sec)
        p13 = re.compile(r'^Active +time:\s+(?P<active_time>\d+)\s+\(sec\)$')

        # Interface management (192.168.253.14): Normal (Waiting)
        # Interface outside (0.0.0.0/fe80::e8f:c5ff:fe5f:d01): Unknown (Waiting)
        # Interface outside (0.0.0.0/fe80::ecd:e9ff:fe5c:5301): Normal (Not-Monitored)
        p14 = re.compile(
            r'^Interface\s+(?P<interface>\w+)\s+\((?P<ipv4>[0-9\.]+)'
            '(\/(?P<ipv6>[A-Za-z0-9:]+))?\):\s+(?P<state>\w+)\s+'
            '\((?P<monitored_state>[A-Za-z0-9\-_]+)\)$'
        )

        # slot 0: ASAv hw/sw rev (/9.14(1)) status (Up Sys)
        # slot 1: IPS5515 hw/sw rev (N/A/7.1(4)E4) status (Up/Up)
        # slot 0: ASA5515 hw/sw rev (1.0/9.2(2)4) status (Up Sys)
        p15 = re.compile(
            r'^slot\s+(?P<slot>\d+):\s+(?P<model>[A-Za-z0-9\-_]+) +hw\/sw +rev\s+'
            '\((?P<version>\S+)\) +status\s+\((?P<status>[A-Za-z0-9_\-\s\/]+)\)$'
        )

        #         Recv Q:         0       0       0
        p16_1 = re.compile(r'^Recv +Q:\s+(?P<curr>\d+)\s+(?P<max>\d+)\s+(?P<total>\d+)$')

        # Xmit Q:         0       0       0
        p16_2 = re.compile(r'^Xmit +Q:\s+(?P<curr>\d+)\s+(?P<max>\d+)\s+(?P<total>\d+)$')

        # Stateful Failover Logical Update Statistics
        # Link : foupdateif GigabitEthernet0/3 (administratively down)
        p17_1 = re.compile(r'^Stateful +Failover +Logical +Update +Statistics$')
        p17_2 = re.compile(
            r'^Link\s+:\s+(?P<name>[A-Za-z0-9]+)\s+'
            '(?P<interface>(Lo\S*|Fa\S*|Gi\S*|Ten\S*|\S*(SL|VL)\S*|Se\S*|VoIP\S*|Configured))'
            '( +\((?P<status>[A-Za-z0-0_\-\s]+)\))?$'
        )

        parsed_dict = {}

        # Indicates if have reached the This host section or Other host section
        is_this_host = False

        # Indicated if we have reached the Stateful Failover Logical Update Statistics section
        is_stateful_failover_statistics_section = False

        for line in out.splitlines():
            line = line.strip()

            # Failover On
            # Failover Off
            m = p1.match(line)
            if m:
                parsed_dict.update({
                    'failover_enabled': True if m.groupdict()['status'] == 'On' else False
                })
                continue

            # Failover unit Secondary
            # Failover unit Primary
            m = p2.match(line)
            if m:
                parsed_dict.update({'failover_unit': m.groupdict()['is_primary']})
                continue

            # Failover LAN Interface: folink GigabitEthernet0/1 (up)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['name'] == 'not':
                    failover_lan_interface = {
                        'status': 'not Configured'
                    }
                else:
                    failover_lan_interface = {
                        'name': group['name'],
                        'interface': group['interface'],
                        'status': group['status'],
                    }
                parsed_dict.update({'failover_lan_interface': failover_lan_interface})
                continue

            # Reconnect timeout 0:00:00
            m = p4.match(line)
            if m:
                parsed_dict.update({'reconnect_timeout': m.groupdict()['timeout']})
                continue

            # Unit Poll frequency 1 seconds, holdtime 15 seconds
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({
                    'unit_poll_frequency': {
                        'value': int(group['poll']),
                        'time_unit': group['poll_unit']
                    }
                })
                parsed_dict.update({
                    'unit_hold_time': {
                        'value': int(group['holdtime']),
                        'time_unit': group['holdtime_unit']
                    }
                })
                continue

            # Interface Poll frequency 800 milliseconds, holdtime 5 seconds
            m = p6.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({
                    'interface_poll_frequency': {
                        'value': int(group['poll']),
                        'time_unit': group['poll_unit']
                    }
                })
                parsed_dict.update({
                    'interface_hold_time': {
                        'value': int(group['holdtime']),
                        'time_unit': group['holdtime_unit']
                    }
                })
                continue

            # Interface Policy 1
            m = p7.match(line)
            if m:
                parsed_dict.update({'interface_policy': int(m.groupdict()['policy'])})
                continue

            # Monitored Interfaces 1 of 311 maximum
            m = p8.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'monitored_interfaces': int(group['monitored'])})
                parsed_dict.update({'max_monitored_interfaces': int(group['max'])})
                continue

            # Version: Ours 9.14(1), Mate 9.14(1)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({
                    'version': {
                        'ours': group['ours'],
                        'mate': group['mate']
                    }
                })
                continue

            # Serial Number: Ours 9AW2PSRETDT, Mate 9ASGGBEE416
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({
                    'serial_number': {
                        'ours': group['ours'],
                        'mate': group['mate']
                    }
                })
                continue

            # Last Failover at: 20:37:30 UTC Apr 11 2021
            m = p11.match(line)
            if m:
                parsed_dict.update({'last_failover_at': m.groupdict()['failover']})
                continue

            # This host: Primary - Active
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if group['which'] == 'This':
                    this_host_dict = parsed_dict.setdefault('this_host', {})
                    this_host_interfaces_dict = this_host_dict.setdefault('interfaces', {})
                    this_host_slot_dict = this_host_dict.setdefault('slots', {})
                    this_host_dict.update({
                        'is_primary': True if group['is_primary'] == 'Primary' else False
                    })
                    this_host_dict.update({'state': group['state']})
                    is_this_host = True
                if group['which'] == 'Other':
                    other_host_dict = parsed_dict.setdefault('other_host', {})
                    other_host_interfaces_dict = other_host_dict.setdefault('interfaces', {})
                    other_host_slot_dict = other_host_dict.setdefault('slots', {})
                    other_host_dict.update({
                        'is_primary': True if group['is_primary'] == 'Primary' else False
                    })
                    other_host_dict.update({'state': group['state']})
                    is_this_host = False
                continue

            #  Active time: 1106 (sec)
            m = p13.match(line)
            if m:
                if is_this_host:
                    this_host_dict.update({'active_time_secs': int(m.groupdict()['active_time'])})
                else:
                    other_host_dict.update({'active_time_secs': int(m.groupdict()['active_time'])})
                continue

            # Interface outside (0.0.0.0/fe80::e8f:c5ff:fe5f:d01): Unknown (Waiting)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                interface = {
                    'state': group['state'],
                    'monitored_state': group['monitored_state']
                }
                if 'ipv4' in group and group['ipv4']:
                    interface['ipv4_address'] = group['ipv4']
                if 'ipv6' in group and group['ipv6']:
                    interface['ipv6_address'] = group['ipv6']
                if is_this_host:
                    this_host_interfaces_dict.update({group['interface']: interface})
                else:
                    other_host_interfaces_dict.update({group['interface']: interface})
                continue

            #  slot 0: ASAv hw/sw rev (/9.14(1)) status (Up Sys)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                slot = {
                    'model': group['model'],
                    'version': group['version'],
                    'status': group['status']
                }
                if is_this_host:
                    this_host_slot_dict.update({group['slot']: slot})
                else:
                    other_host_slot_dict.update({group['slot']: slot})
                continue

            #  Recv Q:         0       0       0
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                queue_dict = parsed_dict.setdefault('logical_update_queue_info', {})
                queue_stat = {
                    'cur': int(group['curr']),
                    'max': int(group['max']),
                    'total': int(group['total']),
                }
                queue_dict.update({'recv_q': queue_stat})
                continue

            # Xmit Q:         0       0       0
            m = p16_2.match(line)
            if m:
                group = m.groupdict()
                queue_stat = {
                    'cur': int(group['curr']),
                    'max': int(group['max']),
                    'total': int(group['total']),
                }
                queue_dict.update({'xmit_q': queue_stat})
                continue

            # Stateful Failover Logical Update Statistics
            m = p17_1.match(line)
            if m:
                is_stateful_failover_statistics_section = True
                continue

            #  Link : foupdateif GigabitEthernet0/3 (administratively down)
            m = p17_2.match(line)
            if m:
                if is_stateful_failover_statistics_section:
                    group = m.groupdict()
                    stateful_failover_interface = {
                        'name': group['name'],
                        'interface': group['interface'],
                        'status': group['status'],
                    }
                    parsed_dict.update({
                        'stateful_failover_interface': stateful_failover_interface
                    })
                continue

        # Parse Stateful Failover Logical Update Statistics
        header = ['Stateful Obj', 'xmit', 'xerr', 'rcv', 'rerr']

        stateful_failover_statistics = parsergen.oper_fill_tabular(
            device_output=out, device_os='asa', header_fields=header,
            table_terminal_pattern=r"^\n"
        )
        failover_stats = parsed_dict.setdefault('stateful_failover_statistics', {})

        for k in stateful_failover_statistics.entries.keys():
            # Skip malformed values
            if 'SIP Tx' in k:
                continue
            if 'Umbrella Device' in k:
                continue
            curr_dict = stateful_failover_statistics.entries[k]
            try:
                xmit = int(curr_dict['xmit'])
                xerr = int(curr_dict['xerr'])
                rcv = int(curr_dict['rcv'])
                rerr = int(curr_dict['rerr'])
            except:
                continue
            stat_dict = failover_stats.setdefault(k, {})
            stat_dict.update({'xmit': xmit})
            stat_dict.update({'xerr': xerr})
            stat_dict.update({'rcv':  rcv})
            stat_dict.update({'rerr': rerr})

        return parsed_dict


class ShowFailoverInterfaceSchema(MetaParser):
    ''' Schema for:
        * show failover interface
    '''
    schema = {
        Any(): {
            'name': str,
            'interface': str,
            'system_ip': str,
            'my_ip': str,
            'other_ip': str,
        }
    }


class ShowFailoverInterface(ShowFailoverInterfaceSchema):

    cli_command = 'show failover interface'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # interface folink GigabitEthernet0/1
        p1 = re.compile(r'^interface\s+(?P<name>\w+)\s+(?P<interface>[A-Za-z]+\s*[\.\d\/]+)$')

        # System IP Address: 2001:db8:cafe:ffee::a/127
        p2 = re.compile(r'^System +IP +Address:\s+(?P<ip>\S+)$')

        # My IP Address    : 2001:db8:cafe:ffee::a
        p3 = re.compile(r'^My +IP +Address\s+:\s+(?P<ip>\S+)$')

        # Other IP Address : 2001:db8:cafe:ffee::b
        p4 = re.compile(r'^Other +IP +Address\s+:\s+(?P<ip>\S+)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # interface folink GigabitEthernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = parsed_dict.setdefault(group['name'], {})
                interface_dict.update({'interface': group['interface']})
                interface_dict.update({'name': group['name']})
                continue

            # System IP Address: 2001:db8:cafe:ffee::a/127
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'system_ip': group['ip']})
                continue

            # My IP Address    : 2001:db8:cafe:ffee::a
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'my_ip': group['ip']})
                continue

            # Other IP Address : 2001:db8:cafe:ffee::b
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'other_ip': group['ip']})
                continue

        return parsed_dict

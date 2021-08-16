''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging
    * show logging | include {include}
    * show logging | exclude {exclude}
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowLoggingSchema(MetaParser):
    '''Schema for:
        * 'show logging'
        * 'show logging | include {include}'
        * 'show logging | exclude {exclude}'
    '''

    schema={
        Optional('logs'): list,
        Optional('syslog_logging'): {
            Any(): { # enabled
                'counters': {
                    'messages_dropped': int,
                    'messages_rate_limited': int,
                    'flushes': int,
                    'overruns': int,
                    'xml': str, # 'disabled'
                    'filtering': str, # 'disabled'
                }
            }
        },
        Optional('message_discriminator'): {
            Optional(Any()): { # 'Active'|'Inactive'
                Optional('md_name'): {
                    Optional(Any()): { # 'C'
                        Optional('severity_group'): {
                            'flag': str, # 'includes'|'drops'
                            'str': str, # '5'
                        },
                        Optional('facility'): {
                            'flag': str, # 'includes'|'drops'
                            'regexp_str': str, # 'SYS'
                        },
                        Optional('mnemonics'): {
                            'flag': str, # 'include'|'drops'
                            'regexp_str': str, # 'UPDOWN'
                        },
                        Optional('msg_body'): {
                            'flag': str, # 'include'|'drops'
                            'regexp_str': str, # link
                        },
                        Optional('rate_limit_not_to_exceed'): {
                            'rate_limit': int, # 100
                        }
                    }
                }
            }
        },
        Optional('logging'): {
            'console': {
                'status': str, # 'enabled'|'disabled'
                Optional('level'): str,
                Optional('messages_logged'): int,
                Optional('xml'): str,
                Optional('filtering'): str,
            },
            'monitor': {
                'status': str, # 'enabled'|'disabled'
                'level': str,
                'messages_logged': int,
                'xml': str,
                'filtering': str,
                Optional('discriminator'): str,
                Optional('messages_rate_limited'): int,
                Optional('messages_dropped_by_md'): int,
                Optional('logging_to'): {
                    Any(): { # '10.4.29.222'
                        Or('vty','tty'): int,
                    }
                }
            },
            'buffer': {
                'status': str, # 'enabled'|'disabled'
                'level': str,
                'messages_logged': int,
                'xml': str, # 'enabled'|'disabled'
                Optional('xml_buffer_count'): int,
                'filtering': str, # 'enabled'|'disabled'
                Optional('buffer_count'): int,
                Optional('discriminator'): str,
                Optional('messages_rate_limited'): int,
                Optional('messages_dropped_by_md'): int
            },
            'exception': {
                Optional('status'): str, # 'enabled'|'disabled'
                'size_bytes': int, # 4096
            },
            'persistent': {
                Optional('status'): str, # 'enabled'|'disabled'
                Optional('url'): str,
                Optional('disk_space_bytes'): int,
                Optional('file_size_bytes'): int,
                Optional('batch_size_bytes'): int,
            },
            Optional('file'): {
                Optional('status'): str, # 'enabled'|'disabled'
                Optional('file_name'): str,
                Optional('max_size'): int,
                Optional('min_size'): int,
                Optional('level'): str,
                Optional('messages_logged'): int,
            },
            Optional('count_and_time_stamp_logging_messages'): str, # 'enabled'|'disabled'
            'trap': {
                Optional('status'): str, # 'enabled'|'disabled'
                'level': str, # 'informational'
                'message_lines_logged': int, # 70
                Optional('logging_to'): {
                    Any(): { # '10.4.29.222'
                        'protocol': str, # 'tcp'|'udp'|'unknown'
                        'port': int, # 1470
                        'audit': str, # 'disabled'|'enabled'
                        'link': str, # 'up'|'down'
                        'message_lines_logged': int,
                        'message_lines_rate_limited': int,
                        'message_lines_dropped_by_md': int,
                        'xml': str, # 'enabled'|'disabled'
                        'sequence_number': str, # 'enabled'|'disabled'
                        'filtering': str, # 'enabled'|'disabled'
                        Optional('logging_source_interface'): {
                            Any(): str, # 'Vlan200': <vrf>
                        }
                    }
                }
            }
        },
        Optional('filter_modules'): {
            Any(): { # url
                'cli_args': str,
                'invalid': bool, # True|False
            }
        },
        Optional('log_buffer_bytes'): int, # 32000
        }


class ShowLogging(ShowLoggingSchema):
    '''Parser for:
        * 'show logging'
        * 'show logging | include {include}'
        * 'show logging | exclude {exclude}'
    '''

    cli_command = ['show logging | exclude {exclude}',
                   'show logging | include {include}',
                   'show logging']

    def cli(self, exclude='', include='', output=None):

        if output is None:
            # Build the command
            if exclude:
                cmd = self.cli_command[0].format(exclude=exclude)
            elif include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[2]
            # Execute the command
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        log_lines = []

        #Syslog logging: enabled (0 messages dropped, 0 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)
        p1 = re.compile(r'Syslog +logging: +(?P<enable_disable>\S+) +\(+(?P<messages_dropped>\d+) '
                        r'+messages +dropped, +(?P<messages_rate_limited>\d+) +messages +rate-limited, '
                        r'+(?P<flushes>\d+) +flushes, +(?P<overruns>\d+) +overruns, +xml +(?P<xml>\S+), '
                        r'filtering +(?P<filtering>\S+)\)$')

        #Console logging: disabled
        p2 = re.compile(r'(?P<tag>\S+) +logging: +(?P<status>\S+)$')

        #Monitor logging: level debugging, 13 messages logged, xml disabled,
        #Console logging: level debugging, 9789 messages logged, xml disabled,
        p3 = re.compile(r'(?P<tag>\S+) +logging: +level '
                        r'+(?P<level>\S+), +(?P<messages_logged>\d+) '
                        r'+messages +logged, +xml +(?P<xml>\S+),$')

        #filtering disabled
        p4 = re.compile(r'filtering +(?P<filtering>\S+)$')

        #Exception Logging: size (4096 bytes)
        p6 = re.compile(r'Exception +Logging: size +\((?P<size_bytes>\d+) +bytes+\)$')

        #Count and timestamp logging messages: disabled
        p7 = re.compile(r'Count +and +timestamp +logging +messages: '
                        r'+(?P<count_and_time_stamp_logging_messages>\S+)$')

        #File logging: disabled
        p8 = re.compile(r'(?P<tag>File +logging): +(?P<status>\S+)$')

        #Persistent logging: disabled
        #Persistent logging: enabled, url bootflash:/syslog, disk space 104857600 bytes, file size 10485760 bytes, batch size 4096 bytes
        p9 = re.compile(r'Persistent\s+logging:\s+(?P<status>\w+)(,\s+url\s+(?P<url>[\w:/]+),\s+disk\s+space\s+(?P<disk_space_bytes>\d+)\s+bytes,\s+file\s+size\s+(?P<file_size_bytes>\d+)\s+bytes,\s+batch\s+size\s+(?P<batch_size_bytes>\d+)\s+bytes)?$')

        #Trap logging: level informational, 1570 message lines logged
        p10 = re.compile(r'(?P<tag>Trap) +logging: +level +'
                         r'(?P<level>\S+), +(?P<message_lines_logged>\d+) '
                         r'+message +lines +logged$')

        #Logging to 192.168.1.3  (tcp port 1514, audit disabled,
        p11 = re.compile(r'Logging +to (?P<logging_to>[\d\.]+) +\((?P<protocol>\S+) '
                        r'+port +(?P<port>\d+), +audit +(?P<audit>\S+),$')

        #link down),
        p12 = re.compile(r'link +(?P<link>\S+)\),$')

        #787 message lines logged,
        p13 = re.compile(r'(?P<message_lines_logged>\d+) +message +lines +logged,$')

        #0 message lines rate-limited,
        p14 = re.compile(r'(?P<message_lines_rate_limited>\d+) '
                         r'+message +lines +rate-limited,$')

        #0 message lines dropped-by-MD,
        p15 = re.compile(r'(?P<message_lines_dropped_by_md>\d+) '
                         r'+message +lines +dropped-by-MD,$')

        #xml disabled, sequence number disabled
        p16 = re.compile(r'xml +(?P<xml>\S+), +sequence +number +(?P<sequence_number>\S+)$')

        #Logging Source-Interface:       VRF Name:
        p17 = re.compile(r'Logging Source-Interface: +VRF +Name:$')

        #Vlan200
        p18 = re.compile(r'(?P<interface>\S+)+(?P<vrf>\S+)?$')

        #Log Buffer (32000 bytes):
        p19 = re.compile(r'Log +Buffer +\((?P<vrf>\d+) +bytes+\):$')

        ret_dict = {}
        for line in out.splitlines():

            line = line.strip()

            #Syslog logging: enabled (0 messages dropped, 0 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sys_log_entry = ret_dict.setdefault("syslog_logging", {})
                logging_entry = ret_dict.setdefault("logging", {})
                filter_modules_entry = ret_dict.setdefault(
                    "syslog_logging", {})
                log_buffer_bytes_entry = ret_dict.setdefault(
                    "log_buffer_bytes", {})

                outer_logging_dict = {}
                inner_key = group['enable_disable']
                parent_dict = {}
                counter_dict = {
                    'messages_dropped': int(group['messages_dropped']),
                    'messages_rate_limited': int(group['messages_rate_limited']),
                    'flushes': int(group['flushes']),
                    'overruns': int(group['overruns']),
                    'xml': group['xml'],
                    'filtering': group['filtering'],
                }

                parent_dict['counters'] = counter_dict
                sys_log_entry[inner_key] = parent_dict
                continue

            #Console logging: disabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_tag = group['tag'].lower()
                logging_entry.setdefault(current_tag, {}).setdefault(
                    'status', group['status'])
                continue

            #Monitor logging: level debugging, 13 messages logged, xml disabled,
            #Console logging: level debugging, 9789 messages logged, xml disabled,
            m = p3.match(line)
            if m:
                group = m.groupdict()
                current_tag = group['tag'].lower()
                logging_entry.setdefault(current_tag,
                                         {}).setdefault('status', 'enabled')
                logging_entry[current_tag].setdefault('level', group['level'])
                logging_entry[current_tag].setdefault(
                    'messages_logged', int(group['messages_logged']))
                logging_entry[current_tag].setdefault('xml', group['xml'])
                continue

            #filtering disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if current_tag == 'trap':
                    logging_entry.setdefault(current_tag, {}).setdefault(
                        'logging_to',
                        {}).setdefault(current_logging_to,
                                       {}).setdefault('filtering',
                                                     group['filtering'])
                else:
                    logging_entry.setdefault(current_tag, {}).setdefault(
                        'filtering', group['filtering'])
                continue

            #Exception Logging: size (4096 bytes)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                exception_dict = {'size_bytes': int(group['size_bytes'])}
                logging_entry['exception'] = exception_dict
                continue

            #Count and timestamp logging messages: disabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                logging_entry['count_and_time_stamp_logging_messages'] = group[
                    'count_and_time_stamp_logging_messages']
                continue

            #File logging: disabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                file_dict = {'status': group['status']}
                logging_entry['file'] = file_dict
                continue

            #Persistent logging: disabled
            #Persistent logging: enabled, url bootflash:/syslog, disk space 104857600 bytes, file size 10485760 bytes, batch size 4096 bytes
            m = p9.match(line)
            if m:
                group = m.groupdict()
                for item in group:
                    if group[item]:
                        logging_entry.setdefault('persistent', {}).setdefault(
                            item,
                            int(group[item])
                            if 'bytes' in item else group[item])
                continue

            #Trap logging: level informational, 1570 message lines logged
            m = p10.match(line)
            if m:
                group = m.groupdict()
                trap_dict = {}
                current_tag = group['tag'].lower()

                trap_dict['level'] = group['level']
                trap_dict['message_lines_logged'] = int(
                    group['message_lines_logged'])

                logging_entry['trap'] = trap_dict
                continue

            #Logging to 192.168.1.3  (tcp port 1514, audit disabled,
            m = p11.match(line)
            if m:
                group = m.groupdict()
                logging_dict = {}
                current_logging_to = group['logging_to']

                logging_dict['protocol'] = group['protocol']
                logging_dict['port'] = int(group['port'])
                logging_dict['audit'] = group['audit']

                outer_logging_dict.update({current_logging_to: logging_dict})
                trap_dict['logging_to'] = outer_logging_dict
                continue

            #link down),
            m = p12.match(line)
            if m:
                group = m.groupdict()
                logging_dict['link'] = group['link']
                continue

            #787 message lines logged,
            m = p13.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_logged'] = int(
                    group['message_lines_logged'])
                continue

            #0 message lines rate-limited,
            m = p14.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_rate_limited'] = int(
                    group['message_lines_rate_limited'])
                continue

            #0 message lines dropped-by-MD,
            m = p15.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_dropped_by_md'] = int(
                    group['message_lines_dropped_by_md'])
                continue

            #xml disabled, sequence number disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                logging_dict['xml'] = group['xml']
                logging_dict['sequence_number'] = group['sequence_number']
                continue

            #Logging Source-Interface:       VRF Name:
            m = p17.match(line)
            if m:
                # do nothing, but need to parse for skipping this line
                continue

            #Vlan200
            #Vlan200                         VRF-A
            m = p18.match(line)
            if m:
                group = m.groupdict()
                logging_source_dict = {}
                if group['vrf']:
                    logging_source_dict['logging_configuration'] = group[
                        'interface'] + ':' + group['vrf']
                else:
                    logging_source_dict['logging_configuration'] = group[
                        'interface']

                logging_dict['logging_source_interface'] = logging_source_dict
                continue

            #Log Buffer (32000 bytes):
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict['log_buffer_bytes'] = int(group['vrf'])

                continue

            if line:
                if not line.lower().startswith(
                    'no active'
                ) and not line.lower().startswith('no inactive'):
                    log_lines.append(line)
                    ret_dict['logs'] = log_lines
                continue
        return ret_dict
''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging
    * show logging | include {include}
    * show logging | exclude {exclude}
    * show logging onboard rp active uptime
    * show logging onboard rp {rp_standby} uptime
    * show logging onboard rp active status
    * show logging onboard rp {rp_standby} status
    * show logging onboard rp active {include}
    * show logging onboard rp {rp_standby} {include}
    * show logging onboard rp {rp} {feature} detail
    * show logging process smd reverse
    * show logging process smd {switch} {mode} reverse
    * show logging onboard slot {slot} uptime latest
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, ListOf


class ShowLoggingSchema(MetaParser):
    '''Schema for:
        * 'show logging'
        * 'show logging | include {include}'
        * 'show logging | exclude {exclude}'
    '''

    schema = {
        Optional('logs'): list,
        Optional('syslog_logging'): {
            Any(): {  # enabled
                'counters': {
                    'messages_dropped': int,
                    'messages_rate_limited': int,
                    'flushes': int,
                    'overruns': int,
                    'xml': str,  # 'disabled'
                    'filtering': str,  # 'disabled'
                }
            }
        },
        Optional('message_discriminator'): {
            Optional(Any()): {  # 'Active'|'Inactive'
                Optional('md_name'): {
                    Optional(Any()): {  # 'C'
                        Optional('severity_group'): {
                            'flag': str,  # 'includes'|'drops'
                            'str': str,  # '5'
                        },
                        Optional('facility'): {
                            'flag': str,  # 'includes'|'drops'
                            'regexp_str': str,  # 'SYS'
                        },
                        Optional('mnemonics'): {
                            'flag': str,  # 'include'|'drops'
                            'regexp_str': str,  # 'UPDOWN'
                        },
                        Optional('msg_body'): {
                            'flag': str,  # 'include'|'drops'
                            'regexp_str': str,  # link
                        },
                        Optional('rate_limit_not_to_exceed'): {
                            'rate_limit': int,  # 100
                        }
                    }
                }
            }
        },
        Optional('logging'): {
            'console': {
                'status': str,  # 'enabled'|'disabled'
                Optional('level'): str,
                Optional('messages_logged'): int,
                Optional('xml'): str,
                Optional('filtering'): str,
            },
            'monitor': {
                'status': str,  # 'enabled'|'disabled'
                Optional('level'): str,
                Optional('messages_logged'): int,
                Optional('xml'): str,
                Optional('filtering'): str,
                Optional('discriminator'): str,
                Optional('messages_rate_limited'): int,
                Optional('messages_dropped_by_md'): int,
                Optional('logging_to'): {
                    Any(): {  # '10.4.29.222'
                        Or('vty', 'tty'): int,
                    }
                }
            },
            'buffer': {
                'status': str,  # 'enabled'|'disabled'
                Optional('level'): str,
                Optional('messages_logged'): int,
                'xml': str,  # 'enabled'|'disabled'
                Optional('xml_buffer_count'): int,
                'filtering': str,  # 'enabled'|'disabled'
                Optional('buffer_count'): int,
                Optional('discriminator'): str,
                Optional('messages_rate_limited'): int,
                Optional('messages_dropped_by_md'): int
            },
            'exception': {
                Optional('status'): str,  # 'enabled'|'disabled'
                Optional('size_bytes'): int,  # 4096
            },
            'persistent': {
                Optional('status'): str,  # 'enabled'|'disabled'
                Optional('url'): str,
                Optional('disk_space_bytes'): int,
                Optional('file_size_bytes'): int,
                Optional('batch_size_bytes'): int,
                # threshold capacity 5  alert , immediate , protected , notify
                Optional('logging_threshold'): int,
                Optional('threshold_percent'): int,
                Optional('threshold_alert'): str,
                Optional('immediate_write'): str,
                Optional('notify'): str,
                Optional('protected'): str
            },

            Optional('file'): {
                Optional('status'): str,  # 'enabled'|'disabled'
                Optional('file_name'): str,
                Optional('max_size'): int,
                Optional('min_size'): int,
                Optional('level'): str,
                Optional('messages_logged'): int,
            },
            Optional('count_and_time_stamp_logging_messages'): str,  # 'enabled'|'disabled'
            'trap': {
                Optional('status'): str,  # 'enabled'|'disabled'
                Optional('level'): str,  # 'informational'
                Optional('message_lines_logged'): int,  # 70
                Optional("logging_source_interface"): {
                    Any(): {  # Loopback0
                        Optional("vrf"): str  # Mgmt-intf
                    }
                },
                Optional('logging_to'): {
                    Any(): {  # '10.4.29.222'
                        'protocol': str,  # 'tcp'|'udp'|'unknown'
                        'port': int,  # 1470
                        'audit': str,  # 'disabled'|'enabled'
                        'link': str,  # 'up'|'down'
                        'message_lines_logged': int,
                        'message_lines_rate_limited': int,
                        'message_lines_dropped_by_md': int,
                        'xml': str,  # 'enabled'|'disabled'
                        'sequence_number': str,  # 'enabled'|'disabled'
                        'filtering': str,  # 'enabled'|'disabled'
                        Optional('vrf'): str,
                        Optional('logging_source_interface'): {
                            Any(): str,  # 'Vlan200': <vrf>
                        },
                        Optional('authentication'): str,
                        Optional('encryption'): str
                    }
                }
            }
        },
        Optional('filter_modules'): {
            Any(): {  # url
                'cli_args': str,
                'invalid': bool,  # True|False
            }
        },
        Optional('tls_profiles'): {
            Any(): {  # 'tls-profile-name
                'ciphersuites': list,  # rsa-aes-cbc-sha2 ecdhe-rsa-aes-cbc-sha2
                'trustpoint': str,  # tls-trustpoint
                'tls_version': str  # TLSv1.1 | TLSv1.2 | Default
            }
        },
        Optional('log_buffer_bytes'): int,  # 32000
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

        # Syslog logging: enabled (0 messages dropped, 0 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)
        p1 = re.compile(r'^Syslog +logging: +(?P<enable_disable>\S+) +\(+(?P<messages_dropped>\d+) '
                        r'+messages +dropped, +(?P<messages_rate_limited>\d+) +messages +rate-limited, '
                        r'+(?P<flushes>\d+) +flushes, +(?P<overruns>\d+) +overruns, +xml +(?P<xml>\S+), '
                        r'filtering +(?P<filtering>\S+)\)$')

        # Console logging: disabled
        p2 = re.compile(r'^(?P<tag>\S+) +logging: +(?P<status>\S+)$')

        # Buffer logging: disabled, xml disabled,
        p3 = re.compile(r'^(?P<tag>\S+) +[Ll]ogging: +(?P<status>\S+), +xml +(?P<xml>\S+),$')

        # Monitor logging: level debugging, 13 messages logged, xml disabled,
        # Console logging: level debugging, 9789 messages logged, xml disabled,
        p4 = re.compile(r'^(?P<tag>\S+) +logging: +level '
                        r'+(?P<level>\S+), +(?P<messages_logged>\d+) '
                        r'+messages +logged, +xml +(?P<xml>\S+),$')

        # filtering disabled
        # filtering enabled (0 messages logged)
        p5 = re.compile(r'^filtering +(?P<filtering>\S+)(?: +\(\d+ messages logged\))?$')


        # Exception Logging: size (4096 bytes)
        # Exception Logging: Disabled
        p6 = re.compile(r'^Exception +Logging:\s+((?P<disabled>[Dd]isabled)|size\s+\((?P<size_bytes>\d+) +bytes\))$')

        # Count and timestamp logging messages: disabled
        p7 = re.compile(r'^Count +and +timestamp +logging +messages: '
                        r'+(?P<count_and_time_stamp_logging_messages>\S+)$')

        # File logging: disabled
        p8 = re.compile(r'^(?P<tag>File +logging): +(?P<status>\S+)$')

        # Persistent logging: disabled
        # Persistent logging: enabled, url bootflash:/, disk space 16384 bytes, file size 8192 bytes, batch size 4096 bytes, threshold capacity 5  alert , immediate , protected , notify
        p9 = re.compile(r'^Persistent\s+logging:\s+(?P<status>\w+)(,\s+url\s+(?P<url>[\w:/]+),\s+disk\s+space\s+'
                        r'(?P<disk_space_bytes>\d+)\s+bytes,\s+file\s+size\s+(?P<file_size_bytes>\d+)'
                        r'\s+bytes,\s+batch\s+size\s+(?P<batch_size_bytes>\d+)\s+bytes)'
                        r'(,?\s+threshold\s+capacity\s+'
                        r'(?P<threshold_percent>\d+))?(\s+(?P<threshold_alert>alert))?'
                        r'(\s+,\s+(?P<immediate_write>immediate))?(\s+,\s+(?P<protected>protected))?'
                        r'(\s+,\s+(?P<notify>notify))?$')

        # Trap logging: level informational, 1570 message lines logged
        p10 = re.compile(r'^(?P<tag>Trap) +logging: +level +'
                         r'(?P<level>\S+), +(?P<message_lines_logged>\d+) '
                         r'+message +lines +logged$')

        # Logging to 192.168.1.3  (tcp port 1514, audit disabled,
        # Logging to 55.55.55.70  (Mgmt-vrf) (udp port 514, audit disabled,
        # Logging to 2001:DB8::1  (MGMT) (udp port 514, audit disabled,
        p11 = re.compile(r'^Logging +to (?P<logging_to>[\w\.\:]+) +'
                         r'(\((?P<vrf>(\S+))\) +)?'
                         r'\((?P<protocol>\S+) '
                         r'+port +(?P<port>\d+), +audit +(?P<audit>\S+),$')

        # link down),
        # authentication disabled, encryption disabled, link up),
        p12 = re.compile(r'^(authentication (?P<authentication>\w+), encryption (?P<encryption>\w+), )?link +(?P<link>\S+)\),$')

        # 787 message lines logged,
        p13 = re.compile(r'^(?P<message_lines_logged>\d+) +message +lines +logged,$')

        # 0 message lines rate-limited,
        p14 = re.compile(r'^(?P<message_lines_rate_limited>\d+) '
                         r'+message +lines +rate-limited,$')

        # 0 message lines dropped-by-MD,
        p15 = re.compile(r'^(?P<message_lines_dropped_by_md>\d+) '
                         r'+message +lines +dropped-by-MD,$')

        # xml disabled, sequence number disabled
        p16 = re.compile(r'^xml +(?P<xml>\S+), +sequence +number +(?P<sequence_number>\S+)$')

        # TLS Profiles:
        p17 = re.compile(r'^TLS\s+Profiles:$')

        # Profile Name:
        p18 = re.compile(r'^Profile +Name: +(?P<tls_profile_name>\S+)$')

        # Ciphersuites:  rsa-aes-cbc-sha2 ecdhe-rsa-aes-cbc-sha2 ecdhe-ecdsa-aes-gcm-sha2
        p19 = re.compile(r'^Ciphersuites: +(?P<tls_cipher_suites>.*)$')

        # Trustpoint:
        p20 = re.compile(r'^Trustpoint: +(?P<tls_trustpoint>\S+)$')

        # TLS version:
        p21 = re.compile(r'^TLS +version: +(?P<tls_version>\S+)$')

        # Logging Source-Interface:       VRF Name:
        p22 = re.compile(r'^Logging Source-Interface: +VRF +Name:$')

        # Vlan200
        p23 = re.compile(r'^(?P<interface>\S+)\s*(?P<vrf>\S+)?$')

        # Log Buffer (32000 bytes):
        p24 = re.compile(r'^Log +Buffer +\((?P<vrf>\d+) +bytes+\):$')

        ret_dict = {}
        logging_dict = {}
        outer_logging_dict = {}
        outer_logging_sources_dict = {}
        trap_dict = {}
        for line in out.splitlines():

            line = line.strip()

            # Syslog logging: enabled (0 messages dropped, 0 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sys_log_entry = ret_dict.setdefault("syslog_logging", {})
                logging_entry = ret_dict.setdefault("logging", {})

                outer_tls_profile_dict = {}
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

            # Console logging: disabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_tag = group['tag'].lower()
                logging_entry.setdefault(current_tag, {}).setdefault(
                    'status', group['status'].lower())
                continue

            # Buffer logging: disabled, xml disabled,
            m = p3.match(line)
            if m:
                group = m.groupdict()
                current_tag = group['tag'].lower()
                logging_entry.setdefault(current_tag, {}).setdefault(
                    'status', group['status'])
                logging_entry[current_tag].setdefault('xml', group['xml'])
                continue

            # Monitor logging: level debugging, 13 messages logged, xml disabled,
            # Console logging: level debugging, 9789 messages logged, xml disabled,
            m = p4.match(line)
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

            # filtering disabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if current_tag == 'trap':
                    logging_entry.setdefault(current_tag, {}).setdefault(
                        'logging_to',
                        {}).setdefault(current_logging_to, {}).setdefault(
                            'filtering',
                            group['filtering']
                        )
                else:
                    logging_entry.setdefault(current_tag, {}).setdefault(
                        'filtering', group['filtering'])
                continue

            # Exception Logging: size (4096 bytes)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['disabled']:
                    exception_dict = {'status': 'disabled'}
                else:
                    exception_dict = {'size_bytes': int(group['size_bytes'])}
                logging_entry['exception'] = exception_dict
                continue

            # Count and timestamp logging messages: disabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                logging_entry['count_and_time_stamp_logging_messages'] = group[
                    'count_and_time_stamp_logging_messages']
                continue

            # File logging: disabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                file_dict = {'status': group['status']}
                logging_entry['file'] = file_dict
                continue

            # Persistent logging: disabled
            # Persistent logging: enabled, url bootflash:/syslog, disk space 104857600 bytes, file size 10485760 bytes, batch size 4096 bytes

            m = p9.match(line)
            if m:
                group = m.groupdict()

                persistent_options = {}

                if group['threshold_percent']:
                    persistent_options['threshold_percent'] = int(group['threshold_percent'])

                if group['threshold_alert']:
                    persistent_options['threshold_alert'] = 'enabled'

                if group['immediate_write']:
                    persistent_options['immediate_write'] = 'enabled'

                if group['notify']:
                    persistent_options['notify'] = 'enabled'

                if group['protected']:
                    persistent_options['protected'] = 'enabled'

                for item in group:
                    if group[item]:
                        logging_entry.setdefault('persistent', {}).setdefault(
                            item,
                            int(group[item])
                            if 'bytes' in item else group[item])

                logging_entry['persistent'].update(persistent_options)
                continue

            # Trap logging: level informational, 1570 message lines logged
            m = p10.match(line)
            if m:
                group = m.groupdict()
                current_tag = group['tag'].lower()

                trap_dict['level'] = group['level']
                trap_dict['message_lines_logged'] = int(
                    group['message_lines_logged'])

                logging_entry['trap'] = trap_dict
                continue

            # Logging to 192.168.1.3  (tcp port 1514, audit disabled,
            # Logging to 55.55.55.70  (Mgmt-vrf) (udp port 514, audit disabled,
            m = p11.match(line)
            if m:
                group = m.groupdict()
                logging_dict = {}
                current_logging_to = group['logging_to']

                logging_dict['protocol'] = group['protocol']
                logging_dict['port'] = int(group['port'])
                logging_dict['audit'] = group['audit']

                if group['vrf']:
                    logging_dict['vrf'] = group['vrf']

                outer_logging_dict.update({current_logging_to: logging_dict})
                trap_dict['logging_to'] = outer_logging_dict
                continue

            # link down),
            # authentication disabled, encryption disabled, link up),
            m = p12.match(line)
            if m:
                group = m.groupdict()
                logging_dict['link'] = group['link']
                if group.get('authentication'):
                    logging_dict['authentication'] = group['authentication']
                if group.get('encryption'):
                    logging_dict['encryption'] = group['encryption']
                continue

            # 787 message lines logged,
            m = p13.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_logged'] = int(
                    group['message_lines_logged'])
                continue

            # 0 message lines rate-limited,
            m = p14.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_rate_limited'] = int(
                    group['message_lines_rate_limited'])
                continue

            # 0 message lines dropped-by-MD,
            m = p15.match(line)
            if m:
                group = m.groupdict()
                logging_dict['message_lines_dropped_by_md'] = int(
                    group['message_lines_dropped_by_md'])
                continue

            # xml disabled, sequence number disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                logging_dict['xml'] = group['xml']
                logging_dict['sequence_number'] = group['sequence_number']
                continue

            # TLS Profiles:
            m = p17.match(line)
            if m:
                continue

            # Profile name:
            m = p18.match(line)
            if m:
                group = m.groupdict()
                tls_profile_dict = {}
                current_tls_profile = {
                    group['tls_profile_name']: tls_profile_dict
                }

                ret_dict['tls_profiles'] = outer_tls_profile_dict
                outer_tls_profile_dict.update(current_tls_profile)
                continue

            # Ciphersuites: Default
            # Ciphersuites:  rsa-aes-cbc-sha2 ecdhe-rsa-aes-cbc-sha2 ecdhe-ecdsa-aes-gcm-sha2
            m = p19.match(line)
            if m:
                group = m.groupdict()
                tls_profile_dict['ciphersuites'] = group['tls_cipher_suites'].split()
                continue

            # Trustpoint:
            m = p20.match(line)
            if m:
                group = m.groupdict()
                tls_profile_dict['trustpoint'] = group['tls_trustpoint']
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                tls_profile_dict['tls_version'] = group['tls_version']
                continue

            # Logging Source-Interface:       VRF Name:
            m = p22.match(line)
            if m:
                # do nothing, but need to parse for skipping this line
                continue

            # Vlan200
            # Vlan200                         VRF-A
            m = p23.match(line)
            if m:
                group = m.groupdict()
                logging_source_dict = {}

                logging_source_iface = {
                    group['interface']: {}
                }

                if group['vrf']:
                    logging_source_dict['logging_configuration'] = group[
                        'interface'] + ':' + group['vrf']

                    logging_source_iface[group['interface']] = {
                        "vrf": group['vrf']
                    }
                else:
                    logging_source_dict['logging_configuration'] = group[
                        'interface']

                outer_logging_sources_dict.update(logging_source_iface)
                logging_dict['logging_source_interface'] = logging_source_dict
                trap_dict['logging_source_interface'] = outer_logging_sources_dict

                continue

            # Log Buffer (32000 bytes):
            m = p24.match(line)
            if m:
                group = m.groupdict()
                ret_dict['log_buffer_bytes'] = int(group['vrf'])

                continue

            if (
                line
                and not line.lower().startswith('no active')
                and not line.lower().startswith('no inactive')
                and not line.lower().startswith('show logging')
            ):
                log_lines.append(line)
                ret_dict['logs'] = log_lines
        return ret_dict


class ShowLoggingOnboardRpActiveUptimeSchema(MetaParser):

    '''Schema for:
        'show logging onboard Rp active uptime'
        'show logging onboard Rp {rp_standby} uptime'
        'show logging onboard switch {switch_num} {rp_active} uptime'
        'show logging onboard switch {switch_num} uptime'
    '''

    schema={
        'uptime_summary':{
            'first_customer_power_on':str,
            'number_of_reset':int,
            'number_of_slot_changes':int,
            'current_reset_reason':str,
            'current_reset_timestamp':str,
            'current_slot':int,
            'chassis_type':str,
            Any():{
                'years':int,
                'weeks':int,
                'days':int,
                'hours':int,
                'minutes':int,
            },
        },
    }

class ShowLoggingOnboardRpActiveUptime(ShowLoggingOnboardRpActiveUptimeSchema):
    """
    Parser for :
        'show logging onboard Rp active uptime'
        'show logging onboard Rp {rp_standby} uptime'
        'show logging onboard switch {switch_num} {rp_active} uptime'
        'show logging onboard switch {switch_num} uptime'

    """

    cli_command = ['show logging onboard switch {switch_num} {rp_active} uptime',
                   'show logging onboard switch {switch_num} uptime',
                   'show logging onboard Rp active uptime',
                   'show logging onboard rp {rp_standby} uptime']

    def cli(self,switch_num="",rp_active="",output=None,rp_standby=""):

        if output is None:
            # Build the command
            if rp_standby:
                cmd = self.cli_command[3].format(rp_standby=rp_standby)

            elif switch_num and rp_active:
                cmd = self.cli_command[0].format(switch_num=switch_num,rp_active=rp_active)

            elif switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)

            else:
                cmd = self.cli_command[2]

            # Execute the command
            output = self.device.execute(cmd)

        ret_dict ={}

        #First customer power on : 06/22/2021 12:35:40
        p1= re.compile(r'^First customer power on :?\s?(?P<first_customer_poweron>(\d+\/){2}\d+ \d+:\d+:\d+)$')

        #Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
        p2=re.compile(r'^Total uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        #Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
        p3=re.compile(r'^Total downtime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        #Number of resets        : 630
        p4=re.compile(r'^Number of resets\s+: (?P<numberof_reset>\d+)$')

        #Number of slot changes  : 1
        p5=re.compile(r'^Number of slot changes\s+: (?P<numberof_slot_changes>\d+)$')

        #Current reset reason    : Reload Command
        p6=re.compile(r'^Current reset reason\s+: (?P<current_reset_reason>[A-Z a-z\S]+)$')

        #Current reset timestamp : 10/06/2019 01:28:26
        p7=re.compile(r'^Current reset timestamp\s+: (?P<current_reset_timestamp>(\d+\/){2}\d+.*)$')

        #Current slot            : 1
        p8=re.compile(r'^Current slot\s+: (?P<current_slot>\d+)$')

        #Chassis type            : 80
        p9=re.compile(r'^Chassis type\s+: (?P<chassis_type>\w+)$')

        #Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
        p10=re.compile(r'^Current uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        for line in output.splitlines():
            line = line.strip()

            root_dict=ret_dict.setdefault('uptime_summary',{})

            #First customer power on : 06/22/2021 12:35:40
            m=p1.match(line)
            if m:
                group=m.groupdict()
                root_dict['first_customer_power_on']= group['first_customer_poweron']
                continue

            #Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('total_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            #Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('total_downtime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            #Number of resets        : 630
            m=p4.match(line)
            if m:
                group=m.groupdict()
                root_dict['number_of_reset']=int(group['numberof_reset'])
                continue

            #Number of slot changes  : 1
            m=p5.match(line)
            if m:
                group=m.groupdict()
                root_dict['number_of_slot_changes']=int(group['numberof_slot_changes'])
                continue

            #Current reset reason    : Reload Command
            m=p6.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_reset_reason'] =group['current_reset_reason']
                continue

            #Current reset timestamp : 10/06/2019 01:28:26
            m=p7.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_reset_timestamp'] =group['current_reset_timestamp']
                continue

            #Current slot            : 1
            m=p8.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_slot'] =int(group['current_slot'])
                continue

            ##Chassis type            : 80
            m=p9.match(line)
            if m:
                group=m.groupdict()
                root_dict['chassis_type'] = str(group['chassis_type'])
                continue

            #Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
            m=p10.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('current_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

        return ret_dict



class ShowLoggingOnboardRpActiveStatusSchema(MetaParser):
    '''Schema for:
        show logging onboard rp active status
        show logging onboard rp {rp_standby} status
    '''
    schema={
        'application':{
            Any():{
                'path': str,
                'status': bool,
            },
        },
    }


class ShowLoggingOnboardRpActiveStatus(ShowLoggingOnboardRpActiveStatusSchema):
    """
    Parser for :
        'show logging onboard rp active status'
        'show logging onboard rp {rp_standby} status'
    """

    cli_command = ['show logging onboard rp active status',
                   'show logging onboard rp {rp_standby} status']

    def cli(self, output=None, rp_standby=""):

        if output is None:
            # Build the command
            if rp_standby:
                cmd = self.cli_command[1].format(rp_standby=rp_standby)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        ret_dict ={}
        #Application Clilog:
        p1=re.compile(r'^Application (?P<application>\S+):$')

        #Cli enable status: enabled
        p2=re.compile(r'^Cli (?P<enable_status>enable status): (?P<status>\S+)$')

        # Path: /obfl0/
        p3=re.compile(r'^Path\: (?P<path>\S+)$')

        for line in output.splitlines():
            line=line.strip()

            #Application Clilog:
            m=p1.match(line)
            if m:
                group = m.groupdict()
                root_dict=ret_dict.setdefault('application', {}).setdefault(group['application'].lower(),{})
                continue

            #Cli enable status: enabled
            m=p2.match(line)
            if m:
                group = m.groupdict()
                status = True if \
                    group['status'].lower() == 'enabled' else\
                    False
                root_dict.setdefault('status',status)

            ## Path: /obfl0/
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict.setdefault('path',group['path'])
                continue

        return ret_dict


class ShowLoggingOnboardRpActiveTemperatureContinuousSchema(MetaParser):
    '''Schema for:
        show logging onboard rp active {include} continuous
        show logging onboard rp {rp_standby} {include} continuous
        show logging onboard rp active temperature continuous
        show logging onboard rp {rp_standby} temperature continuous
        show logging onboard rp active voltage continuous
        show logging onboard rp {rp_standby} voltage continuou
    '''

    schema={
        'application':str,
        Optional('temperature_sensors'):{
            Any():{
                'id': int,
                'history':{
                    Any():int,
                },
            },
        },
        Optional('voltage_sensors'):{
            Any():{
                'id': int,
                'history':{
                    Any():int,
                },
            },
        },
        Optional('error_message'):{
            Any():ListOf(str),
        },
    }


class ShowLoggingOnboardRpActiveTemperatureContinuous(ShowLoggingOnboardRpActiveTemperatureContinuousSchema):
    """
    Parser for :
        show logging onboard rp active {include} continuous
        show logging onboard rp {rp_standby} {include} continuous
        show logging onboard rp active temperature continuous
        show logging onboard rp {rp_standby} temperature continuous
        show logging onboard rp active voltage continuous
        show logging onboard rp {rp_standby} voltage continuous
    """

    cli_command = ['show logging onboard switch {switch_num} rp active {include} continuous',
                   'show logging onboard rp active {include} continuous',
                   'show logging onboard rp {rp_standby} {include} continuous']
    def cli(self, include="", switch_num="", output=None, rp_standby="",):

        if output is None:
            # Build the command
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num,include=include)
            elif rp_standby:
                cmd = self.cli_command[2].format(rp_standby=rp_standby,include=include)
            else:
                cmd = self.cli_command[1].format(include=include)

            # Execute the command
            output = self.device.execute(cmd)
        #TEMPERATURE CONTINUOUS INFORMATION
        p1 = re.compile(r'^(?P<continuous_info>[A-Z ]+) CONTINUOUS INFORMATION$')

        #No continuous data
        p2 = re.compile(r'^(?P<no_date>No continuous data|Application is not yet initialized.*)$')

        #Temp: CPU board           23
        p3 = re.compile(r'^(\w+\: )?(?P<sensor_name>\w+.*?)\s+(?P<sensor_count>\d+)$')

        #10/13/2019 21:58:42  40  38  33
        p4 = re.compile(r'^(?P<time>\d+\/\d+\/\d+ \d+:\d+:\d+)\s+(?P<sensor_value>[\d\s]+).*$')

        #10/29/2019 07:38:01 %IOSXE-2-DIAGNOSTICS_PASSED : Diagnostics Thermal passed
        p5 = re.compile(r'^(?P<time>\d+\/\d+\/\d+ \d+:\d+:\d+)\s+%(?P<info>\S+\s+\: [\w\s\/?]+)$')

        sensor_list=[]
        ret_dict = {}
        sensor_name_list=[]

        for line in output.splitlines():
            line = line.strip()

            #No continuous data
            m= p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('application',group['no_date'])
                continue

            #TEMPERATURE CONTINUOUS INFORMATION
            m=p1.match(line)
            if m:
                group1 = m.groupdict()
                ret_dict.setdefault('application',group1['continuous_info'])
                continue

            #10/13/2019 21:58:42  40  38  33
            m=p4.match(line)
            if m:
                group = m.groupdict()
                root_dict=ret_dict.setdefault((group1['continuous_info'].lower()).replace(' ','_')+"_sensors",{})
                if group['sensor_value']:
                    sensor_list=[]
                    for value in group['sensor_value'].split(" "):
                        if value.isdigit():
                            sensor_list.append(int(value))
                if len(sensor_list)==len(sensor_name_list):
                    for i in range(0,len(sensor_name_list)):
                        root_dict1=root_dict.setdefault(sensor_name_list[i],{})
                        root_dict1['id']=i
                        root_dict1.setdefault('history',{}).setdefault(group['time'],sensor_list[i])
                continue

            #Temp: CPU board           23
            m=p3.match(line)
            if m:
                group = m.groupdict()
                sensor_name_list.append(group['sensor_name'])
                continue

            #10/29/2019 07:38:01 %IOSXE-2-DIAGNOSTICS_PASSED : Diagnostics Thermal passed
            m=p5.match(line)
            if m:
                group=m.groupdict()
                root_dict=ret_dict.setdefault((group1['continuous_info'].lower()).replace(' ','_'),{})
                if group['time'] not in root_dict.keys():
                    root_dict[group['time']]=[group['info']]
                else:
                    root_dict[group['time']].append(group['info'])
                continue

        return ret_dict


class ShowLoggingOnboardRpActiveTemperatureDetailSchema(MetaParser):
    """Schema for show logging onboard rp [active|standby] [temperature|voltage] detail
                  show logging onboard rp [active|standby] [temperature|voltage]
                """

    schema = {
        Optional('number_of_sensors'): int,
        'sensors': {
            Any(): {
                'sensor_id': int,
                'normal_range_min': int,
                'normal_range_max': int,
                'maximum_sensor_value': int
            },
        }
    }



class ShowLoggingOnboardRpActiveTemperatureDetail(ShowLoggingOnboardRpActiveTemperatureDetailSchema):
    """Schema for show logging onboard rp [active|standby] [temperature|voltage] detail
                """

    cli_command = ['show logging onboard rp {rp} {feature} {detail}',
                   'show logging onboard rp {rp} {feature}']

    def cli(self, rp , feature ,detail = "", output=None):
        if output is None:
            if detail:
                cmd = self.cli_command[0].format(rp=rp,feature=feature,detail=detail)
            else:
                cmd = self.cli_command[1].format(rp=rp,feature=feature)

            output = self.device.execute(cmd)
        ret_dict = {}

        #Number of sensors          : 15
        p1 = re.compile(r'^Number +of +sensors +: +(?P<number_of_sensors>\d+)$')

        #--------------------------------------------------------------------------------
        #Sensor                    ID         Normal Range          Maximum Sensor Value
        #--------------------------------------------------------------------------------
        #SYSTEM OUTLET-A           35         0 - 70                121
        #SYSTEM OUTLET-B           36         0 - 60                121
        #SYSTEM INLET-A            37         0 - 50                121
        #SYSTEM INLET-B            38         0 - 45                121
        #Temp: UADP_0_0            39         0 - 105               121
        #DOPPLER0 UADP_0_2         6          0 - 124               91
        p2 = re.compile(r'^(?P<sensors>.+?)\s+(?P<sensor_id>\d+)\s+(?P<normal_range_min>\d+) - (?P<normal_range_max>\d+)\s+(?P<maximum_sensor_value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Number of sensors          : 15
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['number_of_sensors'] = int(group['number_of_sensors'])
                continue

            #--------------------------------------------------------------------------------
            #Sensor                    ID         Normal Range          Maximum Sensor Value
            #--------------------------------------------------------------------------------
            #SYSTEM OUTLET-A           35         0 - 70                121
            #SYSTEM OUTLET-B           36         0 - 60                121
            #SYSTEM INLET-A            37         0 - 50                121
            #SYSTEM INLET-B            38         0 - 45                121
            #Temp: UADP_0_0            39         0 - 105               121
            #DOPPLER0 UADP_0_2         6          0 - 124               91
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sensors = group.pop('sensors')
                temp_dict = ret_dict.setdefault('sensors', {}).setdefault(sensors, {})
                temp_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict

class ShowLoggingOnboardRpActiveUptimeDetailSchema(MetaParser):

    '''Schema for:
        show logging onboard Rp active uptime detail
    '''

    schema = {
        'uptime_summary': {
            'first_customer_power_on': str,
            'number_of_reset': int,
            'number_of_slot_changes': int,
            'current_reset_reason': str,
            'current_reset_timestamp': str,
            'current_slot': int,
            'chassis_type': str,
            Any(): {
                'years': int,
                'weeks': int,
                'days': int,
                'hours': int,
                'minutes': int,
            },
        },
        'uptime_continuous': {
            'time_stamp': {
                Any(): {
                'reset_reason': str,
                'uptime_days': str,
                'uptime_hours': str,
                'uptime_minutes': str,
                'uptime_weeks': str,
                'uptime_years': str,
                },
            },
        },
    }

class ShowLoggingOnboardRpActiveUptimeDetail(ShowLoggingOnboardRpActiveUptimeDetailSchema):
    """
    Parser for :
        'show logging onboard Rp active uptime detail'
    """
    cli_command = ['show logging onboard rp active uptime detail',
                   'show logging onboard switch {switch_num} rp active uptime detail']
    def cli(self, switch_num="", output=None):

        if output is None:
            # Build the command
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        ret_dict = {}

        # First customer power on : 06/22/2021 12:35:40
        p1 = re.compile(r'^First customer power on :?\s?(?P<first_customer_poweron>(\d+\/){2}\d+ \d+:\d+:\d+)$')

        # Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
        p2 = re.compile(r'^Total uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
        p3 = re.compile(r'^Total downtime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Number of resets        : 630
        p4 = re.compile(r'^Number of resets\s+: (?P<numberof_reset>\d+)$')

        # Number of slot changes  : 1
        p5 = re.compile(r'^Number of slot changes\s+: (?P<numberof_slot_changes>\d+)$')

        # Current reset reason    : Reload Command
        p6 = re.compile(r'^Current reset reason\s+: (?P<current_reset_reason>[A-Z a-z]+)$')

        # Current reset timestamp : 10/06/2019 01:28:26
        p7 = re.compile(r'^Current reset timestamp\s+: (?P<current_reset_timestamp>(\d+\/){2}\d+.*)$')

        # Current slot            : 1
        p8 = re.compile(r'^Current slot\s+: (?P<current_slot>\d+)$')

        # Chassis type            : 80
        p9 = re.compile(r'^Chassis type\s+: (?P<chassis_type>.+?)$')

        # Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
        p10 = re.compile(r'^Current uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # --------------------------------------------------------------------------------
        # Time Stamp          | Reset                       | Uptime
        # MM/DD/YYYY HH:MM:SS | Reason                      | years weeks days hours minutes
        # --------------------------------------------------------------------------------
        # 04/02/2022 21:32:31   EHSA standby down             0     0     0     0     13
        # 04/02/2022 22:11:32   Reload Command                0     0     0     0     38

        p11 = re.compile(r'^(?P<time_stamp>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<reset_reason>.+?)\s+?(?P<uptime_years>\d+)\s+(?P<uptime_weeks>\d+)\s+(?P<uptime_days>\d+)\s+(?P<uptime_hours>\d+)\s+(?P<uptime_minutes>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            root_dict=ret_dict.setdefault('uptime_summary',{})

            # First customer power on : 06/22/2021 12:35:40
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict['first_customer_power_on'] = group['first_customer_poweron']
                continue

            # Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('total_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('total_downtime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Number of resets        : 630
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_reset'] = int(group['numberof_reset'])
                continue

            # Number of slot changes  : 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_slot_changes'] = int(group['numberof_slot_changes'])
                continue

            # Current reset reason    : Reload Command
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_reason'] = group['current_reset_reason']
                continue

            # Current reset timestamp : 10/06/2019 01:28:26
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_timestamp'] = group['current_reset_timestamp']
                continue

            # Current slot            : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_slot'] = int(group['current_slot'])
                continue

            # Chassis type            : 80
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict['chassis_type'] = group['chassis_type']
                continue

            # Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('current_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue


            root_dict=ret_dict.setdefault('uptime_continuous',{})
            # --------------------------------------------------------------------------------
            # Time Stamp          | Reset                       | Uptime
            # MM/DD/YYYY HH:MM:SS | Reason                      | years weeks days hours minutes
            # --------------------------------------------------------------------------------
            # 04/02/2022 21:32:31   EHSA standby down             0     0     0     0     13
            # 04/02/2022 22:11:32   Reload Command                0     0     0     0     38

            m = p11.match(line)
            if m:
                group = m.groupdict()
                time_stamp=group.pop('time_stamp')
                temp_dict = root_dict.setdefault('time_stamp', {}).setdefault(time_stamp, {})
                temp_dict.update({k: v for k, v in group.items()})
                continue

        return ret_dict


class ShowLoggingProcessSmdReverseSchema(MetaParser):
    """
        Schema for
            * show logging process smd reverse
            * show logging process smd {switch} {mode} reverse
    """
    schema = {
        'requested_date': str,
        'requested_time': str,
        'hostname': str,
        'model': str,
        'version': str,
        'serial_number': str,
        'md_sn': str,
        'logs_date': {
            'days': int,
            'hours': int,
            'minutes': int,
            'seconds': int
        },
        'chassis': list,
        'utm_level': {
            'verbose': int,
            'noise': int,
            'invalid': int,
            'warning': int,
            'notice': int,
            'info': int,
            'debug': int,
            'emergency': int,
            'alert': int,
            'critical': int,
            'error': int,
        },
        'utm': {
            'luid_not_found': int,
            'pcap': int,
            'marker': int,
            'app_context': int,
            'tdl_tan': int,
            'module_id': int,
            'dyn_lib': int,
            'plain_text': int,
            'encoded': int,
            'skipped': int,
            'rendered': int,
            'total': int
        },
        'last_utm_timestamp': {
            'date': str,
            'time': str
        },
        'first_utm_timestamp': {
            'date': str,
            'time': str
        },
        'decoder': {
            'output': {
                'mrst_filter_rules': int,
                'utm_process_filter': str,
                'utm_to_process': int,
                'utf_to_process': int,
                'unique_streams': int
            },
            Optional('input'): {
                'date': {
                    Any(): {
                        'time': {
                            Any(): {
                                'message_type': str,
                                'message': str,
                                'process': str,
                                'pid': int
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLoggingProcessSmdReverse(ShowLoggingProcessSmdReverseSchema):
    """
        Parser for
            * show logging process smd reverse
            * show logging process smd {switch} {mode} reverse
    """
    cli_command = ['show logging process smd reverse',
                'show logging process smd {switch} {mode} reverse']

    def cli(self, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Logging display requested on 2023/04/27 21:34:18 (UTC) for Hostname:
        # [stack3-nyquist-1], Model: [C9300-48P], Version: [17.12.01], SN: [FOC21446Z0R], MD_SN: [FCW2146L00Y]
        p1 = re.compile(r'^Logging display requested on (?P<requested_date>\S+) (?P<requested_time>\S+) \(.+\) for Hostname:'
                        r' \[(?P<hostname>\S+)\], Model: \[(?P<model>\S+)\], Version: \[(?P<version>\S+)\],'
                        r' SN: \[(?P<serial_number>\S+)\], MD_SN: \[(?P<md_sn>\S+)\]$')

        # Displaying logs from the last 0 days, 0 hours, 10 minutes, 0 seconds
        p2 = re.compile(r'^Displaying logs from the last (?P<days>\d+) days, (?P<hours>\d+) hours,'
                        r' (?P<minutes>\d+) minutes, (?P<seconds>\d+) seconds$')

        # executing cmd on chassis 2 ...
        p3 = re.compile(r'^executing cmd on chassis (?P<chassisd>\d+).+$')

        #  UTM Level [VERBOSE / NOISE / INVALID] ............. 0 / 0 / 0
        p4 = re.compile(r'^UTM Level \[VERBOSE \/ NOISE \/ INVALID\]\s+\.+\s+(?P<verbose>\d+)'
                        r' \/ (?P<noise>\d+) \/ (?P<invalid>\d+)$')

        #  UTM Level [WARNING / NOTICE / INFO / DEBUG] ....... 0 / 0 / 0 / 0
        p5 = re.compile(r'^UTM Level \[WARNING \/ NOTICE \/ INFO \/ DEBUG\]\s+\.+\s+(?P<warning>\d+)'
                        r' \/ (?P<notice>\d+) \/ (?P<info>\d+) \/ (?P<debug>\d+)$')

        #  UTM Level [EMERGENCY / ALERT / CRITICAL / ERROR] .. 0 / 0 / 0 / 24
        p6 = re.compile(r'^UTM Level \[EMERGENCY \/ ALERT \/ CRITICAL \/ ERROR\]\s+\.+\s+(?P<emergency>\d+)'
                        r' \/ (?P<alert>\d+) \/ (?P<critical>\d+) \/ (?P<error>\d+)$')

        #  UTM [LUID NOT FOUND] .............. 0
        #  UTM [PCAP] ........................ 0
        #  UTM [MARKER] ...................... 0
        #  UTM [APP CONTEXT] ................. 0
        #  UTM [TDL TAN] ..................... 0
        #  UTM [MODULE ID] ................... 0
        #  UTM [DYN LIB] ..................... 0
        #  UTM [PLAIN TEXT] .................. 0
        #  UTM [ENCODED] ..................... 24
        p7 = re.compile(r'^UTM \[(?P<utm_name>.+)\] \.+ (?P<utm_value>\d+)$')

        #  UTM [Skipped / Rendered / Total] .. 153967 / 24 / 153991
        p8 = re.compile(r'^UTM \[Skipped \/ Rendered \/ Total\] \.+ (?P<skipped>\d+) \/ (?P<rendered>\d+) \/ (?P<total>\d+)$')

        #  Last UTM TimeStamp ................ 2023/04/27 21:34:17.692905538
        #  First UTM TimeStamp ............... 2023/04/27 20:57:07.075475821
        p9 = re.compile(r'^(?P<utm_timestamp>(Last|First) UTM TimeStamp) \.+ (?P<date>\S+) (?P<time>\S+)$')

        # ----------------- Decoder Output Information --------------
        p10 = re.compile(r'^\-+ Decoder Output Information \-+$')

        #  MRST Filter Rules ...... 1
        p11 = re.compile(r'^MRST Filter Rules \.+ (?P<mrst_filter_rules>\d+)$')

        #  UTM Process Filter ..... smd
        p12 = re.compile(r'^UTM Process Filter \.+ (?P<utm_process_filter>\w+)$')

        #  Total UTM To Process ... 153991
        p13 = re.compile(r'^Total UTM To Process \.+ (?P<utm_to_process>\d+)$')

        #  Total UTF To Process ... 2
        p14 = re.compile(r'^Total UTF To Process \.+ (?P<utf_to_process>\d+)$')

        #  Num of Unique Streams .. 1
        p15 = re.compile(r'^Num of Unique Streams \.+ (?P<unique_streams>\d+)$')

        # 2023/04/27 21:29:51.918681533 {smd_R0-0}{2}: [radius] [30442]: (ERR): Failed to mark Identifier for reuse
        p16 = re.compile(r'^(?P<date>\S+) (?P<time>\S+) \{.+\}\{.+\}: \[(?P<process>.+)\] \[(?P<pid>\d+)\]: \((?P<message_type>\S+)\): (?P<message>.+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Logging display requested on 2023/04/27 21:34:18 (UTC) for Hostname:
            # [stack3-nyquist-1], Model: [C9300-48P], Version: [17.12.01], SN: [FOC21446Z0R], MD_SN: [FCW2146L00Y]
            m = p1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Displaying logs from the last 0 days, 0 hours, 10 minutes, 0 seconds
            m = p2.match(line)
            if m:
                group_dict = m.groupdict()
                logs_date_dict = ret_dict.setdefault('logs_date', {})
                logs_date_dict['days'] = int(group_dict['days'])
                logs_date_dict['hours'] = int(group_dict['hours'])
                logs_date_dict['minutes'] = int(group_dict['minutes'])
                logs_date_dict['seconds'] = int(group_dict['seconds'])
                continue

            # executing cmd on chassis 2 ...
            m = p3.match(line)
            if m:
                ret_dict.setdefault('chassis', []).append(m.groupdict()['chassisd'])
                continue

            #  UTM Level [VERBOSE / NOISE / INVALID] ............. 0 / 0 / 0
            m = p4.match(line)
            if m:
                group_dict = m.groupdict()
                utm_level_dict = ret_dict.setdefault('utm_level', {})
                utm_level_dict['verbose'] = int(group_dict['verbose'])
                utm_level_dict['noise'] = int(group_dict['noise'])
                utm_level_dict['invalid'] = int(group_dict['invalid'])
                continue

            #  UTM Level [WARNING / NOTICE / INFO / DEBUG] ....... 0 / 0 / 0 / 0
            m = p5.match(line)
            if m:
                group_dict = m.groupdict()
                utm_level_dict['warning'] = int(group_dict['warning'])
                utm_level_dict['notice'] = int(group_dict['notice'])
                utm_level_dict['info'] = int(group_dict['info'])
                utm_level_dict['debug'] = int(group_dict['debug'])
                continue

            #  UTM Level [EMERGENCY / ALERT / CRITICAL / ERROR] .. 0 / 0 / 0 / 24
            m = p6.match(line)
            if m:
                group_dict = m.groupdict()
                utm_level_dict['emergency'] = int(group_dict['emergency'])
                utm_level_dict['alert'] = int(group_dict['alert'])
                utm_level_dict['critical'] = int(group_dict['critical'])
                utm_level_dict['error'] = int(group_dict['error'])
                continue

            #  UTM [LUID NOT FOUND] .............. 0
            #  UTM [PCAP] ........................ 0
            #  UTM [MARKER] ...................... 0
            #  UTM [APP CONTEXT] ................. 0
            #  UTM [TDL TAN] ..................... 0
            #  UTM [MODULE ID] ................... 0
            #  UTM [DYN LIB] ..................... 0
            #  UTM [PLAIN TEXT] .................. 0
            #  UTM [ENCODED] ..................... 24
            m = p7.match(line)
            if m:
                utm_dict = ret_dict.setdefault('utm', {})
                utm_dict[m.groupdict()['utm_name'].lower().replace(' ', '_')] = int(m.groupdict()['utm_value'])
                continue

            #  UTM [Skipped / Rendered / Total] .. 153967 / 24 / 153991
            m = p8.match(line)
            if m:
                group_dict = m.groupdict()
                utm_dict['skipped'] = int(group_dict['skipped'])
                utm_dict['rendered'] = int(group_dict['rendered'])
                utm_dict['total'] = int(group_dict['total'])
                continue

            #  Last UTM TimeStamp ................ 2023/04/27 21:34:17.692905538
            #  First UTM TimeStamp ............... 2023/04/27 20:57:07.075475821
            m = p9.match(line)
            if m:
                group_dict = m.groupdict()
                utm_timestamp_dict = ret_dict.setdefault(group_dict['utm_timestamp'].lower().replace(' ', '_'), {})
                utm_timestamp_dict['date'] = group_dict['date']
                utm_timestamp_dict['time'] = group_dict['time']
                continue

            # ----------------- Decoder Output Information --------------
            m = p10.match(line)
            if m:
                decoder_out_dict = ret_dict.setdefault('decoder', {}).setdefault('output', {})
                continue

            #  MRST Filter Rules ...... 1
            m = p11.match(line)
            if m:
                decoder_out_dict['mrst_filter_rules'] = int(m.groupdict()['mrst_filter_rules'])
                continue

            #  UTM Process Filter ..... smd
            m = p12.match(line)
            if m:
                decoder_out_dict['utm_process_filter'] = m.groupdict()['utm_process_filter']
                continue

            #  Total UTM To Process ... 153991
            m = p13.match(line)
            if m:
                decoder_out_dict['utm_to_process'] = int(m.groupdict()['utm_to_process'])
                continue

            #  Total UTF To Process ... 2
            m = p14.match(line)
            if m:
                decoder_out_dict['utf_to_process'] = int(m.groupdict()['utf_to_process'])
                continue

            #  Num of Unique Streams .. 1
            m = p15.match(line)
            if m:
                decoder_out_dict['unique_streams'] = int(m.groupdict()['unique_streams'])
                continue

            # 2023/04/27 21:29:51.918681533 {smd_R0-0}{2}: [radius] [30442]: (ERR): Failed to mark Identifier for reuse
            m = p16.match(line)
            if m:
                group_dict = m.groupdict()
                time_dict = ret_dict.setdefault('decoder', {}).setdefault('input', {}).setdefault('date', {}).setdefault(group_dict['date'], {})\
                    .setdefault('time', {}).setdefault(group_dict['time'], {})
                time_dict['process'] = group_dict['process']
                time_dict['pid'] = int(group_dict['pid'])
                time_dict['message_type'] = group_dict['message_type']
                time_dict['message'] = group_dict['message']
                continue

        return ret_dict

class ShowLoggingOnboardRpStandbyUptimeDetailSchema(MetaParser):

    '''Schema for:
        show logg onboard rp standby up detail
    '''

    schema = {
        'uptime_summary': {
            'first_customer_power_on': str,
            'number_of_reset': int,
            'number_of_slot_changes': int,
            'current_reset_reason': str,
            'current_reset_timestamp': str,
            'current_slot': int,
            'chassis_type': str,
            Any(): {
                'years': int,
                'weeks': int,
                'days': int,
                'hours': int,
                'minutes': int,
            },
        },
        'uptime_continuous': {
            'time_stamp': {
                Any(): {
                'reset_reason': str,
                'uptime_days': str,
                'uptime_hours': str,
                'uptime_minutes': str,
                'uptime_weeks': str,
                'uptime_years': str,
                },
            },
        },
    }

class ShowLoggingOnboardRpStandbyUptimeDetail(ShowLoggingOnboardRpStandbyUptimeDetailSchema):
    """
    Parser for :
        'show logging onboard rp standby uptime detail'
    """
    cli_command = ['show logging onboard rp standby uptime detail',
                   'show logging onboard switch {switch_num} rp standby uptime detail']
    def cli(self, switch_num="", output=None):

        if output is None:
            # Build the command
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        ret_dict = {}

        # First customer power on : 06/22/2021 12:35:40
        p1 = re.compile(r'^First customer power on :?\s?(?P<first_customer_poweron>(\d+\/){2}\d+ \d+:\d+:\d+)$')

        # Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
        p2 = re.compile(r'^Total uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
        p3 = re.compile(r'^Total downtime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Number of resets        : 630
        p4 = re.compile(r'^Number of resets\s+: (?P<numberof_reset>\d+)$')

        # Number of slot changes  : 1
        p5 = re.compile(r'^Number of slot changes\s+: (?P<numberof_slot_changes>\d+)$')

        # Current reset reason    : Reload Command
        p6 = re.compile(r'^Current reset reason\s+: (?P<current_reset_reason>[A-Z a-z]+)$')

        # Current reset timestamp : 10/06/2019 01:28:26
        p7 = re.compile(r'^Current reset timestamp\s+: (?P<current_reset_timestamp>(\d+\/){2}\d+.*)$')

        # Current slot            : 1
        p8 = re.compile(r'^Current slot\s+: (?P<current_slot>\d+)$')

        # Chassis type            : 80
        p9 = re.compile(r'^Chassis type\s+: (?P<chassis_type>.+?)$')

        # Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
        p10 = re.compile(r'^Current uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # --------------------------------------------------------------------------------
        # Time Stamp          | Reset                       | Uptime
        # MM/DD/YYYY HH:MM:SS | Reason                      | years weeks days hours minutes
        # --------------------------------------------------------------------------------
        # 04/02/2022 21:32:31   EHSA standby down             0     0     0     0     13
        # 04/02/2022 22:11:32   Reload Command                0     0     0     0     38

        p11 = re.compile(r'^(?P<time_stamp>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<reset_reason>.+?)\s+?(?P<uptime_years>\d+)\s+(?P<uptime_weeks>\d+)\s+(?P<uptime_days>\d+)\s+(?P<uptime_hours>\d+)\s+(?P<uptime_minutes>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            root_dict=ret_dict.setdefault('uptime_summary',{})

            # First customer power on : 06/22/2021 12:35:40
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict['first_customer_power_on'] = group['first_customer_poweron']
                continue

            # Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('total_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('total_downtime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Number of resets        : 630
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_reset'] = int(group['numberof_reset'])
                continue

            # Number of slot changes  : 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_slot_changes'] = int(group['numberof_slot_changes'])
                continue

            # Current reset reason    : Reload Command
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_reason'] = group['current_reset_reason']
                continue

            # Current reset timestamp : 10/06/2019 01:28:26
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_timestamp'] = group['current_reset_timestamp']
                continue

            # Current slot            : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_slot'] = int(group['current_slot'])
                continue

            # Chassis type            : 80
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict['chassis_type'] = group['chassis_type']
                continue

            # Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict1=root_dict.setdefault('current_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # --------------------------------------------------------------------------------
            # Time Stamp          | Reset                       | Uptime
            # MM/DD/YYYY HH:MM:SS | Reason                      | years weeks days hours minutes
            # --------------------------------------------------------------------------------
            # 04/02/2022 21:32:31   EHSA standby down             0     0     0     0     13
            # 04/02/2022 22:11:32   Reload Command                0     0     0     0     38

            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict=ret_dict.setdefault('uptime_continuous',{})
                time_stamp=group.pop('time_stamp')
                temp_dict = root_dict.setdefault('time_stamp', {}).setdefault(time_stamp, {})
                temp_dict.update({k: v for k, v in group.items()})
                continue

        return ret_dict

class ShowLoggingProcessSchema(MetaParser):
    """Schema for show logging onboard rp [active|syandby] [temperature|voltage] detail
                """

    schema = {
        'date_time': str,
        'hostname': str,
        'model': str,
        'version': str,
        'sn' : str,
        'md_sn': str,
        'time_period': str,
    }



class ShowLoggingProcess(ShowLoggingProcessSchema):
    """Schema for show logging onboard rp [active|standby] [temperature|voltage] detail
                """

    cli_command = 'show logging process {word} internal start last boot to-file {location}'

    def cli(self, word, location, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(word=word,location=location))

        ret_dict = {}

        #Logging display requested on 2024/08/22 04:14:42 (PDT) for Hostname: [hendrix], Model: [C9350-48HX], Version: [17.16.01], SN: [FOC27361DWU], MD_SN: [FOC2743Y44V]
        p1 = re.compile(r'^Logging +display +requested +on +'
                        r'(?P<date_time>\d+\/\d+\/\d+ +\d+\:\d+\:\d+ +\(\w+\)) +for +'
                        r'Hostname\: +\[(?P<hostname>\w+)\]\, +'
                        r'Model\: +\[(?P<model>\S+)\]\, +'
                        r'Version\: +\[(?P<version>\d+\.\d+\.\d+)\]\, +'
                        r'SN\: +\[(?P<sn>\S+)\]\, +MD_SN\: +\[(?P<md_sn>\S+)\]$')

        #Displaying logs from the last 2 days, 1 hours, 54 minutes, 14 seconds
        p2 = re.compile(r'^Displaying +logs +from +the +last +(?P<time_period>.*)$')


        for line in output.splitlines():
            line = line.strip()

            # Logging display requested on 2024/08/22 04:14:42 (PDT) for Hostname: [hendrix], Model: [C9350-48HX], Version: [17.16.01], SN: [FOC27361DWU], MD_SN: [FOC2743Y44V]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['date_time'] = group['date_time']
                ret_dict['hostname'] = group['hostname']
                ret_dict['model'] = group['model']
                ret_dict['version'] = group['version']
                ret_dict['sn'] =  group['sn']
                ret_dict['md_sn'] =  group['md_sn']
                continue

            # Displaying logs from the last 2 days, 1 hours, 54 minutes, 14 seconds
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['time_period'] =  group['time_period']
                continue

        return ret_dict


class ShowLoggingOnboardSlotUptimeSchema(MetaParser):
    """Schema for show logging onboard slot {slot} uptime latest"""
    schema = {
        'slot': {
            str: {
                'resets': ListOf(
                    {
                        'reset_reason': str,
                        'power_on': str
                    }
                )
            }
        }
    }



class ShowLoggingOnboardSlotUptime(ShowLoggingOnboardSlotUptimeSchema):
    """Parser for show logging onboard slot {slot} uptime latest"""

    cli_command = 'show logging onboard slot {slot} uptime latest'

    def cli(self, slot='R0', output=None):
        if output is None:
            cmd = self.cli_command.format(slot=slot)
            output = self.device.execute(cmd)

        parsed_dict = {}
        # R0      PowerCycle            05/17/25 15:40:12
        p1 = re.compile(r'^(?P<slot>\S+)\s+(?P<reset_reason>[\w\s]+)\s+(?P<power_on>\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})$')

        for line in output.splitlines():
            line = line.strip()
            # R0      PowerCycle            05/17/25 15:40:12
            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot_dict = parsed_dict.setdefault('slot', {}).setdefault(group['slot'], {})
                resets_list = slot_dict.setdefault('resets', [])
                resets_list.append({
                    'reset_reason': group['reset_reason'].strip(),
                    'power_on': group['power_on'].strip()
                })

        return parsed_dict

class ShowLoggingCountSchema(MetaParser):
    """Schema for:
        * 'show logging count'
    """
    schema = {
        'facility': {
            Any(): {
                'message_name': {
                    Any(): {
                        'severity': int,
                        'occurrences': int,
                        'last_time': str
                    }
                },
                Optional('total'): int
            }
        }
    }


class ShowLoggingCount(ShowLoggingCountSchema):
    """Parser for:
        * 'show logging count'
    """

    cli_command = 'show logging count'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize variables
        ret_dict = {}

        # Facility       Message Name                     Sev Occur      Last Time
        # ==================================================================================
        # SYS            CONFIG_I                           5    1 *May  1 06:13:57.803
        # SYS            LOGGINGHOST_STARTSTOP              6    2 *May  1 06:13:56.862
        # -------------  -------------------------------  ----------------------------------
        # SYS TOTAL                                              3
        p1 = re.compile(r'^(?P<facility>\S+)\s+(?P<message_name>[\S ]+?)\s+(?P<severity>\d+)\s+(?P<occurrences>\d+)\s+(?P<last_time>[\S ]+)$')
        # Facility  ,SYS TOTAL                                              3
        p2 = re.compile(r'^(?P<facility>\S+)\s+TOTAL\s+(?P<total>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Facility       Message Name                     Sev Occur      Last Time
            # ==================================================================================
            # SYS            CONFIG_I                           5    1 *May  1 06:13:57.803
            # SYS            LOGGINGHOST_STARTSTOP              6    2 *May  1 06:13:56.862
            # -------------  -------------------------------  ----------------------------------
            # SYS TOTAL                                                  3

            m = p1.match(line)
            if m:
                group = m.groupdict()
                facility = group['facility']
                message_name = group['message_name'].strip()
                severity = int(group['severity'])
                occurrences = int(group['occurrences'])
                last_time = group['last_time']

                facility_dict = ret_dict.setdefault('facility', {}).setdefault(facility, {})
                message_dict = facility_dict.setdefault('message_name', {}).setdefault(message_name, {})
                message_dict.update({
                    'severity': severity,
                    'occurrences': occurrences,
                    'last_time': last_time
                })
                continue

            # Facility  ,SYS TOTAL                                              3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                facility = group['facility']
                total = int(group['total'])

                facility_dict = ret_dict.setdefault('facility', {}).setdefault(facility, {})
                facility_dict['total'] = total
                continue

        return ret_dict

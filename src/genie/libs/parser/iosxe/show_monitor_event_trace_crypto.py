# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, ListOf, Optional, Any, Use
# parser utils
from genie.libs.parser.utils.common import Common

class ShowMonitorEventTraceCryptoMergedSchema(MetaParser):
    ''' Schema for show monitor event-trace crypto merged {word} {lines_count} {detail}
                   show monitor event-trace crypto merged {word} {lines_count}
                   show monitor event-trace crypto merged {word} '''
    schema = {
        'events': ListOf({
            'timestamp': str,
            'event_type': str,
            'message': str,
            Optional('traceback'): str,
        })
    }

class ShowMonitorEventTraceCryptoMerged(ShowMonitorEventTraceCryptoMergedSchema):
    """
    Parser for:
        show monitor event-trace crypto merged all detail
        show monitor event-trace crypto merged back 20 detail
        show monitor event-trace crypto merged latest
        show monitor event-trace crypto merged latest detail
    """
    cli_command = ["show monitor event-trace crypto merged {word} {lines_count} {detail}",
                   "show monitor event-trace crypto merged {word} {detail}",
                   "show monitor event-trace crypto merged {word}"]

    def cli(self, word='', lines_count='', detail='', output=None):
        if output is None:
            # Execute the command if output is not provided
            if lines_count and detail:
                cmd = self.cli_command[0].format(word=word,lines_count=lines_count, detail=detail)
            elif detail:
                    cmd = self.cli_command[1].format(word=word, detail=detail)
            else:
                cmd = self.cli_command[2].format(word=word)
            out = self.device.execute(cmd)
        else:
            out = output
        # Initialize the parsed dictionary
        parsed_dict = {}
        current_event = None
        # *Apr  3 23:53:30.376: pki_event: EST client initialized.
        p1 = re.compile(
            r'^\*(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+\.\d+):\s+(?P<event_type>\S+):\s+(?P<message>.+)$'
        )
        # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
        p2 = re.compile(
            r'^-Traceback=\s+(?P<traceback>.+)$'
        )
        
        for line in out.splitlines():
            line = line.strip()
    
            # *Apr  3 23:53:30.376: pki_event: EST client initialized.
            m1 = p1.match(line)
            if m1:
                # If previous event exists and traceback not yet added, append it
                if current_event:
                    parsed_dict.setdefault('events',[]).append(current_event)
                current_event = {
                    'timestamp': m1.group('timestamp'),
                    'event_type': m1.group('event_type'),
                    'message': m1.group('message'),
                }
                continue

            # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
            m2 = p2.match(line)
            if m2 and current_event:
                current_event['traceback'] = m2.group('traceback')
                continue

            # Append last event if exists
        if current_event:
            parsed_dict.setdefault('events',[]).append(current_event)

        return parsed_dict

class ShowMonitorEventTraceCryptoIpsecSchema(MetaParser):
    ''' Schema for show monitor event-trace crypto ipsec event latest
                   show monitor event-trace crypto ipsec event back 1:10'''
    schema = {
        'events': ListOf({
            'timestamp': str,
            'event_type': str,
            'message': str,
            Optional('details'): {
                Optional('session_id'): int,
                Optional('sa_action'): str,
                Optional('sa_dest'): str,
                Optional('sa_proto'): int,
                Optional('sa_spi'): str,
                Optional('sa_trans'): str,
                Optional('sa_conn_id'): int,
                Optional('sa_lifetime_k'): int,
                Optional('sa_lifetime_sec'): int,
                Optional('loc'): str,
                Optional('rem'): str,
                Optional('l_proxy'): str,
                Optional('r_proxy'): str,
                Optional('kmi_direction'): str,
                Optional('kmi_source'): str,
                Optional('kmi_destination'): str,
                Optional('kmi_type'): str,
                Optional('port_loc'): int,
                Optional('port_rem'): int,
                Optional('prot'): str,
            }
        })
    }

class ShowMonitorEventTraceCryptoIpsec(ShowMonitorEventTraceCryptoIpsecSchema):
    """
    Parser for:
        show monitor event-trace crypto ipsec event latest
        show monitor event-trace crypto ipsec event back 1:10
    """
    cli_command = ["show monitor event-trace crypto ipsec event latest",
                   "show monitor event-trace crypto ipsec event back {linenum_range}"]

    def cli(self, output=None, linenum_range=''):
        if output is None:
            if linenum_range:
                out = self.device.execute(self.cli_command[1].format(linenum_range=linenum_range))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Initialize the parsed dictionary
        parsed_dict = {}

        # *Apr  4 00:10:51.826:
        # IPSEC-EVENT:IPSEC-DELETE-SA:
        p1 = re.compile(
            r'^\*(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+\.\d+):\s+'
            r'(?P<event_type>\S+):\s+(?P<message>.+)$'
        )

        # sa delete : (sa) sa_dest = 30.1.1.1, sa_proto = 50, sa_spi = 0xB820B40F(3089150991)
        p2 = re.compile(
            r'^(?:SESSION ID:\s*(?P<session_id>\d+),\s+)?'
            r'sa\s+(?P<sa_action>create|delete)\s*:\s*\(sa\)\s+'
            r'sa_dest\s*=?\s*(?P<sa_dest>\S+)\s*,'
            r'\s*sa_proto\s*=?\s*(?P<sa_proto>\d+)\s*,'
            r'\s*sa_spi\s*=?\s*(?P<sa_spi>0x[a-fA-F0-9]+\(\d+\))\s*,'
            r'\s*sa_trans\s*=?\s*(?P<sa_trans>.+?)\s*,'
            r'\s*sa_conn_id\s*=?\s*(?P<sa_conn_id>\d+)\s*,'
            r'\s*sa_lifetime\(k/sec\)\s*=?\s*\((?P<sa_lifetime_k>\d+)/(?P<sa_lifetime_sec>\d+)\)'
        )

        # sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256
        p3 = re.compile(
            r'^(?:SESSION ID:\s*(?P<session_id>\d+),\s+)?'
            r'sa\s+(?P<sa_action>create|delete)\s*:\s*\(sa\),\s+'
            r'loc:\s*(?P<loc>\S+?)\s*,'
            r'\s*rem:\s*(?P<rem>\S+?)\s*,'
            r'\s*l_proxy:\s*(?P<l_proxy>\S+?)\s*,'
            r'\s*r_proxy:\s*(?P<r_proxy>\S+)'
        )

        # SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_DELETE_SAS, loc: 30.1.1.1, rem: 30.1.1.2, port loc/        # rem: 0/500, prot: DOI-3
        p4 = re.compile(
            r'^(?:SESSION ID:\s*(?P<session_id>\d+),\s+)?'
            r'KMI\s+(?P<kmi_direction>Sent|Received):\s+'
            r'(?P<kmi_source>[^->]+)->(?P<kmi_destination>[^:]+):'
            r'(?P<kmi_type>[^,]+)(?P<optional_part>.*)$'
        )
        # SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_DECR_COUNT
        p5 = re.compile(
            r'^(?:SESSION ID:\s*(?P<session_id>\d+),\s+)?'
            r'KMI\s+(?P<kmi_direction>Sent|Received):\s+'
            r'(?P<kmi_source>[^->]+)->(?P<kmi_destination>[^:]+):'
            r'(?P<kmi_type>.+)$'
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue
            # *Apr  4 00:10:51.826:
            # IPSEC-EVENT:IPSEC-DELETE-SA:
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                event_dict = {
                    'timestamp': groups['timestamp'],
                    'event_type': groups['event_type'],
                    'message': groups['message'].strip()
                }

                events_list = parsed_dict.setdefault('events', [])
                events_list.append(event_dict)

                msg = event_dict['message']
                details_dict = event_dict.setdefault('details', {})

                m2 = p2.match(msg)
                m3 = p3.match(msg)

                # sa delete : (sa) sa_dest = 30.1.1.1, sa_proto = 50, sa_spi = 0xB820B40F(3089150991)
                if m2:
                    details = m2.groupdict()
                    if details.get('session_id'): details_dict['session_id'] = int(details['session_id'])
                    details_dict.update({
                        'sa_action': details['sa_action'],
                        'sa_dest': details['sa_dest'],
                        'sa_proto': int(details['sa_proto']),
                        'sa_spi': details['sa_spi'],
                        'sa_trans': details['sa_trans'].strip(),
                        'sa_conn_id': int(details['sa_conn_id']),
                        'sa_lifetime_k': int(details['sa_lifetime_k']),
                        'sa_lifetime_sec': int(details['sa_lifetime_sec']),
                    })
                # sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256
                if m3:
                    details = m3.groupdict()
                    if details.get('session_id'): details_dict['session_id'] = int(details['session_id'])
                    details_dict.update({
                        'sa_action': details['sa_action'],
                        'loc': details['loc'],
                        'rem': details['rem'],
                        'l_proxy': details['l_proxy'],
                        'r_proxy': details['r_proxy'],
                    })
                else:
                    # SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_DELETE_SAS, loc: 30.1.1.1, rem: 30.1.1.                    #2, port loc/rem: 0/500, prot: DOI-3

                    m4 = p4.match(msg)
                    if m4:
                        details = m4.groupdict()
                        optional_part = details.pop('optional_part', '')

                        if details.get('session_id'):
                            details_dict['session_id'] = int(details['session_id'])
                        details_dict['kmi_direction'] = details['kmi_direction']
                        details_dict['kmi_source'] = details['kmi_source'].strip()
                        details_dict['kmi_destination'] = details['kmi_destination'].strip()
                        details_dict['kmi_type'] = details['kmi_type'].strip()

                        m_loc = re.search(r'loc:\s*(\S+)', optional_part)
                        if m_loc: details_dict['loc'] = m_loc.group(1).strip(',')

                        m_rem = re.search(r'rem:\s*(\S+)', optional_part)
                        if m_rem: details_dict['rem'] = m_rem.group(1).strip(',')

                        m_port = re.search(r'port\s+loc/rem:\s*(\d+)/(\d+)', optional_part)
                        if m_port:
                            details_dict['port_loc'] = int(m_port.group(1))
                            details_dict['port_rem'] = int(m_port.group(2))

                        m_prot = re.search(r'prot:\s*(\S+)', optional_part)
                        if m_prot: details_dict['prot'] = m_prot.group(1).strip(',')

                        m_lproxy = re.search(r'l_proxy:\s*(\S+)', optional_part)
                        if m_lproxy: details_dict['l_proxy'] = m_lproxy.group(1).strip(',')

                        m_rproxy = re.search(r'r_proxy:\s*(\S+)', optional_part)
                        if m_rproxy: details_dict['r_proxy'] = m_rproxy.group(1).strip(',')

                    else:
                        # SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_DECR_COUNT
                        m5 = p5.match(msg)
                        if m5:
                            details = m5.groupdict()
                            if details.get('session_id'):
                                details_dict['session_id'] = int(details['session_id'])
                            details_dict['kmi_direction'] = details['kmi_direction']
                            details_dict['kmi_source'] = details['kmi_source'].strip()
                            details_dict['kmi_destination'] = details['kmi_destination'].strip()
                            details_dict['kmi_type'] = details['kmi_type'].strip()

                if not details_dict:
                    del event_dict['details']

        return parsed_dict

class ShowMonitorEventTraceCryptoLatestDetailSchema(MetaParser):
    """Schema for show monitor event-trace crypto latest detail"""
    schema = {
        Optional('event_traces'): {
            Any(): {
                'status': str,
                Optional('reason'): str,
            }
        },
        Optional('interrupt_context_allocation_count'): int
    }

class ShowMonitorEventTraceCryptoLatestDetail(ShowMonitorEventTraceCryptoLatestDetailSchema):
    """Parser for show monitor event-trace crypto latest detail"""
    cli_command = "show monitor event-trace crypto latest detail"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        current_event_type = None

        # pki_event:
        p1 = re.compile(r'^(?P<event_type>\w+):$')

        # Tracing currently disabled, from exec command
        p2 = re.compile(r'^Tracing currently disabled, from (?P<reason>.+)$')

        # interrupt context allocation count = 0
        p3 = re.compile(r'^interrupt context allocation count = (?P<count>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match event type headers like "pki_event:"
            m = p1.match(line)
            if m:
                current_event_type = m.group('event_type')
                # Lazily create the parent dict and the entry for this event type
                parsed_dict.setdefault('event_traces', {}).setdefault(current_event_type, {})
                continue

            # Match "Tracing currently disabled..."
            m = p2.match(line)
            if m and current_event_type:
                groups = m.groupdict()
                event_section = parsed_dict.setdefault('event_traces', {}).setdefault(current_event_type, {})
                event_section['status'] = 'disabled'
                event_section['reason'] = groups['reason']
                continue

            # Match "interrupt context allocation count..."
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict['interrupt_context_allocation_count'] = int(groups['count'])
                continue

        if 'event_traces' in parsed_dict:
            for event, details in parsed_dict['event_traces'].items():
                if not details:
                    details['status'] = 'enabled_no_events'

        return parsed_dict

class ShowMonitorEventTraceCryptoIpsecEventAllSchema(MetaParser):
    ''' Schema for show monitor event-trace crypto ipsec event all '''
    schema = {
        'tracing_status': str,
        Optional('source'): str,
    }

class ShowMonitorEventTraceCryptoIpsecEventAll(ShowMonitorEventTraceCryptoIpsecEventAllSchema):
    """
    Parser for:
        show monitor event-trace crypto ipsec event all
    """
    cli_command = "show monitor event-trace crypto ipsec event all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Tracing currently disabled, from exec command
        p1 = re.compile(r'^Tracing currently (?P<status>disabled|enabled)(?:, from (?P<source>.+))?$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Tracing currently disabled, from exec command
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict['tracing_status'] = groups['status']
                if groups.get('source'):
                    parsed_dict['source'] = groups['source']
                continue

        return parsed_dict

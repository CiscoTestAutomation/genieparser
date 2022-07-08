''' show_perfmon.py

Parser for the following show commands:
    * show perfmon
    * show perfmon detail
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from pyats.configuration import setdefault

# =============================================
# Schema for 'show perfmon'
# =============================================
class ShowPerfmonSchema(MetaParser):
    """Schema for
        * show perfmon
        * show perfmon detail
    """

    schema = {
    	'perfmon': {
            'context': {
                Any(): {
                    'stats_per_sec': {
                        'xlates': {
                            'current': int,
                            'average': int
                        },
                        'connections': {
                            'total': {
                                'current': int,
                                'average': int
                            },
                            'tcp': {
                                'current': int,
                                'average': int
                            },
                            'udp': {
                                'current': int,
                                'average': int
                            },
                        },
                        'url_access': {
                            'current': int,
                            'average': int
                        },
                        'url_server_req': {
                            'current': int,
                            'average': int
                        },
                        'tcp': {
                            'intercept_established_conns': {
                                'current': int,
                                'average': int
                            },
                            'intercept_attempts': {
                                'current': int,
                                'average': int
                            },
                            'embryonic_conns_timeout': {
                                'current': int,
                                'average': int
                            },
                        },
                        'fixup': {
                            'tcp': {
                                'current': int,
                                'average': int
                            },
                            'ftp': {
                                'current': int,
                                'average': int
                            },
                            'http': {
                                'current': int,
                                'average': int
                            },
                        },
                        'aaa': {
                            'authen': {
                                'current': int,
                                'average': int
                            },
                            'author': {
                                'current': int,
                                'average': int
                            },
                            'account': {
                                'current': int,
                                'average': int
                            },
                        }
                    }
                },
            },
            'tcp_intercept' : {
                'valid_conns_rate': {
                    'current': str,
                    'average': str
                }
            },
            Optional('setup_rates_per_sec'): {
                'one_min': {
                    'total': int,
                    'tcp': int,
                    'udp': int
                },
                'five_min': {
                    'total': int,
                    'tcp': int,
                    'udp': int
                }
            }
        }
    }

# =============================================
# Parser for:
#     * show perfmon
#     * show perfmon detail
# =============================================
class ShowPerfmon(ShowPerfmonSchema):
    """Parser for
        * show perfmon
        * show perfmon detail
    """

    cli_command = [ 'show perfmon',
                    'show perfmon detail' ]

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Context: ctx1
        p1 = re.compile(r'Context: (?P<context>\S*)')
        
        # Xlates                                0/s          0/s
        # Connections                           0/s          0/s
        # TCP Conns                             0/s          0/s
        # UDP Conns                             0/s          0/s
        # URL Access                            0/s          0/s
        # URL Server Req                        0/s          0/s
        # TCP Fixup                             0/s          0/s
        # FTP Fixup                             0/s          0/s
        # HTTP Fixup                            0/s          0/s
        # TCP Intercept Established Conns       0/s          0/s
        # TCP Intercept Attempts                0/s          0/s
        # TCP Embryonic Conns Timeout           0/s          0/s
        # AAA Authen                            0/s          0/s
        # AAA Author                            0/s          0/s
        # AAA Account                           0/s          0/s
        p2 = re.compile(r'(?P<type>Xlates|Connections|TCP Conns|UDP Conns|'\
                        r'URL Access|URL Server Req|TCP Fixup|FTP Fixup|'\
                        r'HTTP Fixup|TCP Intercept Established Conns|'\
                        r'TCP Intercept Attempts|TCP Embryonic Conns Timeout|'\
                        r'AAA Authen|AAA Author|AAA Account)\s+(?P<current>\d+)/s\s+(?P<average>\d+)/s')
        
        # VALID CONNS RATE in TCP INTERCEPT:    Current      Average
        p3 = re.compile(r'VALID CONNS RATE in TCP INTERCEPT:\s*Current\s*Average')
        #                                        100.00%         97.38%

        p3_1 = re.compile(r'(?P<current>\S+)\s+(?P<average>\S+)')
        
        # Connections for 1 minute = 0/s; 5 minutes = 0/s
        # TCP Conns for 1 minute = 0/s; 5 minutes = 0/s
        # UDP Conns for 1 minute = 0/s; 5 minutes = 0/s
        p4 = re.compile(r'(?P<type>Connections|TCP Conns|UDP Conns) for 1 minute = (?P<conns_1min>\d+)/s; 5 minutes = (?P<conns_5min>\d+)/s')
        

        perfmon = None
        context = None
        valid_conns_line_matched = False

        for line in output.splitlines():
            line = line.strip()

            if line == '':
                continue

            # Context: ctx1

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ctx = groups['context']
                perfmon = ret_dict.setdefault('perfmon', {})
                context = perfmon.setdefault('context', {})\
                    .setdefault(ctx,{})
                continue
            
            # Xlates                                0/s          0/s
            # Connections                           0/s          0/s
            # TCP Conns                             0/s          0/s
            # UDP Conns                             0/s          0/s
            # URL Access                            0/s          0/s
            # URL Server Req                        0/s          0/s
            # TCP Fixup                             0/s          0/s
            # FTP Fixup                             0/s          0/s
            # HTTP Fixup                            0/s          0/s
            # TCP Intercept Established Conns       0/s          0/s
            # TCP Intercept Attempts                0/s          0/s
            # TCP Embryonic Conns Timeout           0/s          0/s
            # AAA Authen                            0/s          0/s
            # AAA Author                            0/s          0/s
            # AAA Account                           0/s          0/s

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                stats = context.setdefault('stats_per_sec', {})
                if type == 'Xlates':
                    container = stats.setdefault('xlates', {})
                elif type == 'Connections':
                    container = stats.setdefault('connections', {})\
                                    .setdefault('total',{})
                elif type == 'TCP Conns':
                    container = stats.setdefault('connections', {})\
                                    .setdefault('tcp',{})
                elif type == 'UDP Conns':
                    container = stats.setdefault('connections', {})\
                                    .setdefault('udp',{})
                elif type == 'URL Access':
                    container = stats.setdefault('url_access', {})
                elif type == 'URL Server Req':
                    container = stats.setdefault('url_server_req', {})
                elif type == 'TCP Fixup':
                    container = stats.setdefault('fixup', {})\
                                    .setdefault('tcp',{})
                elif type == 'FTP Fixup':
                    container = stats.setdefault('fixup', {})\
                                    .setdefault('ftp',{})
                elif type == 'HTTP Fixup':
                    container = stats.setdefault('fixup', {})\
                                    .setdefault('http',{})
                elif type == 'TCP Intercept Established Conns':
                    container = stats.setdefault('tcp', {})\
                                    .setdefault('intercept_established_conns',{})
                elif type == 'TCP Intercept Attempts':
                    container = stats.setdefault('tcp', {})\
                                    .setdefault('intercept_attempts',{})
                elif type == 'TCP Embryonic Conns Timeout':
                    container = stats.setdefault('tcp', {})\
                                    .setdefault('embryonic_conns_timeout',{})
                elif type == 'AAA Authen':
                    container = stats.setdefault('aaa', {})\
                                    .setdefault('authen',{})
                elif type == 'AAA Author':
                    container = stats.setdefault('aaa', {})\
                                    .setdefault('author',{})
                elif type == 'AAA Account':
                    container = stats.setdefault('aaa', {})\
                                    .setdefault('account',{})

                container['current'] = int(groups['current'])
                container['average'] = int(groups['average'])
                continue

            # VALID CONNS RATE in TCP INTERCEPT:    Current      Average
            m = p3.match(line)
            if m:
                 valid_conns_line_matched = True
                 continue

            #                                        100.00%         97.38%
            m = p3_1.match(line)
            if m and valid_conns_line_matched:
                valid_conns_line_matched = False
                groups = m.groupdict()
                rate = perfmon.setdefault('tcp_intercept', {})\
                    .setdefault('valid_conns_rate', {})
                rate['current'] = groups['current']
                rate['average'] = groups['average']
                continue


            # Connections for 1 minute = 0/s; 5 minutes = 0/s
            # TCP Conns for 1 minute = 0/s; 5 minutes = 0/s
            # UDP Conns for 1 minute = 0/s; 5 minutes = 0/s
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                setup = perfmon.setdefault('setup_rates_per_sec',{})
                one_min = setup.setdefault('one_min', {})
                five_min = setup.setdefault('five_min', {})
                if type == 'Connections':
                    field = 'total'
                elif type == 'TCP Conns':
                    field = 'tcp'
                elif type == 'UDP Conns':
                    field = 'udp'
                one_min[field] = int(groups['conns_1min'])
                five_min[field] = int(groups['conns_5min'])
                continue

        return ret_dict

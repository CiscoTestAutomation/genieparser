"""show_parser.py
   supported commands:
     * show parser encrypt file status
     * show parser statistics

"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional



# =============================================
# Parser for 'show parser encrypt file status'
# =============================================

class ShowParserEncryptFileStatusSchema(MetaParser):
    """
    Schema for show parser encrypt file status
    """

    schema = {
        'feature': bool,
        'file_format': str,
        'encryption_version':str,  
    }  

class ShowParserEncryptFileStatus(ShowParserEncryptFileStatusSchema):
    """ Parser for show parser encrypt file status"""

    # Parser for 'show parser encrypt file status'
    cli_command = 'show parser encrypt file status'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
        # initial variables
        ret_dict = {}
        
        #Feature:            Enabled
        p1=re.compile('^Feature\:\s+(?P<feature>Enabled|Disabled)$')
        
        #File Format:        Cipher text
        p2=re.compile('^File Format:\s+(?P<format>(Plain|Cipher) text)$')
        
        #Encryption Version: ver1 
        p3= re.compile('^Encryption Version:\s+(?P<encrypt_ver>\S+)$')
        
        for line in output.splitlines():
            line = line.strip() 
            
            #Feature:            Enabled
            m = p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict['feature'] = True if \
                    group['feature'] == 'Enabled' else\
                    False
                continue
                
            #File Format:        Cipher text
            m=p2.match(line)
            if m:
                group=m.groupdict()
                ret_dict['file_format'] =group['format']
                continue
            
            #Encryption Version: ver1 
            m=p3.match(line) 
            if m:
                group=m.groupdict()
                ret_dict['encryption_version']=group['encrypt_ver']
                continue
                
        return ret_dict


class ShowParserStatisticsSchema(MetaParser):
    """
    Schema for show parser statistics
    """

    schema = {
        'last_configuration_file_parsed': {
            'number_of_commands': int,
            'time': str
        },
        'parser_cache': {
            'status': str,
            'hits': str,
            'misses': str,
        },
        'active_startup_time': int,
        'standby_startup_time': int,
        'copy_to_running_config_time': int,
        'bulksync_time': int,
        'top_10_slowest_command': {
            Any(): {   # additional
                'function': str,
                'time': int,
                'command': str,
                'date': str,
                'time_with_seconds': str,
                'time_zone': str,
            }
        },
        'parser_last_bootup_cache_hits': {
            'bootup_hits': int,
            'bootup_misses': int,
            'bootup_clear_parser_cache': int,
        }
    }


class ShowParserStatistics(ShowParserStatisticsSchema):
    """ Parser for show parser statistics"""

    # Parser for 'show parser statistics'
    cli_command = 'show parser statistics'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
        # initial variables
        ret_dict = {}
        index = 0
        # Last configuration file parsed: Number of Commands: 15, Time: 12 ms
        # ^Last configuration file parsed: +(?P<last_config>(Number of Commands: +(?P<number_of_commands>\d+)+,+ Time: (?P<time>\d+)+ ms$))
        # p1 = re.compile(r'^Last configuration file parsed: Number of Commands:'
        #                r' +(?P<number_of_commands>\d+)+,+ Time: (?P<time>\d+)+ ms$')
        p1 = re.compile(r'^Last configuration file parsed: +(?P<last_config>Number of Commands: +(?P<number_of_commands>\d+)+,+ Time: (?P<time>\d+)+ ms$)')

        # Parser cache: enabled, 397 hits, 663 misses
        p2 = re.compile(r'^Parser cache: (?P<status>\w+)+, +(?P<hits>\d+)+ hits+, +(?P<misses>\d+)+ misses$')

        # Active startup time
        p3 = re.compile(r'^Active startup time:+\s+(?P<active_startup_time>\d+)$')
        # p12 = re.compile(r'^([^:]+)+:+\s+(\d+)$')

        # Standby startup time
        p4 = re.compile(r'^Standby startup time:+\s+(?P<standby_startup_time>\d+)$')

        # Copy to running-config time
        p5 = re.compile(r'^Copy to running-config time:+\s+(?P<copy_running_config_time>\d+)$')

        # BulkSync time
        p6 = re.compile(r'^Bulksync time:+\s+(?P<bulksync_time>\d+)$')

        # Top 10 commands
        p7 = re.compile(r'(?P<function>\S+)\s+(?P<time_ms>\d+)\s+(?P<command>.*)\s*(?P<date>\d{4}\/\d+\/\d+)\s+(?P<time_with_seconds>\d+:\d+:\d+.\d+)\s+(?P<timezone>\w+)')

        # Bootup hits
        p8 = re.compile(r'^Bootup hits:+\s+(?P<bootup_time>\d+)$')

        # Bootup misses
        p9 = re.compile(r'^Bootup misses:+\s+(?P<bootup_misses>\d+)$')

        # Bootup clear parser cache
        p10 = re.compile(r'^Bootup clear parser cache:+\s+(?P<bootup_clear_parser_cache>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last configuration file parsed
            m = p1.match(line)
            if m:
                group = m.groupdict()
                last_config_file = ret_dict.setdefault('last_configuration_file_parsed', {})
                last_config_file.update({'number_of_commands': int(group['number_of_commands'])})
                last_config_file.update({'time': group['time']})
                continue

            # Parser cache
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parser_cache_details = ret_dict.setdefault('parser_cache', {})
                parser_cache_details.update({'status': group['status']})
                parser_cache_details.update({'hits': group['hits']})
                parser_cache_details.update({'misses': group['misses']})
                continue

            # Active startup time
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'active_startup_time': int(group['active_startup_time'])})
                continue
            # Standby startup time
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'standby_startup_time': int(group['standby_startup_time'])})
                continue

            # Copy running-config time
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'copy_to_running_config_time': int(group['copy_running_config_time'])})
                continue

            # BulkSync time
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'bulksync_time': int(group['bulksync_time'])})
                continue

            # Top 10 commands
            m = p7.match(line)
            if m:
                group = m.groupdict()
                index += 1
                top_commands = ret_dict.setdefault('top_10_slowest_command', {}). \
                    setdefault(index, {})
                top_commands.setdefault('function', group['function'])
                top_commands.setdefault('time', int(group['time_ms']))
                top_commands.setdefault('command', group['command'])
                top_commands.update({'command': group['command'].strip()})
                top_commands.setdefault('date', group['date'])
                top_commands.setdefault('time_with_seconds', group['time_with_seconds'])
                top_commands.setdefault('time_zone', group['timezone'])
                continue

            # Bootup hits
            m = p8.match(line)
            if m:
                group = m.groupdict()
                parser_last_bootup = ret_dict.setdefault('parser_last_bootup_cache_hits', {})
                parser_last_bootup.update({'bootup_hits': int(group['bootup_time'])})
                continue

            # Bootup misses
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parser_last_bootup = ret_dict.setdefault('parser_last_bootup_cache_hits', {})
                parser_last_bootup.update({'bootup_misses': int(group['bootup_misses'])})
                continue

            # Bootup clear parser cache
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parser_last_bootup = ret_dict.setdefault('parser_last_bootup_cache_hits', {})
                parser_last_bootup.update({'bootup_clear_parser_cache': int(group['bootup_clear_parser_cache'])})
                continue

        return ret_dict

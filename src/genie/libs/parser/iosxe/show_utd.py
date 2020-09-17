# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowSdwanUtdEngineSchema(MetaParser):
    ''' Schema for show sdwan utd engine'''
    schema = {
        'version': str,
        'profile': str,
        'status': str,
        'reason': str,
        'memory_usage': float,
        'memory_status': str,
        Optional('engine_id'): {
            int: {
                'running': str,
                'status': str,
                'reason': str
                }
            }
        }


class ShowSdwanUtdEngine(ShowSdwanUtdEngineSchema):

    """ Parser for "show sdwan utd engine" """

    cli_command = "show sdwan utd engine"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)
        
        # utd-oper-data utd-engine-status version 1.0.6_SV2.9.13.0_XE17.3
        # utd-oper-data utd-engine-status profile Cloud-Medium
        # utd-oper-data utd-engine-status status utd-oper-status-green
        # utd-oper-data utd-engine-status reason ""
        # utd-oper-data utd-engine-status memory-usage 11.3
        # utd-oper-data utd-engine-status memory-status utd-oper-status-green
        p1 = re.compile(r'utd-oper-data utd-engine-status +(?P<key>[\S]+) +(?P<value>[\s\S]+)')

        # ID  RUNNING  STATUS                 REASON
        # 1   true     utd-oper-status-green 
        # 2   true     utd-oper-status-green 
        p2 = re.compile(r'^(?P<id>[\d]+)[\s]+(?P<running>[\w]+)[\s]+(?P<status>[s\S]+\S)(?P<reason>($|[\s\S]+))')

        parsed_dict = {}
        for line in output.splitlines():
            line = line.strip()
    
            # utd-oper-data utd-engine-status version 1.0.6_SV2.9.13.0_XE17.3
            # utd-oper-data utd-engine-status profile Cloud-Medium
            # utd-oper-data utd-engine-status status utd-oper-status-green
            # utd-oper-data utd-engine-status reason ""
            # utd-oper-data utd-engine-status memory-usage 11.3
            # utd-oper-data utd-engine-status memory-status utd-oper-status-green
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').lower()
                value = groups['value']
                if "memory-usage" in groups['key']:
                    key = groups['key'].replace('-', '_').lower()
                    value = float(groups['value'])

                parsed_dict.update({key: value})
                continue

            # ID  RUNNING  STATUS                 REASON
            # 1   true     utd-oper-status-green 
            # 2   true     utd-oper-status-green 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict = int(group['id'])

                connection_dict = parsed_dict.setdefault("engine_id", {}).setdefault(id_dict, {})
                keys = ['running', 'status', 'reason']
                for k in keys:
                    connection_dict[k] = group[k]

        return parsed_dict


class ShowUtdEngineStandardStatusSchema(MetaParser):
    ''' Schema for show utd engine standard status'''
    schema = {
        'engine_version': str,
        'profile': str,
        'system_memory': {
            'usage_percentage': float,
            'status': str
            },
        Optional('number_of_engines'): int,
        Optional('engine_id'): {
            int: {
                'running_status': str,
                'health': str,
                'reason': str
                }
            },
        'overall_system_status': str,
        'signature_update_status': {
            'current_signature_package_version': str,
            'last_update_status': str,
            'last_successful_update_time': str,
            'last_failed_update_time': str,
            'last_failed_update_reason': str,
            'next_update_scheduled_at': str,
            'current_status': str
            }
        }


class ShowUtdEngineStandardStatus(ShowUtdEngineStandardStatusSchema):

    """ Parser for "show utd engine standard status" """

    cli_command = "show utd engine standard status"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)
        
        # Engine version : 1.0.4_SV2.9.13.0_XE17.3
        # Profile : Cloud-Medium
        # Number of engines : 2
        # Overall system status: Green
        p1 = re.compile(r'(?P<key>[Engine version|Profile|Number of engines|Overall system status]+\w)(\s+:|:)+\s+(?P<value>[\s\S]+)$')

        # System memory :
        p2 = re.compile(r'^System +memory +:$')

        # Engine(#1): Yes Green None
        p3 = re.compile(r'^(?P<engine>[\s\S]+): +(?P<running_status>[\w]+) +(?P<health>[\w]+) +(?P<reason>[\s\S]+\S)$')

        # Signature update status
        p4 = re.compile(r'^Signature +update +status:$')

        # Usage : 8.80 %
        # Status : Green
        # Current signature package version: 29.0.c\n
        # Last update status: None\n
        # Last successful update time: None\n
        # Last failed update time: None\n
        # Last failed update reason: None\n
        # Next update scheduled at: None\n
        # Current status: Idle\n
        p5 = re.compile(r'^(?P<key>[\s\S]+\w)(\s+:|:)+\s+(?P<value>[\s\S]+)$')

        parsed_dict = {}
        last_dict_ptr = {}

        for line in output.splitlines():
            line = line.strip()

            # Engine version : 1.0.4_SV2.9.13.0_XE17.3
            # Profile : Cloud-Medium
            # Number of engines : 2
            # Overall system status: Green
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                parsed_dict.update({key: value})
                continue

            # System memory :
            m = p2.match(line)
            if m:
                group = m.groupdict()
                system_memory_dict = parsed_dict.setdefault('system_memory', {})
                last_dict_ptr = system_memory_dict
                continue

            # Engine(#1): Yes Green None
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict = int(group['engine'].strip(')').strip('Engine(#'))
                utd_engine_dict = parsed_dict.setdefault("engine_id", {}).setdefault(id_dict, {})
                keys = ['running_status', 'health', 'reason']
                for k in keys:
                    utd_engine_dict[k] = group[k]
                continue

            # Signature update status
            m = p4.match(line)
            if m:
                group = m.groupdict()
                signature_update_status_dict = parsed_dict.setdefault('signature_update_status', {})
                last_dict_ptr = signature_update_status_dict
                continue

            # Engine version : 1.0.4_SV2.9.13.0_XE17.3
            # Profile : Cloud-Medium
            # Usage : 8.80 %
            # Status : Green
            # Overall system status: Green
            # Current signature package version: 29.0.c\n
            # Last update status: None\n
            # Last successful update time: None\n
            # Last failed update time: None\n
            # Last failed update reason: None\n
            # Next update scheduled at: None\n
            # Current status: Idle\n
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').lower()
                value = groups['value']
                if "Usage" in groups['key']:
                    key = groups['key'].replace('-', '_').lower().replace('usage', 'usage_percentage')
                    value = float(groups['value'].strip('%'))

                last_dict_ptr.update({key: value})
        
        return parsed_dict
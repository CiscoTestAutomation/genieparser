# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema


class ShowSdwanAppqoeTcpoptStatusSchema(MetaParser):
    ''' Schema for show sdwan appqoe tcpopt status'''
    schema = {
        'status': {
            'tcp_opt_operational_state': str,
            'tcp_proxy_operational_state': str
            }
        }


class ShowSdwanAppqoeTcpoptStatus(ShowSdwanAppqoeTcpoptStatusSchema):

    """ Parser for "show sdwan appqoe tcpopt status" """
    
    cli_command = "show sdwan appqoe tcpopt status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Status
        p1 = re.compile(r'^Status$')
                                                                                                              
        # TCP OPT Operational State      : RUNNING
        # TCP Proxy Operational State    : RUNNING
        p2 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Status
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tcpopt_status_dict = parsed_dict.setdefault('status', {})
                last_dict_ptr = tcpopt_status_dict
                continue

            # TCP OPT Operational State      : RUNNING
            # TCP Proxy Operational State    : RUNNING
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict


class ShowSdwanAppqoeNatStatisticsSchema(MetaParser):
    ''' Schema for show sdwan appqoe nat-statistics'''
    schema = {
        'nat_statistics': {
            'insert_success': int,
            'delete_success': int,
            'duplicate_entries': int,
            'allocation_failures': int,
            'port_alloc_success': int,
            'port_alloc_failures': int,
            'port_free_success': int,
            'port_free_failures': int
        }
    }


class ShowSdwanAppqoeNatStatistics(ShowSdwanAppqoeNatStatisticsSchema):

    """ Parser for "show sdwan appqoe nat-statistics" """
    
    cli_command = "show sdwan appqoe nat-statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # NAT Statistics
        p1 = re.compile(r'^NAT Statistics$')

        #  Insert Success      : 518181
        #  Delete Success      : 518181
        #  Duplicate Entries   : 5
        #  Allocation Failures : 0
        #  Port Alloc Success  : 0
        #  Port Alloc Failures : 0
        #  Port Free Success   : 0
        #  Port Free Failures  : 0
        p2 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\d]+)$')

        for line in out.splitlines():
            line = line.strip()

            # NAT Statistics
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                nat_statistics_dict = parsed_dict.setdefault('nat_statistics', {})
                last_dict_ptr = nat_statistics_dict
                continue

            #  Insert Success      : 518181
            #  Delete Success      : 518181
            #  Duplicate Entries   : 5
            #  Allocation Failures : 0
            #  Port Alloc Success  : 0
            #  Port Alloc Failures : 0
            #  Port Free Success   : 0
            #  Port Free Failures  : 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict


class ShowSdwanAppqoeRmResourcesSchema(MetaParser):
    ''' Schema for show sdwan appqoe rm-resources'''
    schema = {
        'rm_resources': {
            'rm_global_resources': {
                'max_services_memory_kb': int,
                'available_system_memory_kb': int,
                'used_services_memory_kb': int,
                'used_services_memory_percentage': int,
                'system_memory_status': str,
                'num_sessions_status': str,
                'overall_htx_health_status': str
                },
            'registered_service_resources': {
                'tcp_resources': {
                    'max_sessions': int,
                    'used_sessions': int,
                    'memory_per_session': int
                    },
                'ssl_resources': {
                    'max_sessions': int,
                    'used_sessions': int,
                    'memory_per_session': int
                    }
                }
            }
        }


class ShowSdwanAppqoeRmResources(ShowSdwanAppqoeRmResourcesSchema):

    """ Parser for "show sdwan appqoe rm-resources" """
    
    cli_command = "show sdwan appqoe rm-resources"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # RM Resources
        p1 = re.compile(r'^RM +Resources$')

        # RM Global Resources :
        p2 = re.compile(r'^RM +Global +Resources +:$')

        # Registered Service Resources :
        p3 = re.compile(r'^Registered +Service +Resources +:$')

        # TCP Resources:
        p4 = re.compile(r'^TCP +Resources:$')

        # SSL Resources:
        p5 = re.compile(r'^SSL +Resources:$')

        # Max Services Memory (KB)    : 6434914
        # Available System Memory(KB) : 12869828
        # Used Services Memory (KB)   : 0
        # Used Services Memory (%)    : 0
        # System Memory Status        : GREEN
        # Num sessions Status         : GREEN
        # Overall HTX health Status   : GREEN
        # Max Sessions                : 11000
        # Used Sessions               : 0
        # Memory Per Session          : 128
        p6 = re.compile(r'^(?P<key>[\s\S]+\S) +: +(?P<value>[\s\S]+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # RM Resources
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                rm_resources_dict = ret_dict.setdefault('rm_resources', {})
                last_dict_ptr = rm_resources_dict
                continue

            # RM Global Resources :
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rm_global_resources_dict = rm_resources_dict.setdefault('rm_global_resources', {})
                last_dict_ptr = rm_global_resources_dict
                continue

            # Registered Service Resources :
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                registered_service_resources_dict = rm_resources_dict.setdefault('registered_service_resources', {})
                last_dict_ptr = registered_service_resources_dict
                continue

            # TCP Resources:
            m = p4.match(line)
            if m:
                tcp_resources_dict = registered_service_resources_dict.setdefault('tcp_resources', {})
                last_dict_ptr = tcp_resources_dict
                continue

            # SSL Resources:
            m = p5.match(line)
            if m:
                ssl_resources_dict = registered_service_resources_dict.setdefault('ssl_resources', {})
                last_dict_ptr = ssl_resources_dict
                continue

            # Max Services Memory (KB)    : 6434914
            # Available System Memory(KB) : 12869828
            # Used Services Memory (KB)   : 0
            # Used Services Memory (%)    : 0
            # System Memory Status        : GREEN
            # Num sessions Status         : GREEN
            # Overall HTX health Status   : GREEN
            # Max Sessions                : 11000
            # Used Sessions               : 0
            # Memory Per Session          : 128
            m = p6.match(line)
            if  m:
                groups = m.groupdict()
                key = groups['key'].replace('(KB)', '_kb').replace('(%)', 'percentage').\
                    replace(' ', '_').replace('__', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return ret_dict
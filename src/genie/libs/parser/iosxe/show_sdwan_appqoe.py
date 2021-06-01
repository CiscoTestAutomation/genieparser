# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional


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


class ShowSdwanAppqoeFlowAllSchema(MetaParser):
    ''' Schema for show sdwan appqoe flow all'''
    schema = {
        "active_flows": int,
        "vpn": {
            int: {
                "flow_id": {
                    int: {
                        "source_ip": str,
                        "source_port": int,
                        "destination_ip": str,
                        "destination_port": int,
                        "service": str,
                        }
                    },
                }
            },
        }


class ShowSdwanAppqoeFlowAll(ShowSdwanAppqoeFlowAllSchema):

    """ Parser for "show sdwan appqoe flow all" """

    cli_command = "show sdwan appqoe flow all"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        # Active Flows: 2139
        p1 = re.compile(r'^(?P<key>[\s\S]+\w):+\s+(?P<value>[\d]+)$')

        # Flow ID      VPN  Source IP:Port        Destination IP:Port   Service
        # 171064589     1    10.34.0.2:53350       10.36.211.203:443    TSU
        p2 = re.compile(
            r'^(?P<flow_id>[\d]+)[\s]+(?P<vpn>[\d]+)[\s]+(?P<source_ip>[\S]+\w)'
            r':(?P<source_port>[\d]+)[\s]+(?P<destination_ip>[\S]+\w)'
            r':(?P<destination_port>[\d]+)[\s]+(?P<service>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Active Flows: 2139
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                value = int(groups['value'])
                parsed_dict.update({key: value})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vpn_dict = parsed_dict.setdefault(
                            'vpn', {}).setdefault(int(group['vpn']), {})
                flow_id_dict = vpn_dict.setdefault(
                            'flow_id', {}).setdefault(int(group['flow_id']), {})
                keys = ['source_ip', 'source_port', 'destination_ip',
                        'destination_port', 'service']
                for k in keys:
                    try:
                        flow_id_dict[k] = int(group[k])
                    except ValueError:
                        flow_id_dict[k] = group[k]
        return parsed_dict

"""
    show_igmp_interface.py
    IOSXR parsers for the following show commands:

    * show igmp interface
    * show igmp vrf <vrf> interface
    * show igmp summary
    * show igmp vrf <vrf> summary
    * show igmp groups detail
    * show igmp vrf <vrf> groups detail
"""

# python
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)

#############################################################################
# Parser For Show Igmp Interface
#############################################################################

class ShowIgmpInterfaceSchema(MetaParser):
    """Schema for show igmp interface"""
    schema = {
        Any():{
            'oper_status': str,
            Optional('line_protocol'): str,
            'enabled': bool, 
            Optional('ipv4'): {
                Any(): {
                    Optional('ip'): str,
                    Optional('prefix_length'): int,
                },
            },  
            'igmp_state': str,
            Optional('igmp_version'): int,
            Optional('igmp_query_interval'): int,
            Optional('igmp_querier_timeout'): int,
            Optional('igmp_max_query_response_time'): int,
            Optional('igmp_query_response_interval'): int,
            Optional('igmp_activity_joins'): int,
            Optional('igmp_activity_leaves'): int,
            Optional('igmp_querying_router'): str,
            Optional('igmp_time_since_last_query_sent'): str,
            Optional('igmp_time_since_router_enabled'): str,
            Optional('igmp_time_since_last_report_received'): str
            },
        }


class ShowIgmpInterface(ShowIgmpInterfaceSchema):
    """Parser for show ip interface """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = ['show igmp interface', 'show igmp interface {interface}', 'show igmp vrf {vrf} interface']
    def cli(self, interface="", vrf="", output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif vrf:
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Loopback0 is up, line protocol is up
        p1 = re.compile(r'^(?P<interface>\S+) +is +(?P<enabled>[\w\s]+), '
                        r'+line +protocol +is +(?P<line_protocol>[\w\s]+)$') 

        # Internet address is 2.2.2.2/32
        p2 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[\d\.]+)'
                         '\/(?P<prefix_length>[\d]+))?$') 

        # IGMP is enabled on interface
        p3 = re.compile(r'^IGMP +is +(?P<igmp_state>[a-zA-Z]+) +on +interface$')
        
        # Current IGMP version is 3
        p4 = re.compile(r'^Current +IGMP +version +is +(?P<igmp_version>[\d]+)')
        
        # IGMP query interval is 60 seconds
        p5 = re.compile(r'^IGMP +query +interval +is +(?P<igmp_query_interval>[\d]+) +seconds$')
        
        # IGMP querier timeout is 125 seconds
        p6 = re.compile(r'^IGMP +querier +timeout +is +(?P<igmp_querier_timeout>[\d]+) +seconds$')
        
        # IGMP max query response time is 10 seconds
        p7 = re.compile(r'^IGMP +max +query +response +time +is +(?P<igmp_max_query_response_time>[\d]+) +seconds$')
        
        # Last member query response interval is 1 seconds
        p8 = re.compile(r'^Last +member +query +response +interval +is +(?P<igmp_query_response_interval>[\d]+) +seconds$')
        
        # IGMP activity: 6 joins, 0 leaves
        p9 = re.compile(r'^IGMP +activity: +(?P<igmp_activity_joins>[\d]+) +joins, +(?P<igmp_activity_leaves>[\d]+) +leaves$')
        
        # IGMP querying router is 2.2.2.2 (this system)
        p10 = re.compile(r'^IGMP +querying +router +is +(?P<igmp_querying_router>[\d\.]+)')
        
        # Time elapsed since last query sent 00:00:53
        p11 = re.compile(r'^Time +elapsed +since +last +query +sent +(?P<igmp_time_since_last_query_sent>[\d\:]+)$')
        
        # Time elapsed since IGMP router enabled 02:46:41
        p12 = re.compile(r'^Time +elapsed +since +IGMP +router +enabled +(?P<igmp_time_since_router_enabled>[\d\:]+)$')
        
        # Time elapsed since last report received 00:00:51
        p13 = re.compile(r'^Time +elapsed +since +last +report +received +(?P<igmp_time_since_last_report_received>[\d\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Loopback0 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                enabled = group['enabled']
                line_protocol = group['line_protocol']

                intf_dict = result_dict.setdefault(interface, {})
                if 'administratively down' in enabled or 'delete' in enabled:
                    intf_dict['enabled'] = False
                else:
                    intf_dict['enabled'] = True

                if line_protocol:
                    intf_dict['line_protocol'] = line_protocol
                    intf_dict['oper_status'] = line_protocol
                continue

            # Internet address is 2.2.2.2/32
            m = p2.match(line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']

                if ipv4:
                    ipv4_dict = intf_dict.setdefault('ipv4', {}).setdefault(ipv4, {})
                    ipv4_dict['ip'] = ip
                    ipv4_dict['prefix_length'] = int(prefix_length)
                continue

            # IGMP is enabled on interface
            m = p3.match(line)
            if m:
                igmp_state = m.groupdict()['igmp_state']
                intf_dict['igmp_state'] = igmp_state
                continue
                
            # Current IGMP version is 3
            m = p4.match(line)
            if m:
                igmp_version = m.groupdict()['igmp_version']
                intf_dict['igmp_version'] = int(igmp_version)
                continue
                
            # IGMP query interval is 60 seconds
            m = p5.match(line)
            if m:
                igmp_query_interval = m.groupdict()['igmp_query_interval']
                intf_dict['igmp_query_interval'] = int(igmp_query_interval)
                continue
                
            # IGMP querier timeout is 125 seconds
            m = p6.match(line)
            if m:
                igmp_querier_timeout = m.groupdict()['igmp_querier_timeout']
                intf_dict['igmp_querier_timeout'] = int(igmp_querier_timeout)
                continue
                
            # IGMP max query response time is 10 seconds
            m = p7.match(line)
            if m:
                igmp_max_query_response_time = m.groupdict()['igmp_max_query_response_time']
                intf_dict['igmp_max_query_response_time'] = int(igmp_max_query_response_time)
                continue
                
            # Last member query response interval is 1 seconds
            m = p8.match(line)
            if m:
                igmp_query_response_interval = m.groupdict()['igmp_query_response_interval']
                intf_dict['igmp_query_response_interval'] = int(igmp_query_response_interval)
                continue
                
            # IGMP activity: 6 joins, 0 leaves
            m = p9.match(line)
            if m:
                igmp_activity_joins = m.groupdict()['igmp_activity_joins']
                igmp_activity_leaves = m.groupdict()['igmp_activity_leaves']
                intf_dict['igmp_activity_joins'] = int(igmp_activity_joins)
                intf_dict['igmp_activity_leaves'] = int(igmp_activity_leaves)
                continue
                
            # IGMP querying router is 2.2.2.2 (this system)
            m = p10.match(line)
            if m:
                igmp_querying_router = m.groupdict()['igmp_querying_router']
                intf_dict['igmp_querying_router'] = igmp_querying_router
                continue
                
            # Time elapsed since last query sent 00:00:53
            m = p11.match(line)
            if m:
                igmp_time_since_last_query_sent = m.groupdict()['igmp_time_since_last_query_sent']
                intf_dict['igmp_time_since_last_query_sent'] = igmp_time_since_last_query_sent
                continue
               
            # Time elapsed since IGMP router enabled 02:46:41
            m = p12.match(line)
            if m:
                igmp_time_since_router_enabled = m.groupdict()['igmp_time_since_router_enabled']
                intf_dict['igmp_time_since_router_enabled'] = igmp_time_since_router_enabled
                continue
                
            # Time elapsed since last report received 00:00:51
            m = p13.match(line)
            if m:
                igmp_time_since_last_report_received = m.groupdict()['igmp_time_since_last_report_received']
                intf_dict['igmp_time_since_last_report_received'] = igmp_time_since_last_report_received
                continue
                                
        return result_dict
        
#############################################################################
# Parser For Show Igmp Summary 
#############################################################################

class ShowIgmpSummarySchema(MetaParser):
    """Schema for show igmp groups detail"""
    schema = {
        Any():{
            'Robustness_value': int,
            'GroupxInterfaces': int,
            'NoOfGroupsForVrf': int,
            'Supported_Interfaces': int,
            'Unsupported_Interfaces': int,
            'Enabled_Interfaces': int,
            'Disabled_Interfaces': int,
            'MTE_tuple_count': int,
            'Interface': {
                Any(): {
                    'Number_Groups': int,
                    'Max_Groups': int,
                },
            }, 
        }
    }
    
class ShowIgmpSummary(ShowIgmpSummarySchema):
    """Parser for show igmp summary"""
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = ['show igmp summary', 'show igmp vrf {vrf} summary']
    def cli(self, vrf='', output=None):
        '''
        parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Robustness Value 2
        p1 = re.compile(r'^Robustness +Value +(?P<Robustness_value>[\d]+)$') 

        # No. of Group x Interfaces 25
        p2 = re.compile(r'^No. +of +Group +x +Interfaces +(?P<GroupxInterfaces>[\d]+)$')
        
        # Maximum number of Groups for this VRF 50000
        p3 = re.compile(r'^Maximum +number +of +Groups +for +this +VRF +(?P<NoOfGroupsForVrf>[\d]+)$')
        
        # Supported Interfaces   : 9
        p4 = re.compile(r'^Supported +Interfaces +: +(?P<Supported_Interfaces>[\d]+)$')
        
        # Unsupported Interfaces : 0
        p5 = re.compile(r'^Unsupported +Interfaces +: +(?P<Unsupported_Interfaces>[\d]+)$')
        
        # Enabled Interfaces     : 3
        p6 = re.compile(r'^Enabled +Interfaces +: +(?P<Enabled_Interfaces>[\d]+)$')
        
        # Disabled Interfaces    : 6
        p7 = re.compile(r'^Disabled +Interfaces +: +(?P<Disabled_Interfaces>[\d]+)$')
        
        # MTE tuple count        : 0
        p8 = re.compile(r'^MTE +tuple +count +: +(?P<MTE_tuple_count>[\d]+)$')
        
        # Interface                       Number  Max #
        #                                 Groups  Groups
        # Loopback0                       6       25000
        # GigabitEthernet0/0/0/0.90       1       25000
        # GigabitEthernet0/0/0/1.90       1       25000
        # GigabitEthernet0/0/0/0.110      6       25000
        # GigabitEthernet0/0/0/0.115      4       25000
        # GigabitEthernet0/0/0/0.120      1       25000
        # GigabitEthernet0/0/0/1.110      5       25000
        # GigabitEthernet0/0/0/1.115      0       25000
        # GigabitEthernet0/0/0/1.120      1       25000
        
        p9 = re.compile(r'(?P<interface>(\S+)) +(?P<Number_Groups>(\d+)) +(?P<Max_Groups>(\d+))?$')
        
        for line in out.splitlines():
            line = line.strip()

            # Robustness Value 2
            m = p1.match(line)
            if m:
                Robustness_value = m.groupdict()['Robustness_value']
                igmp_dict = result_dict.setdefault('igmp', {})
                igmp_dict['Robustness_value'] = int(Robustness_value)
                continue
                
            # No. of Group x Interfaces 25
            m = p2.match(line)
            if m:
                GroupxInterfaces = m.groupdict()['GroupxInterfaces']
                igmp_dict['GroupxInterfaces'] = int(GroupxInterfaces)
                continue
                
            # Maximum number of Groups for this VRF 50000
            m = p3.match(line)
            if m:
                NoOfGroupsForVrf = m.groupdict()['NoOfGroupsForVrf']
                igmp_dict['NoOfGroupsForVrf'] = int(NoOfGroupsForVrf)
                continue
               
            # Supported Interfaces   : 9
            m = p4.match(line)
            if m:
                Supported_Interfaces = m.groupdict()['Supported_Interfaces']
                igmp_dict['Supported_Interfaces'] = int(Supported_Interfaces)
                continue
                
            # Unsupported Interfaces : 0
            m = p5.match(line)
            if m:
                Unsupported_Interfaces = m.groupdict()['Unsupported_Interfaces']
                igmp_dict['Unsupported_Interfaces'] = int(Unsupported_Interfaces)
                continue
                
            # Enabled Interfaces     : 3
            m = p6.match(line)
            if m:
                Enabled_Interfaces = m.groupdict()['Enabled_Interfaces']
                igmp_dict['Enabled_Interfaces'] = int(Enabled_Interfaces)
                continue
            
            # Disabled Interfaces    : 6
            m = p7.match(line)
            if m:
                Disabled_Interfaces = m.groupdict()['Disabled_Interfaces']
                igmp_dict['Disabled_Interfaces'] = int(Disabled_Interfaces)
                continue
                
            # MTE tuple count        : 0
            m = p8.match(line)
            if m:
                MTE_tuple_count = m.groupdict()['MTE_tuple_count']
                igmp_dict['MTE_tuple_count'] = int(MTE_tuple_count)
                continue
                
            # Interface                       Number  Max #
            #                                 Groups  Groups
            # Loopback0                       6       25000
            # GigabitEthernet0/0/0/0.90       1       25000
            # GigabitEthernet0/0/0/1.90       1       25000
            # GigabitEthernet0/0/0/0.110      6       25000
            # GigabitEthernet0/0/0/0.115      4       25000
            # GigabitEthernet0/0/0/0.120      1       25000
            # GigabitEthernet0/0/0/1.110      5       25000
            # GigabitEthernet0/0/0/1.115      0       25000
            # GigabitEthernet0/0/0/1.120      1       25000
            
            m = p9.match(line)
            if m:
                interface = m.groupdict()['interface']
                Number_Groups = m.groupdict()['Number_Groups']
                Max_Groups = m.groupdict()['Max_Groups']
                interface_dict = igmp_dict.setdefault('Interface', {}).setdefault(interface, {})
                interface_dict.update({'Number_Groups': int(Number_Groups), 'Max_Groups': int(Max_Groups)})
                continue
             
        return result_dict

        

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
        'vrf': {
            Any(): {
                'interfaces': {
                    Any():{
                        'oper_status': str,
                        Optional('line_protocol'): str,
                        'interface_status': str, 
                        Optional('ip_address'): str,  
                        'igmp_state': str,
                        Optional('igmp_version'): int,
                        Optional('igmp_query_interval'): int,
                        Optional('igmp_querier_timeout'): int,
                        Optional('igmp_max_query_response_time'): int,
                        Optional('last_member_query_response_interval'): int,
                        Optional('igmp_activity'): {
                            Optional('joins'): int,
                            Optional('leaves'): int
                        },
                        Optional('igmp_querying_router'): str,
                        Optional('igmp_querying_router_info'): str,
                        Optional('time_elapsed_since_last_query_sent'): str,
                        Optional('time_elapsed_since_router_enabled'): str,
                        Optional('time_elapsed_since_last_report_received'): str
                        },
                    }
                }
            }
        }


class ShowIgmpInterface(ShowIgmpInterfaceSchema):
    """Parser for show ip interface """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = [
            'show igmp interface', 
            'show igmp interface {interface}', 
            'show igmp vrf {vrf} interface',
            'show igmp vrf {vrf} interface {interface}'
    ]
    def cli(self, interface="", vrf="", output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            if interface and not vrf:
                cmd = self.cli_command[1].format(interface=interface)
                vrf = 'default'
            elif vrf and not interface:
                cmd = self.cli_command[2].format(vrf=vrf)
            elif vrf and interface:
                cmd = self.cli_command[3].format(vrf=vrf, interface=interface)
            else:
                cmd = self.cli_command[0]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Loopback0 is up, line protocol is up
        p1 = re.compile(r'^(?P<interface>\S+) +is +(?P<interface_status>[\w\s]+), '
                        r'+line +protocol +is +(?P<line_protocol>[\w\s]+)$') 

        # Internet address is 10.16.2.2/32
        p2 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ip_address>[\d\.\/]+)$')

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
        p8 = re.compile(r'^Last +member +query +response +interval +is +(?P<last_member_query_response_interval>[\d]+) +seconds$')
        
        # IGMP activity: 6 joins, 0 leaves
        p9 = re.compile(r'^IGMP +activity: +(?P<joins>[\d]+) +joins, +(?P<leaves>[\d]+) +leaves$')
        
        # IGMP querying router is 10.16.2.2 (this system)
        p10 = re.compile(r'^IGMP +querying +router +is +(?P<igmp_querying_router>[\d\.]+)+([\s*]+\(+(?P<igmp_querying_router_info>[\S\s*]+)+\))?$')
        
        # Time elapsed since last query sent 00:00:53
        p11 = re.compile(r'^Time +elapsed +since +last +query +sent +(?P<time_elapsed_since_last_query_sent>[\d\:]+)$')
        
        # Time elapsed since IGMP router enabled 02:46:41
        p12 = re.compile(r'^Time +elapsed +since +IGMP +router +enabled +(?P<time_elapsed_since_router_enabled>[\d\:]+)$')
        
        # Time elapsed since last report received 00:00:51
        p13 = re.compile(r'^Time +elapsed +since +last +report +received +(?P<time_elapsed_since_last_report_received>[\d\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Loopback0 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                interface_status = group['interface_status']
                line_protocol = group['line_protocol']

                intf_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                            setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['interface_status'] = interface_status
                if line_protocol:
                    intf_dict['line_protocol'] = line_protocol
                    intf_dict['oper_status'] = line_protocol
                continue

            # Internet address is 10.16.2.2/32
            m = p2.match(line)
            if m:
                ip_address = m.groupdict()['ip_address']
                intf_dict['ip_address'] = ip_address
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
                last_member_query_response_interval = m.groupdict()['last_member_query_response_interval']
                intf_dict['last_member_query_response_interval'] = int(last_member_query_response_interval)
                continue
                
            # IGMP activity: 6 joins, 0 leaves
            m = p9.match(line)
            if m:
                joins = m.groupdict()['joins']
                leaves = m.groupdict()['leaves']
                igmp_activity_dict = intf_dict.setdefault('igmp_activity', {})
                igmp_activity_dict['joins'] = int(joins)
                igmp_activity_dict['leaves'] = int(leaves)
                continue
                
            # IGMP querying router is 10.16.2.2 (this system)
            m = p10.match(line)
            if m:
                igmp_querying_router = m.groupdict()['igmp_querying_router']
                igmp_querying_router_info = m.groupdict()['igmp_querying_router_info']
                intf_dict['igmp_querying_router'] = igmp_querying_router
                if igmp_querying_router_info is not None:
                    intf_dict['igmp_querying_router_info'] = str(igmp_querying_router_info)
                continue
                
            # Time elapsed since last query sent 00:00:53
            m = p11.match(line)
            if m:
                time_elapsed_since_last_query_sent = m.groupdict()['time_elapsed_since_last_query_sent']
                intf_dict['time_elapsed_since_last_query_sent'] = time_elapsed_since_last_query_sent
                continue
               
            # Time elapsed since IGMP router enabled 02:46:41
            m = p12.match(line)
            if m:
                time_elapsed_since_router_enabled = m.groupdict()['time_elapsed_since_router_enabled']
                intf_dict['time_elapsed_since_router_enabled'] = time_elapsed_since_router_enabled
                continue
                
            # Time elapsed since last report received 00:00:51
            m = p13.match(line)
            if m:
                time_elapsed_since_last_report_received = m.groupdict()['time_elapsed_since_last_report_received']
                intf_dict['time_elapsed_since_last_report_received'] = time_elapsed_since_last_report_received
                continue
                                
        return result_dict
        
#############################################################################
# Parser For Show Igmp Summary 
#############################################################################

class ShowIgmpSummarySchema(MetaParser):
    """Schema for show igmp groups detail"""
    schema = {
        'vrf': {
            Any(): {
                'robustness_value': int,
                'no_of_group_x_interface': int,
                'maximum_number_of_groups_for_vrf': int,
                'supported_interfaces': int,
                'unsupported_interfaces': int,
                'enabled_interfaces': int,
                'disabled_interfaces': int,
                'mte_tuple_count': int,
                'interfaces': {
                    Any(): {
                        'number_groups': int,
                        'max_groups': int,
                    },
                }, 
            }
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

    cli_command = [
            'show igmp summary', 
            'show igmp vrf {vrf} summary'
    ]
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
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Robustness Value 2
        p1 = re.compile(r'^Robustness +Value +(?P<robustness_value>[\d]+)$') 

        # No. of Group x Interfaces 25
        p2 = re.compile(r'^No. +of +Group +x +Interfaces +(?P<no_of_group_x_interface>[\d]+)$')
        
        # Maximum number of Groups for this VRF 50000
        p3 = re.compile(r'^Maximum +number +of +Groups +for +this +VRF +(?P<maximum_number_of_groups_for_vrf>[\d]+)$')
        
        # Supported Interfaces   : 9
        p4 = re.compile(r'^Supported +Interfaces +: +(?P<supported_interfaces>[\d]+)$')
        
        # Unsupported Interfaces : 0
        p5 = re.compile(r'^Unsupported +Interfaces +: +(?P<unsupported_interfaces>[\d]+)$')
        
        # Enabled Interfaces     : 3
        p6 = re.compile(r'^Enabled +Interfaces +: +(?P<enabled_interfaces>[\d]+)$')
        
        # Disabled Interfaces    : 6
        p7 = re.compile(r'^Disabled +Interfaces +: +(?P<disabled_interfaces>[\d]+)$')
        
        # MTE tuple count        : 0
        p8 = re.compile(r'^MTE +tuple +count +: +(?P<mte_tuple_count>[\d]+)$')
        
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
        
        p9 = re.compile(r'(?P<interface>(\S+)) +(?P<number_groups>(\d+)) +(?P<max_groups>(\d+))?$')
        
        for line in out.splitlines():
            line = line.strip()

            # Robustness Value 2
            m = p1.match(line)
            if m:
                robustness_value = m.groupdict()['robustness_value']
                igmp_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})
                igmp_dict['robustness_value'] = int(robustness_value)
                continue
                
            # No. of Group x Interfaces 25
            m = p2.match(line)
            if m:
                no_of_group_x_interface = m.groupdict()['no_of_group_x_interface']
                igmp_dict['no_of_group_x_interface'] = int(no_of_group_x_interface)
                continue
                
            # Maximum number of Groups for this VRF 50000
            m = p3.match(line)
            if m:
                maximum_number_of_groups_for_vrf = m.groupdict()['maximum_number_of_groups_for_vrf']
                igmp_dict['maximum_number_of_groups_for_vrf'] = int(maximum_number_of_groups_for_vrf)
                continue
               
            # Supported Interfaces   : 9
            m = p4.match(line)
            if m:
                supported_interfaces = m.groupdict()['supported_interfaces']
                igmp_dict['supported_interfaces'] = int(supported_interfaces)
                continue
                
            # Unsupported Interfaces : 0
            m = p5.match(line)
            if m:
                unsupported_interfaces = m.groupdict()['unsupported_interfaces']
                igmp_dict['unsupported_interfaces'] = int(unsupported_interfaces)
                continue
                
            # Enabled Interfaces     : 3
            m = p6.match(line)
            if m:
                enabled_interfaces = m.groupdict()['enabled_interfaces']
                igmp_dict['enabled_interfaces'] = int(enabled_interfaces)
                continue
            
            # Disabled Interfaces    : 6
            m = p7.match(line)
            if m:
                disabled_interfaces = m.groupdict()['disabled_interfaces']
                igmp_dict['disabled_interfaces'] = int(disabled_interfaces)
                continue
                
            # MTE tuple count        : 0
            m = p8.match(line)
            if m:
                mte_tuple_count = m.groupdict()['mte_tuple_count']
                igmp_dict['mte_tuple_count'] = int(mte_tuple_count)
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
                number_groups = m.groupdict()['number_groups']
                max_groups = m.groupdict()['max_groups']
                interface_dict = igmp_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict.update({'number_groups': int(number_groups), 'max_groups': int(max_groups)})
                continue
             
        return result_dict
        
#############################################################################
# Parser For Show Groups Detail 
#############################################################################

class ShowIgmpGroupsDetailSchema(MetaParser):
    """Schema for show igmp groups detail"""
    schema = {
        'vrf': {
            Any(): {
                'interfaces': {
                    Any(): {
                        'group': {
                            Any(): {
                                'up_time': str,
                                'router_mode': str,
                                'router_mode_expires': str,
                                'host_mode': str,
                                'last_reporter': str,
                                Optional('suppress'): int,
                                Optional('source'): {
                                    Any(): {
                                        'up_time': str,
                                        'expire': str,
                                        Optional('forward'): str,
                                        Optional('flags'): str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIgmpGroupsDetail(ShowIgmpGroupsDetailSchema):
    """Parser for show igmp groups detail"""
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = [
            'show igmp groups detail', 
            'show igmp vrf {vrf} groups detail'
    ]    
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
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Interface:	Loopback0
        p1 = re.compile(r'^Interface:+[\s]+(?P<interface>[\S]+)$') 
        
        # Group:		224.0.0.2
        p2 = re.compile(r'^Group:+[\s*]+(?P<group>[\d\.]+)$')
        
        # Uptime:		02:44:55
        p3 = re.compile(r'^Uptime:+[\s*]+(?P<up_time>[\d\:\S]+)$')
        
        # Router mode:	EXCLUDE (Expires: never)
        p4 = re.compile(r'^Router mode:+[\s*]+(?P<router_mode>[\S]+)+([\s*]+\(Expires: +(?P<router_mode_expires>[\S]+)+\))?$')
        
        # Host mode:	EXCLUDE
        p5 = re.compile(r'^Host mode:+[\s*]+(?P<host_mode>[\S]+)$')
        
        # Last reporter:	10.16.2.2
        p6 = re.compile(r'^Last reporter:+[\s*]+(?P<last_reporter>[\d\.]+)$')
        
        # Suppress:	0
        p7 = re.compile(r'^Suppress:+[\s*]+(?P<suppress>[\d]+)$')
        
        # Source Address   Uptime    Expires   Fwd  Flags
        # 192.168.1.18     00:04:55  00:01:28  Yes  Remote
        p8 = re.compile(r'^(?P<source>[\d\.\:]+) +'
                             '(?P<up_time>[\w\.\:]+) +'
                             '(?P<expire>[\w\:]+) +'
                             '(?P<forward>\w+)? +'
                             '(?P<flags>\w+)?$')
        
        for line in out.splitlines():
            line = line.strip()

            # Interface:	Loopback0
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                intf_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                            setdefault('interfaces', {}).setdefault(interface, {})
                continue
            
            # Group:		224.0.0.2
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                group_dict = intf_dict.setdefault('group', {}).setdefault(group, {})
                continue
            
            # Uptime:		02:44:55
            m = p3.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                group_dict['up_time'] = up_time
                continue
            
            # Router mode:	EXCLUDE (Expires: never)
            m = p4.match(line)
            if m:
                router_mode = m.groupdict()['router_mode']
                router_mode_expires = m.groupdict()['router_mode_expires']
                group_dict['router_mode'] = router_mode
                group_dict['router_mode_expires'] = str(router_mode_expires)
                continue
             
            # Host mode:	EXCLUDE
            m = p5.match(line)
            if m:
                host_mode = m.groupdict()['host_mode']
                group_dict['host_mode'] = host_mode.lower()
                continue
            
            # Last reporter:	10.16.2.2
            m = p6.match(line)
            if m:
                last_reporter = m.groupdict()['last_reporter']
                group_dict['last_reporter'] = last_reporter
                continue
            
            # Suppress:	0
            m = p7.match(line)
            if m:
                suppress = m.groupdict()['suppress']
                group_dict['suppress'] = int(suppress)
                continue
              
            # Source Address   Uptime    Expires   Fwd  Flags
            # 192.168.1.18     00:04:55  00:01:28  Yes  Remote
            m = p8.match(line)
            if m:
                source = m.groupdict()['source']
                up_time = m.groupdict()['up_time']
                expire = m.groupdict()['expire']
                forward = m.groupdict()['forward']
                flags = m.groupdict()['flags']
                
                source_dict = group_dict.setdefault('source', {}).setdefault(source, {})
                source_dict['up_time'] = up_time
                source_dict['expire'] = expire
                source_dict['forward'] = forward
                source_dict['flags'] = flags
                continue
            
        return result_dict


# ==========================================================================
# Schema for 'show igmp groups summary'
# ==========================================================================
class ShowIgmpGroupsSummarySchema(MetaParser):
    """ Schema for show igmp [vrf <vrf>] groups summary. """

    schema = {
        'vrf':
            {Any():
                {'no_g_routes': int,
                 'no_sg_routes': int,
                 'no_group_x_intfs': int
                 },
             },
        }


# ==========================================================================
# Parser for 'show igmp groups summary'
# ==========================================================================
class ShowIgmpGroupsSummary(ShowIgmpGroupsSummarySchema):
    """
    Parser for show igmp [vrf <vrf>] groups summary.

    Parameters
    ----------
    device : Router
        Device to be parsed.
    vrf : str, optional
        Vrf to be summarized.
    output: str, optional
        Output to be parsed.

    Returns
    -------
    parsed_dict : dict
        Contains the CLI output parsed into a dictionary.

    Examples
    --------
    >>> dev.parse('show igmp groups summary')

    {'vrf':
        {'default':
            {'no_g_routes': 4,
             'no_group_x_intfs': 27,
             'no_sg_routes': 2
            }
        }
    }

    """

    cli_command = ["show igmp groups summary",
                   "show igmp vrf {vrf} groups summary"]

    def cli(self, vrf='', output=None):

        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # IGMP Route Summary for vrf default
        p1 = re.compile(r"IGMP +Route +Summary +for +vrf +(?P<vrf>\S+)")

        # No. of (*,G) routes = 4
        p2 = re.compile(r"No\. +of +\(\*,G\) +routes += +(?P<no_g_routes>\d+)")

        # No. of (S,G) routes = 2
        p3 = re.compile(r"No\. +of +\(\S,G\) +routes += +(?P<no_sg_routes>\d+)")

        # No. of Group x Interfaces = 27
        p4 = re.compile(r"No\. +of +Group +x +Interfaces += +"
                        r"(?P<no_group_x_intfs>\d+)")

        for line in out.splitlines():
            line = line.strip()

            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                vrf = group['vrf']
                vrf_dict = parsed_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {})
                continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                vrf_dict['no_g_routes'] = int(group['no_g_routes'])
                continue

            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                vrf_dict['no_sg_routes'] = int(group['no_sg_routes'])
                continue

            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                vrf_dict['no_group_x_intfs'] = int(group['no_group_x_intfs'])
                continue

        return parsed_dict

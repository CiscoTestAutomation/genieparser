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
                    Optional('prefix_length'): str,
                },
            },  
            'igmp_state': str,
            Optional('igmp_version'): str,
            Optional('igmp_query_interval'): str,
            Optional('igmp_querier_timeout'): str,
            Optional('igmp_max_query_response_time'): str,
            Optional('igmp_query_response_interval'): str,
            Optional('igmp_activity_joins'): str,
            Optional('igmp_activity_leaves'): str,
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

    cli_command = ['show igmp interface', 'show igmp interface {interface}']
    def cli(self, interface="", output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Loopback0 is up, line protocol is up
        p1 = re.compile(r'^(?P<interface>\S+) +is +(?P<enabled>[\w\s]+), '
                         '+line +protocol +is +(?P<line_protocol>[\w\s]+)$') 

        # Internet address is 2.2.2.2/32
        p2 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[\d\.]+)'
                         '\/(?P<prefix_length>[\d]+))?$') 

        # IGMP is enabled on interface
        p3 = re.compile(r'^IGMP +is +(?P<igmp_state>[a-zA-Z]+) +on +interface$')
        
        # Current IGMP version is 3
        p4 = re.compile(r'^Current +IGMP +version +is +(?P<igmp_version>(?P<ip>[\d]+))')
        
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
                    ipv4_dict['prefix_length'] = prefix_length
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
                intf_dict['igmp_version'] = igmp_version
                continue
                
            # IGMP query interval is 60 seconds
            m = p5.match(line)
            if m:
                igmp_query_interval = m.groupdict()['igmp_query_interval']
                intf_dict['igmp_query_interval'] = igmp_query_interval
                continue
                
            # IGMP querier timeout is 125 seconds
            m = p6.match(line)
            if m:
                igmp_querier_timeout = m.groupdict()['igmp_querier_timeout']
                intf_dict['igmp_querier_timeout'] = igmp_querier_timeout
                continue
                
            # IGMP max query response time is 10 seconds
            m = p7.match(line)
            if m:
                igmp_max_query_response_time = m.groupdict()['igmp_max_query_response_time']
                intf_dict['igmp_max_query_response_time'] = igmp_max_query_response_time
                continue
                
            # Last member query response interval is 1 seconds
            m = p8.match(line)
            if m:
                igmp_query_response_interval = m.groupdict()['igmp_query_response_interval']
                intf_dict['igmp_query_response_interval'] = igmp_query_response_interval
                continue
                
            # IGMP activity: 6 joins, 0 leaves
            m = p9.match(line)
            if m:
                igmp_activity_joins = m.groupdict()['igmp_activity_joins']
                igmp_activity_leaves = m.groupdict()['igmp_activity_leaves']
                intf_dict['igmp_activity_joins'] = igmp_activity_joins
                intf_dict['igmp_activity_leaves'] = igmp_activity_leaves
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
        

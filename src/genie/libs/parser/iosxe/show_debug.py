'''  show_debug.py
IOSXE parsers for the  show debug:
'''

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf
from genie import parsergen


# ======================================================
# Parser for 'show debug '
# ======================================================

class ShowDebugSchema(MetaParser):
    schema = {
        Optional('iosxe_conditional_debug_configs'):str, 
        Optional('conditional_debug_state'): str,
        Optional('hsrp'): {
            'hsrp_errors_debugging': str,
            'hsrp_events_debugging': {
                'status': str,
                Optional('types'): ListOf(str)
            },
            'hsrp_packets_debugging': {
                'status': str,
                Optional('types'): ListOf(str)
            }
        }
    }

class ShowDebug(ShowDebugSchema):
    """ Parser for 'show debug' """

    cli_command = 'show debug'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #IOSXE Conditional Debug Configs:
        p1 = re.compile(r'^IOSXE Conditional Debug Configs:(?: (?P<status>\S+))?$')

        #Conditional Debug Global State: Stop
        p2 = re.compile(r'^Conditional Debug Global State: (?P<conditional_debug_state>\w+)$')

        #IOSXE Packet Tracing Configs:
        p3 = re.compile(r'^IOSXE Packet Tracing Configs:(?: (?P<status>\S+))?$')

        #HSRP Errors debugging is on
        p4 = re.compile(r'^HSRP Errors debugging is (?P<hsrp_errors_debugging>\w+)$')

        #HSRP Events debugging is on
        p5 = re.compile(r'^HSRP Events debugging is (?P<hsrp_events_debugging>\w+)$')

        #(protocol, neighbor, redundancy, track, ha, arp, interface)
        p6 = re.compile(r'^\((?P<types>[^)]+)\)$')

        #HSRP Packets debugging is on
        p7 = re.compile(r'^HSRP Packets debugging is (?P<hsrp_packets_debugging>\w+)$')
        
        result = {}
        context = None

        for line in output.splitlines():
            line = line.strip()

            #IOSXE Conditional Debug Configs:
            m = p1.match(line)
            if m:
                if m.group('status'):
                    result['iosxe_conditional_debug_configs'] = m.group('status')
                continue

            #Conditional Debug Global State: Stop
            m = p2.match(line)
            if m:
                if m.group('conditional_debug_state'):
                 result['conditional_debug_state'] = m.group('conditional_debug_state')
                continue

            #IOSXE Packet Tracing Configs:
            m = p3.match(line)
            if m:
                if m.group('status'):
                    result['iosxe_packet_tracing_configs'] = m.group('status')
                continue

            # HSRP Errors debugging is on
            m = p4.match(line)
            if m:
                if m.group('hsrp_errors_debugging'):
                    result.setdefault('hsrp', {})['hsrp_errors_debugging'] = m.group('hsrp_errors_debugging')
                continue

            # HSRP Events debugging is on
            m = p5.match(line)
            if m:
                if m.group('hsrp_events_debugging'):
                    result.setdefault('hsrp', {}).setdefault('hsrp_events_debugging', {})['status'] = m.group('hsrp_events_debugging')
                    context = 'hsrp_events_debugging'
                continue

            # HSRP Packets debugging is on
            m = p7.match(line)
            if m:
                if m.group('hsrp_packets_debugging'):
                    result.setdefault('hsrp', {}).setdefault('hsrp_packets_debugging', {})['status'] = m.group('hsrp_packets_debugging')
                    context = 'hsrp_packets_debugging'
                continue

            #(protocol, neighbor, redundancy, track, ha, arp, interface)
            m = p6.match(line)
            if m and context:
                types_list = [x.strip() for x in m.group('types').split(',')]
                result['hsrp'][context]['types'] = types_list
                context = None  
            continue
        
        return result
    
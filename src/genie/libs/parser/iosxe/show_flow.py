''' show_flow.py

IOSXE parsers for the following show commands:
    * show flow monitor {name} cache format table

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# =========================================================
# Schema for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitorSchema(MetaParser):
    ''' Schema for "show flow monitor {name} cache format table" '''

    schema = {
        'cache_type': str,
        'cache_size': int,
        'current_entries': int,
        'high_water_mark': int,
        'flows_added': int,
        'flows_aged': int,
        'ipv4_src_addr': {
            Any(): {
                'ipv4_dst_addr': {
                    Any(): {
                        'trns_src_port': int,
                        'trns_dst_port': int,
                        'ip_tos': str,
                        'ip_port': int,
                        'bytes_long': int,
                        'pkts_long': int
                    }
                }
            }
        }
    }

# =========================================================
# Parser for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitor(ShowFlowMonitorSchema):
    ''' Parser for
      "show flow monitor {name} cache format table"
    '''

    cli_command = 'show flow monitor {name} cache format table'

    def cli(self, name, output=None):
        if output is None:
            cmd = self.cli_command.format(name=name)
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Cache type:                               Normal (Platform cache)
        p1 = re.compile(r'^Cache +type: +(?P<cache_type>[\S\s]+)$')
        
        # Cache size:                                   16
        p2 = re.compile(r'^Cache +size: +(?P<cache_size>\d+)$')

        # Current entries:                               1
        p3 = re.compile(r'^Current +entries: +(?P<current_entries>\d+)$')

        # High Watermark:                                1
        p4 = re.compile(r'^High +Watermark: +(?P<high_water_mark>\d+)$')

        # Flows added:                                   1
        p5 = re.compile(r'^Flows +added: +(?P<flows_added>\d+)$')

        # Flows aged:                                   0
        p6 = re.compile(r'^Flows +aged: +(?P<flows_aged>\d+)$')

        # 1.1.1.10         22.10.10.1                    0              0  0xC0         89                   100                     1
        p7 = re.compile(r'^(?P<ipv4_src_addr>\S+) +(?P<ipv4_dst_addr>\S+) +'
                        '(?P<trns_src_port>\d+) +(?P<trns_dst_port>\d+) +'
                        '(?P<ip_tos>\S+) +(?P<ip_port>\d+) +(?P<bytes_long>\d+) +'
                        '(?P<pkts_long>\d+)$')
        for line in out.splitlines():

            line = line.strip()
            
            # Cache type:                               Normal (Platform cache)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_type': group['cache_type']})
                continue
            
            # Cache size:                                   16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_size': int(group['cache_size'])})
                continue
            
            # Current entries:                               1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_entries': int(group['current_entries'])})
                continue

            # High Watermark:                                1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'high_water_mark': int(group['high_water_mark'])})
                continue
            
            # Flows added:                                   1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_added': int(group['flows_added'])})
                continue
            
            # Flows aged:                                   0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_aged': int(group['flows_aged'])})
                continue
            
            # 1.1.1.10         22.10.10.1                    0              0  0xC0         89                   100                     1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ipv4_dst_addr_dict = ret_dict.setdefault('ipv4_src_addr', {}).\
                    setdefault(group['ipv4_src_addr'], {}).\
                    setdefault('ipv4_dst_addr', {}).\
                    setdefault(group['ipv4_dst_addr'], {})
                
                ipv4_dst_addr_dict.update({'trns_src_port': int(group['trns_src_port'])})
                ipv4_dst_addr_dict.update({'trns_dst_port': int(group['trns_dst_port'])})
                ipv4_dst_addr_dict.update({'ip_tos': group['ip_tos']})
                ipv4_dst_addr_dict.update({'ip_port': int(group['ip_port'])})
                ipv4_dst_addr_dict.update({'bytes_long': int(group['bytes_long'])})
                ipv4_dst_addr_dict.update({'pkts_long': int(group['pkts_long'])})
                continue

        return ret_dict
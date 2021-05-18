"""ping.py

JunOS parsers for the following show commands:
    * monitor interface traffic
"""
# Python
import re
import time

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema)
""" Schema for:
            * monitor interface traffic
"""
class MonitorInterfaceTrafficSchema(MetaParser):
    schema = {
        Optional("no-output"):bool,
        Optional("monitor-time"): {
            Any(): {
                "hostname": str,
                "seconds": str,
                Optional("interface"): {
                    Any(): {
                        "link": str,
                        "input-packets": int,
                        Optional("input-pps"): int,
                        "output-packets": int,
                        Optional("output-pps"): int,
                    }
                }
            }
        } 
    }

""" Parser for:
            * monitor interface traffic
"""
class MonitorInterfaceTraffic(MonitorInterfaceTrafficSchema):
    
    cli_command = ['monitor interface traffic']

    def cli(self, output=None, timeout=10):
        if not output:
            self.device.sendline(self.cli_command[0])
            try:
                out = self.device.expect(
                    [r'{}[\S\s]+Time:\s+\S+'.format(self.device._hostname)],
                    timeout=timeout).match_output
                skip_timeout=False
            except AttributeError:
                out = self.device.expect(
                    [r'{}[\S\s]+Time:\s+\S+'.format(self.device._hostname)],
                    timeout=timeout)
                skip_timeout=True
            ansi_escape = re.compile(r'(\x00|\x9B|\x1B\[[0-?]*[ -\/]*[@-~])')
            out = ansi_escape.sub('\t', out)
            self.device.sendline('q')
            if not skip_timeout:
                time.sleep(5)
            self.device.expect('.*')
        else:
            out = output

        ret_dict = {}
        monitor_time_sub_dict = {}
        
        p1 = re.compile(r'^(?P<hostname>\S+)\s+Seconds:\s+(?P<seconds>\d+)$')

        p2 = re.compile(r'^(?P<interface>\S+)\s+(?P<link>Up|Down)\s+'
            r'(?P<input_packets>\d+)(\s+\((?P<input_pps>\d+)\))?\s+'
            r'(?P<output_packets>\d+)(\s+\((?P<output_pps>\d+)\))?$')
        
        p3 = re.compile(r'Time:\s+(?P<monitor_time>\S+)$')
        
        for line in out.splitlines():
            line = line.strip()

            if line == '{master}':
                return {'no-output':True}

            m = p1.match(line)
            if m:
                group = m.groupdict()
                seconds = group['seconds']
                hostname = group['hostname']
                monitor_time_sub_dict = {}
                monitor_time_sub_dict.update({'hostname': hostname})
                monitor_time_sub_dict.update({'seconds': seconds})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict = monitor_time_sub_dict.setdefault('interface', {}). \
                    setdefault(group['interface'], {})
                interface_dict.update({'link': group['link']})
                interface_dict.update({'input-packets': int(group['input_packets'])})
                input_pps = group['input_pps']
                if input_pps:
                    interface_dict.update({'input-pps': int(input_pps)})
                interface_dict.update({'output-packets': int(group['output_packets'])})
                output_pps = group['output_pps']
                if output_pps:
                    interface_dict.update({'output-pps': int(output_pps)})
                continue
            
            m = p3.search(line)
            if m:
                group = m.groupdict()
                monitor_time = group['monitor_time']
                monitor_time_dict = ret_dict.setdefault('monitor-time', {}). \
                    setdefault(monitor_time, monitor_time_sub_dict)
                continue

        return ret_dict
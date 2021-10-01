"""monitor.py
Iosxr parsers for the following show commands:
    * monitor interface {interface}
"""
# Python
import re
import time

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)
from genie.libs.parser.utils.common import Common

""" Schema for:
      * monitor interface {interface}
"""

class MonitorInterfaceInterfaceSchema(MetaParser):
    schema = {
    "monitor_time": {
        Any(): {
            "hostname": str,
            "sys_up_time": str,
            Optional("protocol"): str,
            Optional("line_protocol_status"): str,
            Optional("interface_status"): str,
            Optional("encapsulation"): str,
            Optional("interface"): {
                Any(): {
                    Optional("interface_status"): str,
                    Optional("input_bps"): int,
                    Optional("output_bps"): int,
                    Optional("input_bps_percent"): float,
                    Optional("output_bps_percent"): float,
                    Optional("input_bytes"): float,
                    Optional("input_bytes_unit"): str,
                    Optional("output_bytes"): float,
                    Optional("output_bytes_unit"): str,
                    Optional("input_delta"): int,
                    Optional("output_delta"): int,
                    Optional("traffic_stats"): {
                        "input_packets": int,
                        "input_packets_delta": int,
                        "input_pps": int,
                        "input_bytes": int,
                        "input_bytes_delta": int,
                        "input_kbps_rate": int,
                        "input_kbps_delta": float,
                        "output_packets": int,
                        "output_packets_delta": int,
                        "output_pps": int,
                        "output_bytes": int,
                        "output_bytes_delta": int,
                        "output_kbps_rate": int,
                        "output_kbps_delta": float
                    },
                    Optional("error_stats"):{
                        "input_total": int,
                        "input_total_delta": int,
                        "input_crc": int,
                        "input_crc_delta": int,
                        Optional("input_frame"): int,
                        Optional("input_frame_delta"): int,
                        "input_overrun": int,
                        "input_overrun_delta": int,
                        "output_total": int,
                        "output_total_delta": int,
                        Optional("output_underrun"): int,
                        Optional("output_underrun_delta"): int
                    }
                }
            },
        }
    }
}


""" Parser for:
      * monitor interface {interface}
"""
class MonitorInterfaceInterface(MonitorInterfaceInterfaceSchema):

    cli_command = ['monitor interface {interface}']

    def cli(self, output=None, interface=None, timeout=10):

        if output is None:
            self.device.sendline(self.cli_command[0].format(interface=interface))
            try:
                out = self.device.expect(
                    [r"{}\s+Monitor\sTime:[\s\S]+Quit='q'".format(self.device._hostname)],
                    timeout=timeout).match_output
                skip_timeout = False
            except AttributeError:
                out = self.device.expect(
                    [r"{}\s+Monitor\sTime:[\s\S]+Quit='q'".format(self.device._hostname)],\
                    timeout=timeout)
                skip_timeout = True
            self.device.sendline('q')
            if not skip_timeout:
                time.sleep(5)
            self.device.expect('.*')
        else:
            out = output

        #Initialize dictionaries
        ret_dict = {}

        #Initialize flag
        control_flag = None

        # F17-ASR9922          Monitor Time: 00:00:00          SysUptime: 09:47:06
        p1 = re.compile(r'^(?P<hostname>[\S]+)\s+Monitor Time:\s+(?P<monitor_time>'
                        r'[\S]+)\s+SysUptime:\s+(?P<sys_up_time>[\S]+)$')

        # Protocol:General
        p2 = re.compile(r'^Protocol:(?P<protocol>\S+)$')

        # Hu0/0/0/0             22000/  0%    23000/  0%   114.6M/0        280.5M/0
        p3 = re.compile(r'^(?P<interface>\S+)\s+(?P<input_bps>[\d]+)\/\s+?(?P<input_bps_percent>[\S]+)'
                        r'%\s+(?P<output_bps>[\d]+)\/\s+?(?P<output_bps_percent>[\S]+)%\s+'
                        r'(?P<input_bytes>[\d\.]+)(?P<int_bytes>\w)?\/(?P<input_delta>[\d]+)\s+'
                        r'(?P<output_bytes>[\d\.]+)(?P<out_bytes>\w)?\/(?P<output_delta>[\d]+)$')

        # Gi0/0/0/1            (statistics not available)
        p3_1 = re.compile(r'^(?P<interface>\S+)\s+\((?P<statistics>[\s\S]+)\)')

        # MgmtEth0/RP0/CPU0/0 is up, line protocol is up
        p4 = re.compile(r'^(?P<interface>\S+) +is +(?P<interface_status>\S+), '
                        r'+line +protocol +is +(?P<line_protocol_status>\S+)$')

        # Encapsulation 802.1Q
        p5 = re.compile(r'^Encapsulation\s+(?P<encapsulation>.+)$')

        # Input  Packets:                    282171                            0
        p6 = re.compile(r'^Input\s+Packets:\s+(?P<input_packets>\d+)\s+'
                        r'(?P<input_packets_delta>\d+)$')

        # Input  pps:                           133
        p7 = re.compile(r'^Input\s+pps:\s+(?P<input_pps>\d+)$')

        # Input  Bytes:                   261447750                        40913
        p8 = re.compile(r'^Input\s+Bytes:\s+(?P<input_bytes>\d+)\s+(?P<input_bytes_delta>\d+)$')

        # Input  Kbps (rate):                   176                       (  0%)
        p9 = re.compile(r'^Input\s+Kbps\s+\(rate\):\s+(?P<input_kbps_rate>\S+)'
                        r'\s+\((?P<input_kbps_delta>.*)\)$')

        # Output Packets:                      1178                            0
        p10 = re.compile(r'^Output\s+Packets:\s+(?P<output_packets>\d+)\s+'
                         r'(?P<output_packets_delta>\d+)$')

        # Output  pps:                           133
        p11 = re.compile(r'^Output\s+pps:\s+(?P<output_pps>\d+)$')

        # Output  Bytes:                   261447750                        40913
        p12 = re.compile(r'^Output\s+Bytes:\s+(?P<output_bytes>\d+)\s+(?P<output_bytes_delta>\d+)$')

        # Output  Kbps (rate):                   176                       (  0%)
        p13 = re.compile(r'^Output\s+Kbps\s+\(rate\):\s+(?P<output_kbps_rate>\S+)'
                         r'\s+\((?P<output_kbps_delta>.*)\)$')

        # Input  Total:                           0                            0
        p14 = re.compile(r'^Input\s+Total:\s+(?P<input_total>\d+)\s+(?P<input_total_delta>\d+)$')

        # Input  CRC:                           0                            0
        p15 = re.compile(r'^Input\s+CRC:\s+(?P<input_crc>\d+)\s+(?P<input_crc_delta>\d+)$')

        # Input  Frame:                           0                            0
        p16 = re.compile(r'^Input\s+Frame:\s+(?P<input_frame>\d+)\s+(?P<input_frame_delta>\d+)$')

        # Input  Frame:
        p16_1 = re.compile(r'^Input\s+Frame:$')

        #0                            0
        p16_2 = re.compile(r'^(?P<input_frame>\d+)\s+(?P<input_frame_delta>\d+)$')

        # Input  Overrun:                         0                            0
        p17 = re.compile(r'^Input\s+Overrun:\s+(?P<input_overrun>\d+)\s+'
                         r'(?P<input_overrun_delta>\d+)$')

        # Output  Total:                           0                            0
        p18 = re.compile(r'^Output\s+Total:\s+(?P<output_total>\d+)\s+(?P<output_total_delta>\d+)$')

        # Output Underrun:                        0                            0
        p19 = re.compile(r'^Output\s+Underrun:\s+(?P<output_underrun>\d+)\s+'
                         r'(?P<output_underrun_delta>\d+)$')

        # Output Underrun:                        0
        p19_1 = re.compile(r'^Output\s+Underrun:\s+(?P<output_underrun>\d+)$')

        #0
        p19_2 = re.compile(r'^(?P<output_underrun_delta>\d+)$')

        for line in out.splitlines():

            #To remove all ANSI directives
            ansi_escape3 = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]', flags=re.IGNORECASE)
            line = ansi_escape3.sub('', line)
            line = line.strip()

            # F17-ASR9922          Monitor Time: 00:00:00          SysUptime: 09:47:06
            m = p1.match(line)
            if m:
                group = m.groupdict()
                monitor_time_dict = ret_dict.setdefault('monitor_time', {}).\
                    setdefault(group['monitor_time'], {})
                monitor_time_dict.update({'hostname': group['hostname'],
                                          'sys_up_time': group['sys_up_time']
                                          })
                continue

            # Protocol:General
            m = p2.match(line)
            if m:
                group = m.groupdict()
                monitor_time_dict.update({'protocol': group['protocol']})
                continue

            # Hu0/0/0/0             22000/  0%    23000/  0%   114.6M/0        280.5M/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                #convert interface to full name
                interface = Common.convert_intf_name(group['interface'])

                interface_dict = monitor_time_dict.setdefault("interface", {})
                each_intf_dict = interface_dict.setdefault(interface, {})
                each_intf_dict.update({
                    'input_bps': int(group['input_bps']),
                    'output_bps': int(group['output_bps']),
                    'input_delta': int(group['input_delta']),
                    'output_delta': int(group['output_delta']),
                    'input_bytes': float(group['input_bytes']),
                    'output_bytes': float(group['output_bytes']),
                })


                if group['input_bps_percent'] == '--':
                    input_bps_percent = 0.0
                else:
                    input_bps_percent = float(group['input_bps_percent'])

                if group['output_bps_percent'] == '--':
                    output_bps_percent = 0.0
                else:
                    output_bps_percent = float(group['output_bps_percent'])

                each_intf_dict.update({'input_bps_percent': input_bps_percent,
                                       'output_bps_percent': output_bps_percent})

                if group['int_bytes']:
                    each_intf_dict.update({'input_bytes_unit': group['int_bytes']})
                if group['out_bytes']:
                    each_intf_dict.update({'output_bytes_unit': group['out_bytes']})
                continue

            # Gi0/0/0/1            (statistics not available)
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])

                interface_dict = monitor_time_dict.setdefault("interface", {})
                each_intf_dict = interface_dict.setdefault(interface, {})
                each_intf_dict.update({'interface_status': group['statistics']})


            # MgmtEth0/RP0/CPU0/0 is up, line protocol is up
            m = p4.match(line)
            if m:
                group = m.groupdict()
                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])
                interface_dict = monitor_time_dict.setdefault("interface", {})
                each_intf_dict = interface_dict.setdefault(interface, {})

                monitor_time_dict.update({'interface_status': group['interface_status'],
                                          'line_protocol_status': group['line_protocol_status']})
                continue

            # Encapsulation 802.1Q
            m = p5.match(line)
            if m:
                group = m.groupdict()
                monitor_time_dict.update({'encapsulation': group['encapsulation']})
                continue

            # Input  Packets:                    282171                            0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict = each_intf_dict.setdefault('traffic_stats', {})
                traffic_stats_dict.update({'input_packets': int(group['input_packets']),
                                           'input_packets_delta': int(group['input_packets_delta'])})
                continue

            # Input  pps:                           133
            m = p7.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict.update({'input_pps': int(group['input_pps'])})
                continue

            # Input  Bytes:                   261447750                        40913
            m = p8.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict.update({'input_bytes': int(group['input_bytes']),
                                           'input_bytes_delta': int(group['input_bytes_delta'])})
                continue

            # Input  Kbps (rate):                   176                       (  0%)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                input_kbps_delta = re.sub('[\s%]+', "", group['input_kbps_delta'])

                if group['input_kbps_rate'] == 'NA':
                    input_kbps_rate = 0
                else:
                    input_kbps_rate = int(group['input_kbps_rate'])

                if input_kbps_delta == 'NA':
                    input_kbps_delta = 0.0
                else:
                    input_kbps_delta = float(input_kbps_delta)

                traffic_stats_dict.update({'input_kbps_rate': input_kbps_rate,
                                           'input_kbps_delta': input_kbps_delta})
                continue

            # Output Packets:                      1178                            0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict.update({'output_packets': int(group['output_packets']),
                                           'output_packets_delta': int(group['output_packets_delta'])})
                continue

            # Output  pps:                           133
            m = p11.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict.update({'output_pps': int(group['output_pps'])})
                continue

            # Output  Bytes:                   261447750                        40913
            m = p12.match(line)
            if m:
                group = m.groupdict()
                traffic_stats_dict.update({'output_bytes': int(group['output_bytes']),
                                           'output_bytes_delta': int(group['output_bytes_delta'])})
                continue

            # Output Kbps (rate):                     0                       (  0%)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                output_kbps_delta = re.sub('[\s%]+', "", group['output_kbps_delta'])

                if group['output_kbps_rate'] == 'NA':
                    output_kbps_rate = 0
                else:
                    output_kbps_rate = int(group['output_kbps_rate'])

                if output_kbps_delta == 'NA':
                    output_kbps_delta = 0.0
                else:
                    output_kbps_delta = float(output_kbps_delta)


                traffic_stats_dict.update({'output_kbps_rate': output_kbps_rate,
                                           'output_kbps_delta': output_kbps_delta})
                continue

            # Input  Total:                           0                            0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict = each_intf_dict.setdefault('error_stats', {})
                error_stats_dict.update({'input_total': int(group['input_total']),
                                         'input_total_delta': int(group['input_total_delta'])})
                continue

            # Input  CRC:                             0                            0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'input_crc': int(group['input_crc']),
                                         'input_crc_delta': int(group['input_crc_delta'])})
                continue

            # Input  Frame:                           0                            0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'input_frame': int(group['input_frame']),
                                         'input_frame_delta': int(group['input_frame_delta'])})
                continue

            # Input  Frame:
            m = p16_1.match(line)
            if m:
                control_flag = 'input_frame'
                continue

            #                           0                            0
            m = p16_2.match(line)
            if m and control_flag=='input_frame':
                group = m.groupdict()
                error_stats_dict.update({'input_frame': int(group['input_frame']),
                                         'input_frame_delta': int(group['input_frame_delta'])})
                continue

            # Input  Overrun:                         0                            0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'input_overrun': int(group['input_overrun']),
                                         'input_overrun_delta': int(group['input_overrun_delta'])})
                continue

            # Output Total:                           0                            0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'output_total': int(group['output_total']),
                                         'output_total_delta': int(group['output_total_delta'])})
                continue

            # Output Underrun:                        0                            0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'output_underrun': int(group['output_underrun']),
                                         'output_underrun_delta': int(group['output_underrun_delta'])})
                continue

            # Output Underrun:                        0
            m = p19_1.match(line)
            if m:
                group = m.groupdict()
                error_stats_dict.update({'output_underrun': int(group['output_underrun'])})
                control_flag="output_underrun"

            # 0
            m = p19_2.match(line)
            if m and control_flag == "output_underrun":
                group = m.groupdict()
                error_stats_dict.update({'output_underrun_delta': int(group['output_underrun_delta'])})

        return ret_dict

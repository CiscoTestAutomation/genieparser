
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

class ShowInterfaceSchema(MetaParser):
    schema = { 
        Any(): {
            'state': str,
            'mac-addr': str,
            'type': str,
            "link-state": str,
            'mtu': int,
            'auto-negotiation': str,
            'speed': str,
            'ipv6-autoconfig': str,
            'duplex': str,
            'monitor-mode': str,
            'link-speed': str,
            'comments': str,
            'ipv4-address': str,
            'ipv6-address': str,
            'ipv6-local-link-address': str,
            'statistics' :{
                'TX' : {
                    'bytes': int,
                    'packets': int,
                    'errors' : int,
                    'dropped': int,
                    'overruns': int,
                    'carrier': int,
                },
                'RX' : {
                    'bytes': int,
                    'packets': int,
                    'errors' : int,
                    'dropped': int,
                    'overruns': int,
                    'frame': int,
                },
            }
        }
    }

class ShowInterface(ShowInterfaceSchema):
    """parser for   show interface <interface>
                    show interfaces all"""

    cli_command = ['show interface {interface}','show interfaces all']

    def cli(self,interface="",output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
                out = self.device.execute(cmd)
            else:
                cmd = self.cli_command[1]
                out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        current_interface = ''

        if interface != "":
            current_interface = interface
            ret_dict.update({
                interface:{
                    'statistics': {
                        'TX':{},
                        'RX':{}
                        }
                    }
                })
        
        for line in out.splitlines():
            line = line.strip()

            p0 = re.compile(r'^Interface (?P<interface_name>.*)$')
            m = p0.match(line)
            if m:
                current_interface = m.groupdict()['interface_name']
                ret_dict.update({current_interface:{
                    'statistics': {
                        'TX':{},
                        'RX':{}
                        }
                    }})
                continue

            p1 = re.compile(r'^state (?P<state>.*)$')
            m = p1.match(line)
            if m:
                ret_dict[current_interface]['state'] = m.groupdict()['state']
                continue
            
            p2 = re.compile(r'^mac-addr (?P<mac_addr>.*)$')
            m = p2.match(line)
            if m:
                ret_dict[current_interface]['mac-addr'] = m.groupdict()['mac_addr']
                continue

            p3 = re.compile(r'^type (?P<type>.*)$')
            m = p3.match(line)
            if m:
                ret_dict[current_interface]['type'] = m.groupdict()['type']
                continue

            p4 = re.compile(r'^link-state (?P<link_state>.*)$')
            m = p4.match(line)
            if m:
                ret_dict[current_interface]['link-state'] = m.groupdict()['link_state']
                continue

            p5 = re.compile(r'^mtu (?P<mtu>.*)$')
            m = p5.match(line)
            if m:
                ret_dict[current_interface]['mtu'] = int(m.groupdict()['mtu'])
                continue

            p6 = re.compile(r'^auto-negotiation (?P<auto_negotiation>.*)$')
            m = p6.match(line)
            if m:
                ret_dict[current_interface]['auto-negotiation'] = m.groupdict()['auto_negotiation']
                continue
            
            p7 = re.compile(r'^speed (?P<speed>.*)$')
            m = p7.match(line)
            if m:
                ret_dict[current_interface]['speed'] = m.groupdict()['speed']
                continue

            p8 = re.compile(r'^ipv6-autoconfig (?P<ipv6_autoconfig>.*)$')
            m = p8.match(line)
            if m:
                ret_dict[current_interface]['ipv6-autoconfig'] = m.groupdict()['ipv6_autoconfig']
                continue

            p9 = re.compile(r'^duplex (?P<duplex>.*)$')
            m = p9.match(line)
            if m:
                ret_dict[current_interface]['duplex'] = m.groupdict()['duplex']
                continue

            p10 = re.compile(r'^monitor-mode (?P<monitor_mode>.*)$')
            m = p10.match(line)
            if m:
                ret_dict[current_interface]['monitor-mode'] = m.groupdict()['monitor_mode']
                continue
            
            p11 = re.compile(r'^link-speed (?P<link_speed>.*)$')
            m = p11.match(line)
            if m:
                ret_dict[current_interface]['link-speed'] = m.groupdict()['link_speed']
                continue

            p12 = re.compile(r'^comments\s*(?P<comments>.*)$')
            m = p12.match(line)
            if m:
                ret_dict[current_interface]['comments'] = m.groupdict()['comments']
                continue
            
            p13 = re.compile(r'^ipv4-address (?P<ipv4_address>.*)$')
            m = p13.match(line)
            if m:
                ret_dict[current_interface]['ipv4-address'] = m.groupdict()['ipv4_address']
                continue

            p14 = re.compile(r'^ipv6-address (?P<ipv6_address>.*)$')
            m = p14.match(line)
            if m:
                ret_dict[current_interface]['ipv6-address'] = m.groupdict()['ipv6_address']
                continue

            p15 = re.compile(r'^ipv6-local-link-address (?P<ipv6_local_link_address>.*)$')
            m = p15.match(line)
            if m:
                ret_dict[current_interface]['ipv6-local-link-address'] = m.groupdict()['ipv6_local_link_address']
                continue

            p16 = re.compile(r'^TX bytes:(?P<tx_bytes>\d+) packets:(?P<tx_packets>\d+) errors:(?P<tx_errors>\d+) dropped:(?P<tx_dropped>\d+) overruns:(?P<tx_overruns>\d+) carrier:(?P<tx_carrier>\d+)$')
            m = p16.match(line)
            if m:
                ret_dict[current_interface]['statistics']['TX'] = {
                    'bytes': int(m.groupdict()['tx_bytes']),
                    'packets': int(m.groupdict()['tx_packets']),
                    'errors': int(m.groupdict()['tx_errors']),
                    'dropped': int(m.groupdict()['tx_dropped']),
                    'overruns': int(m.groupdict()['tx_overruns']),
                    'carrier': int(m.groupdict()['tx_carrier'])
                }
                continue
            
            p17 = re.compile(r'^RX bytes:(?P<rx_bytes>\d+) packets:(?P<rx_packets>\d+) errors:(?P<rx_errors>\d+) dropped:(?P<rx_dropped>\d+) overruns:(?P<rx_overruns>\d+) frame:(?P<rx_frame>\d+)$')
            m = p17.match(line)
            if m:
                ret_dict[current_interface]['statistics']['RX'] = {
                    'bytes':    int(m.groupdict()['rx_bytes']),
                    'packets':  int(m.groupdict()['rx_packets']),
                    'errors':   int(m.groupdict()['rx_errors']),
                    'dropped':  int(m.groupdict()['rx_dropped']),
                    'overruns': int(m.groupdict()['rx_overruns']),
                    'frame':    int(m.groupdict()['rx_frame'])
                }
                continue

        return ret_dict
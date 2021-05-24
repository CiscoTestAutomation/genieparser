""" show_interface.py

Check Point Gaia parsers for the following show commands:
    * show interface {interface}
    * show interfaces all

"""

import re
from collections import defaultdict

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowInterfaceSchema(MetaParser):
    schema = {
        'interfaces': {
            Any(): {
                'state': str,
                'mac_addr': str,
                'type': str,
                "link_state": str,
                'mtu': int,
                'auto_negotiation': str,
                'speed': str,
                'ipv6_autoconfig': str,
                'duplex': str,
                'monitor_mode': str,
                'link_speed': str,
                'comments': str,
                'ipv4_address': str,
                'ipv6_address': str,
                'ipv6_local_link_address': str,
                Optional('alias'): {     #
                    Any(): {             # 'eth1:1': {
                    'state': str,        #     'state': on
                    'ipv4_address': str  #     'ipv4_address': '192.168.1.1'
                    }
                },
                'statistics' :{
                    'tx_bytes': int,
                    'tx_packets': int,
                    'tx_errors' : int,
                    'tx_dropped': int,
                    'tx_overruns': int,
                    'tx_carrier': int,
                    'rx_bytes': int,
                    'rx_packets': int,
                    'rx_errors' : int,
                    'rx_dropped': int,
                    'rx_overruns': int,
                    'rx_frame': int,
                }
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

        ret_dict = defaultdict(dict)
        interfaces = defaultdict(dict)

        current_interface = '' # Track current interface in output
        current_alias = '' # Track name of interface alias, if applicable

        if interface != "":
            current_interface = interface
            current_interface_is_alias = False
            interfaces[interface] = defaultdict(dict)


        ''' Sample Output
        gw-a> show interfaces all
        Interface eth0
            state on
            mac-addr 50:00:00:ff:01:01
            type ethernet
            link-state link up
            mtu 1500
            auto-negotiation on
            speed 1000M
            ipv6-autoconfig Not configured
            duplex full
            monitor-mode Not configured
            link-speed 1000M/full
            comments
            ipv4-address 10.1.1.3/24
            ipv6-address Not Configured
            ipv6-local-link-address Not Configured

        Statistics:
            TX bytes:29871552 packets:80540 errors:0 dropped:0 overruns:0 carrier:0
            RX bytes:106812763 packets:88415 errors:0 dropped:0 overruns:0 frame:0
        Interface eth0:1
            ipv4-address 10.1.1.1/24
            state on
        '''

        p0 = re.compile(r'^Interface (?P<interface_name>(?!.*:).*)$') # Does not match alias interfaces (eth1:1)  
        p1 = re.compile(r'^state (?P<state>.*)$')
        p2 = re.compile(r'^mac-addr (?P<mac_addr>.*)$')
        p3 = re.compile(r'^type (?P<type>.*)$')
        p4 = re.compile(r'^link-state (?P<link_state>.*)$')
        p5 = re.compile(r'^mtu (?P<mtu>.*)$')
        p6 = re.compile(r'^auto-negotiation (?P<auto_negotiation>.*)$')
        p7 = re.compile(r'^speed (?P<speed>.*)$')
        p8 = re.compile(r'^ipv6-autoconfig (?P<ipv6_autoconfig>.*)$')
        p9 = re.compile(r'^duplex (?P<duplex>.*)$')
        p10 = re.compile(r'^monitor-mode (?P<monitor_mode>.*)$')
        p11 = re.compile(r'^link-speed (?P<link_speed>.*)$')
        p12 = re.compile(r'^comments\s*(?P<comments>.*)$')
        p13 = re.compile(r'^ipv4-address (?P<ipv4_address>.*)$')
        p14 = re.compile(r'^ipv6-address (?P<ipv6_address>.*)$')
        p15 = re.compile(r'^ipv6-local-link-address (?P<ipv6_local_link_address>.*)$')
        p16 = re.compile(r'^TX bytes:(?P<tx_bytes>\d+) packets:(?P<tx_packets>\d+) errors:(?P<tx_errors>\d+) dropped:(?P<tx_dropped>\d+) overruns:(?P<tx_overruns>\d+) carrier:(?P<tx_carrier>\d+)$')
        p17 = re.compile(r'^RX bytes:(?P<rx_bytes>\d+) packets:(?P<rx_packets>\d+) errors:(?P<rx_errors>\d+) dropped:(?P<rx_dropped>\d+) overruns:(?P<rx_overruns>\d+) frame:(?P<rx_frame>\d+)$')
        p18 = re.compile(r'^Interface (?P<alias_name>\w+[:]\.?\d+)') # Matches alias interfaces (eth1:1)

        for line in out.splitlines():
            line = line.strip()       

            # Interface eth0
            m = p0.match(line)
            if m:
                current_interface = m.groupdict()['interface_name']
                current_interface_is_alias = False # Moved onto a new Interface

                interfaces[current_interface] = defaultdict(dict)
                continue
            
            # state on
            m = p1.match(line)
            if m:
                state = m.groupdict()['state']
                
                if not current_interface_is_alias:
                    interfaces[current_interface]['state'] = state
                    continue
                else:
                    interfaces[current_interface]['alias'][current_alias]['state'] = state
                    continue

            # mac-addr 50:00:00:ff:01:01
            m = p2.match(line)
            if m:
                interfaces[current_interface]['mac_addr'] = m.groupdict()['mac_addr']
                continue

            # type ethernet
            m = p3.match(line)
            if m:
                interfaces[current_interface]['type'] = m.groupdict()['type']
                continue

            # link-state link up
            m = p4.match(line)
            if m:
                interfaces[current_interface]['link_state'] = m.groupdict()['link_state']
                continue

            # mtu 1500
            m = p5.match(line)
            if m:
                interfaces[current_interface]['mtu'] = int(m.groupdict()['mtu'])
                continue
            
            # auto-negotiation on
            m = p6.match(line)
            if m:
                interfaces[current_interface]['auto_negotiation'] = m.groupdict()['auto_negotiation']
                continue

            # speed 1000M
            m = p7.match(line)
            if m:
                interfaces[current_interface]['speed'] = m.groupdict()['speed']
                continue

            # ipv6-autoconfig Not configured
            m = p8.match(line)
            if m:
                interfaces[current_interface]['ipv6_autoconfig'] = m.groupdict()['ipv6_autoconfig']
                continue

            # duplex full
            m = p9.match(line)
            if m:
                interfaces[current_interface]['duplex'] = m.groupdict()['duplex']
                continue

            # monitor-mode Not configured
            m = p10.match(line)
            if m:
                interfaces[current_interface]['monitor_mode'] = m.groupdict()['monitor_mode']
                continue

            # link-speed 1000M/full
            m = p11.match(line)
            if m:
                interfaces[current_interface]['link_speed'] = m.groupdict()['link_speed']
                continue

            # comments This is an interface comment
            m = p12.match(line)
            if m:
                interfaces[current_interface]['comments'] = m.groupdict()['comments']
                continue

            # ipv4-address 10.1.1.3/24
            m = p13.match(line)
            if m:
                ipv4_address = m.groupdict()['ipv4_address']

                if not current_interface_is_alias:
                    interfaces[current_interface]['ipv4_address'] = ipv4_address
                    continue
                else:
                    interfaces[current_interface]['alias'][current_alias]['ipv4_address'] = ipv4_address
                    continue

            # ipv6-address Not Configured
            m = p14.match(line)
            if m:
                interfaces[current_interface]['ipv6_address'] = m.groupdict()['ipv6_address']
                continue

            # ipv6-local-link-address Not Configured
            m = p15.match(line)
            if m:
                interfaces[current_interface]['ipv6_local_link_address'] = m.groupdict()['ipv6_local_link_address']
                continue

            # TX bytes:29871552 packets:80540 errors:0 dropped:0 overruns:0 carrier:0
            m = p16.match(line)
            if m:
                interfaces[current_interface]['statistics'].update({
                    'tx_bytes': int(m.groupdict()['tx_bytes']),
                    'tx_packets': int(m.groupdict()['tx_packets']),
                    'tx_errors': int(m.groupdict()['tx_errors']),
                    'tx_dropped': int(m.groupdict()['tx_dropped']),
                    'tx_overruns': int(m.groupdict()['tx_overruns']),
                    'tx_carrier': int(m.groupdict()['tx_carrier'])
                })
                continue

            # RX bytes:106812763 packets:88415 errors:0 dropped:0 overruns:0 frame:0
            m = p17.match(line)
            if m:
                interfaces[current_interface]['statistics'].update({
                    'rx_bytes':    int(m.groupdict()['rx_bytes']),
                    'rx_packets':  int(m.groupdict()['rx_packets']),
                    'rx_errors':   int(m.groupdict()['rx_errors']),
                    'rx_dropped':  int(m.groupdict()['rx_dropped']),
                    'rx_overruns': int(m.groupdict()['rx_overruns']),
                    'rx_frame':    int(m.groupdict()['rx_frame'])
                })
                continue
            
            # eth1:1  This matches interface aliases
            m = p18.match(line)
            if m:
                # Set to True until a new interface is matched by p0
                current_interface_is_alias = True
                current_alias = m.groupdict()['alias_name']
                interfaces[current_interface]['alias'] = {}
                interfaces[current_interface]['alias'][current_alias] = {}
                continue

        if len(interfaces.keys()) != 0:
            ret_dict = {"interfaces": interfaces}
        
        return ret_dict

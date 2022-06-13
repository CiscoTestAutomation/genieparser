"""show_derived.py

IOSXE parsers for the following show commands:
   * show derived-config interface <INTF>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

# Genie Libs
from genie.libs.parser.utils.common import Common

# ====================================================
#  Schema for 'show derived-config interface'
# ====================================================
class ShowDerivedConfigInterfaceSchema(MetaParser):
    """Schema for show derived-config interface <INTF>"""
    schema = {
        'derived_config': {
            Any(): {
                Optional('ip_address'): str,
                Optional('ipv6_address'): str,
                Optional('ip_access_group_in'): str,
                Optional('ip_access_group_out'): str,
                Optional('ipv6'): str,
                Optional('ipv6_access_group_in'): str,
                Optional('ipv6_access_group_out'): str,
                Optional('tunnel_source'): str,
                Optional('tunnel_mode'): str,
                Optional('tunnel_destination'): str,
                Optional('tunnel_ipsec_profile'): str
            },
        },
    }
# ====================================================
#  Parser for 'show crypto ipsec internal dual'
# ====================================================    
class ShowDerivedConfigInterface(ShowDerivedConfigInterfaceSchema):
    """ Parser for 
        * show derived-config interface <INTF>
    """

    cli_command = ['show derived-config interface {interface}', 'show derived-config']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize return dict
        ret_dict = {}

        # interface Tunnel1
        p1 = re.compile(r"^interface\s+(?P<interface_name>[\S\s]+)$")

        # ip address 192.168.1.1 255.255.255.0
        p2 = re.compile(r"^ip\s+address\s+(?P<ip_address>[\S\s]+)\s+(?P<ip_mask>[\S\s]+)$")

        # ipv6 address 8001::100/64
        p3 = re.compile(r"^ipv6\s+address\s+(?P<ipv6_address>[\S\s]+)$")

        # ip access-group Tu1-ipsec-ds-ipv4-in in
        p4 = re.compile(r"^ip\s+access-group\s+(?P<ip_access_group_in>[\S\s]+)\s+in$")
        
        # ip access-group Tu1-ipsec-ds-ipv4-out out
        p5 = re.compile(r"^ip\s+access-group\s+(?P<ip_access_group_out>[\S\s]+)\s+out$")
        
        # ipv6 enable
        p6 = re.compile(r"^ipv6\s+enable$")
        
        # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-in in
        p7 = re.compile(r"^ipv6\s+traffic-filter\s+(?P<ipv6_access_group_in>[\S\s]+)\s+in$")

        # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-out out
        p8 = re.compile(r"^ipv6\s+traffic-filter\s+(?P<ipv6_access_group_out>[\S\s]+)\s+out$")

        # tunnel source 11.11.11.2
        p9 = re.compile(r"^tunnel\s+source\s+(?P<tunnel_source>[\S\s]+)$")

        # tunnel mode ipsec dual-overlay
        p10 = re.compile(r"^tunnel\s+mode\s+(?P<tunnel_mode>[\S\s]+)$")

        # tunnel destination 30.30.30.2
        p11 = re.compile(r"^tunnel\s+destination\s+(?P<tunnel_destination>[\S\s]+)$")

        # tunnel protection ipsec profile ipsec_global_profile
        p12 = re.compile(
            r"^tunnel\s+protection\s+ipsec\s+profile\s+(?P<tunnel_ipsec_profile>[\S\s]+)$")

        for line in out.splitlines():
            line = line.strip()

            # interface Tunnel1
            m = p1.match(line)
            if m:
                interface_name = m.groupdict()["interface_name"]
                intf_dict = ret_dict.setdefault('derived_config', {}).setdefault(interface_name, {})
                continue

            # ip address 192.168.1.1 255.255.255.0
            m = p2.match(line)
            if m:
                intf_dict['ip_address'] = m.groupdict()['ip_address']
                continue

            # ipv6 address 8001::100/64
            m = p3.match(line)
            if m:
                intf_dict['ipv6_address'] = m.groupdict()['ipv6_address']
                continue

            # ip access-group Tu1-ipsec-ds-ipv4-in in
            m = p4.match(line)
            if m:
                intf_dict['ip_access_group_in'] = m.groupdict()['ip_access_group_in']
                continue

            # ip access-group Tu1-ipsec-ds-ipv4-out out
            m = p5.match(line)
            if m:
                intf_dict['ip_access_group_out'] = m.groupdict()['ip_access_group_out']
                continue

            # ipv6 enable
            m = p6.match(line)
            if m:
                intf_dict['ipv6'] = 'enabled'
                continue

            # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-in in
            m = p7.match(line)
            if m:
                intf_dict['ipv6_access_group_in'] = m.groupdict()['ipv6_access_group_in']
                continue

            # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-out out
            m = p8.match(line)
            if m:
                intf_dict['ipv6_access_group_out'] = m.groupdict()['ipv6_access_group_out']
                continue

            # tunnel source 11.11.11.2
            m = p9.match(line)
            if m:
                intf_dict['tunnel_source'] = m.groupdict()['tunnel_source']
                continue

            # tunnel mode ipsec dual-overlay
            m = p10.match(line)
            if m:
                intf_dict['tunnel_mode'] = m.groupdict()['tunnel_mode']
                continue

            # tunnel destination 30.30.30.2
            m = p11.match(line)
            if m:
                intf_dict['tunnel_destination'] = m.groupdict()['tunnel_destination']
                continue

            # tunnel protection ipsec profile ipsec_global_profile
            m = p12.match(line)
            if m:
                intf_dict['tunnel_ipsec_profile'] = m.groupdict()['tunnel_ipsec_profile']
                continue
            
        return ret_dict


''' show_ipv6_nd.py
IOSXE parsers for the following show commands:
    * show ipv6 nd  routing-proxy 
Copyright (c) 2023 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ====================================================
# Schema for 'show ipv6 nd routing-proxy'
# ====================================================
class ShowIpv6NdRoutingProxySchema(MetaParser):
    """ Schema for 'show ipv6 nd routing-proxy' """

    schema = {
        'ipv6_nd_router_proxy_config': {
            'policy_name': str,
            'proxying': str,
            "targets": {
                Optional(str): {
                    'target': str,
                    'type': str,
                    'feature': str,
                    'target_range': str
                }
            }
        }
    }

# =============================================
# Parser for 'show ipv6 nd routing-proxy'
# =============================================
class ShowIpv6NdRoutingProxy(ShowIpv6NdRoutingProxySchema):
    """ 'show ipv6 nd routing-proxy' """

    cli_command = 'show ipv6 nd routing-proxy'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Routing Proxy default configuration:
        p1 = re.compile(r'^Routing Proxy\s+(?P<policy_name>.+)\s+configuration:$')

        # Proxying NDP
        p2 = re.compile(r'^Proxying\s+(?P<proxying>\S+)$')

        # Target               Type  Policy               Feature        Target range
        # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
        # Et0/0                PORT  pol1                 DHCP Guard     vlanall
        p3 = re.compile \
            (r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Routing Proxy default configuration:
            m = p1.match(line)
            if m:
                policy_config_dict = parser_dict.setdefault('ipv6_nd_router_proxy_config', {})
                policy_config_dict.update({'policy_name': m.groupdict()['policy_name']})
                continue
            # proxying  NDP
            m = p2.match(line)
            if m:
                policy_config_dict = parser_dict.setdefault('ipv6_nd_router_proxy_config', {})
                policy_config_dict.update({'proxying': m.groupdict()['proxying']})
                continue
            # Target               Type  Policy               Feature        Target range
            # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
            # Et0/0                PORT  pol1                 DHCP Guard     vlanall
            m = p3.match(line)
            if m:
                group = m.groupdict()
                policy_config_dict = parser_dict.setdefault('ipv6_nd_router_proxy_config', {})
                targets_dict = policy_config_dict.setdefault('targets', {})
                target_dict = targets_dict.setdefault(group['target'], {})
                target_dict.update({
                    'target':  group['target'],
                    'type': group['type'],
                    'feature': group['feature'],
                    'target_range' : group['target_range']
                })
                continue

        return parser_dict



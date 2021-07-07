''' ShowIpv6DhcpGuardPolicy.py

IOSXE parsers for the following show commands:

    * show ipv6 dhcp guard policy <policy name>

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================================================
# Schema for 'show ipv6 dhcp guard policy <policy name>'
# ====================================================
class ShowIpv6DhcpGuardPolicySchema(MetaParser):
    """ Schema for show ipv6 dhcp guard policy <policy name> """

    schema = {
        'dhcp_guard_policy_config': {            
            'policy_name': str,
            'trusted_port': bool,
            'device_role': str,
            Optional('max_preference'): int,
            Optional('min_preference'): int,
            Optional('access_list'): str,
            Optional('prefix_list') : str,
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
# Parser for 'show ipv6 guard policy <policy name>'
# =============================================
class ShowIpv6DhcpGuardPolicy(ShowIpv6DhcpGuardPolicySchema):
    """ show ipv6 dhcp guard policy <policy name> """

    cli_command = 'show ipv6 dhcp guard policy {policy_name}'

    def cli(self, policy_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(policy_name=policy_name))
        else:
            output = output

        # Dhcp guard policy pol1 configuration:
        p = re.compile(r'^Dhcp\s+guard\s+policy\s+(?P<policy_name>.+)\s+configuration:$')
        
        # Device Role: dhcp server
        p1 = re.compile(r'^Device\sRole:\s(?P<device_role>dhcp (client|server))$')

        #Trusted Port 
        p2 = re.compile(r'^(?P<trusted_port>Trusted Port)$')

        # Max Preference: 255
        p3 = re.compile(r'^Max Preference:\s+((?P<max_preference>\d+))$')

        # Min Preference: 0
        p4 = re.compile(r'^Min Preference:(\s+(?P<min_preference>\d+))$')

        #Source Address Match Access List: acl1
        p5 = re.compile(r'^Source Address Match Access List:\s+(?P<access_list>\S+)$')

        #Prefix List Match Prefix List: abc
        p6 = re.compile(r'^Prefix List Match Prefix List:\s+(?P<prefix_list>\S+)$')

        #Target               Type  Policy               Feature        Target range
        # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
        # Et0/0                PORT  pol1                 DHCP Guard     vlanall
        p7 = re.compile(r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()

            policy_config_dict = parser_dict.setdefault('dhcp_guard_policy_config', {})
            targets_dict = policy_config_dict.setdefault('targets', {})
            policy_config_dict.setdefault('trusted_port', False)

            m = p.match(line)
            if m:
                policy_config_dict.update({'policy_name': m.groupdict()['policy_name']})
                continue
            
            m1 = p1.match(line)
            if m1:
                policy_config_dict.update({'device_role': m1.groupdict()['device_role']})
                continue

            m2 = p2.match(line)     
            if m2:
                policy_config_dict.update({'trusted_port': True})
                continue
            
            m3 = p3.match(line)
            if m3:
                policy_config_dict.update({'max_preference': int(m3.groupdict()['max_preference'])})
                continue

            m4 = p4.match(line)
            if m4:
                policy_config_dict.update({'min_preference':  int(m4.groupdict()['min_preference'])})
                continue

            m5 = p5.match(line)
            if m5:
                policy_config_dict.update({'access_list':  m5.groupdict()['access_list']})
                continue
            
            m6 = p6.match(line)
            if m6: 
                policy_config_dict.update({'prefix_list': m6.groupdict()['prefix_list']})
                continue

            m7 = p7.match(line)
            if m7:
                target = m7.groupdict()['target']
                target_dict = targets_dict.setdefault(target, {})
                target_dict.update({'target': m7.groupdict()['target']})
                target_dict.update({'type':  m7.groupdict()['type']})
                target_dict.update({'feature':  m7.groupdict()['feature']})
                target_dict.update({'target_range': m7.groupdict()['target_range']})

        return parser_dict

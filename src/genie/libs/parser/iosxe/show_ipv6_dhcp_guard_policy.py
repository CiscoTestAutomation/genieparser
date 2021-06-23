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
        'dhcp_guard_policy': 
        {            
        'policy_name': str,
        'trusted_port': bool,
        'device_role': str,
        Optional('max_preference'): int,
        Optional('min_preference'): int,
        Optional('access_list'): str,
        Optional('prefix_list') : str,
        "targets": {
            Optional(Any()): {
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
    """ show device-tracking features """

    cli_command = 'show ipv6 dhcp guard policy {policy_name}'

    def cli(self, policy_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(policy_name=policy_name))
        else:
            output = output

        #device role
        p = re.compile(r'^\S+\s+\S+:\s(?P<device_role>\S+\s\S+)$')

        #trusted port
        p1 = re.compile(r'^(?P<trusted_port>\S+\s+\S+)$')

        #max preference 
        p2 = re.compile(r'^Max Preference:\s+((?P<max_preference>\d+))$')

        #min preference
        p3 = re.compile(r'^Min Preference:(\s+(?P<min_preference>\d+))$')

        #Source Address Match Access List
        p4 = re.compile(r'^Source Address Match Access List:\s+(?P<access_list>\S+)$')

        #Prefix List Match Prefix List:
        p5 = re.compile(r'^Prefix List Match Prefix List:\s+(?P<prefix_list>\S+)$')

        #targets 
        p6 = re.compile(r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}
        targets_dict = {}
        policy_config_dict = {}

        for line in output.splitlines():
            line = line.strip()
            dhcp_guard_policy = 'dhcp_guard_policy'
        
            if dhcp_guard_policy not in parser_dict:
                policy_config_dict = parser_dict.setdefault(dhcp_guard_policy, {})
                policy_config_dict.update({'policy_name': policy_name})
                policy_config_dict.setdefault('trusted_port', False)
                continue
            
            m = p.match(line)
            if m:
                policy_config_dict.update({'device_role': m.groupdict()['device_role']})
            m1 = p1.match(line)     
            if m1:
                policy_config_dict.update({'trusted_port': True})
                continue
            
            m2 = p2.match(line)
            if m2:
                policy_config_dict['max_preference'] = int(m2.groupdict()['max_preference'])
                continue

            m3 = p3.match(line)
            if m3:
                policy_config_dict['min_preference'] = int(m3.groupdict()['min_preference'])
                continue
            m4 = p4.match(line)
            if m4:
                policy_config_dict['access_list'] = m4.groupdict()['access_list']
                continue
            m5 = p5.match(line)
            if m5: 
                policy_config_dict['prefix_list'] = m5.groupdict()['prefix_list']
                continue

            m6 = p6.match(line)
            if m6:
                target = m6.groupdict()['target']
                targets_dict[target] = {}
                targets_dict[target]['target'] = m6.groupdict()['target']
                targets_dict[target]['type'] = m6.groupdict()['type']
                targets_dict[target]['feature'] = m6.groupdict()['feature']
                targets_dict[target]['target_range'] = m6.groupdict()['target_range']

        policy_config_dict['targets'] = targets_dict
        parser_dict['dhcp_guard_policy'] = policy_config_dict
        return parser_dict

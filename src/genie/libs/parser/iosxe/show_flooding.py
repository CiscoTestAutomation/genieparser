''' show_flooding.py

IOSXE parsers for the following show commands:

    * show flooding-suppression policy <policy name>

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ====================================================
# Schema for 'show flooding-suppression policy <policy name>'
# ====================================================
class ShowFloodingSuppressionPolicySchema(MetaParser):
    """ Schema for show flooding-suppression policy <policy name> """
    
    schema = {
        'flooding_supression_policy_config': {
            'policy_name': str,
            'suppressing': str,
            'mode': str,
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
# Parser for 'show flooding-suppression policy <policy name>'
# =============================================
class ShowFloodingSuppressionPolicy(ShowFloodingSuppressionPolicySchema):
    """ show flooding-suppression policy <policy name> """

    cli_command = 'show flooding-suppression policy {policy_name}'

    def cli(self, policy_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(policy_name=policy_name))
        else:
            output = output

        #Flooding suppress policy fspol3 configuration:
        p = re.compile(r'^Flooding suppress policy\s+(?P<policy_name>.+)\s+configuration:$')
        
        #Suppressing  NDP
        p1 = re.compile(r'^Suppressing\s+(?P<suppressing>\S+)$') 

        #mode:Proxy multicast resolution requests
        p2 = re.compile(r'^mode:(?P<mode>.+)')

        #Target               Type  Policy               Feature        Target range
        # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
        # Et0/0                PORT  pol1                 DHCP Guard     vlanall
        p3 = re.compile(r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Flooding suppress policy fspol3 configuration:
            m = p.match(line)
            if m:
                policy_config_dict = parser_dict.setdefault('flooding_supression_policy_config', {})
                policy_config_dict.update({'policy_name': m.groupdict()['policy_name']})
                continue

            #Suppressing  NDP
            m1 = p1.match(line)
            if m1:
                policy_config_dict = parser_dict.setdefault('flooding_supression_policy_config', {})
                policy_config_dict.update({'suppressing': m1.groupdict()['suppressing']})
                continue
            
            #mode:Proxy multicast resolution requests
            m2 = p2.match(line)
            if m2:
                policy_config_dict.update({'mode': m2.groupdict()['mode']})
                continue

            #Target               Type  Policy               Feature        Target range
            # vlan 2               VLAN  pol1                 DHCP Guard     vlan all
            # Et0/0                PORT  pol1                 DHCP Guard     vlanall
            m3 = p3.match(line)
            if m3:
                policy_config_dict = parser_dict.setdefault('flooding_supression_policy_config', {})
                targets_dict = policy_config_dict.setdefault('targets', {})
                target = m3.groupdict()['target']
                target_dict = targets_dict.setdefault(target, {})
                
                target_dict.update({'target':  m3.groupdict()['target']})
                target_dict.update({'type': m3.groupdict()['type']})
                target_dict.update({'feature': m3.groupdict()['feature']})
                target_dict.update({'target_range' : m3.groupdict()['target_range']})
                continue

        return parser_dict

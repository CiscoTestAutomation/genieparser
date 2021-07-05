''' ShowFloodingSupressionPolicy.py

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
class ShowFloodingSupressionPolicySchema(MetaParser):
    """ Schema for show flooding-suppression policy <policy name> """
    
    schema = {
        'flooding_supression_policy_config': {
            'policy_name': str,
            'supressing': str,
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
class ShowFloodingSupressionPolicy(ShowFloodingSupressionPolicySchema):
    """ show flooding-suppression policy <policy name> """

    cli_command = 'show flooding-suppression policy {policy_name}'

    def cli(self, policy_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(policy_name=policy_name))
        else:
            output = output

        #policy name
        p = re.compile(r'^\S+\s+\S+\s*\S+\s+(?P<policy_name>\S+)\s+configuration:$')
        
        #supressing 
        p1 = re.compile(r'^\S+\s+(?P<supressing>\S+)$') 

        #mode 
        p2 = re.compile(r'^\S+:(?P<mode>.+)')

        #targets 
        p3 = re.compile(r'^(?P<target>\S+\s*\S+)\s{2,}(?P<type>\S+)\s+\S+\s+(?P<feature>\S+\s\S+)\s+(?P<target_range>\S+.*\S+)$')

        parser_dict = {}

        for line in output.splitlines():
            line = line.strip()
    
            policy_config_dict = parser_dict.setdefault('flooding_supression_policy_config', {})
            targets_dict = policy_config_dict.setdefault('targets', {})

            m = p.match(line)
            if m:
                policy_config_dict.update({'policy_name': m.groupdict()['policy_name']})
                continue

            m1 = p1.match(line)
            if m1:
                policy_config_dict.update({'supressing': m1.groupdict()['supressing']})
                continue

            m2 = p2.match(line)
            if m2:
                policy_config_dict.update({'mode': m2.groupdict()['mode']})
                continue

            m3 = p3.match(line)
            if m3:
                target = m3.groupdict()['target']
                target_dict = targets_dict.setdefault(target, {})
                target_dict.update({'target':  m3.groupdict()['target']})
                target_dict.update({'type': m3.groupdict()['type']})
                target_dict.update({'feature': m3.groupdict()['feature']})
                target_dict.update({'target_range' : m3.groupdict()['target_range']})
                continue

        return parser_dict

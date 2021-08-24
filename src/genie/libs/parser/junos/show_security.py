"""show_security.py
JunOS parsers for the following show commands:
    * show security policies hit-count
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Schema, ListOf


class ShowSecurityPoliciesHitCountSchema(MetaParser):
    """ Schema for:
            * show security policies hit-count
    """
    schema = {
        "security_policy_counts": {
            Any(): {
                "security_policy": ListOf(
                    {
                        "index": str,
                        "from_zone": str,
                        "to_zone": str,
                        "name": str,
                        "policy_hit_count": str,
                    }
                ),
                "total_policies": str
            }
        }
    }


class ShowSecurityPoliciesHitCount(ShowSecurityPoliciesHitCountSchema):
    """ Parser for:
            * show security policies hit-count
    """
    cli_command = 'show security policies hit-count'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Logical system: root-logical-system
        p1 = re.compile(r'^(Logical system:)\s(?P<logical_system>\S+)$')

        # 9       junos-global     junos-global      GLOBAL-PERMIT-SSH-IN 541543
        # 11      untrust          UNTRUST-STRICT        STRICT-PERMIT-NTP-IN 1243
        p2 = re.compile(r'^(?P<index>\d+)\s+(?P<from_zone>\S+)\s+(?P<to_zone>\S+)\s+(?P<name>\S+)\s+(?P<policy_hit_count>\d+)$')

        # Number of policy: 12
        p3 = re.compile(r'(Number of policy:)\s(?P<total_policies>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Logical system: root-logical-system
            m = p1.match(line)
            if m:
                group = m.groupdict()
                logical_system = group['logical_system'] or "None"
                security_policy_count_list = ret_dict.setdefault('security_policy_counts', {})\
                    .setdefault(logical_system, {})\
                    .setdefault('security_policy', [])

                continue

            # 9       junos-global     junos-global      GLOBAL-PERMIT-SSH-IN 541543
            # 11      untrust          UNTRUST-STRICT        STRICT-PERMIT-NTP-IN 1243
            m = p2.match(line)
            if m:
                group = m.groupdict()
                security_policy_count_list.append({k: v for k, v in group.items()})
                continue

            # Number of policy: 12
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_policies = group['total_policies']
                ret_dict['security_policy_counts'][logical_system].update({'total_policies': total_policies})
                continue
        return ret_dict

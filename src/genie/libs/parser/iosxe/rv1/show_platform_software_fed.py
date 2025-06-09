"""show_platform_software_fed.py

    * 'show platform software fed switch {switch_var} access-security table usage'

"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import ListOf

log = logging.getLogger(__name__)

class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_var} access-security table usage'"""

    schema = {
        'feature': {
            str: {
                'asic': {
                    int: ListOf({
                        'mask': str,
                        'maximum': int,
                        'in_use': int,
                        'total_allocated': int,
                        'total_freed': int
                    })
                }
            }
        }
    }
                                
class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage(ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema):
    """Parser for 'show platform software fed switch {switch_var} access-security table usage'"""

    cli_command = 'show platform software fed switch {switch_var} access-security table usage'

    def cli(self, switch_var, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_var=switch_var)

        output = self.device.execute(cmd)

        # Initialize parsed dictionary
        ret_dict = {}

        # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
        p1 = re.compile(
            r'^(?P<feature>[\w\-]+)\s+(?P<mask>[\w\-]+)\s+(?P<asic>\d+)\s+'
            r'(?P<maximum>\d+)\s+(?P<in_use>\d+)\s+(?P<total_allocated>\d+)\s+'
            r'(?P<total_freed>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                feature_dict = ret_dict.setdefault('feature', {}).setdefault(group['feature'], {})
                asic_dict = feature_dict.setdefault('asic', {}).setdefault(int(group['asic']), [])
                asic_dict.append({
                    'mask': group['mask'],
                    'maximum': int(group['maximum']),
                    'in_use': int(group['in_use']),
                    'total_allocated': int(group['total_allocated']),
                    'total_freed': int(group['total_freed'])
                })

        return ret_dict

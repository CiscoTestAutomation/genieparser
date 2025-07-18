"""show_fips.py
    supported commands:
        * show fips authorization-key 
        * show fips status
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#  * 'show_fips_authorization_key '
# =================================================

class ShowFipsAuthorizationKeySchema(MetaParser):
    """Schema for show fips authorization-key"""

    schema = {
        "fips": {
            "stored_key": str
        }
    }


# =================================================
# Parser for:
#  * 'show_fips_authorization_key'
# =================================================
class ShowFipsAuthorizationKey(ShowFipsAuthorizationKeySchema):
    """Parser for show fips authorization-key"""

    cli_command = 'show fips authorization-key'

    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}
        #                  FIPS: Stored key (16) : 12345678901234567890123456789012
        p1 = re.compile(r'^FIPS: +Stored key +\((\d+)\) +: +(?P<stored_key>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #  FIPS: Stored key (16) : 12345678901234567890123456789012
            m =  p1.match(line)
            if m:
                group = m.groupdict()
                fp_dict = ret_dict.setdefault('fips', {})
                fp_dict.update({
                    'stored_key': (group['stored_key'])
                })
            else:
                fp_dict = ret_dict.setdefault('fips', {})
                fp_dict.update({
                    'stored_key': 'No key installed'
                })
                continue
        return ret_dict

class ShowFipsStatusSchema(MetaParser):
    """Schema for show fips status"""

    schema = {
        "fips_state": str,
        Optional("sesa_ready"): bool
    }

class ShowFipsStatus(ShowFipsStatusSchema):
    """Parser for show fips status"""

    cli_command = 'show fips status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}
        # Switch is in Fips Not-Configured state and not SESA Ready
        # Switch is in Fips Configured state and not SESA Ready
        # Switch is in Fips Running state and SESA Ready
        # Switch and Stacking are in Fips Not-Configured state and not SESA Ready
        p1 = re.compile(r'^Switch (is|and Stacking are) +in +Fips +(?P<fips_state>[\S\s]+)\s+state\s+and\s+(?P<sesa_ready>\S+)')

        # Switch and Stacking are running in fips mode
        # Switch and Stacking are not running in fips mode
        p2 = re.compile(r'^Switch and Stacking are (?P<fips_state>[\S\s]+) in fips mode')

        # Switch is not running in fips mode
        # Switch is running in fips mode
        p3 = re.compile(r'^Switch is (?P<fips_state>[\S\s]+) in fips mode$')

        for line in output.splitlines():
            line = line.strip()
            # Switch is in Fips Not-Configured state and not SESA Ready
            # Switch is in Fips Configured state and not SESA Ready
            # Switch is in Fips Running state and SESA Ready
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['sesa_ready'] == 'not':
                    ret_dict.update({
                        'fips_state': group['fips_state'],
                        'sesa_ready': False
                    })
                else:
                    ret_dict.update({
                        'fips_state': group['fips_state'],
                        'sesa_ready': True
                    })
                continue

            # Switch and Stacking are running in fips mode
            # Switch and Stacking are not running in fips mode
            m = p2.match(line)
            if m:
                ret_dict['fips_state'] = m.groupdict()['fips_state']
                continue
            
            # Switch is not running in fips mode
            # Switch is running in fips mode
            m = p3.match(line)
            if m:
                ret_dict['fips_state'] = m.groupdict()['fips_state']
                continue

        return ret_dict
''' show_license.py

IOSXE parsers for the following show commands:
    * show license
    * show license udi
    * show license summary
    * show license rum id all
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show license'
# =================

class ShowLicenseSchema(MetaParser):
    """Schema for show license."""

    schema = {
        'licenses': {
            int: {
                'feature': str,
                Optional('period_left'): str,
                Optional('period_minutes'): int,
                Optional('period_seconds'): int,
                Optional('license_type'): str,
                Optional('license_state'): str,
                Optional('count_in_use'): int,
                Optional('count_violation'): int,
                Optional('count'): str,
                Optional('license_priority'): str

            }
        }
    }



# =================
# Parser for:
#  * 'show license'
# =================
class ShowLicense(ShowLicenseSchema):
    """Parser for show license"""

    cli_command = 'show license'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Index 1 Feature: appxk9
        p1 = re.compile(r"Index\s+(?P<id>\d+)\s+Feature:\s+(?P<feature>\S+)")
        #         Period left: Life time
        p2 = re.compile(r"\s+(?P<period_left>(Life\s+time|Not\s+Activated))")
        # 	        Period Used: 0  minute  0  second
        p3 = re.compile(r"\s+(?P<period_minutes>\d+)\s+minute\s+(?P<period_seconds>\d+)\s+second")
        #         License Type: Permanent
        p4 = re.compile(r"\s+(?P<license_type>(Permanent|EvalRightToUse))")
        #         License State: Active, In Use
        p5 = re.compile(r"\s+((?P<count_in_use>\d+)/(?P<count_violation>\d+)\s+\(In-use/Violation\)|(?P<count>\S+))")
        #         License Priority: None
        p6 = re.compile(r"\s+(?P<license_priority>\S+)")
        #         License State: Active, Not in Use
        #         License State: Active, Not in Use, EULA not accepted
        p7 = re.compile(r"\s+(?P<license_state>(Active,\s+Not\s+in\s+Use,\s+EULA\s+not\s+accepted|Active,\s+In\s+Use|Active,\s+Not in\s+Use))")

        regex_map = {
            "Period left": p2,
            "Period Used": p3,
            "License Type": p4,
            "License Count": p5,
            "License Priority": p6,
            "License State": p7,
        }

        # initial variables
        license_dict = {}
        # Index 1 Feature: appxk9
        #         Period left: Life time
        #         License Type: Permanent
        #         License State: Active, In Use
        #         License Count: Non-Counted
        #         License Priority: Medium

        for line in out.splitlines():
            line_strip = line.strip()
            if not line_strip.startswith("Index"):
                try:
                    data_type, value = line_strip.split(":", 1)
                    regex = regex_map.get(data_type)
                except ValueError:
                    continue
            else:
                match = p1.match(line_strip)
                # Index 1 Feature: appxk9
                groups = match.groupdict()
                group_id = int(groups['id'])
                license_dict.update({group_id: {'feature': groups['feature']}})
                continue

            if regex:
                match = regex.match(value)
                groups = match.groupdict()
                for k, v in groups.items():
                    if v is None:
                        continue
                    if v.isdigit():
                        v = int(v)
                    license_dict[group_id].update({k: v})

        if license_dict:
            return {"licenses": license_dict}
        else:
            return {}
# ----------------------
class ShowLicenseUdiSchema(MetaParser):
    """Schema for show license udi"""
    schema = {
            'slotid': str,
            'pid': str,
            'sn': str,
            'udi': str
            }

class ShowLicenseUdi(ShowLicenseUdiSchema):
    """Parser for show license udi"""
    cli_command = 'show license udi'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # slotid pid sn udi
        p1 = re.compile(r"(?P<slotid>\S+)\s+(?P<pid>\S+)\s+(?P<sn>\S+)\s+(?P<udi>\S+)")
        # fixed length strings on third line
        # slotid: 9
        # pid   : 23
        # sn    : 15
        # udi   : 33
        # total 80 chars
        #SlotID   PID                    SN                      UDI
        #--------------------------------------------------------------------------------
        #*        ASR1001-X             JAF211403VH     ASR1001-X:JAF211403VH
        ret_dict={}
        for line in out.splitlines():
            line=line.strip()

            # udi line
            m=p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue
            '''
            if line.startswith('SlotID') or line.startswith('------'):
              continue
            else:
              ret_dict.update({'slotid':line[0:9].strip()})
              ret_dict.update({'pid':line[9:30].strip()})
              ret_dict.update({'sn':line[30:47].strip()})
              ret_dict.update({'udi':line[47:].strip()})
            ''' 

        return ret_dict

# ----------------------
# =================
# Schema for:
#  * 'show license summary'
# =================
class ShowLicenseSummarySchema(MetaParser):
    """Schema for show license udi"""
    schema = {
        'license_usage': {
            Any(): {
                'entitlement': str,
                'count': str,
                'status': str,
            }
        }
    }

# =================
# Parser for:
#  * 'show license summary'
# =================
class ShowLicenseSummary(ShowLicenseSummarySchema):
    """Parser for show license summary"""
    cli_command = 'show license summary'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        license_summ_dict = {}
        
        result_dict = {}

        # network-advantage       (C9300-48 Network Advan...)       1 IN USE
        # dna-advantage           (C9300-48 DNA Advantage)          1 IN USE

        # C9300 48P DNA Advantage  (C9300-48 DNA Advantage)          2 AUTHORIZED
        p0 = re.compile(r"^(?P<license>.+?)\s+\((?P<entitlement>.+)\)\s+(?P<count>\d+)\s+(?P<status>.+)$")

        for line in out.splitlines():
            line=line.strip()

            # udi line
            m=p0.match(line)
            if m:
                if 'license_usage' not in license_summ_dict:
                    result_dict = license_summ_dict.setdefault('license_usage', {})
                license = m.groupdict()['license']
                entitlement = m.groupdict()['entitlement']
                count = m.groupdict()['count']
                status = m.groupdict()['status']
                result_dict[license] = {}
                result_dict[license]['entitlement'] = entitlement
                result_dict[license]['count'] = count
                result_dict[license]['status'] = status
                continue
        return license_summ_dict

# =================
# Schema for:
#  * 'show license rum id all'
# =================

class ShowLicenseRumIdAllSchema(MetaParser):
    """Schema for show license rum id all."""
    schema = {
        'smart_license_usage_reports': {
            Any(): {
                'state': str,
                'flag': str,
                'feature_name': str
                }
        }
    }

# =================
# Parser for:
#  * 'show license rum id all'
# =================
class ShowLicenseRumIdAll(ShowLicenseRumIdAllSchema):
    """Parser for show license rum id all"""

    cli_command = 'show license rum id all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        # 1629870048          CLOSED    N     network-premier_2.5G
        p1 = re.compile(r'^(?P<report_id>\d+)\s+(?P<state>\S+)\s+(?P<flag>\w+)\s+(?P<feature_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            m =p1.match(line)
            if m:
                groups =m.groupdict()
                report_id = int(groups['report_id'])
                rum_id_dict = ret_dict.setdefault('smart_license_usage_reports', {}).setdefault(report_id, {})
                rum_id_dict['state'] = groups['state']
                rum_id_dict['flag'] =  groups['flag']
                rum_id_dict['feature_name'] = groups['feature_name']
                continue
        return ret_dict

"""show_incompatibility.py
NXOS parser for the following show commands:
* 'Schema for show incompatibility nxos {image}'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowIncompatibilityNxosSchema(MetaParser):
    """ Schema for show incompatibility nxos {image}."""

    schema = {
        Optional('incompatible_configuartion_status'): str,
        Optional('incompatible_configuartion_list'): {
            int: {
                "service": str,
                "capability": str,
                "description": str,
                "capability_requirement": str,
                "enable_Disable_command": str,
            },
        },
        'dynamic_incompatibility_status': str,
    }


class ShowIncompatibilityNxos(ShowIncompatibilityNxosSchema):
    """ Parser for show incompatibility nxos {image} """

    cli_command = [
        'show incompatibility nxos {image}'
    ]

    def cli(self, image=' ', output=None):
        if output is None:
            cmd = self.cli_command[0].format(image=image)
        output = self.device.execute(cmd)

        parsed_dict = {}

        # Checking incompatible configuration(s):
        # ---------------------------------------
        # No incompatible configurations
        # Checking dynamic incompatibilities:
        # -----------------------------------
        # No incompatible configurations
        p1 = re.compile(r'^(?P<status>No incompatible configurations)$')

        # 1) Service : otm , Capability : CAP_FEATURE_OTM_TRACK_DELAY_MS_CONFIGURED
        p2 = re.compile(r'^(?P<number>[\d]+)\)\s+Service : (?P<service>[\w]+)\s+,\s+Capability : (?P<capability>[\w]+)$')

        # Description : Objects with track delay in millliseconds detected
        p3 = re.compile(r'^Description : (?P<desc>(.*))$')

        # Capability requirement : STRICT
        p4 = re.compile(r'^Capability requirement : (?P<req>[\w]+)$')

        # Enable/Disable command : Please remove track delay in milliseconds from all objects
        p5 = re.compile(r'^Enable\/Disable command : (?P<enable_cmd>(.*))$')

        for line in output.splitlines():
            line = line.strip()

            # Checking incompatible configuration(s):
            # ---------------------------------------
            # No incompatible configurations
            # Checking dynamic incompatibilities:
            # -----------------------------------
            # No incompatible configurations
            m = p1.match(line)
            if m:
                if parsed_dict.get('incompatible_configuartion_list') or parsed_dict.get(
                        'incompatible_configuartion_status'):
                    parsed_dict['dynamic_incompatibility_status'] = m.groupdict()['status']
                else:
                    parsed_dict['incompatible_configuartion_status'] = m.groupdict()['status']
                continue

            # 1) Service : otm , Capability : CAP_FEATURE_OTM_TRACK_DELAY_MS_CONFIGURED
            m = p2.match(line)
            if m:
                group = m.groupdict()
                new_dict = parsed_dict.setdefault('incompatible_configuartion_list', {})
                no = int(group['number'])
                result_dict1 = new_dict.setdefault(no, {})
                result_dict1['service'] = group['service']
                result_dict1['capability'] = group['capability']
                continue

            # Description : Objects with track delay in millliseconds detected
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_dict1['description'] = group['desc']
                continue

            # Capability requirement : STRICT
            m = p4.match(line)
            if m:
                group = m.groupdict()
                result_dict1['capability_requirement'] = group['req']
                continue

            # Enable/Disable command : Please remove track delay in milliseconds from all objects
            m = p5.match(line)
            if m:
                group = m.groupdict()
                result_dict1['enable_Disable_command'] = group['enable_cmd']
                continue

        return parsed_dict

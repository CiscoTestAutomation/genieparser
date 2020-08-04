import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================
# Schema for:
#  * 'show class-map'
# ===================
class ShowClassMapSchema(MetaParser):
    """Schema for show class-map."""

    schema = {
        "class_maps": {
            str: {
              "match_criteria": str,
              "cm_id": int,
              "match_policy": str,
              Optional("description"): str,
            }
        }
    }


# ===================
# Parser for:
#  * 'show class-map'
# ===================
class ShowClassMap(ShowClassMapSchema):
    """Parser for show class-map"""

    cli_command = ['show class-map']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        class_map_dict = {}

        cm_header_capture = re.compile(
            r"^(\s+|)Class\sMap\s(?P<match_criteria>\S+)\s+(?P<cm_name>\S+)\s+\(id\s+(?P<cm_id>\d+)\)", re.MULTILINE)
        description_capture = re.compile(r"^Description:\s+(?P<description>.*$)", re.MULTILINE)
        match_policy_capture = re.compile(r"^Match\s+(?P<match_policy>\S+)", re.MULTILINE)


        # Remove unwanted lines from raw text
        for line in out.splitlines():
            line = line.strip()
            cm_match = cm_header_capture.match(line)
            if not class_map_dict.get('class_maps'):
                class_map_dict['class_maps'] = {}
            if cm_match:
                groups = cm_match.groupdict()
                cm_name = groups['cm_name']
                match_criteria = groups['match_criteria']
                cm_id = int(groups['cm_id'])
                if not class_map_dict['class_maps'].get(cm_name, {}):
                    class_map_dict['class_maps'].update({cm_name: {}})
                class_map_dict['class_maps'][cm_name].update({'match_criteria': match_criteria, 'cm_id': cm_id})
                continue
            desc_match = description_capture.match(line)
            if desc_match:
                groups = desc_match.groupdict()
                description = groups['description']
                if class_map_dict['class_maps'].get(cm_name, {}):
                    class_map_dict['class_maps'][cm_name].update({'description': description})
                continue
            match_policy_match = match_policy_capture.match(line)
            if match_policy_match:
                groups = match_policy_match.groupdict()
                match_policy = groups['match_policy']
                if class_map_dict['class_maps'].get(cm_name, {}):
                    class_map_dict['class_maps'][cm_name].update({'match_policy': match_policy})
                continue

        return class_map_dict
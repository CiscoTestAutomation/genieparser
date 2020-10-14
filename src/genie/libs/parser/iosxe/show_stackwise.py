import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#  * 'show_stackwise_virtual_dual_active_detection'
# =================================================
class ShowStackwiseVirtualDualActiveDetectionSchema(MetaParser):
    """Schema for show_stackwise_virtual_dual_active_detection."""

    schema = {
        "dad_port": {
            "switches": {
                int: {
                    str: {
                        "status": str
                    }
                }
            }
        }
    }


# =================================================
# Parser for:
#  * 'show_stackwise_virtual_dual_active_detection'
# =================================================
class ShowStackwiseVirtualDualActiveDetection(ShowStackwiseVirtualDualActiveDetectionSchema):
    """Parser for show stackwise-virtual dual-active-detection"""

    cli_command = 'show stackwise-virtual dual-active-detection'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        dad_dict = {'switches': {}}
        # Dual-Active-Detection Configuration:
        # -------------------------------------
        # Switch  Dad port                        Status
        # ------  ------------                    ---------
        # 1       FortyGigabitEthernet1/0/3       up
        #         FortyGigabitEthernet1/0/4       up
        # 2       FortyGigabitEthernet2/0/3       up
        #         FortyGigabitEthernet2/0/4       up
        #         p1 = re.compile(r"^(?P<switch_id>\d+)\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)
        #         p2 = re.compile(r"^\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)
        #

        dad_dict = {}

        # 1       FortyGigabitEthernet1/0/3       up
        switch_id_capture = re.compile(r"^(?P<switch_id>\d+)\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))",
                                         re.MULTILINE)
        #         FortyGigabitEthernet1/0/4       up
        port_capture = re.compile(r"^\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if clean_line_strip.startswith(remove_lines):
                    clean_lines.remove(clean_line)
            return clean_lines

        remove_lines = ('----', 'Switch', 'Dual')
        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        switch_id = ''

        for line in out:
            match = switch_id_capture.match(line)
            # 1       FortyGigabitEthernet1/0/3       up
            if not dad_dict.get('dad_port'):
                dad_dict['dad_port'] = {}
            if not dad_dict['dad_port'].get('switches'):
                dad_dict['dad_port']['switches'] = {}
            if match:
                groups = match.groupdict()
                switch_id = int(groups['switch_id'])
                dad_dict['dad_port']['switches'].update({switch_id: {groups['dad_port']: {'status': groups['status']}}})
            port_match = port_capture.match(line)
            #         FortyGigabitEthernet1/0/4       up
            if port_match:
                groups = port_match.groupdict()
                dad_dict['dad_port']['switches'][switch_id].update({groups['dad_port']: {'status': groups['status']}})
        return dad_dict

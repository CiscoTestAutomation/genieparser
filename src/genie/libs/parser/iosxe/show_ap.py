import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =========================================
# Schema for:
#  * 'show ap led-brightness-level summary'
# =========================================
class ShowApLedBrightnessLevelSummarySchema(MetaParser):
    """Schema for show ap led-brightness-level summary."""

    schema = {
        "ap_name": {
            str: {
                "led_brightness_level": int
            }
        }
    }


# =========================================
# Parser for:
#  * 'show ap led-brightness-level summary'
# =========================================
class ShowApLedBrightnessLevelSummary(ShowApLedBrightnessLevelSummarySchema):
    """Parser for show ap led-brightness-level summary"""

    cli_command = 'show ap led-brightness-level summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_led_brightness_level_summary_dict = {}

        # AP Name                           LED Brightness level
        # --------------------------------------------------------
        # b881-cap4                     8
        # b852-cap6                     8
        # b861-cap14                    8
        # b822-cap10                    8
        # b871-cap1                     8
        # b861-cap7                     8
        # b852-cap18                    8
        # b871-cap3                     8
        # b862-cap2                     8
        # b801-cap16                    8
        #
        # AP Name                           LED Brightness level
        # --------------------------------------------------------
        # b832-cap3                     8
        # b802-cap4                     8
        # b862-cap5                     8
        # b851-cap9                     8
        # b802-cap8                     8
        # b822-cap14                    8
        # b872-cap8                     8
        # b872-cap6                     8
        # b862-cap18                    8
        # b822-cap16                    8

        # AP Name                           LED Brightness level
        ap_header_capture = re.compile(r"^AP\s+Name\s+LED\s+Brightness\s+level$")
        # --------------------------------------------------------
        delimiter_capture = re.compile(r"^--------------------------------------------------------$")
        # jain-farallon                  8
        ap_info_capture = re.compile(r"^(?P<ap_name>\S+)\s+(?P<led_brightness_level>\d+)$")

        for line in out.splitlines():
            line = line.strip()
            # AP Name                           LED Brightness level
            if ap_header_capture.match(line):
                continue
            # --------------------------------------------------------
            elif delimiter_capture.match(line):
                continue
            # jain-farallon                  8
            elif ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = groups['ap_name']
                led_brightness_level = int(groups['led_brightness_level'])
                if not ap_led_brightness_level_summary_dict.get('ap_name', {}):
                    ap_led_brightness_level_summary_dict['ap_name'] = {}
                ap_led_brightness_level_summary_dict['ap_name'][ap_name] = {
                    'led_brightness_level': led_brightness_level}
                continue

        return ap_led_brightness_level_summary_dict
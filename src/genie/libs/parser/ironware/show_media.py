"""
Module:
    genie.libs.parser.ironware.show_media

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Media parsers for IronWare devices

Parsers:
    * show media <interface>
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show media {interface}'
# ======================================================
class ShowMediaInterfaceSchema(MetaParser):
    """Schema for show media"""
    schema = {
        Any(): {
            'type': str,
            'version': str,
            'part': str,
            'serial': str
        }
    }


# ====================================================
#  parser for 'show media {interface}'
# ====================================================
class ShowMediaInterface(ShowMediaInterfaceSchema):
    """
    Parser for show media on Ironware devices
    """
    cli_command = 'show media {interface}'

    """
    Type  : 10GE LR 10km SFP+
    Vendor:          FIBERSTORE      , Version:                 A
    Part# :          SFP-10GLR-31    , Serial#:     J0612100048
    """

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                                        interface=interface))
        else:
            out = output

        result_dict = {}

        # Type  : 10GE LR 10km SFP+
        p1 = re.compile(r'(^Type\s+:\s+(?P<type>[^\n]+))')

        # Vendor:          FIBERSTORE, Version:   A
        p2 = re.compile(r'(^Vendor:\s+(?P<vendor>[^\s|,]+)(\s+,|,)\s+'
                        r'Version:(\s+(?P<ver>[^\n]+)|$))')

        # Part# :  SFP-10GLR-31, Serial#: J0612100048
        p3 = re.compile(r'(^Part#\s+:\s+(?P<part>[^\s|,]+)(\s+,|,)\s+'
                        r'Serial#:\s+(?P<serial>[^$]+))')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                media_dict = result_dict.setdefault(interface, {})

                media_dict['type'] = m.groupdict()['type']
                continue

            m = p2.match(line)
            if m:
                ver = m.groupdict().get('ver')
                media_dict['version'] = ver if ver is not None else 'Unknown'
                continue

            m = p3.match(line)
            if m:
                media_dict['part'] = m.groupdict()['part']
                media_dict['serial'] = m.groupdict()['serial']
                continue

        return result_dict

"""show_platform.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_power import ShowStackPower as ShowStackPower_iosxe,\
                                               ShowPowerInlineInterface as ShowPowerInlineInterface_iosxe


class ShowStackPower(ShowStackPower_iosxe):
    """Parser for show stack-power"""
    pass


class ShowPowerInlineInterface(ShowPowerInlineInterface_iosxe):
    """Parser for show power inline <interface>"""
    pass
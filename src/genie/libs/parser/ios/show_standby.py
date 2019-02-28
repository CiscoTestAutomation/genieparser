'''
IOS Parsers

'''
# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, Optional

from genie.libs.parser.iosxe.show_standby import ShowStandbyDelay as ShowStandbyDelay_iosxe, \
                                                 ShowStandbyAll as ShowStandbyAll_iosxe,\
                                                 ShowStandbyInternal as ShowStandbyInternal_iosxe


class ShowStandbyInternal(ShowStandbyInternal_iosxe):
    """Parser for show standby internal"""
    pass

class ShowStandbyAll(ShowStandbyAll_iosxe):
    """Parser for show standby all"""
    pass

class ShowStandbyDelay(ShowStandbyDelay_iosxe):
    """Parser for show standby delay"""
    pass

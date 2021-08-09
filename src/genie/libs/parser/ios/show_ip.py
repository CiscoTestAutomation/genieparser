"""show_ip_nat.py
    supported commands:
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat statistics
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional,
                                                Or,
                                                And,
                                                Default,
                                                Use)

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_ip import (ShowIpNatTranslations 
                                                as ShowIpNatTranslationsIosxe,
                                                ShowIpNatStatistics 
                                                as ShowIpNatStatisticsIosxe)


class ShowIpNatTranslations(ShowIpNatTranslationsIosxe):
    """
        * show ip nat translations
        * show ip nat translations verbose
    """

    pass


class ShowIpNatStatistics(ShowIpNatStatisticsIosxe):
    """ Schema for command:
            * show ip nat statistics
    """

    pass

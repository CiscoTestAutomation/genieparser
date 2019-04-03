'''show_issu.py

IOSXE parsers for the following show commands:
   * show issu state detail
   * show issu rollback-timer
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                               Default, Use
# Genie Libs
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_issu import ShowIssuStateDetail as ShowIssuStateDetail_iosxe,\
                                              ShowIssuRollbackTimer as ShowIssuRollbackTimer_iosxe


# ====================================
#  Parser for 'show issu state detail'
# ====================================
class ShowIssuStateDetail(ShowIssuStateDetail_iosxe):
    """Parser for show issu state detail"""
    pass


# ======================================
#  Parser for 'show issu rollback-timer'
# ======================================
class ShowIssuRollbackTimer(ShowIssuRollbackTimer_iosxe):
    """Parser for show issu rollback-timer"""
    pass
'''show_issu.py

IOSXE parsers for the following show commands:
   * show issu state detail
   * show issu rollback-timer
'''
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
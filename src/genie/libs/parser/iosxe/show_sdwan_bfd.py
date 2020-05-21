'''
* 'show sdwan bfd sessions'
* 'show sdwan bfd summary'
'''
from genie.libs.parser.viptela.show_bfd_sessions import ShowBfdSessions as ShowBfdSessions_viptela
from genie.libs.parser.viptela.show_bfd_summary import ShowBfdSummary as ShowBfdSummary_viptela


# =====================================
# Parser for 'show sdwan bfd sessions'
# =====================================
class ShowSdwanBfdSessions(ShowBfdSessions_viptela):

    """ Parser for "show sdwan bfd sessions" """
    pass


# ===============================================
# Parser for 'show sdwan bfd summary'
# ===============================================
class ShowSdwanBfdSummary(ShowBfdSummary_viptela):

    """ Parser for "show sdwan bfd summary" """
    pass

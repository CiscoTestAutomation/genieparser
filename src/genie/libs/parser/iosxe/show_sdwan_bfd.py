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
    cli_command = 'show sdwan bfd sessions'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
    
        return super().cli(output = show_output)


# ===============================================
# Parser for 'show sdwan bfd summary'
# ===============================================
class ShowSdwanBfdSummary(ShowBfdSummary_viptela):

    """ Parser for "show sdwan bfd summary" """
    cli_command = 'show sdwan bfd summary'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
    
        return super().cli(output = show_output)

'''
* 'show sdwan system status'
'''
from genie.libs.parser.viptela.show_system_status import ShowSystemStatus as ShowSystemStatus_viptela

# =====================================
# Parser for 'show sdwan system status'
# =====================================
class ShowSdwanSystemStatus(ShowSystemStatus_viptela):

    """ Parser for "show sdwan system status" """
    cli_command = 'show sdwan system status'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)
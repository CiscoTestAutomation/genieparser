'''
* 'show sdwan reboot history'
'''
from genie.libs.parser.viptela.show_reboot_history import ShowRebootHistory as ShowRebootHistory_viptela

# =====================================
# Parser for 'show sdwan reboot history'
# =====================================
class ShowSdwanRebootHistory(ShowRebootHistory_viptela):

    """ Parser for "show sdwan reboot history" """
    cli_command = 'show sdwan reboot history'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)
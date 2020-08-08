'''
* 'show sdwan version'
'''
from genie.libs.parser.viptela.show_version import ShowVersion as ShowVersion_viptela

# =====================================
# Parser for 'show sdwan version'
# =====================================
class ShowSdwanVersion(ShowVersion_viptela):

    """ Parser for "show sdwan version" """
    cli_command = 'show sdwan version'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)
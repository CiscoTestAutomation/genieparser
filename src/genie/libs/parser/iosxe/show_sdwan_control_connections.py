'''
* 'show sdwan control connections'
'''
from genie.libs.parser.viptela.show_control_connections import ShowControlConnections as ShowControlConnections_viptela


# ===========================================
# Parser for 'show sdwan control connections'
# ===========================================
class ShowSdwanControlConnections(ShowControlConnections_viptela):

    """ Parser for "show sdwan control connections" """
    cli_command = 'show sdwan control connections'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
    
        return super().cli(output = show_output)

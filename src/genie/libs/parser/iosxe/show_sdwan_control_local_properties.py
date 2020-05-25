'''
* 'show control local-properties'
'''
from genie.libs.parser.viptela.show_control_local_properties import ShowControlLocalProperties as ShowControlLocalProperties_viptela


# ===============================================
# Parser for 'show sdwan control local-properties'
# ===============================================

class ShowSdwanControlLocalProperties(ShowControlLocalProperties_viptela):

    """ Parser for "show sdwan control local-properties" """
    cli_command = 'show sdwan control local-properties'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
    
        return super().cli(output = show_output)
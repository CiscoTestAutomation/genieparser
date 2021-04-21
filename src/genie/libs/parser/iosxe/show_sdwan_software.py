'''
* 'show sdwan software'
'''
from genie.libs.parser.viptela.show_software import ShowSoftwaretab as ShowSoftwaretab_viptela
import re

# =====================================
# Parser for 'show sdwan software'
# =====================================
class ShowSdwanSoftware(ShowSoftwaretab_viptela):

    """ Parser for "show sdwan software" """
    cli_command = 'show sdwan software'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        if re.search('Total Space:',show_output):
            fin=re.search('Total Space:.*',show_output)
            show_output=show_output.replace(fin.group(0),' ')
            
        return super().cli(output = show_output)
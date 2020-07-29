'''
* 'show sdwan omp summary'
'''

from genie.libs.parser.viptela.show_omp import ShowOmpSummary as ShowOmpSummary_viptela


# ===============================================
# Parser for 'show sdwan omp summary'
# ===============================================
class ShowSdwanOmpSummary(ShowOmpSummary_viptela):

    """ Parser for "show sdwan omp summary" """
    cli_command = 'show sdwan omp summary'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
    
        return super().cli(output = show_output)
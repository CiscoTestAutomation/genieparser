'''
* 'show sdwan omp summary'
* 'show sdwan omp peers'
* 'show sdwan omp tlocs'
* 'show sdwan omp tloc-paths'
'''

from genie.libs.parser.viptela.show_omp import ShowOmpSummary as ShowOmpSummary_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocs as ShowOmpTlocs_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpPeers as ShowOmpPeers_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocPath as ShowOmpTlocPath_viptela

# ===============================================
# Parser for 'show sdwan omp summary'
# ===============================================
class ShowSdwanOmpSummary(ShowOmpSummary_viptela):

    """ Parser for "show sdwan omp summary" """
    cli_command = 'show sdwan omp summary'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)
    
        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp peers'
# ===============================================
class ShowSdwanOmpPeers(ShowOmpPeers_viptela):

    """ Parser for "show sdwan omp peers" """
    cli_command = 'show sdwan omp peers'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)
    
        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp tlocs'
# ===============================================
class ShowSdwanOmpTlocs(ShowOmpTlocs_viptela):

    """ Parser for "show sdwan omp tlocs" """
    cli_command = 'show sdwan omp tlocs'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)
    
        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp tloc-paths'
# ===============================================
class ShowSdwanOmpTlocPath(ShowOmpTlocPath_viptela):

    """ Parser for "show sdwan omp tloc-paths" """
    cli_command = 'show sdwan omp tloc-paths'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)
    
        return super().cli(output = show_output)

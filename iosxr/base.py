__all__ = (
        'IosxrCaasMetaParser',
)

from ats import tcl
from ats.tcl import tclobj, tclstr
from xbu_shared.parser import CaasMetaParser

class IosxrCaasMetaParser(CaasMetaParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tcl.call('package', 'require', 'IOSXR_Parser')


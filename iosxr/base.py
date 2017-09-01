__all__ = (
        'IosxrCaasMetaParser',
)

try:
    from ats import tcl
except ImportError:
    pass

from parser import CaasMetaParser

class IosxrCaasMetaParser(CaasMetaParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tcl.call('package', 'require', 'IOSXR_Parser')


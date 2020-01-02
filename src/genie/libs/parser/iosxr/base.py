__all__ = (
        'IosxrCaasMetaParser',
)

try:
    from pyats import tcl
except Exception:
    pass

from genie.libs.parser import CaasMetaParser

class IosxrCaasMetaParser(CaasMetaParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tcl.call('package', 'require', 'IOSXR_Parser')


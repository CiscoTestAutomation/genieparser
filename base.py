__all__ = (
        'CaasMetaParser',
)

import os
from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser

class CaasMetaParser(MetaParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.environ['XBU_SHARED'] not in tcl.cast_list(tcl.get_var('::auto_path'), item_cast=tclstr):
            tcl.call('lappend', '::auto_path', os.environ['XBU_SHARED'])
        tcl.call('package', 'require', 'cAAs')


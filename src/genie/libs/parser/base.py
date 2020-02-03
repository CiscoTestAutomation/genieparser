__all__ = (
    'tcl_invoke_ats_cmd',
    'tcl_package_require_caas',
    'tcl_package_require_caas_parsers',
    'tcl_invoke_caas_abstract_parser',
    'CaasMetaParser',
)

import os

try:
    from pyats import tcl
    from pyats.tcl import tclstr, TclCommand
except Exception:
    pass

from genie.metaparser import MetaParser


def tcl_invoke_ats_cmd(cmd, *, cast_=None, **kwargs):

    cmd = TclCommand(cmd, keywords=kwargs, cast=tcl.cast_list)
    result = cmd()
    result_code = result[0]
    result_msg = result[1] if len(result) == 2 else result[1:]
    try:
        result_code = tcl.cast_int(result[0])
    except ValueError:
        result_code = tclstr(result[0])
    if result_code in ('passed', 1):
        if cast_:
            result_msg = cast_(result_msg)
        return result_msg
    else:
        raise RuntimeError(tclstr(result_msg))


def tcl_package_require_caas():
    if 'XBU_SHARED' in os.environ \
            and os.environ['XBU_SHARED'] not in \
            tcl.cast_list(tcl.get_var('::auto_path'), item_cast=tclstr):
        tcl.call('lappend', '::auto_path', os.environ['XBU_SHARED'])
    tcl.call('package', 'require', 'cAAs')


def tcl_package_require_caas_parsers():
    tcl_package_require_caas()
    tcl.call('package', 'require', 'IOS_Parser')
    tcl.call('package', 'require', 'IOSXE_Parser')
    tcl.call('package', 'require', 'NXOS_Parser')
    tcl.call('package', 'require', 'IOSXR_Parser')
    tcl.call('package', 'require', 'MULTIOS_Parser')


def tcl_invoke_caas_abstract_parser(device, exec, *,
                                    cast_ = None,
                                    **kwargs):
    tcl_package_require_caas_parsers()

    try:
        device = device.handle
    except AttributeError:
        pass
    kwargs['device'] = device
    kwargs['exec'] = exec

    return tcl_invoke_ats_cmd('::caas::abstract',
                              cast_ = cast_ or tcl.cast_keyed_list,
                              **kwargs)


class CaasMetaParser(MetaParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tcl_package_require_caas_parsers()

# vim: ft=python ts=8 sw=4 et

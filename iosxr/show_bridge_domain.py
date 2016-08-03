''' show_bridge_domain.py

show bridge domain parser class

'''
from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any
from xbu_shared.parser.iosxr import IosxrCaasMetaParser

"""
    TODO: bpetrovi - Aug 2, 2016 
# XR command: "show l2vpn bridge-domain [group <group>] [bd-name <name>]"
# XR command: "show l2vpn bridge-domain [neighbor <neighbor> [pw-id <id>]]"
# XR command: "show l2vpn bridge-domain [interface <interface>]"
# XR command: "show l2vpn bridge-domain [pbb core]"
# XR command: "show l2vpn bridge-domain [pbb edge [core-bridge <name>]]"
# XR command: "show l2vpn bridge-domain [pbb isid <isid>]"
# XR command: "show l2vpn bridge-domain [no-statistics]"
# XR command: "show l2vpn bridge-domain [location <loc> | standby]"
# XR command: "show l2vpn bridge-domain [group <group>] [bd-name <name>] detail"
# XR command: "show l2vpn bridge-domain [neighbor <neighbor> [pw-id <id>]] detail"
# XR command: "show l2vpn bridge-domain [interface <interface>] detail"
# XR command: "show l2vpn bridge-domain [pbb core] detail"
# XR command: "show l2vpn bridge-domain [pbb edge [core-bridge <name>]] detail"
# XR command: "show l2vpn bridge-domain [pbb isid <isid>] detail"
# XR command: "show l2vpn bridge-domain [no-statistics] detail"
# XR command: "show l2vpn bridge-domain detail [location <loc> | standby]"
# XR command: "show l2vpn bridge-domain [group <group>] [bd-name <name>] brief"
# XR command: "show l2vpn bridge-domain [neighbor <neighbor> [pw-id <id>]] brief"
# XR command: "show l2vpn bridge-domain [interface <interface>] brief"
# XR command: "show l2vpn bridge-domain [pbb core] brief"
# XR command: "show l2vpn bridge-domain [pbb edge [core-bridge <name>]] brief"
# XR command: "show l2vpn bridge-domain [pbb isid <isid>] brief"
# XR command: "show l2vpn bridge-domain [no-statistics] brief"
# XR command: "show l2vpn bridge-domain brief [location <loc> | standby]"
# XR command: "show l2vpn bridge-domain bd-name <name> detail"
# XR command: "show l2vpn bridge-domain neighbor <neighbor> detail"
# XR command: "show l2vpn bridge-domain group <grp> detail"
"""


class ShowL2VpnBridgeDomainSummary(IosxrCaasMetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'TODO:': {
                        'module': {
                                 Any(): {
                                         'bios_compile_time': str,
                                         'bios_version': str,
                                         'image_compile_time': str,
                                         'image_version': str,
                                         'status': str},}},
              'hardware': {
                        'bootflash': str,
                        'chassis': str,
                        'cpu': str,
                        'device_name': str,
                        'memory': str,
                        'model': str,
                        'processor_board_id': str,
                        'slots': str,
                        Any(): str,},
              'kernel_uptime': {
                        'days': str,
                        'hours': str,
                        'minutes': str,
                        'seconds': str},
              'reason': str,
              'software': {
                        'bios': str,
                        'bios_compile_time': str,
                        'kickstart': str,
                        'kickstart_compile_time': str,
                        'kickstart_image_file': str,
                        'system': str,
                        'system_compile_time': str,
                        'system_image_file': str},
              'system_version': str,
              Any(): str,}
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        #no need to do router_show calls, internally MetaParser code looks
        #in caas, then goes 4, or 7 levels down to find the right parser, with
        #router_show being one of the options
        #TODO: look into how we can utilize hfr-mpls parsers
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show l2vpn bridge-domain summary')
        return tcl.cast_any(result[1])

class ShowL2VpnBridgeDomainBrief(IosxrCaasMetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'TODO:': {
                        'module': {
                                 Any(): {
                                         'bios_compile_time': str,
                                         'bios_version': str,
                                         'image_compile_time': str,
                                         'image_version': str,
                                         'status': str},}},
              'hardware': {
                        'bootflash': str,
                        'chassis': str,
                        'cpu': str,
                        'device_name': str,
                        'memory': str,
                        'model': str,
                        'processor_board_id': str,
                        'slots': str,
                        Any(): str,},
              'kernel_uptime': {
                        'days': str,
                        'hours': str,
                        'minutes': str,
                        'seconds': str},
              'reason': str,
              'software': {
                        'bios': str,
                        'bios_compile_time': str,
                        'kickstart': str,
                        'kickstart_compile_time': str,
                        'kickstart_image_file': str,
                        'system': str,
                        'system_compile_time': str,
                        'system_image_file': str},
              'system_version': str,
              Any(): str,}
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        #no need to do router_show calls, internally MetaParser code looks
        #in caas, then goes 4, or 7 levels down to find the right parser, with
        #router_show being one of the options
        #TODO: look into how we can utilize hfr-mpls parsers
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show l2vpn bridge-domain brief')
        return tcl.cast_any(result[1])


class ShowL2VpnBridgeDomain(IosxrCaasMetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'TODO:': {
                        'module': {
                                 Any(): {
                                         'bios_compile_time': str,
                                         'bios_version': str,
                                         'image_compile_time': str,
                                         'image_version': str,
                                         'status': str},}},
              'hardware': {
                        'bootflash': str,
                        'chassis': str,
                        'cpu': str,
                        'device_name': str,
                        'memory': str,
                        'model': str,
                        'processor_board_id': str,
                        'slots': str,
                        Any(): str,},
              'kernel_uptime': {
                        'days': str,
                        'hours': str,
                        'minutes': str,
                        'seconds': str},
              'reason': str,
              'software': {
                        'bios': str,
                        'bios_compile_time': str,
                        'kickstart': str,
                        'kickstart_compile_time': str,
                        'kickstart_image_file': str,
                        'system': str,
                        'system_compile_time': str,
                        'system_image_file': str},
              'system_version': str,
              Any(): str,}
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        #no need to do router_show calls, internally MetaParser code looks
        #in caas, then goes 4, or 7 levels down to find the right parser, with
        #router_show being one of the options
        #TODO: look into how we can utilize hfr-mpls parsers
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show l2vpn bridge-domain')
        return tcl.cast_any(result[1])


class ShowL2VpnBridgeDomainDetail(IosxrCaasMetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'TODO:': {
                        'module': {
                                 Any(): {
                                         'bios_compile_time': str,
                                         'bios_version': str,
                                         'image_compile_time': str,
                                         'image_version': str,
                                         'status': str},}},
              'hardware': {
                        'bootflash': str,
                        'chassis': str,
                        'cpu': str,
                        'device_name': str,
                        'memory': str,
                        'model': str,
                        'processor_board_id': str,
                        'slots': str,
                        Any(): str,},
              'kernel_uptime': {
                        'days': str,
                        'hours': str,
                        'minutes': str,
                        'seconds': str},
              'reason': str,
              'software': {
                        'bios': str,
                        'bios_compile_time': str,
                        'kickstart': str,
                        'kickstart_compile_time': str,
                        'kickstart_image_file': str,
                        'system': str,
                        'system_compile_time': str,
                        'system_image_file': str},
              'system_version': str,
              Any(): str,}
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        #no need to do router_show calls, internally MetaParser code looks
        #in caas, then goes 4, or 7 levels down to find the right parser, with
        #router_show being one of the options
        #TODO: look into how we can utilize hfr-mpls parsers
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show l2vpn bridge-domain detail')
        return tcl.cast_any(result[1])

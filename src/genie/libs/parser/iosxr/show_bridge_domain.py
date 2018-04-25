"""show_bridge_domain.py

show bridge domain parser class

"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

from genie.libs.parser.base import *

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


class ShowL2VpnBridgeDomainSummary(MetaParser):
    """Parser for show l2vpn bridge-domain summary"""
    # parser class - implements detail parsing mechanisms for cli, xml, and yang output.

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
        '''parsing mechanism: cli
        '''

        cmd = 'show l2vpn bridge-domain summary'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowL2VpnBridgeDomainBrief(MetaParser):
    """Parser for show l2vpn bridge-domain brief"""
    # parser class - implements detail parsing mechanisms for cli, xml, and yang output.

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
        '''parsing mechanism: cli
        '''

        cmd = 'show l2vpn bridge-domain brief'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowL2VpnBridgeDomain(MetaParser):
    """Parser for show l2vpn bridge-domain"""
    # parser class - implements detail parsing mechanisms for cli, xml, and yang output.

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
        '''parsing mechanism: cli
        '''

        cmd = 'show l2vpn bridge-domain'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowL2VpnBridgeDomainDetail(MetaParser):
    """Parser for show l2vpn bridge-domain detail"""
    # parser class - implements detail parsing mechanisms for cli, xml, and yang output.

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
        '''parsing mechanism: cli
        '''

        cmd = 'show l2vpn bridge-domain detail'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl

# vim: ft=python ts=8 sw=4 et

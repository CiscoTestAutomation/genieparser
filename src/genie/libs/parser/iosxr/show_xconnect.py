"""show_xconnect.py

show xsconnect parser class

"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

from genie.libs.parser.base import *

"""
    TODO: bpetrovi - Aug 2, 2016
        # XR command: "show l2vpn xconnect group xc1g"
        # XR command: "show l2vpn xconnect interface <intf>"
        # Yang section for all parsers
        # XML section for all parsers

"""


class ShowL2VpnXconnectSummary(MetaParser):
    """Parser for show l2vpn xconnect summary"""
    # parser class - implements detail parsing mechanisms for cli output.


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
    cli_command = 'show l2vpn xconnect summary'

    def cli(self):
        '''parsing mechanism: cli
        '''

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl


class ShowL2VpnXconnectBrief(MetaParser):
    """Parser for show l2vpn xconnect brief"""
    # parser class - implements detail parsing mechanisms for cli output.


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
    cli_command = 'show l2vpn xconnect brief'
    def cli(self):
        '''parsing mechanism: cli
        '''

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl


class ShowL2VpnXconnectDetail(MetaParser):
    """Parser for show l2vpn xconnect detail"""
    # parser class - implements detail parsing mechanisms for cli output.

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'cmp': {
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
    cli_command = 'show l2vpn xconnect detail'

    def cli(self):
        '''parsing mechanism: cli
        '''


        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl


class ShowL2VpnXconnectMp2mpDetail(MetaParser):
    """Parser for show l2vpn xconnect mp2mp detail"""
    # parser class - implements detail parsing mechanisms for cli output.

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    """
    schema = {'cmp': {
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
    cli_command = 'show l2vpn xconnect mp2mp detail'

    def cli(self):
        '''parsing mechanism: cli
        '''

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl

# vim: ft=python ts=8 sw=4 et

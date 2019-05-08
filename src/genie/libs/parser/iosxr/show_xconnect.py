"""show_xconnect.py

show xsconnect parser class

  supported commands:
   *  show l2vpn xconnect
   
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use

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


class ShowL2VpnXconnectSchema(MetaParser):
    """Schema for show l2vpn xconnect"""
    schema = {
      'groups': {
        Any(): {
          'Name': {
            Any(): {
              's0': str,
              'segment_1': {
                Any(): {
                  's1': str,
                  'segment_2': {
                    Any(): {
                      's2': str,
                    },
                  },
                },
              },
            },
          },
        },
      },
    }


class ShowL2VpnXconnect(ShowL2VpnXconnectSchema):
    """Parser for show l2vpn xconnect """

    cli_command = 'show l2vpn xconnect'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

#    Test_XCONN_Group
#               1000     DN   Gi0/0/0/5.1000    UP   1.1.1.206       1000   DN
            p1 = re.compile(r'^(?P<group>[\w]+)$')

            p2 = re.compile(r'^(?P<name>[a-zA-Z0-9]+) '
                            '+(?P<s0>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                            '+(?P<segment_1>.*?) ' 
                            '+(?P<s1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                            '+(?P<segment_2>.*?) ' 
                            '+(?P<s2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}) \
                    .setdefault(str(group['group']), {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = group_dict.setdefault('Name', {}) \
                    .setdefault(str(group['name']), {})
                name_dict['s0'] = str(group['s0'])
                segment1_dict = name_dict.setdefault('segment_1',{}) \
                    .setdefault(str(group['segment_1']), {})
                segment1_dict['s1'] = str(group['s1'])
                segment1_dict.setdefault('segment_2', {}) \
                    .setdefault( str(group['segment_2']), {}) \
                    .setdefault('s2', str(group['s2']))

        return ret_dict
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
from genie.libs.parser.utils.common import Common

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


class ShowL2vpnXconnectSchema(MetaParser):
    """Schema for show l2vpn xconnect"""
    schema = {
      'groups': {
        Any(): {
          'name': {
            Any(): {
              'status': str,
              'segment1': {
                Any(): {
                  'status': str,
                  'segment2': {
                    Any(): {
                      'status': str,
                    },
                  },
                },
              },
            },
          },
        },
      },
    }


class ShowL2vpnXconnect(ShowL2vpnXconnectSchema):
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
                            '+(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                            '+(?P<segment_1>.*?) ' 
                            '+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                            '+(?P<segment_2>.*?) ' 
                            '+(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}) \
                    .setdefault(str(group['group']), {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = group_dict.setdefault('name', {}) \
                    .setdefault(str(group['name']), {})
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment1_dict.setdefault('segment2', {}) \
                    .setdefault( str(group['segment_2']), {}) \
                    .setdefault('status', str(group['status_seg2']))

        return ret_dict
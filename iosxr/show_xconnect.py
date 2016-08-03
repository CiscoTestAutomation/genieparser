''' show_xconnect.py

show xsconnect parser class

'''
from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any
from xbu_shared.parser.iosxr import IosxrCaasMetaParser

"""
    TODO: bpetrovi - Aug 2, 2016 
        # XR command: "show l2vpn xconnect group xc1g"
        # XR command: "show l2vpn xconnect interface <intf>"
        # Yang section for all parsers
        # XML section for all parsers

"""


class ShowL2VpnXconnectSummary(IosxrCaasMetaParser):
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
                                     exec='show l2vpn xconnect summary')
        return tcl.cast_any(result[1])


class ShowL2VpnXconnectBrief(MetaParser):
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
                                     exec='show l2vpn xconnect brief')
        return tcl.cast_any(result[1])



class ShowL2VpnXconnectDetail(MetaParser):
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
                                     exec='show l2vpn xconnect detail')
        return tcl.cast_any(result[1])


class ShowL2VpnXconnectMp2mpDetail(MetaParser):
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
                                     exec='show l2vpn xconnect mp2mp detail')
        return tcl.cast_any(result[1])



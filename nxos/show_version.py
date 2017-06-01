''' showversion.py

Example parser class

'''
import xmltodict
from ats import tcl
from metaparser import MetaParser
from metaparser.util.schemaengine import Any
try:
    import iptools
    from cnetconf import testmodel
except ImportError:
    pass


class ShowVersion(MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).
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
    
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show version')
        
        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle, 
                                      exec='show version | xml')
        result = tcl.cast_any(output[1])

        # transform the parser output to compliance with CLI version
        result.update({'cmp':{'module':{'*':{'bios_compile_time':'',
                                             'bios_version':'',
                                             'image_compile_time':'',
                                             'image_version':'',
                                             'status':'',}}}})
        return result

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        base = testmodel.BaseTest()
        base.connect_netconf()

        netconf_request = """
          <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <get>
              <filter>
                <native xmlns="">
                    <version>
                    </version>
                </native>
              </filter>
            </get>
          </rpc>
        """
        
        netconf_request += "\n##\n"
        ncout = base.netconf.send_config(netconf_request)
        
        #    ### XML output from yang
        #    <ns0:rpc-reply xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" 
        #    xmlns:ns1="urn:ios" message-id="101"><ns0:data><ns1:native>
        #    ....
        #    </ns1:native></ns0:data></ns0:rpc-reply>
        
        filtered_result = xmltodict.parse(ncout, 
                                          process_namespaces=True,
                                          namespaces={
                            'urn:ietf:params:xml:ns:netconf:base:1.0':None,
                            'urn:ios':None,'urn:iosxr':None,'urn:nxos':None,})
        partial_result = dict(
                            filtered_result['rpc-reply']['data'].get('native'))
        # to satisfy the schema, need to complete the dict by merging cli output
        result = self.cli()
        result.update(partial_result)
        return result

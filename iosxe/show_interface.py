''' show_interface.py

Example parser class

'''
import xmltodict
from ats import tcl
from metaparser import MetaParser
from metaparser.util import merge_dict, keynames_convert
from metaparser.util.schemaengine import Any, Optional
from cnetconf import testmodel
from collections import defaultdict
import iptools
import os
from ats.log.utils import banner
import pprint

import logging
logger = logging.getLogger(__name__)


class ShowInterfaces(MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and 
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output 
    # (nested dict) that has the same data structure across all supported 
    # parsing mechanisms (cli(), yang(), xml()).

    schema = {'intf': {Any(): {'admin_state': str,
                               Optional('ip_address'): str,
                               Any(): str,
                              }
                      }
              }

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle, 
                                     exec='show interfaces')

        out = keynames_convert(tcl.cast_any(result[1]), 
                               [('interfaces','intf'), ])
        for key in out['intf']:
            out['intf'][key]['encap'] = out['intf'][key].pop('encapsulation')
        return out

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''

        base = testmodel.BaseTest()
        logger.info(banner('Connecting Netconf Server {ip} {port} ...'.format(
                ip = os.environ['YTOOL_NETCONF_HOST'], 
                port = os.environ['YTOOL_NETCONF_PORT'])))
        base.connect_netconf()

        netconf_request = """
            <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
                <get> 
                    <filter>
                        <native xmlns="urn:ios"><interface></interface></native>
                    </filter>
                </get>
            </rpc>"""

        logger.info('NETCONF REQUEST: %s' % netconf_request)
        
        # netconf_request += "\n##\n"
        ncout = base.netconf.send_config(netconf_request)

        logger.info('NETCONF RETURN: %s' % ncout)

        filtered_result = xmltodict.parse(ncout, process_namespaces=True,
            namespaces={'urn:ietf:params:xml:ns:netconf:base:1.0':None,
                        'urn:ios':None,'urn:iosxr':None,'urn:nxos':None,})
        partial_result = dict(
                            filtered_result['rpc-reply']['data'].get('native'))
        logger.info('NETCONF DICT: %s' % pprint.pformat(partial_result))

        # to satisfy the schema, we need to rerange thestructure for yang output
        recursivedict = lambda: defaultdict(recursivedict)
        transfered_dict = recursivedict()
        
        for intf in partial_result['interface']:
            if type(partial_result['interface'][intf]) is list:
                for item in partial_result['interface'][intf]:
                    ip = item['ip']['address']['primary']['address'] \
                        if 'address' in item['ip'] else ''
                    mask = item['ip']['address']['primary']['mask'] \
                        if 'address' in item['ip'] else ''
                    ip_mask = ip + \
                              '/' + \
                              str(iptools.ipv4.netmask2prefix(mask)) \
                              if ip and mask else ''
                    admin_state = 'administratively down' \
                        if 'shutdown' in item else 'up'
                    interface = (intf+item['name']).lower()
                    transfered_dict['intf'][interface]['ip_address'] = \
                        ip_mask
                    transfered_dict['intf'][interface]['admin_state'] = \
                        admin_state
            else:
                item = partial_result['interface'][intf]
                ip = item['ip']['address']['primary']['address'] \
                    if 'address' in item['ip'] else ''
                mask = item['ip']['address']['primary']['mask'] \
                    if 'address' in item['ip'] else ''
                ip_mask = ip + '/' + str(iptools.ipv4.netmask2prefix(mask)) \
                    if ip and mask else ''
                admin_state = 'administratively down' \
                    if 'shutdown' in item else 'up'
                interface  = (intf + 
                              partial_result['interface'][intf]['name']).lower()
                transfered_dict['intf'][interface]\
                               ['ip_address'] = ip_mask
                transfered_dict['intf'][interface]\
                               ['admin_state'] = admin_state

        # to satisfy the schema, need to complete the dict by merging cli output
        result = self.cli()
        result = merge_dict(result, transfered_dict, update=True)
        return result

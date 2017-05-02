''' show_interface.py

Example parser class

'''

from cnetconf import testmodel
from collections import defaultdict
import iptools
import logging
import os
import pprint
import xmltodict

from ats.log.utils import banner

from metaparser import MetaParser
from metaparser.util import merge_dict
from metaparser.util.schemaengine import Any

from parser.base import *

logger = logging.getLogger()


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

    schema = {
        'intf': {
            Any(): {
                'admin_state': str,
                'bw': str,
                'encap': str,
                'line_protocol': str,
                'mtu': str,
                Any(): str,
            },
        },
    }

    def cli(self):
        '''parsing mechanism: cli
        '''

        cmd = 'show interfaces'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl

    def yang(self):
        '''parsing mechanism: yang
        '''

        base = testmodel.BaseTest()

        logger.info(banner('Connecting Netconf Server {ip} {port} ...'.format(
                ip=os.environ['YTOOL_NETCONF_HOST'],
                port=os.environ['YTOOL_NETCONF_PORT'])))

        base.logfile = logger

        base.connect_netconf()

        netconf_request = """
            <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <get>
                    <filter>
                        <interface-properties xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper"/>
                    </filter>
                </get>
            </rpc>"""

        logger.info('NETCONF REQUEST: %s' % netconf_request)
        ncout = base.netconf.send_config(netconf_request)

        logger.info('NETCONF RETURN: %s' % ncout)

        filtered_result = xmltodict.parse(
            ncout,
            process_namespaces=True,
            namespaces={
                'urn:ietf:params:xml:ns:netconf:base:1.0': None,
                'http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper': None,
                'urn:ios': None,
                'urn:iosxr': None,
                'urn:nxos': None,
            })
        partial_result = dict(
            filtered_result['rpc-reply']['data']['interface-properties']
            ['data-nodes']['data-node']['locationviews']['locationview'].
            get('interfaces'))

        logger.info('NETCONF DICT: %s' % pprint.pformat(partial_result))

        # to satisfy the schema, we need to rerange thestructure for yang output
        recursivedict = lambda: defaultdict(recursivedict)
        transfered_dict = recursivedict()

        for intf in partial_result['interface']:
            name = intf['interface-name'].lower()
            admin_state = intf['actual-state']
            line_protocol = intf['actual-line-state']
            encap = intf['encapsulation']
            bw = intf['bandwidth']
            mtu = intf['mtu']
            transfered_dict['intf'][name]['admin_state'] = admin_state
            transfered_dict['intf'][name]['line_protocol'] = line_protocol
            transfered_dict['intf'][name]['encap'] = encap
            transfered_dict['intf'][name]['bw'] = bw
            transfered_dict['intf'][name]['mtu'] = mtu

        # to satisfy the schema, need to complete the dict by merging cli output
        result = self.cli()
        result = merge_dict(result, transfered_dict, update=True)
        return result

########### future to - switch to a better yang schema #########################

#<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#  <get>
#    <filter>
#      <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-pfi-im-cmd-oper">
#        <interface-xr/>
#      </interfaces>
#    </filter>
#  </get>
#</rpc>

# vim: ft=python ts=8 sw=4 et

''' show_interface.py

Example parser class

'''

import os
import logging
import pprint
import re
import unittest
from collections import defaultdict

from ats import tcl
from ats.tcl.keyedlist import KeyedList
from ats.log.utils import banner
import xmltodict
try:
    import iptools
    from cnetconf import testmodel
except ImportError:
    pass

import parsergen

from metaparser import MetaParser
from metaparser.util import merge_dict, keynames_convert
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

logger = logging.getLogger(__name__)


def regexp(expression):
    def match(value):
        if re.match(expression, value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                            % (value, expression))
    return match


class ShowInterfaces(MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
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

# parser using parsergen
# ----------------------
class ShowIpInterfaceBriefSchema(MetaParser):
    schema = {'interface':
                {Any():
                    {Optional('vlan_id'):
                        {Optional(Any()):
                                {'ip_address': str,
                                 Optional('interface_is_ok'): str,
                                 Optional('method'): str,
                                 Optional('status'): str,
                                 Optional('protocol'): str}
                        },
                     Optional('ip_address'): str,
                     Optional('interface_is_ok'): str,
                     Optional('method'): str,
                     Optional('status'): str,
                     Optional('protocol'): str}
                },
            }

class ShowIpInterfaceBrief(ShowIpInterfaceBriefSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief'.format()

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        res = parsergen.oper_fill_tabular(device=self.device,
                                          show_command=self.cmd,
                                          header_fields=
                                           [ "Interface",
                                             "IP-Address",
                                             "OK\?",
                                             "Method",
                                             "Status",
                                             "Protocol" ],
                                          label_fields=
                                           [ "Interface",
                                             "IP-Address",
                                             "OK?",
                                             "Method",
                                             "Status",
                                             "Protocol" ],
                                          index=[0])
        return (res)

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        pass

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output

class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief | include Vlan'.format()

    def cli(self):
        super(ShowIpInterfaceBriefPipeVlan, self).cli()

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''

        ret = {}
        cmd = '''<native><interface><Vlan/></interface></native>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for native in data:
                for interface in native:
                    vlan_id = None
                    interface_name = None
                    ip_address = None
                    ip_mask = None
                    for vlan in interface:
                        # Remove the namespace
                        text = vlan.tag[vlan.tag.find('}')+1:]
                        #ydk.models.ned_edison.ned.Native.Interface.Vlan.name
                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.name
                        if text == 'name':
                            vlan_id = vlan.text
                            interface_name = 'Vlan' + str(vlan_id)
                            continue
                        if text == 'ip':
                            for ip in vlan:
                                text = ip.tag[ip.tag.find('}')+1:]
                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address
                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address
                                if text == 'address':
                                    for address in ip:
                                        text = address.tag[address.tag.find('}')+1:]
                                        #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary
                                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary
                                        if text == 'primary':
                                            for primary in address:
                                                # Remove the namespace
                                                text = primary.tag[primary.tag.find('}')+1:]
                                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary.address
                                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary.address
                                                if text == 'address':
                                                    ip_address = primary.text
                                                    continue
                                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary.mask
                                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary.mask
                                                if text == 'mask':
                                                    ip_mask = primary.text
                                                    continue
                    # Let's build it now
                    if 'interface' not in ret:
                        ret['interface'] = {}
                    if interface_name is not None:
                        ret['interface'][interface_name] = {}
                        if vlan_id is not None:
                            ret['interface'][interface_name]['vlan_id'] = {}
                            ret['interface'][interface_name]['vlan_id'][vlan_id] = {}
                            if ip_address is not None:
                                ret['interface'][interface_name]['vlan_id'][vlan_id]['ip_address'] = ip_address
                            else:
                                ret['interface'][interface_name]['vlan_id'][vlan_id]['ip_address'] = 'unassigned'

        return ret

    def yang_cli(self):
        super(ShowIpInterfaceBriefPipeVlan, self).yang_cli()


# switchport administrative mode is what's configured on the switch port while operational mode is what is actually functioning at the moment.
class ShowInterfacesSwitchportSchema(MetaParser):
    schema = {'interface':
                {Any():
                    {Optional('switchport_mode'):
                        {Optional(Any()):
                            {Optional('vlan_id'):
                                {Optional(Any()):
                                    {Optional('admin_trunking_encapsulation'): str,
                                     Optional('allowed_vlans'): str}
                                },
                            }
                        },
                    },
                },
            }

class ShowInterfacesSwitchport(ShowInterfacesSwitchportSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show interfaces switchport'.format()
        out = self.device.execute(cmd)
        intf_dict = {}
        trunk_section = False
        access_section = False
        trunk_encapsulation = ''
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Name:\s*(?P<interface_name>[a-zA-Z0-9\/]+)$')
            m = p1.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                if 'interface' not in intf_dict:
                    intf_dict['interface'] = {}
                if interface_name not in intf_dict['interface']:
                    intf_dict['interface'][interface_name] = {}
                continue

            p2 = re.compile(r'^\s*Administrative Mode:\s*(?P<admin_mode>[a-z\s*]+)$')
            m = p2.match(line)
            if m:
                admin_mode = m.groupdict()['admin_mode']
                if any(word in admin_mode for word in ['trunk', 'access']):
                    if 'switchport_mode' not in intf_dict['interface']:
                        intf_dict['interface'][interface_name]['switchport_mode'] = {}
                    if admin_mode not in intf_dict['interface'][interface_name]['switchport_mode']:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode] = {}

                if 'trunk' in admin_mode:
                    trunk_section = True
                    access_section = False
                elif 'access' in admin_mode:
                    access_section = True
                    trunk_section = False
                continue

            p3 = re.compile(r'^\s*Trunking Native Mode VLAN:\s*(?P<trunking_native_vlan>[0-9]+)( \([a-zA-Z]+\))*$')
            m = p3.match(line)
            if m:
                vlan_id = m.groupdict()['trunking_native_vlan']
                if any(word in admin_mode for word in ['trunk', 'access']):
                    if 'vlan_id' not in intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'] = {}
                    if vlan_id not in intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id']:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'][vlan_id] = {}
                    if trunk_encapsulation:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]\
                            ['vlan_id'][vlan_id]['admin_trunking_encapsulation'] = trunk_encapsulation
                continue

            p4 = re.compile(r'^\s*Access Mode VLAN:\s*(?P<access_mode_vlan_id>[a-z0-9]+)( \([a-zA-Z]+\))*$')
            m = p4.match(line)
            if m:
                vlan_id = m.groupdict()['access_mode_vlan_id']
                if any(word in admin_mode for word in ['trunk', 'access']):
                    if 'vlan_id' not in intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'] = {}
                    if vlan_id not in intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id']:
                        intf_dict['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'][vlan_id] = {}
                continue

            if trunk_section:
                p5 = re.compile(r'^\s*Administrative Trunking Encapsulation:\s*(?P<admin_trunking_encapsulation>[a-z0-9]+)$')
                m = p5.match(line)
                if m:
                    trunk_encapsulation = m.groupdict()['admin_trunking_encapsulation']
                    continue

        return intf_dict

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        ret = {}
        cmd = '''<native><interface><GigabitEthernet/></interface></native>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for native in data:
                for interface in native:
                    gig_number = None
                    interface_name = None
                    admin_mode = None
                    vlan_id = None
                    allowed_vlans = None
                    for gigabitethernet in interface:
                        # Remove the namespace
                        text = gigabitethernet.tag[gigabitethernet.tag.find('}')+1:]
                        if text == 'name':
                            gig_number = gigabitethernet.text
                            interface_name = 'Gigabitethernet' + str(gig_number)
                            continue
                        if text == 'switchport':
                            for switchport in gigabitethernet:
                                # admin_mode = None
                                text = switchport.tag[switchport.tag.find('}')+1:]
                                #ydk.models.ned_edison.ned.Native.Interface.Gigabitethernet.Switchport.Trunk
                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Gigabitethernet.Switchport.Trunk
                                if text == 'trunk':
                                    admin_mode = 'trunk'
                                    for vlan in switchport:
                                        # vlan_id = None
                                        text = vlan.tag[vlan.tag.find('}')+1:]
                                        #ydk.models.ned_edison.ned.Native.Interface.Gigabitethernet.Switchport.Trunk.Native_
                                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Gigabitethernet.Switchport.Trunk.Native_
                                        if text == 'native':
                                            for item in vlan:
                                                text = item.tag[item.tag.find('}')+1:]
                                                vlan_id = item.text
                                        #ydk.models.ned_edison.ned.Native.Interface.Gigabitethernet.Switchport.Trunk.Allowed
                                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Gigabitethernet.Switchport.Trunk.Allowed
                                        # allowed_vlans = None
                                        if text == 'allowed':
                                            #ydk.models.ned_edison.ned.Native.Interface.Gigabitethernet.Switchport.Trunk.Allowed.Vlan
                                            #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Gigabitethernet.Switchport.Trunk.Allowed.Vlan
                                            for item in vlan:
                                                # Remove the namespace
                                                text = item.tag[item.tag.find('}')+1:]
                                                if text == 'vlan':
                                                    for stuff in item:
                                                        text = stuff.tag[stuff.tag.find('}')+1:]
                                                        if text == 'vlans':
                                                            allowed_vlans = stuff.text
                                                        continue
                                #ydk.models.ned_edison.ned.Native.Interface.Gigabitethernet.Switchport.Access
                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Gigabitethernet.Switchport.Access
                                if text == 'access':
                                    admin_mode = 'access'
                                    for vlan in switchport:
                                        vlan_id = None
                                        for item in vlan:
                                            text = item.tag[item.tag.find('}')+1:]
                                            vlan_id = item.text
                                            continue
                    # Let's build it now
                    if 'interface' not in ret:
                        ret['interface'] = {}
                    if interface_name is not None:
                        ret['interface'][interface_name] = {}
                        if admin_mode is not None:
                            if 'switchport_mode' not in ret['interface'][interface_name]:
                                ret['interface'][interface_name]['switchport_mode'] = {}
                            ret['interface'][interface_name]['switchport_mode'][admin_mode] = {}
                            if vlan_id is not None:
                                if 'vlan_id' not in ret['interface'][interface_name]['switchport_mode'][admin_mode]:
                                    ret['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'] = {}
                                ret['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'][vlan_id] = {}
                                if allowed_vlans is not None:
                                    ret['interface'][interface_name]['switchport_mode'][admin_mode]['vlan_id'][vlan_id]['allowed_vlans'] = allowed_vlans

        return ret

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output
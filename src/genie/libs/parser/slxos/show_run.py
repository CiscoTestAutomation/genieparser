"""
Author:
    Fabio Pessoa Nunes (https://www.linkedin.com/in/fpessoanunes/)

show_run.py

SLXOS parsers for the following show commands:
    * show run bridge-domain
    * show run bridge-domain {bd_id} {bd_type}
    * show run mac access-list
    * show run mac access-list {acl_type}
    * show run mac access-list {acl_type} {acl_name}

Schemas based on SLX's YANG models
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#   * 'show run bridge-domain'
# ==================================================
class ShowRunBridgeDomainSchema(MetaParser):
    """Schema for show run bridge-domain"""

    schema = {
        'bridge_domains': {
            Any(): {
                'bridge_domain_id': int,
                'bridge_domain_type': str,
                Optional('vc_id_num'): int,
                Optional('description'): str,
                Optional('peers'): {
                    Any(): {
                        'peer_ip': str,
                        Optional('load_balance'): bool,
                        Optional('cos'): int,
                        Optional('lsps'): {
                            Any(): {
                                'lsp_name': str
                            }
                        },
                        Optional('flow_label'): bool,
                        Optional('control_word'): bool
                    }
                },
                Optional('statistics'): bool,
                Optional('router_interface'): {
                    'router_ve': int,
                    Optional('disallow_oar_ac'): bool
                },
                Optional('logical_interfaces'): {
                    'ethernet': {
                        Any(): {
                            'lif_bind_id': str
                        }
                    },
                    'port_channel': {
                        Any(): {
                            'pc_lif_bind_id': str
                        }
                    }
                },
                Optional('pw_profile_name'): str,
                Optional('bpdu_drop_enable'): bool,
                Optional('local_switching'): bool,
                Optional('mac_address'): {
                    Optional('withdrawal'): bool
                },
                Optional('suppress_arp'): {
                    Optional('suppress_arp_enable'): bool
                },
                Optional('suppress_nd'): {
                    Optional('suppress_nd_enable'): bool
                }
            }
        }
    }


# ===================================
# Parser for:
#   * 'show run bridge-domain'
#   * 'show run bridge-domain {bd_id} {bd_type}'
# ===================================
class ShowRunBridgeDomain(ShowRunBridgeDomainSchema):
    ''' Parser for "show run bridge-domain"	'''

    cli_command = ['show run bridge-domain',
                   'show run bridge-domain {bd_id} {bd_type}']

    def cli(self, bd_id=None, bd_type=None, output=None):

        if output is None:
            if bd_id:
                cmd = self.cli_command[1].format(bd_id=bd_id, bd_type=bd_type)
            else:
                cmd = self.cli_command[0]
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        res_dict = {}

        # bridge-domain 20 p2mp
        p1 = re.compile(
            r'^bridge-domain (?P<bd_id>\d+)\s(?P<bd_type>p2mp|p2p)$')
        # vc-id 20
        p2 = re.compile(
            r'^vc-id (?P<vc_id>\d+)$')
        # peer 1.1.1.1 lsp abc def ed
        # peer 3.3.3.3 lsp 1 abc cos
        # peer 4.4.4.4 load-balance cos 4 flow-label control-word lsp abc ds
        p3 = re.compile(
            r'^peer\s(?P<peer_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(\s((?P<load_balance>load-balance)|cos (?P<cos>\d)|(?P<flow_label>flow-label)|(?P<control_word>control-word)|lsp\s(?P<lsp>(\w+\s?)+)))+$')
        # description client1
        p4 = re.compile(
            r'^description\s(?P<description>\w+)$')
        # logical-interface ethernet 0/30.2
        # logical-interface port-channel 100.1
        p5 = re.compile(
            r'^logical-interface\s(?P<interface_type>ethernet|port-channel)\s(?P<interface>\S+)$')
        
        # router-interface Ve 123
        p6 = re.compile(
            r'^router-interface\sVe\s(?P<ve_id>\d+)$')

        # pw-profile default
        p7 = re.compile(
            r'^pw-profile\s(?P<pw_profile>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # bridge-domain 20 p2mp
            m = p1.match(line)
            if m:
                group = m.groupdict()
                bridge_domains = res_dict.setdefault('bridge_domains', {})
                bridge_domain = bridge_domains.setdefault(
                    int(group["bd_id"]),
                    {"bridge_domain_id": int(group["bd_id"]), "bridge_domain_type": group["bd_type"]},
                )
                continue

            # vc-id 20
            m = p2.match(line)
            if m:
                bridge_domain['vc_id_num'] = int(m.groupdict()['vc_id'])
                continue

            # peer 1.1.1.1 lsp abc def ed
            # peer 3.3.3.3 lsp 1 abc cos
            # peer 4.4.4.4 load-balance cos 4 flow-label control-word lsp abc ds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                peers = bridge_domain.setdefault('peers', {})
                peer = peers.setdefault(group['peer_ip'], {})
                peer['peer_ip'] = group['peer_ip']
                if group['load_balance'] is not None:
                    peer['load_balance'] = True
                if group['cos'] is not None:
                    peer['cos'] = int(group['cos'])
                if group['lsp'] is not None:
                    peer['lsps'] = {}
                    for lsp in group['lsp'].strip().split(' '):
                        peer['lsps'][lsp] = {'lsp_name': lsp}
                if group['flow_label'] is not None:
                    peer['flow_label'] = True
                if group['control_word'] is not None:
                    peer['control_word'] = True
                continue

            # description test
            m = p4.match(line)
            if m:
                bridge_domain['description'] = m.groupdict()['description']
                continue

            # statistics
            m = re.compile('^statistics$').match(line)
            if m:
                bridge_domain['statistics'] = True
                continue

            # logical-interface ethernet 0/30.2
            # logical-interface port-channel 100.1 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                logical_interfaces = bridge_domain.setdefault('logical_interfaces', {'ethernet': {}, 'port_channel': {}})
                if group['interface_type'] == 'ethernet':
                    ethernet = logical_interfaces.setdefault('ethernet', {})
                    ethernet[group['interface']] = {'lif_bind_id': 'Ethernet ' + group['interface']}
                elif group['interface_type'] == 'port-channel':
                    port_channel = logical_interfaces.setdefault('port_channel', {})
                    port_channel[group['interface']] = {'pc_lif_bind_id': 'Port-channel ' + group['interface']}

            # router-interface Ve 123
            m = p6.match(line)
            if m:
                bridge_domain['router_interface'] = {'router_ve': int(m.groupdict()['ve_id'])}
                continue

            # disallow-oar-ac
            m = re.compile('^disallow-oar-ac$').match(line)
            if m:
                bridge_domain['router_interface']['disallow_oar_ac'] = True
                continue

            # local-switching
            m = re.compile('^local-switching$').match(line)
            if m:
                bridge_domain['local_switching'] = True
                continue

            # pw-profile default
            m = p7.match(line)
            if m:
                group = m.groupdict()
                bridge_domain['pw_profile_name'] = group['pw_profile']
                continue

            # bpdu-drop-enable
            m = re.compile('^bpdu-drop-enable$').match(line)
            if m:
                bridge_domain['bpdu_drop_enable'] = True
                continue

            # mac-address withdrawal
            m = re.compile('^mac-address withdrawal$').match(line)
            if m:
                bridge_domain['mac_address'] = {'withdrawal': True}
                continue

            # suppress-nd
            m = re.compile('^suppress-nd$').match(line)
            if m:
                bridge_domain['suppress_nd'] = {'suppress_nd_enable': True}
                continue

            # suppress-arp
            m = re.compile('^suppress-arp$').match(line)
            if m:
                bridge_domain['suppress_arp'] = {'suppress_arp_enable': True}
                continue
        return res_dict

    def yang(self, bd_id=None, bd_type=None):
        rpc_request_bd = """
        <filter>
            <bridge-domain xmlns="urn:brocade.com:mgmt:brocade-bridge-domain">
                {bd_id_template}
            </bridge-domain>
        </filter>
            """
        bd_id_template = """
                <bridge-domain-id>{bd_id}</bridge-domain-id>
                <bridge-domain-type>{bd_type}</bridge-domain-type>
        """

        if bd_id:
            rpc_request = rpc_request_bd.format(bd_id_template=bd_id_template.format(bd_id=bd_id, bd_type=bd_type))
        else:
            rpc_request = rpc_request_bd.format(bd_id_template='')

        res_dict = {}
        bridge_domains = res_dict.setdefault('bridge_domains', {})

        output = self.device.get(rpc_request)

        for bd in output.data:
            if bd.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}bridge-domain':
                for iter in bd:
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}bridge-domain-id':
                        bridge_domain = bridge_domains.setdefault(int(iter.text), {})
                        bridge_domain['bridge_domain_id'] = int(iter.text)
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}bridge-domain-type':
                        bridge_domain['bridge_domain_type'] = iter.text
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}vc-id-num':
                        bridge_domain['vc_id_num'] = int(iter.text)
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}description':
                        bridge_domain['description'] = iter.text
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}peer':
                        if 'peers' in bridge_domain.keys():
                            peers = bridge_domain['peers']
                        else:
                            peers = bridge_domain.setdefault('peers', {})
                        for peer_element in iter:
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}peer-ip':
                                peer = peers.setdefault(peer_element.text, {})
                                peer['peer_ip'] = peer_element.text
                                continue
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}load-balance':
                                peer['load_balance'] = True
                                continue
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}cos':
                                peer['cos'] = int(peer_element.text)
                                continue
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}lsp':
                                if 'lsps' in peer.keys():
                                    lsps = peer['lsps']
                                else:
                                    lsps = peer.setdefault('lsps', {})
                                lsps[peer_element.text] = {}
                                lsps[peer_element.text]['lsp_name'] = peer_element.text
                                continue
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}flow-label':
                                peer['flow_label'] = True
                                continue
                            if peer_element.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}control-word':
                                peer['control_word'] = True
                                continue
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}statistics':
                        bridge_domain['statistics'] = True
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}router-interface':
                        bridge_domain['router_interface'] = {}
                        for rt_interface_elem in iter:
                            if rt_interface_elem.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}router-ve':
                                bridge_domain['router_interface']['router_ve'] = int(rt_interface_elem.text)
                                continue
                            if rt_interface_elem.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}disallow-oar-ac':
                                bridge_domain['router_interface']['disallow_oar_ac'] = True
                                continue
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}logical-interface':
                        logical_interfaces = bridge_domain.setdefault('logical_interfaces', {})
                        ethernet = logical_interfaces.setdefault('ethernet', {})
                        port_channel = logical_interfaces.setdefault('port_channel', {})
                        for logical_type in iter:
                            for logical in logical_type:
                                if logical_type.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}ethernet':
                                    ethernet[logical.text] = {}
                                    ethernet[logical.text]['lif_bind_id'] = 'Ethernet ' + logical.text
                                elif logical_type.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}port-channel':
                                    port_channel[logical.text] = {}
                                    port_channel[logical.text]['pc_lif_bind_id'] = 'Port-channel ' + logical.text
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}pw-profile-name':
                        bridge_domain['pw_profile_name'] = iter.text
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}bpdu-drop-enable':
                        bridge_domain['bpdu_drop_enable'] = True
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}local-switching':
                        bridge_domain['local_switching'] = True
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}mac-address':
                        for mac in iter:
                            if mac.tag == '{urn:brocade.com:mgmt:brocade-bridge-domain}withdrawal':
                                bridge_domain.setdefault('mac_address', {'withdrawal': True})
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-arp}suppress-arp':
                        for x in iter:
                            if x.tag == '{urn:brocade.com:mgmt:brocade-arp}suppress-arp-enable':
                                bridge_domain.setdefault('suppress_arp', {'suppress_arp_enable': True})
                        continue
                    if iter.tag == '{urn:brocade.com:mgmt:brocade-ipv6-nd-ra}suppress-nd':
                        for x in iter:
                            if x.tag == '{urn:brocade.com:mgmt:brocade-ipv6-nd-ra}suppress-nd-enable':
                                bridge_domain.setdefault('suppress_nd', {'suppress_nd_enable': True})
                        continue
        return res_dict


# =================================================
# Schema for:
#   * 'show run mac access-list'
# ==================================================
class ShowRunMacAccessListSchema(MetaParser):
    """Schema for show run mac access-list"""

    schema = {
        'mac': {
            'access-list': {
                Optional('standard'): {
                    Any(): {
                        'name': str,
                        Optional('seqs'): {
                            Any(): {
                                'seq-id': int,
                                'action': str,
                                'source': str,
                                Optional('srchost'): str,
                                Optional('src-mac-addr-mask'): str,
                                Optional('count'): bool,
                                Optional('log'): bool,
                                Optional('copy-sflow'): bool
                            }
                        }
                    }
                },
                Optional('extended'): {
                    Any(): {
                        'name': str,
                        Optional('seqs'): {
                            Any(): {
                                'seq-id': int,
                                'action': str,
                                'source': str,
                                Optional('srchost'): str,
                                Optional('src-mac-addr-mask'): str,
                                'dst': str,
                                Optional('dsthost'): str,
                                Optional('dst-mac-addr-mask'): str,
                                Optional('vlan-tag-format'): str,
                                Optional('vlan'): str,
                                Optional('vlan-id-mask'): str,
                                Optional('outer-vlan'): str,
                                Optional('outer-vlan-id-mask'): str,
                                Optional('inner-vlan'): str,
                                Optional('inner-vlan-id-mask'): str,
                                Optional('ethertype'): str,
                                Optional('arp-guard'): bool,
                                Optional('pcp'): int,
                                Optional('pcp-force'): int,
                                Optional('drop-precedence-force'): int,
                                Optional('count'): bool,
                                Optional('log'): bool,
                                Optional('mirror'): bool,
                                Optional('copy-sflow'): bool,
                                Optional('known-unicast-only'): bool,
                                Optional('unknown-unicast-only'): bool
                            }
                        }
                    }
                }
            }
        }
    }


# ===================================
# Parser for:
#   * 'show run mac access-list'
#   * 'show run mac access-list {acl_type}'
#   * 'show run mac access-list {acl_type} {acl_name}'
# ===================================
class ShowRunMacAccessList(ShowRunMacAccessListSchema):
    ''' Parser for 
        "show run mac access-list"
        "show run mac access-list {acl_type}"
        "show run mac access-list {acl_type} {acl_name}"
    '''

    cli_command = [
        'show run mac access-list',
        'show run mac access-list {acl_type}',
        'show run mac access-list {acl_type} {acl_name}'
    ]

    def cli(self, acl_type=None, acl_name=None, output=None):

        if output is None:
            if acl_type:
                if acl_name:
                    cmd = self.cli_command[2].format(acl_type=acl_type, acl_name=acl_name)
                else:
                    cmd = self.cli_command[1].format(acl_type=acl_type)
            else:
                cmd = self.cli_command[0]

            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        res_dict = {}

        # mac access-list extended test3
        # mac access-list standard test-1
        p1 = re.compile(
            r'^mac access-list (?P<acl_type>\w+) (?P<acl_name>\S+)$')

        # seq 10 permit host aaaa.aaaa.aaaa count
        # seq 20 deny aaaa.aaaa.aaa0 ffff.ffff.fff0 log
        # seq 30 hard-drop any copy-sflow
        # seq 103 permit host abcd.abcd.abcd any vlan-tag-format double-tagged outer-vlan 200 inner-vlan 1234 arp
        # seq 110 permit host abcd.abcd.abcd any vlan-tag-format single-tagged vlan 321 arp
        # seq 200 permit host abcd.abcd.abcd any vlan-tag-format single-tagged vlan 10 pcp 1 pcp-force 3 drop-precedence-force 2 count log mirror
        p2 = re.compile(
            r'^seq (?P<seq_id>\d+) (?P<action>permit|deny|hard-drop) '
            r'(?P<src>any|(host (([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}) (([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})))'
            r'(?P<dst> (any|(host (([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}) (([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}))))'
            r'?( vlan-tag-format (single-tagged vlan ((?P<vlan_tag_single>\d{1,4})( (?P<vlan_tag_single_mask>0x[a-fA-F0-9]{3}))?)|(double-tagged outer-vlan ((?P<vlan_tag_double_outer>\d{1,4})( (?P<vlan_tag_double_outer_mask>0x[a-fA-F0-9]{3}))?|any) inner-vlan ((?P<vlan_tag_double_inner>\d{1,4})( (?P<vlan_tag_double_inner_mask>0x[a-fA-F0-9]{3}))?|any))))'
            r'?( vlan (?P<vlan>\d{1,4}))?(?P<ethertype> (arp|ipv4|ipv6|\d{4,5}))'
            r'?(?P<flags>( log| copy-sflow| arp-guard| count| known-unicast-only| unknown-unicast-only| mirror| drop-precedence-force (?P<drop_precedence_force>\d)| pcp (?P<pcp>\d)| pcp-force (?P<pcp_force>\d))*)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                acls_dict = res_dict.setdefault('mac', {'access-list': {}})
                if group['acl_type'] == 'standard':
                    acl_group = acls_dict['access-list'].setdefault('standard', {})
                elif group['acl_type'] == 'extended':
                    acl_group = acls_dict['access-list'].setdefault('extended', {})
                acl = acl_group.setdefault(group['acl_name'], {})
                acl['name'] = group['acl_name']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                seqs = acl.setdefault('seqs', {})
                seq = seqs.setdefault(int(group['seq_id']), {})
                seq['seq-id'] = int(group['seq_id'])
                seq['action'] = group['action'].strip()

                src = group['src'].strip()
                if 'host' in src:
                    seq['source'] = 'host'
                    seq['srchost'] = src.strip('host ')
                elif 'any' in src:
                    seq['source'] = 'any'
                else:
                    seq['source'], seq['src-mac-addr-mask'] = src.split(' ')

                if group['dst'] is not None:
                    dst = group['dst'].strip()
                    if 'host' in dst:
                        seq['dst'] = 'host'
                        seq['dsthost'] = dst.strip('host ')
                    elif 'any' in dst:
                        seq['dst'] = 'any'
                    else:
                        seq['dst'], seq['dst-mac-addr-mask'] = dst.split(' ')

                if group['vlan'] is not None:
                    seq['vlan'] = group['vlan']
                    pass

                if group['vlan_tag_single'] is not None:
                    seq['vlan-tag-format'] = 'single-tagged'
                    seq['vlan'] = group['vlan_tag_single']
                    if group['vlan_tag_single_mask'] is not None:
                        seq['vlan-id-mask'] = group['vlan_tag_single_mask']
                if group['vlan_tag_double_outer'] is not None:
                    seq['vlan-tag-format'] = 'double-tagged'
                    seq['outer-vlan'] = group['vlan_tag_double_outer']
                    if group['vlan_tag_double_outer_mask'] is not None:
                        seq['outer-vlan-id-mask'] = group['vlan_tag_double_outer_mask']
                if group['vlan_tag_double_inner'] is not None:
                    seq['vlan-tag-format'] = 'double-tagged'
                    seq['inner-vlan'] = group['vlan_tag_double_inner']
                    if group['vlan_tag_double_inner_mask'] is not None:
                        seq['inner-vlan-id-mask'] = group['vlan_tag_double_inner_mask']

                if group['ethertype'] is not None:
                    seq['ethertype'] = group['ethertype'].strip()

                if group['flags'] is not None:
                    if 'log' in group['flags']:
                        seq['log'] = True
                    if 'copy-sflow' in group['flags']:
                        seq['copy-sflow'] = True
                    if 'arp-guard' in group['flags']:
                        seq['arp-guard'] = True
                    if 'mirror' in group['flags']:
                        seq['mirror'] = True
                    if 'count' in group['flags']:
                        seq['count'] = True
                    if ' known-unicast-only' in group['flags']:
                        seq['known-unicast-only'] = True
                    if 'unknown-unicast-only' in group['flags']:
                        seq['unknown-unicast-only'] = True
                    if group['drop_precedence_force'] is not None:
                        seq['drop-precedence-force'] = int(group['drop_precedence_force'])
                    if group['pcp_force'] is not None:
                        seq['pcp-force'] = int(group['pcp_force'])
                    if group['pcp'] is not None:
                        seq['pcp'] = int(group['pcp'])
                continue
        return res_dict

    def yang(self, acl_type=None, acl_name=None):
        rpc_request_mac_acl = """
            <filter>
            <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
                <access-list>{acl_type_template}</access-list>
            </mac>
            </filter>
        """
        acl_type_template = """
                <{acl_type}>{acl_name_template}</{acl_type}>
        """
        acl_name_template = """
                    <name>{acl_name}</name>
        """

        if acl_type:
            if acl_name:
                rpc_request = rpc_request_mac_acl.format(
                    acl_type_template=acl_type_template.format(
                        acl_type=acl_type,
                        acl_name_template=acl_name_template.format(acl_name=acl_name),
                    )
                )
            else:
                rpc_request = rpc_request_mac_acl.format(
                    acl_type_template=acl_type_template.format(
                        acl_type=acl_type, acl_name_template=""
                    )
                )
        else:
            rpc_request = rpc_request_mac_acl.format(acl_type_template='')

        res_dict = {}
        acls_dict = res_dict.setdefault('mac', {'access-list': {}})

        output = self.device.get(rpc_request)

        for mac in output.data:
            for acls in mac:
                for acl in acls:
                    if acl.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}standard':
                        standard_dict = acls_dict['access-list'].setdefault('standard', {})
                        for acl_elem in acl:
                            if acl_elem.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}name':
                                acl_dict = standard_dict.setdefault(acl_elem.text, {'name': acl_elem.text})
                            elif acl_elem.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}hide-mac-acl-std':
                                for seq in acl_elem:
                                    seqs_dict = acl_dict.setdefault('seqs', {})
                                    for seq_element in seq:
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}seq-id':
                                            seq_dict = seqs_dict.setdefault(int(seq_element.text), {'seq-id': int(seq_element.text)})
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}action':
                                            seq_dict['action'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}source':
                                            seq_dict['source'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}srchost':
                                            seq_dict['srchost'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}src-mac-addr-mask':
                                            seq_dict['src-mac-addr-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}count':
                                            seq_dict['count'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}log':
                                            seq_dict['log'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}copy-sflow':
                                            seq_dict['copy-sflow'] = True
                                            continue
                    elif acl.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}extended':
                        extended_dict = acls_dict['access-list'].setdefault('extended', {})
                        for acl_elem in acl:
                            if acl_elem.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}name':
                                acl_dict = extended_dict.setdefault(acl_elem.text, {'name': acl_elem.text})
                            elif acl_elem.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}hide-mac-acl-ext':
                                for seq in acl_elem:
                                    seqs_dict = acl_dict.setdefault('seqs', {})
                                    for seq_element in seq:
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}seq-id':
                                            seq_dict = seqs_dict.setdefault(int(seq_element.text), {'seq-id': int(seq_element.text)})
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}action':
                                            seq_dict['action'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}source':
                                            seq_dict['source'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}srchost':
                                            seq_dict['srchost'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}src-mac-addr-mask':
                                            seq_dict['src-mac-addr-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}dst':
                                            seq_dict['dst'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}dsthost':
                                            seq_dict['dsthost'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}dst-mac-addr-mask':
                                            seq_dict['dst-mac-addr-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}vlan-tag-format':
                                            seq_dict['vlan-tag-format'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}vlan':
                                            seq_dict['vlan'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}vlan-id-mask':
                                            seq_dict['vlan-id-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}outer-vlan':
                                            seq_dict['outer-vlan'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}outer-vlan-id-mask':
                                            seq_dict['outer-vlan-id-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}inner-vlan':
                                            seq_dict['inner-vlan'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}inner-vlan-id-mask':
                                            seq_dict['inner-vlan-id-mask'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}ethertype':
                                            seq_dict['ethertype'] = seq_element.text
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}arp-guard':
                                            seq_dict['arp-guard'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}pcp':
                                            seq_dict['pcp'] = int(seq_element.text)
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}pcp-force':
                                            seq_dict['pcp-force'] = int(seq_element.text)
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}drop-precedence-force':
                                            seq_dict['drop-precedence-force'] = int(seq_element.text)
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}count':
                                            seq_dict['count'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}log':
                                            seq_dict['log'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}mirror':
                                            seq_dict['mirror'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}copy-sflow':
                                            seq_dict['copy-sflow'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}known-unicast-only':
                                            seq_dict['known-unicast-only'] = True
                                            continue
                                        if seq_element.tag == '{urn:brocade.com:mgmt:brocade-mac-access-list}unknown-unicast-only':
                                            seq_dict['unknown-unicast-only'] = True
                                            continue
        return res_dict

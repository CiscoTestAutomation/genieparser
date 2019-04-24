''' show_acl.py

IOSXR parsers for the following show commands:
    * show access-lists afi-all
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common
# =======================================
# Schema for 'show access-lists afi-all'
# =======================================

class ShowAclAfiAllSchema(MetaParser):
	"""
	Schema for 'show access-lists afi-all'
	"""
	schema = {
        Any():{
            'name': str,
            'type': str,
            Optional('aces'): {
                Any(): {
                    'name': str,
                    'matches': {
                        Optional('l2'): {
                            'eth': {
                                'destination_mac_address': str,
                                'source_mac_address': str,
                                Optional('ether_type'): str,
                                Optional('vlan'): int,
                            }
                        },
                        Optional('l3'): {
                            Optional('ipv4'): {   # protocols
                                Optional('ttl'): int,
                                Optional('ttl_operator'): str,
                                Optional('precedence'): str,
                                'destination_ipv4_network': {
                                    Any(): {
                                        'destination_ipv4_network': str,
                                    }
                                },
                                'source_ipv4_network': {
                                    Any(): {
                                        'source_ipv4_network': str,
                                    }
                                }
                            },
                            Optional('ipv6'): {   # protocols
                                Optional('ttl'): int,
                                Optional('ttl_operator'): str,
                                Optional('precedence'): str,
                                'destination_ipv6_network': {
                                    Any(): {
                                        'destination_ipv6_network': str,
                                    }
                                },
                                'source_ipv6_network': {
                                    Any(): {
                                        'source_ipv6_network': str,
                                    }
                                }
                            },
                        },
                        Optional('l4'): {
                            Any(): {   # protocols
                                Optional('established'): bool,
                                Optional('source-port'): {
                                    Optional('operator'): {
                                        'operator': str,
                                        'port': str,
                                    }
                                },
                                Optional('destination_port'): {
                                    Optional('operator'): {
                                        'operator': str,                                        
                                        'port': str,
                                    }
                                }
                            }
                        },
                    },
                    'actions': {
                        'forwarding': str,
                        Optional('logging'): str,
                    },
                }
            }
        }
    }

# =======================================
# Parser for 'show access-lists afi-all'
# =======================================
class ShowAclAfiAll(ShowAclAfiAllSchema):
    """Parser for:
        'show access-lists afi-all'
    """

    cli_command = 'show access-lists afi-all'
    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ipv4 access-list acl_name
        # ipv6 access-list ipv6_acl
        p1 = re.compile(r'^(?P<ip>(ipv4|ipv6)) +access\-list +(?P<name>[\w\-\.#]+)$')

        # 10 permit tcp any any eq www
        # 30 permit tcp any any eq 443
        # 10 permit tcp 192.168.1.0 0.0.0.255 host 1.1.1.1 established log
        # 20 permit tcp host 2.2.2.2 eq www any precedence network ttl eq 255
        # 30 deny ipv4 any any
        # 10 permit ipv4 65.21.21.0 0.0.0.255 65.6.6.0 0.0.0.255
        p2 = re.compile(r'^(?P<seq>\d+) +(?P<actions_forwarding>permit|deny) +'
            '(?P<protocol>tcp|ipv4|ipv6) +(?P<src>(([\d\.]+ +[\d\.]+)|any|'
            '(host +[\d\.:]+))|([\d\.]+ +[\d\.]+))( ?(?P<src_operator>eq) +'
            '(?P<src_port>\w+))? +(?P<dst>(host +[\d\.:]+)|any|([\d\.]+ +'
            '[\d\.]+))(?P<log> +log)?( +(?P<des_operator>eq) +(?P<des_port>\w+))'
            '?(?P<established_log> +established +log)?( +precedence +'
            '(?P<precedence>network) +ttl +(?P<ttl_operator>eq) +(?P<ttl>\d+))?')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # ipv4 access-list acl_name
            # ipv6 access-list ipv6_acl
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_type = group['ip']
                acl_dict = ret_dict.setdefault(group['name'], {})
                acl_dict['name'] = group['name']
                acl_dict['type'] = acl_type + '-acl-type'
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                seq = int(group['seq'])
                actions_forwarding = group['actions_forwarding']
                protocol = group['protocol']
                src = group['src']
                src_operator = group['src_operator']
                src_port = group['src_port']
                dst = group['dst']
                des_operator = group['des_operator']
                des_port = group['des_port']
                established_log = group['established_log']
                log = group['log']
               

                seq_dict = acl_dict.setdefault('aces', {}).setdefault(seq, {})
                seq_dict['name'] = group['seq']
                l3_dict = seq_dict.setdefault('matches', {}).setdefault('l3', {})\
                    .setdefault(acl_type, {})

                l3_dict.setdefault('source_'+acl_type+'_network', {}).\
                    setdefault(src, {}).setdefault('source_'+acl_type+'_network', src)

                l3_dict.setdefault('destination_'+acl_type+'_network', {}).\
                    setdefault(src, {}).setdefault('destination_'+acl_type+'_network', dst)

                if src_operator and src_port:
                    l4_dict = seq_dict.setdefault('matches', {}).setdefault('l4', {})\
                    .setdefault(protocol, {})
                    source_port_operator_dict = l4_dict.setdefault('source-port', {}). \
                        setdefault('operator', {})
                    source_port_operator_dict.update({'operator' : src_operator})
                    source_port_operator_dict.update({'port' : src_port})

                if des_operator and des_port:
                    l4_dict = seq_dict.setdefault('matches', {}).setdefault('l4', {})\
                    .setdefault(protocol, {})
                    dest_port_operator_dict = l4_dict.setdefault('destination_port', {}). \
                        setdefault('operator', {})
                    dest_port_operator_dict.update({'operator' : des_operator})
                    dest_port_operator_dict.update({'port' : des_port})

                if established_log:
                    l4_dict = seq_dict.setdefault('matches', {}).setdefault('l4', {})\
                    .setdefault(protocol, {})
                    l4_dict.update({'established': True })

                if group['precedence']:
                    precedence = group['precedence']
                    l3_dict.update({'precedence' : precedence})

                if group['ttl_operator'] and  group['ttl']: 
                    ttl_operator = group['ttl_operator']
                    ttl = int(group['ttl'])
                    l3_dict.update({'ttl': ttl})
                    l3_dict.update({'ttl_operator': ttl_operator})

                if group['actions_forwarding']:
                    actions_forwarding = group['actions_forwarding']
                    seq_dict.setdefault('actions', {}).setdefault('forwarding', actions_forwarding)

                seq_dict['actions']['logging'] = 'log-syslog' if log or established_log else 'log-none'
                continue
        return ret_dict

# =======================================
# Parser for 'show access-lists ethernet-services'
# =======================================
class ShowAclEthernetServices(ShowAclAfiAllSchema):
    """Parser for:
        'show access-lists ethernet-services'
    """

    cli_command = 'show access-lists ethernet-services'
    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ethernet-services access-list eth_acl
        p1 = re.compile(r'^(?P<ip>(ethernet-services)) +access\-list +(?P<name>[\w\-\.#]+)$')

        # 10 permit host 0000.0000.0000 host 0000.0000.0000
        # 20 deny host 0000.0000.0000 host 0000.0000.0000 8041
        # 30 deny host 0000.0000.0000 host 0000.0000.0000 vlan 10
        # 40 permit host aaaa.aaaa.aaaa host bbbb.bbbb.bbbb 80f3
        p2 = re.compile(r'^(?P<seq>\d+) +(?P<actions_forwarding>permit|deny)? +'
            '(?P<source_mac_address>(any|(host +[\d\.\w]+))|([\d\.]+ +[\d\.]+))'
            ' +(?P<destination_mac_address>(host +[\d\.\w]+)|any)( +'
            '(?P<ether_type_dynamic>\w+) +(?P<ether_type_value>\d+))?'
            '( +(?P<ether_type>[\w\s]+))?$')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # ipv4 access-list acl_name
            # ipv6 access-list ipv6_acl
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_type = 'eth-acl-type'
                acl_dict = ret_dict.setdefault(group['name'], {})
                acl_dict['name'] = group['name']
                acl_dict['type'] = acl_type
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                seq = int(group['seq'])
                actions_forwarding = group['actions_forwarding']
               
                seq_dict = acl_dict.setdefault('aces', {}).setdefault(seq, {})
                seq_dict['name'] = group['seq']
                l2_dict = seq_dict.setdefault('matches', {}).setdefault('l2', {})\
                    .setdefault('eth', {})
                l2_dict.update({'destination_mac_address' : group['destination_mac_address']})
                l2_dict.update({'source_mac_address' : group['source_mac_address']})

                if group['ether_type_dynamic'] and group['ether_type_value']:
                    l2_dict.update({group['ether_type_dynamic'] : int(group['ether_type_value'])})

                if group['ether_type']:
                    l2_dict.update({'ether_type' : group['ether_type']})

                if group['actions_forwarding']:
                    actions_forwarding = group['actions_forwarding']
                    seq_dict.setdefault('actions', {}).setdefault('forwarding', actions_forwarding)
                continue

        return ret_dict
"""
show_run.py

IOSXR parsers for the following show commands:
    * show run key chain
    * show run router isis

"""

# Python
import re
from collections import OrderedDict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ====================================
# Schema for 'show run key chain'
# ====================================
class ShowRunKeyChainSchema(MetaParser):
    """Schema for show run key chain"""

    schema = {
        'key_chain': {
            Optional(Any()): {
                Optional('keys'): {
                    Optional(Any()): {
                        Optional('accept_lifetime'): str,
                        Optional('key_string'): str,
                        Optional('send_lifetime'): str,
                        Optional('cryptographic_algorithm'): str
                    },
                },
                Optional('accept_tolerance'): str
            },
        },
    }


class ShowRunKeyChain(ShowRunKeyChainSchema):
    """Parser for show run key chain"""

    cli_command = 'show run key chain'

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # key chain ISIS-HELLO-CORE
        p1 = re.compile(r'^key +chain +(?P<key_chain_name>.*)$')

        # key 1
        p2 = re.compile(r'^key +(?P<key_name>(\w+))$')

        # accept-lifetime 00:01:00 january 01 2013 infinite
        p3 = re.compile(r'^accept-lifetime +(?P<accept_lifetime>.*)$')

        # key-string password 020F175218
        p4 = re.compile(r'^key-string +(?P<key_string>.*)$')

        # send-lifetime 00:01:00 january 01 2013 infinite
        p5 = re.compile(r'^send-lifetime +(?P<send_lifetime>.*)$')

        # cryptographic-algorithm HMAC-MD5
        p6 = re.compile(r'^cryptographic-algorithm +(?P<cryptographic_algorithm>.*)$')

        # accept-tolerance infinite
        p7 = re.compile(r'^accept-tolerance +(?P<accept_tolerance>(\w+)) !$')

        for line in out.splitlines():
            line = line.strip()

            # key chain ISIS-HELLO-CORE
            m = p1.match(line)
            if m:
                key_chain_name = m.groupdict()['key_chain_name']
                key_chain_dict = ret_dict.setdefault('key_chain', {}).setdefault(key_chain_name, {})
                continue

            # key 1
            m = p2.match(line)
            if m:
                key_name = m.groupdict()['key_name']
                key_dict = key_chain_dict.setdefault('keys', {}).setdefault(key_name, {})
                continue

            # accept-lifetime 00:01:00 january 01 2013 infinite
            m = p3.match(line)
            if m:
                key_dict['accept_lifetime'] = m.groupdict()['accept_lifetime']
                continue

            # key-string password 020F175218
            m = p4.match(line)
            if m:
                key_dict['key_string'] = m.groupdict()['key_string']
                continue

            # send-lifetime 00:01:00 january 01 2013 infinite
            m = p5.match(line)
            if m:
                key_dict['send_lifetime'] = m.groupdict()['send_lifetime']
                continue

            # cryptographic-algorithm HMAC-MD5
            m = p6.match(line)
            if m:
                key_dict['cryptographic_algorithm'] = m.groupdict()['cryptographic_algorithm']
                continue

            # accept-tolerance infinite
            m = p7.match(line)
            if m:
                key_chain_dict['accept_tolerance'] = m.groupdict()['accept_tolerance']
                continue

        return ret_dict


# =================================
# Schema for 'show run router isis'
# =================================
class ShowRunRouterIsisSchema(MetaParser):
    """Schema for show run router isis"""
    
    schema = {
        'isis': {
            Any(): {
                Optional('segment_routing'): {
                    Optional(Any()): str,
                },
                Optional('lsp_gen_interval'): {
                    Optional(Any()): Any(),
                },
                Optional('address_family'): {
                    Optional(Any()): OrderedDict({
                        Optional('fast_reroute'): {
                            Optional('per_prefix'): {
                                Optional('tiebreaker'):{
                                    Optional(Any()): Any(),
                                },
                            },
                        },
                        Optional('mpls'): {
                            Optional('traffic_eng'): Any(),
                        },
                        Optional('spf_interval'): {
                            Optional(Any()): Any(),
                        },
                        Optional('spf_prefix_priority'): {
                            Optional(Any()): Any(),
                        },
                        Optional('segment_routing'): {
                            Optional(Any()): str,
                        },
                        Optional(Any()): str,
                    })
                },
                Optional('interfaces'): {
                    Optional(Any()): OrderedDict({
                        Optional('bfd'): {
                            Optional(Any()): Any(),
                        },
                        Optional('address_family'): {
                            Optional(Any()): {
                                Optional(Any()): Any(),
                                Optional(Any()): {
                                    Optional(Any()): Any(),
                                },
                            },
                        },
                        Optional(Any()): Any(),
                    })
                },
                Optional(Any()): Any(),
            }
        }
    }


class ShowRunRouterIsis(ShowRunRouterIsisSchema):
    """Parser for show run router isis"""
    
    cli_command = 'show run router isis'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        router_isis_dict = {}
        is_interface = False
        is_address_family = False
        isis_name = None
        for line in out.splitlines():
            line = line.rstrip()
            
            p0 = re.compile(r'^\s*!+\s*$')
            m = p0.match(line)
            if m:
                is_address_family = False
            
            # Parsers for ISIS Address Family
            if is_address_family:
                # fast-reroute per-prefix tiebreaker srlg-disjoint index 255
                a1 = re.compile(r'^\s*fast-reroute\sper-prefix\stiebreaker\s+(?P<key>\S+)\s+(?P<value>.+)$')
                m = a1.match(line)
                if m:
                    if is_interface:
                        if not 'fast_reroute' in router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family]:
                            router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family]['fast_reroute'] = {'per_prefix':{'tiebreaker': {}}}
                        router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family]['fast_reroute']['per_prefix']['tiebreaker'][m.groupdict()['key'].replace('-', '_')] = m.groupdict()['value']
                    if not is_interface:
                        if not 'fast_reroute' in router_isis_dict['isis'][isis_name]['address_family'][address_family]:
                            router_isis_dict['isis'][isis_name]['address_family'][address_family]['fast_reroute'] = {'per_prefix':{'tiebreaker': {}}}
                        router_isis_dict['isis'][isis_name]['address_family'][address_family]['fast_reroute']['per_prefix']['tiebreaker'][m.groupdict()['key'].replace('-', '_')] = m.groupdict()['value']
                    continue
                
                # mpls traffic-eng level-2-only
                a2 = re.compile(r'^\s*mpls\straffic-eng\s+(?P<mpls_traffic_eng>.+)$')
                m = a2.match(line)
                if m:
                    if is_interface:
                        if not 'mpls' in router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family]:
                            router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family]['mpls'] = {'traffic_eng': []}
                        router_isis_dict['isis'][isis_name][interface]['address_family'][address_family]['mpls']['traffic_eng'].append(m.groupdict()['mpls_traffic_eng'])
                    if not is_interface:
                        if not 'mpls' in router_isis_dict['isis'][isis_name]['address_family'][address_family]:
                            router_isis_dict['isis'][isis_name]['address_family'][address_family]['mpls'] = {'traffic_eng': []}
                        router_isis_dict['isis'][isis_name]['address_family'][address_family]['mpls']['traffic_eng'].append(m.groupdict()['mpls_traffic_eng'])
                    continue
                
                # segment-routing mpls sr-prefer
                a3 = re.compile(r'^\s*segment-routing\s+(?P<segment_key>\S+)\s+(?P<segment_value>.+)$')
                m = a3.match(line)
                if m:
                    if not 'segment_routing' in router_isis_dict['isis'][isis_name]['address_family'][address_family]:
                        router_isis_dict['isis'][isis_name]['address_family'][address_family]['segment_routing'] = {}
                    router_isis_dict['isis'][isis_name]['address_family'][address_family]['segment_routing'][m.groupdict()['segment_key'].replace('-', '_')] = m.groupdict()['segment_value']
                    continue
                
                # spf prefix-priority critical tag 1000
                a4 = re.compile(r'^\s*spf\sprefix-priority\s+(?P<tag_key>\S+\stag+)\s+(?P<tag_value>.+)$')
                m = a4.match(line)
                if m:
                    if not 'spf_prefix_priority' in router_isis_dict['isis'][isis_name]['address_family'][address_family]:
                        router_isis_dict['isis'][isis_name]['address_family'][address_family]['spf_prefix_priority'] = {}
                    router_isis_dict['isis'][isis_name]['address_family'][address_family]['spf_prefix_priority'][m.groupdict()['tag_key'].replace(' ', '_')] = m.groupdict()['tag_value']
                    continue
                
                # spf-interval maximum-wait 8000 initial-wait 300 secondary-wait 500
                a5 = re.compile(r'^\s*spf-interval\s+(?P<spf_interval>.+)$')
                m = a5.match(line)
                if m:
                    spf_interval = m.groupdict()['spf_interval']
                    pattern = re.compile('(\S+-wait)\s([0-9]+)')
                    matches = pattern.findall(spf_interval)
                    spf_interval_pairs = {key.replace('-', '_'):val for key,val in matches}
                    router_isis_dict['isis'][isis_name]['address_family'][address_family]['spf_interval'] = spf_interval_pairs
                    continue
                
                   
                # Generic, catch all key/value
                a9 = re.compile(r'^\s*(?P<generic_key>\S+)\s+(?P<generic_value>.+)$')
                m = a9.match(line)
                if m:
                    if is_interface:
                        router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'][address_family][m.groupdict()['generic_key'].replace('-', '_')] = m.groupdict()['generic_value']
                    if not is_interface:
                        router_isis_dict['isis'][isis_name]['address_family'][address_family][m.groupdict()['generic_key'].replace('-', '_')] = m.groupdict()['generic_value']
                    continue
                
                # End Parsers for ISIS Address Family
                continue
            
            
            # router isis 65109
            p1 = re.compile(r'^\s*router\sisis\s+(?P<isis_name>.+)$')
            m = p1.match(line)
            if m:
                router_isis_dict.setdefault('isis', {})
                isis_name = m.groupdict()['isis_name']
                router_isis_dict['isis'][isis_name] = {}
                router_isis_dict['isis'][isis_name]['address_family'] = {}
                router_isis_dict['isis'][isis_name]['segment_routing'] = {}
                router_isis_dict['isis'][isis_name]['interfaces'] = {}
                continue
            
            # segment-routing global-block 160000 167999
            p2 = re.compile(r'^\s*segment-routing\s+(?P<segment_routing_key>\S+)\s+(?P<segment_routing_value>.+)$')
            m = p2.match(line)
            if m:
                router_isis_dict['isis'][isis_name]['segment_routing'][m.groupdict()['segment_routing_key'].replace('-', '_')] = m.groupdict()['segment_routing_value']
                continue
            
            # lsp-gen-interval maximum-wait 8000 initial-wait 1 secondary-wait 250
            p3 = re.compile(r'^\s*lsp-gen-interval\s+(?P<lsp_gen_interval>.+)$')
            m = p3.match(line)
            if m:
                lsp_gen_interval = m.groupdict()['lsp_gen_interval']
                pattern = re.compile('(\S+-wait)\s([0-9]+)')
                matches = pattern.findall(lsp_gen_interval)
                lsp_gen_pairs = {key.replace('-', '_'):val for key,val in matches}
                router_isis_dict['isis'][isis_name]['lsp_gen_interval'] = lsp_gen_pairs
                continue
            
            # address-family ipv4 unicast 
            p4 = re.compile(r'^\s*address-family\s+(?P<address_family>.+)$')
            m = p4.match(line)
            if m:
                is_address_family = True
                address_family = m.groupdict()['address_family'].replace(' ', '_')
                if not is_interface:
                    router_isis_dict['isis'][isis_name]['address_family'][address_family] = {}
                if is_interface:
                    router_isis_dict['isis'][isis_name]['interfaces'][interface]['address_family'] = {address_family: {}}
                continue
            
            # interface Bundle-Ether2
            p5 = re.compile(r'^\s*interface\s+(?P<interface>\S+)\s*$')
            m = p5.match(line)
            if m:
                is_interface = True
                interface = m.groupdict()['interface']
                router_isis_dict['isis'][isis_name]['interfaces'][interface] = {}
                continue
            
            # Parsers for Interface Only
            if is_interface:
                # interface Bundle-Ether2
                i1 = re.compile(r'^\s*bfd\s+(?P<bfd_key>\S+)\s+(?P<bfd_value>.+)$')
                m = i1.match(line)
                if m:
                    if not 'bfd' in router_isis_dict['isis'][isis_name]['interfaces'][interface]:
                        router_isis_dict['isis'][isis_name]['interfaces'][interface]['bfd'] = {}
                    router_isis_dict['isis'][isis_name]['interfaces'][interface]['bfd'][m.groupdict()['bfd_key'].replace('-', '_')] = m.groupdict()['bfd_value']
                    continue
                # passive
                i1 = re.compile(r'^\s*(?P<other>[^\s!]+)\s*$')
                m = i1.match(line)
                if m:
                    if not 'other' in router_isis_dict['isis'][isis_name]['interfaces'][interface]:
                        router_isis_dict['isis'][isis_name]['interfaces'][interface]['other'] = []
                    router_isis_dict['isis'][isis_name]['interfaces'][interface]['other'].append(m.groupdict()['other'])
                    continue
            # End Parsers for Interface Only
            
            # Generic, catch all key/value
            # Skip if isis_name has not been found yet - skip timestamp value
            if not isis_name == None:
                p9 = re.compile(r'^\s*(?P<generic_key>\S+)\s+(?P<generic_value>.+)$')
                m = p9.match(line)
                if m:
                    if not is_interface:
                        router_isis_dict['isis'][isis_name][m.groupdict()['generic_key'].replace('-', '_')] = m.groupdict()['generic_value']
                        continue
                    if is_interface:
                        router_isis_dict['isis'][isis_name]['interfaces'].setdefault(interface, {}).setdefault(m.groupdict()['generic_key'].replace('-', '_'), m.groupdict()['generic_value'])
                        continue
        
        return router_isis_dict
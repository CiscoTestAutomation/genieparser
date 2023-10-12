"""show_derived.py

IOSXE parsers for the following show commands:
   * show derived-config interface <INTF>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

# Genie Libs
from genie.libs.parser.utils.common import Common

# ====================================================
#  Schema for 'show derived-config interface'
# ====================================================
class ShowDerivedConfigInterfaceSchema(MetaParser):
    """Schema for show derived-config interface <INTF>"""
    schema = {
        'derived_config': {
            Any(): {
                Optional('host_reachability_protocol'): str,
                Optional('source_interface'): str,
                Optional('dual_stack_ip'): str,
                Optional('pim_operation'): str,
                Optional('member_vni'): {
                    Any(): {
                        Optional('vrf'): str,
                        Optional('ingress_replication'): {
                            'ir_enabled': bool,
                            Optional('remote_peer_ip'): str,
                        },
                        Optional('mcast_group_ip'): str,
                        Optional('mcast_group_ipv6'): str,
                        Optional('local_routing'): bool
                    }
                },
                Optional('ip_address'): str,
                Optional('ipv6_address'): str,
                Optional('ip_access_group_in'): str,
                Optional('ip_access_group_out'): str,
                Optional('ipv6'): str,
                Optional('ipv6_access_group_in'): str,
                Optional('ipv6_access_group_out'): str,
                Optional('tunnel_source'): str,
                Optional('tunnel_mode'): str,
                Optional('tunnel_destination'): str,
                Optional('tunnel_ipsec_profile'): str,
                Optional('description'): str,
                Optional('switchport_mode'): str,
                Optional('allowed_vlan'): str,
                Optional('switchport_block'): str,
                Optional('switchport_port_security'): {
                    'switchport_port_security': bool,
                    Optional('violation'): str,
                    Optional('aging_time'): int,
                    Optional('aging_type'): str,
                    Optional('maximum'): {
                        Any(): {
                            Optional('vlan'): str
                        }
                    }
                },
                Optional('vxlan_encapsulation'): {
                    Optional('encapsulation_type'): str,
                    Optional('dual_stack_ip'): str,
                },
                Optional('load_interval'): int,
                Optional('storm_control'): {
                    Optional('broadcast_level_pps'): str,
                    Optional('multicast_level_pps'): str,
                    Optional('action'): str
                },
                Optional('spanning_tree'): {
                    Optional('portfast'): bool,
                    Optional('bpduguard'): str
                },
                Optional('service_policy'): {
                    Optional('input'): str,
                    Optional('output'): str
                },
                Optional('ip_dhcp_snooping_limit_rate'): int,

                Optional('vrf'): str,
                Optional('ipv4_unnumbered_intf'): str,
                Optional('ipv6_unnumbered_intf'): str,
                Optional('autostate'): bool,

            }
        }
    }
# ====================================================
#  Parser for 'show crypto ipsec internal dual'
# ====================================================    
class ShowDerivedConfigInterface(ShowDerivedConfigInterfaceSchema):
    """ Parser for 
        * show derived-config interface <INTF>
    """

    cli_command = ['show derived-config interface {interface}', 'show derived-config']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize return dict
        ret_dict = {}

        # interface Tunnel1
        p1 = re.compile(r"^interface\s+(?P<interface_name>[\S\s]+)$")

        # ip address 192.168.1.1 255.255.255.0
        p2 = re.compile(r"^ip\s+address\s+(?P<ip_address>[\S\s]+)\s+(?P<ip_mask>[\S\s]+)$")

        # ipv6 address 8001::100/64
        p3 = re.compile(r"^ipv6\s+address\s+(?P<ipv6_address>[\S\s]+)$")

        # ip access-group Tu1-ipsec-ds-ipv4-in in
        p4 = re.compile(r"^ip\s+access-group\s+(?P<ip_access_group_in>[\S\s]+)\s+in$")
        
        # ip access-group Tu1-ipsec-ds-ipv4-out out
        p5 = re.compile(r"^ip\s+access-group\s+(?P<ip_access_group_out>[\S\s]+)\s+out$")
        
        # ipv6 enable
        p6 = re.compile(r"^ipv6\s+enable$")
        
        # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-in in
        p7 = re.compile(r"^ipv6\s+traffic-filter\s+(?P<ipv6_access_group_in>[\S\s]+)\s+in$")

        # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-out out
        p8 = re.compile(r"^ipv6\s+traffic-filter\s+(?P<ipv6_access_group_out>[\S\s]+)\s+out$")

        # tunnel source 11.11.11.2
        p9 = re.compile(r"^tunnel\s+source\s+(?P<tunnel_source>[\S\s]+)$")

        # tunnel mode ipsec dual-overlay
        p10 = re.compile(r"^tunnel\s+mode\s+(?P<tunnel_mode>[\S\s]+)$")

        # tunnel destination 30.30.30.2
        p11 = re.compile(r"^tunnel\s+destination\s+(?P<tunnel_destination>[\S\s]+)$")

        # tunnel protection ipsec profile ipsec_global_profile
        p12 = re.compile(
            r"^tunnel\s+protection\s+ipsec\s+profile\s+(?P<tunnel_ipsec_profile>[\S\s]+)$")

        # description Sourcing interface template beta
        p13 = re.compile(r"^description\s+(?P<description>[\S\s]+)$")
        
        # switchport trunk allowed vlan 3
        p14 = re.compile(r"^switchport trunk allowed vlan\s+(?P<allowed_vlan>\S+)$")
        
        # switchport mode trunk
        p15 = re.compile(r"^switchport mode\s+(?P<switchport_mode>\w+)$")

        # switchport block unicast
        p16 = re.compile(r"^switchport block\s+(?P<switchport_block>\w+)$")
        
        # switchport port-security maximum 3
        p17 = re.compile(r"^switchport port-security maximum\s+(?P<maximum>\d+)$")

        # switchport port-security maximum 2 vlan access
        p18 = re.compile(r"^switchport port-security maximum\s+(?P<maximum>\d+) vlan (?P<vlan>\w+)$")

        # switchport port-security violation restrict
        p19 = re.compile(r"^switchport port-security violation\s+(?P<violation>\w+)$")

        # switchport port-security aging time 2
        p20 = re.compile(r"^switchport port-security aging time\s+(?P<aging_time>\d+)$")

        # switchport port-security aging type inactivity
        p21 = re.compile(r"^switchport port-security aging type\s+(?P<aging_type>\w+)$")

        # switchport port-security
        p22 = re.compile(r"^switchport port-security$")

        # load-interval 30
        p23 = re.compile(r"^load-interval\s+(?P<load_interval>\d+)$")

        # storm-control broadcast level pps 1k
        p24 = re.compile(r"^storm-control broadcast level pps\s+(?P<broadcast_level_pps>\w+)$")
        
        # storm-control multicast level pps 2k
        p25 = re.compile(r"^storm-control multicast level pps\s+(?P<multicast_level_pps>\w+)$")
        
        # storm-control action trap
        p26 = re.compile(r"^storm-control action\s+(?P<action>\w+)$")

        # spanning-tree portfast
        p27 = re.compile(r"^spanning-tree\s+(?P<portfast>\w+)$")

        # spanning-tree bpduguard enable
        p28 = re.compile(r"^spanning-tree bpduguard\s+(?P<bpduguard>\w+)$")

        # service-policy input AutoConf-4.0-CiscoPhone-Input-Policy
        p29 = re.compile(r"^service-policy input\s+(?P<input>\S+)$")

        # service-policy output AutoConf-4.0-Output-Policy
        p30 = re.compile(r"^service-policy output\s+(?P<output>\S+)$")

        # ip dhcp snooping limit rate 15
        p31 = re.compile(r"^ip dhcp snooping limit rate\s+(?P<ip_dhcp_snooping_limit_rate>\d+)$")

        # host-reachability protocol bgp
        p32 = re.compile(r'^host-reachability protocol (?P<protocol>[a-zA-Z]+)$')

        # source-interface loopback1
        p33 = re.compile(r'^source-interface (?P<src_intf>[a-zA-Z0-9\-]+)$')

        # member vni 20011 ingress-replication
        p34 = re.compile(r'^member vni (?P<vni>[0-9]+) ingress-replication$')

        # member vni 20012 mcast-group 224.1.1.1
        p35 = re.compile(r'^member vni (?P<vni>[0-9]+) mcast-group (?P<ip>[0-9\.]+)$')

        # member vni 20010 mcast-group FF0E::A
        p36 = re.compile(r'^member vni (?P<vni>[0-9]+) mcast-group (?P<ipv6>[a-fA-F\d\:]+)$')

        # member vni 20011 ingress-replication local-routing
        p37 = re.compile(r'^member vni (?P<vni>[0-9]+) ingress-replication '
                        r'local-routing$')

        # member vni 20011
        p38 = re.compile(r'^member vni (?P<vni>[0-9]+)$')

        # ingress-replication 1.1.1.1
        p39 = re.compile(r'^ingress-replication (?P<ip>[0-9\.]+)$')

        # member vni 20012 mcast-group 224.1.1.1 local-routing
        p40 = re.compile(r'^member vni (?P<vni>[0-9]+) mcast-group (?P<ip>[0-9\.]+) '
                        r'local-routing$')

        # member vni 30000 vrf red
        p41 = re.compile(r'^member vni (?P<vni>[0-9]+) vrf (?P<vrf>\S+)$')

        #member vni 2000401 mcast-group 239.4.0.145 FF1E::91
        p42 = re.compile(r"member vni (?P<vni>[0-9]+) mcast-group (?P<ipv4_group>\S+) (?P<ipv6_group>\S+)$")

        # vxlan encapsulation dual-stack prefer-ipv6 underlay-mcast ipv4
        # vxlan encapsulation ipv6
        p43 = re.compile(r'^vxlan encapsulation +(?P<type>dual-stack|ipv6|ipv4)\s+(?P<dual_stack_ip>\S+)$')

        #ip pim sparse-mode
        p44 = re.compile(r"ip pim (?P<pim_operation>\S+)$")

        # vrf forwarding VRF1
        p45 = re.compile(r"^vrf forwarding\s+(?P<vrf>\S+)$")

        # ip unnumbered Loopback0
        p46 = re.compile(r"^ip unnumbered\s+(?P<ipv4_unnumbered_intf>\S+)$")

        # ipv6 unnumbered Loopback0
        p47 = re.compile(r"^ipv6 unnumbered\s+(?P<ipv6_unnumbered_intf>\S+)$")

        # no autostate
        p48 = re.compile(r"^no autostate$")

        for line in out.splitlines():
            line = line.strip()

            # interface Tunnel1
            m = p1.match(line)
            if m:
                interface_name = m.groupdict()["interface_name"]
                intf_dict = ret_dict.setdefault('derived_config', {}).setdefault(interface_name, {})
                continue

            # ip address 192.168.1.1 255.255.255.0
            m = p2.match(line)
            if m:
                intf_dict['ip_address'] = m.groupdict()['ip_address']
                continue

            # ipv6 address 8001::100/64
            m = p3.match(line)
            if m:
                intf_dict['ipv6_address'] = m.groupdict()['ipv6_address']
                continue

            # ip access-group Tu1-ipsec-ds-ipv4-in in
            m = p4.match(line)
            if m:
                intf_dict['ip_access_group_in'] = m.groupdict()['ip_access_group_in']
                continue

            # ip access-group Tu1-ipsec-ds-ipv4-out out
            m = p5.match(line)
            if m:
                intf_dict['ip_access_group_out'] = m.groupdict()['ip_access_group_out']
                continue

            # ipv6 enable
            m = p6.match(line)
            if m:
                intf_dict['ipv6'] = 'enabled'
                continue

            # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-in in
            m = p7.match(line)
            if m:
                intf_dict['ipv6_access_group_in'] = m.groupdict()['ipv6_access_group_in']
                continue

            # ipv6 traffic-filter Tu1-ipsec-ds-ipv6-out out
            m = p8.match(line)
            if m:
                intf_dict['ipv6_access_group_out'] = m.groupdict()['ipv6_access_group_out']
                continue

            # tunnel source 11.11.11.2
            m = p9.match(line)
            if m:
                intf_dict['tunnel_source'] = m.groupdict()['tunnel_source']
                continue

            # tunnel mode ipsec dual-overlay
            m = p10.match(line)
            if m:
                intf_dict['tunnel_mode'] = m.groupdict()['tunnel_mode']
                continue

            # tunnel destination 30.30.30.2
            m = p11.match(line)
            if m:
                intf_dict['tunnel_destination'] = m.groupdict()['tunnel_destination']
                continue

            # tunnel protection ipsec profile ipsec_global_profile
            m = p12.match(line)
            if m:
                intf_dict['tunnel_ipsec_profile'] = m.groupdict()['tunnel_ipsec_profile']
                continue

            m = p13.match(line)
            if m:
                intf_dict['description'] = m.groupdict()['description']
                continue

            m = p14.match(line)
            if m:
                intf_dict['allowed_vlan'] = m.groupdict()['allowed_vlan']
                continue

            m = p15.match(line)
            if m:
                intf_dict['switchport_mode'] = m.groupdict()['switchport_mode']
                continue

            # switchport block unicast
            m = p16.match(line)
            if m:
                intf_dict['switchport_block'] = m.groupdict()['switchport_block']
                continue
            
            # switchport port-security maximum 3
            m = p17.match(line)
            if m:
                intf_dict.setdefault('switchport_port_security', {}).setdefault('maximum', {})\
                    .setdefault(m.groupdict()['maximum'], {})
                continue

            # switchport port-security maximum 2 vlan access
            m = p18.match(line)
            if m:
                max_dict = intf_dict.setdefault('switchport_port_security', {}).setdefault('maximum', {})\
                    .setdefault(m.groupdict()['maximum'], {})
                max_dict['vlan'] = m.groupdict()['vlan']
                continue

            # switchport port-security violation restrict
            m = p19.match(line)
            if m:
                intf_dict.setdefault('switchport_port_security', {}).setdefault('violation', m.groupdict()['violation'])
                continue

            # switchport port-security aging time 2
            m = p20.match(line)
            if m:
                intf_dict.setdefault('switchport_port_security', {}).setdefault('aging_time', int(m.groupdict()['aging_time']))
                continue

            # switchport port-security aging type inactivity
            m = p21.match(line)
            if m:
                intf_dict.setdefault('switchport_port_security', {}).setdefault('aging_type', m.groupdict()['aging_type'])
                continue

            # switchport port-security
            m = p22.match(line)
            if m:
                intf_dict.setdefault('switchport_port_security', {}).setdefault('switchport_port_security', True)
                continue

            # load-interval 30
            m = p23.match(line)
            if m:
                intf_dict['load_interval'] = int(m.groupdict()['load_interval'])
                continue

            # storm-control broadcast level pps 1k
            m = p24.match(line)
            if m:
                intf_dict.setdefault('storm_control', {}).setdefault('broadcast_level_pps', m.groupdict()['broadcast_level_pps'])
                continue
            
            # storm-control multicast level pps 2k
            m = p25.match(line)
            if m:
                intf_dict.setdefault('storm_control', {}).setdefault('multicast_level_pps', m.groupdict()['multicast_level_pps'])
                continue

            # storm-control action trap
            m = p26.match(line)
            if m:
                intf_dict.setdefault('storm_control', {}).setdefault('action', m.groupdict()['action'])
                continue

            # spanning-tree portfast
            m = p27.match(line)
            if m:
                intf_dict.setdefault('spanning_tree', {}).setdefault('portfast', True)
                continue

            # spanning-tree bpduguard enable
            m = p28.match(line)
            if m:
                intf_dict.setdefault('spanning_tree', {}).setdefault('bpduguard', m.groupdict()['bpduguard'])
                continue

            # service-policy input AutoConf-4.0-CiscoPhone-Input-Policy
            m = p29.match(line)
            if m:
                intf_dict.setdefault('service_policy', {}).setdefault('input', m.groupdict()['input'])
                continue

            # service-policy output AutoConf-4.0-Output-Policy
            m = p30.match(line)
            if m:
                intf_dict.setdefault('service_policy', {}).setdefault('output', m.groupdict()['output'])
                continue

            # ip dhcp snooping limit rate 15
            p31 = re.compile(r"^ip dhcp snooping limit rate\s+(?P<ip_dhcp_snooping_limit_rate>\d+)$")
            m = p31.match(line)
            if m:
                intf_dict['ip_dhcp_snooping_limit_rate'] = int(m.groupdict()['ip_dhcp_snooping_limit_rate'])
                continue
            
            # host-reachability protocol bgp
            m = p32.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'host_reachability_protocol': group['protocol']})
                continue

            # source-interface loopback1
            m = p33.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'source_interface': group['src_intf']})
                continue

            # member vni 20011 ingress-replication
            m = p34.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'ingress_replication': {
                                                    'ir_enabled': True}}})
                continue

            # member vni 20012 mcast-group 224.1.1.1
            m = p35.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group_ip': group['ip']}})
                continue
            
            # member vni 20012 mcast-group FF0E::C
            m = p36.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group_ipv6': group['ipv6']}})
                continue
            # member vni 20011 ingress-replication local-routing
            m = p37.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'ingress_replication': {
                                                    'ir_enabled': True
                                                  },
                                                  'local_routing': True}})
                continue

            # member vni 20011
            m = p38.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                vni = group['vni']
                continue

            # ingress-replication 1.1.1.1
            m = p39.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({vni: {'ingress_replication': {
                                            'ir_enabled': True,
                                            'remote_peer_ip': group['ip']}}})
                continue

            # member vni 20012 mcast-group 224.1.1.1 local-routing
            m = p40.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group': group['ip'],
                                                  'local_routing': True}})
                continue

            # member vni 30000 vrf red
            m = p41.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'vrf': group['vrf']}})
                continue

            # member vni 20012 mcast-group 224.1.1.1 local-routing
            m = p42.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group_ip': group['ipv4_group'],'mcast_group_ipv6': group['ipv6_group']}})
                continue

            # vxlan encapsulation dual-stack prefer-ipv6 underlay-mcast ipv4
            # vxlan encapsulation ipv6
            m = p43.match(line)
            if m:
                intf_dict.setdefault('vxlan_encapsulation', {}).setdefault('encapsulation_type', m.groupdict()['type'])
                intf_dict.setdefault('vxlan_encapsulation', {}).setdefault('dual_stack_ip', m.groupdict()['dual_stack_ip'])
                continue

            #ip pim sparse-mode
            m = p44.match(line)
            if m:
                intf_dict['pim_operation'] = m.groupdict()['pim_operation']
                continue

            # vrf forwarding VRF1
            m = p45.match(line)
            if m:
                intf_dict['vrf'] = m.groupdict()['vrf']
                continue

            # ip unnumbered Loopback0
            m = p46.match(line)
            if m:
                intf_dict['ipv4_unnumbered_intf'] = m.groupdict()['ipv4_unnumbered_intf']
                continue

            # ipv6 unnumbered Loopback0
            m = p47.match(line)
            if m:
                intf_dict['ipv6_unnumbered_intf'] = m.groupdict()['ipv6_unnumbered_intf']
                continue

            # no autostate
            m = p48.match(line)
            if m:
                intf_dict['autostate'] = False
                continue

        return ret_dict

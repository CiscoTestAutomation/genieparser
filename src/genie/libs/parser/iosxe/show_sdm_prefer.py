"""show_sdm_prefer.py
   supported commands:
     *  show sdm prefer
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

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowSdmPreferSchema(MetaParser):
    """Schema for show sdm prefer"""
    schema = {
        str:{ #title of data
            'template_type': str, #template used 
            Optional('current_ingress_ipv4'): int, 
            Optional('proposed_ingress_ipv4'): int, 
            Optional('current_ingress_non_ipv4'): int, 
            Optional('proposed_ingress_non_ipv4'): int, 
            Optional('current_egress_ipv4'): int, 
            Optional('proposed_egress_ipv4'): int, 
            Optional('current_egress_non_ipv4'): int, 
            Optional('proposed_egress_non_ipv4'): int, 
            Optional('current_qos_ingress_ipv4'): int, 
            Optional('proposed_qos_ingress_ipv4'): int, 
            Optional('current_qos_ingress_non_ipv4'): int, 
            Optional('proposed_qos_ingress_non_ipv4'): int, 
            Optional('current_qos_egress_ipv4'): int, 
            Optional('proposed_qos_egress_ipv4'): int, 
            Optional('current_qos_egress_non_ipv4'): int, 
            Optional('proposed_qos_egress_non_ipv4'): int, 
            Optional('current_netflow_input_entry'): int, 
            Optional('proposed_netflow_input_entry'): int, 
            Optional('current_netflow_output_entry'): int, 
            Optional('proposed_netflow_output_entry'): int, 
            Optional('current_flow_span_input_entry'): int, 
            Optional('proposed_flow_span_input_entry'): int, 
            Optional('current_flow_span_output_entry'): int, 
            Optional('proposed_flow_span_output_entry'): int, 
            'vlan_count': int, 
            'unicast_mac_addresses_count': int, 
            'overflow_mac_addresses_count': int, 
            'overflow_l2_muticast_entries': int, 
            'l3_muticast_entries': int, 
            'overflow_l3_muticast_entries': int, 
            Optional('ipv4_v6_shared_unicast_routes'): int, 
            Optional('overflow_shared_unicast_routes'): int, 
            'policy_based_routing_aces/nat_aces': int, 
            'tunnels_count': int, 
            'lisp_instance_entries': int, 
            'control_plane_entries': int, 
            'input_netflow_flows': int, 
            'output_netflow_flows': int, 
            'sgt/dgt_or_mpls_vpn_entries': int, 
            'sgt_dgt_vpn_overflow_entries': int, 
            'wired_clients': int, 
            'macsec_spd_entries': int, 
            'vrf_count': int, 
            'mpls_labels': int, 
            'mpls_l3_vpn_routes_vrf_mode': int, 
            'mpls_l3_vpn_routes_prefix_mode': int, 
            'mvpn_mdt_tunnels': int, 
            'l2_vpn_eompls_attachment_circuit': int, 
            'max_vpls_bridge_domains': int, 
            'max_vpls_peers_per_bridge_domain': int, 
            'max_vpls/vpws_pseudowires': int, 
            Optional('vlan_filters_entries'): int
    }
}

class ShowSdmPrefer(ShowSdmPreferSchema):
    """Parser for show sdm prefer"""

    cli_command = 'show sdm prefer'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {} 
        result_dict = {}
        re_dict = {}
        title = '' # to store the title of the this whole data
        # initial regexp pattern for

        # Showing SDM Template Info
        p0 = re.compile(r'^Showing+\s+(?P<template_title>[\w]+)+\s+Template Info+$')

        # "This is the Custom template"
        p1 = re.compile(r'^This is the+\s+(?P<template_type>[\w]+)+\s+template+\.+$')

        #  Security Ingress IPv4 Access Control Entries*:       7168   (current) - 7168   (proposed)
        p2 = re.compile(r'^Security Ingress IPv4 Access Control Entries\*\:+\s+(?P<current_ingress_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_ingress_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  Security Ingress Non-IPv4 Access Control Entries*:   5120   (current) - 5120   (proposed)
        p3 = re.compile(r'^Security Ingress Non-IPv4 Access Control Entries\*\:+\s+(?P<current_ingress_non_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_ingress_non_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  Security Egress IPv4 Access Control Entries*:        7168   (current) - 7168   (proposed)
        p4 = re.compile(r'^Security Egress IPv4 Access Control Entries\*\:+\s+(?P<current_egress_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_egress_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  Security Egress Non-IPv4 Access Control Entries*:    8192   (current) - 8192   (proposed)
        p5 = re.compile(r'^Security Egress Non-IPv4 Access Control Entries\*\:+\s+(?P<current_egress_non_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_egress_non_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  QoS Ingress IPv4 Access Control Entries*:            5632   (current) - 5632   (proposed)
        p6 = re.compile(r'^QoS Ingress IPv4 Access Control Entries\*\:+\s+(?P<current_qos_ingress_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_qos_ingress_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  QoS Ingress Non-IPv4 Access Control Entries*:        2560   (current) - 2560   (proposed)
        p7 = re.compile(r'^QoS Ingress Non-IPv4 Access Control Entries\*\:+\s+(?P<current_qos_ingress_non_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_qos_ingress_non_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  QoS Egress IPv4 Access Control Entries*:             6144   (current) - 6144   (proposed)
        p8 = re.compile(r'^QoS Egress IPv4 Access Control Entries\*\:+\s+(?P<current_qos_egress_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_qos_egress_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  QoS Egress Non-IPv4 Access Control Entries*:         2048   (current) - 2048   (proposed)
        p9 = re.compile(r'^QoS Egress Non-IPv4 Access Control Entries+\*+\:+\s+(?P<current_qos_egress_non_ipv4>[\d]+)+\s+\(current\) -+\s+(?P<proposed_qos_egress_non_ipv4>[\d]+)+\s+\(proposed\)+$')

        #  Netflow Input Access Control Entries*:               512    (current) - 512    (proposed)
        p10 = re.compile(r'^Netflow Input Access Control Entries\*\:+\s+(?P<current_netflow_input_entry>[\d]+)+\s+\(current\) -+\s+(?P<proposed_netflow_input_entry>[\d]+)+\s+\(proposed\)+$')

        #  Netflow Output Access Control Entries*:              512    (current) - 512    (proposed)
        p11 = re.compile(r'^Netflow Output Access Control Entries\*\:+\s+(?P<current_netflow_output_entry>[\d]+)+\s+\(current\) -+\s+(?P<proposed_netflow_output_entry>[\d]+)+\s+\(proposed\)+$')

        #  Flow SPAN Input Access Control Entries*:             512    (current) - 512    (proposed)
        p12 = re.compile(r'^Flow SPAN Input Access Control Entries\*\:+\s+(?P<current_flow_span_input_entry>[\d]+)+\s+\(current\) -+\s+(?P<proposed_flow_span_input_entry>[\d]+)+\s+\(proposed\)+$')

        #   Flow SPAN Output Access Control Entries*:            512    (current) - 512    (proposed)
        p13 = re.compile(r'^Flow SPAN Output Access Control Entries\*\:+\s+(?P<current_flow_span_output_entry>[\d]+)+\s+\(current\) -+\s+(?P<proposed_flow_span_output_entry>[\d]+)+\s+\(proposed\)+$')

        #Number of VLANs:                                      4094
        p14 = re.compile(r'^Number of VLANs+\:+\s+(?P<vlan_count>[\d]+)$')

        # Unicast MAC addresses*:                              98304
        p15 = re.compile(r'^Unicast MAC addresses+\*?\:+\s+(?P<unicast_mac_addresses_count>[\d]+)$')

        # Overflow Unicast MAC addresses*:                     768
        p16 = re.compile(r'^Overflow Unicast MAC addresses+\*?\:+\s+(?P<overflow_mac_addresses_count>[\d]+)$')

        # Overflow L2 Multicast entries*:                      2048
        p17 = re.compile(r'^Overflow L2 Multicast entries+\*?\:+\s+(?P<overflow_l2_muticast_entries>[\d]+)$')

        # L3 Multicast entries*:                               16384
        p18 = re.compile(r'^L3 Multicast entries\*?\:+\s+(?P<l3_muticast_entries>[\d]+)$')

        # Overflow L3 Multicast entries*:                      768
        p19 = re.compile(r'^Overflow L3 Multicast entries\*?\:+\s+(?P<overflow_l3_muticast_entries>[\d]+)$')

        # Ipv4/Ipv6 shared unicast routes*:                    81920
        p20 = re.compile(r'^Ipv4\/Ipv6 shared unicast routes\*?\:+\s+(?P<ipv4_v6_shared_unicast_routes>[\d]+)+$')

        # Overflow shared unicast routes*:                     1536
        p21 = re.compile(r'^Overflow shared unicast routes\*?\:+\s+(?P<overflow_shared_unicast_routes>[\d]+)$')

        # Policy Based Routing ACEs / NAT ACEs*:               3072
        p22 = re.compile(r'^Policy Based Routing ACEs( \/ NAT ACEs)?\*?\:+\s+(?P<policy_based_routing_aces>[\d]+)$')

        # Tunnels*:                                            2816
        p23 = re.compile(r'^Tunnels\*?\:+\s+(?P<tunnels_count>[\d]+)$')

        # LISP Instance Mapping Entries*:                      2048
        p24 = re.compile(r'^LISP Instance Mapping Entries\*?\:+\s+(?P<lisp_instance_entries>[\d]+)$')

        # Control Plane Entries*:                              512
        p25 = re.compile(r'^Control Plane Entries\*?\:+\s+(?P<control_plane_entries>[\d]+)$')

        # Input Netflow flows*:                                49152
        p26 = re.compile(r'^Input Netflow flows\*?\:+\s+(?P<input_netflow_flows>[\d]+)$')

        # Output Netflow flows*:                               49152
        p27 = re.compile(r'^Output Netflow flows\*?\:+\s+(?P<output_netflow_flows>[\d]+)$')

        # SGT/DGT (or) MPLS VPN entries*:                      32768
        p28 = re.compile(r'^SGT\/DGT \(or\) MPLS VPN entries\*?\:+\s+(?P<sgt_dgt_mpls_vpn_entries>[\d]+)$')

        # SGT/DGT (or) MPLS VPN Overflow entries*:             768
        p29 = re.compile(r'^SGT\/DGT \(or\) MPLS VPN Overflow entries\*?\:+\s+(?P<sgt_dgt_vpn_overflow_entries>[\d]+)$')

        # Wired clients:                                       2048
        p30 = re.compile(r'^Wired clients\:+\s+(?P<wired_clients>[\d]+)$')

        # MACSec SPD Entries*:                                 256
        p31 = re.compile(r'^MACSec SPD Entries\*?\:+\s+(?P<macsec_spd_entries>[\d]+)$')

        # VRF:                                                 1024
        p32 = re.compile(r'^VRF\:+\s+(?P<vrf_count>[\d]+)$')

        # MPLS Labels:                                         45056
        p33 = re.compile(r'^MPLS Labels\:+\s+(?P<mpls_labels>[\d]+)$')

        # MPLS L3 VPN Routes VRF Mode*:                        81920
        p34 = re.compile(r'^MPLS L3 VPN Routes VRF Mode\*?\:+\s+(?P<mpls_l3_vrf_mode>[\d]+)$')

        # MPLS L3 VPN Routes Prefix Mode*:                     32768
        p35 = re.compile(r'^MPLS L3 VPN Routes Prefix Mode\*?\:+\s+(?P<mpls_l3_prefix_mode>[\d]+)$')

        # MVPN MDT Tunnels:                                    1024
        p36 = re.compile(r'^MVPN MDT Tunnels\:+\s+(?P<mvpn_mdt_tunnels>[\d]+)$')

        # L2 VPN EOMPLS Attachment Circuit:                    1024
        p37 = re.compile(r'^L2 VPN EOMPLS Attachment Circuit\:+\s+(?P<l2_vpn_eompls_circuit>[\d]+)$')

        # MAX VPLS Bridge Domains :                            1000
        p38 = re.compile(r'^MAX VPLS Bridge Domains \:+\s+(?P<main_vpls_domains>[\d]+)$')

        # MAX VPLS Peers Per Bridge Domain:                    128
        p39 = re.compile(r'^MAX VPLS Peers Per Bridge Domain\:+\s+(?P<max_vpls_peers_domains>[\d]+)$')

        # MAX VPLS/VPWS Pseudowires :                          16384
        p40 = re.compile(r'^MAX VPLS\/VPWS Pseudowires \:+\s+(?P<max_vpls_vpws_pseudowires>[\d]+)$')

        # VLAN Filter Entries:                                 16384
        p41 = re.compile(r'^VLAN Filter Entries\:+\s+(?P<vlan_filters_entries>[\d]+)$')

        # loop to split lines of output
        for line in out.splitlines():
            line = line.strip()

            # Showing SDM Template Info
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                title = str(groups["template_title"]) #putting the title of the data inside the variable 'title'
                result_dict = ret_dict.setdefault(str(groups["template_title"]),{})

            # This is the Custom template.  
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                re_dict = result_dict.setdefault(title,{})
                re_dict.update({"template_type":str(groups['template_type'])})

            # Security Ingress IPv4 Access Control Entries*:       7168   (current) - 7168   (proposed)
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_ingress_ipv4":int(groups['current_ingress_ipv4']),
                "proposed_ingress_ipv4":int(groups['proposed_ingress_ipv4'])})

            # Security Ingress Non-IPv4 Access Control Entries*:   5120   (current) - 5120   (proposed)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_ingress_non_ipv4":int(groups['current_ingress_non_ipv4']),
                "proposed_ingress_non_ipv4":int(groups['proposed_ingress_non_ipv4'])})

            # Security Egress IPv4 Access Control Entries*:        7168   (current) - 7168   (proposed)
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_egress_ipv4":int(groups['current_egress_ipv4']),
                "proposed_egress_ipv4":int(groups['proposed_egress_ipv4'])})

            # Security Egress Non-IPv4 Access Control Entries*:    8192   (current) - 8192   (proposed)
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_egress_non_ipv4":int(groups['current_egress_non_ipv4']),
                "proposed_egress_non_ipv4":int(groups['proposed_egress_non_ipv4'])})

            # QoS Ingress IPv4 Access Control Entries*:            5632   (current) - 5632   (proposed)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_qos_ingress_ipv4":int(groups['current_qos_ingress_ipv4']),
                "proposed_qos_ingress_ipv4":int(groups['proposed_qos_ingress_ipv4'])})
                    
            # QoS Ingress Non-IPv4 Access Control Entries*:        2560   (current) - 2560   (proposed)
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_qos_ingress_non_ipv4":int(groups['current_qos_ingress_non_ipv4']),
                "proposed_qos_ingress_non_ipv4":int(groups['proposed_qos_ingress_non_ipv4'])})

            # QoS Egress IPv4 Access Control Entries*:             6144   (current) - 6144   (proposed)
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_qos_egress_ipv4":int(groups['current_qos_egress_ipv4']),
                "proposed_qos_egress_ipv4":int(groups['proposed_qos_egress_ipv4'])})

            # QoS Egress Non-IPv4 Access Control Entries*:         2048   (current) - 2048   (proposed)
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_qos_egress_non_ipv4":int(groups['current_qos_egress_non_ipv4']),
                "proposed_qos_egress_non_ipv4":int(groups['proposed_qos_egress_non_ipv4'])})

            # Netflow Input Access Control Entries*:               512    (current) - 512    (proposed)
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_netflow_input_entry":int(groups['current_netflow_input_entry']),
                "proposed_netflow_input_entry":int(groups['proposed_netflow_input_entry'])})

            # Netflow Output Access Control Entries*:              512    (current) - 512    (proposed)
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_netflow_output_entry":int(groups['current_netflow_output_entry']),
                "proposed_netflow_output_entry":int(groups['proposed_netflow_output_entry'])})

            # Flow SPAN Input Access Control Entries*:             512    (current) - 512    (proposed)
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_flow_span_input_entry":int(groups['current_flow_span_input_entry']),
                "proposed_flow_span_input_entry":int(groups['proposed_flow_span_input_entry'])})

            # Flow SPAN Output Access Control Entries*:            512    (current) - 512    (proposed)
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"current_flow_span_output_entry":int(groups['current_flow_span_output_entry']),
                "proposed_flow_span_output_entry":int(groups['proposed_flow_span_output_entry'])})

            # Number of VLANs:                                     4094
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"vlan_count":int(groups['vlan_count'])})

            # Unicast MAC addresses*:                              98304
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"unicast_mac_addresses_count":int(groups['unicast_mac_addresses_count'])})

            # Overflow Unicast MAC addresses*:                     768
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"overflow_mac_addresses_count":int(groups['overflow_mac_addresses_count'])})

            # Overflow L2 Multicast entries*:                      2048
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"overflow_l2_muticast_entries":int(groups['overflow_l2_muticast_entries'])})

            # L3 Multicast entries*:                               16384
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"l3_muticast_entries":int(groups['l3_muticast_entries'])})

            # Overflow L3 Multicast entries*:                      768
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"overflow_l3_muticast_entries":int(groups['overflow_l3_muticast_entries'])})

            # Ipv4/Ipv6 shared unicast routes*:                    81920
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"ipv4_v6_shared_unicast_routes":int(groups['ipv4_v6_shared_unicast_routes'])})

            # Overflow shared unicast routes*:                     1536
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"overflow_shared_unicast_routes":int(groups['overflow_shared_unicast_routes'])})

            # Policy Based Routing ACEs / NAT ACEs*:               3072
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"policy_based_routing_aces/nat_aces":int(groups['policy_based_routing_aces'])})

            # Tunnels*:                                            2816
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"tunnels_count":int(groups['tunnels_count'])})

            # LISP Instance Mapping Entries*:                      2048
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"lisp_instance_entries":int(groups['lisp_instance_entries'])})

            # Control Plane Entries*:                              512
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"control_plane_entries":int(groups['control_plane_entries'])})

            # Input Netflow flows*:                                49152
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"input_netflow_flows":int(groups['input_netflow_flows'])})

            # Output Netflow flows*:                               49152
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"output_netflow_flows":int(groups['output_netflow_flows'])})

            # SGT/DGT (or) MPLS VPN entries*:                      32768
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"sgt/dgt_or_mpls_vpn_entries":int(groups['sgt_dgt_mpls_vpn_entries'])})

            # SGT/DGT (or) MPLS VPN Overflow entries*:             768
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"sgt_dgt_vpn_overflow_entries":int(groups['sgt_dgt_vpn_overflow_entries'])})

            # Wired clients:                                       2048
            m = p30.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"wired_clients":int(groups['wired_clients'])})

            # MACSec SPD Entries*:                                 256
            m = p31.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"macsec_spd_entries":int(groups['macsec_spd_entries'])})

            # VRF:                                                 1024
            m = p32.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"vrf_count":int(groups['vrf_count'])})

            # MPLS Labels:                                         45056
            m = p33.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"mpls_labels":int(groups['mpls_labels'])})

            # MPLS L3 VPN Routes VRF Mode*:                        81920
            m = p34.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"mpls_l3_vpn_routes_vrf_mode":int(groups['mpls_l3_vrf_mode'])})

            # MPLS L3 VPN Routes Prefix Mode*:                     32768
            m = p35.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"mpls_l3_vpn_routes_prefix_mode":int(groups['mpls_l3_prefix_mode'])})

            # MVPN MDT Tunnels:                                    1024
            m = p36.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"mvpn_mdt_tunnels":int(groups['mvpn_mdt_tunnels'])})

            # L2 VPN EOMPLS Attachment Circuit:                    1024
            m = p37.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"l2_vpn_eompls_attachment_circuit":int(groups['l2_vpn_eompls_circuit'])})
                        
            # MAX VPLS Bridge Domains :                            1000
            m = p38.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"max_vpls_bridge_domains":int(groups['main_vpls_domains'])})
                
            # MAX VPLS Peers Per Bridge Domain:                    128
            m = p39.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"max_vpls_peers_per_bridge_domain":int(groups['max_vpls_peers_domains'])})
                        
            # MAX VPLS/VPWS Pseudowires :                          16384
            m = p40.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"max_vpls/vpws_pseudowires":int(groups['max_vpls_vpws_pseudowires'])})
                
            # VLAN Filter Entries:                                 16384
            m = p41.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({"vlan_filters_entries":int(groups['vlan_filters_entries'])})
                
        return result_dict

class ShowSdmPreferCustomSchema(MetaParser):
    """Schema for show sdm prefer"""
    schema = {
        'template_title': str,
        'template_type': str, #template used 
        Optional('ipv4/ipv6_shared_unicast_routes'): int,
        Optional('wired_clients'): int,
        Optional('mpls_labels'): int,
        Optional('max_vpls/vpws_pseudowires'): int,
        Optional('qos_egress_non-ipv4_access_control_entries'): int,
        Optional('netflow_input_access_control_entries'): int,
        Optional('max_vpls_bridge_domains'): int,
        Optional('qos_ingress_ipv4_access_control_entries'): int,
        Optional('sgt/dgt_(or)_mpls_vpn_entries'): int,
        Optional('number_of_vlans'): int,
        Optional('l2_vpn_eompls_attachment_circuit'): int,
        Optional('max_vpls_peers_per_bridge_domain'): int,
        Optional('l2_multicast_entries'): int,
        Optional('l3_multicast_entries'): int,
        Optional('overflow_unicast_mac_addresses'): int,
        Optional('input_netflow_flows'): int,
        Optional('netflow_output_access_control_entries'): int,
        Optional('mpls_l3_vpn_routes_vrf_mode'): int,
        Optional('flow_span_output_access_control_entries'): int,
        Optional('mpls_l3_vpn_routes_prefix_mode'): int,
        Optional('security_ingress_non-ipv4_access_control_entries'): int,
        Optional('tunnels'): int,
        Optional('control_plane_entries'): int,
        Optional('output_netflow_flows'): int,
        Optional('policy_based_routing_aces_/_nat_aces'): int,
        Optional('mvpn_mdt_tunnels'): int,
        Optional('unicast_mac_addresses'): int,
        Optional('overflow_l2_multicast_entries'): int,
        Optional('overflow_l3_multicast_entries'): int,
        Optional('sgt/dgt_(or)_mpls_vpn_overflow_entries'): int,
        Optional('lisp_instance_mapping_entries'): int,
        Optional('security_egress_non-ipv4_access_control_entries'): int,
        Optional('qos_ingress_non-ipv4_access_control_entries'): int,
        Optional('security_egress_ipv4_access_control_entries'): int,
        Optional('macsec_spd_entries'): int,
        Optional('overflow_shared_unicast_routes'): int,
        Optional('qos_egress_ipv4_access_control_entries'): int,
        Optional('flow_span_input_access_control_entries'): int,
        Optional('vrf'): int,
        Optional('security_ingress_ipv4_access_control_entries'): int
    }

# ===================================================
# Parser for 'show sdm prefer custom'
# ===================================================
class ShowSdmPreferCustom(ShowSdmPreferCustomSchema):
    """Parser for show sdm prefer custom"""

    cli_command = 'show sdm prefer custom'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        result_dict = {}

        # Showing SDM Template Info
        p0 = re.compile(r'^Showing+\s+(?P<template_title>[\w]+)+\s+Template Info+$')

        # "This is the Custom template"
        p1 = re.compile(r'^This is the+\s+(?P<template_type>[\w]+)+\s+template+\.?$')

        # initial regexp pattern
        p2 = re.compile(r'^(?P<pattern>[\S \* ]+): +(?P<value>\d+) ?((?P<pattern1>[\w\s\(\)]+) [\-] (?P<value1>\d+) (?P<pattern2>[\w\s\(\)]+))?$')

        # loop to split lines of output
        for line in output.splitlines():
            line = line.strip()

            # Showing SDM Template Info
            m = p0.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'template_title': group['template_title']})
                continue

            # This is the Custom template.  
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'template_type': group['template_type']})
                continue

            # Number of VLANs: 4094
            m = p2.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_').replace('*', '')
                result_dict.update({scrubbed.lower(): int(group['value'])})
                continue

        return result_dict
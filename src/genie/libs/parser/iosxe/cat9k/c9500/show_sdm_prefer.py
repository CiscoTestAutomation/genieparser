"""show_sdm_prefer.py
   supported commands:
     *  show sdm prefer
     *  show sdm prefer custom
"""
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# =======================================================================
# Schema for 'show sdm prefer' for 9500 device
# =======================================================================
class ShowSdmPreferNewSchema(MetaParser):
    """Schema for :
        'show sdm prefer'
        'show sdm prefer custom'
    """
    schema = {
        str:
            {
                Optional('template_type'): str,
                Optional('feature_name'): str,
                Optional('unicast_mac_addresses'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        Optional('resource_programmed'): str,
                },
                Optional('fib_host_route'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        Optional('resource_programmed'): str,
                },
                Optional('og_sgacl_hosts_cells'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        Optional('resource_programmed'): str,
                },
                Optional('l3_multicast_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('l2_multicast_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('number_of_vlans'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('overflow_unicast_mac_addresses'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('overflow_l2_multicast_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('overflow_l3_multicast_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('ipv4_ipv6_shared_unicast_routes'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('overflow_shared_unicast_routes'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('stp_instances'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('tunnels'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('vrf'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_mpls_vpn_routes_per_vrf_label_mode'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_mpls_vpn_routes_per_prefix_label_mode'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_l3_adjacency'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_l3_interface'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_mpls_te_tunnel'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_mpls_label'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                # Core template fields
                Optional('security_ingress_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('security_ingress_non_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('security_egress_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('security_egress_non_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('qos_ingress_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('qos_ingress_non_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('qos_egress_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('qos_egress_non_ipv4_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('netflow_input_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('netflow_output_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('flow_span_input_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('flow_span_output_access_control_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('policy_based_routing_aces_nat_aces'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('lisp_instance_mapping_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('control_plane_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('input_netflow_flows'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('output_netflow_flows'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('sgt_dgt_or_mpls_vpn_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('sgt_dgt_or_mpls_vpn_overflow_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('wired_clients'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('macsec_spd_entries'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('mpls_labels'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('mpls_l3_vpn_routes_vrf_mode'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('mpls_l3_vpn_routes_prefix_mode'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('mvpn_mdt_tunnels'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('l2_vpn_eompls_attachment_circuit'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_vpls_bridge_domains'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_vpls_peers_per_bridge_domain'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('max_vpls_vpws_pseudowires'):
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                Optional('em'): int,
            },
        Optional('scale'):
            {
                'em': int
        }
    }

# ==============================================
# Parser for 'show sdm prefer' for 9500 devices
# ==============================================
class ShowSdmPreferNew(ShowSdmPreferNewSchema):
    """Parser for show sdm prefer and show sdm prefer custom"""
    cli_command = ['show sdm prefer {custom}', 'show sdm prefer']

    def cli(self, custom='', output=None):

        # initial regexp pattern for
        result_dict = {}
        re_dict = {}
        title = '' # to store the title of the this whole data

        # loop to split lines of output
        if output is None:
            if custom:
                cmd = self.cli_command[0].format(custom=custom)
            else:
                cmd = self.cli_command[1]
            
            output = self.device.execute(cmd)

        # Showing SDM Template Info
        p0 = re.compile(r'^Showing+\s+(?P<template_title>[\w]+)+\s+Template Info+$')

        # "This is the Custom template"
        p1 = re.compile(r'^This is the+\s+(?P<template_type>[\w]+)+\s+template+\.+$')

        # Feature-Name                                        Reserved-Scale
        p2 = re.compile(r'^Feature-Name(?:\s*)(?P<feature_name>\S*)$')

        # Unicast MAC addresses                               262144
        # FIB Host Route                                      262144
        # OG/SGACL Hosts/Cells                                32768
        # Unicast MAC addresses:                              32768
        p3 = re.compile(r'^(?P<feature>Unicast MAC addresses|FIB Host Route|OG\/SGACL Hosts\/Cells)\s*:?(?:\s*)(?P<number_feature>\d+)$')

        # Unicast MAC addresses*                              131072 (current) - 262144 (proposed)
        # FIB Host Route*                                     131072 (current) - 262144 (proposed)
        # OG/SGACL Hosts/Cells*                               32768  (current) - 32768  (proposed)
        # Unicast MAC addresses*:                             32768  (current) - 32768  (proposed)
        p3_1 = re.compile(r'^(?P<feature>Unicast MAC addresses|FIB Host Route|OG\/SGACL Hosts\/Cells)\*\s*:?(?:\s*)'
                            r'(?P<current_feature>\d+)\s*\(current\)\s*-\s*(?P<proposed_feature>\d+)\s*\(proposed\)$')

        # Resource-Programmed: EM
        p4 = re.compile(r'^Resource-Programmed:(?:\s*)(?P<em>\w*)$')

        # Resource scale information
        p6 = re.compile(r'^Resource\s(?P<resource_scale>\w*)\sinformation$')

        # EM                                                  622592
        p7 = re.compile(r'^EM(?:\s*)(?P<em_number>\d*)$')

        # Generic feature line with current/proposed values. Matches lines like:
        # L3 Multicast entries*                               32768  (current) - 32768  (proposed) (**)
        # Security Ingress IPv4 Access Control Entries*:      7168   (current) - 7168   (proposed)
        # Security Ingress Non-IPv4 Access Control Entries*: 5120   (current) - 5120   (proposed)
        # Security Egress IPv4 Access Control Entries*:      7168   (current) - 7168   (proposed)
        # Security Egress Non-IPv4 Access Control Entries*:  8192   (current) - 8192   (proposed)
        # QoS Ingress IPv4 Access Control Entries*:          5632   (current) - 5632   (proposed)
        # QoS Ingress Non-IPv4 Access Control Entries*:      2560   (current) - 2560   (proposed)
        # QoS Egress IPv4 Access Control Entries*:           6144   (current) - 6144   (proposed)
        # QoS Egress Non-IPv4 Access Control Entries*:       2048   (current) - 2048   (proposed)
        # Netflow Input Access Control Entries*:             512    (current) - 512    (proposed)
        # Netflow Output Access Control Entries*:            512    (current) - 512    (proposed)
        # Flow SPAN Input Access Control Entries*:           512    (current) - 512    (proposed)
        # Flow SPAN Output Access Control Entries*:          512    (current) - 512    (proposed)
        # Policy Based Routing ACEs / NAT ACEs*:             3072   (current) - 3072   (proposed)
        # LISP Instance Mapping Entries*:                    2048   (current) - 2048   (proposed)
        # Control Plane Entries*:                            512    (current) - 512    (proposed)
        # Input Netflow flows*:                              49152  (current) - 49152  (proposed)
        # Output Netflow flows*:                             49152  (current) - 49152  (proposed)
        # SGT/DGT (or) MPLS VPN entries*:                    32768  (current) - 32768  (proposed)
        # SGT/DGT (or) MPLS VPN Overflow entries*:           768    (current) - 768    (proposed)
        # Wired clients*:                                    2048   (current) - 2048   (proposed)
        # MACSec SPD Entries*:                               256    (current) - 256    (proposed)
        # VRF*:                                              1024   (current) - 1024   (proposed)
        # MPLS Labels*:                                      45056  (current) - 45056  (proposed)
        # MPLS L3 VPN Routes VRF Mode*:                      81920  (current) - 81920  (proposed)
        # MPLS L3 VPN Routes Prefix Mode*:                   32768  (current) - 32768  (proposed)
        # MVPN MDT Tunnels*:                                 1024   (current) - 1024   (proposed)
        # L2 VPN EOMPLS Attachment Circuit*:                 1024   (current) - 1024   (proposed)
        # MAX VPLS Bridge Domains*:                          1000   (current) - 1000   (proposed)
        # MAX VPLS Peers Per Bridge Domain*:                 128    (current) - 128    (proposed)
        # MAX VPLS/VPWS Pseudowires*:                        16384  (current) - 16384  (proposed)
        p5 = re.compile(r'^(?P<type>[A-Za-z][A-Za-z0-9 /()\-]*?)\s*\*\s*:?\s+'
                        r'(?P<current_l>\d+)\s*\(current\)\s*-\s*'
                        r'(?P<proposed_l>\d+)\s*\(proposed\)\s*(?:\(\*+\))?$')

        # Generic feature line (proposed only). Matches lines like:
        # L3 Multicast entries                                32768 (**)
        # Number of VLANs:                                    4094
        # Policy Based Routing ACEs / NAT ACEs:               3072
        # SGT/DGT (or) MPLS VPN entries:                      32768
        # MAX VPLS Bridge Domains :                           1000
        p5_1 = re.compile(r'^(?P<type>[A-Za-z][A-Za-z0-9 /()\-]*?)\s*:?\s+'
                          r'(?P<input_number>\d+)\s*(?:\(\*+\))?$')

        def _normalize_key(name):
            key = re.sub(r'[^a-z0-9]+', '_', name.lower())
            return key.strip('_')

        def _ensure_re_dict():
            nonlocal title, re_dict, result_dict
            if not title:
                title = 'sdm'
                result_dict = result_dict.setdefault(title, {})
                re_dict = result_dict
            elif not re_dict:
                re_dict = result_dict.setdefault(title, {})
            return re_dict

        # loop to split lines of output
        for line in output.splitlines():
            line = line.strip()

            # Showing SDM Template Info
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                title = groups['template_title'] #putting the title of the data inside the variable 'title'
                result_dict = result_dict.setdefault(groups['template_title'],{})
                continue

            # This is the Custom template.  
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                re_dict = result_dict.setdefault(title,{})
                re_dict.update({'template_type': groups['template_type']})
                continue

            # Feature-Name                                        Reserved-Scale
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                re_dict.update({'feature_name':str(groups['feature_name'])})
                continue
            
            #Unicast MAC addresses                               262144
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                _ensure_re_dict()
                feature = _normalize_key(groups['feature'])
                feature_dict = re_dict.setdefault(feature, {})
                feature_dict.update({
                    'proposed': int(groups['number_feature']),
                })
                continue

            #Unicast MAC addresses*                              131072 (current) - 262144 (proposed)
            m = p3_1.match(line)
            if m:
                groups = m.groupdict()
                _ensure_re_dict()
                feature = _normalize_key(groups['feature'])
                feature_dict = re_dict.setdefault(feature, {})
                feature_dict.update({
                    'current': int(groups['current_feature']),
                    'proposed': int(groups['proposed_feature']),
                })
                continue

            #Resource-Programmed: EM
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                re_dict.setdefault(feature, {}).update({
                    'resource_programmed': str(groups['em']),
                })
                continue

            #Resource scale information
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                result_dict.setdefault('scale',{})
                continue

            #EM                                                  622592
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                result_dict.setdefault('scale',{}).update({'em':int(groups['em_number'])})
                continue

            # L3 Multicast entries*                              32768  (current) - 32768  (proposed) (**)
            # Security Ingress IPv4 Access Control Entries*:     7168   (current) - 7168   (proposed)
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sdm_type = _normalize_key(groups['type'])
                if not sdm_type:
                    continue
                _ensure_re_dict()
                re_dict.setdefault(sdm_type, {}).update({
                    'current':int(groups['current_l']),
                    'proposed':int(groups['proposed_l']),
                })
                continue

            # L3 Multicast entries                               32768 (**)
            # Number of VLANs:                                   4094
            # Policy Based Routing ACEs / NAT ACEs:              3072
            m = p5_1.match(line)
            if m:
                groups = m.groupdict()
                sdm_type = _normalize_key(groups['type'])
                if not sdm_type:
                    continue
                _ensure_re_dict()
                re_dict.setdefault(sdm_type, {}).update({'proposed':int(groups['input_number'])})
                continue

        return result_dict

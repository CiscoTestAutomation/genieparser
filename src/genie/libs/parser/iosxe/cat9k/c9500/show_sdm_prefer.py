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
                'template_type': str, 
                'feature_name': str,
                'unicast_mac_addresses':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        'resource_programmed': str,
                },
                'fib_host_route':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        'resource_programmed': str,
                },
                'og_sgacl_hosts_cells':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                        'resource_programmed': str,
                },
                'l3_multicast_entries':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'l2_multicast_entries':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'number_of_vlans':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'overflow_unicast_mac_addresses':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'overflow_l2_multicast_entries':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'overflow_l3_multicast_entries':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'ipv4_ipv6_shared_unicast_routes':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'overflow_shared_unicast_routes':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'stp_instances':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'tunnels':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'vrf':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'max_mpls_vpn_routes_per_vrf_label_mode':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'max_mpls_vpn_routes_per_prefix_label_mode':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'max_l3_adjacency':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'max_l3_interface':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                },
                'max_mpls_te_tunnel':
                    {
                        Optional('current'): int,
                        Optional('proposed'): int,
                }          
        },
        'scale': 
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
        p3 = re.compile(r'^(?P<feature>Unicast MAC addresses|FIB Host Route|OG\/SGACL Hosts\/Cells)(?:\s*)(?P<number_feature>\d*)$')

        # Unicast MAC addresses*                              131072 (current) - 262144 (proposed)
        # FIB Host Route*                                     131072 (current) - 262144 (proposed)
        # OG/SGACL Hosts/Cells*                               32768  (current) - 32768  (proposed)
        p3_1 = re.compile(r'^(?P<feature>Unicast MAC addresses|FIB Host Route|OG\/SGACL Hosts\/Cells)\S(?:\s*)'
                            r'(?P<current_feature>\d*)(?:\s*\Scurrent\S)(?:\s*-\s*)(?P<proposed_feature>\d*)(?:\s*\Sproposed\S)$')

        # Resource-Programmed: EM
        p4 = re.compile(r'^Resource-Programmed:(?:\s*)(?P<em>\w*)$')

        # L3 Multicast entries                                32768 (**)
        # L2 Multicast entries                                16384 (**)
        # Number of VLANs                                     4094 (**)
        # Overflow Unicast MAC addresses                      512 (**)
        # Overflow L2 Multicast entries                       512 (**)
        # Overflow L3 Multicast entries                       512 (**)
        # Ipv4/Ipv6 shared unicast routes                     262144 (**)
        # Overflow shared unicast routes                      2000000 (**)
        # STP Instances                                       4094 (**)
        # Tunnels                                             1024 (**)
        # VRF                                                 3840 (**)
        # Max MPLS VPN Routes Per-Vrf label mode              2000000 (**)
        # Max MPLS VPN Routes Per-Prefix label mode           65536 (**)
        # Max L3 adjacency                                    131072 (**)
        # Max L3 Interface                                    8192 (**)
        # Max MPLS TE TUNNEL                                  4096 (**)
        p5 = re.compile(r'^(?P<type>L3 Multicast entries|L2 Multicast entries|Number of VLANs|'
                        r'Overflow Unicast MAC addresses|Overflow L2 Multicast entries|Overflow L3 Multicast entries|'
                        r'Ipv4\/Ipv6 shared unicast routes|Overflow shared unicast routes|STP Instances|Tunnels|VRF|'
                        r'Max MPLS VPN Routes Per-Vrf label mode|Max MPLS VPN Routes Per-Prefix label mode|Max L3 adjacency|'
                        r'Max L3 Interface|Max MPLS TE TUNNEL)(?:\s*)(?P<input_number>\d*)(?:\s*\S*)$')

        #L3 Multicast entries*                               32768  (current) - 32768  (proposed) (**)
        #L2 Multicast entries*                               16384  (current) - 16384  (proposed) (**)
        p5_1 = re.compile(r'^(?P<type_1>L3 Multicast entries\S|L2 Multicast entries\S|Number of VLANs\S|'
                        r'Overflow Unicast MAC addresses\S|Overflow L2 Multicast entries\S|Overflow L3 Multicast entries\S|'
                        r'Ipv4\/Ipv6 shared unicast routes\S|Overflow shared unicast routes\S|STP Instances\S|Tunnels\S|VRF\S|'
                        r'Max MPLS VPN Routes Per-Vrf label mode\S|Max MPLS VPN Routes Per-Prefix label mode\S|Max L3 adjacency\S|'
                        r'Max L3 Interface\S|Max MPLS TE TUNNEL\S)(?:\s*)(?P<current_l>\d*)(?:\s*\Scurrent\S)(?:\s*-\s*)'
                        r'(?P<proposed_l>\d*)(?:\s*\Sproposed\S)(?:\s*\S*)$')

        #Resource scale information
        p6 = re.compile(r'^Resource\s(?P<resource_scale>\w*)\sinformation$')

        #EM                                                  622592
        p7 = re.compile(r'^EM(?:\s*)(?P<em_number>\d*)$')

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
                feature = groups['feature'].lower().replace(' ', '_').replace('/', '_')
                feature_dict = re_dict.setdefault(feature, {})
                feature_dict.update({
                    'proposed': int(groups['number_feature']),
                })
                continue

            #Unicast MAC addresses*                              131072 (current) - 262144 (proposed)
            m = p3_1.match(line)
            if m:
                groups = m.groupdict()
                feature = groups['feature'].lower().replace(' ', '_').replace('/', '_')
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
                    
            # L3 Multicast entries                                32768 (**)
            # L2 Multicast entries                                16384 (**)
            # Number of VLANs                                     4094 (**)
            # Overflow Unicast MAC addresses                      512 (**)
            # Overflow L2 Multicast entries                       512 (**)
            # Overflow L3 Multicast entries                       512 (**)
            # Ipv4/Ipv6 shared unicast routes                     262144 (**)
            # Overflow shared unicast routes                      2000000 (**)
            # STP Instances                                       4094 (**)
            # Tunnels                                             1024 (**)
            # VRF                                                 3840 (**)
            # Max MPLS VPN Routes Per-Vrf label mode              2000000 (**)
            # Max MPLS VPN Routes Per-Prefix label mode           65536 (**)
            # Max L3 adjacency                                    131072 (**)
            # Max L3 Interface                                    8192 (**)
            # Max MPLS TE TUNNEL                                  4096 (**)
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sdm_type = m.groupdict()['type'].lower().replace(' ', '_').replace('-', '_').replace('/', '_')
                re_dict.setdefault(sdm_type, {}).update({'proposed':int(groups['input_number'])})
                continue

            #L3 Multicast entries*                               32768  (current) - 32768  (proposed) (**)
            #L2 Multicast entries*                               16384  (current) - 16384  (proposed) (**)
            m = p5_1.match(line)
            if m:
                groups = m.groupdict()
                sdm_type = m.groupdict()['type_1'].lower().replace(' ', '_').replace('-', '_').replace('*', '')
                re_dict.setdefault(sdm_type, {}).update({
                    'current':int(groups['current_l']),
                    'proposed':int(groups['proposed_l']),
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
        
        return result_dict

"""show_vpc.py

Parser for the following show commands:
    * show vpc
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


# ========================================
# Schema for "show vpc"
# ========================================

class ShowVpcSchema(MetaParser):
    """Schema for "show vpc"""

    schema = {
        'vpc_domain_id': str,
        'vpc_peer_status': str,
        Optional('vpc_plus_switch_id'): str,
        'vpc_peer_keepalive_status': str,
        Optional('vpc_fabricpath_status'): str,
        'vpc_configuration_consistency_status': str,
        Optional('vpc_configuration_consistency_reason'): str,
        Optional('vpc_per_vlan_consistency_status'): str,        
        Optional('vpc_type_2_consistency_status'): str,
        Optional('vpc_role'): str,
        'num_of_vpcs': int,
        Optional('peer_gateway'): str,
        Optional('peer_gateway_exculded_bridge_domains'): str,
        Optional('delay_restore_orphan_ports_status'): {
            'timer': str,
            'timeout_sec': int,
        },
        Optional('dual_active_excluded_vlans_and_bds'): str,
        Optional('peer_gateway_exculded_vlans'): str,
        Optional('self_isolation'): str,
        Optional('dual_active_excluded_vlans'): str,
        Optional('vpc_graceful_consistency_check_status'): str,
        Optional('vpc_auto_recovery_status'): str,
        Optional('vpc_delay_restore_status'): str,
        Optional('vpc_delay_restore_svi_status'): str,
        Optional('operational_l3_peer_router'): str,
        Optional('track_object'): int,
        Optional('peer_link'): {
            Any(): {
                'peer_link_id': int,
                'peer_link_ifindex': str,
                'peer_link_port_state': str,
                'peer_up_vlan_bitset': str,
                Optional('vlan_bds'): str,
            }
        },
        Optional('vpc'): {
            Any(): {
                'vpc_id': int,
                'vpc_ifindex': str,
                'vpc_port_state': str,
                'vpc_consistency': str,
                'vpc_consistency_status': str,
                'up_vlan_bitset': str,
                Optional('vpc_plus_attrib'): str
            }
        }
    }


# ========================================
# Parser for "show vpc"
# ========================================
class ShowVpc(ShowVpcSchema):
    """Parser for show vpc"""

    cli_command = "show vpc"
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        up_vlan_bitset = peer_up_vlan_bitset = ''
        vlan_type = None
        vpc_dict = {}
        # vPC domain id                     : 1
        # vPC domain id                     : Not configured
        p1 = re.compile(r'^vPC +domain +id\s*: +(?P<domain_id>[\w\s]+)$')

        # Peer status                       : peer adjacency formed ok 
        p2 = re.compile(r'^Peer +status\s*: +(?P<peer_status>[\S\s]+)$')

        # vPC keep-alive status             : peer is alive 
        p3 = re.compile(r'^vPC +keep-alive +status\s*: +(?P<keepalive_status>[\S\s]+)$')

        # Configuration consistency status  : success
        # Configuration consistency status: success
        p4 = re.compile(r'^Configuration +consistency +status\s*: '
            '+(?P<config_status>[\S\s]+)$')

        # Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
        p5 = re.compile(r'^Configuration +consistency +reason\s*: '
            '+(?P<config_status_reason>[\S\s]+)$')

        # Per-vlan consistency status       : success 
        p6 = re.compile(r'^Per-vlan +consistency +status\s*: '
            '+(?P<per_vlan_status>[\S\s]+)$')

        # Type-2 consistency status         : success 
        p7 = re.compile(r'^Type-2 +consistency +status\s*: '
            '+(?P<type_2_status>[\S\s]+)$')

        # vPC role                          : primary  
        p8 = re.compile(r'^vPC +role\s*: +(?P<vpc_role>[\S\s]+)$')

        # Number of vPCs configured         : 1 
        p9 = re.compile(r'Number +of +(vPC|vPCs) +configured\s*: +(?P<num_of_vpc>\d+)$')

        # Peer Gateway                      : Enabled
        p10 = re.compile(r'^Peer +Gateway\s*: +(?P<peer_gateway>[\S\s]+)$')

        # Dual-active excluded VLANs        : -       
        p11 = re.compile(r'^Dual-active +excluded +VLANs\s*: '
            '+(?P<dual_active_excluded_vlan>[\S\s]+)$')

        # Graceful Consistency Check        : Enabled
        p12 = re.compile(r'^Graceful +Consistency +Check\s*: '
            '+(?P<graceful_check>[\S\s]+)$')

        # Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
        p13 = re.compile(r'^Auto-recovery +status\s*: '
            '+(?P<auto_recovery_status>[\S\s]+)$')

        # Delay-restore status              : Timer is off.(timeout = 30s)
        p14 = re.compile(r'^Delay-restore +status\s*: '
            '+(?P<delay_recovery_status>[\S\s]+)$')

        # Delay-restore SVI status          : Timer is off.(timeout = 10s)
        p15 = re.compile(r'^Delay-restore +SVI +status\s*: '
            '+(?P<delay_svi_recovery_status>[\S\s]+)$')

        # Operational Layer3 Peer-router    : Disabled
        p16 = re.compile(r'^Operational +Layer3 +Peer-router\s*: '
            '+(?P<layer3_peer_router>[\S\s]+)$')

        # Track object : 12
        p17 = re.compile(r'^Track +object\s*: +(?P<track_object>\d+)$')

        # 1 Po10 up 1-100
        # 1     Po101  up     1,100-102,200-
        # 1 Po10 up 1-100
        # 1 Po100 down -
        # 1    Po1    up     1,8,17,60-62,65,67-68,92-93,11 -
        # 1     Po101  up     1,100-102,200-202
        p18 = re.compile(r'^(?P<peer_link_id>\d+) +(?P<peer_link_ifindex>\S+) +'
                r'(?P<peer_link_port_state>\S+) +(?P<peer_up_vlan_bitset>-|\S+)'
                r'( +(?P<vlan_bds>-|\S+))?$')

        # 1     Po1           up     success     success               1,100-102,200-
        # 20 Po20 up failed vPC type-1 configuration -
        # 1 Po1 down success success -
        # 11 Po11 up success success 1,10-28,30-5 DF: Partial
        p19 = re.compile(r'^(?P<vpc_id>\d+) +(?P<vpc_ifindex>\S+) '
            '+(?P<vpc_port_state>\S+) +(?P<vpc_consistency>\S+) '
            '+(?P<vpc_consistency_status>success|[\S\s]+) '
            '+(?P<up_vlan_bitset>[\d\,\-]+)'
            '(?: +(?P<vpc_plus_attrib>(.*)+))?$')
        # vPC Peer-link status
        p20 = re.compile(r'^vPC +(p|P)eer-link +status$')

        # vPC status
        p21 = re.compile(r'^vPC +status$')

        # Id               : 4
        p22 = re.compile(r'^Id +: +(?P<vpc_id>\d+)$')

        # Port           : Po4
        p23 = re.compile(r'^Port +: +(?P<vpc_ifindex>\S+)$')

        # Status         : up
        p24 = re.compile(r'^Status +: +(?P<vpc_port_state>\S+)$')

        # Consistency    : success
        p25 = re.compile(r'^Consistency +: +(?P<vpc_consistency>\S+)$')

        # Reason         : success
        # Reason         : Compatibility check failed for speed
        p26 = re.compile(r'^Reason +: +(?P<vpc_consistency_status>[\S ]+)$')

        # Active Vlans   : 65,67-68,401-402,1199
        p27 = re.compile(r'^Active +Vlans +: +(?P<up_vlan_bitset>\S+)$')

        # Peer gateway excluded VLANs            : -
        p28 = re.compile(r'^Peer +gateway +excluded +VLANs +: +(?P<peer_gateway_exculded_vlans>\S+)$')

        # Peer gateway excluded bridge-domains   : -
        p29 = re.compile(r'^Peer +gateway +excluded +bridge-domains +: +(?P<peer_gateway_exculded_bridge_domains>\S+)$')

        # Dual-active excluded VLANs and BDs     : -
        p30 = re.compile(r'^Dual-active +excluded +VLANs +and +BDs +: +(?P<dual_active_excluded_vlans_and_bds>\S+)$')

        # Delay-restore orphan ports status      : Timer is off.(timeout = 0s)
        p31 = re.compile(r'^Delay-restore +orphan +ports +status +: +(Timer +is +(?P<timer>\w+))\.\(timeout += +(?P<timeout>\d+)s\)$')

        # Self-isolation                         : Disabled
        p32 = re.compile(r'^Self-isolation +: +(?P<self_isolation>\S+)$')

        # 200
        # 300-330, 350, 400-500
        
        p33 = re.compile(r'^(?P<additional_vlan>(?!--)[\d\,\-]+)$')
        
        # vPC+ switch id : 312
        p34 = re.compile(r'^vPC[+] +switch +id\s*: +(?P<vpc_plus_switch_id>[\w\s]+)$')

        # vPC fabricpath status : peer is reachable through fabricpath
        p35 = re.compile(r'^vPC+ fabricpath+ status\s*: +(?P<vpc_fabricpath_status>[\w\s]+)$')

        # 4,56-82,138, FP MAC:
        # 530,2587     312.0.0
        p36 = re.compile(r'^(?P<additional_vlan>[\d\-\,]+) (?P<additional_vpc_plus_attrib>[\S\-\,\s\.\:]+)$')
        for line in output.splitlines():
            line = line.strip()

            # vPC domain id                     : 1
            match = p1.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_domain_id': group['domain_id']})
                continue

            # Peer status                       : peer adjacency formed ok 
            match = p2.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_peer_status': group['peer_status']})
                continue

            # vPC keep-alive status             : peer is alive 
            match = p3.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_peer_keepalive_status': group['keepalive_status']})
                continue

            # Configuration consistency status  : success
            # Configuration consistency status: success
            match = p4.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_configuration_consistency_status': group['config_status']})
                continue

            # Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
            match = p5.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_configuration_consistency_reason': group['config_status_reason']})
                continue

            # Per-vlan consistency status       : success 
            match = p6.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_per_vlan_consistency_status': group['per_vlan_status']})
                continue

            # Type-2 consistency status         : success 
            match = p7.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_type_2_consistency_status': group['type_2_status']})
                continue

            # vPC role                          : primary
            match = p8.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_role': group['vpc_role']})
                continue

            # Number of vPCs configured         : 1 
            match = p9.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'num_of_vpcs': int(group['num_of_vpc'])})
                continue

            # Peer Gateway                      : Enabled
            match = p10.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'peer_gateway': group['peer_gateway']})
                continue

            # Dual-active excluded VLANs        : -   
            match = p11.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'dual_active_excluded_vlans': group['dual_active_excluded_vlan']})
                continue

            # Graceful Consistency Check        : Enabled
            match = p12.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_graceful_consistency_check_status': group['graceful_check']})
                continue

            # Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
            match = p13.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_auto_recovery_status': group['auto_recovery_status']})
                continue

            # Delay-restore status              : Timer is off.(timeout = 30s)
            match = p14.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_delay_restore_status': group['delay_recovery_status']})
                continue

            # Delay-restore SVI status          : Timer is off.(timeout = 10s)
            match = p15.match(line)
            if match:
                group = match.groupdict()
                ret_dict \
                .update({'vpc_delay_restore_svi_status': group['delay_svi_recovery_status']})
                continue

            # Operational Layer3 Peer-router    : Disabled
            match = p16.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'operational_l3_peer_router': group['layer3_peer_router']})
                continue

            # Track object : 12
            match = p17.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'track_object': int(group['track_object'])})
                continue            
            
            # 1     Po101  up     1,100-102,200-202
            # 1 Po100 down -
            # 1    Po1    up     1,8,17,60-62,65,67-68,92-93,11 -
            match = p18.match(line)
            if match:
                group = match.groupdict()
                vlan_type = 'vpc_peer_link_status'
                peer_link_id = int(group['peer_link_id'])
                peer_link_ifindex = Common.convert_intf_name(group['peer_link_ifindex'])
                peer_link_port_state = group['peer_link_port_state']
                peer_up_vlan_bitset = group['peer_up_vlan_bitset']
                vlan_bds = group.get('vlan_bds', None)
                peer_link_dict = ret_dict.setdefault('peer_link', {}). \
                    setdefault(peer_link_id, {})

                peer_link_dict.update({'peer_link_id': peer_link_id})
                peer_link_dict.update({'peer_link_ifindex': peer_link_ifindex})
                peer_link_dict.update({'peer_link_port_state': peer_link_port_state})
                peer_link_dict.update({'peer_up_vlan_bitset': peer_up_vlan_bitset})
                if vlan_bds:
                    peer_link_dict.update({'vlan_bds': vlan_bds})
                continue

            # 1     Po1           up     success     success               1,100-102,200-
            # 20 Po20 up failed vPC type-1 configuration -
            # 1 Po1 down success success -
            match = p19.match(line)
            if match:
                group = match.groupdict()
                vlan_type = 'vpc_status'
                vpc_id = int(group['vpc_id'])
                up_vlan_bitset = group['up_vlan_bitset']
                vpc_dict = ret_dict.setdefault('vpc', {}).setdefault(vpc_id, {})
                vpc_dict.update({'vpc_id': vpc_id})
                vpc_ifindex = Common.convert_intf_name(group['vpc_ifindex'])
                vpc_dict.update({'vpc_ifindex': vpc_ifindex})
                vpc_dict.update({'vpc_port_state': group['vpc_port_state']})
                vpc_dict.update({'vpc_consistency': group['vpc_consistency']})
                vpc_dict. \
                update({'vpc_consistency_status': group['vpc_consistency_status'].strip()})
                vpc_dict.update({'up_vlan_bitset': up_vlan_bitset})
                if group['vpc_plus_attrib'] is not None:
                    vpc_dict.update({'vpc_plus_attrib': group['vpc_plus_attrib']})
                continue
            
            # vPC peer-link status
            m = p20.match(line)
            if m:
                vlan_type = 'vpc_peer_link_status'
                continue
            
            # vPC status
            m = p21.match(line)
            if m:
                vlan_type = 'vpc_status'
                continue

            # Id               : 4
            match = p22.match(line)
            if match:
                group = match.groupdict()
                vlan_type = 'vpc_status'
                vpc_id = int(group['vpc_id'])
                vpc_dict = ret_dict.setdefault('vpc', {}).setdefault(vpc_id, {})
                vpc_dict.update({'vpc_id': vpc_id})
                continue
            
            # Port           : Po4
            match = p23.match(line)
            if match:
                group = match.groupdict()
                vpc_ifindex = Common.convert_intf_name(group['vpc_ifindex'])
                vpc_dict.update({'vpc_ifindex': vpc_ifindex})
                continue

            # Status         : up
            match = p24.match(line)
            if match:
                group = match.groupdict()
                vpc_port_state = group['vpc_port_state']
                vpc_dict.update({'vpc_port_state': vpc_port_state})
                continue

            # Consistency    : success
            match = p25.match(line)
            if match:
                group = match.groupdict()
                vpc_consistency = group['vpc_consistency']
                vpc_dict.update({'vpc_consistency': vpc_consistency})
                continue

            # Reason         : success
            # Reason         : Compatibility check failed for speed
            match = p26.match(line)
            if match:
                group = match.groupdict()
                vpc_consistency_status = group['vpc_consistency_status']
                vpc_dict.update({'vpc_consistency_status': vpc_consistency_status})
                continue

            # Active Vlans   : 65,67-68,401-402,1199
            match = p27.match(line)
            if match:
                group = match.groupdict()
                up_vlan_bitset = group['up_vlan_bitset']
                vpc_dict.update({'up_vlan_bitset': up_vlan_bitset})
                continue
            
            # Peer gateway excluded VLANs            : -
            match = p28.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'peer_gateway_exculded_vlans': group['peer_gateway_exculded_vlans']})
                continue

            # Peer gateway excluded bridge-domains   : -
            p29 = re.compile(r'^Peer +gateway +excluded +bridge-domains +: +(?P<peer_gateway_exculded_bridge_domains>\S+)$')
            match = p29.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'peer_gateway_exculded_bridge_domains': group['peer_gateway_exculded_bridge_domains']})
                continue

            # Dual-active excluded VLANs and BDs     : -
            match = p30.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'dual_active_excluded_vlans_and_bds': group['dual_active_excluded_vlans_and_bds']})
                continue

            # Delay-restore orphan ports status      : Timer is off.(timeout = 0s)
            match = p31.match(line)
            if match:
                group = match.groupdict()
                delay_restore_orphan_ports_status_dict = ret_dict.setdefault('delay_restore_orphan_ports_status', {})
                delay_restore_orphan_ports_status_dict.update({'timer': group['timer']})
                delay_restore_orphan_ports_status_dict.update({'timeout_sec': int(group['timeout'])})
                continue
            
            # Self-isolation                         : Disabled
            match = p32.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'self_isolation': group['self_isolation']})
                continue

            # 200
            # 202,300-350
            match = p33.match(line)
            if match:
                group = match.groupdict()
                if vlan_type == 'vpc_peer_link_status':
                    peer_up_vlan_bitset += group['additional_vlan']
                    peer_link_dict.update({'peer_up_vlan_bitset': peer_up_vlan_bitset})                    
                else:
                    up_vlan_bitset += group['additional_vlan']
                    vpc_dict.update({'up_vlan_bitset': up_vlan_bitset})
                continue
                
            # vPC+ switch id : 312
            match = p34.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_plus_switch_id': group['vpc_plus_switch_id']})
                continue
                
            # vPC fabricpath status : peer is reachable through fabricpath
            match = p35.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_fabricpath_status': group['vpc_fabricpath_status']})
                continue

            # 4,56-82,138, FP MAC:
            # 530,2587     312.0.0
            match = p36.match(line)
            if match:
                group = match.groupdict()
                if vlan_type == 'vpc_status' and vpc_dict.get('vpc_plus_attrib'):
                    vpc_dict['vpc_plus_attrib'] += group['additional_vpc_plus_attrib'].strip()
                    vpc_dict.update({'vpc_plus_attrib': vpc_dict['vpc_plus_attrib']})
                    up_vlan_bitset += group['additional_vlan']
                    vpc_dict.update({'up_vlan_bitset': up_vlan_bitset})                                  
                continue
        return ret_dict
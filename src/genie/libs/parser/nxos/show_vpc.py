"""show_vpc.py

Parser for the following show commands:
    * show vpc
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ========================================
# Schema for "show vpc"
# ========================================

class ShowVpcSchema(MetaParser):
    """Schema for "show vpc"""

    schema = {
        'vpc_domain_id': int,
        'vpc-peer-status': str,
        'vpc-peer-keepalive-status': str,
        'vpc-configuration-consistency-status': str,
        Optional('vpc-configuration-consistency-reason'): str,
        Optional('vpc-per-vlan-consistency-status'): str,        
        Optional('vpc-type-2-consistency-status'): str,
        Optional('vpc-role'): str,
        'num-of-vpcs': int,
        Optional('peer-gateway'): str,
        Optional('dual-active-excluded-vlans'): str,
        Optional('vpc-graceful-consistency-check-status'): str,
        Optional('vpc-auto-recovery-status'): str,
        Optional('vpc-delay-restore-status'): str,
        Optional('vpc-delay-restore-svi-status'): str,
        Optional('operational-l3-peer-router'): str,
        Optional('track-object'): int,
        Optional('peer-link'): {
            Any(): {
                'peer-link-id': int,
                'peer-link-ifindex': str,
                'peer-link-port-state': str,
                'peer-up-vlan-bitset': str
            }
        },
        Optional('vpc'): {
            Any(): {
                'vpc-id': int,
                'vpc-ifindex': str,
                'vpc-port-state': str,
                'vpc-consistency': str,
                'vpc-consistency-status': str,
                'up-vlan-bitset': str
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

        ret_dict = vpc_dict = peer_link_dict = {}
        up_vlan_bitset = peer_up_vlan_bitset = ''

        # vPC domain id                     : 1
        p1 = re.compile(r'^vPC +domain +id\s*: +(?P<domain_id>\d+)$')

        # Peer status                       : peer adjacency formed ok 
        p2 = re.compile(r'^Peer +status\s*: +(?P<peer_status>[\S\s]+)$')

        # vPC keep-alive status             : peer is alive 
        p3 = re.compile(r'^vPC +keep-alive +status\s*: +(?P<keepalive_status>[\S\s]+)$')

        # Configuration consistency status  : success
        # Configuration consistency status: success
        p4 = re.compile(r'^Configuration +consistency +status\s*: +(?P<config_status>[\S\s]+)$')

        # Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
        p5 = re.compile(r'^Configuration +consistency +reason\s*: +(?P<config_status_reason>[\S\s]+)$')

        # Per-vlan consistency status       : success 
        p6 = re.compile(r'^Per-vlan +consistency +status\s*: +(?P<per_vlan_status>[\S\s]+)$')

        # Type-2 consistency status         : success 
        p7 = re.compile(r'^Type-2 +consistency +status\s*: +(?P<type_2_status>[\S\s]+)$')

        # vPC role                          : primary  
        p8 = re.compile(r'^vPC +role\s*: +(?P<vpc_role>[\S\s]+)$')

        # Number of vPCs configured         : 1 
        p9 = re.compile(r'Number +of +(vPC|vPCs) +configured\s*: +(?P<num_of_vpc>\d+)$')

        # Peer Gateway                      : Enabled
        p10 = re.compile(r'^Peer +Gateway\s*: +(?P<peer_gateway>[\S\s]+)$')

        # Dual-active excluded VLANs        : -       
        p11 = re.compile(r'^Dual-active +excluded +VLANs\s*: +(?P<dual_active_excluded_vlan>[\S\s]+)$')

        # Graceful Consistency Check        : Enabled
        p12 = re.compile(r'^Graceful +Consistency +Check\s*: +(?P<graceful_check>[\S\s]+)$')

        # Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
        p13 = re.compile(r'^Auto-recovery +status\s*: +(?P<auto_recovery_status>[\S\s]+)$')

        # Delay-restore status              : Timer is off.(timeout = 30s)
        p14 = re.compile(r'^Delay-restore +status\s*: +(?P<delay_recovery_status>[\S\s]+)$')

        # Delay-restore SVI status          : Timer is off.(timeout = 10s)
        p15 = re.compile(r'^Delay-restore +SVI +status\s*: +(?P<delay_svi_recovery_status>[\S\s]+)$')

        # Operational Layer3 Peer-router    : Disabled
        p16 = re.compile(r'^Operational +Layer3 +Peer-router\s*: +(?P<layer3_peer_router>[\S\s]+)$')

        # Track object : 12
        p17 = re.compile(r'^Track +object\s*: +(?P<track_object>\d+)$')

        # 1     Po101  up     1,100-102,200-202
        # 1 Po100 down -
        p18 = re.compile(r'^(?P<peer_link_id>\d+) +(?P<peer_link_ifindex>\S+) +(?P<peer_link_port_state>\S+) +(?P<peer_up_vlan_bitset>[\d\,\-]+)$')

        # 1     Po1           up     success     success               1,100-102,200-
        # 20 Po20 up failed vPC type-1 configuration -
        # 1 Po1 down success success -
        p19 = re.compile(r'^(?P<vpc_id>\d+) +(?P<vpc_ifindex>\S+) +(?P<vpc_port_state>\S+) +(?P<vpc_consistency>\S+) +(?P<vpc_consistency_status>success|[\S\s]+) +(?P<up_vlan_bitset>[\d\,\-]+)$')

        # 200
        # 300-330, 350, 400-500
        p19_1 = re.compile(r'^(?P<additional_vlan>(?!--)[\d\,\-]+)$')        



        for line in output.splitlines():
            line = line.strip()

            # vPC domain id                     : 1
            match = p1.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc_domain_id': int(group['domain_id'])})
                continue

            # Peer status                       : peer adjacency formed ok 
            match = p2.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-peer-status': group['peer_status']})
                continue

            # vPC keep-alive status             : peer is alive 
            match = p3.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-peer-keepalive-status': group['keepalive_status']})
                continue

            # Configuration consistency status  : success
            # Configuration consistency status: success
            match = p4.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-configuration-consistency-status': group['config_status']})
                continue

            # Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
            match = p5.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-configuration-consistency-reason': group['config_status_reason']})
                continue

            # Per-vlan consistency status       : success 
            match = p6.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-per-vlan-consistency-status': group['per_vlan_status']})
                continue

            # Type-2 consistency status         : success 
            match = p7.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-type-2-consistency-status': group['type_2_status']})
                continue

            # vPC role                          : primary
            match = p8.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-role': group['vpc_role']})
                continue

            # Number of vPCs configured         : 1 
            match = p9.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'num-of-vpcs': int(group['num_of_vpc'])})
                continue

            # Peer Gateway                      : Enabled
            match = p10.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'peer-gateway': group['peer_gateway']})
                continue

            # Dual-active excluded VLANs        : -   
            match = p11.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'dual-active-excluded-vlans': group['dual_active_excluded_vlan']})
                continue

            # Graceful Consistency Check        : Enabled
            match = p12.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-graceful-consistency-check-status': group['graceful_check']})
                continue

            # Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
            match = p13.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-auto-recovery-status': group['auto_recovery_status']})
                continue

            # Delay-restore status              : Timer is off.(timeout = 30s)
            match = p14.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-delay-restore-status': group['delay_recovery_status']})
                continue

            # Delay-restore SVI status          : Timer is off.(timeout = 10s)
            match = p15.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'vpc-delay-restore-svi-status': group['delay_svi_recovery_status']})
                continue

            # Operational Layer3 Peer-router    : Disabled
            match = p16.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'operational-l3-peer-router': group['layer3_peer_router']})
                continue

            # Track object : 12
            match = p17.match(line)
            if match:
                group = match.groupdict()
                ret_dict.update({'track-object': int(group['track_object'])})
                continue            

            # 1     Po101  up     1,100-102,200-202
            # 1 Po100 down -
            match = p18.match(line)
            if match:
                group = match.groupdict()
                vpc_dict = {}
                peer_link_id = int(group['peer_link_id'])
                peer_up_vlan_bitset = group['peer_up_vlan_bitset']
                peer_link_dict = ret_dict.setdefault('peer-link', {}).setdefault(peer_link_id, {})
                peer_link_dict.update({'peer-link-id': peer_link_id})
                peer_link_dict.update({'peer-link-ifindex': group['peer_link_ifindex']})
                peer_link_dict.update({'peer-link-port-state': group['peer_link_port_state']})
                peer_link_dict.update({'peer-up-vlan-bitset': peer_up_vlan_bitset})
                continue

            # 1     Po1           up     success     success               1,100-102,200-
            # 20 Po20 up failed vPC type-1 configuration -
            # 1 Po1 down success success -
            match = p19.match(line)
            if match:
                group = match.groupdict()
                vpc_id = int(group['vpc_id'])
                up_vlan_bitset = group['up_vlan_bitset']
                vpc_dict = ret_dict.setdefault('vpc', {}).setdefault(vpc_id, {})
                vpc_dict.update({'vpc-id': vpc_id})
                vpc_dict.update({'vpc-ifindex': group['vpc_ifindex']})
                vpc_dict.update({'vpc-port-state': group['vpc_port_state']})
                vpc_dict.update({'vpc-consistency': group['vpc_consistency']})
                vpc_dict.update({'vpc-consistency-status': group['vpc_consistency_status'].strip()})
                vpc_dict.update({'up-vlan-bitset': up_vlan_bitset})
                continue

            # 200
            # 202,300-350
            match = p19_1.match(line)
            if match:
                group = match.groupdict()
                if vpc_dict == {}:
                    peer_up_vlan_bitset += group['additional_vlan']
                    peer_link_dict.update({'peer-up-vlan-bitset': peer_up_vlan_bitset})                    
                else:
                    up_vlan_bitset += group['additional_vlan']
                    vpc_dict.update({'up-vlan-bitset': up_vlan_bitset})
                continue

        return ret_dict
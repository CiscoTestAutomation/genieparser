''' show_vpn.py

Parser for the following show commands:
    * show vpn load-balancing
    * show vpn-sessiondb summary
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, 
                                                Any,
                                                Optional)

# =============================================
# Schema for 'show vpn load-balancing'
# =============================================
class ShowVPNLoadBalancingSchema(MetaParser):
    """Schema for
        * show vpn load-balancing
    """

    schema = {
        'status': str,
        'role': str,
        'failover': str,
        'encryption': str,
        'peers_count': int,
        'cluster_ip': str,
        'peers': {
            Any(): {
                'role': str,
                'pri': int,
                'model': str,
                'load_balancing_version': int,
                'public_ip': str,
            }
        },
        'total_license_load': {
            Any(): {
                'anyconnect_premium_essentials': {
                    'limit': int,
                    'used': int,
                    'load': int,
                },
                'other_vpn': {
                    'limit': int,
                    'used': int,
                    'load': int,
                },
                'public_ip': str,
            }
        }
    }

# =============================================
# Parser for 'show vpn load-balancing'
# =============================================
class ShowVPNLoadBalancing(ShowVPNLoadBalancingSchema):
    """Parser for
        * show vpn load-balancing
    """

    cli_command = 'show vpn load-balancing'

    def cli(self, output=None):
        if output is None:
            # execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        peers_index = 0
        total_license_load_index = 0
        # Enabled    Master   n/a        Enabled          1     cluster1
        p1 = re.compile(r'^(?P<status>\S+) +(?P<role>\S+) +'
                        r'(?P<failover>\S+) +(?P<encryption>\S+) +'
                        r'(?P<peers>\d+) +(?P<cluster_ip>\S+)$')

        # Master    5  ASA-VASA                               4  10.246.0.1*
        # Backup    5  ASA-VASA                               4  10.246.0.2
        p2 = re.compile(r'^(?P<role>\S+) +(?P<pri>\d+) +(?P<model>\S+) +'
                        r'(?P<version>\d+) +(?P<public_ip>\S+)$')
        
        # 250       0      0%           250       2      1%  10.246.0.1*
        # 0       0      0%             0       0      0%  10.246.0.2
        p3 = re.compile(r'^(?P<limit_1>\d+) +(?P<used_1>\d+) +(?P<load_1>\d+)'
                        r'\% +(?P<limit_2>\d+) +(?P<used_2>\d+) +(?P<load_2>\d+)% +'
                        r'(?P<public_ip>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Enabled    Master   n/a        Enabled          1     cluster1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                role = group['role']
                failover = group['failover']
                encryption = group['encryption']
                peers = int(group['peers'])
                cluster_ip = group['cluster_ip']
                ret_dict.update({'status': status})
                ret_dict.update({'role': role})
                ret_dict.update({'failover': failover})
                ret_dict.update({'encryption': encryption})
                ret_dict.update({'peers_count': peers})
                ret_dict.update({'cluster_ip': cluster_ip})
                continue

            # Master    5  ASA-VASA                               4  10.246.0.1*
            # Backup    5  ASA-VASA                               4  10.246.0.2
            m = p2.match(line)
            if m:
                peers_index += 1
                group = m.groupdict()
                role = group['role']
                pri = int(group['pri'])
                model = group['model']
                version = int(group['version'])
                public_ip = group['public_ip']
                peers_dict = ret_dict.setdefault('peers', {}). \
                    setdefault(peers_index, {})
                peers_dict.update({'role': role})
                peers_dict.update({'pri': pri})
                peers_dict.update({'model': model})
                peers_dict.update({'load_balancing_version': version})
                peers_dict.update({'public_ip': public_ip})
                continue
            
            # 250       0      0%           250       2      1%  10.246.0.1*
            # 0       0      0%             0       0      0%  10.246.0.2
            m = p3.match(line)
            if m:
                total_license_load_index += 1
                group = m.groupdict()
                total_license_load = ret_dict.setdefault('total_license_load', {}). \
                    setdefault(total_license_load_index, {})
                anyconnect_premium_essential_dict = total_license_load.setdefault(
                    'anyconnect_premium_essentials', {})
                other_vpn_dict = total_license_load.setdefault(
                    'other_vpn', {})
                limit_1 = int(group['limit_1'])
                used_1 = int(group['used_1'])
                load_1 = int(group['load_1'])
                anyconnect_premium_essential_dict.update({'limit': limit_1})
                anyconnect_premium_essential_dict.update({'used': used_1})
                anyconnect_premium_essential_dict.update({'load': load_1})
                limit_2 = int(group['limit_2'])
                used_2 = int(group['used_2'])
                load_2 = int(group['load_2'])
                other_vpn_dict.update({'limit': limit_2})
                other_vpn_dict.update({'used': used_2})
                other_vpn_dict.update({'load': load_2})
                public_ip = group['public_ip']
                total_license_load.update({'public_ip': public_ip})
                continue

        return ret_dict

# =============================================
# Schema for 'show vpn-sessiondb summary'
# =============================================
class ShowVPNSessionDBSummarySchema(MetaParser):
    """Schema for
        * show vpn-sessiondb summary
    """

    schema = {
        'ikev1_ipsec_l2tp_ip_sec': {
            'active': int,
            'cumulative': int,
            'peak_concurrent': int,
            Optional('inactive'): int,
        },
        'load_balancing_encryption': {
            'active': int,
            'cumulative': int,
            'peak_concurrent': int,
            Optional('inactive'): int,
        },
        'total_active_and_inactive': int,
        'total_cumulative': int,
        'device_total_vpn_capacity': int,
        'device_load': int,
    }

# =============================================
# Parser for 'show vpn-sessiondb summary'
# =============================================
class ShowVPNSessionDBSummary(ShowVPNSessionDBSummarySchema):
    """Parser for
        * show vpn-sessiondb summary
    """

    cli_command = 'show vpn-sessiondb summary'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # IKEv1 IPsec/L2TP IPsec       :      2 :          2 :           2
        p1 = re.compile(r'^IKEv1 +IPsec\/L2TP +IPsec +: +(?P<active>\d+) *'
                        r': +(?P<cumulative>\d+) *: +(?P<peak_concurrent>\d+)'
                        r'( *: (?P<inactive>\d+))?$')

        # Load Balancing(Encryption)   :      0 :          6 :           1
        p2 = re.compile(r'^Load +Balancing\(Encryption\) +: +(?P<active>\d+) *'
                        r': +(?P<cumulative>\d+) *: +(?P<peak_concurrent>\d+)'
                        r'( *: (?P<inactive>\d+))?$')

        # Total Active and Inactive    :      2             Total Cumulative :      8
        p3 = re.compile(r'^Total +Active +and +Inactive +: +'
                        r'(?P<total_active_and_inactive>\d+) +Total +Cumulative +: +'
                        r'(?P<total_cumulative>\d+)$')
        
        # Device Total VPN Capacity    :    250
        p4 = re.compile(r'^Device +Total +VPN +Capacity +: +'
                        r'(?P<device_total_vpn_capacity>\d+)$')
        
        # Device Load                  :     1%
        p5 = re.compile(r'^Device +Load +: +(?P<device_load>\d+)\%$')

        for line in out.splitlines():
            line = line.strip()

            # IKEv1 IPsec/L2TP IPsec       :      2 :          2 :           2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                active = int(group['active'])
                cumulative = int(group['cumulative'])
                peak_concurrent = int(group['peak_concurrent'])
                inactive = group.get('inactive', None)
                ikev1_ipsec_l2tp_ip_sec_dict = ret_dict.setdefault('ikev1_ipsec_l2tp_ip_sec', {})
                ikev1_ipsec_l2tp_ip_sec_dict.update({'active': active})
                ikev1_ipsec_l2tp_ip_sec_dict.update({'cumulative': cumulative})
                ikev1_ipsec_l2tp_ip_sec_dict.update({'peak_concurrent': peak_concurrent})
                if inactive:
                    ikev1_ipsec_l2tp_ip_sec_dict.update({'inactive': int(inactive)})
                continue

            # Load Balancing(Encryption)   :      0 :          6 :           1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                active = int(group['active'])
                cumulative = int(group['cumulative'])
                peak_concurrent = int(group['peak_concurrent'])
                inactive = group.get('inactive', None)
                load_balancing_encryption_dict = ret_dict.setdefault('load_balancing_encryption', {})
                load_balancing_encryption_dict.update({'active': active})
                load_balancing_encryption_dict.update({'cumulative': cumulative})
                load_balancing_encryption_dict.update({'peak_concurrent': peak_concurrent})
                if inactive:
                    load_balancing_encryption_dict.update({'inactive': int(inactive)})
                continue

            # Total Active and Inactive    :      2             Total Cumulative :      8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_active_and_inactive = int(group['total_active_and_inactive'])
                total_cumulative = int(group['total_cumulative'])
                ret_dict.update({'total_active_and_inactive': total_active_and_inactive})
                ret_dict.update({'total_cumulative': total_cumulative})
                continue

            # Device Total VPN Capacity    :    250
            m = p4.match(line)
            if m:
                group = m.groupdict()
                device_total_vpn_capacity = int(group['device_total_vpn_capacity'])
                ret_dict.update({'device_total_vpn_capacity': device_total_vpn_capacity})
                continue

            # Device Load                  :     1%
            m = p5.match(line)
            if m:
                group = m.groupdict()
                device_load = int(group['device_load'])
                ret_dict.update({'device_load': device_load})
                continue
        
        return ret_dict
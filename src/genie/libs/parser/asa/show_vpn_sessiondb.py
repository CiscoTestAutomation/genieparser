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
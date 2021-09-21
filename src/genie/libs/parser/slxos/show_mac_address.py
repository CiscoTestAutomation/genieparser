"""
Author:
    Fabio Pessoa Nunes (https://www.linkedin.com/in/fpessoanunes/)

show_mac_address.py

SLXOS parsers for the following show commands:
    * show mac address-table

Schemas based on SLX's YANG models
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#   * 'show mac-address-table'
# ==================================================
class ShowMacAddressTableSchema(MetaParser):
    ''' Schema for "show mac-address-table" '''

    schema = {
        'total-mac-addresses': int,
        Optional('macs'): {
            Any(): {  # mac
                'mac': str,
                'domain-types': {
                    Any(): {
                        'domain-type': str,
                        'domain-ids': {
                            Any(): {  # domain-id
                                'domain-id': int,
                                'port-lif-pw-t': str,
                                'mac-type': str,
                                'mac-state': str
                            }
                        }
                    }
                }
            }
        }
    }


# ===================================
# Parser for:
#   * 'show mac-address-table'
# ===================================
class ShowMacAddressTable(ShowMacAddressTableSchema):
    ''' Parser for "show mac-address-table" '''

    cli_command = ['show mac-address-table']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        res_dict = {}

        # Total MAC addresses    :  6
        p1 = re.compile(r'^Total\s+MAC\s+addresses\s*:\s*(?P<total_mac>\d+)$')

        # VlanId/BDId   Mac-address       Type        State      Ports/LIF/PW/T
        # 199 (V)       deab.0e3e.78df    Dynamic     Active     Eth 0/44
        # 100 (B)       aabb.c951.0801    Dynamic     Active     192.168.90.31
        # 100 (B)       abcd.0f09.0a12    Dynamic     Active     192.168.90.20
        # 100 (B)       1234.45cc.b249    Dynamic     Active     Po 6.100
        # 200 (B)       1234.45cc.b249    Dynamic     Active     Po 6.200
        # 839 (B)       1234.45cc.b249    Dynamic     Active     Po 6.839
        p2 = re.compile(
            r'^(?P<domain_id>\d+)\s\((?P<domain_type>\w+)\)\s+'
            r'(?P<mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
            r'(?P<mac_type>\w+)\s+(?P<mac_state>\w+)\s+'
            r'(?P<port_lif_pw_t>.*)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                res_dict['total-mac-addresses'] = int(m.groupdict()['total_mac'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                macs = res_dict.setdefault('macs', {})
                mac = macs.setdefault(group['mac'], {})
                mac['mac'] = group['mac']
                domain_types = mac.setdefault('domain-types', {})
                domain_type = domain_types.setdefault(group['domain_type'], {})
                domain_type['domain-type'] = group['domain_type']
                domain_ids = domain_type.setdefault('domain-ids', {})
                domain_id = domain_ids.setdefault(int(group['domain_id']), {})
                domain_id['domain-id'] = int(group['domain_id'])
                domain_id['port-lif-pw-t'] = group['port_lif_pw_t']
                domain_id['mac-type'] = group['mac_type']
                domain_id['mac-state'] = group['mac_state']
                continue
        return res_dict

''' show_vpn_sessiondb.py

Parser for the following show commands:
    * show vpn-sessiondb
    * show vpn-sessiondb anyconnect
    * show vpn-sessiondb anyconnect sort inactivity
    * show vpn-sessiondb webvpn
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Any, \
                                                Optional

# =============================================
# Schema for
#     * show vpn-sessiondb
#     * show vpn-sessiondb anyconnect
#     * show vpn-sessiondb anyconnect sort inactivity
#     * show vpn-sessiondb webvpn
# =============================================
class ShowVpnSessiondbSchema(MetaParser):
    schema = {
        'session_type': {
            Any(): {
                'username': {
                    Any(): {
                        'index': int,
                        Optional('ip_addr'): str,
                        Optional('assigned_ip'): str,
                        Optional('public_ip'): str,
                        'protocol': str,
                        Optional('vpn_client_encryption'): str,
                        Optional('license'): str,
                        Optional('encryption'): str,
                        'hashing': str,
                        'auth_mode': str,
                        Optional('group_policy'): str,
                        Optional('group'): str,
                        Optional('tunnel_group'): str,
                        Optional('tcp'): {
                            'src_port': int,
                            'dst_port': int,
                        },
                        'bytes': {
                            'tx': int,
                            'rx': int,
                        },
                        Optional('pkts'): {
                            'tx': int,
                            'rx': int,
                        },

                        Optional('client_version'): str,
                        Optional('client_type'): str,
                        Optional('nac_result'): str,
                        'login_time': str,
                        'duration': str,
                        'inactivity': str,
                        Optional('filter_name'): str,
                        Optional('vlan_mapping'): str,
                        Optional('vlan'): str,
                        Optional('audt_sess_id'): str,
                        Optional('security_group'): str,
                    }
                }
            }
        }
    }

# =============================================
# Parser for
#     * show vpn-sessiondb
# =============================================
class ShowVpnSessiondb(ShowVpnSessiondbSchema):
    """Parser for
        * show vpn-sessiondb
    """

    cli_command = 'show vpn-sessiondb'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
# =============================================
# Parser for
#     * show vpn-sessiondb anyconnect
# =============================================

# =============================================
# Parser for
#     * show vpn-sessiondb anyconnect sort inactivity
# =============================================

# =============================================
# Parser for
#     * show vpn-sessiondb webvpn
# =============================================

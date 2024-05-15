""" show_ip_rsvp_fast_reroute.py

IOSXE parsers for the following show commands:
    * 'show ip rsvp fast-reroute'

Copyright (c) 2022-2024 by cisco Systems, Inc.
All rights reserved
"""

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)


class ShowIpRsvpFastRerouteSchema(MetaParser):
    """Schema for show ip rsvp fast-reroute"""

    schema = {
        Optional('p2p_protected_lsps'): {
            Any(): {
                'protect_intf': str,
                'bandwidth': str,
                'bandwidth_type': str,
                'backup_tunnel': str,
                'backup_label': str,
                'state': str,
                'level': str,
                'type': str
            }
        },
        Optional('p2p_protected_sub_lsps'): {
            Any(): {
                'protect_intf': str,
                'bandwidth': str,
                'bandwidth_type': str,
                'backup_tunnel': str,
                'backup_label': str,
                'state': str
            }
        }
    }


# =====================================
# Parser for 'show ip rsvp fast-reroute'
# =====================================
class ShowIpRsvpFastReroute(ShowIpRsvpFastRerouteSchema):
    """show ip rsvp fast-reroute
    """

    cli_command = 'show ip rsvp fast-reroute'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Protected LSP
        p0 = re.compile(r'Protected\s+LSP')

        # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready  any-unl Nhop
        p1 = re.compile(
            r"(?P<p2p_protected_lsp>\S+)\s+"
            r"(?P<protect_intf>\S+)\s+"
            r"(?P<bandwidth_and_type>\d+[a-zA-Z]+\:\w+)\s+"
            r"(?P<backup_tunnel_and_label>\w+\:\w+)\s+"
            r"(?P<state>\S+)\s+"
            r"(?P<level>\S+)\s+"
            r"(?P<type>\S+)\s*$")

        # *Protected Sub-LSP
        p2 = re.compile(r'\*Protected\s+Sub\-LSP')

        # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready
        p3 = re.compile(
            r"(?P<p2p_protected_sub_lsp>\S+)\s+"
            r"(?P<protect_intf>\S+)\s+"
            r"(?P<bandwidth_and_type>\d+[a-zA-Z]+\:\w+)\s+"
            r"(?P<backup_tunnel_and_label>\w+\:\w+)\s+"
            r"(?P<state>\S+)\s*$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Protected LSP
            m = p0.match(line)
            if m:
                p2p_protected_lsps_dict = ret_dict.setdefault('p2p_protected_lsps', {})
                continue

            # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready  any-unl Nhop
            m = p1.match(line)
            if m:
                group_dict = m.groupdict()
                p2p_protected_lsp_dict = \
                    p2p_protected_lsps_dict.setdefault(group_dict['p2p_protected_lsp'], {})
                bandwidth, bandwidth_type = group_dict['bandwidth_and_type'].strip().split(":")
                backup_tunnel, backup_label = group_dict['backup_tunnel_and_label'].strip().split(":")
                p2p_protected_lsp_dict.update({
                    'protect_intf': Common.convert_intf_name(group_dict['protect_intf']),
                    'bandwidth': bandwidth,
                    'bandwidth_type': bandwidth_type,
                    'backup_tunnel': Common.convert_intf_name(backup_tunnel),
                    'backup_label': backup_label,
                    'state': group_dict['state'],
                    'level': group_dict['level'],
                    'type': group_dict['type']})
                continue

            # *Protected Sub-LSP
            m = p2.match(line)
            if m:
                p2p_protected_sub_lsps_dict = ret_dict.setdefault('p2p_protected_sub_lsps', {})
                continue

            # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready
            m = p3.match(line)
            if m:
                group_dict = m.groupdict()
                p2p_protected_sub_lsp_dict = \
                    p2p_protected_sub_lsps_dict.setdefault(group_dict['p2p_protected_sub_lsp'], {})
                bandwidth, bandwidth_type = group_dict['bandwidth_and_type'].strip().split(":")
                backup_tunnel, backup_label = group_dict['backup_tunnel_and_label'].strip().split(":")
                p2p_protected_sub_lsp_dict.update({
                    'protect_intf': Common.convert_intf_name(group_dict['protect_intf']),
                    'bandwidth': bandwidth,
                    'bandwidth_type': bandwidth_type,
                    'backup_tunnel': Common.convert_intf_name(backup_tunnel),
                    'backup_label': backup_label,
                    'state': group_dict['state']})
                continue

        return ret_dict

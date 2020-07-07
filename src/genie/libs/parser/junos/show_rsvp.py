"""show_rsvp.py

JUNOS parsers for the following commands:
    * show rsvp neighbor
    * show rsvp neighbor detail
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowRSVPNeighborSchema(MetaParser):
    """ Schema for:
        * show rsvp neighbor
    """

    def validate_neighbor_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('RSVP Neighbor not a list')

        rsvp_neighbor_list = Schema({
                "rsvp-neighbor-address": str,
                "neighbor-idle": str,
                "neighbor-up-count": str,
                "neighbor-down-count": str,
                "last-changed-time": str,
                "hello-interval": str,
                "hellos-sent": str,
                "hellos-received": str,
                "messages-received": str,
            })

        for item in value:
            rsvp_neighbor_list.validate(item)
        return value

    schema = {
            "rsvp-neighbor-information": {
                "rsvp-neighbor-count": str,
                "rsvp-neighbor": Use(validate_neighbor_list)
            }
        }

class ShowRSVPNeighbor(ShowRSVPNeighborSchema):
    """ Parser for:
        * show rsvp neighbor
    """

    cli_command = 'show rsvp neighbor'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # RSVP neighbor: 4 learned
        p1 = re.compile(r'^RSVP +neighbor: +(?P<rsvp_neighbor_count>\d+) +learned$')

        # 10.34.3.252      15:55  0/0       15:52        9   106/0    0
        # 10.169.14.240    34:15  0/0       34:13        9   229/0    0
        # 10.169.14.157        0  1/0       34:13        9   230/229  333
        # 2001::AF       0  1/0       15:55        9   105/105  197
        p2 = re.compile(r'^(?P<rsvp_neighbor_address>[\d\.|a-fA-F\:\d]+) +'
                        r'(?P<neighbor_idle>\S+) +'
                        r'((?P<neighbor_up_count>\d+)/(?P<neighbor_down_count>\d+)) +'
                        r'(?P<last_changed_time>\S+) +(?P<hello_interval>\d+) +'
                        r'((?P<hellos_sent>\d+)/(?P<hellos_received>\d+)) +'
                        r'(?P<messages_received>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # RSVP neighbor: 4 learned
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = ret_dict.setdefault('rsvp-neighbor-information', {})
                neighbor_information['rsvp-neighbor-count'] = group['rsvp_neighbor_count']
                continue

            # 10.34.3.252      15:55  0/0       15:52        9   106/0    0
            # 10.169.14.240    34:15  0/0       34:13        9   229/0    0
            # 10.169.14.157        0  1/0       34:13        9   230/229  333
            # 2001::AF       0  1/0       15:55        9   105/105  197
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_list = neighbor_information.setdefault('rsvp-neighbor', [])
                rsvp_neighbor_list.append(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict

class ShowRSVPNeighborDetailSchema(MetaParser):
    """ Schema for 
        * show rsvp neighbor detail
    """

    def validate_neighbor_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('RSVP Neighbor not a list')

        rsvp_neighbor_list = Schema({
                    "rsvp-neighbor-address": str,
                    Optional("rsvp-neighbor-interface"): str,
                    "rsvp-neighbor-status": str,
                    Optional("rsvp-neighbor-node"): bool,
                    "last-changed-time": str,
                    "neighbor-idle": str,
                    "neighbor-up-count": str,
                    "neighbor-down-count": str,
                    "messages-received": str,
                    "hello-interval": str,
                    "hellos-sent": str,
                    "hellos-received": str,
                    "rsvp-neighbor-remote-instance": str,
                    "rsvp-neighbor-local-instance": str,
                    "rsvp-refresh-reduct-status": str,
                    "rsvp-refresh-reduct-remote-status": str,
                    "rsvp-refresh-reduct-ack-status": str,
                    "rsvp-nbr-enh-local-protection": {
                        "rsvp-nbr-enh-lp-status": str,
                        Optional("rsvp-nbr-enh-lp-total-lsp-count"): str,
                        Optional("rsvp-nbr-enh-lp-phop-lsp-count"): str,
                        Optional("rsvp-nbr-enh-lp-pphop-lsp-count"): str,
                        Optional("rsvp-nbr-enh-lp-nhop-lsp-count"): str,
                        Optional("rsvp-nbr-enh-lp-nnhop-lsp-count"): str,
                    }
                })

        for item in value:
            rsvp_neighbor_list.validate(item)
        return value


    schema = {
            "rsvp-neighbor-information": {
                "rsvp-neighbor-count": str,
                "rsvp-neighbor": Use(validate_neighbor_list)
            }
        }

class ShowRSVPNeighborDetail(ShowRSVPNeighborDetailSchema):
    """ Parser for:
        * show rsvp neighbor detail
    """

    cli_command = 'show rsvp neighbor detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # RSVP neighbor: 4 learned
        p1 = re.compile(r'^RSVP +neighbor: +(?P<rsvp_neighbor_count>\d+) +learned$')

        # Address: 59.128.3.252 status: Down (Node neighbor)
        # Address: 106.187.14.157 via: ge-0/0/0.0 status: Up
        p2 = re.compile(r'^Address: +(?P<rsvp_neighbor_address>\S+) +'
                        r'(via: +(?P<rsvp_neighbor_interface>\S+) +)?'
                        r'status: +(?P<rsvp_neighbor_status>\S+)'
                        r'( +(?P<rsvp_neighbor_node>\(Node neighbor\)))?$')

        # Last changed time: 27:54, Idle: 27:55 sec, Up cnt: 0, Down cnt: 0
        # Last changed time: 46:15, Idle: 0 sec, Up cnt: 1, Down cnt: 0
        p3 = re.compile(r'^Last +changed +time: +(?P<last_changed_time>[^\s,]+), +'
                        r'Idle: +(?P<neighbor_idle>\S+) +sec, +'
                        r'Up +cnt: +(?P<neighbor_up_count>\d+), +'
                        r'Down +cnt: +(?P<neighbor_down_count>\d+)$')

        # Message received: 695
        p4 = re.compile(r'^Message +received: +(?P<messages_received>\d+)$')

        # Hello: sent 187, received: 0, interval: 9 sec
        p5 = re.compile(r'^Hello: +sent:? (?P<hellos_sent>\d+), +'
                        r'received: +(?P<hellos_received>\d+), +'
                        r'interval: +(?P<hello_interval>\d+) +sec$')

        # Remote instance: 0xa1a75540, Local instance: 0x41ad0a42
        p6 = re.compile(r'^Remote +instance: +(?P<rsvp_neighbor_remote_instance>[^\s,]+), +'
                        r'Local +instance: +(?P<rsvp_neighbor_local_instance>\S+)$')

        # Refresh reduction:  operational
        p7 = re.compile(r'^Refresh +reduction: +(?P<rsvp_refresh_reduct_status>.*)$')

        # Remote end: disabled, Ack-extension: disabled
        p8 = re.compile(r'^Remote +end: +(?P<rsvp_refresh_reduct_remote_status>[^\s,]+), +'
                        r'Ack-extension: +(?P<rsvp_refresh_reduct_ack_status>[^\s,]+)$')

        # Enhanced FRR: Enabled
        p9 = re.compile(r'^Enhanced +FRR: +(?P<rsvp_nbr_enh_lp_status>\S+)$')

        # LSPs (total 30): Phop 30, PPhop 0, Nhop 0, NNhop 0
        p10 = re.compile(r'^LSPs +\(total +(?P<rsvp_nbr_enh_lp_total_lsp_count>\d+)\): +'
                         r'Phop +(?P<rsvp_nbr_enh_lp_phop_lsp_count>\d+), +'
                         r'PPhop +(?P<rsvp_nbr_enh_lp_pphop_lsp_count>\d+), +'
                         r'Nhop +(?P<rsvp_nbr_enh_lp_nhop_lsp_count>\d+), +'
                         r'NNhop +(?P<rsvp_nbr_enh_lp_nnhop_lsp_count>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # RSVP neighbor: 4 learned
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = ret_dict.setdefault('rsvp-neighbor-information', {})
                neighbor_information['rsvp-neighbor-count'] = group['rsvp_neighbor_count']
                continue

            # Address: 59.128.3.252 status: Down (Node neighbor)
            # Address: 106.187.14.157 via: ge-0/0/0.0 status: Up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_list = neighbor_information.setdefault('rsvp-neighbor', [])
                rsvp_neighbor_dict = {}
                if 'rsvp_neighbor_node' in group:
                    group.pop('rsvp_neighbor_node')
                    rsvp_neighbor_dict.update({'rsvp-neighbor-node': True})
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                rsvp_neighbor_list.append(rsvp_neighbor_dict)
                continue

            # Last changed time: 27:54, Idle: 27:55 sec, Up cnt: 0, Down cnt: 0
            # Last changed time: 46:15, Idle: 0 sec, Up cnt: 1, Down cnt: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Message received: 695
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Hello: sent 187, received: 0, interval: 9 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Remote instance: 0xa1a75540, Local instance: 0x41ad0a42
            m = p6.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Refresh reduction:  operational
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Remote end: disabled, Ack-extension: disabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Enhanced FRR: Enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                rsvp_nbr_dict = rsvp_neighbor_dict.setdefault(
                    'rsvp-nbr-enh-local-protection', {})
                rsvp_nbr_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # LSPs (total 30): Phop 30, PPhop 0, Nhop 0, NNhop 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rsvp_nbr_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue


        return ret_dict
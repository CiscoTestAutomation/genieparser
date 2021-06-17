""" ShowOspfv3SummaryPrefix.py

IOSXE parser for the following show command:
    *show ospfv3 summary-prefix
"""

# python
import re

# Metaparser
from typing import Dict

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default
from genie.libs.parser.utils.common import Common

# ===============================================
# Schema for 'show ospfv3 summary-prefix'
# Optional: allowing either ipv4 or ipv6 or both
# ===============================================

class ShowOspfv3SummaryPrefixSchema(MetaParser):

    schema = {
            Optional('ospf_id'): str,
            Optional('add_family'): str,
            Optional('rtr_id'): str,
            Optional('null_metric'): str,
            Optional('sum_prefix'): str,
            Optional('sum_type'): str,
            Optional('sum_tag'): str
    }

# ================================
# Parser for 'ShowOspfv3SummaryPrefix'
# ================================

class ShowOspfv3SummaryPrefix(ShowOspfv3SummaryPrefixSchema):
    """
        Router#sh ospfv3 summary-prefix

                OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)

        10:2::/96           Metric <unreachable>
        10:2:2::/96         Metric 111, External metric type 2, Tag 111
        Router#
    """

    cli_command = 'show ospfv3 summary-prefix'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init var
        ret_dict: Dict[str, str] = {}

        p1 = re.compile(r'^OSPFv3 +(?P<ospf_id>(\d+)) +address-family +(?P<add_family>(\S+)) +\(router-id +(?P<rtr_id>(\S+))\)')
        # 2nd line of output
        p2 = re.compile(r'^[\d:/]+\s+Metric\s+(?P<null_metric>(\S+$))')
        # 3rd line of output
        p3 = re.compile(r'^(?P<sum_prefix>(\S+)) +.* type +(?P<sum_type>(\d)),\s+Tag +(?P<sum_tag>(\S+))')

        for line in out.splitlines():
            line = line.strip()
            m = p1.search(line)
            if m:
                group = m.groupdict()
                ret_dict [ 'ospf_id' ] = group [ 'ospf_id' ].strip()
                ret_dict [ 'add_family' ] = group [ 'add_family' ].strip()
                ret_dict [ 'rtr_id' ] = group [ 'rtr_id' ].strip()
                continue

            m = p2.search(line)
            if m:
                group = m.groupdict()
                ret_dict [ 'null_metric' ] = group [ 'null_metric' ].strip()
                continue

            m = p3.search(line)
            if m:
                group = m.groupdict()
                ret_dict [ 'sum_prefix' ] = group [ 'sum_prefix' ].strip()
                ret_dict [ 'sum_type' ] = group [ 'sum_type' ].strip()
                ret_dict [ 'sum_tag' ] = group [ 'sum_tag' ].strip()
                continue

        #import pdb; pdb.set_trace()

        return ret_dict

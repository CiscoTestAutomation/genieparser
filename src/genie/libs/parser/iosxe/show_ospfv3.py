""" ShowOspfv3SummaryPrefix.py

IOSXE parser for the following show command:
    * show ospfv3 summary-prefix
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default

# ===============================================
# Schema for 'show ospfv3 summary-prefix'
# Optional: allowing either ipv4 or ipv6 or both
# ===============================================

class ShowOspfv3SummaryPrefixSchema(MetaParser):
    schema = {
        'process_id': {
            Any(): {
                'address_family': str,
                'router_id': str,
                'null_route': {
                    Any(): {
                        'null_metric': str,
                    },
                },
                'summary': {
                    Any(): {
                        'sum_type': str,
                        'sum_tag': int,
                        'sum_metric': int
                    },
                },
            },
        },
    }


# ====================================
# Parser for 'ShowOspfv3SummaryPrefix'
# ====================================

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
        ret_dict = {}
        ospf_id = ""

        # OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)
        p1 = re.compile(
            r'^OSPFv3 +(?P<ospf_id>(\d+)) +address-family +(?P<address_family>(\S+)) +\(router-id +(?P<router_id>(\S+))\)')

        # 10:2::/96           Metric <unreachable>
        p2 = re.compile(r'^(?P<null_prefix>(\S+)) +.* Metric\s+(?P<null_metric>(\S+$))')

        # 10:2:2::/96         Metric 111, External metric type 2, Tag 111
        p3 = re.compile(
            r'^(?P<sum_prefix>(\S+)) +.* Metric\s+(?P<sum_metric>(\d+)),.* +type +(?P<sum_type>(\d)),\s+Tag +(?P<sum_tag>(\S+))')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['process_id'] = {}
                ospf_id = group['ospf_id']
                ret_dict['process_id'][ospf_id] = {}
                ret_dict['process_id'][ospf_id]['null_route'] = {}
                ret_dict['process_id'][ospf_id]['summary'] = {}
                ret_dict['process_id'][ospf_id]['address_family'] = group['address_family']
                ret_dict['process_id'][ospf_id]['router_id'] = group['router_id']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['null_prefix']:
                    n_prefix = group['null_prefix']
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix] = {}
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix]['null_metric'] = group['null_metric']
                    continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['sum_prefix']:
                    prefix = group['sum_prefix']
                    ret_dict['process_id'][ospf_id]['summary'][prefix] = {}
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_metric'] = int(group['sum_metric'])
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_type'] = group['sum_type']
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_tag'] = int(group['sum_tag'])
                    continue


        return ret_dict

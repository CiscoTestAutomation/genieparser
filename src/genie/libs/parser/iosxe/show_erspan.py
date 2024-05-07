import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

# ======================================================
# Parser for 'show capability feature monitor erspan-source / erspan-destination'
# ======================================================

class ShowCapabilityFeatureMonitorErspanSourceDestinationSchema(MetaParser):
    """Schema for show capability feature monitor erspan-source"""

    schema = {
        'erspan_capability': {
            Optional('source_supported'): str,
            Optional('source_rx_session_no'): int,
            Optional('source_tx_session_no'): int,
            'header_type': str,
            Optional('acl_filter'): str,
            Optional('sgt_filter'): str,
            Optional('fragmentation_supported'): str,
            Optional('truncation_supported'): str,
            Optional('sequence_no_supported'): str,
            Optional('qos_supported'): str,
            Optional('destination_supported'): str,
            Optional('destination_max_no'): int,
        },
    }

class ShowCapabilityFeatureMonitorErspanSourceDestination(ShowCapabilityFeatureMonitorErspanSourceDestinationSchema):
    """Parser for show capability feature monitor erspan-source
       Parser for show capability feature monitor erspan-destination
    """

    cli_command = 'show capability feature monitor {target}'

    def cli(self, target=None, output=None):
        if output is None:
            cmd = self.cli_command.format(target=target)
            output = self.device.execute(cmd)

        # ERSPAN Source Session:ERSPAN Source Session Supported: TRUE
        p1 = re.compile(r"^ERSPAN\s+Source\s+Session:ERSPAN\s+Source\s+Session\s+Supported:\s+(?P<source_supported>\w+)$")

        # No of Rx ERSPAN source session: 8
        p1_1 = re.compile(r"^No\s+of\s+Rx\s+ERSPAN\s+source\s+session:\s+(?P<source_rx_session_no>\d+)$")

        # No of Tx ERSPAN source session: 8
        p1_2 = re.compile(r"^No\s+of\s+Tx\s+ERSPAN\s+source\s+session:\s+(?P<source_tx_session_no>\d+)$")

        # ERSPAN Header Type supported: II and III
        # ERSPAN Header Type supported: II
        p1_3 = re.compile(r"^ERSPAN\s+Header\s+Type\s+supported:\s+(?P<header_type>.+)$")

        # ACL filter Supported: TRUE
        p1_4 = re.compile(r"^ACL\s+filter\s+Supported:\s+(?P<acl_filter>\w+)$")

        # SGT filter Supported: TRUE
        p1_5 = re.compile(r"^SGT\s+filter\s+Supported:\s+(?P<sgt_filter>\w+)$")

        # Fragmentation Supported: TRUE
        p1_6 = re.compile(r"^Fragmentation\s+Supported:\s+(?P<fragmentation_supported>\w+)$")

        # Truncation Supported: TRUE
        p1_7 = re.compile(r"^Truncation\s+Supported:\s+(?P<truncation_supported>\w+)$")

        # Sequence number Supported: FALSE
        p1_8 = re.compile(r"^Sequence\s+number\s+Supported:\s+(?P<sequence_no_supported>\w+)$")

        # QOS Supported: TRUE
        p1_9 = re.compile(r"^QOS\s+Supported:\s+(?P<qos_supported>\w+)$")

        # ERSPAN Destination Session:ERSPAN Destination Session Supported: TRUE
        p1_10 = re.compile(r"^ERSPAN\s+Destination\s+Session:ERSPAN\s+Destination\s+Session\s+Supported:\s+(?P<destination_supported>\w+)$")

        # Maximum No of ERSPAN destination session: 8
        p1_11 = re.compile(r"^Maximum\s+No\s+of\s+ERSPAN\s+destination\s+session:\s+(?P<destination_max_no>\d+)$")

        ret_dict = {}

        for line in output.splitlines():

            line = line.strip()
            # ERSPAN Source Session:ERSPAN Source Session Supported: TRUE
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['source_supported'] = dict_val['source_supported']
                continue

            # No of Rx ERSPAN source session: 8
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['source_rx_session_no'] = int(dict_val['source_rx_session_no'])
                continue

            # No of Tx ERSPAN source session: 8
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['source_tx_session_no'] = int(dict_val['source_tx_session_no'])
                continue

            # ERSPAN Header Type supported: II and III
            m = p1_3.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['header_type'] = dict_val['header_type']
                continue

            # ACL filter Supported: TRUE
            m = p1_4.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['acl_filter'] = dict_val['acl_filter']
                continue

            # SGT filter Supported: TRUE
            m = p1_5.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['sgt_filter'] = dict_val['sgt_filter']
                continue

            # Fragmentation Supported: TRUE
            m = p1_6.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['fragmentation_supported'] = dict_val['fragmentation_supported']
                continue

            # Truncation Supported: TRUE
            m = p1_7.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['truncation_supported'] = dict_val['truncation_supported']
                continue

            # Sequence number Supported: FALSE
            m = p1_8.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['sequence_no_supported'] = dict_val['sequence_no_supported']
                continue

            # QOS Supported: TRUE
            m = p1_9.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['qos_supported'] = dict_val['qos_supported']
                continue

            # ERSPAN Destination Session:ERSPAN Destination Session Supported: TRUE
            m = p1_10.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['destination_supported'] = dict_val['destination_supported']
                continue

            # Maximum No of ERSPAN destination session: 8
            m = p1_11.match(line)
            if m:
                dict_val = m.groupdict()
                erspan_capability = ret_dict.setdefault('erspan_capability', {})
                erspan_capability['destination_max_no'] = int(dict_val['destination_max_no'])
                continue


        return ret_dict

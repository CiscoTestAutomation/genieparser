"""show_segment_routing.py

NX-OS parsers for the following show commands:
    * show segment-routing mpls
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ====================================================================
# Schema for 'show segment-routing mpls'
# ====================================================================
class ShowSegmentRoutingMplsSchema(MetaParser):
    """Schema for show segment-routing mpls"""

    schema = {
        'service_name': str,
        'state': str,
        'process_id': int,
        Optional('configured_srgb'): {
            'start': int,
            'end': int,
        },
        Optional('srgb_allocation_status'): str,
        Optional('current_srgb'): {
            'start': int,
            'end': int,
        },
        Optional('cleanup_interval'): int,
        Optional('retry_interval'): int,
    }


# ====================================================================
# Parser for 'show segment-routing mpls'
# ====================================================================
class ShowSegmentRoutingMpls(ShowSegmentRoutingMplsSchema):
    """Parser for show segment-routing mpls"""

    cli_command = 'show segment-routing mpls'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Segment-Routing Mpls Global info
        p1 = re.compile(r'^Segment-Routing +Mpls +Global +info$')

        # Service Name: segment-routing
        p2 = re.compile(r'^Service +Name: +(?P<service_name>\S+)$')

        # State: Not-Configured-Yet
        p3 = re.compile(r'^State: +(?P<state>\S+)$')

        # Process Id: 24564
        p4 = re.compile(r'^Process +Id: +(?P<process_id>\d+)$')

        # Configured SRGB: 16000 - 40000
        p5 = re.compile(
            r'^(?P<srgb_type>Configured|Current) +SRGB: '
            r'(?P<start>\d+) +- +(?P<end>\d+)$'
        )

        # SRGB Allocation status: Alloc-Successful
        p6 = re.compile(
            r'^SRGB +Allocation +status: '
            r'(?P<srgb_allocation_status>\S+)$'
        )

        # Cleanup Interval: 60
        p7 = re.compile(
            r'^(?P<interval_type>Cleanup|Retry) +Interval: '
            r'(?P<interval>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Segment-Routing Mpls Global info
            m = p1.match(line)
            if m:
                continue

            # Service Name: segment-routing
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['service_name'] = groups['service_name']
                continue

            # State: Not-Configured-Yet
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['state'] = groups['state']
                continue

            # Process Id: 24564
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['process_id'] = int(groups['process_id'])
                continue

            # Configured SRGB: 16000 - 40000
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                srgb_type = groups['srgb_type'].lower()
                ret_dict[srgb_type + '_srgb'] = {
                    'start': int(groups['start']),
                    'end': int(groups['end']),
                }
                continue

            # SRGB Allocation status: Alloc-Successful
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['srgb_allocation_status'] = (
                    groups['srgb_allocation_status']
                )
                continue

            # Cleanup Interval: 60
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                interval_type = groups['interval_type'].lower()
                ret_dict[interval_type + '_interval'] = int(
                    groups['interval']
                )
                continue

        return ret_dict

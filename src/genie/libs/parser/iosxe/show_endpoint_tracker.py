"""show_endpoint_tracker.py
IOSXE parser for the following show commands:
    * 'show endpoint-tracker records'
    * 'show endpoint-tracker static-route'
    * 'show endpoint-tracker tracker-group'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================================================
# Parser Schema for 'show endpoint-tracker records '
# ===================================================
class ShowEndpointTrackerRecordsSchema(MetaParser):
    """Schema for "show endpoint-tracker records" """

    schema = {
        'record_name': {
            Any(): {
                'endpoint': str,
                'endpoint_type': str,
                'threshold': str,
                'multiplier': str,
                'interval': str,
                'tracker_type': str
            }
        }
    }


# =============================================
# Parser for 'show endpoint-tracker records'
# =============================================

class ShowEndpointTrackerRecords(ShowEndpointTrackerRecordsSchema):
    """ parser for "show endpoint-tracker records" """

    cli_command = "show endpoint-tracker records"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # group-udp-tcp-10001     tcp-10002 OR udp-10002      N/A      N/A      N/A      N/A       tracker-group
        # nat-dia-tracker-4351    151.151.151.1               IP       300      3         60        interface
        # track3                  www.diatracker.com          DNS_NAME 300      3          60       interface

        p1 = re.compile(
            r'^(?P<record_name>[a-z0-9-]+)\s+(?P<endpoint>[a-z0-9-.]+\sOR\s+[a-z0-9-.]+|[a-z0-9-.]+)\s+'
            r'(?P<endpoint_type>[A-Z]+|[A-Z\/_]+)\s+(?P<threshold>\d+|[A-Z\/]+)\s+(?P<multiplier>\d+|[A-Z\/]+)\s+'
            r'(?P<interval>\d+|[A-Z\/]+)\s+(?P<tracker_type>[a-z-]+)$')

        for line in output.splitlines():
            line = line.strip()

            # group-udp-tcp-10001       tcp-10002 OR udp-10002      N/A      N/A      N/A    N/A    tracker-group
            # nat-dia-tracker-4351      151.151.151.1               IP       300       3     60     interface
            # track3                    www.diatracker.com          DNS_NAME 300       3     60     interface

            m = p1.match(line)
            if m:
                group = m.groupdict()
                record_name = group.pop("record_name")

                record_name_dict = parsed_dict.setdefault("record_name", {}). \
                    setdefault(record_name, {})

                record_name_dict.update({k: v for k, v in group.items()})

        return parsed_dict


# =======================================================
# Parser Schema for 'show endpoint-tracker static-route '
# =======================================================

class ShowEndpointTrackerStaticRouteSchema(MetaParser):
    """Schema for "show endpoint-tracker static-route" """

    schema = {
        'tracker_name': {
            Any(): {
                'status': str,
                'rtt_in_msec': int,
                'probe_id': int,
            }
        }
    }


# =================================================
# Parser for 'show endpoint-tracker static-route'
# =================================================

class ShowEndpointTrackerStaticRoute(ShowEndpointTrackerStaticRouteSchema):
    """ parser for "show endpoint-tracker static-route" """

    cli_command = "show endpoint-tracker static-route"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # tcp-10001       UP        2                2
        p1 = re.compile(
            r'^(?P<tracker_name>[a-z0-9-]+)\s+(?P<status>[A-Z]+)\s+(?P<rtt_in_msec>\d+)\s+(?P<probe_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # tcp-10001       UP        2                2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tracker_name = group.pop("tracker_name")
                tracker_status = group.pop("status")

                tracker_name_dict = parsed_dict.setdefault("tracker_name", {}). \
                    setdefault(tracker_name, {})
                
                tracker_name_dict["status"] = tracker_status
                tracker_name_dict.update({k: int(v) for k, v in group.items()})

        return parsed_dict


# =========================================================
# Parser Schema for 'show endpoint-tracker tracker-group  '
# =========================================================


class ShowEndpointTrackerTrackerGroupSchema(MetaParser):
    """Schema for "show endpoint-tracker tracker-group " """

    schema = {
        'tracker_name': {
            Any(): {
                'element_trackers_name': str,
                'status': str,
                'rtt_in_msec': str,
                'probe_id': str,
            }
        }
    }


# ==================================================
# Parser for 'show endpoint-tracker tracker-group '
# ==================================================

class ShowEndpointTrackerTrackerGroup(ShowEndpointTrackerTrackerGroupSchema):
    """ parser for "show endpoint-tracker tracker-group " """

    cli_command = "show endpoint-tracker tracker-group"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # group-udp-tcp-10001    tcp-10002, udp-10002    UP(UP OR UP)             1, 1             7, 8
        # group5                 track1, track2          DOWN(DOWN OR DOWN)       Timeout, Timeout 0, 0
        # group4                 track1, track2          UP(UP OR UP)             14, 14           201, 202

        p1 = re.compile(
            r'^(?P<tracker_name>[a-z0-9-]+)+\s+(?P<element_trackers_name>[a-z0-9-]+,\s+[a-z0-9-]+|[a-z0-9-])\s+'
            r'(?P<status>[A-Z]+\(([A-Z ]+)\))\s+(?P<rtt_in_msec>\w+,+ \w+|\w+)+\s+(?P<probe_id>\w+,+ \w+)$')

        for line in output.splitlines():
            line = line.strip()

            # group-udp-tcp-10001    tcp-10002, udp-10002   UP(UP OR UP)             1, 1             7, 8
            # group5                 track1, track2         DOWN(DOWN OR DOWN)       Timeout, Timeout 0, 0
            # group4                 track1, track2         UP(UP OR UP)             14, 14           201, 202
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tracker_name = group.pop("tracker_name")

                tracker_name_dict = parsed_dict.setdefault("tracker_name", {}). \
                    setdefault(tracker_name, {})

                tracker_name_dict.update({k: v for k, v in group.items()})

        return parsed_dict

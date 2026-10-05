"""show_icam.py

NXOS parsers for the following show commands:
    * 'show icam scale multicast-routing'
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================================================================
# Schema for 'show icam scale multicast-routing'
# ====================================================================
class ShowIcamScaleMulticastRoutingSchema(MetaParser):
    """Schema for show icam scale multicast-routing"""

    schema = {
        Optional('thresholds'): {
            Optional('info_percent'): int,
            Optional('warning_percent'): int,
            Optional('critical_percent'): int,
        },
        Optional('timestamp_timezone'): str,
        Optional('scale_limits'): {
            Any(): {
                'feature': str,
                'verified_scale': int,
                'config_scale': int,
                'current_scale': int,
                'current_util_percent': float,
                'threshold_exceeded': str,
                'polled_timestamp': str,
                Optional('vdc'): {
                    Any(): {
                        'current_scale': int,
                        'current_util_percent': float,
                        'threshold_exceeded': str,
                        'polled_timestamp': str,
                    },
                },
            },
        },
    }


# ====================================================================
# Parser for 'show icam scale multicast-routing'
# ====================================================================
class ShowIcamScaleMulticastRouting(ShowIcamScaleMulticastRoutingSchema):
    """Parser for show icam scale multicast-routing"""

    cli_command = 'show icam scale multicast-routing'

    @staticmethod
    def _normalize_feature_key(feature):
        key = feature.lower()
        key = key.replace('*,g', 'star_g')
        key = key.replace('s,g', 's_g')
        return re.sub(r'[^a-z0-9]+', '_', key).strip('_')

    def cli(self, command, output=None):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}
        current_feature_dict = None

        # Retrieving data.  This may take some time ...
        p1 = re.compile(
            r'^Retrieving +data\. +This +may +take +some +time +\.\.\.$')

        # Info Threshold =  80 percent (default)           |
        p2 = re.compile(
            r'^Info +Threshold += +(?P<info_percent>\d+) +percent +'
            r'\(default\) *\|$')

        # Warning Threshold =  90 percent (default)        |
        p3 = re.compile(
            r'^Warning +Threshold += +(?P<warning_percent>\d+) +percent +'
            r'\(default\) *\|$')

        # Critical Threshold = 100 percent (default)       |
        p4 = re.compile(
            r'^Critical +Threshold += +(?P<critical_percent>\d+) +percent +'
            r'\(default\) *\|$')

        # All timestamps are in UTC                        |
        p5 = re.compile(
            r'^All +timestamps +are +in +(?P<timestamp_timezone>\S+) *\|$')

        # ==================================================
        # ----------
        p6 = re.compile(r'^[=-]+$')

        # Scale Limits for Multicast Routing
        p7 = re.compile(r'^Scale +Limits +for +Multicast +Routing$')

        # Feature Verified Config Cur Cur Threshold Polled
        p8 = re.compile(
            r'^Feature +Verified +Config +Cur +Cur +Threshold +Polled$')

        # Scale     Scale     Scale    Util    Exceeded            Timestamp
        p9 = re.compile(
            r'^Scale +Scale +Scale +Util +Exceeded +Timestamp$')

        # Multicast Routes 8192 8192 1 0.01 None 2026-09-10 12:03:32
        # IPv4 Mcast *,G Routes 8192 8192 0 0.00 None 2026-09-10 12:03:32
        p10 = re.compile(
            r'^(?P<feature>[A-Za-z0-9*,][A-Za-z0-9 *,]+?) +'
            r'(?P<verified_scale>\d+) +(?P<config_scale>\d+) +'
            r'(?P<current_scale>\d+) +(?P<current_util_percent>\d+\.\d+) +'
            r'(?P<threshold_exceeded>\S+) +'
            r'(?P<polled_timestamp>\d{4}-\d{2}-\d{2} +'
            r'\d{2}:\d{2}:\d{2})$')

        # (VDC:1) - - 1 0.01 None 2026-09-10 12:03:32
        p11 = re.compile(
            r'^\(VDC:(?P<vdc>\d+)\) +- +- +(?P<current_scale>\d+) +'
            r'(?P<current_util_percent>\d+\.\d+) +'
            r'(?P<threshold_exceeded>\S+) +'
            r'(?P<polled_timestamp>\d{4}-\d{2}-\d{2} +'
            r'\d{2}:\d{2}:\d{2})$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Retrieving data.  This may take some time ...
            m = p1.match(line)
            if m:
                continue

            # Info Threshold =  80 percent (default)           |
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                thresholds_dict = ret_dict.setdefault('thresholds', {})
                thresholds_dict['info_percent'] = int(groups['info_percent'])
                continue

            # Warning Threshold =  90 percent (default)        |
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                thresholds_dict = ret_dict.setdefault('thresholds', {})
                thresholds_dict['warning_percent'] = int(
                    groups['warning_percent'])
                continue

            # Critical Threshold = 100 percent (default)       |
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                thresholds_dict = ret_dict.setdefault('thresholds', {})
                thresholds_dict['critical_percent'] = int(
                    groups['critical_percent'])
                continue

            # All timestamps are in UTC                        |
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['timestamp_timezone'] = groups['timestamp_timezone']
                continue

            # Separator lines
            m = p6.match(line)
            if m:
                continue

            # Scale Limits for Multicast Routing
            m = p7.match(line)
            if m:
                continue

            # Table header lines
            m = p8.match(line)
            if m:
                continue

            m = p9.match(line)
            if m:
                continue

            # Multicast Routes 8192 8192 1 0.01 None 2026-09-10 12:03:32
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                feature = groups['feature'].strip()
                feature_key = self._normalize_feature_key(feature)

                current_feature_dict = ret_dict.setdefault(
                    'scale_limits', {}).setdefault(feature_key, {})

                current_feature_dict.update({
                    'feature': feature,
                    'verified_scale': int(groups['verified_scale']),
                    'config_scale': int(groups['config_scale']),
                    'current_scale': int(groups['current_scale']),
                    'current_util_percent':
                        float(groups['current_util_percent']),
                    'threshold_exceeded': groups['threshold_exceeded'],
                    'polled_timestamp': groups['polled_timestamp'],
                })
                continue

            # (VDC:1) - - 1 0.01 None 2026-09-10 12:03:32
            m = p11.match(line)
            if m and current_feature_dict is not None:
                groups = m.groupdict()
                vdc_dict = current_feature_dict.setdefault(
                    'vdc', {}).setdefault(int(groups['vdc']), {})

                vdc_dict.update({
                    'current_scale': int(groups['current_scale']),
                    'current_util_percent':
                        float(groups['current_util_percent']),
                    'threshold_exceeded': groups['threshold_exceeded'],
                    'polled_timestamp': groups['polled_timestamp'],
                })
                continue

        return ret_dict

''' show_flow.py

IOSXE parsers for the following show commands:
    * show flow monitor 
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, ListOf, Optional, And, Default, Use

# Common
from genie.libs.parser.utils.common import Common

# =================================================
# Schema for:
#   * 'show flow monitor'
# ==================================================

class ShowFlowMonitorSchema(MetaParser):
    schema = {
        'flow_monitor': {
            Any(): {
                'description': str,
                'flow_record': str,
                Optional('flow_exporter'): str,
                'cache': {
                    'type': str,
                    'status': str,
                    'size': int,
                    'inactive_timeout': int,
                    'active_timeout': int,
                }
            },
        }
    }


# ===================================
# Parser for:
#   * 'show flow monitor'
# ===================================

class ShowFlowMonitor(ShowFlowMonitorSchema):
    cli_command = 'show flow monitor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Flow Monitor v4_mon_sgt-output:
        p1 = re.compile(r'^Flow\sMonitor\s(?P<flow_monitor>[\w\-]+)\:$')

        # Description:       User defined
        p2 = re.compile(r'^Description:\s+(?P<description>[\w\s\.]+)$')

        # Flow Record:       v4-rec_sgt-output
        p3 = re.compile(r'^Flow\sRecord:\s+(?P<flow_record>[\S\s]+)$')

        # Flow Exporter:     StealthWatch_Exporter
        p4 = re.compile(r'^Flow\sExporter:\s+(?P<flow_exporter>\S+)$')

        # Cache
        p5 = re.compile(r'^(?P<cache>Cache)\:$')

        # Type:                 normal (Platform cache)
        p6 = re.compile(r'^Type:\s+(?P<type>.*)$')

        # Status:               not allocated
        p7 = re.compile(r'^Status:\s+(?P<status>[\w\s]+)$')

        # Size:                 10000 entries
        p8 = re.compile(r'^Size:\s+(?P<size>\d+)\sentries$')

        # Inactive Timeout:     15 secs
        p9 = re.compile(r'^Inactive\sTimeout:\s+(?P<inactive_timeout>\d+)\ssecs$')

        # Active Timeout:       60 secs
        p10 = re.compile(r'^Active\sTimeout:\s+(?P<active_timeout>\d+)\ssecs$')

        for line in out.splitlines():
            line = line.strip()

            # Flow Monitor v4_mon_sgt-output:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_monitor = group['flow_monitor']
                flow_dict = ret_dict.setdefault('flow_monitor', {}).setdefault(flow_monitor, {})
                continue

            # Description:       User defined
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            # Flow Record:       v4-rec_sgt-output
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['flow_record'] = group['flow_record']
                continue

            # Flow Exporter:     StealthWatch_Exporter
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['flow_exporter'] = group['flow_exporter']
                continue

            # Cache
            m = p5.match(line)
            if m:
                group = m.groupdict()
                cache_dict = flow_dict.setdefault('cache', {})
                continue

            # Type:                 normal (Platform cache)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cache_dict['type'] = group['type']
                continue

            # Status:               not allocated
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cache_dict['status'] = group['status']
                continue

            # Size:                 10000 entries
            m = p8.match(line)
            if m:
                group = m.groupdict()
                cache_dict['size'] = int(group['size'])
                continue

            # Inactive Timeout:     15 secs
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cache_dict['inactive_timeout'] = int(group['inactive_timeout'])
                continue

            # Active Timeout:       60 secs
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cache_dict['active_timeout'] = int(group['active_timeout'])
                continue

        return ret_dict


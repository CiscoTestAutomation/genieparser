''' show_flow.py

IOSXE parsers for the following show commands:
    * show flow monitor {name} cache format table
    * show flow exporter statistics
    * show flow exporter {exporter} statistics
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# =========================================================
# Schema for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitorSchema(MetaParser):
    ''' Schema for "show flow monitor {name} cache format table" '''

    schema = {
        'cache_type': str,
        'cache_size': int,
        'current_entries': int,
        'high_water_mark': int,
        'flows_added': int,
        'flows_aged': int,
        'ipv4_src_addr': {
            Any(): {
                'ipv4_dst_addr': {
                    Any(): {
                        'index': {
                            Any(): {
                                'trns_src_port': int,
                                'trns_dst_port': int,
                                'ip_tos': str,
                                'ip_port': int,
                                'bytes_long': int,
                                'pkts_long': int,
                            }
                        }
                    }
                }
            }
        }
    }

# =========================================================
# Parser for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitor(ShowFlowMonitorSchema):
    ''' Parser for
      "show flow monitor {name} cache format table"
    '''

    cli_command = 'show flow monitor {name} cache format table'

    def cli(self, name, output=None):
        if output is None:
            cmd = self.cli_command.format(name=name)
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        dst_addr_index = {}

        # Cache type:                               Normal (Platform cache)
        p1 = re.compile(r'^Cache +type: +(?P<cache_type>[\S\s]+)$')
        
        # Cache size:                                   16
        p2 = re.compile(r'^Cache +size: +(?P<cache_size>\d+)$')

        # Current entries:                               1
        p3 = re.compile(r'^Current +entries: +(?P<current_entries>\d+)$')

        # High Watermark:                                1
        p4 = re.compile(r'^High +Watermark: +(?P<high_water_mark>\d+)$')

        # Flows added:                                   1
        p5 = re.compile(r'^Flows +added: +(?P<flows_added>\d+)$')

        # Flows aged:                                   0
        p6 = re.compile(r'^Flows +aged: +(?P<flows_aged>\d+)$')

        # 1.1.1.10         22.10.10.1                    0              0  0xC0         89                   100                     1
        p7 = re.compile(r'^(?P<ipv4_src_addr>\S+) +(?P<ipv4_dst_addr>\S+) +'
                        '(?P<trns_src_port>\d+) +(?P<trns_dst_port>\d+) +'
                        '(?P<ip_tos>\S+) +(?P<ip_port>\d+) +(?P<bytes_long>\d+) +'
                        '(?P<pkts_long>\d+)$')
        for line in out.splitlines():

            line = line.strip()
            
            # Cache type:                               Normal (Platform cache)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_type': group['cache_type']})
                continue
            
            # Cache size:                                   16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_size': int(group['cache_size'])})
                continue
            
            # Current entries:                               1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_entries': int(group['current_entries'])})
                continue

            # High Watermark:                                1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'high_water_mark': int(group['high_water_mark'])})
                continue
            
            # Flows added:                                   1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_added': int(group['flows_added'])})
                continue
            
            # Flows aged:                                   0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_aged': int(group['flows_aged'])})
                continue
            
            # 1.1.1.10         22.10.10.1                    0              0  0xC0         89                   100                     1
            m = p7.match(line)
            if m:
                group = m.groupdict()

                index = dst_addr_index.get(group['ipv4_dst_addr'], 0) + 1
                
                ipv4_dst_addr_dict = ret_dict.setdefault('ipv4_src_addr', {}).\
                    setdefault(group['ipv4_src_addr'], {}).\
                    setdefault('ipv4_dst_addr', {}).\
                    setdefault(group['ipv4_dst_addr'], {}).\
                    setdefault('index', {}).\
                    setdefault(index, {})

                ipv4_dst_addr_dict.update({'trns_src_port': int(group['trns_src_port'])})
                ipv4_dst_addr_dict.update({'trns_dst_port': int(group['trns_dst_port'])})
                ipv4_dst_addr_dict.update({'ip_tos': group['ip_tos']})
                ipv4_dst_addr_dict.update({'ip_port': int(group['ip_port'])})
                ipv4_dst_addr_dict.update({'bytes_long': int(group['bytes_long'])})
                ipv4_dst_addr_dict.update({'pkts_long': int(group['pkts_long'])})

                dst_addr_index.update({group['ipv4_dst_addr']: index})

                continue

        return ret_dict


class ShowFlowExporterStatisticsSchema(MetaParser):
    """ Schema for:
            * show flow exporter statistics
            * show flow exporter {exporter} statistics
    """
    schema = {
        'flow_exporter': {
            Any(): {
                'pkt_send_stats': {
                    'last_cleared': str,
                    Optional(Any()): int
                },
                'client_send_stats': {
                    Any(): {
                        'records_added': {
                            'total': int,
                            Optional('sent'): int,
                            Optional('failed'): int
                        },
                        'bytes_added': {
                            'total': int,
                            Optional('sent'): int,
                            Optional('failed'): int
                        }
                    }
                }
            }
        }
    }


class ShowFlowExporterStatistics(ShowFlowExporterStatisticsSchema):
    """ Parser for:
            * show flow exporter statistics
            * show flow exporter {exporter} statistics
    """

    cli_command = ["show flow exporter statistics",
                   "show flow exporter {exporter} statistics"]

    def cli(self, exporter=None, output=None):

        if not output:
            if not exporter:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(self.cli_command[1].format(exporter=exporter))

        # Flow Exporter test
        p1 = re.compile(r"^Flow +Exporter +(?P<exporter>\w+):$")

        # Packet send statistics (last cleared 00:10:10 ago):
        p2 = re.compile(r"^Packet +send +statistics +\(last +cleared +(?P<last_cleared>[\d:]+) +ago\):$")

        # Successfully sent:         10                     (1000 bytes)
        # No FIB:                    10                     (1000 bytes)
        # Adjacency failure:         10                     (1000 bytes)
        # Enqueued to process level: 10                     (1000 bytes)
        # Enqueueing failed:         10                     (1000 bytes)
        # IPC failed:                10                     (1000 bytes)
        # Output failed:             10                     (1000 bytes)
        # Fragmentation failed:      10                     (1000 bytes)
        # Encap fixup failed:        10                     (1000 bytes)
        # CEF not enabled:           10                     (1000 bytes)
        # Reason not given:          10                     (1000 bytes)
        # Rate limited:              10                     (1000 bytes)
        # No destination address:    10                     (1000 bytes)
        p3 = re.compile(r"^(?P<statistic>[\w\s]+): +(?P<pkts>\d+) +\((?P<bytes>\d+) +bytes\)$")

        # Client: client_name
        p4 = re.compile(r"^Client: +(?P<client>[\S\s]+)$")

        # Records added:             10
        p5 = re.compile(r"^Records +added: +(?P<total>\d+)$")

        # Bytes added:               10
        p6 = re.compile(r"^Bytes +added: +(?P<total>\d+)$")

        # - sent:                20
        p7 = re.compile(r"^- +sent: +(?P<sent>\d+)$")

        # - failed to send:      30
        p8 = re.compile(r"^- +failed +to +send: +(?P<failed>\d+)$")

        records_flag = False
        bytes_flag = False
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Flow Exporter test
            m = p1.match(line)
            if m:
                exporter_dict = ret_dict.setdefault('flow_exporter', {})\
                                        .setdefault(m.groupdict()['exporter'], {})
                continue

            # Packet send statistics (last cleared 00:10:10 ago):
            m = p2.match(line)
            if m:
                pkt_stats_dict = exporter_dict.setdefault('pkt_send_stats', {})
                pkt_stats_dict.update({'last_cleared': m.groupdict()['last_cleared']})
                continue

            # Successfully sent:         10                     (1000 bytes)
            # No FIB:                    10                     (1000 bytes)
            # Adjacency failure:         10                     (1000 bytes)
            # Enqueued to process level: 10                     (1000 bytes)
            # Enqueueing failed:         10                     (1000 bytes)
            # IPC failed:                10                     (1000 bytes)
            # Output failed:             10                     (1000 bytes)
            # Fragmentation failed:      10                     (1000 bytes)
            # Encap fixup failed:        10                     (1000 bytes)
            # CEF not enabled:           10                     (1000 bytes)
            # Reason not given:          10                     (1000 bytes)
            # Rate limited:              10                     (1000 bytes)
            # No destination address:    10                     (1000 bytes)
            m = p3.match(line)
            if m:
                key = re.sub(' ', '_', m.groupdict()['statistic']).lower()
                bytes_key = '{key}_bytes'.format(key=key)
                pkt_stats_dict.update({key: int(m.groupdict()['pkts'])})
                pkt_stats_dict.update({bytes_key: int(m.groupdict()['bytes'])})
                continue

            # Client: client_name
            m = p4.match(line)
            if m:
                client_dict = exporter_dict.setdefault('client_send_stats', {})\
                                           .setdefault(m.groupdict()['client'], {})
                continue

            # Records added:             10
            m = p5.match(line)
            if m:
                records_flag = True
                bytes_flag = False

                records_dict = client_dict.setdefault('records_added', {})
                records_dict.update({'total': int(m.groupdict()['total'])})
                continue

            # Bytes added:               10
            m = p6.match(line)
            if m:
                records_flag = False
                bytes_flag = True

                bytes_dict = client_dict.setdefault('bytes_added', {})
                bytes_dict.update({'total': int(m.groupdict()['total'])})
                continue

            # - sent:                20
            m = p7.match(line)
            if m:
                if records_flag:
                    records_dict.update({'sent': int(m.groupdict()['sent'])})
                elif bytes_flag:
                    bytes_dict.update({'sent': int(m.groupdict()['sent'])})
                continue

            # - failed to send:      30
            m = p8.match(line)
            if m:
                if records_flag:
                    records_dict.update({'failed': int(m.groupdict()['failed'])})
                elif bytes_flag:
                    bytes_dict.update({'failed': int(m.groupdict()['failed'])})

        return ret_dict


# Python
from contextlib import redirect_stderr
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

''' show_pm.py

IOSXE parsers for the following show commands:

    ----------------------------------------------------------------------------
    * 'show performance-measurement responder counters interface'
    * 'show performance-measurement responder counters interface {name}'
    * 'show performance-measurement responder interfaces'
    * 'show performance-measurement responder interfaces name {name}'
    * 'show performance-measurement responder summary'
    ----------------------------------------------------------------------------
'''

# ====================
# Schema for:
#   * 'show performance-measurement responder interfaces'
#   * 'show performance-measurement responder interfaces name {name}'
# ====================
class ShowPerformanceMeasurementResponderInterfacesSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder interfaces'
        * 'show performance-measurement responder interfaces name {name}'
    '''
    schema = {
        Any(): {  # Interface name
            'interface_handle': str,
            'local_ipv4_address': str,
            'local_ipv6_address': str,
            'current_rate': int,
            'rate_high_water_mark': int,
            'cleanup_time_remaining': int,
            Optional('loss_color_type'): str,
            Optional('loss_color_inact_remain'): int
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder interfaces'
#   * 'show performance-measurement responder interfaces name {name}'
# ====================
class ShowPerformanceMeasurementResponderInterfaces(ShowPerformanceMeasurementResponderInterfacesSchema):
    '''Parser for:
        * 'show performance-measurement responder interfaces',
        * 'show performance-measurement responder interfaces name {name}'

    '''
    cli_command = [
        'show performance-measurement responder interfaces',
        'show performance-measurement responder interfaces name {name}'
    ]

    def cli(self, name=None, output=None):

        if not output:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Interface Name: Ethernet0/1
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')

        # Interface Handle        : 0x3
        p2 = re.compile(r'^Interface Handle\s+: (?P<interface_handle>\S+)$')

        # Local IPV4 Address      : 110.1.1.3
        p3 = re.compile(r'^Local IPV4 Address\s+: (?P<local_ipv4_address>[\d\.]+)$')

        # Local IPV6 Address      : ::
        p4 = re.compile(r'^Local IPV6 Address\s+: (?P<local_ipv6_address>[\d:A-F]+)$')

        # Current rate            : 0 pkts/sec
        p5 = re.compile(r'^Current rate\s+: (?P<current_rate>\d+) pkts/sec$')

        # Rate high water mark    : 0 pkts/sec
        p6 = re.compile(r'^Rate high water mark\s+: (?P<rate_high_watermark>\d+) pkts/sec$')

        # Cleanup time remaining  : 3599 sec
        p7 = re.compile(r'^Cleanup time remaining\s+: (?P<cleanup_time_remaining>\d+) sec$')

        # Loss color type         : dual-color gre
        p8 = re.compile(r'^Loss color type\s+: (?P<loss_color_type>.+)$')

        # Loss color inact remain : 1006 sec
        p9 = re.compile(r'^Loss color inact remain\s+: (?P<loss_color_inact_remain>\d+) sec$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Ethernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group['interface_name']
                ret_dict.setdefault(intf_name, {})
                continue

            # Interface Handle        : 0x3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('interface_handle', group['interface_handle'])
                continue

            # Local IPV4 Address      : 110.1.1.3
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv4_address', group['local_ipv4_address'])
                continue

            # Local IPV6 Address      : ::
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv6_address', group['local_ipv6_address'])
                continue

            # Current rate            : 0 pkts/sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('current_rate', int(group['current_rate']))
                continue

            # Rate high water mark    : 0 pkts/sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('rate_high_water_mark', int(group['rate_high_watermark']))
                continue

            # Cleanup time remaining  : 3599 sec
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('cleanup_time_remaining', int(group['cleanup_time_remaining']))
                continue

            # Loss color type         : dual-color gre
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('loss_color_type', group['loss_color_type'])
                continue

            # Loss color inact remain : 1006 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('loss_color_inact_remain', int(group['loss_color_inact_remain']))
                continue


        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement responder counters interface'
#   * 'show performance-measurement responder counters interface {name}'
# ====================
class ShowPerformanceMeasurementResponderCountersSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder counters interface'
        * 'show performance-measurement responder counters interface {name}'
    '''
    schema = {
        Any(): {  # Interface name
            'total_query_packets_received': int,
            'total_reply_packets_sent': int,
            'total_reply_packets_sent_errors': int,
            'total_uro_tlv_not_present_errors': int,
            'total_invalid_port_number_errors': int,
            'total_no_source_address_errors': int,
            'total_no_return_path_errors': int,
            'total_unsupported_querier_control_code_errors': int,
            'total_unsupported_timestamp_format_errors': int,
            'total_timestamp_not_available_errors': int,
            'total_unsupported_mandatory_tlv_errors': int,
            'total_invalid_packet_errors': int,
            Optional('total_loss_probe_color_errors'): int
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder counters interface'
#   * 'show performance-measurement responder counters interface name {name}'
# ====================
class ShowPerformanceMeasurementResponderCounters(ShowPerformanceMeasurementResponderCountersSchema):
    '''Parser for:
        * 'show performance-measurement responder counters interface'
        * 'show performance-measurement responder counters interface name {name}'
    '''
    cli_command = [
        'show performance-measurement responder counters interface',
        'show performance-measurement responder counters interfaces name {name}'
    ]

    def cli(self, name=None, output=None):

        if not output:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)


        # Interface Name: Ethernet0/1
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')
        
        #     Total query packets received                  : 23304
        p2 = re.compile(r'^Total query packets received\s+: (?P<total_query_packets_received>\d+)$')

        #     Total reply packets sent                      : 23302
        p3 = re.compile(r'^Total reply packets sent\s+: (?P<total_reply_packets_sent>\d+)$')

        #     Total reply packets sent errors               : 2
        p4 = re.compile(r'^Total reply packets sent errors\s+: (?P<total_reply_packets_sent_errors>\d+)$')

        #     Total URO TLV not present errors              : 0
        p5 = re.compile(r'^Total URO TLV not present errors\s+: (?P<total_uro_tlv_not_present_errors>\d+)$')

        #     Total invalid port number errors              : 0
        p6 = re.compile(r'^Total invalid port number errors\s+: (?P<total_invalid_port_number_errors>\d+)$')

        #     Total no source address errors                : 0
        p7 = re.compile(r'^Total no source address errors\s+: (?P<total_no_source_address_errors>\d+)$')

        #     Total no return path errors                   : 0
        p8 = re.compile(r'^Total no return path errors\s+: (?P<total_no_return_path_errors>\d+)$')

        #     Total unsupported querier control code errors : 0
        p9 = re.compile(r'^Total unsupported querier control code errors\s+: (?P<total_unsupported_querier_control_code_errors>\d+)$')

        #     Total unsupported timestamp format errors     : 0
        p10 = re.compile(r'^Total unsupported timestamp format errors\s+: (?P<total_unsupported_timestamp_format_errors>\d+)$')

        #     Total timestamp not available errors          : 0
        p11 = re.compile(r'^Total timestamp not available errors\s+: (?P<total_timestamp_not_available_errors>\d+)$')

        #     Total unsupported mandatory TLV errors        : 0
        p12 = re.compile(r'^Total unsupported mandatory TLV errors\s+: (?P<total_unsupported_mandatory_tlv_errors>\d+)$')

        #     Total invalid packet errors                   : 0
        p13 = re.compile(r'^Total invalid packet errors\s+: (?P<total_invalid_packet_errors>\d+)$')

        #     Total loss probe color errors                 : 2
        p14 = re.compile(r'^Total loss probe color errors\s+: (?P<total_loss_probe_color_errors>\d+)$')


        intf_name = ''
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Ethernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group['interface_name']
                ret_dict.setdefault(intf_name, {})
                continue

            #     Total query packets received                  : 23304
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_query_packets_received', int(group['total_query_packets_received']))
                continue

            #     Total reply packets sent                      : 23302
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_reply_packets_sent', int(group['total_reply_packets_sent']))
                continue

            #     Total reply packets sent errors               : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_reply_packets_sent_errors', int(group['total_reply_packets_sent_errors']))
                continue

            #     Total URO TLV not present errors              : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_uro_tlv_not_present_errors', int(group['total_uro_tlv_not_present_errors']))
                continue

            #     Total invalid port number errors              : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_invalid_port_number_errors', int(group['total_invalid_port_number_errors']))
                continue

            #     Total no source address errors                : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_no_source_address_errors', int(group['total_no_source_address_errors']))
                continue

            #     Total no return path errors                   : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_no_return_path_errors', int(group['total_no_return_path_errors']))
                continue

            #     Total unsupported querier control code errors : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_querier_control_code_errors', int(group['total_unsupported_querier_control_code_errors']))
                continue

            #     Total unsupported timestamp format errors     : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_timestamp_format_errors', int(group['total_unsupported_timestamp_format_errors']))
                continue

            #     Total timestamp not available errors          : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_timestamp_not_available_errors', int(group['total_timestamp_not_available_errors']))
                continue

            #     Total unsupported mandatory TLV errors        : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_mandatory_tlv_errors', int(group['total_unsupported_mandatory_tlv_errors']))
                continue

            #     Total invalid packet errors                   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_invalid_packet_errors', int(group['total_invalid_packet_errors']))
                continue

            #     Total loss probe color errors                 : 2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_loss_probe_color_errors', int(group['total_loss_probe_color_errors']))
                continue

        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement responder summary'
# ====================
class ShowPerformanceMeasurementResponderSummarySchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder summary'
    '''
    schema = {
            'total_interfaces': int,
            'total_query_packets_received': int,
            'total_reply_packets_sent': int,
            'total_reply_packets_sent_errors': int,
            'total_uro_tlv_not_present_errors': int,
            'total_invalid_port_number_errors': int,
            'total_no_source_address_errors': int,
            'total_no_return_path_errors': int,
            'total_unsupported_querier_control_code_errors': int,
            'total_unsupported_timestamp_format_errors': int,
            'total_timestamp_not_available_errors': int,
            'total_unsupported_mandatory_tlv_errors': int,
            'total_invalid_packet_errors': int,
            Optional('total_loss_probe_color_errors'): int,
            'current_rate': int,
            'rate_high_water_mark': int
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder summary'
# ====================
class ShowPerformanceMeasurementResponderSummary(ShowPerformanceMeasurementResponderSummarySchema):
    '''Parser for:
        * 'show performance-measurement responder summary'

    '''
    cli_command = [
        'show performance-measurement responder summary'
    ]
    def cli(self, output=None):
        
        if not output:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Total interfaces                              : 2
        p1 = re.compile(r'^Total interfaces\s+: (?P<total_interfaces>\d+)$')

        # Total query packets received                  : 45501
        p2 = re.compile(r'^Total query packets received\s+: (?P<total_query_packets_received>\d+)$')

        # Total reply packets sent                      : 45499
        p3 = re.compile(r'^Total reply packets sent\s+: (?P<total_reply_packets_sent>\d+)$')

        # Total reply packets sent errors               : 2
        p4 = re.compile(r'^Total reply packets sent errors\s+: (?P<total_reply_packets_sent_errors>\d+)$')

        # Total URO TLV not present errors              : 0
        p5 = re.compile(r'^Total URO TLV not present errors\s+: (?P<total_uro_tlv_not_present_errors>\d+)$')

        # Total invalid port number errors              : 0
        p6 = re.compile(r'^Total invalid port number errors\s+: (?P<total_invalid_port_number_errors>\d+)$')

        # Total no source address errors                : 0
        p7 = re.compile(r'^Total no source address errors\s+: (?P<total_no_source_address_errors>\d+)$')

        # Total no return path errors                   : 0
        p8 = re.compile(r'^Total no return path errors\s+: (?P<total_no_return_path_errors>\d+)$')

        # Total unsupported querier control code errors : 0
        p9 = re.compile(r'^Total unsupported querier control code errors\s+: (?P<total_unsupported_querier>\d+)$')

        # Total unsupported timestamp format errors     : 0
        p10 = re.compile(r'^Total unsupported timestamp format errors\s+: (?P<total_unsupported_timestamp_format_errors>\d+)$')

        # Total timestamp not available errors          : 0
        p11 = re.compile(r'^Total timestamp not available errors\s+: (?P<total_timestamp_not_available_errors>\d+)$')

        # Total unsupported mandatory TLV errors        : 0
        p12 = re.compile(r'^Total unsupported mandatory TLV errors\s+: (?P<total_unsupported_mandatory_tlv_errors>\d+)$')

        # Total invalid packet errors                   : 0
        p13 = re.compile(r'^Total invalid packet errors\s+: (?P<total_invalid_packet_errors>\d+)$')

        #     Total loss probe color errors                 : 2
        p14 = re.compile(r'^Total loss probe color errors\s+: (?P<total_loss_probe_color_errors>\d+)$')

        # Current rate                                  : 0 pkts/sec
        p15 = re.compile(r'^Current rate\s+: (?P<current_rate>\d+) pkts/sec$')

        # Rate high water mark                          : 0 pkts/sec
        p16 = re.compile(r'^Rate high water mark\s+: (?P<rate_high_water_mark>\d+) pkts/sec$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Total interfaces                              : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_interfaces', int(group['total_interfaces']))
                continue

            # Total query packets received                  : 45501
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_query_packets_received', int(group['total_query_packets_received']))
                continue

            # Total reply packets sent                      : 45499
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_reply_packets_sent', int(group['total_reply_packets_sent']))
                continue

            # Total reply packets sent errors               : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_reply_packets_sent_errors', int(group['total_reply_packets_sent_errors']))
                continue

            # Total URO TLV not present errors              : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_uro_tlv_not_present_errors', int(group['total_uro_tlv_not_present_errors']))
                continue

            # Total invalid port number errors              : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_invalid_port_number_errors', int(group['total_invalid_port_number_errors']))
                continue

            # Total no source address errors                : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_no_source_address_errors', int(group['total_no_source_address_errors']))
                continue

            # Total no return path errors                   : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_no_return_path_errors', int(group['total_no_return_path_errors']))
                continue

            # Total unsupported querier control code errors : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_querier_control_code_errors', int(group['total_unsupported_querier']))
                continue

            # Total unsupported timestamp format errors     : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_timestamp_format_errors', int(group['total_unsupported_timestamp_format_errors']))
                continue

            # Total timestamp not available errors          : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_timestamp_not_available_errors', int(group['total_timestamp_not_available_errors']))
                continue

            # Total unsupported mandatory TLV errors        : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_mandatory_tlv_errors', int(group['total_unsupported_mandatory_tlv_errors']))
                continue

            # Total invalid packet errors                   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_invalid_packet_errors', int(group['total_invalid_packet_errors']))
                continue

            #     Total loss probe color errors                 : 2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_loss_probe_color_errors', int(group['total_loss_probe_color_errors']))
                continue

            # Current rate                                  : 0 pkts/sec
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('current_rate', int(group['current_rate']))
                continue

            # Rate high water mark                          : 0 pkts/sec
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('rate_high_water_mark', int(group['rate_high_water_mark']))
                continue

        return ret_dict

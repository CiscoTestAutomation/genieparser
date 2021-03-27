''' show_services.py

JUNOS parsers for the following commands:
'''

'''
    * show services accounting aggregation template template-name {name} extensive
    * show services accounting usage
    * show services accounting errors
    * show services accounting flow
    * show services accounting memory
    * show services accounting status
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


class ShowServicesAccountingAggregationTemplateSchema(MetaParser):
    """ Schema for:
            * show services accounting aggregation template template-name {name} extensive
    """

    schema = {
            "services-accounting-information": {
                "flow-aggregate-template-detail": {
                    "flow-aggregate-template-detail-ipv4": {
                        "detail-entry": ListOf({
                            Optional("source-address"): str,
                            Optional("destination-address"): str,
                            Optional("source-port"): str,
                            Optional("destination-port"): str,
                            Optional("mpls-label-1"): str,
                            Optional("mpls-label-2"): str,
                            Optional("mpls-label-3"): str,
                            Optional("top-label-address"): str,
                            Optional("protocol"): {
                                "#text": str},
                            Optional("tos"): str,
                            Optional("tcp-flags"): str,
                            Optional("source-mask"): str,
                            Optional("destination-mask"): str,
                            "input-snmp-interface-index": str,
                            "output-snmp-interface-index": str,
                            Optional("start-time"): str,
                            Optional("end-time"): str,
                            "packet-count": str,
                            "byte-count": str,
                            }
                        ),
                    }
                },
            }
        }

class ShowServicesAccountingAggregationTemplate(ShowServicesAccountingAggregationTemplateSchema):
    """ Parser for:
            * show services accounting aggregation template template-name {name} extensive
    """

    cli_command = "show services accounting aggregation template template-name {name} extensive"

    def cli(self, name=None, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                name=name
            ))
        else:
            out = output

        ret_dict = {}

        mpls = False

        # Source address: 10.120.202.64, Destination address: 10.169.14.158, Top Label Address: 121
        # Source address: 10.120.202.64, Destination address: 10.169.14.158
        # Source address: 10.120.202.64
        p1 = re.compile(r'^Source +address: +(?P<source_address>\S+)(, +Destination +address: '
                        r'+(?P<destination_address>\S+))?(, Top +Label +Address: +'
                        r'(?P<top_label_address>\S+))?$')

        # Destination address: 000:0:0:0:0:0:0:0
        p1_2 = re.compile(r'^Destination +address: +(?P<destination_address>\S+)$')

        # Source port: 8, Destination port: 0
        p2 = re.compile(r'^Source +port: +(?P<source_port>\d+), '
                       r'+Destination +port: +(?P<destination_port>\d+)$')

        # Protocol: 1, TOS: 0, TCP flags: 0
        p3 = re.compile(r'^Protocol: +(?P<protocol>\d+), +'
                       r'TOS: +(?P<tos>\d+), +'
                       r'TCP +flags: +(?P<tcp_flags>\d+)$')

        # Source mask: 32, Destination mask: 30
        p4 = re.compile(r'^Source +mask: +(?P<source_mask>\d+), '
                       r'+Destination +mask: +(?P<destination_mask>\d+)$')

        # Input SNMP interface index: 618, Output SNMP interface index: 620
        p5 = re.compile(r'^Input +SNMP +interface +index: +(?P<input_snmp_interface_index>\d+), +'
                       r'Output +SNMP +interface index: +(?P<output_snmp_interface_index>\d+)$')

        # Start time: 79167425, End time: 79167425
        p6 = re.compile(r'^Start +time: +(?P<start_time>\d+), +'
                       r'End +time: +(?P<end_time>\d+)$')

        # Packet count: 1, Byte count: 84
        p7 = re.compile(r'^Packet +count: +(?P<packet_count>\d+), +'
                       r'Byte +count: +(?P<byte_count>\d+)$')

        # MPLS label 1: 299888, MPLS label 2: 16, MPLS label 3: 0
        p8 = re.compile(r'^MPLS +label 1: +(?P<mpls_label_1>\d+), +MPLS +label 2: '
                        r'+(?P<mpls_label_2>\d+), MPLS +label 3: +(?P<mpls_label_3>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Source address: 10.120.202.64, Destination address: 10.169.14.158
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if not mpls:
                    entry_dicts = ret_dict.setdefault(
                        "services-accounting-information", {}).setdefault(
                            "flow-aggregate-template-detail", {}).setdefault(
                                "flow-aggregate-template-detail-ipv4", {}).setdefault(
                                    "detail-entry", [])
                    entry_dict = dict()
                    entry_dicts.append(entry_dict)
                else:
                    mpls = False
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Destination address: 000:0:0:0:0:0:0:0
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Source port: 8, Destination port: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Protocol: 1, TOS: 0, TCP flags: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                protocol_dict = entry_dict.setdefault('protocol', {})
                protocol_dict.update({'#text': group['protocol']})
                entry_dict.update({
                    'tos': group['tos'],
                    'tcp-flags': group['tcp_flags']
                })

            # Source mask: 32, Destination mask: 30
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Input SNMP interface index: 618, Output SNMP interface index: 620
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Start time: 79167425, End time: 79167425
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # Packet count: 1, Byte count: 84
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

            # MPLS label 1: 299888, MPLS label 2: 16, MPLS label 3: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mpls = True
                entry_dicts = ret_dict.setdefault(
                    "services-accounting-information", {}).setdefault(
                        "flow-aggregate-template-detail", {}).setdefault(
                            "flow-aggregate-template-detail-ipv4", {}).setdefault(
                                "detail-entry", [])
                entry_dict = dict()
                entry_dicts.append(entry_dict)
                entry_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})

        return ret_dict

class ShowServicesAccountingUsageSchema(MetaParser):
    """ Schema for:
            * show services accounting usage
    """


    schema = {
                "services-accounting-information": {
                    "usage-information": ListOf({
                        "interface-name": str,
                        "uptime": str,
                        "inttime": str,
                        "five-second-load": str,
                        "one-minute-load": str,
                    }),
                }
            }

class ShowServicesAccountingUsage(ShowServicesAccountingUsageSchema):
    """ Parser for:
            * show services accounting usage
    """

    cli_command = "show services accounting usage"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # CPU utilization
        p1 = re.compile(r'^CPU +utilization$')
        p1_1 = re.compile(r'^{master}$')

        # ms-9/0/0
        p2 = re.compile(r'^(?P<interface_name>\S+)$')

        # Uptime: 79203479 milliseconds, Interrupt time: 0 microseconds
        p3 = re.compile(r'^Uptime: (?P<uptime>\d+) +milliseconds, '
                        r'+Interrupt +time: +(?P<inttime>\d+) +microseconds$')

        # Load (5 second): 1%, Load (1 minute): 1%
        p4 = re.compile(r'^Load +\(5 +second\): +(?P<five_second_load>\d+)%, '
                        r'+Load +\(1 +minute\): +(?P<one_minute_load>\d+)%$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue
            
            # {master}
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                continue

            # ms-9/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                usage_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('usage-information', [])
                usage_information_dict = {"interface-name": group['interface_name']}
                usage_information_list.append(usage_information_dict)
                continue

            # Uptime: 79203479 milliseconds, Interrupt time: 0 microseconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                usage_information_dict.update({
                    "uptime": group["uptime"],
                    "inttime": group["inttime"],
                })
                continue

            # Load (5 second): 1%, Load (1 minute): 1%
            m = p4.match(line)
            if m:
                group = m.groupdict()
                usage_information_dict.update({
                    "five-second-load": group["five_second_load"],
                    "one-minute-load": group["one_minute_load"],
                })
                continue

        return ret_dict

class ShowServicesAccountingErrorsSchema(MetaParser):
    """ Schema for:
            * show services accounting errors
    """

    schema = {
                "services-accounting-information": {
                    "v9-error-information": ListOf({
                        "interface-name": str,
                        "service-set-dropped": str,
                        "active-timeout-failures": str,
                        "export-packet-failures": str,
                        "flow-creation-failures": str,
                        "memory-overload": str,
                    }),
                }
            }

class ShowServicesAccountingErrors(ShowServicesAccountingErrorsSchema):
    """ Parser for:
            * show services accounting errors
    """

    cli_command = "show services accounting errors"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Error information
        p1 = re.compile(r'^Error +information$')
        p1_1 = re.compile(r'^{master}$')

        # Service Accounting interface: ms-9/0/0
        p2 = re.compile(r'^Service +Accounting +interface: +(?P<interface_name>\S+)$')

        # Service sets dropped: 0, Active timeout failures: 0
        p3 = re.compile(r'^Service +sets +dropped: +(?P<service_set_dropped>\d+), +'
                        r'Active +timeout +failures: +(?P<active_timeout_failures>\d+)$')

        # Export packet failures: 0, Flow creation failures: 0
        p4 = re.compile(r'^Export +packet +failures: +(?P<export_packet_failures>\d+), +'
                        r'Flow +creation +failures: +(?P<flow_creation_failures>\d+)$')

        # Memory overload: No
        p5 = re.compile(r'^Memory +overload: +(?P<memory_overload>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Error information
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            # {master}
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                continue

            # Service Accounting interface: ms-9/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                error_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('v9-error-information', [])
                error_information_dict = {"interface-name": group['interface_name']}
                error_information_list.append(error_information_dict)
                continue

            # Service sets dropped: 0, Active timeout failures: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                error_information_dict.update({
                    "service-set-dropped": group["service_set_dropped"],
                    "active-timeout-failures": group["active_timeout_failures"],
                })
                continue

            # Export packet failures: 0, Flow creation failures: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                error_information_dict.update({
                    "export-packet-failures": group["export_packet_failures"],
                    "flow-creation-failures": group["flow_creation_failures"],
                })
                continue

            # Memory overload: No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                error_information_dict.update({
                    "memory-overload": group["memory_overload"],
                })
                continue

        return ret_dict

class ShowServicesAccountingFlowSchema(MetaParser):
    """ Schema for:
            * show services accounting flow
    """


    schema = {
                "services-accounting-information": {
                    "flow-information": ListOf({
                "interface-name": str,
                "local-ifd-index": str,
                "flow-packets": str,
                "flow-bytes": str,
                "flow-packets-ten-second-rate": str,
                "flow-bytes-ten-second-rate": str,
                "active-flows": str,
                "flows": str,
                "flows-exported": str,
                "flow-packets-exported": str,
                "flows-expired": str,
                "flows-aged": str,
            }),
                }
            }

class ShowServicesAccountingFlow(ShowServicesAccountingFlowSchema):
    """ Parser for:
            * show services accounting flow
    """

    cli_command = "show services accounting flow"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Flow information
        p1 = re.compile(r'^Flow +information$')
        p1_1 = re.compile(r'^{master}$')

        # Service Accounting interface: ms-9/0/0, Local interface index: 140
        p2 = re.compile(r'^Service +Accounting +interface: +(?P<interface_name>\S+), +'
                        r'Local +interface +index: +(?P<local_ifd_index>\d+)$')

        # Flow packets: 0, Flow bytes: 0
        p3 = re.compile(r'^Flow +packets: +(?P<flow_packets>\d+), +'
                        r'Flow +bytes: +(?P<flow_bytes>\d+)$')

        # Export packet failures: 0, Flow creation failures: 0
        p4 = re.compile(r'^Flow +packets +10-second +rate: +(?P<flow_packets_ten_second_rate>\d+), +'
                        r'Flow +bytes +10-second +rate: +(?P<flow_bytes_ten_second_rate>\d+)$')

        # Active flows: 0, Total flows: 0
        p5 = re.compile(r'^Active +flows: +(?P<active_flows>\d+), +'
                        r'Total +flows: +(?P<flows>\d+)$')

        # Flows exported: 0, Flows packets exported: 9
        p6 = re.compile(r'^Flows +exported: +(?P<flows_exported>\d+), +'
                        r'Flows +packets +exported: +(?P<flow_packets_exported>\d+)$')

        # Flows inactive timed out: 0, Flows active timed out: 0
        p7 = re.compile(r'^Flows +inactive +timed +out: +(?P<flows_expired>\d+), +'
                        r'Flows +active +timed +out: +(?P<flows_aged>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Flow information# Error information
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            # {master}
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                continue

            # Service Accounting interface: ms-9/0/0, Local interface index: 140
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('flow-information', [])
                flow_information_dict = {
                    "interface-name": group['interface_name'],
                    "local-ifd-index": group['local_ifd_index']
                    }
                flow_information_list.append(flow_information_dict)
                continue

            # Flow packets: 0, Flow bytes: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_information_dict.update({
                    "flow-packets": group["flow_packets"],
                    "flow-bytes": group["flow_bytes"],
                })
                continue

            # Export packet failures: 0, Flow creation failures: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_information_dict.update({
                    "flow-packets-ten-second-rate": group["flow_packets_ten_second_rate"],
                    "flow-bytes-ten-second-rate": group["flow_bytes_ten_second_rate"],
                })
                continue

            # Active flows: 0, Total flows: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flow_information_dict.update({
                    "active-flows": group["active_flows"],
                    "flows": group["flows"]
                })
                continue

            # Flows exported: 0, Flows packets exported: 9
            m = p6.match(line)
            if m:
                group = m.groupdict()
                flow_information_dict.update({
                    "flows-exported": group["flows_exported"],
                    "flow-packets-exported": group["flow_packets_exported"],
                })
                continue

            # Flows inactive timed out: 0, Flows active timed out: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                flow_information_dict.update({
                    "flows-expired": group["flows_expired"],
                    "flows-aged": group["flows_aged"],
                })
                continue

        return ret_dict


class ShowServicesAccountingMemorySchema(MetaParser):
    """ Schema for:
            * show services accounting memory
    """


    schema = {
                "services-accounting-information": {
                    "memory-information": ListOf({
                    "interface-name": str,
                    "allocation-count": str,
                    "free-count": str,
                    "allocations-per-second": str,
                    "frees-per-second": str,
                    "memory-used": str,
                    "memory-free": str,
                    "v9-memory-used": str,
                }),
                }
            }

class ShowServicesAccountingMemory(ShowServicesAccountingMemorySchema):
    """ Parser for:
            * show services accounting memory
    """

    cli_command = "show services accounting memory"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Memory information
        p1 = re.compile(r'^Memory +utilization$')
        p1_1 = re.compile(r'^{master}$')

        # Service Accounting interface: ms-9/0/0
        p2 = re.compile(r'^Service +Accounting +interface: +(?P<interface_name>\S+)')

        # Allocation count: 1, Free count: 0
        p3 = re.compile(r'^Allocation +count: +(?P<allocation_count>\d+), +'
                        r'Free +count: +(?P<free_count>\d+)$')

        # Allocations per second: 0, Frees per second: 0
        p4 = re.compile(r'^Allocations +per +second: +(?P<allocations_per_second>\d+), +'
                        r'Frees +per +second: +(?P<frees_per_second>\d+)$')

        # Total memory used (in bytes): 862529184, Total memory free (in bytes): 3164002312
        p5 = re.compile(r'^Total +memory +used +\(in bytes\): +(?P<memory_used>\d+), +'
                        r'Total +memory +free +\(in bytes\): +(?P<memory_free>\d+)$')

        # Memory used by Jflow-v9 (in bytes): 48
        p6 = re.compile(r'^Memory +used +by +Jflow-v9 +\(in bytes\): +(?P<v9_memory_used>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # Memory information
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            # {master}
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                continue

            # Service Accounting interface: ms-9/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                memory_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('memory-information', [])
                memory_information_dict = {
                    "interface-name": group['interface_name']
                    }
                memory_information_list.append(memory_information_dict)
                continue

            # Allocation count: 1, Free count: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                memory_information_dict.update({
                    "allocation-count": group["allocation_count"],
                    "free-count": group["free_count"],
                })
                continue

            # Allocations per second: 0, Frees per second: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                memory_information_dict.update({
                    "allocations-per-second": group["allocations_per_second"],
                    "frees-per-second": group["frees_per_second"],
                })
                continue

            # Total memory used (in bytes): 862529184, Total memory free (in bytes): 3164002312
            m = p5.match(line)
            if m:
                group = m.groupdict()
                memory_information_dict.update({
                    "memory-used": group["memory_used"],
                    "memory-free": group["memory_free"]
                })
                continue

            # Memory used by Jflow-v9 (in bytes): 48
            m = p6.match(line)
            if m:
                group = m.groupdict()
                memory_information_dict.update({
                    "v9-memory-used": group["v9_memory_used"],
                })
                continue

        return ret_dict


class ShowServicesAccountingStatusSchema(MetaParser):
    """ Schema for:
            * show services accounting status
    """


    schema = {
                "services-accounting-information": {
                    "status-information": ListOf({
                    "interface-name": str,
                    "status-export-format": str,
                    "status-route-record-count": str,
                    "status-ifl-snmp-map-count": str,
                    "status-as-count": str,
                    "status-monitor-config-set": str,
                    "status-monitor-route-record-set": str,
                    "status-monitor-ifl-snmp-set": str,
                }),
                }
            }

class ShowServicesAccountingStatus(ShowServicesAccountingStatusSchema):
    """ Parser for:
            * show services accounting status
    """

    cli_command = "show services accounting status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Service Accounting interface: ms-9/0/0
        p1 = re.compile(r'^Service +Accounting +interface: +(?P<interface_name>\S+)')

        # Export format: 9, Route record count: 902244
        p2 = re.compile(r'^Export +format: +(?P<status_export_format>\d+), +'
                        r'Route +record +count: +(?P<status_route_record_count>\d+)$')

        # IFL to SNMP index count: 296, AS count: 0
        p3 = re.compile(r'^IFL +to +SNMP +index +count: +(?P<status_ifl_snmp_map_count>\d+), +'
                        r'AS +count: +(?P<status_as_count>\d+)$')

        # Configuration set: Yes, Route record set: No, IFL SNMP map set: Yes
        p4 = re.compile(r'^Configuration +set: +(?P<status_monitor_config_set>\S+), +'
                        r'Route +record +set: +(?P<status_monitor_route_record_set>\S+), +'
                        r'IFL +SNMP +map +set: +(?P<status_monitor_ifl_snmp_set>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Service Accounting interface: ms-9/0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                status_information_list = ret_dict.setdefault(
                    'services-accounting-information', {}
                    ).setdefault('status-information', [])
                status_information_dict = {
                    "interface-name": group['interface_name']
                    }
                status_information_list.append(status_information_dict)
                continue

            # Export format: 9, Route record count: 902244
            m = p2.match(line)
            if m:
                group = m.groupdict()
                status_information_dict.update({
                    "status-export-format": group["status_export_format"],
                    "status-route-record-count": group["status_route_record_count"],
                })
                continue

            # IFL to SNMP index count: 296, AS count: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                status_information_dict.update({
                    "status-ifl-snmp-map-count": group["status_ifl_snmp_map_count"],
                    "status-as-count": group["status_as_count"],
                })
                continue

            # Configuration set: Yes, Route record set: No, IFL SNMP map set: Yes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                status_information_dict.update({
                    "status-monitor-config-set": group["status_monitor_config_set"],
                    "status-monitor-route-record-set": group["status_monitor_route_record_set"],
                    "status-monitor-ifl-snmp-set": group["status_monitor_ifl_snmp_set"]
                })
                continue

        return ret_dict


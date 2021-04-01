"""show_ddos.py

JUNOS parsers for the following commands:
    * show ddos-protection statistics

"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf

class ShowDdosProtectionStatisticsSchema(MetaParser):
    """
    Schema for:
        * show ddos-protection statistics
    """
    
    schema = {
            "ddos-statistics-information": {
                Optional("aggr-level-control-mode"): str,
                Optional("aggr-level-detection-mode"): str,
                "ddos-flow-detection-enabled": str,
                "ddos-logging-enabled": str,
                "ddos-policing-fpc-enabled": str,
                "ddos-policing-re-enabled": str,
                Optional("detection-mode"): str,
                "flow-report-rate": str,
                "flows-cumulative": str,
                "flows-current": str,
                "packet-types-in-violation": str,
                "packet-types-seen-violation": str,
                "total-violations": str,
                "violation-report-rate": str
            }
        }

class ShowDdosProtectionStatistics(ShowDdosProtectionStatisticsSchema):
    """ Parser for:
        * show ddos-protection statistics
    """

    cli_command = 'show ddos-protection statistics'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        res = {}        

        # DDOS protection global statistics:
        p1 = re.compile(r'^DDOS protection global statistics:$')

        # Policing on routing engine:         Yes
        # Policing on FPC:                    Yes
        # Flow detection:                     No
        # Logging:                            Yes
        # Policer violation report rate:      100
        # Flow report rate:                   100
        # Default flow detection mode         Automatic
        # Default flow level detection mode   Automatic
        # Default flow level control mode     Drop
        # Currently violated packet types:    0
        # Packet types have seen violations:  0
        # Total violation counts:             0
        # Currently tracked flows:            0
        # Total detected flows:               0
        p2 = re.compile(r'(?P<key>[\s\S]+)(:|mode) +(?P<value>[\w\d]+)')

        keys_dict = {
            'Policing on routing engine': 'ddos-policing-re-enabled',
            'Policing on FPC': 'ddos-policing-fpc-enabled',               
            'Flow detection': 'ddos-flow-detection-enabled',
            'Logging': 'ddos-logging-enabled',                          
            'Policer violation report rate': 'violation-report-rate',  
            'Flow report rate':'flow-report-rate',
            'Default flow detection ': 'detection-mode',      
            'Default flow level detection ': 'aggr-level-detection-mode',
            'Default flow level control ': 'aggr-level-control-mode',
            'Currently violated packet types': 'packet-types-in-violation',
            'Packet types have seen violations': 'packet-types-seen-violation',
            'Total violation counts': 'total-violations',      
            'Currently tracked flows': 'flows-current',        
            'Total detected flows': 'flows-cumulative'                  
        }

        for line in out.splitlines():
            line = line.strip()            

            m = p1.match(line)
            if m:
                res = {'ddos-statistics-information':{}}
                continue
            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key = group['key']
                value = group['value']

                res['ddos-statistics-information'][keys_dict[key]] = value 
                continue

        return res

class ShowDDosProtectionProtocolSchema(MetaParser):
    """ Schema for:
            * show ddos-protection protocols {protocol}  
    """

    schema = {
        Optional("@xmlns:junos"): str,
        "ddos-protocols-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "ddos-protocol-group": {
                "ddos-protocol": {
                    "ddos-basic-parameters": {
                        Optional("@junos:style"): str,
                        "policer-bandwidth": str,
                        "policer-burst": str,
                        Optional("policer-enable"): str,
                        "policer-time-recover": str
                    },
                    "ddos-flow-detection": {
                        Optional("@junos:style"): str,
                        "detect-time": str,
                        "detection-mode": str,
                        "flow-aggregation-level-states": {
                            "ifd-bandwidth": str,
                            "ifd-control-mode": str,
                            "ifd-detection-mode": str,
                            "ifl-bandwidth": str,
                            "ifl-control-mode": str,
                            "ifl-detection-mode": str,
                            "sub-bandwidth": str,
                            "sub-control-mode": str,
                            "sub-detection-mode": str
                        },
                        "log-flows": str,
                        "recover-time": str,
                        "timeout-active-flows": str,
                        "timeout-time": str
                    },
                    "ddos-instance": ListOf({
                        Optional("@junos:style"): str,
                        "ddos-instance-parameters": {
                            Optional("@junos:style"): str,
                            Optional("hostbound-queue"): str,
                            "policer-bandwidth": str,
                            Optional("policer-bandwidth-scale"): str,
                            "policer-burst": str,
                            Optional("policer-burst-scale"): str,
                            Optional("policer-enable"): str
                        },
                        "ddos-instance-statistics": {
                            Optional("@junos:style"): str,
                            "packet-arrival-rate": str,
                            "packet-arrival-rate-max": str,
                            "packet-dropped": str,
                            "packet-received": str
                        },
                        "protocol-states-locale": str
                    }),
                    "ddos-system-statistics": {
                        Optional("@junos:style"): str,
                        "packet-arrival-rate": str,
                        "packet-arrival-rate-max": str,
                        "packet-dropped": str,
                        "packet-received": str
                    },
                    "packet-type":
                    str,
                    "packet-type-description":
                    str
                },
                "group-name": str
            },
            "flows-cumulative": str,
            "flows-current": str,
            Optional("mod-packet-types"): str,
            Optional("packet-types-in-violation"): str,
            Optional("packet-types-rcvd-packets"): str,
            Optional("total-packet-types"): str
        }
    }

class ShowDDosProtectionProtocol(ShowDDosProtectionProtocolSchema):
    """ Parser for:
            * show ddos-protection protocols {protocol}  
    """
    cli_command = 'show ddos-protection protocols {protocol}'

    def cli(self, protocol, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                protocol=protocol
            ))
        else:
            out = output

        ret_dict = {}

        # Packet types: 1, Modified: 0, Received traffic: 0, Currently violated: 0
        p1 = re.compile(r'^Packet +types: +(?P<total_packet_types>\d+), +'
            r'Modified: +(?P<mod_packet_types>\d+), +Received +traffic: +(?P<packet_types_rcvd_packets>\d+), +'
            r'Currently +violated: +(?P<packet_types_in_violation>\d+)$')
        
        # Currently tracked flows: 0, Total detected flows: 0
        p2 = re.compile(r'^Currently +tracked +flows: +(?P<flows_current>\d+), +'
            r'Total +detected +flows: +(?P<flows_cumulative>\d+)$')
        
        # Protocol Group: ARP
        p3 = re.compile(r'^Protocol +Group: +(?P<group_name>\S+)$')

        # Packet type: aggregate (Aggregate for all arp traffic)
        p4 = re.compile(r'^Packet +type: +(?P<packet_type>\S+) +\((?P<packet_type_description>[\S\s]+)\)$')

        # Bandwidth:        20000 pps
        p5 = re.compile(r'^Bandwidth: +(?P<policer_bandwidth>\d+) +pps$')

        # Burst:            20000 packets
        p6 = re.compile(r'^Burst: +(?P<policer_burst>\d+) +packets$')

        # Recover time:     300 seconds
        p7 = re.compile(r'^Recover +time: +(?P<policer_time_recover>\d+) +seconds$')

        # Enabled:          Yes
        p8 = re.compile(r'^Enabled: +(?P<policer_enable>\S+)$')

        # Detection mode: Automatic  Detect time:  3 seconds
        p9 = re.compile(r'^Detection +mode: +(?P<detection_mode>\S+) +Detect +time: +(?P<detect_time>\d+) +seconds$')

        # Log flows:      Yes        Recover time: 60 seconds
        p10 = re.compile(r'^Log +flows: +(?P<log_flows>\S+) +Recover +time: +(?P<recover_time>\d+) +seconds$')

        # Timeout flows:  No         Timeout time: 300 seconds
        p11 = re.compile(r'^Timeout +flows: +(?P<timeout_active_flows>\S+) +Timeout +time: +(?P<timeout_time>\d+) +seconds$')

        # Subscriber          Automatic       Drop          10 pps
        p12 = re.compile(r'^Subscriber +(?P<sub_detection_mode>\S+) +(?P<sub_control_mode>\S+) +(?P<sub_bandwidth>\d+) +pps$')

        # Logical interface   Automatic       Drop          10 pps
        p13 = re.compile(r'^Logical +interface +(?P<ifl_detection_mode>\S+) +(?P<ifl_control_mode>\S+) +(?P<ifl_bandwidth>\d+) +pps$')

        # Physical interface  Automatic       Drop          20000 pps
        p14 = re.compile(r'^Physical +interface +(?P<ifd_detection_mode>\S+) +(?P<ifd_control_mode>\S+) +(?P<ifd_bandwidth>\d+) +pps$')

        # System-wide information:
        p15 = re.compile(r'^System-wide +information:$')

        # Received:  0                   Arrival rate:     0 pps
        p16 = re.compile(r'^Received: +(?P<packet_received>\d+) +Arrival +rate: +(?P<packet_arrival_rate>\d+) +pps$')

        # Dropped:   0                   Max arrival rate: 0 pps
        p17 = re.compile(r'^Dropped: +(?P<packet_dropped>\d+) +Max +arrival +rate: +(?P<packet_arrival_rate_max>\d+) +pps$')

        # Routing Engine information:
        p18 = re.compile(r'^Routing +Engine +information:$')

        # FPC slot 0 information:
        # FPC slot 9 information:
        p18_1 = re.compile(r'^FPC +slot +\d+ +information:$')

        # Bandwidth: 20000 pps, Burst: 20000 packets, enabled
        # Bandwidth: 100% (20000 pps), Burst: 100% (20000 packets), enabled
        p19 = re.compile(r'^Bandwidth: +((?P<policer_bandwidth_scale>\d+)% +\()?(?P<policer_bandwidth>\d+) +pps\)?, +Burst: +((?P<policer_burst_scale>\d+)% +\()?(?P<policer_burst>\d+) +packets\)?, +(?P<policer_enable>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Packet types: 1, Modified: 0, Received traffic: 0, Currently violated: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ddos_protocols_information_dict = ret_dict.setdefault('ddos-protocols-information', {})
                ddos_protocols_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Currently tracked flows: 0, Total detected flows: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ddos_protocols_information_dict = ret_dict.setdefault('ddos-protocols-information', {})
                ddos_protocols_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Protocol Group: ARP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ddos_protocol_group_dict = ddos_protocols_information_dict.setdefault('ddos-protocol-group', {})
                ddos_protocol_group_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Packet type: aggregate (Aggregate for all arp traffic)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ddos_protocol_dict = ddos_protocol_group_dict.setdefault('ddos-protocol', {})
                ddos_protocol_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Bandwidth:        20000 pps
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ddos_basic_parameters_dict = ddos_protocol_dict.setdefault('ddos-basic-parameters', {})
                ddos_basic_parameters_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Burst:            20000 packets
            p6 = re.compile(r'^Burst: +(?P<policer_burst>\d+) +packets$')
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ddos_basic_parameters_dict = ddos_protocol_dict.setdefault('ddos-basic-parameters', {})
                ddos_basic_parameters_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Recover time:     300 seconds
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ddos_basic_parameters_dict = ddos_protocol_dict.setdefault('ddos-basic-parameters', {})
                ddos_basic_parameters_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Enabled:          Yes
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ddos_basic_parameters_dict = ddos_protocol_dict.setdefault('ddos-basic-parameters', {})
                ddos_basic_parameters_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Detection mode: Automatic  Detect time:  3 seconds
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ddos_flow_detection_dict = ddos_protocol_dict.setdefault('ddos-flow-detection', {})
                ddos_flow_detection_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Log flows:      Yes        Recover time: 60 seconds
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ddos_flow_detection_dict = ddos_protocol_dict.setdefault('ddos-flow-detection', {})
                ddos_flow_detection_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Timeout flows:  No         Timeout time: 300 seconds
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ddos_flow_detection_dict = ddos_protocol_dict.setdefault('ddos-flow-detection', {})
                ddos_flow_detection_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Subscriber          Automatic       Drop          10 pps
            m = p12.match(line)
            if m:
                group = m.groupdict()
                flow_aggregation_level_states_dict = ddos_flow_detection_dict.setdefault('flow-aggregation-level-states', {})
                flow_aggregation_level_states_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Logical interface   Automatic       Drop          10 pps
            m = p13.match(line)
            if m:
                group = m.groupdict()
                flow_aggregation_level_states_dict = ddos_flow_detection_dict.setdefault('flow-aggregation-level-states', {})
                flow_aggregation_level_states_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Physical interface  Automatic       Drop          20000 pps
            m = p14.match(line)
            if m:
                group = m.groupdict()
                flow_aggregation_level_states_dict = ddos_flow_detection_dict.setdefault('flow-aggregation-level-states', {})
                flow_aggregation_level_states_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # System-wide information:
            m = p15.match(line)
            if m:
                system_wide_info = True
                group = m.groupdict()
                ddos_system_statistics_dict = ddos_protocol_dict.setdefault('ddos-system-statistics', {})
                ddos_system_statistics_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Received:  0                   Arrival rate:     0 pps
            m = p16.match(line)
            if m:
                group = m.groupdict()
                if system_wide_info:
                    ddos_system_statistics_dict.update(
                        {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                else:
                    ddos_instance_statistics_dict.update(
                        {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Dropped:   0                   Max arrival rate: 0 pps
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if system_wide_info:
                    ddos_system_statistics_dict.update(
                        {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                else:
                    ddos_instance_statistics_dict.update(
                        {k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Routing Engine information:
            m = p18.match(line)
            if m:
                system_wide_info = False
                group = m.groupdict()
                ddos_instance_list = ddos_protocol_dict.setdefault('ddos-instance', [])
                ddos_instance_dict = {'protocol-states-locale': "Routing Engine"}
                ddos_instance_list.append(ddos_instance_dict)
                ddos_instance_statistics_dict = ddos_instance_dict.setdefault('ddos-instance-statistics', {})
                continue

            # FPC slot 0 information:
            # FPC slot 9 information:
            m = p18_1.match(line)
            if m:
                system_wide_info = False
                group = m.groupdict()
                ddos_instance_list = ddos_protocol_dict.setdefault('ddos-instance', [])
                ddos_instance_dict = {'protocol-states-locale': line.replace(' information:', '')}
                ddos_instance_list.append(ddos_instance_dict)
                ddos_instance_statistics_dict = ddos_instance_dict.setdefault('ddos-instance-statistics', {})
                continue

            # Bandwidth: 20000 pps, Burst: 20000 packets, enabled
            # Bandwidth: 100% (20000 pps), Burst: 100% (20000 packets), enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ddos_instance_parameters_dict = ddos_instance_dict.setdefault('ddos-instance-parameters', {})
                ddos_instance_parameters_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
        
        return ret_dict
"""show_class_of_service.py

JunOS parsers for the following show commands:
    * show class-of-service interface {interface}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any, Optional, Use, Schema)


class ShowClassOfServiceSchema(MetaParser):
    """ Schema for:
            * show class-of-service interface {interface}
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "cos-interface-information": {
            Optional("@xmlns"): str,
            "interface-map": {
                Optional("cos-objects"): str,
                Optional("forwarding-class-set-attachment"): str,
                Optional("i-logical-map"): {
                    "cos-objects": {
                        "cos-object-index": list,
                        "cos-object-name": list,
                        "cos-object-subtype": list,
                        "cos-object-type": list
                    },
                    "i-logical-index": str,
                    "i-logical-name": str
                },
                "interface-congestion-notification-map": str,
                Optional("interface-exclude-queue-overhead-bytes"): str,
                "interface-index": str,
                Optional("interface-logical-interface-aggregate-statistics"): str,
                "interface-name": str,
                "interface-queues-in-use": str,
                "interface-queues-supported": str,
                Optional("interface-shaping-rate"): str,
                "scheduler-map-index": str,
                "scheduler-map-name": str
            }
        }
    }


class ShowClassOfService(ShowClassOfServiceSchema):
    """ Parser for:
            * show class-of-service interface {interface}
    """
    cli_command = 'show class-of-service interface {interface}'

    def cli(self, interface, output=None):
        if not output:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        
        # Physical interface: ge-0/0/2, Index: 150
        p1 = re.compile(r'^Physical +interface: +(?P<interface_name>\S+), +'
            r'Index: +(?P<interface_index>\d+)$')

        # Maximum usable queues: 8, Queues in use: 4
        # Queues supported: 8, Queues in use: 4
        p2 = re.compile(r'^(Maximum +usable +queues|Queues +supported): +(?P<interface_queues_supported>\d+), +'
            r'Queues +in +use: +(?P<interface_queues_in_use>\d+)$')

        # Exclude aggregate overhead bytes: disabled
        p3 = re.compile(r'^Exclude +aggregate +overhead +bytes: +(?P<overhead_bytes>\S+)$')

        # Logical interface aggregate statistics: disabled
        p4 = re.compile(r'^Logical +interface +aggregate +statistics: +(?P<aggregate_statistics>\S+)$')

        # Shaping rate: 1000000 bps
        p5 = re.compile(r'^Shaping +rate: +(?P<interface_shaping_rate>\d+) +bps$')

        # Scheduler map: <default>, Index: 2
        p6 = re.compile(r'^Scheduler +map: +(?P<scheduler_map_name>\S+), +Index: +(?P<scheduler_map_index>\d+)$')

        # Congestion-notification: Disabled
        p7 = re.compile(r'^Congestion-notification: +(?P<congestion_notification_map>\S+)$')

        # Logical interface: ge-0/0/2.0, Index: 335
        p8 = re.compile(r'^Logical +interface: +(?P<i_logical_name>\S+), +Index: +(?P<i_logical_index>\S+)$')

        # Classifier              dscp-ipv6-compatibility dscp-ipv6                  9
        # Rewrite-Output          EXP-test               exp (mpls-any)          49467
        p9 = re.compile(r'^(?P<object_type>\S+) +(?P<object_name>\S+) +(?P<object_subtype>\S+( +\(\S+\))?) +'
            r'(?P<index>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Physical interface: ge-0/0/2, Index: 150
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict = ret_dict.setdefault('cos-interface-information', {}). \
                    setdefault('interface-map', {})
                interface_map_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Maximum usable queues: 8, Queues in use: 4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_queues_supported = group['interface_queues_supported']
                interface_queues_in_use = group['interface_queues_in_use']
                interface_map_dict.update({'interface-queues-supported': interface_queues_supported})
                interface_map_dict.update({'interface-queues-in-use': interface_queues_in_use})
                continue
            
            # Exclude aggregate overhead bytes: disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict.update({'interface-exclude-queue-overhead-bytes': group['overhead_bytes']})
                continue
            
            # Logical interface aggregate statistics: disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict.update({'interface-logical-interface-aggregate-statistics': group['aggregate_statistics']})
                continue

            # Shaping rate: 1000000 bps
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict.update({'interface-shaping-rate': group['interface_shaping_rate']})
                continue
            
            # Scheduler map: <default>, Index: 2
            m = p6.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Congestion-notification: Disabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                interface_map_dict.update({'interface-congestion-notification-map': group['congestion_notification_map']})
                continue
            
            # Logical interface: ge-0/0/2.0, Index: 335
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_logical_map_dict = interface_map_dict.setdefault('i-logical-map', {})
                intf_logical_map_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Classifier              dscp-ipv6-compatibility dscp-ipv6                  9
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cos_objects = intf_logical_map_dict.setdefault('cos-objects', {})
                cos_object_index = cos_objects.setdefault('cos-object-index', [])
                cos_object_index.append(group['index'])

                cos_object_name = cos_objects.setdefault('cos-object-name', [])
                cos_object_name.append(group['object_name'])

                cos_object_subtype = cos_objects.setdefault('cos-object-subtype', [])
                cos_object_subtype.append(group['object_subtype'])

                cos_object_type = cos_objects.setdefault('cos-object-type', [])
                cos_object_type.append(group['object_type'])

                continue
        return ret_dict
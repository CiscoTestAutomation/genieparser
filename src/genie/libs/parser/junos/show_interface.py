"""show_interface.py

JunOS parsers for the following show commands:
    * show interfaces terse
    * show interfaces terse | match <interface>
    * show interfaces terse {interface}
    * show interfaces {interface} terse
    * show interfaces {interface} detail
    * show interfaces descriptions
    * show interfaces descriptions {interface}
    * show interfaces queue {interface}
    * show interfaces policers {interface}
    * show interfaces diagnostics optics {interface}
    * show interfaces diagnostics optics
    * show interfaces {interface} extensive
    * show interfaces extensive
    * show interfaces extensive {interface}
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, Or, ListOf

# import parser utils
from genie.libs.parser.utils.common import Common


# =======================================================
# Schema for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowInterfacesTerseSchema(MetaParser):
    """Schema for show interfaces terse [| match <interface>]"""

    schema = {
        Any(): {
            'oper_status': str,
            Optional('link_state'): str,
            Optional('admin_state'): str,
            Optional('phys_address'): str,
            'enabled': bool,
            Optional('protocol'): {
                Any():{
                    Optional(Any()): {
                        'local': str,
                        Optional('remote'): str,
                    },
                },
            },
        }
    }

# =======================================================
# Parser for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowInterfacesTerse(ShowInterfacesTerseSchema):
    """ Parser for:
            - show interfaces terse
            - show interfaces {interface} terse
            - show interfaces terse {interface}
    """

    cli_command = [
        'show interfaces terse',
        'show interfaces {interface} terse'
    ]

    exclude = [
        'duration'
    ]

    def cli(self, interface=None, output=None):
        # execute the command
        if output is None:
            if interface:
                cmd = self.cli_command[1]
                cmd = cmd.format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # error: interface ge-0/0/3.0 not found
        p0 = re.compile(r'^error:\s+interface\s+\S+\s+not\s+found$')

        # Interface               Admin Link Proto    Local                 Remote
        # lo0.0                   up    up   inet     10.1.1.1            --> 0/0
        # em1.0                   up    up   inet     10.0.0.4/8
        # fxp0                    up    up
        p1 =  re.compile(r'^(?P<interface>\S+) +(?P<admin_state>\w+) +(?P<link_state>\w+) *'
                          '(?P<protocol>\S+)? *(?P<local>[\w\.\:\/]+)?( *'
                          '[\-\>]+? *(?P<remote>[\w\.\:\/]+))?$')


        #                                             172.16.64.1/2
        #                                    inet6    fe80::250:56ff:fe82:ba52/64
        #                                             2001:db8:8d82:0:a::4/64
        #                                    tnp      0x4
        #                                             10.11.11.11         --> 0/0
        p2 =  re.compile(r'^((?P<protocol>\S+) +)?(?P<local>((\d+\.[\d\.\/]+)|(\w+\:[\w\:\/]+)|(0x\d+))+)'
                          ' *(([\-\>]+) *(?P<remote>[\w\.\:\/]+))?$')
        #                                    multiservice
        p3 = re.compile(r'^((?P<protocol>\S+))$')



        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            if 'show interfaces terse' in line:
                continue

            # error: interface ge-0/0/3.0 not found
            m = p0.match(line)
            if m:
                return ret_dict

            # fxp0                    up    up
            # em1.0                   up    up   inet     10.0.0.4/8
            # lo0.0                   up    up   inet     10.1.1.1            --> 0/0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interface']
                intf_dict = ret_dict.setdefault(interface, {})
                intf_dict.update({'admin_state': groups['admin_state'],
                                  'link_state': groups['link_state'],
                                  'oper_status': groups['link_state'],
                                  'enabled': 'up' in groups['admin_state']})
                if groups['protocol']:
                    protocol = groups['protocol']
                    pro_dict = intf_dict.setdefault('protocol', {}).setdefault(groups['protocol'], {})
                if groups['local']:
                    pro_dict = pro_dict.setdefault(groups['local'], {})
                    pro_dict['local'] = groups['local']
                    if groups['remote']:
                        pro_dict['remote'] = groups['remote']
                continue


            #                                             172.16.64.1/2
            #                                    inet6    fe80::250:56ff:fe82:ba52/64
            #                                             2001:db8:8d82:0:a::4/64
            #                                    tnp      0x4
            #                                             10.11.11.11         --> 0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                try:
                    protocol = groups['protocol'] or protocol
                except Exception:
                    continue
                pro_dict = intf_dict.setdefault('protocol', {}).setdefault(protocol, {}).setdefault(groups['local'], {})
                pro_dict['local'] = groups['local']
                if groups['remote']:
                    pro_dict['remote'] = groups['remote']
                continue

            #                                    multiservice
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                protocol = m.groupdict()['protocol']
                pro_dict = intf_dict.setdefault('protocol', {}).setdefault(protocol, {})
                continue
        return ret_dict

class ShowInterfacesTerseMatch(ShowInterfacesTerse):
    """ Parser for:
            - show interfaces terse | match {interface}
    """

    cli_command = 'show interfaces terse | match {interface}'

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        return super().cli(output=out)

class ShowInterfacesTerseInterface(ShowInterfacesTerse):
    """ Parser for:
            - 'show interfaces terse {interface}'
    """

    cli_command = 'show interfaces terse {interface}'

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        return super().cli(output=out)

class ShowInterfacesDescriptionsSchema(MetaParser):
    """ Schema for:
            * show interfaces descriptions
            * show interfaces descriptions {interface}
    """

    schema = {
        "interface-information": {
            "physical-interface": ListOf({
                "admin-status": str,
                "description": str,
                "name": str,
                "oper-status": str
            })
        }
    }

class ShowInterfacesDescriptions(ShowInterfacesDescriptionsSchema):
    """ Parser for:
            * show interfaces descriptions
            * show interfaces descriptions {interface}
    """
    cli_command = ['show interfaces descriptions',
                    'show interfaces descriptions {interface}']


    def cli(self, interface=None, output=None):
        if not output:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Interface       Admin Link Description
        p1 = re.compile(r'^Interface +Admin +Link +Description$')

        # resolving parser issue to display Interface when Description containing spaces
        # ge-0/0/1.0      up    up   LBT0 link to LABP1 (GigabitEthernet0/0/0/0) - backbone
        p2 = re.compile(r'^(?P<name>\S+)\s+(?P<admin_status>\S+)\s+(?P<oper_status>\S+)\s+(?P<description>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # Interface       Admin Link Description
            m = p1.match(line)
            if m:
                continue

            # ge-0/0/0        up    up   none/100G/in/hktGCS002_ge-0/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("interface-information", {}).setdefault("physical-interface", [])
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                entry_list.append(entry)
                continue

        return ret_dict

class ShowInterfacesSchema(MetaParser):
    """ Parser for:
        'show interfaces'
    """
    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "interface-information": {
    #         Optional("@junos:style"): str,
    #         Optional("@xmlns"): str,
    #         "physical-interface": [
    #             {
    #                 "active-alarms": {
    #                     "interface-alarms": {
    #                         "alarm-not-present": str,
    #                         "ethernet-alarm-link-down": str
    #                     }
    #                 },
    #                 "active-defects": {
    #                     "interface-alarms": {
    #                         "alarm-not-present": str,
    #                         "ethernet-alarm-link-down": str
    #                     }
    #                 },
    #                 "admin-status": {
    #                     "#text": str,
    #                     Optional("@junos:format"): str
    #                 },
    #                 "bpdu-error": str,
    #                 "clocking": str,
    #                 "current-physical-address": str,
    #                 "description": str,
    #                 "eth-switch-error": str,
    #                 "ethernet-fec-mode": {
    #                     Optional("@junos:style"): str,
    #                     "enabled_fec_mode": str
    #                 },
    #                 "ethernet-fec-statistics": {
    #                     Optional("@junos:style"): str,
    #                     "fec_ccw_count": str,
    #                     "fec_ccw_error_rate": str,
    #                     "fec_nccw_count": str,
    #                     "fec_nccw_error_rate": str
    #                 },
    #                 "ethernet-pcs-statistics": {
    #                     Optional("@junos:style"): str,
    #                     "bit-error-seconds": str,
    #                     "errored-blocks-seconds": str
    #                 },
    #                 "hardware-physical-address": str,
    #                 "if-auto-negotiation": str,
    #                 "if-config-flags": str,
    #                 "if-device-flags": {
    #                     "ifdf-present": str,
    #                     "ifdf-running": str
    #                 },
    #                 "if-flow-control": str,
    #                 "if-media-flags": {
    #                     "ifmf-none": str
    #                 },
    #                 "if-remote-fault": str,
    #                 "if-type": str,
    #                 "ifd-specific-config-flags": {
    #                     "internal-flags": str
    #                 },
    #                 "ingress-queue-counters": {
    #                     Optional("@junos:style"): str,
    #                     "interface-cos-short-summary": {
    #                         "intf-cos-num-queues-in-use": str,
    #                         "intf-cos-num-queues-supported": str,
    #                         "intf-cos-queue-type": str
    #                     },
    #                     "queue": [
    #                         {
    #                             "forwarding-class-name": str,
    #                             "queue-counters-queued-packets": str,
    #                             "queue-counters-total-drop-packets": str,
    #                             "queue-counters-trans-packets": str,
    #                             "queue-number": str
    #                         }
    #                     ]
    #                 },
    #                 "queue-counters": {
    #                     Optional("@junos:style"): str,
    #                     "interface-cos-short-summary": {
    #                         "intf-cos-num-queues-in-use": str,
    #                         "intf-cos-num-queues-supported": str,
    #                         "intf-cos-queue-type": str
    #                     },
    #                     "queue": [
    #                         {
    #                             "forwarding-class-name": str,
    #                             "queue-counters-queued-packets": str,
    #                             "queue-counters-total-drop-packets": str,
    #                             "queue-counters-trans-packets": str,
    #                             "queue-number": str
    #                         }
    #                     ]
    #                 },
    #                 "queue-num-forwarding-class-name-map": [
    #                     {
    #                         "forwarding-class-name": str,
    #                         "queue-number": str
    #                     }
    #                 ]
    #                 "interface-flapped": {
    #                     "#text": str,
    #                     Optional("@junos:seconds"): str
    #                 },
    #                 "interface-transmit-statistics": str,
    #                 "l2pt-error": str,
    #                 "ld-pdu-error": str,
    #                 "link-level-type": str,
    #                 "link-type": str,
    #                 "local-index": str,
    #                 "logical-interface": {
    #                     "address-family": [
    #                         {
    #                             "address-family-flags": {
    #                                 "ifff-is-primary": str,
    #                                 "ifff-no-redirects": str,
    #                                 "ifff-none": str,
    #                                 "ifff-sendbcast-pkt-to-re": str,
    #                                 "internal-flags": str
    #                             },
    #                             "address-family-name": str,
    #                             "filter-information": str,
    #                             "generation": str,
    #                             "interface-address": {
    #                                 "generation": str,
    #                                 "ifa-broadcast": str,
    #                                 "ifa-destination": str,
    #                                 "ifa-flags": {
    #                                     "ifaf-current-default": str,
    #                                     "ifaf-current-preferred": str,
    #                                     "ifaf-current-primary": str
    #                                 },
    #                                 "ifa-local": str
    #                             },
    #                             "intf-curr-cnt": str,
    #                             "intf-dropcnt": str,
    #                             "intf-unresolved-cnt": str,
    #                             "max-local-cache": str,
    #                             "maximum-labels": str,
    #                             "mtu": str,
    #                             "new-hold-limit": str,
    #                             "policer-information": str,
    #                             "route-table": str,
    #                         }
    #                     ],
    #                     "encapsulation": str,
    #                     "filter-information": str,
    #                     "if-config-flags": {
    #                         "iff-snmp-traps": str,
    #                         "iff-up": str,
    #                         "internal-flags": str
    #                     },
    #                     "lag-traffic-statistics": {
    #                         "aggregate-member-info": {
    #                             "aggregate-member-count": str
    #                         },
    #                         "if-distribution-list-information": [
    #                             {
    #                                 "if-list": [
    #                                     {
    #                                         "if-child-name": str,
    #                                         "if-status": str
    #                                     }
    #                                 ],
    #                                 "list-status": str,
    #                                 "list-type": str
    #                             }
    #                         ],
    #                         "lag-adaptive-statistics": {
    #                             "adaptive-adjusts": str,
    #                             "adaptive-scans": str,
    #                             "adaptive-updates": str
    #                         },
    #                         "lag-bundle": {
    #                             "input-bps": str,
    #                             "input-bytes": str,
    #                             "input-packets": str,
    #                             "input-pps": str,
    #                             "output-bps": str,
    #                             "output-bytes": str,
    #                             "output-packets": str,
    #                             "output-pps": str
    #                         },
    #                         "lag-lacp-info": [
    #                             {
    #                                 "lacp-port-key": str,
    #                                 "lacp-port-number": str,
    #                                 "lacp-port-priority": str,
    #                                 "lacp-role": str,
    #                                 "lacp-sys-priority": str,
    #                                 "lacp-system-id": str,
    #                                 "name": str
    #                             }
    #                         ],
    #                         "lag-lacp-statistics": [
    #                             {
    #                                 "illegal-rx-packets": str,
    #                                 "lacp-rx-packets": str,
    #                                 "lacp-tx-packets": str,
    #                                 "name": str,
    #                                 "unknown-rx-packets": str
    #                             }
    #                         ],
    #                         "lag-link": [
    #                             {
    #                                 "input-bps": str,
    #                                 "input-bytes": str,
    #                                 "input-packets": str,
    #                                 "input-pps": str,
    #                                 "name": str,
    #                                 "output-bps": str,
    #                                 "output-bytes": str,
    #                                 "output-packets": str,
    #                                 "output-pps": str
    #                             }
    #                         ],
    #                         "lag-marker": [
    #                             {
    #                                 "illegal-rx-packets": str,
    #                                 "lacp-rx-packets": str,
    #                                 "lacp-tx-packets": str,
    #                                 "marker-response-tx-packets": str,
    #                                 "marker-rx-packets": str,
    #                                 "name": str,
    #                                 "unknown-rx-packets": str
    #                             }
    #                         ]
    #                     },
    #                     "local-index": str,
    #                     "logical-interface-bandwidth": str,
    #                     "name": str,
    #                     "policer-overhead": str,
    #                     "snmp-index": str,
    #                     "traffic-statistics": {
    #                         Optional("@junos:style"): str,
    #                         "input-packets": str,
    #                         "output-packets": str
    #                     }
    #                 },
    #                 "loopback": str,
    #                 "minimum-bandwidth-in-aggregate": str,
    #                 "minimum-links-in-aggregate": str,
    #                 "mru": str,
    #                 "mtu": str,
    #                 "name": str,
    #                 "oper-status": str,
    #                 "pad-to-minimum-frame-size": str,
    #                 "physical-interface-cos-information": {
    #                     "physical-interface-cos-hw-max-queues": str,
    #                     "physical-interface-cos-use-max-queues": str
    #                 },
    #                 "snmp-index": str,
    #                 "sonet-mode": str,
    #                 "source-filtering": str,
    #                 "speed": str,
    #                 "traffic-statistics": {
    #                     "input-bps": str,
    #                     "input-bytes": str,
    #                     "input-packets": str,
    #                     "input-pps": str,
    #                     "ipv6-transit-statistics": {
    #                         "input-bps": str,
    #                         "input-bytes": str,
    #                         "input-packets": str,
    #                         "input-pps": str,
    #                         "output-bps": str,
    #                         "output-bytes": str,
    #                         "output-packets": str,
    #                         "output-pps": str
    #                     },
    #                     "output-bps": str,
    #                     "output-bytes": str,
    #                     "output-packets": str,
    #                     "output-pps": str
    #                 }
    #             }
    #         ]
    #     }
    # }

    def verify_physical_interface_list(value):
        # Pass physical-interface list of dict in value
        if not isinstance(value, list):
            raise SchemaError('physical interface is not a list')

    interface_address_schema = {
        Optional("ifa-broadcast"): str,
        Optional("ifa-destination"): str,
        Optional("generation"): str,
        "ifa-flags": {
            Optional("ifaf-current-default"): bool,
            Optional("ifaf-current-preferred"): bool,
            Optional("ifaf-current-primary"): bool,
            Optional("ifaf-is-primary"): bool,
            Optional("ifaf-is-preferred"): bool,
            Optional("ifaf-kernel"): bool,
            Optional("ifaf-preferred"): bool,
            Optional("ifaf-primary"): bool,
            Optional("ifaf-is-default"): bool,
            Optional("ifaf-none"): bool,
            Optional("ifaf-dest-route-down"): bool,
        },
        Optional("ifa-local"): str
    }

    af_schema = Schema({
        Optional("address-family-flags"): {
            Optional("ifff-is-primary"): bool,
            Optional("ifff-no-redirects"): bool,
            Optional("ifff-none"): bool,
            Optional("ifff-sendbcast-pkt-to-re"): bool,
            Optional("internal-flags"): bool,
            Optional("ifff-primary"): bool,
            Optional("ifff-receive-ttl-exceeded"): bool,
            Optional("ifff-receive-options"): bool,
            Optional("ifff-encapsulation"): str,
            Optional("ifff-user-mtu"): bool,
        },
        Optional("address-family-name"): str,
        Optional("filter-information"): str,
        Optional("generation"): str,
        Optional("interface-address"): Or(
            interface_address_schema,
            ListOf(interface_address_schema)
        ),
        Optional("intf-curr-cnt"): str,
        Optional("intf-dropcnt"): str,
        Optional("intf-unresolved-cnt"): str,
        Optional("generation"): str,
        Optional("route-table"): str,
        Optional("max-local-cache"): str,
        Optional("maximum-labels"): str,
        Optional("mtu"): str,
        Optional("new-hold-limit"): str,
        Optional("policer-information"): {
            Optional("policer-input"): str,
            Optional("policer-output"): str,
        }
    })

    lag_bundle_list_schema = Schema({
        Optional("input-bps"): str,
        Optional("input-bytes"): str,
        Optional("input-packets"): str,
        Optional("input-pps"): str,
        Optional("output-bps"): str,
        Optional("output-bytes"): str,
        Optional("output-packets"): str,
        Optional("output-pps"): str
    })

    lag_lacp_info_list_schema = Schema({
        Optional("lacp-port-key"): str,
        Optional("lacp-port-number"): str,
        Optional("lacp-port-priority"): str,
        Optional("lacp-role"): str,
        Optional("lacp-sys-priority"): str,
        Optional("lacp-system-id"): str,
        Optional("name"): str
    })

    lag_lacp_statistics_list_schema = Schema({
        Optional("illegal-rx-packets"): str,
        Optional("lacp-rx-packets"): str,
        Optional("lacp-tx-packets"): str,
        Optional("name"): str,
        Optional("unknown-rx-packets"): str
    })

    lag_link_list_schema = Schema({
        Optional("input-bps"): str,
        Optional("input-bytes"): str,
        Optional("input-packets"): str,
        Optional("input-pps"): str,
        Optional("name"): str,
        Optional("output-bps"): str,
        Optional("output-bytes"): str,
        Optional("output-packets"): str,
        Optional("output-pps"): str
    })

    lag_marker_list_schema = Schema({
        Optional("illegal-rx-packets"): str,
        Optional("lacp-rx-packets"): str,
        Optional("lacp-tx-packets"): str,
        Optional("marker-response-tx-packets"): str,
        Optional("marker-rx-packets"): str,
        Optional("name"): str,
        Optional("unknown-rx-packets"): str
    })

    l_i_schema = Schema({
        Optional("address-family"): ListOf(af_schema),
        Optional("encapsulation"): str,
        Optional("filter-information"): str,
        "if-config-flags": {
            "iff-snmp-traps": bool,
            "iff-up": bool,
            Optional("internal-flags"): str
        },
        Optional("lag-traffic-statistics"): {
            Optional("aggregate-member-info"): {
                "aggregate-member-count": str
            },
            Optional("if-distribution-list-information"): ListOf({
                Optional("if-list"): ListOf({
                    Optional("if-child-name"): str,
                    Optional("if-status"): str,
                }),
                Optional("list-status"): str,
                Optional("list-type"): str
            }),
            Optional("lag-adaptive-statistics"): {
                "adaptive-adjusts": str,
                "adaptive-scans": str,
                "adaptive-updates": str
            },
            Optional("lag-bundle"): Or(
                lag_bundle_list_schema,
                ListOf(lag_bundle_list_schema)
            ),
            Optional("lag-lacp-info"): Or(
                lag_lacp_info_list_schema,
                ListOf(lag_lacp_info_list_schema)
            ),
            Optional("lag-lacp-statistics"): Or(
                lag_lacp_statistics_list_schema,
                ListOf(lag_lacp_statistics_list_schema)
            ),
            Optional("lag-link"): Or(
                lag_link_list_schema,
                ListOf(lag_link_list_schema)
            ),
            Optional("lag-marker"): Or(
                lag_marker_list_schema,
                ListOf(lag_marker_list_schema)
            ),
        },
        "local-index": str,
        Optional("logical-interface-bandwidth"): str,
        "name": str,
        Optional("description"): str,
        Optional("policer-overhead"): str,
        Optional("snmp-index"): str,
        Optional("traffic-statistics"): {
            Optional("@junos:style"): str,
            "input-packets": str,
            Optional("input-bytes"): str,
            "output-packets": str,
            Optional("output-bytes"): str,
            Optional("ipv6-transit-statistics"): {
                "input-bytes": str,
                "input-packets": str,
                "output-bytes": str,
                "output-packets": str,
            },
        },
        Optional("transit-traffic-statistics"): {
                "input-bps": str,
                "input-bytes": str,
                "input-packets": str,
                "input-pps": str,
                Optional("ipv6-transit-statistics"): {
                    Optional("input-bps"): str,
                    "input-bytes": str,
                    "input-packets": str,
                    Optional("input-pps"): str,
                    Optional("output-bps"): str,
                    "output-bytes": str,
                    "output-packets": str,
                    Optional("output-pps"): str
                },
                "output-bps": str,
                "output-bytes": str,
                "output-packets": str,
                "output-pps": str
            }
    })

    queue_schema = Schema({
        Optional("forwarding-class-name"): str,
        "queue-counters-queued-packets": str,
        "queue-counters-total-drop-packets": str,
        "queue-counters-trans-packets": str,
        "queue-number": str,
        Optional("forwarding-class-name"): str
    })

    # Create physical-interface Schema
    physical_interface_schema = Schema({
        Optional("down-hold-time"): str,
        Optional("up-hold-time"): str,
        Optional("statistics-cleared"): str,
        Optional("active-alarms"): {
            Optional("interface-alarms"): {
                Optional("alarm-not-present"): bool,
                Optional("ethernet-alarm-link-down"): bool,
            }
        },
        Optional("active-defects"): {
            Optional("interface-alarms"): {
                Optional("alarm-not-present"): bool,
                Optional("ethernet-alarm-link-down"): bool
            }
        },
        Optional("admin-status"): {
            Optional("#text"): str,
            Optional("@junos:format"): str
        },
        Optional("bpdu-error"): str,
        Optional("clocking"): str,
        Optional("current-physical-address"): str,
        Optional("description"): str,
        Optional("eth-switch-error"): str,
        Optional("ethernet-fec-mode"): {
            Optional("@junos:style"): str,
            "enabled_fec_mode": str
        },
        Optional("ethernet-fec-statistics"): {
            Optional("@junos:style"): str,
            "fec_ccw_count": str,
            "fec_ccw_error_rate": str,
            "fec_nccw_count": str,
            "fec_nccw_error_rate": str
        },
        Optional("ethernet-pcs-statistics"): {
            Optional("@junos:style"): str,
            "bit-error-seconds": str,
            "errored-blocks-seconds": str
        },
        Optional("hardware-physical-address"): str,
        Optional("if-config-flags"): {
            Optional("internal-flags"): str,
            "iff-snmp-traps": bool,
            Optional("iff-hardware-down"): bool,
        },
        Optional("if-auto-negotiation"): str,
        Optional("if-device-flags"): {
            "ifdf-present": bool,
            "ifdf-running": bool,
            Optional("ifdf-loopback"): bool,
            Optional("ifdf-down"): bool,
        },
        Optional("if-flow-control"): str,
        Optional("if-media-flags"): {
            "ifmf-none": bool
        },
        Optional("if-remote-fault"): str,
        Optional("if-type"): str,
        Optional("ifd-specific-config-flags"): {
            Optional("internal-flags"): str
        },
        Optional("interface-flapped"): {
            "#text": str,
            Optional("@junos:seconds"): str
        },
        Optional("interface-transmit-statistics"): str,
        Optional("l2pt-error"): str,
        Optional("ld-pdu-error"): str,
        Optional("link-level-type"): str,
        Optional("link-type"): str,
        Optional("link-mode"): str,
        Optional("local-index"): str,
        Optional("logical-interface"): ListOf(l_i_schema),
        Optional("loopback"): str,
        Optional("minimum-links-in-aggregate"): str,
        Optional("minimum-bandwidth-in-aggregate"): str,
        Optional("lsi-traffic-statistics"): {
            Optional("@junos:style"): str,
            "input-bps": str,
            "input-bytes": str,
            "input-packets": str,
            "input-pps": str
        },
        Optional("mru"): str,
        Optional("mtu"): str,
        Optional("mac-rewrite-error"): str,
        "name": str,
        Optional("oper-status"): str,
        Optional("pad-to-minimum-frame-size"): str,
        Optional("physical-interface-cos-information"): {
            "physical-interface-cos-hw-max-queues": str,
            "physical-interface-cos-use-max-queues": str
        },
        Optional("snmp-index"): str,
        Optional("sonet-mode"): str,
        Optional("source-filtering"): str,
        Optional("speed"): str,
        Optional("stp-traffic-statistics"): {
            Optional("@junos:style"): str,
            Optional("stp-input-bytes-dropped"): str,
            Optional("stp-input-packets-dropped"): str,
            Optional("stp-output-bytes-dropped"): str,
            Optional("stp-output-packets-dropped"): str
        },
        Optional("traffic-statistics"): {
            Optional("@junos:style"): str,
            Optional("input-bps"): str,
            Optional("output-bytes"): str,
            Optional("input-bytes"): str,
            Optional("input-packets"): str,
            Optional("input-pps"): str,
            Optional("output-bps"): str,
            Optional("output-packets"): str,
            Optional("output-pps"): str,
            Optional("ipv6-transit-statistics"): {
                Optional("input-bps"): str,
                Optional("input-bytes"): str,
                Optional("input-packets"): str,
                Optional("input-pps"): str,
                Optional("output-bps"): str,
                Optional("output-bytes"): str,
                Optional("output-packets"): str,
                Optional("output-pps"): str
            },
        },
        Optional("output-error-list"): {
            Optional("aged-packets"): str,
            Optional("carrier-transitions"): str,
            Optional("hs-link-crc-errors"): str,
            Optional("mtu-errors"): str,
            Optional("output-collisions"): str,
            Optional("output-drops"): str,
            Optional("output-errors"): str,
            Optional("output-fifo-errors"): str,
            Optional("output-resource-errors"): str
        },
        Optional("ethernet-mac-statistics"): {
                Optional("@junos:style"): str,
                Optional("input-broadcasts"): str,
                Optional("input-bytes"): str,
                Optional("input-code-violations"): str,
                Optional("input-crc-errors"): str,
                Optional("input-fifo-errors"): str,
                Optional("input-fragment-frames"): str,
                Optional("input-jabber-frames"): str,
                Optional("input-mac-control-frames"): str,
                Optional("input-mac-pause-frames"): str,
                Optional("input-multicasts"): str,
                Optional("input-oversized-frames"): str,
                Optional("input-packets"): str,
                Optional("input-total-errors"): str,
                Optional("input-unicasts"): str,
                Optional("input-vlan-tagged-frames"): str,
                Optional("output-broadcasts"): str,
                Optional("input-multicasts"): str,
                Optional("output-bytes"): str,
                Optional("output-crc-errors"): str,
                Optional("output-fifo-errors"): str,
                Optional("output-mac-control-frames"): str,
                Optional("output-mac-pause-frames"): str,
                Optional("output-multicasts"): str,
                Optional("output-packets"): str,
                Optional("output-total-errors"): str,
                Optional("output-unicasts"): str,
        },
        Optional("ethernet-filter-statistics"): {
            "input-packets": str,
            "input-reject-count": str,
            "input-reject-destination-address-count": str,
            "input-reject-source-address-count": str,
            "output-packet-error-count": str,
            "output-packet-pad-count": str,
            "output-packets": str,
            "cam-destination-filter-count": str,
            "cam-source-filter-count": str,
        },
        Optional("cos-information"): {
            Optional("cos-stream-information"): {
                "cos-direction": str,
                Optional("cos-queue-configuration"): ListOf({
                    "cos-queue-bandwidth": str,
                    "cos-queue-bandwidth-bps": str,
                    "cos-queue-buffer": str,
                    "cos-queue-buffer-bytes": str,
                    "cos-queue-forwarding-class": str,
                    "cos-queue-limit": str,
                    "cos-queue-number": str,
                    "cos-queue-priority": str,
                })
            }
        },
        Optional("input-error-list"): {
                Optional("framing-errors"): str,
                Optional("input-discards"): str,
                Optional("input-drops"): str,
                Optional("input-errors"): str,
                Optional("input-fifo-errors"): str,
                Optional("input-giants"): str,
                Optional("input-l2-channel-errors"): str,
                Optional("input-l2-mismatch-timeouts"): str,
                Optional("input-l3-incompletes"): str,
                Optional("input-resource-errors"): str,
                Optional("input-runts"): str
        },
        Optional("transit-traffic-statistics"): {
            "input-bps": str,
            "input-bytes": str,
            "input-packets": str,
            "input-pps": str,
            Optional("ipv6-transit-statistics"): {
                Optional("input-bps"): str,
                "input-bytes": str,
                "input-packets": str,
                Optional("input-pps"): str,
                Optional("output-bps"): str,
                "output-bytes": str,
                "output-packets": str,
                Optional("output-pps"): str
            },
            "output-bps": str,
            "output-bytes": str,
            "output-packets": str,
            "output-pps": str
        },
        Optional("pfe-information"): {
            "destination-mask": str,
            "destination-slot": str
        },
        Optional("ingress-queue-counters"): {
            "interface-cos-short-summary": {
                "intf-cos-num-queues-in-use": str,
                "intf-cos-num-queues-supported": str,
                "intf-cos-queue-type": str,
            },
            "queue": ListOf(queue_schema),
        },
        Optional("queue-counters"): {
            "interface-cos-short-summary": {
                "intf-cos-num-queues-in-use": str,
                "intf-cos-num-queues-supported": str,
                "intf-cos-queue-type": str,
            },
            "queue": ListOf(queue_schema)
        },
        Optional("queue-num-forwarding-class-name-map"): ListOf({
            "forwarding-class-name": str,
            "queue-number": str,
        })
    })

    schema = {
        Optional("@xmlns:junos"): str,
        "interface-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "physical-interface": ListOf(physical_interface_schema)
        }
    }

class ShowInterfaces(ShowInterfacesSchema):
    cli_command = ['show interfaces', 'show interfaces {interface}']

    def cli(self, interface=None, output=None):

        if not output:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        ret_dict = {}
        
        statistics_type = None

        # Physical interface: ge-0/0/0, Enabled, Physical link is Up
        p1 = re.compile(r'^Physical +interface: +(?P<name>\S+), +'
            r'(?P<admin_status>\S+), +Physical +link +is +(?P<oper_status>\S+)$')

        # Interface index: 148, SNMP ifIndex: 526
        p2 = re.compile(r'^Interface +index: +(?P<local_index>\d+), +'
            r'SNMP +ifIndex: +(?P<snmp_index>\d+)'
            r'(, +Generation: +\S+)?$')

        # Description: none/100G/in/hktGCS002_ge-0/0/0
        # Description: TEST-DESC:1|TEST#1234 DEV
        p3 = re.compile(r'^Description: +(?P<description>.+)$')

        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, Speed: 100Gbps, BPDU Error: None, Loopback: Disabled,
        # Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        # Link-level type: Ethernet, MTU: 1514, Speed: 1Gbps, BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled, Source filtering: Disabled, Flow control: Disabled
        p4 = re.compile(r'^(Type: +\S+, )?Link-level +type: +(?P<link_level_type>\S+), '
                        r'+MTU: +(?P<mtu>\S+)(, +MRU: +(?P<mru>\d+))?(, +(?P<sonet_mode>\S+) +mode)?'
                        r'(, +Link-mode: +(?P<link_mode>\S+))?(, +Speed: +(?P<speed>\S+))?'
                        r'(, +BPDU +Error: +(?P<bpdu_error>\w+))?'
                        r'(, +MAC-REWRITE Error: +(?P<mac_rewrite_error>\S+))?'
                        r'(, +Loopback: +(?P<loopback>\S+))?'
                        r'(, Source +filtering: +(?P<source_filtering>\S+))?'
                        r'(, +Flow +control: +(?P<if_flow_control>\S+))?(,)?$')
        
        # Speed: 1000mbps, BPDU Error: None, Loop Detect PDU Error: None,
        p4_1 = re.compile(r'^(Speed: +(?P<speed>[^\s,]+))(, +)?'
                          r'(BPDU +Error: +(?P<bpdu_error>[^\s,]+))?(, +)?'
                          r'(Loop +Detect +PDU +Error: +(?P<ld_pdu_error>[^\s,]+))?(, +)?')

        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None, Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None,
        p4_2 = re.compile(r'^Link-level +type: +(?P<link_level_type>\S+), +MTU: +(?P<mtu>\S+)'
                          r'(, +MRU: +(?P<mru>\d+))?(, +(?P<sonet_mode>\S+) +mode)?'
                          r'(, +Speed: +(?P<speed>\S+))?(, +BPDU +Error: +(?P<bpdu_error>\S+),)?'
                          r'( +Loop +Detect +PDU +Error: +(?P<ld_pdu_error>\S+),)?'
                          r'( +Ethernet-Switching +Error: +(?P<eth_switch_error>\S+),)?'
                          r'( +MAC-REWRITE +Error: +\S+)?$')

        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, Speed: 100Gbps, BPDU Error: None, Loopback: Disabled,

        # Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        p5 = re.compile(r'^Loop +Detect +PDU +Error: +(?P<ld_pdu_error>\S+), +'
            r'Ethernet-Switching +Error: +(?P<eth_switch_error>\S+), +MAC-REWRITE +'
            r'Error: +\S+, +Loopback: +(?P<loopback>\S+),$')

        # Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        # BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled
        p5_1 = re.compile(r'^((Ethernet-Switching +Error: +(?P<eth_switch_error>[^\s,]+))|(BPDU +Error: +(?P<bpdu_error>[^\s,]+)))(, +)?(MAC-REWRITE +Error: +[^\s,]+)?(, +)?(Loopback: +(?P<loopback>[^\s,]+))(, +)?')

        # Loopback: Disabled, Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        p5_2 = re.compile(r'^(Loopback: +(?P<loopback>\S+),)?'
                          r'( +Source +filtering: +(?P<source_filtering>\S+),)?'
                          r'( +Flow +control: +(?P<if_flow_control>\S+),)?'
                          r'( +Auto-negotiation: +(?P<if_auto_negotiation>\S+),)?'
                          r'( +Remote +fault: +(?P<if_remote_fault>\S+))$')

        # Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        # Source filtering: Disabled, Flow control: Disabled
        p6 = re.compile(r'^Source +filtering: +(?P<source_filtering>\S+), +Flow +control: +(?P<if_flow_control>\S+)(, +Auto-negotiation: +(?P<if_auto_negotiation>\S+), +Remote +fault: +(?P<if_remote_fault>\S+))?$')

        # Pad to minimum frame size: Disabled
        p7 = re.compile(r'^Pad +to +minimum +frame +size: +'
            r'(?P<pad_to_minimum_frame_size>\S+)$')

        # Minimum links needed: 1, Minimum bandwidth needed: 1bps
        p7_1 = re.compile(r'^Minimum +links +needed: +(?P<minimum_links_in_aggregate>\d+), +Minimum +bandwidth +needed: +(?P<minimum_bandwidth_in_aggregate>\S+)$')

        # Device flags   : Present Running
        p8 = re.compile(r'^Device +flags +: +(?P<if_device_flags>[\S\s]+)$')

        # Interface flags: SNMP-Traps Internal: 0x4000
        p9 = re.compile(r'^Interface +flags:( +(?P<hardware_down>Hardware-Down))? +'
                r'(?P<iff_snmp_traps>\S+)( +Internal: +(?P<internal_flags>\S+))?$')

        # Link flags     : None
        p10 = re.compile(r'^Link +flags +: +(?P<if_media_flags>\S+)$')

        # Link type      : Full-Duplex
        p10_1 = re.compile(r'^Link +type +: +(?P<link_type>\S+)$')

        # CoS queues     : 8 supported, 8 maximum usable queues
        p11 = re.compile(r'^CoS +queues +: +(?P<physical_interface_cos_hw_max_queues>\d+) +'
            r'supported, +(?P<physical_interface_cos_use_max_queues>\d+) maximum +'
            r'usable +queues$')

        # Current address: 00:50:56:ff:56:b6, Hardware address: 00:50:56:ff:56:b6
        p12 = re.compile(r'^Current +address: +(?P<current_physical_address>\S+), +'
            r'Hardware +address: +(?P<hardware_physical_address>\S+)$')

        # Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        p13 = re.compile(r'^Last +flapped +: +(?P<interface_flapped>[\S\s]+)$')

        # Input rate     : 2952 bps (5 pps)
        p14 = re.compile(r'^Input +rate +: +(?P<input_bps>\d+) +'
            r'bps +\((?P<input_pps>\d+) +pps\)$')
        
        # Input  bytes  :          19732539397                 3152 bps
        p14_1 = re.compile(r'^Input +bytes *: +(?P<input_bytes>\S+)'
            r'( +(?P<input_bps>\S+) +bps)?$')
        # Output bytes  :          16367814635                 3160 bps
        p14_2 = re.compile(r'^Output +bytes *: +(?P<output_bytes>\S+)'
            r'( +(?P<output_bps>\S+) +bps)?$')
        # Input  packets:            133726363                    5 pps
        p14_3 = re.compile(r'^Input +packets *: +(?P<input_packets>\S+)'
            r'( +(?P<input_pps>\S+) +pps)?$')
        # Output packets:            129306863                    4 pps
        p14_4 = re.compile(r'^Output +packets *: +(?P<output_packets>\S+)'
            r'( +(?P<output_pps>\S+) +pps)?$')
        
        # Output rate    : 3080 bps (3 pps)
        p15 = re.compile(r'^Output +rate +: +(?P<output_bps>\d+) +'
            r'bps +\((?P<output_pps>\d+) +pps\)$')
        
        # Active alarms  : None
        p16 = re.compile(r'^Active +alarms *: +(?P<active_alarms>\S+)$')

        # Active defects : None
        p17 = re.compile(r'^Active +defects *: +(?P<active_defects>\S+)$')
        
        # PCS statistics                      Seconds
        p18 = re.compile(r'^PCS +statistics +Seconds$')

        # Bit errors                             0
        p19 = re.compile(r'^Bit +errors +(?P<bit_error_seconds>\d+)$')

        # Errored blocks                         0
        p20 = re.compile(r'^Errored +blocks +(?P<errored_blocks_seconds>\d+)$')
        
        # Ethernet FEC statistics              Errors
        p21 = re.compile(r'^Ethernet +FEC +statistics +Errors$')

        # FEC Corrected Errors                    0
        # FEC Uncorrected Errors                  0
        # FEC Corrected Errors Rate               0
        # FEC Uncorrected Errors Rate             0
        p22 = re.compile(r'^FEC +Corrected +Errors +(?P<fec_ccw_count>\d+)$')
        p22_1 = re.compile(r'^FEC +Uncorrected +Errors +(?P<fec_nccw_count>\d+)$')
        p22_2 = re.compile(r'^FEC +Corrected +Errors +Rate +(?P<fec_ccw_error_rate>\d+)$')
        p22_3 = re.compile(r'^FEC +Uncorrected +Errors +Rate +(?P<fec_nccw_error_rate>\d+)$')

        # Interface transmit statistics: Disabled
        p23 = re.compile(r'^Interface +transmit +statistics: +'
            r'(?P<interface_transmit_statistics>\S+)$')

        # Logical interface ge-0/0/0.0 (Index 333) (SNMP ifIndex 606)
        p24 = re.compile(r'^Logical +interface +(?P<name>\S+) +'
            r'\(Index +(?P<local_index>\d+)\) +\(SNMP +ifIndex +'
            r'(?P<snmp_index>\d+)\)( +\(Generation +\S+\))?$')

        # Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
        # Flags: Up SNMP-Traps 0x4000 VLAN-Tag [ 0x8100.1 ]  Encapsulation: ENET2
        # Flags: Hardware-Down Device-Down SNMP-Traps 0x4000 VLAN-Tag [ 0x8100.1 ]  Encapsulation: ENET2
        p25 = re.compile(r'^Flags: +(?P<iff_up>(\S+|Hardware-Down Device-Down))'
                         r'( +SNMP-Traps)?( +(?P<internal_flags>\S+))?( +VLAN-Tag +\[[\S\s]+\])?'
                         r' +Encapsulation: +(?P<encapsulation>\S+)$')

        # Input packets : 133657033
        p26 = re.compile(r'^Input +packets *: +(?P<input_packets>\S+)$')

        # Output packets: 129243982
        p27 = re.compile(r'^Output +packets *: +(?P<output_packets>\S+)$')

        # Protocol inet, MTU: 1500, Maximum labels: 2
        # Protocol inet, MTU: 1500, Generation: 150, Route table: 0
        p28 = re.compile(r'^Protocol +(?P<address_family_name>\S+), +'
            r'MTU: +(?P<mtu>\S+)(, +Maximum labels: +'
            r'(?P<maximum_labels>\S+))?(, +Generation: +'
            r'(?P<generation>\S+))?(, +Route table: +'
            r'(?P<route_table>\S+))?$')

        # Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
        # Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1,
        p30 = re.compile(r'^Max +nh +cache: +(?P<max_local_cache>\d+), +New +hold +nh +limit: +(?P<new_hold_limit>\d+), Curr +nh +cnt: +(?P<intf_curr_cnt>\d+),( +Curr +new +hold +cnt: +(?P<intf_unresolved_cnt>\d+), +NH +drop +cnt: +(?P<intf_dropcnt>\d+))?$')

        # Curr new hold cnt: 0, NH drop cnt: 0
        p30_1 = re.compile(r'^Curr +new +hold +cnt: +(?P<intf_unresolved_cnt>\d+), +NH +drop +cnt: +(?P<intf_dropcnt>\d+)$')

        # Flags: No-Redirects, Sendbcast-pkt-to-re
        # Flags: Is-Primary, User-MTU
        # Flags: Up SNMP-Traps 0x4000 Encapsulation: ENET2
        p31 = re.compile(r'^Flags: +(?P<flags>[\S\s]+)')

        # Addresses, Flags: Is-Preferred Is-Primary
        p32 = re.compile(r'^Addresses, +Flags: +(?P<flags>[\S\s]+)$')

        # Addresses
        p32_1 = re.compile(r'^Addresses$')

        # Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95
        p33 = re.compile(r'^Destination: +(?P<ifa_destination>\S+), +Local: +(?P<ifa_local>\S+)(, +Broadcast: +(?P<ifa_broadcast>\S+))?(, +Generation: +(?P<generation>\S+))?$')

        # Broadcast: 10.0.0.255, Generation: 8336
        p33_1 = re.compile(r'^Broadcast: +(?P<ifa_broadcast>\S+), +Generation: +(?P<generation>\S+)$')

        # Bandwidth: 0
        p34 = re.compile(r'^Bandwidth: +(?P<logical_interface_bandwidth>\S+)$')

        # Local: fe80::250:560f:fc8d:7c08
        p35 = re.compile(r'^Local: +(?P<ifa_local>\S+)$')

        # IPv6 transit statistics:
        p36 = re.compile(r'^IPv6 +transit +statistics:$')

        # Dropped traffic statistics due to STP State:
        p37 = re.compile(r'^Dropped +traffic +statistics +due +to +'
            r'STP +State:$')

        # Transit statistics:
        p38 = re.compile(r'^Transit +statistics:$')

        # Hold-times     : Up 2000 ms, Down 0 ms
        p39 = re.compile(r'^Hold-times +: +Up +\d+ +ms, +Down +\d+ +ms$')

        # Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
        p40 = re.compile(r'^Damping +: +half-life: +\d+ +sec, +max-suppress: +'
            r'\d+ +sec, +reuse: +\d+, +suppress: +\d+, +state: +\S+$')

        # Input errors:
        p41 = re.compile(r'^Input +errors:$')

        # Output errors:
        p42 = re.compile(r'^Output +errors:$')

        # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,

        # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0, L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0

        # L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0

        # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0,
        # L3 incompletes: 0, L2 channel errors: 0, L2 mismatch timeouts: 0,
        # FIFO errors: 0, Resource errors: 0
        # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
        p43 = re.compile(r'^(Errors: +(?P<input_errors>\d+),)?'
                           r'( *Drops: +(?P<input_drops>\d+),)?'
                           r'( *Framing +errors: +(?P<framing_errors>\d+),)?'
                           r'( *Runts: +(?P<input_runts>\d+),)?'
                           r'( *Giants: +(?P<input_giants>\d+),)?'
                           r'( *Policed +discards: +(?P<input_discards>\d+),)?'
                           r'( *L3 +incompletes: +(?P<input_l3_incompletes>\d+),)?'
                           r'( *L2 +channel +errors: +(?P<input_l2_channel_errors>\d+),)?'
                           r'( *L2 +mismatch +timeouts: +(?P<input_l2_mismatch_timeouts>\d+),?)?'
                           r'( *FIFO +errors: +(?P<input_fifo_errors>\d+),?)?'
                           r'( *Resource +errors: +(?P<input_resource_errors>\d+))?$')

        # Carrier transitions: 1, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
        # Carrier transitions: 0, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0,
        # Carrier transitions: 0, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0, MTU errors: 0, Resource errors: 0
        p44_1 = re.compile(r'^Carrier +transitions: +(?P<carrier_transitions>\d+),'
                           r' +Errors: +(?P<output_errors>\d+),'
                           r' +Drops: +(?P<output_drops>\d+),'
                           r'( +Collisions: +(?P<output_collisions>\d+),)?'
                           r'( +Aged+ packets: +(?P<aged_packets>\d+),)?'
                           r'(( +FIFO +errors: +(?P<output_fifo_errors>\d+),)?'
                           r' +HS +link +CRC +errors: +(?P<hs_link_crc_errors>\d+),)?'
                           r'( +MTU +errors: +(?P<mtu_errors>\d+),?)?'
                           r'( +Resource +errors: +(?P<output_resource_errors>\d+))?$')

        # MTU errors: 0, Resource errors: 0
        p44_2 = re.compile(r'^MTU +errors: +(?P<mtu_errors>\d+), +Resource +'
            r'errors: +(?P<output_resource_errors>\d+)$')

        # FIFO errors: 0, HS link CRC errors: 0, MTU errors: 0, Resource errors: 0
        p44_3 = re.compile(r'^FIFO +errors: +(?P<output_fifo_errors>\d+), +'
                           r'(HS +link +CRC +errors: +(?P<hs_link_crc_errors>\d+),)?'
                           r'( +MTU +errors: +(?P<mtu_errors>\d+),?)?'
                           r'( +Resource +errors: +(?P<output_resource_errors>\d+))?')

        # Total octets                   21604601324      16828244544
        p45 = re.compile(r'^Total +octets +(?P<input_bytes>\d+) +'
            r'(?P<output_bytes>\d+)$')

        # MAC statistics:                      Receive         Transmit
        p45_1 = re.compile(r'^MAC +statistics: +Receive +Transmit$')

        # Total packets                    133726919        129183374
        p46 = re.compile(r'^Total +packets +(?P<input_packets>\d+) +'
            r'(?P<output_packets>\d+)')

        # Unicast packets                  133726908        129183361
        p47 = re.compile(r'^Unicast +packets +(?P<input_unicasts>\d+) +'
            r'(?P<output_unicasts>\d+)$')

        # Broadcast packets                        0                0
        p48 = re.compile(r'^Broadcast +packets +(?P<input_broadcasts>\d+) +'
            r'(?P<output_broadcasts>\d+)$')

        # Multicast packets                        0                0
        p49 = re.compile(r'^Multicast +packets +(?P<input_multicasts>\d+) +'
            r'(?P<output_multicasts>\d+)$')

        # CRC/Align errors                         0                0
        p50 = re.compile(r'^CRC\/Align +errors +(?P<input_crc_errors>\d+) +'
            r'(?P<output_crc_errors>\d+)$')

        # FIFO errors                              0                0
        p51 = re.compile(r'^FIFO +errors +(?P<input_fifo_errors>\d+) +'
            r'(?P<output_fifo_errors>\d+)$')

        # MAC control frames                       0                0
        p52 = re.compile(r'^MAC +control +frames +(?P<input_mac_control_frames>\d+) +'
            r'(?P<output_mac_control_frames>\d+)$')

        # MAC pause frames                         0                0
        p53 = re.compile(r'^MAC +pause +frames +(?P<input_mac_pause_frames>\d+) +'
            r'(?P<output_mac_pause_frames>\d+)$')

        # Oversized frames                         0
        p54 = re.compile(r'^Oversized +frames +(?P<input_oversized_frames>\d+)$')

        # Jabber frames                            0
        p56 = re.compile(r'^Jabber +frames +(?P<input_jabber_frames>\d+)$')

        # Fragment frames                          0
        p57 = re.compile(r'^Fragment +frames +(?P<input_fragment_frames>\d+)$')

        # VLAN tagged frames                       0
        p58 = re.compile(r'^VLAN +tagged +frames +(?P<input_vlan_tagged_frames>\d+)$')

        # Code violations                          0
        p59 = re.compile(r'^Code +violations +(?P<input_code_violations>\d+)$')

        # Total errors                             0                0
        p60 = re.compile(r'^Total +errors +(?P<input_total_errors>\d+) +(?P<output_total_errors>\d+)$')

        # Label-switched interface (LSI) traffic statistics:
        p61 = re.compile(r'^Label-switched +interface +\(LSI\) +traffic +statistics:$')

        # Ingress queues: 8 supported, 4 in use
        # Egress queues: 8 supported, 4 in use
        p62 = re.compile(r'^((?P<intf_cos_queue_type>(Ingress|Egress) +queues)): +(?P<intf_cos_num_queues_supported>\d+) +supported, +(?P<intf_cos_num_queues_in_use>\d+) +in +use$')

        # 0                                0                    0                    0
        p63 = re.compile(r'^(?P<queue_number>\d+) +(?P<queue_counters_queued_packets>\d+) +'
            r'(?P<queue_counters_trans_packets>\d+) +(?P<drop_packets>\d+)$')

        # Hold-times     : Up 0 ms, Down 0 ms
        p64 = re.compile(r'^Hold-times +: +Up +(?P<up_hold_time>\d+) +ms, +Down +(?P<down_hold_time>\d+) +ms$')

        # Statistics last cleared: 2020-10-14 13:18:51 EST (00:12:30 ago)
        p65 = re.compile(r'^Statistics +last +cleared: +(?P<statistics_cleared>[\S\s]+)$')

        # 0                   best-effort
        # 1                   expedited-forwarding
        # 2                   assured-forwarding
        # 3                   network-control
        p66 = re.compile(r'^(?P<queue_number>\d+) +(?P<forwarding_class_name>best-effort|expedited-forwarding|assured-forwarding|network-control)$')

        # Filter statistics:
        p67 = re.compile(r'^Filter +statistics:$')

        # Input packet count                   38089
        p68 = re.compile(r'^Input +packet +count +(?P<input_packets>\d+)$')

        # Input packet rejects                    24
        p69 = re.compile(r'^Input +packet +rejects +(?P<input_reject_count>\d+)$')

        # Input DA rejects                         0
        p70 = re.compile(r'^Input +DA +rejects +(?P<input_reject_da_count>\d+)$')

        # Input SA rejects                         0
        p71 = re.compile(r'^Input +SA +rejects +(?P<input_reject_sa_count>\d+)$')

        # Output packet count                                    8798
        p72 = re.compile(r'^Output +packet +count +(?P<output_packets>\d+)$')

        # Output packet pad count                                   0
        p73 = re.compile(r'^Output +packet +pad +count +(?P<output_packet_pad_count>\d+)$')

        # Output packet error count                                 0
        p74 = re.compile(r'^Output +packet +error +count +(?P<output_packet_error_count>\d+)$')

        # CAM destination filters: 0, CAM source filters: 0
        p75 = re.compile(r'^CAM +destination +filters: (?P<cam_destination_filter_count>\d+), +CAM +source +filters: (?P<cam_source_filter_count>\d+)$')

        # Destination slot: 0 (0x00)
        p76 = re.compile(r'^Destination +slot: +(?P<destination_slot>\d+) +(?P<destination_mask>\S+)$')

        # 0 best-effort            95     9500000000    95              0      low    none
        p77 = re.compile(r'^(?P<cos_queue_number>\d+) +(?P<cos_queue_forwarding_class>\S+) +(?P<cos_queue_bandwidth>\d+) +(?P<cos_queue_bandwidth_bps>\d+) +(?P<cos_queue_buffer>\d+) +(?P<cos_queue_buffer_bytes>\d+) +(?P<cos_queue_priority>\w+) +(?P<cos_queue_limit>\w+)$')

        # Direction : Output
        p78 = re.compile(r'^Direction : +(?P<cos_direction>\S+)$')

        # Generation: 9549, Route table: 0
        p79 = re.compile(r'^Generation: +(?P<generation>\d+)(, +Route +table: +(?P<route_table>\d+))?$')

        # Policer: Input: GE_1M-xe-0/1/7.0-log_int-i, Output: GE_1M-xe-0/1/7.0-log_int-o
        p80 = re.compile(r'^Policer: +Input: +(?P<policer_input>\S+)(, +Output: +(?P<policer_output>\S+))?$')

        # Bundle:
        # Link:
        p81 = re.compile(r'^(?P<lag_int_type>(Bundle)|(Link)):$')

        # xe-0/1/10.0
        # xe-0/1/10
        p81_1 = re.compile(r'^(?P<name>[a-z]{2}-\d+/\d+/\d+(\.\d+)?)$')

        # Input :           225          0         14514         1952
        # Output:            16          0          1188            0
        p82 = re.compile(r'^(?P<in_out>(Input\s*)|(Output)):\s+(?P<packets>\d+)\s+(?P<pps>\d+)\s+(?P<bytes>\d+)\s+(?P<bps>\d+)$')

        # Adaptive Adjusts:          0
        # Adaptive Scans  :          0
        # Adaptive Updates:          0
        p83 = re.compile(r'^(?P<adaptive>Adaptive\s+(Adjusts|Scans|Updates))\s*:\s+(?P<adaptive_value>\d+)$')

        # Aggregate member links: 2
        p84 = re.compile(r'^Aggregate\s+member\s+links:\s+(?P<aggregate_member_count>\d+)$')

        # LACP info:        Role     System             System       Port     Port    Port
        # LACP Statistics:       LACP Rx     LACP Tx   Unknown Rx   Illegal Rx
        # Marker Statistics:   Marker Rx     Resp Tx   Unknown Rx   Illegal Rx
        p85 = re.compile(r'^(?P<lacp_flag>(LACP info)|(LACP Statistics)|(Marker Statistics)):\s+.+$')

        # ge-0/0/6.0     Actor        127  2c:6b:f5:ff:cf:97        127        2       1
        # ge-0/0/6.0   Partner        127  2c:6b:f5:ff:08:d8        127        2       1
        p86 = re.compile(r'^(?P<name>\S+)\s+(?P<lacp_role>\S+)\s+(?P<lacp_sys_priority>\d+)\s+(?P<lacp_system_id>\S+)\s+(?P<lacp_port_priority>\d+)\s+(?P<lacp_port_number>\d+)\s+(?P<lacp_port_key>\d+)$')

        # For LACP Statistics
        # ge-0/0/6.0                 0           0            0            0
        p87 = re.compile(r'(?P<name>\S+)\s+(?P<lacp_rx_packets>\d+)\s+(?P<lacp_tx_packets>\d+)\s+(?P<unknown_rx_packets>\d+)\s+(?P<illegal_rx_packets>\d+)$')

        # For Marker Statistics
        # ge-0/0/6.0                 0           0            0            0
        p88 = re.compile(r'(?P<name>\S+)\s+(?P<marker_rx_packets>\d+)\s+(?P<marker_response_tx_packets>\d+)\s+(?P<unknown_rx_packets>\d+)\s+(?P<illegal_rx_packets>\d+)$')

        # Primary         Active
        # Backup          Down
        # Standby         Down
        p89 = re.compile(r'^(?P<list_type>(Primary)|(Backup)|(Standby))\s+(?P<list_status>(Active)|(Down))$')

        # ge-0/0/7        Up
        p90 = re.compile(r'^(?P<if_child_name>\S+)\s+(?P<if_status>(Up)|(Down))$')

        cnt = 0
        queue_name = ''
        lag_int_type = ''
        lacp_flag = ''
        if_dist_dict = {}
        for line in out.splitlines():
            line = line.strip()
            if not line:
               continue
            cnt += 1

            # Physical interface: ge-0/0/0, Enabled, Physical link is Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                statistics_type = 'physical'
                interface_info_dict = ret_dict.setdefault('interface-information', {})
                physical_interface_list =  interface_info_dict.setdefault('physical-interface', [])
                physical_interface_dict = {}
                physical_interface_dict.update({'name': group['name']})
                physical_interface_dict.update({'oper-status': group['oper_status']})
                admin_status = group['admin_status']
                admin_status_dict = physical_interface_dict.setdefault('admin-status', {})
                admin_status_dict.update({'@junos:format': admin_status})
                physical_interface_list.append(physical_interface_dict)
                continue

            # Interface index: 148, SNMP ifIndex: 526
            m = p2.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Description: none/100G/in/hktGCS002_ge-0/0/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    physical_interface_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                elif statistics_type == 'logical':
                    logical_interface_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            m = p4.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Speed: 1000mbps, BPDU Error: None, Loop Detect PDU Error: None,
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None, Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None,
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            m = p5.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            # BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Loopback: Disabled, Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            m = p5_2.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            m = p6.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Pad to minimum frame size: Disabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Minimum links needed: 1, Minimum bandwidth needed: 1bps
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Device flags   : Present Running
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if_device_flags = group['if_device_flags']
                if_device_flags_dict = physical_interface_dict.setdefault('if-device-flags', {})
                for flag in if_device_flags.split(' '):
                    key = 'ifdf-{}'.format(flag.lower())
                    if_device_flags_dict.update({key: True})
                continue

            # Interface flags: SNMP-Traps Internal: 0x4000
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if_config_flags_dict = physical_interface_dict.setdefault('if-config-flags', {})
                if_config_flags_dict.update({'iff-snmp-traps': True})
                if group['hardware_down']:
                    if_config_flags_dict.update({'iff-hardware-down': True})
                if group['internal_flags']:
                    if_config_flags_dict.update({'internal-flags': group['internal_flags']})
                continue

            # Link flags     : None
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if_media_flags = group['if_media_flags']
                if_media_flags_dict = physical_interface_dict.setdefault('if-media-flags', {})
                for flag in if_media_flags.split(' '):
                    key = 'ifmf-{}'.format(flag.lower())
                    if_media_flags_dict.update({key: True})
                continue
            
            # Link type      : Full-Duplex
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # CoS queues     : 8 supported, 8 maximum usable queues
            m = p11.match(line)
            if m:
                group = m.groupdict()
                cos_dict = physical_interface_dict.setdefault('physical-interface-cos-information', {})
                cos_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Current address: 00:50:56:ff:56:b6, Hardware address: 00:50:56:ff:56:b6
            m = p12.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                intf_flapped_dict = physical_interface_dict.setdefault('interface-flapped', {})
                intf_flapped_dict.update({'#text': group['interface_flapped']})
                continue
            
            # IPv6 transit statistics:
            m = p36.match(line)
            if m:
                group = m.groupdict()
                traffic_statistics_dict = traffic_statistics_dict.setdefault('ipv6-transit-statistics', {})
                statistics_type = 'ipv6_transit'
                continue
            
            # Dropped traffic statistics due to STP State:
            m = p37.match(line)
            if m:
                statistics_type = 'dropped_stp_state'
                group = m.groupdict()
                traffic_statistics_dict = physical_interface_dict.setdefault('stp-traffic-statistics', {})
                continue

            # Transit statistics:
            m = p38.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('transit-traffic-statistics', {})
                else:
                    traffic_statistics_dict = logical_interface_dict.setdefault('transit-traffic-statistics', {})
                statistics_type = 'transit_statistics'
                continue

            # Input rate     : 2952 bps (5 pps)
            m = p14.match(line)
            if m:
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                group = m.groupdict()
                traffic_statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Input  bytes  :          19732539397                 3152 bps
            m = p14_1.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                if statistics_type == 'dropped_stp_state':
                    traffic_statistics_dict.update({'stp-{}-dropped'.format(k.replace('_','-')):
                        v for k, v in group.items() if v is not None})
                else:
                    traffic_statistics_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue
            # Output bytes  :          16367814635                 3160 bps
            m = p14_2.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                if statistics_type == 'dropped_stp_state':
                    traffic_statistics_dict.update({'stp-{}-dropped'.format(k.replace('_','-')):
                        v for k, v in group.items() if v is not None})
                else:
                    traffic_statistics_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue
            # Input  packets:            133726363                    5 pps
            m = p14_3.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                if statistics_type == 'dropped_stp_state':
                    traffic_statistics_dict.update({'stp-{}-dropped'.format(k.replace('_','-')):
                        v for k, v in group.items() if v is not None})
                else:
                    traffic_statistics_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue
            # Output packets:            129306863                    4 pps
            m = p14_4.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                if statistics_type == 'dropped_stp_state':
                    traffic_statistics_dict.update({'stp-{}-dropped'.format(k.replace('_','-')):
                        v for k, v in group.items() if v is not None})
                else:
                    traffic_statistics_dict.update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue
            
            # Output rate    : 3080 bps (3 pps)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                if statistics_type == 'physical':
                    traffic_statistics_dict = physical_interface_dict.setdefault('traffic-statistics', {})
                elif statistics_type == 'logical':
                    traffic_statistics_dict = logical_interface_dict.setdefault('traffic-statistics', {})
                traffic_statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Active alarms  : None
            m = p16.match(line)
            if m:
                group = m.groupdict()
                active_alarms = group['active_alarms']
                active_alarms_dict = physical_interface_dict.setdefault('active-alarms', {})
                if active_alarms == 'None':
                    active_alarms_dict.setdefault('interface-alarms', {}). \
                        setdefault('alarm-not-present', True)
                else:
                    active_alarms_dict.setdefault('interface-alarms', {}). \
                        setdefault('ethernet-alarm-link-down', True)
                continue

            # Active defects : None
            m = p17.match(line)
            if m:
                group = m.groupdict()
                active_defects = group['active_defects']
                active_defects_dict = physical_interface_dict.setdefault('active-defects', {})
                if active_defects == 'None':
                    active_defects_dict.setdefault('interface-alarms', {}). \
                        setdefault('alarm-not-present', True)
                else:
                    active_defects_dict.setdefault('interface-alarms', {}). \
                        setdefault('ethernet-alarm-link-down', True)
                continue
            
            # PCS statistics                      Seconds
            m = p18.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = physical_interface_dict.setdefault('ethernet-pcs-statistics', {})
                continue

            # Bit errors                             0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Errored blocks                         0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Ethernet FEC statistics              Errors
            m = p21.match(line)
            if m:
                statistics_dict = physical_interface_dict.setdefault('ethernet-fec-statistics', {})
                continue

            # FEC Corrected Errors                    0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k:
                    v for k, v in group.items() if v is not None})
                continue

            # FEC Uncorrected Errors                  0
            m = p22_1.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k:
                    v for k, v in group.items() if v is not None})
                continue

            # FEC Corrected Errors Rate               0
            m = p22_2.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k:
                    v for k, v in group.items() if v is not None})
                continue

            # FEC Uncorrected Errors Rate             0
            m = p22_3.match(line)
            if m:
                group = m.groupdict()
                statistics_dict.update({k:
                    v for k, v in group.items() if v is not None})
                continue

            # Interface transmit statistics: Disabled
            m = p23.match(line)
            if m:
                group = m.groupdict()
                inft_transmit = group['interface_transmit_statistics']
                physical_interface_dict.update({'interface-transmit-statistics': inft_transmit})
                continue

            # Logical interface ge-0/0/0.0 (Index 333) (SNMP ifIndex 606)
            m = p24.match(line)
            if m:
                # found_flag : To check if `physical-interface` list created
                #              for logical-interface
                #              This prevents to create redundant list for same physical interface
                found_flag = False
                statistics_type = 'logical'
                group = m.groupdict()
                phy_interface = '.'.join(group['name'].split('.')[:-1])
                logical_interface_dict = {}
                interface_info_dict = ret_dict.setdefault('interface-information', {})
                physical_interface_list =  interface_info_dict.setdefault('physical-interface', [])
                for phy_dict in physical_interface_list:
                    if phy_dict['name'] == phy_interface:
                        found_flag = True

                if not found_flag:
                    physical_interface_dict = {}
                    physical_interface_dict.update({'name': phy_interface})
                    physical_interface_list.append(physical_interface_dict)

                logical_interface_list = physical_interface_dict.setdefault('logical-interface', [])
                logical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                logical_interface_list.append(logical_interface_dict)
                found_flag = False
                continue

            # Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            m = p25.match(line)
            if m:
                group = m.groupdict()
                if_config_flags_dict = logical_interface_dict.setdefault('if-config-flags', {})
                if_config_flags_dict.update({'iff-up': True})
                if_config_flags_dict.update({'iff-snmp-traps': True})
                if group['internal_flags']:
                    if_config_flags_dict.update({'internal-flags': group['internal_flags']})
                    logical_interface_dict.update({'encapsulation': group['encapsulation']})
                continue

            # Input packets : 133657033
            m = p26.match(line)
            if m:
                group = m.groupdict()
                traffic_statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Output packets: 129243982
            m = p27.match(line)
            if m:
                group = m.groupdict()
                traffic_statistics_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Protocol inet, MTU: 1500
            # Protocol mpls, MTU: 1488, Maximum labels: 3
            m = p28.match(line)
            if m:
                group = m.groupdict()
                address_family_list = logical_interface_dict.setdefault('address-family', [])
                address_family_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                continue

            # Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                address_family_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Curr new hold cnt: 0, NH drop cnt: 0
            m = p30_1.match(line)
            if m:
                group = m.groupdict()
                address_family_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Flags: No-Redirects, Sendbcast-pkt-to-re
            # Flags: Is-Primary, User-MTU
            m = p31.match(line)
            if m:
                group = m.groupdict()
                address_family_flags_dict = address_family_dict.setdefault('address-family-flags', {})
                for flag in group['flags'].split(','):
                    if "encapsulation" in flag.lower():
                        value = flag.split(":")[-1].strip().lower()
                        address_family_flags_dict.update({"ifff-encapsulation": value})
                    else:
                        key = 'ifff-{}'.format(flag.strip().lower())
                        address_family_flags_dict.update({key: True})
                continue

            # Addresses, Flags: Is-Preferred Is-Primary
            m = p32.match(line)
            if m:
                group = m.groupdict()
                af_check = address_family_dict.get('interface-address', None)
                interface_address_dict = {}
                ifa_flags_dict = interface_address_dict.setdefault('ifa-flags', {})
                # ifa_flags_dict.update({'ifaf-current-preferred': True})
                # ifa_flags_dict.update({'ifaf-current-primary': True})
                for flag in group['flags'].split(' '):
                    key = 'ifaf-{}'.format(flag.lower())
                    ifa_flags_dict.update({key: True})
                if af_check:
                    if isinstance(af_check, dict):
                        address_family_dict.update({'interface-address': []})
                        interface_address_list = address_family_dict['interface-address']
                        interface_address_list.append(af_check)
                        interface_address_list.append(interface_address_dict)
                    else:
                        interface_address_list.append(interface_address_dict)
                else:
                    address_family_dict.setdefault('interface-address', interface_address_dict)
                continue

            # Addresses
            m = p32_1.match(line)
            if m:
                group = m.groupdict()
                interface_address_dict = {}
                interface_address_list = address_family_dict.setdefault('interface-address', [])
                interface_address_list.append(interface_address_dict)
                address_family_dict.setdefault('interface-address', interface_address_dict)


            # Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95
            m = p33.match(line)
            if m:
                group = m.groupdict()
                interface_address_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Broadcast: 10.0.0.255, Generation: 8336
            m = p33_1.match(line)
            if m:
                group = m.groupdict()
                interface_address_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Bandwidth: 0
            m = p34.match(line)
            if m:
                group = m.groupdict()
                logical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Local: fe80::250:560f:fc8d:7c08
            m = p35.match(line)
            if m:
                group = m.groupdict()

                interface_address_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Input errors:
            m = p41.match(line)
            if m:
                input_error_list_dict = physical_interface_dict.setdefault('input-error-list', {})
                continue

            # Output errors:
            m = p42.match(line)
            if m:
                output_error_list_dict = physical_interface_dict.setdefault('output-error-list', {})
                continue

            # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,

            # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0, L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0

            # L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0

            # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0,
            # L3 incompletes: 0, L2 channel errors: 0, L2 mismatch timeouts: 0,
            # FIFO errors: 0, Resource errors: 0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                input_error_list_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Carrier transitions: 1, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
            m = p44_1.match(line)
            if m:
                group = m.groupdict()
                output_error_list_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # MTU errors: 0, Resource errors: 0
            m = p44_2.match(line)
            if m:
                group = m.groupdict()
                output_error_list_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # FIFO errors: 0, HS link CRC errors: 0, MTU errors: 0, Resource errors: 0
            m = p44_3.match(line)
            if m:
                group = m.groupdict()
                output_error_list_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Total octets                   21604601324      16828244544
            m = p45.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p45_1.match(line)
            if m:
                ethernet_mac_statistics = physical_interface_dict.setdefault('ethernet-mac-statistics', {})
                continue

            # Total packets                    133726919        129183374
            m = p46.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Unicast packets                  133726908        129183361
            m = p47.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Broadcast packets                        0                0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Multicast packets                        0                0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # CRC/Align errors                         0                0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # FIFO errors                              0                0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # MAC control frames                       0                0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # MAC pause frames                         0                0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Oversized frames                         0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Jabber frames                            0
            m = p56.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Fragment frames                          0
            m = p57.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # VLAN tagged frames                       0
            m = p58.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Code violations                          0
            m = p59.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Total errors                             0                0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                ethernet_mac_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Label-switched interface (LSI) traffic statistics:
            m = p61.match(line)
            if m:
                statistics_type = 'lsi_traffic_statistics'
                traffic_statistics_dict = physical_interface_dict.setdefault('lsi-traffic-statistics', {})
                continue

            # Ingress queues: 8 supported, 4 in use
            # Egress queues: 8 supported, 4 in use
            m = p62.match(line)
            if m:
                group = m.groupdict()
                queue_name = group['intf_cos_queue_type']
                if queue_name == 'Egress queues':
                    cos_short_summary_dict = physical_interface_dict.setdefault('queue-counters', {}).setdefault('interface-cos-short-summary', {})
                elif queue_name == 'Ingress queues':
                    cos_short_summary_dict = physical_interface_dict.setdefault('ingress-queue-counters', {}).setdefault('interface-cos-short-summary', {})

                cos_short_summary_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # 0                                0                    0                    0
            m = p63.match(line)
            if m and queue_name:
                group = m.groupdict()
                if queue_name == 'Egress queues':
                    queue_list = physical_interface_dict.setdefault('queue-counters', {}).setdefault('queue', [])
                elif queue_name == 'Ingress queues':
                    queue_list = physical_interface_dict.setdefault('ingress-queue-counters', {}).setdefault('queue', [])                    
                queue_dict = {}
                queue_dict.update({'queue-number': group['queue_number']})
                queue_dict.update({'queue-counters-queued-packets': group['queue_counters_queued_packets']})
                queue_dict.update({'queue-counters-trans-packets': group['queue_counters_trans_packets']})
                queue_dict.update({'queue-counters-total-drop-packets': group['drop_packets']})
                queue_list.append(queue_dict)
                continue
            
            # Hold-times     : Up 0 ms, Down 0 ms
            m = p64.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Statistics last cleared: 2020-10-14 13:18:51 EST (00:12:30 ago)
            m = p65.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # 0                   best-effort
            # 1                   expedited-forwarding
            # 2                   assured-forwarding
            # 3                   network-control
            m = p66.match(line)
            if m:
                group = m.groupdict()
                queue_number = int(group.pop('queue_number', 0))
                if 'queue-counters' in physical_interface_dict:
                    queue_list = physical_interface_dict.setdefault('queue-counters', {}).setdefault('queue', [])
                    queue_list[queue_number].update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                if 'ingress-queue-counters' in physical_interface_dict:
                    queue_list = physical_interface_dict.setdefault('ingress-queue-counters', {}).setdefault('queue', [])
                    queue_list[queue_number].update({k.replace('_','-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Filter statistics:
            m = p67.match(line)
            if m:
                ethernet_filter_statistics = physical_interface_dict.setdefault('ethernet-filter-statistics', {})
                continue

            # Input packet count                   38089
            m = p68.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Input packet rejects                    24
            m = p69.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Input DA rejects                         0
            m = p70.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update(
                    {'input-reject-destination-address-count': group['input_reject_da_count']})
                #     v for k, v in group.items() if v is not None})
                continue

            # Input SA rejects                         0
            m = p71.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update(
                    {'input-reject-source-address-count': group['input_reject_sa_count']})
                continue

            # Output packet count                                    8798
            m = p72.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Output packet pad count                                   0
            m = p73.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Output packet error count                                 0
            m = p74.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            m = p75.match(line)
            if m:
                group = m.groupdict()
                ethernet_filter_statistics.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p76.match(line)
            if m:
                group = m.groupdict()
                pfe_information = physical_interface_dict.setdefault('pfe-information', {})
                pfe_information.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # 0 best-effort            95     9500000000    95              0      low    none
            m = p77.match(line)
            if m:
                group = m.groupdict()
                pfe_information = physical_interface_dict.setdefault('pfe-information', {})
                cos_stream_information_dict = physical_interface_dict.setdefault("cos-information", {}). \
                    setdefault("cos-stream-information", {})

                cos_queue_configuration_list = cos_stream_information_dict.setdefault('cos-queue-configuration', [])
                cos_queue_configuration_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                cos_queue_configuration_list.append(cos_queue_configuration_dict)
                continue
            
            # Direction : Output
            m = p78.match(line)
            if m:
                group = m.groupdict()
                pfe_information = physical_interface_dict.setdefault('pfe-information', {})
                cos_stream_information_dict = physical_interface_dict.setdefault("cos-information", {}). \
                    setdefault("cos-stream-information", {})
                cos_stream_information_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Generation: 9549, Route table: 0
            m = p79.match(line)
            if m:
                group = m.groupdict()
                address_family_list = logical_interface_dict.setdefault('address-family', [])
                address_family_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                address_family_list.append(address_family_dict)
                continue
            
            # Direction : Output
            m = p80.match(line)
            if m:
                group = m.groupdict()
                policer_information_dict = address_family_dict.setdefault('policer-information', {})
                policer_information_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                continue
            
            # Bundle:
            # Link:
            m = p81.match(line)
            if m:
                in_out_dict = {}
                group = m.groupdict()
                lag_traffic_dict = logical_interface_dict.setdefault('lag-traffic-statistics', {})
                lag_int_type = group['lag_int_type']
                continue

            # xe-0/1/10.0
            # xe-0/1/10
            p81_1 = re.compile(r'^(?P<name>[a-z]{2}-\d+/\d+/\d+(\.\d+)?)$')
            m = p81_1.match(line)
            if m and lag_int_type == 'Link':
                in_out_dict = {}
                group = m.groupdict()
                lag_link_name = group['name']

            # Input :           225          0         14514         1952
            # Output:            16          0          1188            0
            m = p82.match(line)
            if m:
                group = m.groupdict()
                in_out_direction = group.pop('in_out').rstrip().lower()
                in_out_dict.update({"{iod}-{k}".format(iod=in_out_direction, k=k):
                    v for k, v in group.items() if v is not None})
                if 'Bundle' == lag_int_type:
                    lag_traffic_dict.setdefault('lag-bundle', {})
                    lag_traffic_dict['lag-bundle'].update(in_out_dict)
                elif 'Link' == lag_int_type:
                    lag_traffic_dict.setdefault('lag-link', [])
                    if in_out_direction == 'output':
                        in_out_dict.update({'name': lag_link_name})
                        lag_traffic_dict['lag-link'].append(in_out_dict)
                continue

            # Adaptive Adjusts:          0
            # Adaptive Scans  :          0
            # Adaptive Updates:          0
            m = p83.match(line)
            if m:
                group = m.groupdict()
                lag_traffic_dict.setdefault('lag-adaptive-statistics', {}).setdefault(group['adaptive'].lower().replace(' ', '-'), group['adaptive_value'])
                continue

            # Aggregate member links: 2
            m = p84.match(line)
            if m:
                group = m.groupdict()
                lag_traffic_dict.setdefault('aggregate-member-info', {})
                lag_traffic_dict['aggregate-member-info'] = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                continue

            # LACP info:        Role     System             System       Port     Port    Port
            # LACP Statistics:       LACP Rx     LACP Tx   Unknown Rx   Illegal Rx
            # Marker Statistics:   Marker Rx     Resp Tx   Unknown Rx   Illegal Rx
            m = p85.match(line)
            if m:
                lacp_flag = m.groupdict()['lacp_flag']
                continue

            # ge-0/0/6.0     Actor        127  2c:6b:f5:ff:cf:97        127        2       1
            # ge-0/0/6.0   Partner        127  2c:6b:f5:ff:08:d8        127        2       1
            m = p86.match(line)
            if m and lacp_flag == 'LACP info':
                group = m.groupdict()
                lag_link_name = group.pop('name')
                lag_traffic_dict.setdefault('lag-lacp-info', [])
                lag_lacp_info_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                lag_lacp_info_dict['name'] = lag_link_name
                lag_traffic_dict['lag-lacp-info'].append(lag_lacp_info_dict)
                continue

            # For LACP Statistics
            # ge-0/0/6.0                 0           0            0            0
            m = p87.match(line)
            if m and lacp_flag == 'LACP Statistics':
                group = m.groupdict()
                lag_link_name = group.pop('name')
                lag_traffic_dict.setdefault('lag-lacp-statistics', [])
                lag_traffic_dict['lag-lacp-statistics'].append({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # For Maker Statistics
            # ge-0/0/6.0                 0           0            0            0
            m = p88.match(line)
            if m and lacp_flag == 'Marker Statistics':
                group = m.groupdict()
                lag_link_name = group.pop('name')
                lag_traffic_dict.setdefault('lag-marker', [])
                lag_traffic_dict['lag-marker'].append({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Primary         Active
            # Backup          Down
            # Standby         Down
            # p89 = re.compile(r'^(?P<list_type>(Primary)|(Backup)|(Standby))\s+(?P<list_status>(Active)|(Down))$')
            m = p89.match(line)
            if m:
                group = m.groupdict()
                lag_traffic_dict.setdefault('if-distribution-list-information', [])
                if_dist_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                lag_traffic_dict['if-distribution-list-information'].append(if_dist_dict)
                continue

            # ge-0/0/7        Up
            # p90 = re.compile(r'^(?P<if_child_name>\S+)\s+(?P<if_status>(Up)|(Down))$')
            m = p90.match(line)
            if m and if_dist_dict:
                group = m.groupdict()
                lag_traffic_dict['if-distribution-list-information'][-1].setdefault('if-list', [])
                if_list_dict = {k.replace('_','-'):
                    v for k, v in group.items() if v is not None}
                lag_traffic_dict['if-distribution-list-information'][-1]['if-list'].append(if_list_dict)
                continue

        return ret_dict

class ShowInterfacesExtensive(ShowInterfaces):
    cli_command = ['show interfaces extensive',
        'show interfaces {interface} extensive']
    def cli(self, interface=None, output=None):

        if not output:
            if interface:
                out = self.device.execute(self.cli_command[1].format(
                    interface=interface
                ))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        return super().cli(output=out)

class ShowInterfacesExtensiveNoForwarding(ShowInterfacesExtensive):
    cli_command = ['show interfaces extensive no-forwarding']
    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        return super().cli(output=out)


class ShowInterfacesStatisticsSchema(MetaParser):
    """ Schema for:
            * show interfaces statistics
            * show interfaces statistics {interface}
    """

    schema = {
        "interface-information": {
            "physical-interface": ListOf({
                "name": str,
                "admin-status": str,
                "oper-status": str,
                "local-index": str,
                "snmp-index": str,
                Optional("link-level-type"): str,
                Optional("mtu"): str,
                Optional("source-filtering"): str,
                Optional("link-mode"): str,
                Optional("speed"): str,
                Optional("bpdu-error"): str,
                Optional("l2pt-error"): str,
                Optional("loopback"): str,
                Optional("if-flow-control"): str,
                Optional("if-auto-negotiation"): str,
                Optional("if-remote-fault"): str,
                Optional("if-device-flags"): {
                    Optional("ifdf-present"): bool,
                    Optional("ifdf-running"): bool,
                    Optional("ifdf-none"): bool,
                },
                Optional("if-config-flags"): {
                    Optional("iff-snmp-traps"): bool,
                    Optional("internal-flags"): str,
                },
                Optional("if-media-flags"): {
                    Optional("ifmf-none"): bool,
                },
                Optional("physical-interface-cos-information"): {
                    "physical-interface-cos-hw-max-queues": str,
                    "physical-interface-cos-use-max-queues": str,
                },
                Optional("current-physical-address"): str,
                Optional("hardware-physical-address"): str,
                Optional("interface-flapped"): str,
                Optional("statistics-cleared"): str,
                Optional("stp-traffic-statistics"): {
                    "stp-input-bytes-dropped": str,
                    "stp-input-packets-dropped": str,
                    "stp-output-bytes-dropped": str,
                    "stp-output-packets-dropped": str
                },
                Optional("traffic-statistics"): {
                    "input-bps": str,
                    "input-pps": str,
                    "output-bps": str,
                    "output-pps": str
                },
                Optional("input-error-count"): str,
                Optional("output-error-count"): str,
                Optional("active-alarms"): {
                    "interface-alarms": {
                        Optional("alarm-not-present"): bool,
                    },
                },
                Optional("active-defects"): {
                    "interface-alarms": {
                        Optional("alarm-not-present"): bool,
                    },
                },
                Optional("interface-transmit-statistics"): str,
                Optional("logical-interface"): ListOf({
                    "name": str,
                    Optional("local-index"): str,
                    Optional("snmp-index"): str,
                    Optional("if-config-flags"): {
                        "iff-snmp-traps": bool,
                        "internal-flags": str,
                    },
                    Optional("encapsulation"): str,
                    "traffic-statistics": {
                        "input-packets": str,
                        "output-packets": str,
                    },
                    Optional("filter-information"): str,
                    Optional("logical-interface-zone-name"): str,
                    Optional("allowed-host-inbound-traffic"): {
                        Optional("inbound-dhcp"): bool,
                        Optional("inbound-http"): bool,
                        Optional("inbound-https"): bool,
                        Optional("inbound-ssh"): bool,
                        Optional("inbound-telnet"): bool,
                    },
                    Optional("address-family"): ListOf({
                        "address-family-name": str,
                        "mtu": str,
                        Optional("address-family-flags"): {
                            Optional("ifff-is-primary"): bool,
                            Optional("ifff-sendbcast-pkt-to-re"): bool,
                        },
                        Optional("interface-address"): ListOf({
                            "ifa-flags": {
                                Optional("ifaf-current-preferred"): bool,
                                Optional("ifaf-current-primary"): bool,
                                Optional("ifaf-current-default"): bool,
                            },
                            Optional("ifa-destination"): str,
                            Optional("ifa-local"): str,
                            Optional("ifa-broadcast"): str,
                        }),
                    }),
                })
            })
        }
    }


class ShowInterfacesStatistics(ShowInterfacesStatisticsSchema):
    """ Parser for:
            * show interfaces statistics
            * show interfaces statistics {interface}
    """

    cli_command = [
        "show interfaces statistics",
        "show interfaces statistics {interface}"
    ]

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(
                    interface=interface
                ))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Physical interface: ge-0/0/0, Enabled, Physical link is Up
        p1 = re.compile(r'^Physical +interface: +(?P<name>[^\s,]+), +'
                        r'(?P<admin_status>[^\s,]+), +Physical +link +is +'
                        r'(?P<oper_status>\S+)$')

        # Interface index: 133, SNMP ifIndex: 506
        p2 = re.compile(r'^Interface +index: +(?P<local_index>\d+), +'
                        r'SNMP +ifIndex: +(?P<snmp_index>\d+)$')

        # Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        p3 = re.compile(r'^Link-level +type: +(?P<link_level_type>[^\s,]+), +'
                        r'MTU: +(?P<mtu>\d+), +Link-mode: +(?P<link_mode>[^\s,]+), +'
                        r'Speed: +(?P<speed>[^\s,]+),$')

        # BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        p4 = re.compile(r'^BPDU +Error: +(?P<bpdu_error>[^\s,]+), +'
                        r'MAC-REWRITE +Error: +(?P<l2pt_error>[^\s,]+), +'
                        r'Loopback: +(?P<loopback>[^\s,]+),$')

        # Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        p5 = re.compile(r'^Source +filtering: +(?P<source_filtering>[^\s,]+), +'
                        r'Flow +control: +(?P<if_flow_control>[^\s,]+), +'
                        r'Auto-negotiation: +(?P<if_auto_negotiation>[^\s,]+),$')

        # Remote fault: Online
        p6 = re.compile(r'^Remote +fault: +(?P<if_remote_fault>[^\s,]+)$')

        # Device flags   : Present Running
        p7 = re.compile(r'^Device +flags *: +((?P<ifdf_none>None+) *)?'
                        r'((?P<ifdf_present>Present+) *)?'
                        r'((?P<ifdf_running>Running+) *)?$')

        # Interface flags: SNMP-Traps Internal: 0x4000
        p8 = re.compile(r'^Interface +flags: +(?P<iff_snmp_traps>\S+) +'
                        r'Internal: +(?P<internal_flags>\S+)$')

        # Link flags     : None
        p9 = re.compile(r'^Link +flags *: +((?P<ifmf_none>None) *)?$')

        # CoS queues     : 8 supported, 8 maximum usable queues
        p10 = re.compile(r'^CoS +queues *: +(?P<physical_interface_cos_hw_max_queues>\d+) +'
                         r'supported, +(?P<physical_interface_cos_use_max_queues>\d+) +'
                         r'maximum +usable +queues$')

        # Current address: 5e:00:40:ff:00:00, Hardware address: 5e:00:40:ff:00:00
        p11 = re.compile(r'^Current +address: +(?P<current_physical_address>[^\s,]+), +'
                         r'Hardware +address: +(?P<hardware_physical_address>[^\s,]+)$')

        # Last flapped   : 2020-06-22 22:33:51 EST (4d 06:59 ago)
        p12 = re.compile(r'^Last +flapped *: +(?P<interface_flapped>.*)$')

        # Statistics last cleared: 2020-06-27 05:22:04 EST (00:11:36 ago)
        p13 = re.compile(r'^Statistics last cleared: +(?P<statistics_cleared>.*)$')

        # Input rate     : 2144 bps (4 pps)
        p14 = re.compile(r'^Input rate *: +(?P<input_bps>\d+) +bps +'
                         r'\((?P<input_pps>\d+) +pps\)$')

        # Output rate    : 0 bps (0 pps)
        p15 = re.compile(r'^Output rate *: +(?P<output_bps>\d+) +bps +'
                         r'\((?P<output_pps>\d+) +pps\)$')

        # Input errors: 552, Output errors: 0
        p16 = re.compile(r'^Input errors: +(?P<input_error_count>\d+), +'
                         r'Output errors: +(?P<output_error_count>\d+)$')

        # Active alarms  : None
        p17 = re.compile(r'^Active +alarms *: +(?P<alarm_not_present>None)?$')

        # Active defects : None
        p18 = re.compile(r'^Active +defects *: +(?P<alarm_not_present>None)?$')

        # Interface transmit statistics: Disabled
        p19 = re.compile(r'^Interface +transmit +statistics: +'
                         r'(?P<interface_transmit_statistics>\S+)$')

        # Logical interface ge-0/0/0.0 (Index 70) (SNMP ifIndex 507)
        p20 = re.compile(r'^Logical +interface +(?P<name>\S+) +'
                         r'\(Index +(?P<local_index>\d+)\) +'
                         r'\(SNMP +ifIndex +(?P<snmp_index>\d+)\)$')

        # Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
        p21 = re.compile(r'^Flags: +(?P<iff_snmp_traps>SNMP-Traps) +'
                         r'(?P<internal_flags>\S+) +Encapsulation: +'
                         r'(?P<encapsulation>\S+)$')

        # Input packets : 1684
        p22 = re.compile(r'^Input +packets *: +(?P<input_packets>\d+)$')

        # Output packets: 49
        p23 = re.compile(r'^Output +packets *: +(?P<output_packets>\d+)$')

        # Security: Zone: trust
        p24 = re.compile(r'^Security: +Zone: (?P<logical_interface_zone_name>\S+)$')

        # Allowed host-inbound traffic : dhcp http https ssh telnet
        p25 = re.compile(r'^Allowed +host-inbound +traffic *: +'
                         r'(?P<inbound_dhcp>dhcp)( +)?(?P<inbound_http>http)( +)?'
                         r'(?P<inbound_https>https)( +)?(?P<inbound_ssh>ssh)( +)?'
                         r'(?P<inbound_telnet>telnet)( +)?$')

        # Protocol inet, MTU: 1500
        p26 = re.compile(r'^Protocol +(?P<address_family_name>[^\s,]+), +MTU: +(?P<mtu>\S+)$')

        # Flags: Sendbcast-pkt-to-re, Is-Primary
        p27 = re.compile(r'^Flags: +(?P<ifff_sendbcast_pkt_to_re>Sendbcast-pkt-to-re)'
                         r'(, +)?(?P<ifff_is_primary>Is-Primary)?$')

        # Addresses, Flags: Is-Preferred Is-Primary
        p28 = re.compile(r'^Addresses(, Flags: +)?(?P<flags>.+)?$')

        # Destination: 172.16.1/24, Local: 172.16.1.55, Broadcast: 172.16.1.255
        p29 = re.compile(r'^(Destination: +(?P<ifa_destination>[^\s,]+))?(, +)?'
                         r'(Local: +(?P<ifa_local>[^\s,]+))?(, +)?'
                         r'(Broadcast: +(?P<ifa_broadcast>[^\s,]+))?$')


        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_info_dict = ret_dict.setdefault('interface-information', {})
                physical_interface_list =  interface_info_dict.setdefault('physical-interface', [])
                physical_interface_dict = {}
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                physical_interface_list.append(physical_interface_dict)
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            m = p3.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if_device_flags = physical_interface_dict.setdefault('if-device-flags', {})
                if_device_flags.update({k.replace('_', '-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                if_config_flags = physical_interface_dict.setdefault('if-config-flags', {})
                if_config_flags.update({k.replace('_', '-'):
                    True for k, v in group.items() if v is not None and k != "internal_flags"})
                if "internal_flags" in group:
                    if_config_flags.update({"internal-flags": group["internal_flags"]})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                if_media_flags = physical_interface_dict.setdefault('if-media-flags', {})
                if_media_flags.update({k.replace('_', '-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                phys_cos_info = physical_interface_dict.setdefault('physical-interface-cos-information', {})
                phys_cos_info.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                traffic_stats = physical_interface_dict.setdefault('traffic-statistics', {})
                traffic_stats.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                traffic_stats.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                active_alarm = physical_interface_dict.setdefault('active-alarms', {})
                interface_alarm = active_alarm.setdefault('interface-alarms', {})
                interface_alarm.update({k.replace('_', '-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                active_alarm = physical_interface_dict.setdefault('active-defects', {})
                interface_defect = active_alarm.setdefault('interface-alarms', {})
                interface_defect.update({k.replace('_', '-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                logical_interface_list = physical_interface_dict.setdefault('logical-interface', [])
                logical_interface_dict = {}
                logical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                logical_interface_list.append(logical_interface_dict)
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                if_config_flags = logical_interface_dict.setdefault('if-config-flags', {})
                if_config_flags.update({k.replace('_','-'):
                    True for k, v in group.items() if v is not None and k not in [
                        "encapsulation",
                        "internal_flags"]})
                if "encapsulation" in group and group["encapsulation"]:
                    logical_interface_dict.update({"encapsulation": group["encapsulation"]})
                if "internal_flags" in group and group["internal_flags"]:
                    if_config_flags.update({"internal-flags": group["internal_flags"]})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                traffic_stats = logical_interface_dict.setdefault('traffic-statistics', {})
                traffic_stats.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                traffic_stats.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                logical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            m = p25.match(line)
            if m:
                group = m.groupdict()
                allowed_in_traffic = logical_interface_dict.setdefault('allowed-host-inbound-traffic', {})
                allowed_in_traffic.update({k.replace('_','-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                address_family_list = logical_interface_dict.setdefault('address-family', [])
                address_family_dict = {}
                address_family_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                address_family_list.append(address_family_dict)
                continue

            m = p27.match(line)
            if m:
                group = m.groupdict()
                address_family_flags = address_family_dict.setdefault('address-family-flags', {})
                address_family_flags.update({k.replace('_','-'):
                    True for k, v in group.items() if v is not None})
                continue

            m = p28.match(line)
            if m:
                group = m.groupdict()
                interface_address_list = address_family_dict.setdefault('interface-address', [])
                interface_address_dict = {}
                ifa_flags = interface_address_dict.setdefault('ifa-flags', {})
                if 'flags' in group and group['flags']:
                    flags = group['flags'].split(' ')
                    ifa_flags.update({"ifaf-current-{}".format(f.split('-')[-1].lower()):
                        True for f in flags})
                interface_address_list.append(interface_address_dict)
                continue

            m = p29.match(line)
            if m:
                group = m.groupdict()
                if group['ifa_destination']:
                    interface_address_dict.update({'ifa-destination': group['ifa_destination']})
                if group['ifa_local']:
                    interface_address_dict.update({'ifa-local': group['ifa_local']})
                if group['ifa_broadcast']:
                    interface_address_dict.update({'ifa-broadcast': group['ifa_broadcast']})
                continue

        return ret_dict

# =======================================================
# Schema for 'show interfaces policers {interface}'
# =======================================================
class ShowInterfacesPolicersInterfaceSchema(MetaParser):
    """Schema for show interfaces policers {interface}"""

    '''schema = {
    Optional("@xmlns:junos"): str,
    "interface-policer-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "physical-interface": [
            "admin-status": str,
            "logical-interface": [
                "admin-status": str,
                "name": str,
                "oper-status": str,
                "policer-information": [
                    {
                        "policer-family": str,
                        "policer-input": str,
                        "policer-output": str
                    }
                ]
            ],
            "name": str,
            "oper-status": str
        ]
    }
}'''

    schema = {
    Optional("@xmlns:junos"): str,
    "interface-policer-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "physical-interface": ListOf({
            "admin-status": str,
            "logical-interface": ListOf({
                "admin-status": str,
                "name": str,
                "oper-status": str,
                "policer-information": ListOf({
                    "policer-family": str,
                    "policer-input": str,
                    Optional("policer-output"): Or(str,None)
                })
            }),
            "name": str,
            "oper-status": str
        })
    }
}

# =======================================================
# Parser for 'show interfaces policers {interface}'
# =======================================================
class ShowInterfacesPolicersInterface(ShowInterfacesPolicersInterfaceSchema):
    """ Parser for:
            - show interfaces policers {interface}
    """

    cli_command = 'show interfaces policers {interface}'

    def cli(self, interface=None, output=None):
        # execute the command
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ret_dict = {}

        # ge-0/0/2        up    up
        p1 =  re.compile(r'^(?P<interface>[a-zA-Z\-\d\/]+)((?P<physical_interface_value>[\.\d]+))? +(?P<admin>\w+) +(?:(?P<link>\w+))?$')


        # inet  GE_1M-ge-0/0/2.0-log_int-i GE_1M-ge-0/0/2.0-log_int-o
        # multiservice __default_arp_policer__
        p2 =  re.compile(r'^(?P<policer_family>\w+) +(?P<policer_input>\S+)( +((?P<policer_output>\S+)))?$')

        for line in out.splitlines():
            line = line.strip()
            # ge-0/0/2        up    up
            # ge-0/0/2.0      up    up
            m = p1.match(line)
            if m:
                interface_policer_info = ret_dict.setdefault(
                    "interface-policer-information", {}).setdefault("physical-interface",[])
                #logical_interface_list = interface_policer_info.setdefault("logical-interface",[])
                #policer_information_list = logical_interface_list.setdefault("policer-information", [])

                exists = False
                policer_information_list = None
                group = m.groupdict()
                for group_key, group_value in group.items():
                    if group_key == "physical_interface_value":
                        if group_value != None:
                            exists = True
                if exists:
                    
                    logical_interface_dict['name'] = group['interface'] + group['physical_interface_value']
                    logical_interface_dict['admin-status'] = group['admin']
                    logical_interface_dict['oper-status'] = group['link']

                    policer_information_list = []
                    logical_interface_dict["policer-information"] = policer_information_list
                    logical_interface_list.append(logical_interface_dict)

                    interface_policer_info_dict['logical-interface'] = logical_interface_list

                    interface_policer_info.append(interface_policer_info_dict)

                else:
                    logical_interface_list = []
                    logical_interface_dict = {}
                    interface_policer_info_dict= {}
                    interface_policer_info_dict['name'] = group['interface']
                    interface_policer_info_dict['admin-status'] = group['admin']
                    interface_policer_info_dict['oper-status'] = group['link']

                    

            # inet  GE_1M-ge-0/0/2.0-log_int-i GE_1M-ge-0/0/2.0-log_int-o
            # multiservice __default_arp_policer__
            m = p2.match(line)
            if m:    
                group = m.groupdict()
                policer_information_dict = {}
                policer_information_dict['policer-family'] = group['policer_family']
                policer_information_dict['policer-input'] = group['policer_input']

                for group_key, group_value in group.items():
                    if group_key == "policer_output":
                        if group_value != None:
                            policer_information_dict['policer-output'] = group['policer_output']

                policer_information_list.append(policer_information_dict)

                exists = False

        return ret_dict


# =======================================================
# Schema for 'show interfaces queue {interface}'
# =======================================================
class ShowInterfacesQueueSchema(MetaParser):
    """
    Schema for:
        * show interfaces queue {interface}
    """

    schema = {
        "interface-information": {
            "physical-interface": {
                Optional("description"): str,
                "local-index": str,
                "snmp-index": str,
                "name": str,
                "oper-status": str,
                "queue-counters": {
                    "interface-cos-summary": {
                        "intf-cos-forwarding-classes-in-use": str,
                        "intf-cos-forwarding-classes-supported": str,
                        "intf-cos-num-queues-in-use": str,
                        "intf-cos-num-queues-supported": str,
                        "intf-cos-queue-type": str
                    },
                    "queue": ListOf({
                        "forwarding-class-name": str,
                        "queue-counters-queued-bytes": str,
                        "queue-counters-queued-bytes-rate": str,
                        "queue-counters-queued-packets": str,
                        "queue-counters-queued-packets-rate": str,
                        "queue-counters-red-bytes": str,
                        "queue-counters-red-bytes-high": str,
                        "queue-counters-red-bytes-low": str,
                        "queue-counters-red-bytes-medium-high": str,
                        "queue-counters-red-bytes-medium-low": str,
                        "queue-counters-red-bytes-rate": str,
                        "queue-counters-red-bytes-rate-high": str,
                        "queue-counters-red-bytes-rate-low": str,
                        "queue-counters-red-bytes-rate-medium-high": str,
                        "queue-counters-red-bytes-rate-medium-low": str,
                        "queue-counters-red-packets": str,
                        "queue-counters-red-packets-high": str,
                        "queue-counters-red-packets-low": str,
                        "queue-counters-red-packets-medium-high": str,
                        "queue-counters-red-packets-medium-low": str,
                        "queue-counters-red-packets-rate": str,
                        "queue-counters-red-packets-rate-high": str,
                        "queue-counters-red-packets-rate-low": str,
                        "queue-counters-red-packets-rate-medium-high": str,
                        "queue-counters-red-packets-rate-medium-low": str,
                        "queue-counters-tail-drop-packets": str,
                        "queue-counters-tail-drop-packets-rate": str,
                        Optional("queue-counters-rl-drop-packets"): str,
                        Optional("queue-counters-rl-drop-packets-rate"): str,
                        Optional("queue-counters-rl-drop-bytes"): str,
                        Optional("queue-counters-rl-drop-bytes-rate"): str,
                        "queue-counters-trans-bytes": str,
                        "queue-counters-trans-bytes-rate": str,
                        "queue-counters-trans-packets": str,
                        "queue-counters-trans-packets-rate": str,
                        "queue-number": str
                    })
                }
            }
            }
        }


# =======================================================
# Parser for 'show interfaces queue {interface}'
# =======================================================
class ShowInterfacesQueue(ShowInterfacesQueueSchema):
    """
    Parser for:
        * show interfaces queue {interface}
    """
    cli_command = 'show interfaces queue {interface}'

    def cli(self, interface=None, output=None):
        if not output:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # -------------------------------------------------
        # Initialize variables
        # -------------------------------------------------
        ret_dict = {}
        red_dropped_bytes = red_dropped_packets = transmitted = None

        # -------------------------------------------------
        # Regex patterns
        # -------------------------------------------------
        # Physical interface: ge-0/0/2, Enabled, Physical link is Up
        p1 = re.compile(r"^Physical interface: (?P<name>\S+), Enabled, "
                        r"Physical link is (?P<oper_status>\S+)$")
        #           Interface index: 143, SNMP ifIndex: 601
        p2 = re.compile(r"^Interface index: (?P<local_index>\S+), "
                       r"SNMP ifIndex: (?P<snmp_index>\S+)$")
        #           Description: to_ixia_2/4
        p3 = re.compile(r"^Description: (?P<description>\S+)$")
        #         Forwarding classes: 16 supported, 5 in use
        p4 = re.compile(r"^Forwarding classes: "
                        r"(?P<intf_cos_forwarding_classes_supported>\S+) supported, "
                        r"(?P<intf_cos_forwarding_classes_in_use>\S+) in use$")
        #         Egress queues: 8 supported, 5 in use
        p5 = re.compile(r"^(?P<intf_cos_queue_type>Egress queues): (?P<intf_cos_num_queues_supported>\S+) supported, "
                        r"(?P<intf_cos_num_queues_in_use>\S+) in use$")
        #         Queue: 0, Forwarding classes: Bronze-FC
        p6 = re.compile(r"^Queue: (?P<queue_number>\S+), "
                        r"Forwarding classes: (?P<forwarding_class_name>\S+)$")
        #           Queued:
        #             Packets              :            1470816406                     0 pps <-- rate
        #             Bytes                :          564883280956                     0 bps
        #           Transmitted:
        p8 = re.compile(r"^(?P<name>Transmitted):$")
        #             Packets              :            1470816406                      0 pps
        #             Bytes                :          564883280956                     0 bps
        #             Tail-dropped packets :                     0                     0 pps
        #             RED-dropped packets  :                     0                     0 pps
        p9 = re.compile(r"^(?P<name>RED-dropped packets) +: +(?P<counts>\S+) +(?P<rates>\S+) +pps$")
        #              Low                 :                     0                     0 pps
        #              Medium-low          :                     0                     0 pps
        #              Medium-high         :                     0                     0 pps
        #              High                :                     0                     0 pps
        #             RED-dropped bytes    :                     0                     0 bps
        p10 = re.compile(r"^(?P<name>RED-dropped bytes) +: +(?P<counts>\S+) +(?P<rates>\S+) +bps$")
        #              Low                 :                     0                     0 bps
        #              Medium-low          :                     0                     0 bps
        #              Medium-high         :                     0                     0 bps
        #              High                :                     0                     0 bps
        #              RL-dropped packets   :                     0                     0 pps
        #              Tail-dropped packets :                     0                     0 pps
        p7 = re.compile(r"^(?P<name>Packets|Bytes|Tail-dropped +packets|"
                        r"RL-dropped +packets|"
                        r"Low|Medium-low|Medium-high|High) +: "
                        r"+(?P<counts>\S+) +(?P<rates>\S+) +[p|b]ps$")

        # -------------------------------------------------
        # Build parsed output
        # -------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # Physical interface: ge-0/0/2, Enabled, Physical link is Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict = ret_dict.setdefault('interface-information', {}).\
                                                    setdefault('physical-interface', {})
                physical_interface_dict['name'] = group['name']
                physical_interface_dict['oper-status'] = group['oper_status']
                continue

            #           Interface index: 143, SNMP ifIndex: 601
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    physical_interface_dict[entry_key] = group_value
                continue

            #           Description: to_ixia_2/4
            m = p3.match(line)
            if m:
                physical_interface_dict['description'] = m.groupdict()['description']
                continue

            #         Forwarding classes: 16 supported, 5 in use
            #         Egress queues: 8 supported, 5 in use
            m = p4.match(line) or p5.match(line)
            if m:
                if 'queue-counters' not in physical_interface_dict:
                    interface_cos_summary_dict = physical_interface_dict.\
                                                 setdefault('queue-counters', {}).\
                                                 setdefault('interface-cos-summary', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    interface_cos_summary_dict[entry_key] = group_value
                continue

            #         Queue: 0, Forwarding classes: Bronze-FC
            m = p6.match(line)
            if m:
                group = m.groupdict()
                red_dropped_packets = None
                red_dropped_bytes = None
                transmitted = None

                if "queue" not in physical_interface_dict['queue-counters']:
                    physical_interface_dict['queue-counters']['queue'] = []
                current_queue_dict = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    current_queue_dict[entry_key] = group_value

                physical_interface_dict['queue-counters']['queue'].append(current_queue_dict)
                continue

            #             Packets              :            1470816406                      0 pps
            #             Bytes                :          564883280956                     0 bps
            #             Tail-dropped packets :                     0                     0 pps
            #             ...
            #              Low                 :                     0                     0 pps
            #              Medium-low          :                     0                     0 pps
            #              Medium-high         :                     0                     0 pps
            #              High                :                     0                     0 pps
            m = p7.match(line)
            if m:
                group = m.groupdict()
                name = group['name']
                counts = group['counts']
                rates = group['rates']

                # RED-dropped bytes
                if red_dropped_bytes:
                    if name == 'Low':
                        current_queue_dict['queue-counters-red-bytes-low'] = counts
                        current_queue_dict['queue-counters-red-bytes-rate-low'] = rates
                    elif name == 'Medium-low':
                        current_queue_dict['queue-counters-red-bytes-medium-low'] = counts
                        current_queue_dict['queue-counters-red-bytes-rate-medium-low'] = rates
                    elif name == 'Medium-high':
                        current_queue_dict['queue-counters-red-bytes-medium-high'] = counts
                        current_queue_dict['queue-counters-red-bytes-rate-medium-high'] = rates
                    elif name == 'High':
                        current_queue_dict['queue-counters-red-bytes-high'] = counts
                        current_queue_dict['queue-counters-red-bytes-rate-high'] = rates

                # RED-dropped packets
                elif red_dropped_packets:
                    if name == 'Low':
                        current_queue_dict['queue-counters-red-packets-low'] = counts
                        current_queue_dict['queue-counters-red-packets-rate-low'] = rates
                    elif name == 'Medium-low':
                        current_queue_dict['queue-counters-red-packets-medium-low'] = counts
                        current_queue_dict['queue-counters-red-packets-rate-medium-low'] = rates
                    elif name == 'Medium-high':
                        current_queue_dict['queue-counters-red-packets-medium-high'] = counts
                        current_queue_dict['queue-counters-red-packets-rate-medium-high'] = rates
                    elif name == 'High':
                        current_queue_dict['queue-counters-red-packets-high'] = counts
                        current_queue_dict['queue-counters-red-packets-rate-high'] = rates

                # Transmitted
                elif transmitted:
                    if name == 'Packets':
                        current_queue_dict['queue-counters-trans-packets'] = counts
                        current_queue_dict['queue-counters-trans-packets-rate'] = rates
                    elif name == 'Bytes':
                        current_queue_dict['queue-counters-trans-bytes'] = counts
                        current_queue_dict['queue-counters-trans-bytes-rate'] = rates
                    elif name == 'Tail-dropped packets':
                        current_queue_dict['queue-counters-tail-drop-packets'] = counts
                        current_queue_dict['queue-counters-tail-drop-packets-rate'] = rates
                    elif name == 'RL-dropped packets':
                        current_queue_dict['queue-counters-rl-drop-packets'] = counts
                        current_queue_dict['queue-counters-rl-drop-packets-rate'] = rates

                # Queued
                else:
                    if name == 'Packets':
                        current_queue_dict['queue-counters-queued-packets'] = counts
                        current_queue_dict['queue-counters-queued-packets-rate'] = rates
                    elif name == 'Bytes':
                        current_queue_dict['queue-counters-queued-bytes'] = counts
                        current_queue_dict['queue-counters-queued-bytes-rate'] = rates

                continue

            #           Transmitted:
            m = p8.match(line)
            if m:
                transmitted = True
                continue

            #             RED-dropped packets  :                     0                     0 pps
            m = p9.match(line)
            if m:
                red_dropped_packets = True
                group = m.groupdict()
                if group['name'] == 'RED-dropped packets':
                    current_queue_dict['queue-counters-red-packets'] = group['counts']
                    current_queue_dict['queue-counters-red-packets-rate'] = group['rates']
                continue

            #             RED-dropped bytes    :                     0                     0 bps
            m = p10.match(line)
            if m:
                red_dropped_bytes = True
                group = m.groupdict()
                if group['name'] == 'RED-dropped bytes':
                    current_queue_dict['queue-counters-red-bytes'] = group['counts']
                    current_queue_dict['queue-counters-red-bytes-rate'] = group['rates']
                continue
        return ret_dict

class ShowInterfacesExtensiveInterface(ShowInterfaces):
    cli_command = 'show interfaces extensive {interface}'
    def cli(self, interface, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                interface=interface
            ))
        else:
            out = output
        
        return super().cli(output=out)


class ShowInterfacesDiagnosticsOpticsSchema(MetaParser):
    """Schema for
        * show interfaces diagnostics optics {interface}
        * show interfaces diagnostics optics
    """

    schema = {
        'interface-information': {
            'physical-interface': ListOf({
                'name': str,
                'optics-diagnostics': {
                    Optional("laser-bias-current"): str,
                    Optional("laser-output-power"): str,
                    "module-temperature": str,
                    "module-voltage": str,
                    Optional("receiver-signal-average-optical-power"): str,
                    Optional("laser-bias-current-high-alarm"): str,
                    Optional("laser-bias-current-low-alarm"): str,
                    Optional("laser-bias-current-high-warning"): str,
                    Optional("laser-bias-current-low-warning"): str,
                    Optional("laser-output-power-high-alarm"): str,
                    Optional("laser-output-power-low-alarm"): str,
                    Optional("laser-output-power-high-warning"): str,
                    Optional("laser-output-power-low-warning"): str,
                    "module-temperature-high-alarm": str,
                    "module-temperature-low-alarm": str,
                    "module-temperature-high-warning": str,
                    "module-temperature-low-warning": str,
                    "module-voltage-high-alarm": str,
                    "module-voltage-low-alarm": str,
                    "module-voltage-high-warning": str,
                    "module-voltage-low-warning": str,
                    Optional("laser-rx-power-high-alarm"): str,
                    Optional("laser-rx-power-low-alarm"): str,
                    Optional("laser-rx-power-high-warning"): str,
                    Optional("laser-rx-power-low-warning"): str,
                    "laser-bias-current-high-alarm-threshold": str,
                    "laser-bias-current-low-alarm-threshold": str,
                    "laser-bias-current-high-warning-threshold": str,
                    "laser-bias-current-low-warning-threshold": str,
                    "laser-output-power-high-alarm-threshold": str,
                    "laser-output-power-low-alarm-threshold": str,
                    "laser-output-power-high-warning-threshold": str,
                    "laser-output-power-low-warning-threshold": str,
                    "module-temperature-high-alarm-threshold": str,
                    "module-temperature-low-alarm-threshold": str,
                    "module-temperature-high-warning-threshold": str,
                    "module-temperature-low-warning-threshold": str,
                    "module-voltage-high-alarm-threshold": str,
                    "module-voltage-low-alarm-threshold": str,
                    "module-voltage-high-warning-threshold": str,
                    "module-voltage-low-warning-threshold": str,
                    "laser-rx-power-high-alarm-threshold": str,
                    "laser-rx-power-low-alarm-threshold": str,
                    Optional("laser-rx-power-high-warning-threshold"): str,
                    Optional("laser-rx-power-low-warning-threshold"): str,
                    Optional("module-not-ready-alarm"): str,
                    Optional("module-low-power-alarm"): str,
                    Optional("module-initialization-incomplete-alarm"): str,
                    Optional("module-fault-alarm"): str,
                    Optional("pld-flash-initialization-fault-alarm"): str,
                    Optional("power-supply-fault-alarm"): str,
                    Optional("checksum-fault-alarm"): str,
                    Optional("tx-laser-disabled-alarm"): str,
                    Optional("tx-loss-of-signal-functionality-alarm"): str,
                    Optional("tx-cdr-loss-of-lock-alarm"): str,
                    Optional("rx-loss-of-signal-alarm"): str,
                    Optional("rx-cdr-loss-of-lock-alarm"): str,
                    Optional("laser-temperature-high-alarm-threshold"): str,
                    Optional("laser-temperature-low-alarm-threshold"): str,
                    Optional("laser-temperature-high-warning-threshold"): str,
                    Optional("laser-temperature-low-warning-threshold"): str,
                    Optional("lanes"): ListOf({
                        "lane-number": str,
                        "laser-bias-current": str,
                        "laser-output-power": str,
                        "laser-temperature": str,
                        "laser-receiver-power": str,
                        "laser-bias-current-high-alarm": str,
                        "laser-bias-current-low-alarm": str,
                        "laser-bias-current-high-warning": str,
                        "laser-bias-current-low-warning": str,
                        "laser-output-power-high-alarm": str,
                        "laser-output-power-low-alarm": str,
                        "laser-output-power-high-warning": str,
                        "laser-output-power-low-warning": str,
                        "laser-temperature-high-alarm": str,
                        "laser-temperature-low-alarm": str,
                        "laser-temperature-high-warning": str,
                        "laser-temperature-low-warning": str,
                        "laser-receiver-power-high-alarm": str,
                        "laser-receiver-power-low-alarm": str,
                        "laser-receiver-power-high-warning": str,
                        "laser-receiver-power-low-warning": str,
                        "tx-loss-of-signal-functionality-alarm": str,
                        "tx-cdr-loss-of-lock-alarm": str,
                        "rx-loss-of-signal-alarm": str,
                        "rx-cdr-loss-of-lock-alarm": str,
                        "apd-supply-fault-alarm": str,
                        "tec-fault-alarm": str,
                        "wavelength-unlocked-alarm": str,
                    })
                }
            })
        }
    }

class ShowInterfacesDiagnosticsOptics(ShowInterfacesDiagnosticsOpticsSchema):
    """Parser for
        * show interfaces diagnostics optics {interface}
        * show interfaces diagnostics optics
    """

    cli_command = [
        "show interfaces diagnostics optics {interface}",
        "show interfaces diagnostics optics"
        ]

    def cli(self, interface=None, output=None):
        if not output:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1]) 
        else:
            out = output

        ret_dict = {}

        # Physical interface: et-0/0/0
        p1 = re.compile(r'^Physical +interface: +(?P<name>\S+)$')

        # Module temperature                        :  48 degrees C / 119 degrees F
        # Module voltage                            :  3.3340 V
        # Module temperature high alarm             :  Off
        p2 = re.compile(r'^(?P<key>[\S ]+) +: +(?P<value>[\S ]+)$')

        # Lane 0
        p3 = re.compile(r'^Lane +(?P<lane>\d+)$')

        lane = None

        for line in out.splitlines():
            line = line.strip()
            # Physical interface: et-0/0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                physical_interface_list = ret_dict.setdefault(
                    'interface-information',{}).setdefault(
                        'physical-interface', [])
                physical_interface_dict = {
                    'name': group['name']
                }
                physical_interface_list.append(physical_interface_dict)
                continue

            # Module temperature                        :  48 degrees C / 119 degrees F
            # Module voltage                            :  3.3340 V
            # Module temperature high alarm             :  Off
            m = p2.match(line)
            if m:
                group = m.groupdict()
                optics_dict = physical_interface_dict.setdefault('optics-diagnostics', {})
                if not isinstance(lane, dict):
                    optics_dict.update({
                        group['key'].strip().lower().replace(' ', '-'): group['value']
                    })
                else:
                    lane.update({
                        group['key'].strip().lower().replace(' ', '-'): group['value']
                    })
                continue

            # Lane 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                optics_dict = physical_interface_dict.setdefault('optics-diagnostics', {})
                lane_list = optics_dict.setdefault('lanes', [])
                lane = {
                    "lane-number": group['lane']
                }
                lane_list.append(lane)
                continue
                
        return ret_dict

class ShowInterfacesInterfaceDetail(ShowInterfaces):
    cli_command = 'show interfaces {interface} detail'
    def cli(self, interface, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                interface=interface
            ))
        else:
            out = output
        
        return super().cli(output=out)

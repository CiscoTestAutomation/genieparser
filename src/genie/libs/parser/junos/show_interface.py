"""show_interface.py

JunOS parsers for the following show commands:
    * show interfaces terse
    * show interfaces terse | match <interface>
    * show interfaces terse {interface}
    * show interfaces {interface} terse
    * show interfaces descriptions
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.exceptions import SchemaTypeError
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, SchemaTypeError

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
    """
    def validate_physical_interface_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('physical-interface is not a list')
        entry_schema = Schema(
            {
                "admin-status": str,
                "description": str,
                "name": str,
                "oper-status": str
            }
        )
        for item in value:
            entry_schema.validate(item)
        return value

    schema = {
        "interface-information": {
            "physical-interface": Use(validate_physical_interface_list)
        }
    }

class ShowInterfacesDescriptions(ShowInterfacesDescriptionsSchema):
    """ Parser for:
            * show interfaces descriptions
    """
    cli_command = 'show interfaces descriptions'


    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Interface       Admin Link Description
        p1 = re.compile(r'^Interface +Admin +Link +Description$')

        # ge-0/0/0        up    up   none/100G/in/hktGCS002_ge-0/0/0
        p2 = re.compile(r'^(?P<name>\S+) +(?P<admin_status>\S+) +(?P<oper_status>\S+) +(?P<description>\S+)$')

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
    #                             "interface-address": {
    #                                 "ifa-broadcast": str,
    #                                 "ifa-destination": str,
    #                                 "ifa-flags": {
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
    #                             "new-hold-limit": str
    #                         }
    #                     ],
    #                     "encapsulation": str,
    #                     "filter-information": str,
    #                     "if-config-flags": {
    #                         "iff-snmp-traps": str,
    #                         "iff-up": str,
    #                         "internal-flags": str
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
    #                     Optional("@junos:style"): str,
    #                     "input-bps": str,
    #                     "input-packets": str,
    #                     "input-pps": str,
    #                     "output-bps": str,
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
            raise SchemaTypeError('physical interface is not a list')

        def verify_address_family_list(value):
            # Pass address-family list of dict in value
            if not isinstance(value, list):
                raise SchemaTypeError('address-family is not a list')

            def verify_interface_address_list(value):
                # Pass physical-interface list of dict in value
                if not isinstance(value, list) and not isinstance(value, dict):
                    raise SchemaTypeError('interface-address is not a list/dict')

                interface_address_schema = Schema({
                    Optional("ifa-broadcast"): str,
                    Optional("ifa-destination"): str,
                    "ifa-flags": {
                        Optional("ifaf-current-preferred"): bool,
                        Optional("ifaf-current-primary"): bool,
                        Optional("ifaf-is-primary"): bool,
                        Optional("ifaf-is-preferred"): bool,
                        Optional("ifaf-kernel"): bool,
                        Optional("ifaf-preferred"): bool,
                        Optional("ifaf-primary"): bool,
                        Optional("ifaf-is-default"): bool,
                        Optional("ifaf-none"): bool,
                    },
                    Optional("ifa-local"): str
                })

                # Validate each dictionary in list
                if isinstance(value, dict):
                    value = [value]
                for item in value:
                    interface_address_schema.validate(item)
                return value

            af_schema = Schema({
                Optional("address-family-flags"): {
                    Optional("ifff-is-primary"): bool,
                    Optional("ifff-no-redirects"): bool,
                    Optional("ifff-none"): bool,
                    Optional("ifff-sendbcast-pkt-to-re"): bool,
                    Optional("internal-flags"): bool,
                    Optional("ifff-primary"): bool,
                },
                "address-family-name": str,
                Optional("interface-address"): Use(verify_interface_address_list),
                Optional("intf-curr-cnt"): str,
                Optional("intf-dropcnt"): str,
                Optional("intf-unresolved-cnt"): str,
                Optional("max-local-cache"): str,
                Optional("maximum-labels"): str,
                "mtu": str,
                Optional("new-hold-limit"): str
            })
            # Validate each dictionary in list
            for item in value:
                af_schema.validate(item)
            return value

        # Create physical-interface Schema
        physical_interface_schema = Schema({
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
            "if-device-flags": {
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
            Optional("local-index"): str,
            Optional("logical-interface"): {
                Optional("address-family"): Use(verify_address_family_list),
                Optional("encapsulation"): str,
                Optional("filter-information"): str,
                "if-config-flags": {
                    "iff-snmp-traps": bool,
                    "iff-up": bool,
                    Optional("internal-flags"): str
                },
                "local-index": str,
                Optional("logical-interface-bandwidth"): str,
                "name": str,
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
                }
            },
            Optional("loopback"): str,
            Optional("lsi-traffic-statistics"): {
                Optional("@junos:style"): str,
                "input-bps": str,
                "input-bytes": str,
                "input-packets": str,
                "input-pps": str
            },
            Optional("mru"): str,
            Optional("mtu"): str,
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
                    "input-broadcasts": str,
                    "input-bytes": str,
                    "input-code-violations": str,
                    "input-crc-errors": str,
                    "input-fifo-errors": str,
                    "input-fragment-frames": str,
                    "input-jabber-frames": str,
                    "input-mac-control-frames": str,
                    "input-mac-pause-frames": str,
                    "input-multicasts": str,
                    "input-oversized-frames": str,
                    "input-packets": str,
                    Optional("input-total-errors"): str,
                    "input-unicasts": str,
                    "input-vlan-tagged-frames": str,
                    "output-broadcasts": str,
                    "output-bytes": str,
                    "output-crc-errors": str,
                    "output-fifo-errors": str,
                    "output-mac-control-frames": str,
                    "output-mac-pause-frames": str,
                    "output-multicasts": str,
                    "output-packets": str,
                    Optional("output-total-errors"): str,
                    "output-unicasts": str
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
                    "input-bps": str,
                    "input-bytes": str,
                    "input-packets": str,
                    "input-pps": str,
                    "output-bps": str,
                    "output-bytes": str,
                    "output-packets": str,
                    "output-pps": str
                },
                "output-bps": str,
                "output-bytes": str,
                "output-packets": str,
                "output-pps": str
            }
        })
        # Validate each dictionary in list
        for item in value:
            physical_interface_schema.validate(item)
        return value
    
    schema = {
        Optional("@xmlns:junos"): str,
        "interface-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "physical-interface": Use(verify_physical_interface_list)
        }
    }

class ShowInterfaces(ShowInterfacesSchema):
    cli_command = ['show interfaces']

    def cli(self, output=None):

        if not output:
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
            r'(, +Generation: +\S+)$')

        # Description: none/100G/in/hktGCS002_ge-0/0/0
        p3 = re.compile(r'^Description: +(?P<description>\S+)$')

        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        p4 = re.compile(r'^(Type: +\S+, )?Link-level +type: +'
            r'(?P<link_level_type>\S+), +MTU: +(?P<mtu>\S+)'
            r'(, +MRU: +(?P<mru>\d+))?(, +(?P<sonet_mode>\S+) +mode)?'
            r'(, +Speed: +(?P<speed>\S+))?(, +BPDU +Error: +'
            r'(?P<bpdu_error>\S+),)?$')
        
        # Speed: 800mbps
        p4_1 = re.compile(r'^Speed: +(?P<speed>\S+)$')

        p4_2 = re.compile(r'^')

        # Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        p5 = re.compile(r'^Loop +Detect +PDU +Error: +(?P<ld_pdu_error>\S+), +'
            r'Ethernet-Switching +Error: +(?P<eth_switch_error>\S+), +MAC-REWRITE +'
            r'Error: +\S+, +Loopback: +(?P<loopback>\S+),$')

        # Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        p6 = re.compile(r'^Source +filtering: +(?P<source_filtering>\S+), +'
            r'Flow +control: +(?P<if_flow_control>\S+), +'
            r'Auto-negotiation: +(?P<if_auto_negotiation>\S+), +'
            r'Remote +fault: +(?P<if_remote_fault>\S+)$')

        # Pad to minimum frame size: Disabled
        p7 = re.compile(r'^Pad +to +minimum +frame +size: +'
            r'(?P<pad_to_minimum_frame_size>\S+)$')

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
        p25 = re.compile(r'^Flags: +(?P<iff_up>\S+)( +SNMP-Traps)?'
            r'( +(?P<internal_flags>\S+))? +Encapsulation: +'
            r'(?P<encapsulation>\S+)$')

        # Input packets : 133657033
        p26 = re.compile(r'^Input +packets *: +(?P<input_packets>\S+)$')

        # Output packets: 129243982
        p27 = re.compile(r'^Output +packets *: +(?P<output_packets>\S+)$')

        # Protocol inet, MTU: 1500
        p28 = re.compile(r'^Protocol +(?P<address_family_name>\S+), +'
            r'MTU: +(?P<mtu>\S+)(, +Maximum labels: +(?P<maximum_labels>\S+))?$')

        # Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
        p30 = re.compile(r'^Max +nh +cache: +(?P<max_local_cache>\d+), +'
            r'New +hold +nh +limit: +(?P<new_hold_limit>\d+)'
            r', Curr +nh +cnt: +(?P<intf_curr_cnt>\d+), +'
            r'Curr +new +hold +cnt: +(?P<intf_unresolved_cnt>\d+)'
            r', +NH +drop +cnt: +(?P<intf_dropcnt>\d+)$')

        # Flags: No-Redirects, Sendbcast-pkt-to-re
        p31 = re.compile(r'^Flags: +(?P<flags>[\S\s]+)')

        # Addresses, Flags: Is-Preferred Is-Primary
        p32 = re.compile(r'^Addresses, +Flags: +(?P<flags>[\S\s]+)$')

        # Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95
        p33 = re.compile(r'^Destination: +(?P<ifa_destination>\S+)'
            r', +Local: +(?P<ifa_local>\S+)'
            r'(, +Broadcast: +(?P<ifa_broadcast>\S+))?$')

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
        p43_1 = re.compile(r'^Errors: +(?P<input_errors>\d+), +Drops: +'
            r'(?P<input_drops>\d+), +Framing +errors: +(?P<framing_errors>\d+), +'
            r'Runts: +(?P<input_runts>\d+), Policed +discards: +'
            r'(?P<input_discards>\d+), +L3 +incompletes: +'
            r'(?P<input_l3_incompletes>\d+), +L2 +channel +errors: +'
            r'(?P<input_l2_channel_errors>\d+),$')
        
        # L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
        p43_2 = re.compile(r'^L2 +mismatch +timeouts: +'
            r'(?P<input_l2_mismatch_timeouts>\d+), +FIFO +errors: +'
            r'(?P<input_fifo_errors>\d+), +Resource +errors: +'
            r'(?P<input_resource_errors>\d+)')

        # Carrier transitions: 1, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
        p44_1 = re.compile(r'^Carrier +transitions: +(?P<carrier_transitions>\d+), +'
            r'Errors: +(?P<output_errors>\d+), +Drops: +(?P<output_drops>\d+), +'
            r'Collisions: +(?P<output_collisions>\d+), +Aged+ packets: +'
            r'(?P<aged_packets>\d+), +FIFO +errors: +(?P<output_fifo_errors>\d+), +'
            r'HS +link +CRC +errors: +(?P<hs_link_crc_errors>\d+),$')

        # MTU errors: 0, Resource errors: 0
        p44_2 = re.compile(r'^MTU +errors: +(?P<mtu_errors>\d+), +Resource +'
            r'errors: +(?P<output_resource_errors>\d+)$')
        
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
        p60 = re.compile(r'^Total +errors +(?P<input_total_errors>\d+)$')

        # Label-switched interface (LSI) traffic statistics:
        p61 = re.compile(r'^Label-switched +interface +\(LSI\) +traffic +statistics:$')

        cnt = 0
        for line in out.splitlines():
            line = line.strip()
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
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            m = p4.match(line)
            if m:
                group = m.groupdict()
                physical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Speed: 800mbps
            m = p4_1.match(line)
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
                statistics_type = 'ipv6_transit'
                group = m.groupdict()
                traffic_statistics_dict = traffic_statistics_dict.setdefault('ipv6-transit-statistics', {})
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
                statistics_type = 'transit_statistics'
                group = m.groupdict()
                traffic_statistics_dict = physical_interface_dict.setdefault('transit-traffic-statistics', {})
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
                statistics_type = 'logical'
                group = m.groupdict()
                logical_interface_dict = physical_interface_dict.setdefault('logical-interface', {})
                logical_interface_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
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
                address_family_list.append(address_family_dict)
                continue

            # Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                address_family_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Flags: No-Redirects, Sendbcast-pkt-to-re
            m = p31.match(line)
            if m:
                group = m.groupdict()
                address_family_flags_dict = address_family_dict.setdefault('address-family-flags', {})
                for flag in group['flags'].split(','):
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

            # Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95
            m = p33.match(line)
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
            # p41 = re.compile(r'^Input +errors:$')
            m = p41.match(line)
            if m:
                input_error_list_dict = physical_interface_dict.setdefault('input-error-list', {})
                continue

            # Output errors:
            # p42 = re.compile(r'^Output +errors:$')
            m = p42.match(line)
            if m:
                output_error_list_dict = physical_interface_dict.setdefault('output-error-list', {})
                continue

            # Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
            m = p43_1.match(line)
            if m:
                group = m.groupdict()
                input_error_list_dict.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            m = p43_2.match(line)
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
        return ret_dict

class ShowInterfacesExtensive(ShowInterfaces):
    cli_command = ['show interfaces extensive',
        'show interfaces extensive {interface}']
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
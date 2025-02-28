"""show_dhcp.py

NXOS parsers for the following show commands:
	* 'show ip dhcp snooping binding dynamic evpn'
	* 'show ip dhcp snooping binding static evpn'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (
                                                Schema, 
                                                Any, 
                                                Optional, 
                                                Or, 
                                                And,
                                                Default, 
                                                Use,
                                                ListOf
                                                )
from genie import parsergen
from genie.libs.parser.utils.common import Common

# This API is for DHCP snoop table - dynamic/static with evpn keyword for Vxlan
class ShowIpDhcpSnoopingBindingSchema(MetaParser):
    schema = {
        'bindings': {
            Any(): {
                'mac_address': str,
                'ip_address': str,
                'lease_sec': Or(int, str),
                'type': str,
                'bd': int,
                'interface': str,
                Optional('anchor'): str,
                Optional('freeze'): str,
            }
        }
    }

class ShowIpDhcpSnoopingBindingDynamicEvpn(ShowIpDhcpSnoopingBindingSchema):
    # Parser for 'show ip dhcp snooping binding dynamic evpn'
    # show ip dhcp snooping binding dynamic evpn
    # MacAddress         IpAddress        Lease(Sec)  Type      BD    Interface           anchor       Freeze
    # -----------------  ---------------  --------  ----------  ----  -------------      -------    -----------
    # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
    # 00:10:01:03:02:01  100.10.1.148     3278      dhcp-snoop  1001  port-channel11       YES       NONE
    # 00:10:01:05:02:01  100.10.1.101     3268      dhcp-snoop  1001  nve1(peer-id: 1)     NO        NONE
    cli_command = ['show ip dhcp snooping binding dynamic evpn',
                   'show ip dhcp snooping binding interface {intf} dynamic evpn', 
                   'show ip dhcp snooping binding vlan {vlan} dynamic evpn', 
                   'show ip dhcp snooping binding interface {intf} vlan {vlan} dynamic evpn'
                   ]

    def cli(self, intf='', vlan='', output=None):
        if (intf and vlan):
            cmd = self.cli_command[3].format(intf=intf, vlan=vlan)
        elif intf:
            cmd = self.cli_command[1].format(intf=intf)
        elif vlan:
            cmd = self.cli_command[2].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}

        # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
        p1 = re.compile(
            r'^(?P<mac_address>[0-9A-Fa-f:]+)\s+'
            r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)\s+'
            r'(?P<lease_sec>\d+)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<bd>\d+)\s+'
            r'(?P<interface>[^\s]+\s*[^\s]*)\s+'
            r'(?P<anchor>\S+)\s+'
            r'(?P<freeze>\S+)$'
        )

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1
            match = p1.match(line)
            if match:
                bindings_dict = result.setdefault("bindings", {})
                group = match.groupdict()
                key = group['mac_address']
                bindings_dict[key] = {
                    'mac_address': group['mac_address'],
                    'ip_address': group['ip_address'],
                    'lease_sec': int(group['lease_sec']),
                    'type': group['type'],
                    'bd': int(group['bd']),
                    'interface': group['interface'].rstrip(),
                    'anchor': group['anchor'],
                    'freeze': group['freeze'],
                }
                continue
        return result

class ShowIpDhcpSnoopingBindingStaticEvpn(ShowIpDhcpSnoopingBindingSchema):
    # Parser for 'show ip dhcp snooping binding dynamic evpn'
    # show ip dhcp snooping binding dynamic evpn
    # MacAddress         IpAddress        Lease(Sec)  Type      BD    Interface           anchor       Freeze
    # -----------------  ---------------  --------  ----------  ----  -------------      -------    -----------
    # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
    # 00:10:01:03:02:01  100.10.1.148     3278      dhcp-snoop  1001  port-channel11       YES       NONE
    # 00:10:01:05:02:01  100.10.1.101     3268      dhcp-snoop  1001  nve1(peer-id: 1)     NO        NONE
    cli_command = ['show ip dhcp snooping binding static evpn',
                   'show ip dhcp snooping binding interface {intf} static evpn', 
                   'show ip dhcp snooping binding vlan {vlan} static evpn', 
                   'show ip dhcp snooping binding interface {intf} vlan {vlan} static evpn'
                   ]

    def cli(self, intf='', vlan='', output=None):
        if (intf and vlan):
            cmd = self.cli_command[3].format(intf=intf, vlan=vlan)
        elif intf:
            cmd = self.cli_command[1].format(intf=intf)
        elif vlan:
            cmd = self.cli_command[2].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}

        # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
        p1 = re.compile(
            r'^(?P<mac_address>[0-9A-Fa-f:]+)\s+'
            r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)\s+'
            r'(?P<lease_sec>infinite)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<bd>\d+)\s+'
            r'(?P<interface>[^\s]+\s*[^\s]*)\s+'
            r'(?P<anchor>\S+)\s+'
            r'(?P<freeze>\S+)$'
        )

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
            match = p1.match(line)
            if match:
                bindings_dict = result.setdefault("bindings", {})
                group = match.groupdict()
                key = group['mac_address']
                bindings_dict[key] = {
                    'mac_address': group['mac_address'],
                    'ip_address': group['ip_address'],
                    'lease_sec': group['lease_sec'],
                    'type': group['type'],
                    'bd': int(group['bd']),
                    'interface': group['interface'].rstrip(),
                    'anchor': group['anchor'],
                    'freeze': group['freeze'],
                }
                continue

        return result

class ShowIpDhcpSnoopingBindingDynamic(ShowIpDhcpSnoopingBindingSchema):
    # Parser for 'show ip dhcp snooping binding dynamic evpn'
    # show ip dhcp snooping binding dynamic evpn
    # MacAddress         IpAddress        Lease(Sec)  Type      BD    Interface           
    # -----------------  ---------------  --------  ----------  ----  -------------      
    # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1     
    # 00:10:01:03:02:01  100.10.1.148     3278      dhcp-snoop  1001  port-channel11   
    # 00:10:01:05:02:01  100.10.1.101     3268      dhcp-snoop  1001  nve1(peer-id: 1)
    cli_command = ['show ip dhcp snooping binding dynamic',
                   'show ip dhcp snooping binding interface {intf} dynamic', 
                   'show ip dhcp snooping binding vlan {vlan} dynamic', 
                   'show ip dhcp snooping binding interface {intf} vlan {vlan} dynamic'
                   ]

    def cli(self, intf='', vlan='', output=None):
        if (intf and vlan):
            cmd = self.cli_command[3].format(intf=intf, vlan=vlan)
        elif intf:
            cmd = self.cli_command[1].format(intf=intf)
        elif vlan:
            cmd = self.cli_command[2].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}
        # 00:10:01:03:02:01  100.10.1.148     3278      dhcp-snoop  1001  port-channel11
        p1 = re.compile(
            r'^(?P<mac_address>[0-9A-Fa-f:]+)\s+'
            r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)\s+'
            r'(?P<lease_sec>\d+)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<bd>\d+)\s+'
            r'(?P<interface>[^\s]+\s*[^\s]*\(?[^\)]*\)?)\s*$'
        )

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
            match = p1.match(line)
            if match:
                bindings_dict = result.setdefault("bindings", {})
                group = match.groupdict()
                key = group['mac_address']
                bindings_dict[key] = {
                    'mac_address': group['mac_address'],
                    'ip_address': group['ip_address'],
                    'lease_sec': int(group['lease_sec']),
                    'type': group['type'],
                    'bd': int(group['bd']),
                    'interface': group['interface'].rstrip(),
                }
                continue

        return result

class ShowIpDhcpSnoopingBindingStatic(ShowIpDhcpSnoopingBindingSchema):
    # Parser for 'show ip dhcp snooping binding dynamic evpn'
    # show ip dhcp snooping binding dynamic evpn
    # MacAddress         IpAddress        Lease(Sec)  Type      BD    Interface           
    # -----------------  ---------------  --------  ----------  ----  -------------      
    # 00:10:01:01:02:01  100.10.1.104     infinite      static  1001  Ethernet1/1     
    # 00:10:01:03:02:01  100.10.1.148     infinite      static  1001  port-channel11   
    # 00:10:01:05:02:01  100.10.1.101     infinite      static  1001  nve1(peer-id: 1)
    cli_command = ['show ip dhcp snooping binding static',
                   'show ip dhcp snooping binding interface {intf} static', 
                   'show ip dhcp snooping binding vlan {vlan} static', 
                   'show ip dhcp snooping binding interface {intf} vlan {vlan} static'
                   ]

    def cli(self, intf='', vlan='', output=None):
        if (intf and vlan):
            cmd = self.cli_command[3].format(intf=intf, vlan=vlan)
        elif intf:
            cmd = self.cli_command[1].format(intf=intf)
        elif vlan:
            cmd = self.cli_command[2].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}
        # 00:10:01:05:02:01  100.10.1.101     infinite      static  1001  nve1(peer-id: 1)
        p1 = re.compile(
            r'^(?P<mac_address>[0-9A-Fa-f:]+)\s+'
            r'(?P<ip_address>\d+\.\d+\.\d+\.\d+)\s+'
            r'(?P<lease_sec>infinite)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<bd>\d+)\s+'
            r'(?P<interface>[^\s]+\s*[^\s]*\(?[^\)]*\)?)\s*$'
        )

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            # 00:10:01:01:02:01  100.10.1.104     3259      dhcp-snoop  1001  Ethernet1/1          YES       NONE
            match = p1.match(line)
            if match:
                bindings_dict = result.setdefault("bindings", {})
                group = match.groupdict()
                key = group['mac_address']
                bindings_dict[key] = {
                    'mac_address': group['mac_address'],
                    'ip_address': group['ip_address'],
                    'lease_sec': group['lease_sec'],
                    'type': group['type'],
                    'bd': int(group['bd']),
                    'interface': group['interface'].rstrip(),
                }
                continue

        return result

class ShowL2routeFhsSchema(MetaParser):
    """
    Schema for:
        * show l2route fhs all
        * show l2route fhs topology {vlan}
    """
    schema = {
        int: {  # Topology ID
            "mac_address": {
                str: {  # MAC Address
                    "host_ip": str,  # Host IP
                    "prod": str,  # Protocol
                    "flags": ListOf(str),  # Flags
                    "seq_no": int,  # Sequence Number
                    "next_hops": ListOf(str)  # List of Next-Hops
                }
            }
        }
    }

class ShowL2routeFhs(ShowL2routeFhsSchema):
    """
    Parser for:
        * show l2route fhs all
        * show l2route fhs topology {vlan}
    """
    # Flags - (Stt):Static (Dyn):Dynamic (R):Remote
    # Topo ID  Mac Address     Host IP                                 Prod          Flags      Seq No     Next-Hops
    # -------- --------------- --------------------------------------- ------------- ---------- ---------- --------------------------------------------
    # 1001     0010.0101.0201  100.10.1.104                            DHCP_DYNAMIC  Dyn,       0          Eth1/15/1
    # 1001     0010.0103.0201  100.10.1.229                            DHCP_DYNAMIC  Dyn,       0          Po11

    # Command to parse
    cli_command = ["show l2route fhs all", "show l2route fhs topology {vlan}"]

    def cli(self, vlan='', output=None):
        if vlan:
            cmd = self.cli_command[1].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}
        # 1001     0010.0101.0201  100.10.1.104                            DHCP_DYNAMIC  Dyn,       0          Eth1/15/1
        p1 = re.compile(
                r"(?P<topo_id>\d+)\s+" # 1001
                r"(?P<mac_address>[\w.]+)\s+" # 0010.0101.0201
                r"(?P<host_ip>[\d.]+)\s+" # 100.10.1.104
                r"(?P<prod>[\w_]+)\s+" # DHCP_DYNAMIC
                r"(?P<flags>[A-Za-z,]+)\s+" # Dyn
                r"(?P<seq_no>\d+)\s+" # 0
                r"(?P<next_hops>.+)" # Eth1/15/1
            )

        for line in output.splitlines():
            line = line.strip()
            # Regex to match each line
            # 1001     0010.0101.0201  100.10.1.104                            DHCP_DYNAMIC  Dyn,       0          Eth1/15/1
            match = p1.match(line)
            if match:
                groups = match.groupdict()
                topo_id = int(groups['topo_id'])
                mac_address = groups['mac_address']
                host_ip = groups['host_ip']
                prod = groups['prod']
                flags = [flag.strip() for flag in groups['flags'].split(',') if flag.strip()]
                seq_no = int(groups['seq_no'])
                next_hops = [nh.strip() for nh in groups['next_hops'].split(",")]

                # Organize parsed data into the result dictionary
                topo_dict = result.setdefault(topo_id, {}).setdefault("mac_address", {})
                topo_dict[mac_address] = {
                    "host_ip": host_ip,
                    "prod": prod,
                    "flags": flags,
                    "seq_no": seq_no,
                    "next_hops": next_hops
                }

        return result


class ShowForwardingRouteIpsgVrfSchema(MetaParser):
    """Schema for 'show forwarding route ipsg'"""
    schema = {
        'slots': {
            Any(): {
                'tables': {
                    Any(): {
                        Optional('prefixes'): {
                            Any(): {
                                'next_hop': str,
                                'interface': str,
                                Optional('labels'): str,
                                Optional('partial_install'): str,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowForwardingRouteIpsgVrf(ShowForwardingRouteIpsgVrfSchema):
    """Parser for 'show forwarding route ipsg '"""
    # slot  1
    # =======

    # IPv4 routes for table default/base

    # ------------------+-----------------------------------------+----------------------+-----------------+-----------------
    # Prefix            | Next-hop                                | Interface            | Labels          | Partial Install
    # ------------------+-----------------------------------------+----------------------+-----------------+-----------------
    # IPv4 routes for table vxlan-3001/base

    # ------------------+-----------------------------------------+----------------------+-----------------+-----------------
    # Prefix            | Next-hop                                | Interface            | Labels          | Partial Install
    # ------------------+-----------------------------------------+----------------------+-----------------+-----------------
    # 100.10.1.30/32       100.10.1.30                               port-channel11
    # 100.10.1.31/32       100.10.1.31                               port-channel11
    # 100.10.1.32/32       100.10.1.32                               port-channel11
    # 100.10.1.33/32       100.10.1.33                               port-channel11
    # 100.10.1.104/32      100.10.1.104                              Ethernet1/15/1
    # 100.10.1.108/32      100.10.1.108                              Ethernet1/15/1
    cli_command = [
        'show forwarding route ipsg vrf all',
        'show forwarding route ipsg vrf {vrf}',
        'show forwarding route ipsg max-display-count {max_count} vrf {vrf}',
        'show forwarding route ipsg module {ipsg_module} vrf all',
        'show forwarding route ipsg module {ipsg_module} vrf {vrf}',
        'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf all',
        'show forwarding route ipsg max-display-count {max_count} module {ipsg_module} vrf {vrf}',
        'show forwarding route ipsg max-display-count {max_count} vrf all'
    ]

    def cli(self, max_count='', ipsg_module='', vrf='', output=None):
        if (max_count and ipsg_module and vrf):
            cmd = self.cli_command[6].format(max_count=max_count, ipsg_module=ipsg_module, vrf=vrf)
        elif (max_count and ipsg_module):
            cmd = self.cli_command[5].format(max_count=max_count, ipsg_module=ipsg_module)
        elif (max_count and vrf):
            cmd = self.cli_command[2].format(max_count=max_count, vrf=vrf)
        elif (ipsg_module and vrf):
            cmd = self.cli_command[4].format(ipsg_module=ipsg_module, vrf=vrf)
        elif ipsg_module:
            cmd = self.cli_command[3].format(ipsg_module=ipsg_module)
        elif vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        elif max_count:
            cmd = self.cli_command[7].format(max_count=max_count)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict = {}
        # if output:
        #     parsed_dict = {'slots': {}}

        current_slot = None
        current_table = None

        # 100.10.1.30/32       100.10.1.30                               port-channel11
        prefix_pattern = re.compile(
            r"^(?P<prefix>\S+/[0-9]+)\s+"  # Match the prefix (e.g., 100.10.1.30/32), ensuring it contains '/'
            r"(?P<next_hop>\S+)\s+"        # Match the next hop (e.g., 100.10.1.30)
            r"(?P<interface>\S+)"          # Match the interface (e.g., port-channel11)
            r"(?:\s+(?P<labels>\S+))?"     # Optionally match labels (e.g., label1)
            r"(?:\s+(?P<partial_install>\S+))?"  # Optionally match partial_install (e.g., Yes)
        )

        # Slot detection (use ipsg_module as slot if "slot" is not explicitly mentioned)
        # slot  1
        pattern = re.compile(r"^slot\s+(?P<slot_num>\d+)")
        # IPv4 routes for table default/base
        table_pattern = re.compile(r"^IPv4 routes for table (?P<table_name>\S+)")
        # ---
        pref_pattern = re.compile(r'---')
        # Process each line
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Slot detection (use ipsg_module as slot if "slot" is not explicitly mentioned)
            # slot  1
            match = pattern.match(line)
            if match:
                current_slot = match.group("slot_num")
                table_dict = parsed_dict.setdefault('slots', {}).setdefault(current_slot, {'tables': {}})
                continue

            # Use ipsg_module as slot if slot is not mentioned explicitly
            if current_slot is None and ipsg_module:
                current_slot = str(ipsg_module)
                table_dict = parsed_dict.setdefault('slots', {}).setdefault(current_slot, {'tables': {}})

            # Table detection
            # IPv4 routes for table default/base
            match = table_pattern.match(line)
            if match:
                current_table = match.group("table_name")
                table_dict = parsed_dict.setdefault('slots', {}).setdefault(current_slot, {}).setdefault('tables', {}).setdefault(current_table, {'prefixes': {}})
                continue

            # ---
            if pref_pattern.match(line) or "Prefix" in line:
                continue

            # Parse routes
            # 100.10.1.30/32       100.10.1.30                               port-channel11
            match = prefix_pattern.match(line)
            if match:
                prefix_info     = match.groupdict()
                prefix          = prefix_info["prefix"]
                next_hop        = prefix_info["next_hop"]
                interface       = prefix_info["interface"]
                labels          =  prefix_info.get("labels", "") or ""  # Default to empty string if no labels
                partial_install = prefix_info.get("partial_install", "") or ""

                # Add parsed prefix data to the dictionary
                prefix_dict = parsed_dict.setdefault("slots", {}).setdefault(current_slot, {}) \
                         .setdefault("tables", {}).setdefault(current_table, {}) \
                         .setdefault("prefixes", {})
                prefix_dict[prefix] = {
                    "next_hop": next_hop,
                    "interface": interface,
                    "labels": labels,
                    "partial_install": partial_install,
                }
                continue
        return parsed_dict

class ShowIpDhcpSnoopingStatisticsSchema(MetaParser):
    """Schema for `show ip dhcp snooping statistics`."""
    schema = {
        'message_type': {
            Any(): {
                'rx': int,
                'tx': int,
                'drops': int,
            }
        },
        'totals': {
            'rx': int,
            'tx': int,
            'drops': int,
        },
        'dhcp_l2_forwarding': {
            'total_packets_forwarded': int,
            'total_packets_received': int,
            'total_packets_dropped': int,
        },
        'non_dhcp': {
            'total_packets_received': int,
            'total_packets_forwarded': int,
            'total_packets_dropped': int,
        },
        'drop': {
            'received_on_untrusted_port': int,
            'unknown_failure': int,
            'source_mac_validation_failed': int,
            'binding_entry_validation_failed': int,
            'invalid_dhcp_message_type': int,
            'interface_error': int,
            'tx_over_trusted_port_failed': int,
            'trust_port_not_configured': int,
            'vlan_validation_failure': int,
            'insertion_of_option_82_failed': int,
            'packet_malformed': int,
        }
    }

class ShowIpDhcpSnoopingStatistics(ShowIpDhcpSnoopingStatisticsSchema):
    """Parser for `show ip dhcp snooping statistics`."""

    cli_command = ['show ip dhcp snooping statistics',
                    'show ip dhcp snooping statistics vlan {vlan}'
                ]

    def cli(self, vlan='', output=None):
        if vlan:
            cmd = self.cli_command[1].format(vlan=vlan)
        else:
            cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(cmd)

        # Initialize result dictionary
        result = {}
        
        # Regex patterns for parsing
        # Discover             114618          114618               0
        # Offer                     4               4               0
        # Request                 772             772               0
        # Ack                     392             392               0
        # Release                   0               0               0
        # Decline                   0               0               0
        # Inform                    0               0               0
        # Nack                      0               0               0
        
        p1 = re.compile(
                    r'^(?!Total\s)(?P<message_type>\S+)\s+(?P<rx>\d+)\s+(?P<tx>\d+)\s+(?P<drops>\d+)$'
        )
        # Total                115786          115786               0
        p2 = re.compile(
            r'^Total\s+(?P<rx>\d+)\s+(?P<tx>\d+)\s+(?P<drops>\d+)$'
        )
        # DHCP L2 Forwarding:
        # Total Packets Forwarded                          :         0
        # Total Packets Received                           :         0
        # Total Packets Dropped                            :         0
        p3 = re.compile(
            r'^(?P<key>[\w\s]+):\s+(?P<value>\d+)$'
        )
        # DHCP L2 Forwarding:
        p_dhcp_l2_forwarding = re.compile(r'.*DHCP L2 Forwarding:.*')
        # Non DHCP:
        p_non_dhcp = re.compile(r'.*Non DHCP:.*')
        # DROP:
        p_drop = re.compile(r'.*DROP:.*')

        section_dict = None

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('-'):
                continue

            # Match Message Type stats
            # Discover             114618          114618               0
            # Offer                     4               4               0
            # Request                 772             772               0
            # Ack                     392             392               0
            # Release                   0               0               0
            # Decline                   0               0               0
            # Inform                    0               0               0
            # Nack                      0               0               0
            m = p1.match(line)
            if m:
                message_dict = result.setdefault("message_type", {})
                group = m.groupdict()
                result['message_type'][group['message_type'].lower()] = {
                    'rx': int(group['rx']),
                    'tx': int(group['tx']),
                    'drops': int(group['drops']),
                }
                continue
            
            # Total                115786          115786               0
            m1 = p2.match(line)
            if m1:
                group = m1.groupdict()
                # result.setdefault('totals', {})
                result['totals'] = {
                    'rx': int(group['rx']),
                    'tx': int(group['tx']),
                    'drops': int(group['drops']),
                }
                continue
            
            # DHCP L2 Forwarding:
            if p_dhcp_l2_forwarding.match(line):
                section_dict = result.setdefault('dhcp_l2_forwarding', {})
                continue
            
            # Non DHCP:
            elif p_non_dhcp.match(line):
                section_dict = result.setdefault('non_dhcp', {})
                continue
            
            # DROP:
            elif p_drop.match(line):
                section_dict = result.setdefault('drop', {})
                continue
                
            # Match any of the line below:
            # DHCP L2 Forwarding:
            # Total Packets Forwarded                          :         0
            # Total Packets Received                           :         0
            # Total Packets Dropped                            :         0
            # Non DHCP:
            # Total Packets Received                           :         0
            # Total Packets Forwarded                          :         0
            # Total Packets Dropped                            :         0
            # DROP:
            # Received on untrusted port                       :         0
            # Unknown Failure                                  :         0
            # Source mac validation failed                     :         0
            # Binding entry validation Failed                  :         0
            # Invalid DHCP message type                        :         0
            # Interface error                                  :         0
            # Tx over trusted port failed                      :         0
            # Trust port not configured                        :         0
            # Vlan validation failure                          :         0
            # Insertion of option 82 failed                    :         0
            # Packet Malformed                                 :         0
            if section_dict is not None and (m := p3.match(line)):
                group = m.groupdict()
                key = group['key'].strip().replace(' ', '_').lower()
                section_dict[key] = int(group['value'])
                continue

        return result

class ShowIpDhcpRelayStatisticsInterfaceVlanSchema(MetaParser):
    """Schema for show ip dhcp relay statistics interface vlan <vlan>"""
    
    schema = {
        'message_types': {
            str: {'rx': int, 'tx': int, 'drops': int}
        },
        'dhcp_server_stats': {
            'servers': ListOf({
                'server': str,
                Optional('vrf'): str,
                'request': int,
                'response': int,
            })
        },
        'dhcp_l3_fwd_stats': {
            'total_packets_received': int,
            'total_packets_forwarded': int,
            'total_packets_dropped': int
        },
        'non_dhcp_drop_stats': {
            'total_packets_received': int,
            'total_packets_forwarded': int,
            'total_packets_dropped': int
        },
        'dhcp_drop_stats': {
            'dhcp_relay_not_enabled': int,
            'invalid_dhcp_message_type': int,
            'interface_error': int,
            'tx_failure_towards_server': int,
            'tx_failure_towards_client': int,
            'unknown_output_interface': int,
            'unknown_vrf_or_interface_for_server': int,
            'max_hops_exceeded': int,
            'option_82_validation_failed': int,
            'packet_malformed': int,
            'dhcp_request_dropped_on_mct': int,
            'relay_trusted_port_not_configured': int
        }
    }

class ShowIpDhcpRelayStatisticsInterfaceVlan(ShowIpDhcpRelayStatisticsInterfaceVlanSchema):
    """Parser for show ip dhcp relay statistics interface vlan <vlan>"""

    cli_command = 'show ip dhcp relay statistics interface vlan {vlan}'

    def cli(self, vlan='', output=None):
        if output is None:
            # Execute command on the device
            output = self.device.execute(self.cli_command.format(vlan=vlan))

        parsed_data = {}
        current_section = None
    
        # Discover                 16              16               0
        # Offer                    16              16               0
        # Request(*)              322             322               0
        # Ack                     322             322               0
        # Release(*)               18              18               0
        # Decline                   0               0               0
        # Inform(*)                 0               0               0
        # Nack                      0               0               0
        # Total                   694             694               0
        message_regex = re.compile(
            r"^(?P<message_type>Discover|Offer|Request\(\*\)|Ack|Release\(\*\)|Decline|Inform\(\*\)|Nack|Total)\s+"
            r"(?P<rx>\d+)\s+(?P<tx>\d+)\s+(?P<drops>\d+)$"
        )
        # 192.0.2.42                                               356            338
        server_stats_regex = re.compile(
            r"^(?P<server_ip>\d{1,3}(?:\.\d{1,3}){3})\s+(?P<vrf>\S+|\s*)?\s+(?P<request>\d+)\s+(?P<response>\d+)$"
        )
        # Total Packets Received                           :         0
        generic_stats_regex = re.compile(
            r"^(?P<field>[\w\s\-]+):\s+(?P<value>\d+)$"
        )
        
        # Matches - DHCPv6 Server stats:
        server_stats_flag_regex = re.compile(r"^DHCP server stats:")
        # Matches - DHCP L3 FWD:
        dhcp_l3_fwd_flag_regex = re.compile(r"^DHCP L3 FWD:")
        # Matches - Non DHCP:
        non_dhcp_drop_flag_regex = re.compile(r"^Non DHCP:")
        # matches - DROPS:
        dhcp_drop_flag_regex = re.compile(r"^DROP:")

        # This will match dhcp message tx/rx/drop count, match below        
        for line in output.splitlines():
            # Discover                 16              16               0
            match = message_regex.match(line.strip())
            if match:
                group = match.groupdict()
                message_type = (group['message_type']).lower().replace("(*)", "").strip()
                
                message_types = parsed_data.setdefault('message_types', {})

                message_types[message_type] = {
                    'rx': int(group['rx']),
                    'tx': int(group['tx']),
                    'drops': int(group['drops'])
                }
                continue
            
            # Matches - DHCPv6 Server stats:
            if server_stats_flag_regex.match(line):
                current_section = "dhcp_server_stats"
                parsed_data.setdefault(current_section, {"servers": []})
                continue

            # Matches - DHCP L3 FWD:
            elif dhcp_l3_fwd_flag_regex.match(line):
                current_section = "dhcp_l3_fwd_stats"
                parsed_data.setdefault(current_section, {})
                continue

            # Non DHCP:
            elif non_dhcp_drop_flag_regex.match(line):
                current_section = "non_dhcp_drop_stats"
                parsed_data.setdefault(current_section, {})
                continue

            # matches - DROPS:
            elif dhcp_drop_flag_regex.match(line):
                current_section = "dhcp_drop_stats"
                parsed_data.setdefault(current_section, {})
                continue

            # Parse server stats
            if current_section == "dhcp_server_stats":
                # Matches below server stats
                # 192.0.2.42                                               356            338
                match = server_stats_regex.match(line)
                if match:
                    parsed_data[current_section]["servers"].append({
                        "server": match.group("server_ip"),
                        "vrf": match.group("vrf").strip() if match.group("vrf") else '',
                        "request": int(match.group("request")),
                        "response": int(match.group("response")),
                    })
                continue

            # Parse generic stats (DHCP L3 FWD, Non DHCP, and DROP)
            # Parse below:
                # DHCP L3 FWD:
                # Total Packets Received                           :         0
                # Total Packets Forwarded                          :         0
                # Total Packets Dropped                            :         0
                # Non DHCP:
                # Total Packets Received                           :         0
                # Total Packets Forwarded                          :         0
                # Total Packets Dropped                            :         0
                # DROP:
                # DHCP Relay not enabled                           :         0
                # Invalid DHCP message type                        :         0
                # Interface error                                  :         0
                # Tx failure towards server                        :         0
                # Tx failure towards client                        :         0
                # Unknown output interface                         :         0
                # Unknown vrf or interface for server              :         0
                # Max hops exceeded                                :         0
                # Option 82 validation failed                      :         0
                # Packet Malformed                                 :         0
                # DHCP Request dropped on MCT                      :         0
                # Relay Trusted port not configured                :         0
            match = generic_stats_regex.match(line)
            if match and current_section:
                parsed_data[current_section][
                    match.group("field").lower().strip().replace(" ", "_").replace("-", "_")
                ] = int(match.group("value"))

        return parsed_data

class ShowIpv6DhcpRelayStatisticsInterfaceVlanSchema(MetaParser):
    schema = {
        'message_types': {
            str: {'rx': int, 'tx': int, 'drops': int}
        },
        'server_stats': {
            'relay_address': str,
            Optional('vrf_name'): str,
            Optional('destination_interface'): str,
            'request': int,
            'response': int
        },
        'drops': {
            'dhcpv6_relay_is_disabled': int,
            'max_hops_exceeded': int,
            'packet_validation_fails': int,
            'unknown_output_interface': int,
            'invalid_vrf': int,
            'option_insertion_failed': int,
            'direct_replies': int,
            'ipv6_addr_not_configured': int,
            'interface_error': int,
            'vpn_option_disabled': int,
            'ipv6_extn_headers_present': int,
            'dhcp_request_dropped_on_mct': int
        }
    }

# Parser Implementation
class ShowIpv6DhcpRelayStatisticsInterfaceVlan(ShowIpv6DhcpRelayStatisticsInterfaceVlanSchema):
    cli_command = 'show ipv6 dhcp relay statistics interface vlan {vlan}'

    def cli(self, vlan='', output=None):
        if output is None:
            # Execute command on the device
            output = self.device.execute(self.cli_command.format(vlan=vlan))

        result = {}        
        current_section = None  # Keeps track of the current section

        # Patterns for parsing each section
        # Message Type                           Rx              Tx           Drops
        # -------------------------------------------------------------------------
        # SOLICIT                                40               0               0
        # ADVERTISE                               0              40               0
        # REQUEST                                40               0               0
        # CONFIRM                                 0               0               0
        # RENEW                                  20               0               0
        # REBIND                                  0               0               0
        # REPLY                                   0              90               0
        # RELEASE                                30               0               0
        # DECLINE                                 0               0               0
        # RECONFIGURE                             0               0               0
        # INFORMATION_REQUEST                     0               0               0
        # RELAY_FWD                               0             130               0
        # RELAY_REPLY                           130               0               0
        # UNKNOWN                                 0               0               0
        message_pattern = re.compile(
            r'^(?P<message_type>[A-Z_]+)\s+(?P<rx>\d+)\s+(?P<tx>\d+)\s+(?P<drops>\d+)$'
        )
        # 192:0:2::42               ---                  ---               130        130
        server_stats_pattern = re.compile(
            r'^(?P<relay_address>[0-9a-fA-F:]+)\s+(?P<vrf_name>\S*)\s+(?P<dest_interface>\S+)\s+(?P<request>\d+)\s+(?P<response>\d+)$'
        )
        # DHCPv6 Relay is disabled                     :   0
        drops_pattern = re.compile(
    r'^(?:Direct Replies \(Recnfg/Adv/Reply\) from server:\s+(?P<direct_replies>\d+)|(?P<key>.+?):\s+(?P<value>\d+))$'
)
        # Total                                 260             260               0
        total_pattern = re.compile(
                    r'^Total\s+(?P<rx>\d+)\s+(?P<tx>\d+)\s+(?P<drops>\d+)$'
                )
        # DHCPv6 Server stats:
        server_stats_flag = re.compile(r"^DHCPv6 Server stats:")
        # DROPS:
        drop_flag = re.compile(r"^DROPS:")

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Parsing message statistics
            # SOLICIT                                40               0               0
            m = message_pattern.match(line)
            if m:

                group = m.groupdict()
                message_type = (group['message_type']).rstrip().lower().replace(' ', '_')
                
                message_types = result.setdefault('message_types', {})

                message_types[message_type] = {
                    'rx': int(group['rx']),
                    'tx': int(group['tx']),
                    'drops': int(group['drops'])
                }
                continue
            
            # Total                                 260             260               0    
            total_match = total_pattern.match(line)
            if total_match:
                total_group = total_match.groupdict()
                result.setdefault("message_types", {}).setdefault("total", {
                    "rx": int(total_group["rx"]),
                    "tx": int(total_group["tx"]),
                    "drops": int(total_group["drops"])
                })
            
            # Start parsing server stats
            # DHCPv6 Server stats:
            if server_stats_flag.match(line):
                current_section = "server_stats"
                result.setdefault("server_stats", {})
                continue
            
            # Drops:
            if drop_flag.match(line):
                current_section = "drops"
                result.setdefault("drops", {})
                continue
            
            if current_section == "server_stats":
                # 192:0:2::42               ---                  ---               130        130
                m = server_stats_pattern.match(line)                
                if m:
                    group = m.groupdict()
                    vrf_name = group['vrf_name'].strip()
                    destination_interface = group['dest_interface'].strip()
                    server_stats = {
                        'relay_address': group['relay_address'],
                        'request': int(group['request']),
                        'response': int(group['response'])
                    }
                    
                    if vrf_name and vrf_name != "---":
                        server_stats['vrf_name'] = vrf_name
                    if destination_interface and destination_interface != "---":
                        server_stats['destination_interface'] = destination_interface
                    result['server_stats'] = server_stats
                continue

            if current_section == "drops":
                # Match one of below:
                # DHCPv6 Relay is disabled                     :   0
                # Max hops exceeded                            :   0
                # Packet validation fails                      :   0
                # Unknown output interface                     :   0
                # Invalid VRF                                  :   0
                # Option insertion failed                      :   0
                # Direct Replies (Recnfg/Adv/Reply) from server:   0
                # IPv6 addr not configured                     :   0
                # Interface error                              :   0
                # VPN Option Disabled                          :   0
                # IPv6 extn headers present                    :   0
                # DHCP Request dropped on MCT                  :   0
                m = drops_pattern.match(line)
                if m:
                    result.setdefault("drops", {})
                    if m.group("direct_replies"):
                        result["drops"]["direct_replies"] = int(m.group("direct_replies"))
                    else:
                        key = (
                            m.group("key")
                            .strip()
                            .lower()
                            .replace(" ", "_")
                            .replace("(", "")
                            .replace(")", "")
                        )
                        result["drops"][key] = int(m.group("value"))

        return result
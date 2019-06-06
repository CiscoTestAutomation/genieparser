''' show_interface_summary.py

ASA parserr for the following show commands:
    * show interface summary
    * show interface ip brief
    * show interface details
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Schema for 'show interface summary'
# =============================================
class ShowInterfaceSummarySchema(MetaParser):
    """Schema for
        * show interface summary
    """

    schema = {
        'interfaces': {
            Any(): {
                'oper_status': str,
                'protocol_status': str,
                Optional('name'): str,
                Optional('mac_address'): str,
                Optional('mtu'): int,
                Optional('ip_address'): str,
                Optional('subnet'): str,
                Optional('interface_state'): bool,
                Optional('config_status'): bool,
                Optional('config_issue'): str
            },
        }
    }

# =============================================
# Parser for 'show interface summary'
# =============================================
class ShowInterfaceSummary(ShowInterfaceSummarySchema):
    """Parser for
        * show interface summary
    """

    cli_command = 'show interface summary'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Interface Vlan1000 "pod100", is up, line protocol is up
        p1 = re.compile(r'^Interface +(?P<interface>\w+) +"(?P<name>[\w\-\+\/\_]*)"'
            ', +is +(?P<oper_status>up|down), +line +protocol +is '
            '+(?P<protocol_status>up|down)$')

        # MAC address 286f.7fb1.032c, MTU 1500
        p2 = re.compile(r'^MAC address +(?P<mac_address>[\w\.]+), +MTU +(?P<mtu>\d+)$')

        # IP address 172.16.100.251, subnet mask 255.255.255.0
        p3 = re.compile(r'^IP +address +(?P<ip_address>[\w\.]+), +subnet +mask '
            '+(?P<subnet>[\w\.]+)$')

        p4 = re.compile(r'^(?P<interface_state>Available) +but '
            '+(?P<config_status>not +configured) +via '
            '+(?P<config_issue>[\w\-\+\/\_]*)$')

        for line in out.splitlines():
            line = line.strip()

            # Interface Vlan1000 "pod100", is up, line protocol is up
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interface']
                instance_dict = ret_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                instance_dict.update({'name': groups['name']})
                instance_dict.update({'oper_status': groups['oper_status']})
                instance_dict.update(
                    {'protocol_status': groups['protocol_status']})
                if groups['name'] != '' \
                and groups['oper_status'] == 'up' \
                and groups['protocol_status'] == 'up':
                    instance_dict.update({'interface_state': True, \
                        'config_status': True})
                if groups['name'] != '' \
                and groups['oper_status'] == 'down' \
                and groups['protocol_status'] == 'down':
                    instance_dict.update({'interface_state': False, \
                        'config_status': True})
                if groups['name'] == '' \
                and groups['oper_status'] == 'down' \
                and groups['protocol_status'] == 'down':
                    instance_dict.update({'interface_state': False, \
                        'config_status': False})
                continue

            # MAC address 286f.7fb1.032c, MTU 1500
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'mac_address': groups['mac_address']})
                instance_dict.update({'mtu': int(groups['mtu'])})
                continue

            # IP address 172.16.100.251, subnet mask 255.255.255.0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'ip_address': groups['ip_address']})
                instance_dict.update({'subnet': groups['subnet']})
                continue

              # Available but not configured via nameif
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if groups['interface_state'] == 'Available' \
                and groups['config_status'] == 'not configured':
                    instance_dict.update({'interface_state': True})
                    instance_dict.update({'config_status': False})
                    instance_dict.update({'config_issue': groups['config_issue']})
                continue

        return ret_dict

# =============================================
# Schema for 'show interface ip brief'
# =============================================
class ShowInterfaceIpBriefSchema(MetaParser):
    """Schema for
        * show interface ip brief
    """

    schema = {
        'interfaces': {
            Any(): {
                    Optional('ip_address'): str,
                    Optional('check'): str,
                    Optional('method'): str,
                    Optional('oper_status'): str,
                    Optional('protocol_status'): str
                    },
                }
            }

# =============================================
# Parser for 'show interface ip brief'
# =============================================
class ShowInterfaceIpBrief(ShowInterfaceIpBriefSchema):
    """Parser for
        * show interface ip brief
    """

    cli_command = 'show interface ip brief'
    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Vlan1000                   172.16.100.251  YES CONFIG up                    up
        p1 = re.compile(r'^(?P<interface>\w+) +(?P<ip_address>[\w\.]+) '
            '+(?P<check>\w+) +(?P<method>\w+) +(?P<oper_status>up|down) '
            '+(?P<protocol_status>up|down)$')

        for line in out.splitlines():
            line = line.strip()

            # Interface Vlan1000 "pod100", is up, line protocol is up
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interface']
                instance_dict = ret_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                instance_dict.update({'ip_address': groups['ip_address']})
                instance_dict.update({'check': groups['check']})
                instance_dict.update({'method': groups['method']})
                instance_dict.update({'oper_status': groups['oper_status']})
                instance_dict.update({'protocol_status': groups['protocol_status']})
                continue

        return ret_dict

# =============================================
# Schema for 'show interface detail'
# =============================================
class ShowInterfaceDetailSchema(MetaParser):
    """Schema for
        * show interface detail
    """

    schema = {
        'interfaces': {
            Any(): {
                'oper_status': str,
                'protocol_status': str,
                Optional('name'): str,
                Optional('mac_address'): str,
                Optional('mtu'): int,
                Optional('ip_address'): str,
                Optional('subnet'): str,
                Optional('interface_state'): bool,
                Optional('config_status'): bool,
                Optional('config_issue'): str,
                Optional('traffic_input_packets'): int,
                Optional('traffic_input_bytes'): int,
                Optional('traffic_output_packets'): int,
                Optional('traffic_output_bytes'): int,
                Optional('traffic_dropped_packets'): int,
                Optional('interface_number'): int,
                Optional('vlan_config'): bool,
                Optional('vlan_state'): str
            },
        }
    }

# =============================================
# Parser for 'show interface detail'
# =============================================
class ShowInterfaceDetail(ShowInterfaceDetailSchema):
    """Parser for
        * show interface detail
    """

    cli_command = 'show interface detail'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Interface Vlan1000 "pod100", is up, line protocol is up
        p1 = re.compile(r'^Interface +(?P<interface>\w+) +"(?P<name>[\w\-\+\/\_]*)", +is '
            '+(?P<oper_status>up|down), +line +protocol +is '
            '+(?P<protocol_status>up|down)$')

        # MAC address 286f.7fb1.032c, MTU 1500
        p2 = re.compile(r'^MAC address +(?P<mac_address>[\w\.]+), +MTU +(?P<mtu>\d+)$')

        # IP address 172.16.100.251, subnet mask 255.255.255.0
        p3 = re.compile(r'^IP +address +(?P<ip_address>[\w\.]+), +subnet +mask '
            '+(?P<subnet>[\w\.]+)$')

        p4 = re.compile(r'^(?P<interface_state>Available) +but '
            '+(?P<config_status>not +configured) +via '
            '+(?P<config_issue>[\w\-\+\/\_]*)$')

        p5 = re.compile(r'^(?P<traffic_input_packets>[\d]+) +packets +input, '
            '+(?P<traffic_input_bytes>[\d]+) +bytes$')

        p6 = re.compile(r'^(?P<traffic_output_packets>[\d]+) +packets +output, '
            '+(?P<traffic_output_bytes>[\d]+) +bytes$')

        p7 = re.compile(r'^(?P<traffic_dropped_packets>[\d]+) +packets +dropped$')

        p8 = re.compile(r'^Interface +number +is +(?P<interface_number>[\d]+)$')

        p9 = re.compile(r'^Interface +vlan +config +status +is '
            '+(?P<vlan_config>not +active|active)$')

        p10 = re.compile(r'^Interface +vlan +state +is +(?P<vlan_state>UP|DOWN)'
            '+([\w\(\)down in system space]+)?$')

        for line in out.splitlines():
            line = line.strip()

            # Interface Vlan1000 "pod100", is up, line protocol is up
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interface']
                instance_dict = ret_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                instance_dict.update({'name': groups['name']})
                instance_dict.update({'oper_status': groups['oper_status']})
                instance_dict.update(
                    {'protocol_status': groups['protocol_status']})
                if groups['name'] != '' \
                and groups['oper_status'] == 'up' \
                and groups['protocol_status'] == 'up':
                    instance_dict.update({'interface_state': True, \
                        'config_status': True})
                if groups['name'] != '' \
                and groups['oper_status'] == 'down' \
                and groups['protocol_status'] == 'down':
                    instance_dict.update({'interface_state': False, \
                        'config_status': True})
                if groups['name'] == '' \
                and groups['oper_status'] == 'down' \
                and groups['protocol_status'] == 'down':
                    instance_dict.update({'interface_state': False, \
                        'config_status': False})
                continue

            # MAC address 286f.7fb1.032c, MTU 1500
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'mac_address': groups['mac_address']})
                instance_dict.update({'mtu': int(groups['mtu'])})
                continue

            # IP address 172.16.100.251, subnet mask 255.255.255.0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'ip_address': groups['ip_address']})
                instance_dict.update({'subnet': groups['subnet']})
                continue

            # Available but not configured via nameif
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if groups['interface_state'] == 'Available' \
                and groups['config_status'] == 'not configured':
                    instance_dict.update({'interface_state': True})
                    instance_dict.update({'config_status': False})
                    instance_dict.update({'config_issue': groups['config_issue']})
                continue

            # 16863445 packets input, 10312133394 bytes
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'traffic_input_packets': \
                    int(groups['traffic_input_packets'])})
                instance_dict.update({'traffic_input_bytes': \
                    int(groups['traffic_input_bytes'])})
                continue

            # 10475426 packets output, 5376026271 bytes
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'traffic_output_packets': \
                    int(groups['traffic_output_packets'])})
                instance_dict.update({'traffic_output_bytes': \
                    int(groups['traffic_output_bytes'])})
                continue

            # 2551519 packets dropped
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'traffic_dropped_packets': \
                    int(groups['traffic_dropped_packets'])})
                continue

            # Interface number is 756
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'interface_number': \
                    int(groups['interface_number'])})
                continue

            # Interface vlan config status is active
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                if groups['vlan_config'] == 'active':
                    instance_dict.update({'vlan_config': True})
                else:
                    instance_dict.update({'vlan_config': False})
                continue

            # Interface vlan state is UP
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'vlan_state': groups['vlan_state']})
                continue

        return ret_dict
"""show_dhcp.py

CHEETAH parsers for the following show commands:

    * show ip dhcp lease

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf


class ShowIpDhcpLeaseSchema(MetaParser):
    """Schema for show ip dhcp lease."""

    schema = {
        'interfaces': {
            Any(): {
                'lease_server': str,
                'leases': ListOf({
                    'vlan': int,
                    'added_by': str,
                    'active': bool,
                    'state': str,
                    'disc_ago': int,
                    'offer_ago': int,
                    'req_ago': int,
                    'ack_delay': float,
                    'renew_at': int,
                    'exp_at': int,
                    'ip': str,
                    'gw': str,
                    'bcast': str,
                    'dns': str,
                    'mtu': int,
                })
            }
        }
    }


class ShowIpDhcpLease(ShowIpDhcpLeaseSchema):
    """Parser for show ip dhcp lease."""

    cli_command = 'show ip dhcp lease'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        interface_dict = None
        pending_lease = None

        # Interface wired0
        p1 = re.compile(r'^Interface\s+(?P<interface>[\w.-]+)$')

        # DHCP lease server: 192.0.2.1
        p2 = re.compile(
            r'^DHCP lease server:\s+'
            r'(?P<lease_server>(?:\d{1,3}\.){3}\d{1,3})$'
        )

        # 0 C true bound 120 118 60 0.0012 30 90
        # 0 C true bound 120 118 60 0.0012 30 90 192.0.2.196/24 192.0.2.1 192.0.2.255 0.0.0.0 0
        p3 = re.compile(
            r'^(?P<vlan>\d+)\s+(?P<added_by>[A-Za-z]+)\s+'
            r'(?P<active>true|false)\s+(?P<state>[A-Za-z]+)\s+'
            r'(?P<disc_ago>\d+)\s+(?P<offer_ago>\d+)\s+'
            r'(?P<req_ago>\d+)\s+(?P<ack_delay>\d+(?:\.\d+)?)\s+'
            r'(?P<renew_at>\d+)\s+(?P<exp_at>\d+)'
            r'(?:\s+(?P<ip>(?:\d{1,3}\.){3}\d{1,3}/\d+)\s+'
            r'(?P<gw>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<bcast>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<dns>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<mtu>\d+))?$'
        )

        # 192.0.2.196/24 192.0.2.1 192.0.2.255 0.0.0.0 0
        p4 = re.compile(
            r'^(?P<ip>(?:\d{1,3}\.){3}\d{1,3}/\d+)\s+'
            r'(?P<gw>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<bcast>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<dns>(?:\d{1,3}\.){3}\d{1,3})\s+'
            r'(?P<mtu>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Interface wired0
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(
                    interface, {'leases': []}
                )
                pending_lease = None
                continue

            # DHCP lease server: 192.0.2.1
            m = p2.match(line)
            if m and interface_dict is not None:
                interface_dict['lease_server'] = m.groupdict()['lease_server']
                continue

            # 0 C true bound 120 118 60 0.0012 30 90
            # 0 C true bound 120 118 60 0.0012 30 90 192.0.2.196/24 192.0.2.1 192.0.2.255 0.0.0.0 0
            m = p3.match(line)
            if m and interface_dict is not None:
                groups = m.groupdict()
                pending_lease = {
                    'vlan': int(groups['vlan']),
                    'added_by': groups['added_by'],
                    'active': groups['active'] == 'true',
                    'state': groups['state'],
                    'disc_ago': int(groups['disc_ago']),
                    'offer_ago': int(groups['offer_ago']),
                    'req_ago': int(groups['req_ago']),
                    'ack_delay': float(groups['ack_delay']),
                    'renew_at': int(groups['renew_at']),
                    'exp_at': int(groups['exp_at']),
                }
                if groups['ip'] is not None:
                    pending_lease.update({
                        'ip': groups['ip'],
                        'gw': groups['gw'],
                        'bcast': groups['bcast'],
                        'dns': groups['dns'],
                        'mtu': int(groups['mtu']),
                    })
                    interface_dict['leases'].append(pending_lease)
                    pending_lease = None
                continue

            # 192.0.2.196/24 192.0.2.1 192.0.2.255 0.0.0.0 0
            m = p4.match(line)
            if m and interface_dict is not None and pending_lease is not None:
                groups = m.groupdict()
                pending_lease.update({
                    'ip': groups['ip'],
                    'gw': groups['gw'],
                    'bcast': groups['bcast'],
                    'dns': groups['dns'],
                    'mtu': int(groups['mtu']),
                })
                interface_dict['leases'].append(pending_lease)
                pending_lease = None

        return ret_dict

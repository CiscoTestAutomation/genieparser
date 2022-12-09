"""display_bgp.py

HVPR parsers for the following display commands:
    * 'display bgp {address_family} all peer {peer_address} verbose'
    * 'display bgp {address_family} all peer verbose'
    * 'display bgp {address_family} peer verbose'
    * 'display bgp {address_family} peer {peer_address} verbose'
    * 'display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose'
    * 'display bgp {address_family} vpn-instance {vrf} peer verbose'
    * 'display bgp all summary'
    * 'display bgp {address_family} vpn-instance {vrf} peer'
    * 'display bgp {address_family} all peer'
    * 'display bgp {address_family} peer'
    * 'display bgp peer'
    """

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (
    Any,
    Optional
)
# Logger
logger = logging.getLogger(__name__)


class DisplayBgpPeerSchema(MetaParser):
    """Schema for:
        'display bgp all summary'
        'display bgp {address_family} vpn-instance {vrf} peer'
        'display bgp {address_family} all peer'
        'display bgp {address_family} peer'
        'display bgp peer'
    """

    schema = {
        "local_router_id": str,
        "local_as": str,
        Optional("vrf"): {
            Any(): {
                Optional("address_family"): {
                    Any(): {
                        Optional("peer"): {
                            Any(): {
                                "remote_as": str,
                                "total_messages": {
                                    "sent": int,
                                    "received": int,
                                },
                                Optional("bgp_version"): int,
                                "out_queue": int,
                                "up_down_time": str,
                                "state": str,
                                "prefixes_counters": {
                                    "received": int,
                                    Optional("advertised"): int
                                },
                            }
                        }
                    },
                },
            },
        },
    }


class DisplayBgpPeer(DisplayBgpPeerSchema):
    """Parser for:
        'display bgp {address_family} vpn-instance {vrf} peer'
        'display bgp {address_family} all peer'
        'display bgp {address_family} peer'
        'display bgp peer'
    """
    cli_command = ['display bgp {address_family} {vrf_type} peer',
                   'display bgp {address_family} vpn-instance {vrf} peer',
                   'display bgp {address_family} peer',
                   'display bgp peer']

    def cli(self, address_family='ipv4', vrf='default', vrf_type='', output=None):

        if output is None:
            if vrf != "default":
                command = self.cli_command[1].format(address_family=address_family,vrf=vrf)
            elif vrf_type:
                command = self.cli_command[0].format(address_family=address_family, vrf_type=vrf_type)
            elif address_family == 'ipv4':
                command = self.cli_command[3]
            else:
                command = self.cli_command[2].format(address_family=address_family)
            logger.debug(f"Executing command: {command}")
            out = self.device.execute(command)
        else:
            out = output

        ret_dict = {}

        # BGP local router ID : 3.3.3.3
        p1 = re.compile(r'^BGP local router ID : (?P<local_router_id>[a-zA-Z0-9.:]+)$')

        # Local AS number : 64666
        p2 = re.compile(r'^Local AS number : (?P<local_as>[0-9.]+)$')

        # Address Family:Ipv4 Unicast
        p3 = re.compile(r'^Address Family:(?P<address_family>.+)$')

        # Peer of IPv4-family for vpn instance :
        p4 = re.compile(r'^Peer of (?P<address_family>\S+) for vpn instance :$')

        # VPN-Instance mobile, Router ID 1.1.1.1:
        p5 = re.compile(r'^VPN-Instance (?P<vrf>\S+), Router ID [a-zA-Z0-9.:]+:$')

        # 10.10.10.10                              65000        0        0     0 1272h18m     Connect        0        0
        # 20.20.20.20                              65000   232782   279631     0 0646h36m Established        1        7
        p6 = re.compile(r'^(?P<peer_address>[a-zA-Z0-9.:]+)\s+(?P<remote_as>[0-9.]+)\s+(?P<messages_received>\d+)\s+'
                        r'(?P<messages_sent>\d+)\s+(?P<out_queue>\d+)\s+(?P<up_down_time>\S+)\s+(?P<state>\S+)\s+(?P<prefixes_received>\d+)\s+(?P<prefixes_advertised>\d+)$')

        # 5.5.5.5                          4       65000        0        0     0 00:08:50     Connect        0
        # 172.16.100.1                     4       65000       46       60     0 00:07:09 Established        1
        p7 = re.compile(
            r'^(?P<peer_address>[a-zA-Z0-9.:]+)\s+(?P<bgp_version>\d+)\s+(?P<remote_as>[0-9.]+)\s+(?P<messages_received>\d+)\s+'
            r'(?P<messages_sent>\d+)\s+(?P<out_queue>\d+)\s+(?P<up_down_time>\S+)\s+(?P<state>\S+)\s+(?P<prefixes_received>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # BGP local router ID : 3.3.3.3
            m = p1.match(line)
            if m:
                local_router_id = m.groupdict()['local_router_id']
                ret_dict['local_router_id'] = local_router_id
                continue

            # Local AS number : 64666
            m = p2.match(line)
            if m:
                local_as = m.groupdict()['local_as']
                ret_dict['local_as'] = local_as
                continue

            # Address Family:Ipv4 Unicast
            m = p3.match(line)
            if m:
                address_family = m.groupdict()['address_family']
                address_family_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',
                                                                                                    {})
                address_family_dict = address_family_dict.setdefault(address_family.lower(), {})
                continue
            # Peer of IPv4-family for vpn instance :
            m = p4.match(line)
            if m:
                address_family = m.groupdict()['address_family']
                if address_family.lower() == 'ipv4-family':
                    address_family = 'ipv4 unicast'
                elif address_family.lower() == 'ipv6-family':
                    address_family = 'ipv6 unicast'
                address_family_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{})
                continue

            # VPN-Instance mobile, Router ID 1.1.1.1:
            m = p5.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})
                address_family_dict = vrf_dict.setdefault('address_family', {}).setdefault(address_family.lower(), {})
                continue

            # 10.10.10.10                              65000        0        0     0 1272h18m     Connect        0        0
            # 20.20.20.20                              65000   232782   279631     0 0646h36m Established        1        7
            m = p6.match(line)
            if m:
                peer_address = m.groupdict()['peer_address']
                remote_as = m.groupdict()['remote_as']
                messages_received = m.groupdict()['messages_received']
                messages_sent = m.groupdict()['messages_sent']
                out_queue = m.groupdict()['out_queue']
                up_down_time = m.groupdict()['up_down_time']
                state = m.groupdict()['state']
                prefixes_received = m.groupdict()['prefixes_received']
                prefixes_advertised = m.groupdict()['prefixes_advertised']
                address_family_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',
                                                                                                    {})
                address_family_dict = address_family_dict.setdefault(address_family.lower(), {})
                peer_dict = address_family_dict.setdefault('peer', {}).setdefault(peer_address, {})
                peer_dict['remote_as'] = remote_as
                messages_dict = peer_dict.setdefault('total_messages', {})
                messages_dict['received'] = int(messages_received)
                messages_dict['sent'] = int(messages_sent)
                peer_dict['out_queue'] = int(out_queue)
                peer_dict['up_down_time'] = up_down_time
                peer_dict['state'] = state
                prefixes_counters_dict = peer_dict.setdefault('prefixes_counters', {})
                prefixes_counters_dict['received'] = int(prefixes_received)
                prefixes_counters_dict['advertised'] = int(prefixes_advertised)
                continue

            # 5.5.5.5                          4       65000        0        0     0 00:08:50     Connect        0
            # 172.16.100.1                     4       65000       46       60     0 00:07:09 Established        1
            m = p7.match(line)
            if m:
                peer_address = m.groupdict()['peer_address']
                bgp_version = m.groupdict()['bgp_version']
                remote_as = m.groupdict()['remote_as']
                messages_received = m.groupdict()['messages_received']
                messages_sent = m.groupdict()['messages_sent']
                out_queue = m.groupdict()['out_queue']
                up_down_time = m.groupdict()['up_down_time']
                state = m.groupdict()['state']
                prefixes_received = m.groupdict()['prefixes_received']
                address_family_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',
                                                                                                    {})
                address_family_dict = address_family_dict.setdefault(address_family.lower(), {})
                peer_dict = address_family_dict.setdefault('peer', {}).setdefault(peer_address, {})
                peer_dict['remote_as'] = remote_as
                peer_dict['bgp_version'] = int(bgp_version)
                messages_dict = peer_dict.setdefault('total_messages', {})
                messages_dict['received'] = int(messages_received)
                messages_dict['sent'] = int(messages_sent)
                peer_dict['out_queue'] = int(out_queue)
                peer_dict['up_down_time'] = up_down_time
                peer_dict['state'] = state
                prefixes_counters_dict = peer_dict.setdefault('prefixes_counters', {})
                prefixes_counters_dict['received'] = int(prefixes_received)
                continue

        return ret_dict


class DisplayBgpPeerSummary(DisplayBgpPeer):
    """Parser for:
        'display bgp all summary'
    """
    cli_command = ['display bgp all summary']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        return super().cli(output=out)


class DisplayBgpPeerVerboseSchema(MetaParser):
    """Schema for:
     'display bgp {address_family} peer {peer_address} verbose'
     'display bgp {address_family} peer verbose'
     'display bgp {address_family} all peer {peer_address} verbose'
     'display bgp {address_family} all peer verbose'
     'display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose'
     'display bgp {address_family} vpn-instance {vrf} peer verbose'
     'display bgp peer {peer_address} verbose'
     'display bgp peer verbose'
    """

    schema = {
        "vrf": {
            Any(): {
                "peer": {
                    Any(): {
                        "remote_as": str,
                        "peer_type": str,
                        "current_state": str,
                        "bgp_version": int,
                        Optional("last_state"): str,
                        Optional("peer_up_count"): int,
                        Optional("description"): str,
                        Optional("up_time"): str,
                        Optional("remote_router_id"): str,
                        Optional("update_group_id"): int,
                        Optional("messages_counters"): {
                            Optional("sent"): {
                                Any(): int,
                            },
                            Optional("received"): {
                                Any(): int,
                            },
                        },
                        Optional("capabilities"): {
                            Any(): str
                        },
                        Optional("prefixes_counters"): {
                            Optional("received"): int,
                            Optional("active"): int,
                            Optional("advertised"): int
                        },
                        Optional("route_update_interval"): str,
                        Optional("route_policies"): {
                            Optional('import'): str,
                            Optional('export'): str,
                        },
                        Optional("transport"): {
                            Optional("local_port"): int,
                            Optional("remote_port"): int,
                        },
                    },
                },
            },
        },
    }


class DisplayBgpPeerVerbose(DisplayBgpPeerVerboseSchema):
    """Parser for:
     'display bgp {address_family} peer {peer_address} verbose'
     'display bgp {address_family} peer verbose'
     'display bgp {address_family} all peer {peer_address} verbose'
     'display bgp {address_family} all peer verbose'
     'display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose'
     'display bgp {address_family} vpn-instance {vrf} peer verbose'
     'display bgp peer {peer_address} verbose'
     'display bgp peer verbose'
    """
    cli_command = [
        'display bgp {address_family} {vrf_type} peer {peer_address} verbose',
        'display bgp {address_family} {vrf_type} peer verbose',
        'display bgp {address_family} vpn-instance {vrf} peer {peer_address} verbose',
        'display bgp {address_family} vpn-instance {vrf} peer verbose',
        'display bgp {address_family} peer {peer_address} verbose',
        'display bgp {address_family} peer verbose',
        'display bgp peer {peer_address} verbose',
        'display bgp peer verbose']

    def cli(self, address_family='ipv4', peer_address='', vrf='default', vrf_type='', output=None):

        if output is None:
            if address_family == 'ipv4':
                if peer_address:
                    command = self.cli_command[6].format(peer_address=peer_address)
                else:
                    command = self.cli_command[7]
            else:
                if vrf_type:
                    if peer_address:
                        command = self.cli_command[0].format(address_family=address_family,vrf_type=vrf_type, peer_address=peer_address)
                    else:
                        command = self.cli_command[1].format(address_family=address_family,vrf_type=vrf_type)
                elif vrf != 'default':
                    if peer_address:
                        command = self.cli_command[2].format(address_family=address_family, vrf=vrf, peer_address=peer_address)
                    else:
                        command = self.cli_command[3].format(address_family=address_family, vrf=vrf)
                else:
                    if peer_address:
                        command = self.cli_command[4].format(address_family=address_family, peer_address=peer_address)
                    else:
                        command = self.cli_command[5].format(address_family=address_family)

            logger.debug(f"Executing command: {command}")
            out = self.device.execute(command)
        else:
            out = output

        ret_dict = {}

        # IPv4-family for VPN instance:   mobile
        p1 = re.compile(r'^IPv[46]-family for VPN instance:\s+(?P<vrf>.+)$')

        # BGP Peer is 30.30.30.30,  remote AS 65000
        p2 = re.compile(r'^BGP Peer is (?P<peer_address>[a-zA-Z0-9.:]+),\s+remote AS (?P<remote_as>[0-9.]+)$')

        # Type: EBGP link
        p3 = re.compile(r'^Type: (?P<peer_type>.+)$')

        # Peer's description: "TEST"
        p4 = re.compile(r'^Peer\'s description: "(?P<description>[^"]+)"')

        # BGP version 4, Remote router ID 1.1.1.1
        p5 = re.compile(r'^BGP version (?P<bgp_version>\d+), Remote router ID (?P<remote_router_id>[a-zA-Z0-9.:]+)$')

        # Update-group ID: 1
        p6 = re.compile(r'^Update-group ID: (?P<update_group_id>\d+)')

        # BGP current state: Established, Up for 26d05h20m49s
        p7 = re.compile(r'^BGP current state: (?P<current_state>[^,]+), Up for (?P<up_time>[A-z0-9]+)$')

        # BGP current state: Idle(Admin)
        p7_1 = re.compile(r'^BGP current state: (?P<current_state>[^,]+)$')

        # BGP last state: Established
        p8 = re.compile(r'^BGP last state: (?P<last_state>.*)$')

        # BGP Peer Up count: 3
        p9 = re.compile(r'^BGP Peer Up count: (?P<peer_up_count>\d+)$')

        # Received total routes: 40
        p10 = re.compile(r'^Received total routes: (?P<prefixes_received>\d+)')

        # Received active routes total: 24
        p11 = re.compile(r'^Received active routes total: (?P<prefixes_active>\d+)')
        # Advertised total routes: 16
        p12 = re.compile(r'^Advertised total routes: (?P<prefixes_advertised>\d+)')
        # Port: Local - 49801        Remote - 179
        p13 = re.compile(r'^Port: Local - (?P<local_port>\d+)\s+Remote - (?P<remote_port>\d+)$')

        # Peer supports bgp multi-protocol extension
        # Peer supports bgp route refresh capability
        # Peer supports bgp 4-byte-as capability
        p14 = re.compile(r'^Peer supports bgp (?P<capability_name>.*)$')

        # Address family VPNv4 Unicast: advertised and received
        # Address family IPv4 Unicast: advertised
        p15 = re.compile(
            r"^Address family (?P<address_family>[^:]+): (?P<negotiation_state>(?:advertised and received)|advertised|received)$")

        # Received: Total 238538 messages
        # Sent: Total 272113 messages
        #  Update messages                713
        #  Open messages                  1
        #  KeepAlive messages             237824
        #  Notification messages          0
        #  Refresh messages               0
        p16_1 = re.compile(r'^Received: Total (?P<total_received>\d+) messages$')
        p16_2 = re.compile(r'^Sent: Total (?P<total_sent>\d+) messages$')
        p16_3 = re.compile(r'^(?P<message_type>[A-z]+) messages\s+(?P<message_count>\d+)$')

        #  Minimum route advertisement interval is 30 seconds
        p17 = re.compile(r'^Minimum route advertisement interval is (?P<route_update_interval>\d+) seconds$')

        # Import route policy is: FROM_RRVPN
        # Export route policy is: KEEP_MED
        p18 = re.compile(r'(?P<route_policy_direction>Import|Export) route policy is: (?P<route_policy_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IPv4-family for VPN instance:   mobile
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                ret_dict.setdefault('vrf', {}).setdefault(vrf, {})
                continue

            # BGP Peer is 30.30.30.30,  remote AS 65000
            m = p2.match(line)
            if m:
                peer_address = m.groupdict()['peer_address']
                remote_as = m.groupdict()['remote_as']
                peer_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('peer', {})
                peer_dict = peer_dict.setdefault(peer_address, {})
                peer_dict['remote_as'] = remote_as
                continue

            # Type: EBGP link
            m = p3.match(line)
            if m:
                peer_type = m.groupdict()['peer_type']
                peer_dict['peer_type'] = peer_type
                continue

            # Peer's description: "TEST"
            m = p4.match(line)
            if m:
                description = m.groupdict()['description']
                peer_dict['description'] = description
                continue

            # BGP version 4, Remote router ID 1.1.1.1
            m = p5.match(line)
            if m:
                bgp_version = m.groupdict()['bgp_version']
                remote_router_id = m.groupdict()['remote_router_id']
                peer_dict['bgp_version'] = int(bgp_version)
                peer_dict['remote_router_id'] = remote_router_id
                continue

            # Update-group ID: 1
            m = p6.match(line)
            if m:
                update_group_id = m.groupdict()['update_group_id']
                peer_dict['update_group_id'] = int(update_group_id)
                continue

            # BGP current state: Established, Up for 26d05h20m49s
            m = p7.match(line)
            if m:
                current_state = m.groupdict()['current_state']
                up_time = m.groupdict()['up_time']
                peer_dict['current_state'] = current_state
                peer_dict['up_time'] = up_time
                continue

            # BGP current state: Idle(Admin)
            m = p7_1.match(line)
            if m:
                current_state = m.groupdict()['current_state']
                peer_dict['current_state'] = current_state
                continue

            # BGP last state: Established
            m = p8.match(line)
            if m:
                last_state = m.groupdict()['last_state']
                peer_dict['last_state'] = last_state
                continue

            # BGP Peer Up count: 3
            m = p9.match(line)
            if m:
                peer_up_count = m.groupdict()['peer_up_count']
                peer_dict['peer_up_count'] = int(peer_up_count)
                continue

            # Received total routes: 40
            m = p10.match(line)
            if m:
                prefixes_dict = peer_dict.setdefault('prefixes_counters', {})
                prefixes_received = m.groupdict()['prefixes_received']
                prefixes_dict['received'] = int(prefixes_received)
                continue

            # Received active routes total: 24
            m = p11.match(line)
            if m:
                prefixes_dict = peer_dict.setdefault('prefixes_counters', {})
                prefixes_active = m.groupdict()['prefixes_active']
                prefixes_dict['active'] = int(prefixes_active)
                continue

            # Advertised total routes: 16
            m = p12.match(line)
            if m:
                prefixes_dict = peer_dict.setdefault('prefixes_counters', {})
                prefixes_advertised = m.groupdict()['prefixes_advertised']
                prefixes_dict['advertised'] = int(prefixes_advertised)
                continue

            # Port: Local - 49801        Remote - 179
            m = p13.match(line)
            if m:
                transport_dict = peer_dict.setdefault('transport', {})
                local_port = m.groupdict()['local_port']
                remote_port = m.groupdict()['remote_port']
                transport_dict['local_port'] = int(local_port)
                transport_dict['remote_port'] = int(remote_port)
                continue

            # Peer supports bgp multi-protocol extension
            # Peer supports bgp route refresh capability
            # Peer supports bgp 4-byte-as capability
            m = p14.match(line)
            if m:
                capability_name = m.groupdict()['capability_name']
                capabilities_dict = peer_dict.setdefault('capabilities', {})
                capabilities_dict[capability_name] = ""
                continue

            # Address family VPNv4 Unicast: advertised and received
            # Address family IPv4 Unicast: advertised
            m = p15.match(line)
            if m:
                address_family = m.groupdict()['address_family']
                negotiation_state = m.groupdict()['negotiation_state']
                capabilities_dict = peer_dict.setdefault('capabilities', {})
                capabilities_dict[address_family] = negotiation_state
                continue

            # Received: Total 238538 messages
            m = p16_1.match(line)
            if m:
                messages_dict = peer_dict.setdefault("messages_counters", {}).setdefault("received", {})
                total_received = m.groupdict()['total_received']
                messages_dict['total'] = int(total_received)
                continue

            # Sent: Total 272113 messages
            m = p16_2.match(line)
            if m:
                messages_dict = peer_dict.setdefault("messages_counters", {}).setdefault("sent", {})
                total_sent = m.groupdict()['total_sent']
                messages_dict['total'] = int(total_sent)
                continue

            #  Update messages                713
            #  Open messages                  1
            #  KeepAlive messages             237824
            #  Notification messages          0
            #  Refresh messages               0
            # Sent: Total 272113 messages
            m = p16_3.match(line)
            if m:
                message_type = m.groupdict()['message_type']
                message_count = m.groupdict()['message_count']
                messages_dict[message_type.lower()] = int(message_count)
                continue

            #  Minimum route advertisement interval is 30 seconds
            m = p17.match(line)
            if m:
                route_update_interval = m.groupdict()['route_update_interval']
                peer_dict['route_update_interval'] = route_update_interval
                continue

            # Import route policy is: FROM_RRVPN
            # Export route policy is: KEEP_MED
            m = p18.match(line)
            if m:
                route_policy_dict = peer_dict.setdefault("route_policies", {})
                route_policy_direction = m.groupdict()['route_policy_direction']
                route_policy_name = m.groupdict()['route_policy_name']
                route_policy_dict[route_policy_direction.lower()] = route_policy_name

        return ret_dict

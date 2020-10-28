'''show_telemetry.py
IOSXE parsers for the following commands

    * 'show telemetry ietf subscription all'
    * 'show telemetry ietf subscription all brief'
    * 'show telemetry ietf subscription all detail'
    * 'show telemetry ietf subscription {sub_id}'
    * 'show telemetry ietf subscription {sub_id} brief'
    * 'show telemetry ietf subscription {sub_id} detail'
    * 'show telemetry ietf subscription dynamic'
    * 'show telemetry ietf subscription dynamic detail'
    * 'show telemetry ietf subscription {sub_id} receiver'
    * 'show telemetry ietf subscription receiver'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any, Use, Schema

# pyATS
from pyats.utils.exceptions import SchemaTypeError


class ShowTelemetryIETFSubscriptionSchema(MetaParser):
    '''schema for:
        * show telemetry ietf subscription {sub_id}
        * show telemetry ietf subscription {sub_id} detail
    '''

    schema = {
        'id':{
            int: {
            Optional('type'): str,
            'state': str,
            Optional('stream'): str,
            'filter': {
                'filter_type': str,
                Optional('xpath'): str,
            },
            Optional('update_policy'): {
                'update_trigger': str,
                Optional('period'): int,
                Optional('synch_on_start'): str,
                Optional('dampening_period'): int,
            },
            Optional('encoding'): str,
            Optional('source'): str,
            Optional('source_vrf'): str,
            Optional('source_address'): str,
            Optional('notes'): str,
            Optional('legacy_receivers'): {
                str: {
                    'port': int,
                    'protocol': str,
                    Optional('protocol_profile'): str,
                    }
                }
            }
        }
    }

class ShowTelemetryIETFSubscription(ShowTelemetryIETFSubscriptionSchema):
    '''parser for:
        * show telemetry ietf subscription {sub_id}
    '''

    cli_command = 'show telemetry ietf subscription {sub_id}'

    def cli(self, sub_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                sub_id=sub_id
            ))
        else:
            out = output
        
        # 2147483659       Dynamic     Valid       xpath
        p1 = re.compile(r'^(?P<id>\d+) +(?P<type>\S+) +(?P<state>\S+) +(?P<filter_type>\S+)$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # 2147483659       Dynamic     Valid       xpath
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub = ret_dict.setdefault('id', {})
                subscription = sub.setdefault(int(group['id']), {})
                subscription.update({
                    'type': group['type'],
                    'state': group['state'],
                    'filter': {'filter_type': group['filter_type']},
                })

        return ret_dict

class ShowTelemetryIETFSubscriptionDetail(ShowTelemetryIETFSubscriptionSchema):
    '''parser for:
        * show telemetry ietf subscription {sub_id} detail
    '''

    cli_command = 'show telemetry ietf subscription {sub_id} detail'

    def cli(self, sub_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                    sub_id=sub_id
            ))
        else:
            out = output
        
        # Subscription ID: 2147483659
        p1 = re.compile(r'^Subscription +ID: +(?P<id>\d+)$')

        # State: Valid
        p2 = re.compile(r'^State: +(?P<state>\S+)$')

        # Stream: yang-push
        p3 = re.compile(r'^Stream: +(?P<stream>\S+)$')

        #     Filter type: xpath
        p4 = re.compile(r'^Filter +type: +(?P<filter>[\S\s]+)$')

        #     XPath: /if:interfaces-state/interface/oper-status
        p5 = re.compile(r'^XPath: +(?P<xpath>\S+)$')

        #     Update Trigger: periodic
        p6 = re.compile(r'^Update +Trigger: +(?P<trigger>[\S\s]+)$')

        #     Period: 1000
        p7 = re.compile(r'^Period: +(?P<period>\d+)$')

        #     Synch on start: No
        p7_1 = re.compile(r'^Synch +on +start: +(?P<sync>\S+)$')

        #     Dampening period: 0
        p7_2 = re.compile(r'^Dampening +period: +(?P<period>\d+)$')

        # Encoding: encode-xml
        p8 = re.compile(r'^Encoding: +(?P<encoding>\S+)$')

        # Source VRF:
        p9 = re.compile(r'^Source +VRF: +(?P<source>\S+)$')

        # Source Address:
        p10 = re.compile(r'^Source +Address: +(?P<address>\S+)$')

        # Notes:
        p11 = re.compile(r'^Notes: +(?P<notes>\S+)$')

        #     10.69.35.35                                 45128    netconf
        p12 = re.compile(r'^(?P<address>\S+) +(?P<port>\d+) +(?P<protocol>\S+)( +(?P<protocol_profile>\S+))?$')


        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # Subscription ID: 2147483659
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub = ret_dict.setdefault('id', {})
                subscription = sub.setdefault(int(group['id']), {})
                continue

            # State: Valid
            m = p2.match(line)
            if m:
                group = m.groupdict()
                subscription['state'] = group['state']
                continue

            # Stream: yang-push
            m = p3.match(line)
            if m:
                group = m.groupdict()
                subscription['stream'] = group['stream']
                continue

            #     Filter type: xpath
            m = p4.match(line)
            if m:
                group = m.groupdict()
                filters = subscription.setdefault('filter', {})
                filters['filter_type'] = group['filter']
                continue

            #     XPath: /if:interfaces-state/interface/oper-status
            m = p5.match(line)
            if m:
                group = m.groupdict()
                filters = subscription.setdefault('filter', {})
                filters['xpath'] = group['xpath']
                continue

            #     Update Trigger: periodic
            m = p6.match(line)
            if m:
                group = m.groupdict()
                update = subscription.setdefault('update_policy', {})
                update['update_trigger'] = group['trigger']
                continue

            #     Period: 1000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                update = subscription.setdefault('update_policy', {})
                update['period'] = int(group['period'])
                continue

            #     Synch on start: No
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                update = subscription.setdefault('update_policy', {})
                update['synch_on_start'] = group['sync']
                continue

            #     Dampening period: 0
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                update = subscription.setdefault('update_policy', {})
                update['dampening_period'] = int(group['period'])
                continue

            # Encoding: encode-xml
            m = p8.match(line)
            if m:
                group = m.groupdict()
                subscription['encoding'] = group['encoding']
                continue

            # Source VRF:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                subscription['source_vrf'] = group['source']
                continue

            # Source Address:
            m = p10.match(line)
            if m:
                group = m.groupdict()
                subscription['source_address'] = group['address']
                continue

            # Notes:
            m = p11.match(line)
            if m:
                group = m.groupdict()
                subscription['notes'] = group['notes']
                continue

            #     10.69.35.35                                 45128    netconf
            m = p12.match(line)
            if m:
                group = m.groupdict()
                receivers = subscription.setdefault('legacy_receivers', {})
                receiver = receivers.setdefault(group['address'], {})
                receiver.update({
                    'port': int(group['port']),
                    'protocol': group['protocol'],
                })
                if group['protocol_profile']:
                    receiver.update({
                        'protocol_profile': group['protocol_profile']
                    })
                continue

        return ret_dict


class ShowTelemetryIETFSubscriptionReceiverSchema(MetaParser):
    '''schema for:
        * show telemetry ietf subscription dynamic
    '''

    schema = {
        'id':{
            int: {
                'address': str,
                'port': int,
                'protocol': str,
                Optional('profile'): str,
                'connection': int,
                'state': str,
                Optional('explanation'): str,
            }
        }
    }

class ShowTelemetryIETFSubscriptionReceiver(ShowTelemetryIETFSubscriptionReceiverSchema):
    '''parser for:
        * show telemetry ietf subscription receiver
        * show telemetry ietf subscription {sub_id} receiver
    '''

    cli_command = [
        'show telemetry ietf subscription receiver',
        'show telemetry ietf subscription {sub_id} receiver',
        ]

    def cli(self, sub_id=None, output=None):
        if output is None:
            if sub_id:
                out = self.device.execute(self.cli_command[1].format(
                    sub_id=sub_id
                ))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        # Subscription ID: 2147483659
        p1 = re.compile(r'^Subscription +ID: +(?P<id>\d+)$')

        # Address: 10.69.35.35
        p2 = re.compile(r'^Address: +(?P<address>\S+)$')

        # Port: 45128
        p3 = re.compile(r'^Port: +(?P<port>\d+)$')

        # Protocol: netconf
        p4 = re.compile(r'^Protocol: +(?P<protocol>\S+)$')

        # Profile: 
        p5 = re.compile(r'^Profile: +(?P<profile>\S+)$')

        # Connection: 11
        p6 = re.compile(r'^Connection: +(?P<connection>\S+)$')

        # State: Valid
        p7 = re.compile(r'^State: +(?P<state>\S+)$')

        # Explanation:
        p8 = re.compile(r'^Explanation: +(?P<explanation>\S+)$')


        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # Subscription ID: 2147483659
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub = ret_dict.setdefault('id', {})
                subscription = sub.setdefault(int(group['id']), {})
                continue

            # Address: 10.69.35.35
            m = p2.match(line)
            if m:
                group = m.groupdict()
                subscription['address'] = group['address']
                continue

            # Port: 45128
            m = p3.match(line)
            if m:
                group = m.groupdict()
                subscription['port'] = int(group['port'])
                continue

            # Protocol: netconf
            m = p4.match(line)
            if m:
                group = m.groupdict()
                subscription['protocol'] = group['protocol']
                continue

            # Profile: 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                subscription['profile'] = group['profile']
                continue

            # Connection: 11
            m = p6.match(line)
            if m:
                group = m.groupdict()
                subscription['connection'] = int(group['connection'])
                continue

            # State: Valid
            m = p7.match(line)
            if m:
                group = m.groupdict()
                subscription['state'] = group['state']
                continue

            # Explanation:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                subscription['explanation'] = group['explanation']
                continue

        return ret_dict


# =======================================
# Schema for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnectionSchema(MetaParser):
    """Schema for show telemetry internal connection."""

    schema = {
        Optional("peer_address"): str,
        Optional("port"): int,
        Optional("profile"): str,
        Optional("source_address"): str,
        Optional("state"): str,
        Optional("transport"): str,
        Optional("vrf"): int,
        Optional("index"): {
            int: {
                "peer_address": str,
                "port": int,
                "source_address": str,
                "state": str,
                "vrf": int,
            },
        },
    }


# =======================================
# Parser for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnection(ShowTelemetryInternalConnectionSchema):
    """Parser for show telemetry internal connection"""

    cli_command = "show telemetry internal connection"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        # Telemetry connection

        # Peer Address    Port  VRF Source Address  Transport  State         Profile
        # --------------- ----- --- --------------- ---------- ------------- -------------
        # 10.37.174.7    25103   0 10.8.138.4      tls-native Active        sdn-network-101-wan

        # 10.37.174.7    25103   0 10.8.138.4      tls-native Active        sdn-network-101-wan
        no_index_capture = re.compile(
            r"^(?P<peer_address>[\d.]+)\s+(?P<port>\d+)\s+(?P<vrf>\d+)\s+(?P<source_address>[\d.]+)\s+(?P<transport>\S+)\s+(?P<state>\S+)\s+(?P<profile>\S+)$"
        )

        # 6 10.10.76.186              20830   0 10.64.47.177               Active
        index_capture = re.compile(
            r"(?P<index>\d+)\s+(?P<peer_address>[\d.]+)\s+(?P<port>\d+)\s+(?P<vrf>\d+)\s+(?P<source_address>[\d.]+)\s+(?P<state>\S+)"
        )

        tele_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            match = no_index_capture.match(line)
            if match:
                group = match.groupdict()

                # convert str to int
                int_list = ["port", "vrf"]
                for item in int_list:
                    group[item] = int(group[item])

                tele_info_obj.update(group)

                continue

            match = index_capture.match(line)
            if match:
                group = match.groupdict()

                # convert str to int
                int_list = ["port", "vrf", "index"]
                for item in int_list:
                    group[item] = int(group[item])

                # pull a key from group to use as new_key
                new_key = "index"
                new_group = {group[new_key]: {}}

                # update and pop new_key
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                if not tele_info_obj.get(new_key):
                    tele_info_obj = {new_key: {}}

                tele_info_obj[new_key].update(new_group)

                continue

        return tele_info_obj
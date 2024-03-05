'''show_telemetry.py
IOSXE parsers for the following commands

    * 'show telemetry ietf subscription all'
    * 'show telemetry ietf subscription all brief'
    * 'show telemetry ietf subscription all detail'
    * 'show telemetry ietf subscription all receivers'
    * 'show telemetry ietf subscription {sub_id}'
    * 'show telemetry ietf subscription {sub_id} brief'
    * 'show telemetry ietf subscription {sub_id} detail'
    * 'show telemetry ietf subscription dynamic'
    * 'show telemetry ietf subscription dynamic brief'
    * 'show telemetry ietf subscription dynamic detail'
    * 'show telemetry ietf subscription configured'
    * 'show telemetry ietf subscription configured brief'
    * 'show telemetry ietf subscription configured detail'
    * 'show telemetry ietf subscription permanent'
    * 'show telemetry ietf subscription permanent brief'
    * 'show telemetry ietf subscription permanent detail'
    * 'show telemetry ietf subscription {sub_id} receiver'
    * 'show telemetry ietf subscription receiver'
    * 'show telemetry connection {con_idx} detail'
    * 'show telemetry connection all'
    * 'show telemetry connection {con_idx} brief'
    * 'show telemetry internal sensor subscription {sub_id}'
    * 'show telemetry internal sensor stream {stream_type}'
    * 'show telemetry internal subscription all stats'
    * 'show telemetry internal protocol {protocol} manager {peer_ip} {port} source-vrf {vrf_id} {source_ip}'
    * 'show telemetry receiver name {name}'
    * 'show telemetry receiver all'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any, Use, Schema
from genie import parsergen

# pyATS
from pyats.utils.exceptions import SchemaTypeError

class ShowTelemetryIETFSubscriptionSchema(MetaParser):
    '''schema for:
        * show telemetry ietf subscription all
        * show telemetry ietf subscription all brief
        * show telemetry ietf subscription all detail
        * show telemetry ietf subscription {sub_id}
        * show telemetry ietf subscription {sub_id} brief
        * show telemetry ietf subscription {sub_id} detail
        * show telemetry ietf subscription dynamic
        * show telemetry ietf subscription dynamic brief
        * show telemetry ietf subscription dynamic detail
        * show telemetry ietf subscription configured
        * show telemetry ietf subscription configured brief
        * show telemetry ietf subscription configured detail
        * show telemetry ietf subscription permanent
        * show telemetry ietf subscription permanent brief
        * show telemetry ietf subscription permanent detail
    '''

    schema = {
        'id':{
            int: {
            Optional('type'): str,
            'state': str,
            Optional('stream'): str,
            Optional('filter'): {
                Optional('filter_type'): str,
                Optional('xpath'): str,
            },
            Optional('state_description'): str,
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
        * show telemetry connection {con_idx} subscription
        * show telemetry ietf subscription {sub_id} brief
    '''

    cli_command = [
            'show telemetry ietf subscription {sub_id}',
            'show telemetry connection {con_idx} subscription',
            'show telemetry ietf subscription {sub_id} brief',
            ]

    def cli(self, sub_id=None, con_idx=None, output=None):
        if output is None:
            if sub_id:
                output = self.device.execute(self.cli_command[0].format(
                    sub_id=sub_id
                ))
            elif con_idx:
                output = self.device.execute(self.cli_command[1].format(
                    con_idx=con_idx
                ))
        
        # 2147483659       Dynamic     Valid       xpath
        p = re.compile(r'^(?P<id>\d+) +(?P<type>\S+) +(?P<state>\S+) +(?P<filter_type>\S+)$')

        #New format was added as 17.7
        #ID         Type       State      State Description
        pNew = re.compile(r'^(?P<id>\d+) +(?P<type>\S+) +(?P<state>\S+) *(?P<state_description>.*)$')
        isLatestFormat = False

        if con_idx:
            p = pNew
            isLatestFormat = True
        else:
            #Determine what format the data is displayed in from the header
            words = output.strip().split()
            if words:
                headerInOutput = (words[0] == "ID")

                if headerInOutput:
                    isLatestFormat = (words[4] == "Description")

                    if isLatestFormat:
                        p = pNew
        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                group = m.groupdict()
                sub = ret_dict.setdefault('id', {})
                subscription = sub.setdefault(int(group['id']), {})
                subscription['type'] = group['type']
                subscription['state'] = group['state']
                if isLatestFormat:
                    subscription['state_description'] = group['state_description']
                else:
                    subscription['filter'] = {'filter_type': group['filter_type']}
        return ret_dict


class ShowTelemetryIETFSubscriptionAll(ShowTelemetryIETFSubscription):
    '''parser for:
        * show telemetry ietf subscription all
        * show telemetry ietf subscription all brief
    '''

    cli_command = [
        'show telemetry ietf subscription all',
        'show telemetry ietf subscription all brief',
    ]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        return super().cli(output=output)


class ShowTelemetryIETFSubscriptionConfigured(ShowTelemetryIETFSubscriptionAll):
    '''parser for:
        * show telemetry ietf subscription configured
        * show telemetry ietf subscription configured brief
    '''

    cli_command = [
        'show telemetry ietf subscription configured',
        'show telemetry ietf subscription configured brief',
    ]


class ShowTelemetryIETFSubscriptionDynamic(ShowTelemetryIETFSubscriptionAll):
    '''parser for:
        * show telemetry ietf subscription dynamic
        * show telemetry ietf subscription dynamic brief
    '''

    cli_command = [
        'show telemetry ietf subscription dynamic',
        'show telemetry ietf subscription dynamic brief',
    ]


class ShowTelemetryIETFSubscriptionPermanent(ShowTelemetryIETFSubscriptionAll):
    '''parser for:
        * show telemetry ietf subscription permanent
        * show telemetry ietf subscription permanent brief
    '''

    cli_command = [
        'show telemetry ietf subscription permanent',
        'show telemetry ietf subscription permanent brief',
    ]


class ShowTelemetryIETFSubscriptionDetail(ShowTelemetryIETFSubscriptionSchema):
    '''parser for:
        * show telemetry ietf subscription {sub_id} detail
    '''

    cli_command = 'show telemetry ietf subscription {sub_id} detail'

    def cli(self, sub_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(
                    sub_id=sub_id
            ))
        
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

        for line in output.splitlines():
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


class ShowTelemetryIETFSubscriptionAllDetail(ShowTelemetryIETFSubscriptionDetail):
    '''parser for:
        * show telemetry ietf subscription all detail
    '''

    cli_command = 'show telemetry ietf subscription all detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(sub_id=None, output=output)

class ShowTelemetryIETFSubscriptionConfiguredDetail(ShowTelemetryIETFSubscriptionAllDetail):
    '''parser for:
        * show telemetry ietf subscription configured detail
    '''

    cli_command = 'show telemetry ietf subscription configured detail'


class ShowTelemetryIETFSubscriptionDynamicDetail(ShowTelemetryIETFSubscriptionAllDetail):
    '''parser for:
        * show telemetry ietf subscription dynamic detail
    '''

    cli_command = 'show telemetry ietf subscription dynamic detail'


class ShowTelemetryIETFSubscriptionPermanentDetail(ShowTelemetryIETFSubscriptionAllDetail):
    '''parser for:
        * show telemetry ietf subscription permanent detail
    '''

    cli_command = 'show telemetry ietf subscription permanent detail'


class ShowTelemetryIETFSubscriptionAllReceiverSchema(MetaParser):
    '''schema for:
        * show telemetry ietf subscription all receivers
    '''
    schema = {
        int:{
            str: {
                'connection': int,
                'state': str,
                'explanation': str
            }
        }
    }


class ShowTelemetryIETFSubscriptionAllReceivers(ShowTelemetryIETFSubscriptionAllReceiverSchema):
    '''parser for:
        * show telemetry ietf subscription all receivers
    '''

    cli_command = 'show telemetry ietf subscription all receivers'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = dict()
        # 101              grpc-tcp                           0      Resolving      Resolution request in progress
        p1 = re.compile(r'^(?P<id>\d+) +'
                        r'(?P<name>\S+) +'
                        r'(?P<connection>\S+) +'
                        r'(?P<state>.\S+) *'
                        r'(?P<explanation>.*)$')


        for line in out.splitlines():
            # 101              grpc-tcp                           0      Resolving      Resolution request in progress
            m = p1.match(line)
            # If whole line matches p1 regex
            if m:
                group = m.groupdict()

                id = group.pop('id')
                name = group.pop('name')

                id_dict = ret_dict.setdefault(int(id), {})
                name_dict = id_dict.setdefault(name, {})

                name_dict.update({
                    'connection': int(group['connection']),
                    'state': group['state'],
                    'explanation': group['explanation']
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
                Optional('address'): str,
                Optional('port'): int,
                Optional('protocol'): str,
                Optional('profile'): str,
                'connection': int,
                Optional('state'): str,
                Optional('explanation'): str,
                Optional('name'): str,
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
                cmd = self.cli_command[1].format(sub_id=sub_id)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
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
        # State: Transport Requested
        # State: Valid
        p7 = re.compile(r'^State: +(?P<state>.*)$')

        # Explanation:
        p8 = re.compile(r'^Explanation: *(?P<explanation>.*)$')

        # Name: grpc-tcp
        p9 = re.compile(r'^Name: +(?P<name>\S+)$')

        ret_dict = dict()

        for line in output.splitlines():
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

            # Name
            m = p9.match(line)
            if m:
                group = m.groupdict()
                subscription['name'] = group['name']
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
            output = self.device.execute(self.cli_command)

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

        for line in output.splitlines():
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


class ShowTelemetryConnectionSchema(MetaParser):
    """Schema for:
        show telemetry connection all
        show telemetry connection {con_idx} detail
    """

    schema = {
        "index": {
            int: {
                "peer_address": str,
                "port": int,
                "vrf": int,
                "source_address": str,
                Optional("type"): str,
                "state": str,
                Optional("state_description"): str,
                Optional("peer_id"): str,
                Optional("receiver_name"): str,
                Optional("transport"): str,
                Optional("use_count"): int,
                Optional("state_change_time"): str,
            },
        }
    }


class ShowTelemetryConnectionAll(ShowTelemetryConnectionSchema):
    """Parser for:
        show telemetry connection all
        show telemetry connection {con_idx} brief
    """

    cli_command = [
        "show telemetry connection all",
        "show telemetry connection {con_idx} brief",
        ]

    def cli(self, con_idx=None, output=None):
        if output is None:
            if con_idx:
                cmd = self.cli_command[1].format(con_idx=con_idx)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = dict()

        if output:
            #Index Peer Address               Port  VRF Source Address             State      State Description
            #----- -------------------------- ----- --- -------------------------- ---------- --------------------
            #    0 5.40.26.169                49066 0   0.0.0.0                    Active     Connection created for protocol netconf
            # or
            #Index Peer Address               Port  VRF Source Address             State      State Description
            #----- -------------------------- ----- --- -------------------------- ---------- --------------------
            #    0 5.40.26.169                49066 0 M 0.0.0.0                    Active     Connection created for protocol netconf
            header = ["Index", "Peer Address", "Port", "VRF", "Source Address", "State", "State Description"]
            label_fields = ["index", "peer_address", "port", "vrf", "source_address", "state", "state_description"]

            tmp_dict = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header,
                    label_fields=label_fields, index=[0]).entries

            for k in tmp_dict:
                del tmp_dict[k]["index"]
                ret_dict[int(k)] = tmp_dict[k]

                ret_dict[int(k)]["port"] = int(ret_dict[int(k)]["port"])
                ret_dict[int(k)]["vrf"] = int(re.sub('M', '', ret_dict[int(k)]["vrf"]))

            ret_dict = {"index": ret_dict}

        return ret_dict


class ShowTelemetryConnectionDetail(ShowTelemetryConnectionSchema):
    """Parser for:
        show telemetry connection {con_idx} detail
    """

    cli_command = "show telemetry connection {con_idx} detail"

    def cli(self, con_idx=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(con_idx=con_idx))

        ret_dict = {}

        #Index             : 0
        p1 = re.compile(r'^Index *: *(?P<idx>\d*)$')

        #Peer Address      : 5.40.26.169
        p2 = re.compile(r'^Peer +Address *: *(?P<peer_addr>\S*)$')

        #Port              : 49066
        p3 = re.compile(r'^Port *: *(?P<port>\d*)$')

        #VRF               : 0
        p4 = re.compile(r'^VRF *: *(?P<vrf>\d*)$')

        #Source Address    : 0.0.0.0
        p5 = re.compile(r'^Source +Address *: *(?P<source_addr>\S*)$')

        #Type              : PROTOCOL
        p6 = re.compile(r'^Type *: *(?P<type>\S*)$')

        #State             : Active
        p7 = re.compile(r'^State *: *(?P<state>\S*)$')

        #State Description : Connection created for protocol netconf
        p8 = re.compile(r'^State +Description *: *(?P<state_description>.*)$')

        #Peer ID           : admin
        p9 = re.compile(r'^Peer +ID *: *(?P<peer_id>\S*)$')

        #Receiver Name     :
        p10 = re.compile(r'^Receiver +Name *: *(?P<receiver_name>\S*)$')

        #Transport         : netconf
        p11 = re.compile(r'^Transport *: *(?P<transport>\S*)$')

        #Use Count         : 1
        p12 = re.compile(r'^Use +Count *: *(?P<use_count>\d*)$')

        #State Change Time : 10/26/21 17:27:31
        p13 = re.compile(r'^State +Change +Time *: +(?P<state_change_time>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # Subscription ID: 2147483659
            m = p1.match(line)
            if m:
                group = m.groupdict()
                indexDict = ret_dict.setdefault('index', {}).\
                        setdefault(int(group['idx']), {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                indexDict["peer_address"] = group['peer_addr']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                indexDict["port"] = int(group["port"])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                indexDict["vrf"] = int(group["vrf"])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                indexDict["source_address"] = group["source_addr"]
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                indexDict["type"] = group["type"]
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                indexDict["state"] = group["state"]
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                indexDict["state_description"] = group["state_description"]
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                indexDict["peer_id"] = group["peer_id"]
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                indexDict["receiver_name"] = group["receiver_name"]
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                indexDict["transport"] = group["transport"]
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                indexDict["use_count"] = int(group["use_count"])
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                indexDict["state_change_time"] = group["state_change_time"]
                continue

        return ret_dict


class ShowTelemetryInternalSubscriptionAllStatsSchema(MetaParser):
    '''schema for:
        * show telemetry internal subscription all stats
    '''

    schema = {
        'sub_id':{
            int: {
                'msg_sent': int,
                'msg_drop': int,
                'record_sent': int,
                'connection_info': str,
            }
        }
    }

class ShowTelemetryInternalSubscriptionAllStats(ShowTelemetryInternalSubscriptionAllStatsSchema):
    '''parser for:
        * show telemetry internal subscription all stats
    '''

    cli_command = 'show telemetry internal subscription all stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #Subscription ID  Msgs Sent  Msgs Drop  Records Sent Connection Info
        #---------------- ---------- ---------- ------------ -----------------------------------------
        #2147483648       246        0          126690       admin
        header = ["Subscription ID", "Msgs Sent", "Msgs Drop", "Records Sent", "Connection Info"]
        label_fields = ['sub_id', 'msg_sent', 'msg_drop', 'record_sent', 'connection_info']

        ret_dict = dict()
        if output:
            tmp_dict = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header,
                    label_fields=label_fields, index=[0]).entries

            for k in tmp_dict:
                del tmp_dict[k]["sub_id"]
                ret_dict[int(k)] = tmp_dict[k]

                ret_dict[int(k)]["msg_sent"] = int(ret_dict[int(k)]["msg_sent"])
                ret_dict[int(k)]["msg_drop"] = int(ret_dict[int(k)]["msg_drop"])
                ret_dict[int(k)]["record_sent"] = int(ret_dict[int(k)]["record_sent"])
            ret_dict = {"sub_id": ret_dict}

        return ret_dict


class ShowTelemetryInternalSensorSchema(MetaParser):
    """Schema for:
        * show telemetry internal sensor subscription {sub_id}
        * show telemetry internal sensor stream {stream_type}
    """

    schema = {
        "instance": {
            int: {
                Optional("sensor_type"): {
                    "type": str,
                    "filter_type": str,
                    "filter_selector": str,
                },
                Optional("data_collector"): {
                    Any(): {
                        "dc_type": str,
                        "sub_filter": str,
                    }
                }
            }
        }
    }

class ShowTelemetryInternalSensor(ShowTelemetryInternalSensorSchema):
    """Parser for:
        * show telemetry internal sensor subscription {sub_id}
        * show telemetry internal sensor stream {stream_type}
    """

    cli_command = [
        'show telemetry internal sensor subscription {sub_id}',
        'show telemetry internal sensor stream {stream_type}',
    ]
    def cli(self, sub_id=None, stream_type=None, output=None):
        if output is None:
            if sub_id:
                output = self.device.execute(self.cli_command[0].format(
                    sub_id=sub_id
                ))
            elif stream_type:
                output = self.device.execute(self.cli_command[1].format(
                    stream_type=stream_type
                ))
            else:
                return {}

        # Subscription ID: 2147483659
        p1 = re.compile(r'^Subscription +ID: *(?P<sub_id>\d*)$')

        #  Sensor Type: yang-push periodic
        p2 = re.compile(r'^Sensor +Type: *(?P<sensor_type>.*)$')

        #    Filter type: xpath
        p3 = re.compile(r'^Filter +type: *(?P<filter_type>\S*)$')

        #    Filter selector: /if:interfaces-state/interface[name="GigabitEthernet0/0"]/oper-status
        p4 = re.compile(r'^Filter +selector: *(?P<filter_selector>\S*)$')

        #    DC: confd periodic, SubFilter: /if:interfaces-state/interface[name="GigabitEthernet0/0"]/oper-status
        p5 = re.compile(r'^DC: *(?P<dc_type>.*), SubFilter: *(?P<sub_filter>\S*)$')

        ret_dict = dict()
        dcCtr = 0

        for line in output.splitlines():
            line = line.strip()

            # Subscription ID: 2147483648
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sensorDict = ret_dict.setdefault('instance', {}).\
                        setdefault(int(group['sub_id']), {})
                dcCtr = 0
                continue


            # Sensor Type: yang-push periodic
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sensorTypeDic = sensorDict.setdefault("sensor_type", {})
                sensorTypeDic['type'] = group['sensor_type']
                continue

            # Filter type: xpath
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sensorTypeDic['filter_type'] = group['filter_type']
                continue

            # Filter selector: /if:interfaces-state/interface[name="GigabitEthernet0/0"]/oper-status
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensorTypeDic['filter_selector'] = group['filter_selector']
                continue

            # DC: confd periodic, SubFilter: /if:interfaces-state/interface[name="GigabitEthernet0/0"]/oper-status
            m = p5.match(line)
            if m:
                group = m.groupdict()
                dataCollectorDict = sensorDict.setdefault("data_collector", {})

                dcKey = "dc" + str(dcCtr)
                dcDic = dataCollectorDict.setdefault(dcKey, {})
                dcDic['dc_type'] = group['dc_type']
                dcDic['sub_filter'] = group['sub_filter']
                dcCtr += 1
                continue
        return ret_dict


class ShowTelemetryReceiverNameSchema(MetaParser):
    '''schema for:
        * show telemetry receiver name {name}
        * show telemetry receiver all
    '''
    schema = {
            "name": {
                Any(): {
                    'profile': str,
                    'state': str,
                    Optional('state_description'): str,
                    Optional('last_change'): str,
                    'type': str,
                    Optional('protocol'): str,
                    Optional('host'): str,
                    Optional('port'): int,
                    Optional('explanation'): str
                    },
                }
            }

class ShowTelemetryReceiverName(ShowTelemetryReceiverNameSchema):
    '''parser for:
        * show telemetry receiver name {name}
    '''

    cli_command = 'show telemetry receiver name {name}'

    def cli(self, name, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(
                name=name
            ))

        #Name: test0
        p1 = re.compile("^Name:\s*(?P<name>\S*)$")

        #Profile:
        p2 = re.compile("^Profile:\s*(?P<profile>\S*)$")

        #State: Valid
        p3 = re.compile("^State:\s*(?P<state>\S*)$")

        #State Description:
        p4 = re.compile("^State Description:\s*(?P<state_description>\S*)$")

        #Last State Change: 10/26/21 17:55:47
        p5 = re.compile("^Last State Change:\s*(?P<last_change>\S* *\S*)$")

        #Type: protocol
        p6 = re.compile("^Type:\s*(?P<type>\S*)$")

        #Protocol: native
        p7 = re.compile("^Protocol:\s*(?P<protocol>\S*)$")

        #Host: 161.44.223.172
        p8 = re.compile("^Host:\s*(?P<host>\S*)$")

        #Port: 123
        p9 = re.compile("^Port:\s*(?P<port>\S*)$")

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                val = group["name"]
                nameEntry = ret_dict.setdefault("name", {}).setdefault(val, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                nameEntry["profile"] = group["profile"]
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                nameEntry["state"] = group["state"]
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                nameEntry["state_description"] = group["state_description"]
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                nameEntry["last_change"] = group["last_change"]
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                nameEntry["type"] = group["type"]
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                nameEntry["protocol"] = group["protocol"]
                continue
            
            m = p8.match(line)
            if m:
                group = m.groupdict()
                nameEntry["host"] = group["host"]
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                nameEntry["port"] = int(group["port"])
                continue
            
        return ret_dict

class ShowTelemetryReceiverAll(ShowTelemetryReceiverNameSchema):
    '''parser for:
        * show telemetry receiver all
    '''

    cli_command = 'show telemetry receiver all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = dict()
        if output:
            header = ["Name", "Type", "Profile", "State", "Explanation"]
            label_fields = [i.lower() for i in header]

            ret_dict = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, 
                    label_fields=label_fields, index=[0]).entries

            for k in ret_dict:
                del ret_dict[k]["name"]

            ret_dict = {"name": ret_dict}
        return ret_dict

class ShowTelemetryIETFSubscriptionSummarySchema(MetaParser):
    """Schema for:
        show telemetry ietf subscription summary
    """

    schema = {
        "max_supported": int,
        "type": {
            str: {
                "total": int,
                "valid": int,
                "invalid": int,
            },
        }
    }

class ShowTelemetryIETFSubscriptionSummary(ShowTelemetryIETFSubscriptionSummarySchema):
    """Parser for:
        show telemetry ietf subscription summary
    """

    cli_command = "show telemetry ietf subscription summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Maximum supported: 128
        p1 = re.compile(r'^Maximum +supported: +(?P<max_supported>[0-9]+)$')

        # Subscription     Total       Valid      Invalid
        # -----------------------------------------------
        # All              0           0          0
        # Dynamic          0           0          0
        # Configured       0           0          0
        # Permanent        0           0          0
        p2 = re.compile(r'^(?P<type>(All|Dynamic|Configured|Permanent)+) +(?P<total>[0-9]+) +'
                        r'(?P<valid>[0-9]+) +(?P<invalid>[0-9]+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # Maximum supported: 128
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['max_supported'] = int(group['max_supported'])
                continue

            # Subscription     Total       Valid      Invalid
            # -----------------------------------------------
            # All              0           0          0
            # Dynamic          0           0          0
            # Configured       0           0          0
            # Permanent        0           0          0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                types = ret_dict.setdefault('type', {})
                states = types.setdefault(group['type'].lower(), {})
                for state in ['total', 'valid', 'invalid']:
                    states.update({state: int(group[state])})
                continue

        return ret_dict


class ShowTelemetryInternalProtocolManagerSchema(MetaParser):
    '''schema for:
        * show telemetry internal protocol {protocol} manager {peer_ip} {port} source-vrf {vrf_id} {source_ip}
    '''

    schema = {
        "con": {
            str: {
                "sock_fd": int,
                "protocol": str,
                "state": str,
                Optional("version"): str,
                Optional("profile"): str,
                "table_id": int,
                Optional("wait_mask"): str,
                Optional("con_retries"): int,
                Optional("send_retries"): int,
                Optional("pending_events"): int,
                Optional("session_reqs"): int,
                Optional("session_resp"): int,
                "source_ip": str,
                "bytes_sent": int,
                "msgs_sent": int,
                "msgs_recv": int,
                Optional("bytes_queued"): int,
                Optional("creation_time"): str,
                Optional("last_con_time"): str,
                Optional("last_discon_time"): str,
                Optional("last_error"): str,
                Optional("con_flaps"): int,
                Optional("last_flap_reason"): str,
                Optional("keep_alive_timeouts"): int,
                Optional("last_transport_error"): str
            }
        }
    }

class ShowTelemetryInternalProtocolManager(ShowTelemetryInternalProtocolManagerSchema):
    '''parser for:
        * show telemetry internal protocol {protocol} manager {peer_ip} {port} source-vrf {vrf_id} {source_ip}
    '''

    cli_command = [
        'show telemetry internal protocol {protocol} manager {peer_ip} {port} source-vrf {vrf_id} {source_ip}'
    ]

    def cli(self, protocol, peer_ip, port, vrf_id, source_ip=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(protocol=protocol,
                                                                    peer_ip=peer_ip,
                                                                    port=port,
                                                                    vrf_id=vrf_id,
                                                                    source_ip=source_ip))

        #Con str                : 161.44.237.28:45000:0:172.16.0.6
        p1 = re.compile(r'^Con str *: *(?P<con_str>\S*)$')

        #Sockfd                 : 138
        p2 = re.compile(r'^Sockfd *: *(?P<sock_fd>\d*)$')

        #Protocol               : native
        p3 = re.compile(r'^Protocol *: *(?P<protocol>\S*)$')

        #State                  : CNDP_STATE_CONNECTED
        p4 = re.compile(r'^State *: *(?P<state>\w*)$')

        #Version                :
        p5 = re.compile(r'^Version *: *(?P<version>\S*)$')

        #Profile                :
        p6 = re.compile(r'^Profile *: *(?P<profile>\S*)$')

        #Table id               : 0
        p7 = re.compile(r'^Table id *: *(?P<table_id>\d*)$')

        #Wait Mask              :
        p8 = re.compile(r'^Wait Mask *: *(?P<wait_mask>\S*)$')

        #Connection Retries     : 0
        p9 = re.compile(r'^Connection Retries *: *(?P<con_retries>\d*)$')

        #Send Retries           : 0
        p10 = re.compile(r'^Send Retries *: *(?P<send_retries>\d*)$')

        #Pending events         : 0
        p11 = re.compile(r'^Pending events *: *(?P<pending_events>\d*)$')

        #Session requests       : 1
        p12 = re.compile(r'^Session requests *: *(?P<session_reqs>\d*)$')

        #Session replies        : 1
        p13 = re.compile(r'^Session replies *: *(?P<session_resp>\d*)$')

        #Source ip              : 172.16.0.6
        p14 = re.compile(r'^Source ip *: *(?P<source_ip>\S*)$')

        #Bytes Sent             : 4835
        p15 = re.compile(r'^Bytes Sent *: *(?P<bytes_sent>\d*)$')

        #Msgs Sent              : 8
        p16 = re.compile(r'^Msgs Sent *: *(?P<msgs_sent>\d*)$')

        #Msgs Received          : 0
        p17 = re.compile(r'^Msgs Received *: *(?P<msgs_recv>\d*)$')

        #Bytes in queue         : 0
        p18 = re.compile(r'^Bytes in queue *: *(?P<bytes_queued>\d*)$')

        #Creation time:         : Mon Jan 15 21:49:23:54
        p19 = re.compile(r'^Creation time: *: *(?P<creation_time>.*)$')

        #Last connected time:   : Mon Jan 15 21:49:23:59
        p20 = re.compile(r'^Last connected time: *: *(?P<last_con_time>.*)$')

        #Last disconnect time:  :
        p21 = re.compile(r'^Last disconnect time: *: *(?P<last_discon_time>.*)$')

        #Last error:            :
        p22 = re.compile(r'^Last error: *: *(?P<last_error>.*)$')

        #Connection flaps:      : 0
        p23 = re.compile(r'^Connection flaps: *: *(?P<con_flaps>\d*)$')

        #Last flap Reason:      :
        p24 = re.compile(r'^Last flap reason: *: *(?P<last_flap_reason>.*)$')

        #Keep Alive Timeouts:   : 0
        p25 = re.compile(r'^Keep Alive Timeouts: *: *(?P<keep_alive_timeouts>\d*)$')

        #Last Transport Error   :
        p26 = re.compile(r'^Last Transport Error *: *(?P<last_transport_error>.*)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            #Con str                : 161.44.237.28:45000:0:172.16.0.6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                con_dict = ret_dict.setdefault('con', {}).setdefault(group['con_str'], {})
                continue

            #Sockfd                 : 138
            m = p2.match(line)
            if m:
                group = m.groupdict()
                con_dict['sock_fd'] = int(group['sock_fd'])
                continue

            #Protocol               : native
            m = p3.match(line)
            if m:
                group = m.groupdict()
                con_dict['protocol'] = group['protocol']
                continue

            #State                  : CNDP_STATE_CONNECTED
            m = p4.match(line)
            if m:
                group = m.groupdict()
                con_dict['state'] = group['state']
                continue

            #Version                :
            m = p5.match(line)
            if m:
                group = m.groupdict()
                con_dict['version'] = group['version']
                continue

            #Profile                :
            m = p6.match(line)
            if m:
                group = m.groupdict()
                con_dict['profile'] = group['profile']
                continue

            #Table id               : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                con_dict['table_id'] = int(group['table_id'])
                continue

            #Wait Mask              :
            m = p8.match(line)
            if m:
                group = m.groupdict()
                con_dict['wait_mask'] = group['wait_mask']
                continue

            #Connection Retries     : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                con_dict['con_retries'] = int(group['con_retries'])
                continue

            #Send Retries           : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                con_dict['send_retries'] = int(group['send_retries'])
                continue

            #Pending events         : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                con_dict['pending_events'] = int(group['pending_events'])
                continue

            #Session requests       : 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                con_dict['session_reqs'] = int(group['session_reqs'])
                continue

            #Session replies        : 1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                con_dict['session_resp'] = int(group['session_resp'])
                continue

            #Source ip              : 172.16.0.6
            m = p14.match(line)
            if m:
                group = m.groupdict()
                con_dict['source_ip'] = group['source_ip']
                continue

            #Bytes Sent             : 4835
            m = p15.match(line)
            if m:
                group = m.groupdict()
                con_dict['bytes_sent'] = int(group['bytes_sent'])
                continue

            #Msgs Sent              : 8
            m = p16.match(line)
            if m:
                group = m.groupdict()
                con_dict['msgs_sent'] = int(group['msgs_sent'])
                continue

            #Msgs Received          : 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                con_dict['msgs_recv'] = int(group['msgs_recv'])
                continue

            #Bytes in queue         : 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                con_dict['bytes_queued'] = int(group['bytes_queued'])
                continue

            #Creation time:         : Mon Jan 15 21:49:23:54
            m = p19.match(line)
            if m:
                group = m.groupdict()
                con_dict['creation_time'] = group['creation_time']
                continue

            #Last connected time:   : Mon Jan 15 21:49:23:59
            m = p20.match(line)
            if m:
                group = m.groupdict()
                con_dict['last_con_time'] = group['last_con_time']
                continue

            #Last disconnect time:  :
            m = p21.match(line)
            if m:
                group = m.groupdict()
                con_dict['last_discon_time'] = group['last_discon_time']
                continue

            #Last error:            :
            m = p22.match(line)
            if m:
                group = m.groupdict()
                con_dict['last_error'] = group['last_error']
                continue

            #Connection flaps:      : 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                con_dict['con_flaps'] = int(group['con_flaps'])
                continue

            #Last flap Reason:      :
            m = p24.match(line)
            if m:
                group = m.groupdict()
                con_dict['last_flap_reason'] = group['last_flap_reason']
                continue

            #Keep Alive Timeouts:   : 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                con_dict['keep_alive_timeouts'] = int(group['keep_alive_timeouts'])
                continue

            #Last Transport Error   :
            m = p26.match(line)
            if m:
                group = m.groupdict()
                con_dict['last_transport_error'] = group['last_transport_error']
                continue

        return ret_dict

"""show_track.py
IOSXE parser for the following show commands:
    * 'show track'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================
# Schema for 'show track'
# =======================
class ShowTrackSchema(MetaParser):
    """ Schema for 'show track' """
    schema = {
        'type': {
            Any(): {
                Optional('name'): str,
                Optional('address'): str,
                Optional('mask'): str,
                'state': str,
                Optional('state_description'): str,
                Optional('delayed'): {
                    Optional('delayed_state'): str,
                    Optional('secs_remaining'): float,
                    Optional('connection_state'): str,
                },
                'change_count': int,
                'last_change': str,
                Optional('threshold_down'): int,
                Optional('threshold_up'): int,
            },
        },
        Optional('delay_up_secs'): float,
        Optional('delay_down_secs'): float,
        Optional('first_hop_interface_state'): str,
        Optional('prev_first_hop_interface'): str,
        Optional('tracked_by'): {
            Optional(Any()): {   #increasing index 0, 1, 2, 3, ...
                Optional('name'): str,
                Optional('interface'): str,
                Optional('group_id'): str,
            }
        },
    }

# =======================
# Parser for 'show track'
# =======================
class ShowTrack(ShowTrackSchema):
    """ Parser for 'show track' """
    cli_command = 'show track'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #Init vars
        parsed_dict = {}

        # Interface GigabitEthernet3.420 line-protocol
        # IP route 10.21.12.0 255.255.255.0 reachability
        # IP route 172.16.52.0 255.255.255.0 metric threshold
        p1 = re.compile(r'^(?P<type>IP route|Interface) +'
            r'((?P<address>[\d.]+) +(?P<mask>[\d.]+)|'
            r'(?P<name>[\d\w.]+)) +(?P<parameter>[\w \-]+)')

        # Line protocol is Up
        # Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
        # Metric threshold is Down (no route)
        p2 = re.compile(r'^(?P<parameter>[\w ]+) +is +(?P<state>Up|Down)'
            r'( +\((?P<state_description>[\w ]+)\),*( delayed '
            r'(?P<delayed_state>Up|Down) \((?P<secs_remaining>\d+) sec '
            r'remaining\) \((?P<connection_state>\w+)\))*)*')

        # 1 change, last change 00:00:27
        p3 = re.compile(r'^(?P<change_count>\d+) +change, +last +change'
            r' +(?P<last_change>[\d:]+)')

        # Delay up 20 secs, down 10 secs
        p4 = re.compile(r'^Delay +up +(?P<delay_up_secs>\d+)'
            r' +secs,* +down +(?P<delay_down_secs>\d+) +sec')

        # First-hop interface is unknown (was Ethernet1/0)
        p5 = re.compile(r'^First-hop +interface +is +'
            r'(?P<first_hop_interface_state>\w+)( +\(was'
            r' +(?P<prev_first_hop_interface>[\w\d\/\.\-\_]+)\))*')

        # Metric threshold down 255 up 254
        p6 = re.compile(r'^Metric +threshold +down'
            r' +(?P<threshold_down>\d+) +up +(?P<threshold_up>\d+)')

        # VRRP GigabitEthernet3.420 10
        # HSRP Ethernet0/0 3
        # HSRP Ethernet0/1 3
        p7 = re.compile(r'^(?P<name>[a-zA-Z]{3,4}) +'
            r'(?P<interface>[A-Za-z0-9/.]+) +((?P<group_id>\d+)|(\n))')

        for line in output.splitlines():
            line = line.strip()

            # Interface GigabitEthernet3.420 line-protocol
            # IP route 10.21.12.0 255.255.255.0 reachability
            # IP route 172.16.52.0 255.255.255.0 metric threshold
            m = p1.match(line)
            if m:
                group = m.groupdict()
                type_name = group['type']
                type_dict = parsed_dict.setdefault('type', {})\
                    .setdefault(type_name, {})

                if group['name']:
                    type_dict['name'] = group['name']
                if group['address']:
                    type_dict['address'] = group['address']
                if group['mask']:
                    type_dict['mask'] = group['mask']
                continue

            # Line protocol is Up
            # Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
            # Metric threshold is Down (no route)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_dict['state'] = group['state']
                if group['state_description']:
                    type_dict['state_description'] = group['state_description']
                if group['delayed_state']:
                    delayed_dict = type_dict.setdefault('delayed', {})
                    delayed_dict['delayed_state'] = group['delayed_state']
                if group['secs_remaining']:
                    delayed_dict = type_dict.setdefault('delayed', {})
                    delayed_dict['secs_remaining'] = \
                        float(group['secs_remaining'])
                if group['connection_state']:
                    delayed_dict = type_dict.setdefault('delayed', {})
                    delayed_dict['connection_state'] = \
                        group['connection_state']
                continue

            # 1 change, last change 00:00:27
            m = p3.match(line)
            if m:
                group = m.groupdict()
                type_dict['change_count'] = int(group['change_count'])
                type_dict['last_change'] = group['last_change']
                continue

            # Delay up 20 secs, down 10 secs
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group['delay_up_secs']:
                    parsed_dict['delay_up_secs'] = \
                        float(group['delay_up_secs'])
                if group['delay_down_secs']:
                    parsed_dict['delay_down_secs'] = \
                        float(group['delay_down_secs'])
                continue

            # First-hop interface is unknown (was Ethernet1/0)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['first_hop_interface_state']:
                    parsed_dict['first_hop_interface_state'] = \
                        group['first_hop_interface_state']
                if group['prev_first_hop_interface']:
                    parsed_dict['prev_first_hop_interface'] = \
                        group['prev_first_hop_interface']
                continue

            # Metric threshold down 255 up 254
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['threshold_down']:
                    type_dict['threshold_down'] = \
                        int(group['threshold_down'])
                if group['threshold_up']:
                    type_dict['threshold_up'] = \
                        int(group['threshold_up'])
                continue

            # VRRP GigabitEthernet3.420 10
            # HSRP Ethernet0/0 3
            # HSRP Ethernet0/1 3
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tracked_by_dict = parsed_dict.setdefault('tracked_by', {})
                tracker_index = len(tracked_by_dict) + 1
                tracker_dict = tracked_by_dict.setdefault(tracker_index, {})
                tracker_dict['name'] = group['name']
                if group['interface']:
                    tracker_dict['interface'] = group['interface']
                if group['group_id']:
                    tracker_dict['group_id'] = group['group_id']
                continue

        return parsed_dict

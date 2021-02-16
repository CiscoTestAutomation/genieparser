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
        'tracks':{
            Any(): {
                'type': str,
                Optional('name'): str,
                Optional('ip_address'): str,
                Optional('subnet_mask'): str,
                'parameter': str,
                Any(): {
                    'parameter_state': str,
                    Optional('issue'): str,
                    Optional('delayed'): {
                        Optional('delayed_state'): str,
                        Optional('seconds_remaining'): float,
                        Optional('connection_state'): str,
                    },
                    'change_count': int,
                    'last_change': str,
                    Optional('threshold_down'): int,
                    Optional('threshold_up'): int,
                },
                Optional('delay_up_seconds'): float,
                Optional('delay_down_seconds'): float,
                Optional('first_hop_interface_state'): str,
                Optional('prev_first_hop_interface'): str,
                Optional('tracked_by') : {
                    Any(): {   #increasing index 0, 1, 2, 3, ...
                        'name': str,
                        'interface': str,
                        Optional('group_id'): str,
                    }
                }
            }
        }
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

        #Track 1
        p1 = re.compile(r'^Track +(?P<track_number>\d+)')

        # Interface GigabitEthernet3.420 line-protocol
        # IP route 10.21.12.0 255.255.255.0 reachability
        # IP route 172.16.52.0 255.255.255.0 metric threshold
        p2 = re.compile(r'^(?P<type>IP route|Interface) +'
            r'((?P<ip_address>[\d.]+) +(?P<subnet_mask>[\d.]+)|'
            r'(?P<name>[\d\w.]+)) +(?P<parameter>[\w \-]+)')

        # Line protocol is Up
        # Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
        # Metric threshold is Down (no route)
        p3 = re.compile(r'^(?P<parameter>[\w ]+) +is +'
            r'(?P<parameter_state>Up|Down)'
            r'( +\((?P<issue>[\w ]+)\),*( delayed (?P<delayed_state>Up|Down)'
            r' \((?P<seconds_remaining>\d+) sec remaining\)'
            r' \((?P<connection_state>\w+)\))*)*')

        # 1 change, last change 00:00:27
        p4 = re.compile(r'^(?P<change_count>\d+) +change, +last +change'
            r' +(?P<last_change>[\d:]+)')

        # Delay up 20 secs, down 10 secs
        p5 = re.compile(r'^Delay +up +(?P<delay_up_seconds>\d+)'
            r' +secs,* +down +(?P<delay_down_seconds>\d+) +sec')

        # First-hop interface is unknown (was Ethernet1/0)
        p6 = re.compile(r'^First-hop +interface +is +'
            r'(?P<first_hop_interface_state>\w+)( +\(was'
            r' +(?P<prev_first_hop_interface>[\w\d\/\.\-\_]+)\))*')

        # Metric threshold down 255 up 254
        p7 = re.compile(r'^Metric +threshold +down'
            r' +(?P<threshold_down>\d+) +up +(?P<threshold_up>\d+)')

        # VRRP GigabitEthernet3.420 10
        # HSRP Ethernet0/0 3
        # HSRP Ethernet0/1 3
        p8 = re.compile(r'^(?P<name>[a-zA-Z]{3,4}) +'
            r'(?P<interface>[A-Za-z0-9/.]+) +((?P<group_id>\d+)|(\n))')

        for line in output.splitlines():
            line = line.strip()

            #Track 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                track_number = int(group['track_number'])
                track_dict = parsed_dict.setdefault('tracks', {})\
                    .setdefault(track_number, {})
                continue

            # Interface GigabitEthernet3.420 line-protocol
            # IP route 10.21.12.0 255.255.255.0 reachability
            # IP route 172.16.52.0 255.255.255.0 metric threshold
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['name']:
                    track_dict['name'] = group['name']
                if group['ip_address']:
                    track_dict['ip_address'] = group['ip_address']
                if group['subnet_mask']:
                    track_dict['subnet_mask'] = group['subnet_mask']

                track_dict['type'] = group['type']
                track_dict['parameter'] = group['parameter']
                continue

            # Line protocol is Up
            # Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
            # Metric threshold is Down (no route)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parameter_object_name = group['parameter'].lower()\
                    .replace(' ', '_')\
                    .replace('-', '_')
                parameter_dict = \
                    track_dict.setdefault(parameter_object_name, {})
                parameter_dict['parameter_state'] = group['parameter_state']
                if group['issue']:
                    parameter_dict['issue'] = group['issue']
                if group['delayed_state']:
                    delayed_dict = parameter_dict.setdefault('delayed', {})
                    delayed_dict['delayed_state'] = group['delayed_state']
                if group['seconds_remaining']:
                    delayed_dict = parameter_dict.setdefault('delayed', {})
                    delayed_dict['seconds_remaining'] = \
                        float(group['seconds_remaining'])
                if group['connection_state']:
                    delayed_dict = parameter_dict.setdefault('delayed', {})
                    delayed_dict['connection_state'] = \
                        group['connection_state']
                continue

            # 1 change, last change 00:00:27
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parameter_dict['change_count'] = int(group['change_count'])
                parameter_dict['last_change'] = group['last_change']
                continue

            # Delay up 20 secs, down 10 secs
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['delay_up_seconds']:
                    track_dict['delay_up_seconds'] = \
                    float(group['delay_up_seconds'])
                if group['delay_down_seconds']:
                    track_dict['delay_down_seconds'] = \
                        float(group['delay_down_seconds'])
                continue

            # First-hop interface is unknown (was Ethernet1/0)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['first_hop_interface_state']:
                    track_dict['first_hop_interface_state'] = \
                        group['first_hop_interface_state']
                if group['prev_first_hop_interface']:
                    track_dict['prev_first_hop_interface'] = \
                        group['prev_first_hop_interface']
                continue

            # Metric threshold down 255 up 254
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if group['threshold_down']:
                    parameter_dict['threshold_down'] = \
                        int(group['threshold_down'])
                if group['threshold_up']:
                    parameter_dict['threshold_up'] = \
                        int(group['threshold_up'])
                continue

            # VRRP GigabitEthernet3.420 10
            # HSRP Ethernet0/0 3
            # HSRP Ethernet0/1 3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                tracked_by_dict = track_dict.setdefault('tracked_by', {})
                tracker_index = len(tracked_by_dict) + 1
                tracker_dict = tracked_by_dict.setdefault(tracker_index, {})
                tracker_dict['name'] = group['name']
                if group['interface']:
                    tracker_dict['interface'] = group['interface']
                if group['group_id']:
                    tracker_dict['group_id'] = group['group_id']
                continue

        return parsed_dict

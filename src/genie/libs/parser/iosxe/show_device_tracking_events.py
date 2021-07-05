''' ShowDeviceTrackingEvents.py

IOSXE parsers for the following show commands:

    * show device-tracking events

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from pprint import pprint

# ====================================================
# Schema for 'show device-tracking events'
# ====================================================
class ShowDeviceTrackingEventsSchema(MetaParser):
    """ Schema for show device-tracking events """

    schema = {
        'events': {
              str:{
                int: {
                  "event_type": str,
                  Optional('event_name'): str, 
                  Optional('event_state'): str,
                  Optional('event_prev_state'): str,
                  Optional('entry_state'): str,
                  Optional('fsm_name'): str,
                  Optional('fsm_state'): str,
                  Optional(Any()): str,
                  Optional(Any()): str,
                  "ssid": str,
                  "timestamp": str
                }
            }
        }
    }

# =============================================
# Parser for 'show device-tracking events'
# =============================================
class ShowDeviceTrackingEvents(ShowDeviceTrackingEventsSchema):
    """ show device-tracking events """

    cli_command = 'show device-tracking events'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # timestamp and ssid
        p = re.compile(r'^(?P<timestamp>.+\])\s+(?P<ssid>\S+\s+\d+)')

        #fsm_run event 
        p1 = re.compile(r"^.+(?<=\sFSM)(?P<fsm_name>.*)(?=\srunning)\s+(?P<fsm_state>\S+).+(?P<event_name>(?<=event\s{1})\S+).+(?P<event_state>(?<=state\s{1})\S+)$")

        #fsm_transition event 
        p2 = re.compile(r'.+\s+\d+\s+\S+\s+\S+\s+(?P<prev_state>\S+)\s+\S+\s+(?P<state>\S+).+\s(?P<event_name>(?<=event\s{1})\S+)$')

        #create bt entry, #bt_entry event
        p3 = re.compile(r'^.+\s+\d+\s+(?P<entry_state>\S+\s+\S+\s+\S+)\s+(?P<mac_addr_type>\S+\s\S+)\s+(?P<mac_addr>([\w\d]{4}\.*){3})\s+(?P<ip_addr_type>\S+)\s+(?P<ip_addr>[\w\d\.:]+)$')    

        #bt entry changed state, #bt_entry event
        p4 = re.compile(r'^(.+\s+\d+\s+\S+\s+\S+\s+(?P<entry_state>\S+\s+\S+)\s+(?P<mac_addr_type>\S+\s\S+)\s+(?P<mac_addr>([\w\d]{4}\.*){3})\s+(?P<ip_addr_type>\S+)\s+(?P<ip_addr>[\w\d\.:]+)$)')

        parser_dict = {}
        ssid_event_no_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p.match(line)
            
            if m:
                events = parser_dict.setdefault('events', {})
                ssid = m.groupdict()['ssid']
                events.setdefault(ssid, {})
                ec = ssid_event_no_dict.setdefault(ssid, 1)
                timestamp = m.groupdict()['timestamp']
                event_no = ssid_event_no_dict[ssid]
                m1 = p1.match(line)
                
                if m1:
                    event = {}
                    event.update({'ssid': ssid})
                    event.update({'event_type': 'fsm_run'})
                    event.update({'event_name': m1.groupdict()['event_name']})
                    event.update({'fsm_name': m1.groupdict()['fsm_name']})
                    event.update({'fsm_state': m1.groupdict()['fsm_state']})
                    event.update({'timestamp': timestamp})
                    events[ssid][event_no] = event
                    ssid_event_no_dict[ssid]+=1
                    continue
            
                m2 = p2.match(line)
                if m2:
                    event = {}
                    event.update({'ssid':  ssid})
                    event.update({'event_type':  'fsm_transition'})
                    event.update({'event_name':  m2.groupdict()['event_name']})
                    event.update({'state':  m2.groupdict()['state']})
                    event.update({'prev_state':  m2.groupdict()['prev_state']})
                    event.update({'timestamp':  timestamp})
                    events[ssid][event_no] = event
                    ssid_event_no_dict[ssid]+=1
                    continue
                    
                m3 = p3.match(line)
                if m3:
                    event = {}
                    mac_addr_type = m3.groupdict()['mac_addr_type']
                    ip_addr_type = m3.groupdict()['ip_addr_type']
                    event.update({'ssid': ssid})
                    event.update({'event_type': 'bt_entry'})
                    event.update({'entry_state': m3.groupdict()['entry_state']})
                    event.update({mac_addr_type: m3.groupdict()['mac_addr']})
                    event.update({ip_addr_type: m3.groupdict()['ip_addr']})
                    event.update({'timestamp': timestamp})
                    events[ssid][event_no] = event
                    ssid_event_no_dict[ssid]+=1
                    continue
            
                m4 = p4.match(line)
                if m4:
                    event = {}
                    mac_addr_type = m4.groupdict()['mac_addr_type']
                    ip_addr_type = m4.groupdict()['ip_addr_type']
                    event.update({'ssid': ssid})
                    event.update({'event_type': 'bt_entry'})
                    event.update({'entry_state': m4.groupdict()['entry_state']})
                    event.update({mac_addr_type: m4.groupdict()['mac_addr']})
                    event.update({ip_addr_type: m4.groupdict()['ip_addr']})
                    event.update({'timestamp': timestamp})
                    events[ssid][event_no] = event
                    ssid_event_no_dict[ssid]+=1
                    continue

        return parser_dict

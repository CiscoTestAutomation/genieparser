"""starOS implementation of show_alarm_all.py

"""
import re
import pprint
from string import capwords
from typing import Optional
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema, Optional

class ShowAlarmAllSchema(MetaParser):
    """Schema for show alarm all"""

    schema = {
        'alarms': {
            Any(): {
                'Current': {
                    'TOTAL': str,
                    'CRITICAL': str,
                    'MAJOR': str,
                    'MINOR': str
                },
                'Cumulative': {
                    'TOTAL': str,
                    'CRITICAL': str,
                    'MAJOR': str,
                    'MINOR': str
                },
            },
            'LAST_AL': str,
            Optional('OA'): {
                Any(): {
                    'SEV': str,
                    'EVENT': str
                },
            },
        }
    }


class ShowAlarmAll(ShowAlarmAllSchema):
    """Parser for show alarm all"""

    cli_command = 'show alarm all'

    """
Monday June 27 11:05:49 ART 2022
Facility Alarm Information:

Audible Alarm OFF
Note: Audible Alarm is Disabled
All Central Office (CO) alarms are off

Alarm Statistics:
  Current Outstanding Alarms
    Total:    5
    Critical: 0
    Major:    0
    Minor:    5
  Cumulative Totals
    Total:    7
    Critical: 0
    Major:    0
    Minor:    7
  Last Alarm Received: Thursday June 16 15:51:31 ART 2022

Outstanding Alarms:

Sev Object          Event
--- ----------      --------------------------------------------------------------------------------------------
MN  Card 7          The Packet Services Card 2 in slot 7 is a single point of failure. Another Packet Services Card 2 of the same type is needed.
MN  Card 10         The Packet Services Card 2 in slot 10 is a single point of failure. Another Packet Services Card 2 of the same type is needed.
MN  Card 11         The Packet Services Card 2 in slot 11 is a single point of failure. Another Packet Services Card 2 of the same type is needed.
MN  Port 23/1       Port link down
MN  Card 26         The 10 Gig Ethernet Line Card in slot 26 is a single point of failure. A 10 Gig Ethernet Line Card is needed in slot 23     
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        alarm_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(Current Outstanding Alarms$)')
        p2 = re.compile(r'^((Total:\s+)(?P<total>\d+))')
        p3 = re.compile(r'^(Critical:\s+(?P<crit>\d+))')
        p4 = re.compile(r'^(Major:\s+(?P<maj>\d+))')
        p5 = re.compile(r'^(Minor:\s+(?P<min>\d+))')
        p6 = re.compile(r'^(Cumulative Totals$)')
        p7 = re.compile(r'^(Last Alarm Received:\s(?P<last_alm_date>\w+\s\w+\s\d+\s\d+:\d+:\d+\s\w+\s\d+))')
        p8 = re.compile(r'^((?P<sev>CR|MJ|MN)\s+\w+\s(?P<card>\d+|\d+.\d)\s+(?P<event>.+$))')

        i = 0
        for line in out.splitlines():
            line = line.strip()

            if i==1:
                #Match en linea anterior a 'Current Outstanding Alarms'
                m2 = p2.match(line)
                if m2:
                    #Current total
                     if 'alarms' not in alarm_dict:
                        result_dict = alarm_dict.setdefault('alarms', {}).setdefault('Statistics', {})

                     curr_total = m2.groupdict()['total']
                     continue

                m3 = p3.match(line)  
                if m3:
                    #Current Critical
                     curr_crit = m3.groupdict()['crit']
                     continue

                m4 = p4.match(line)  
                if m4:
                    #Current Major
                     curr_maj = m4.groupdict()['maj']
                     continue               

                m5 = p5.match(line)  
                if m5:
                    #Current Minor
                     curr_min = m5.groupdict()['min']
                     i = 0
                     continue 

            if i==2:
                #Match en linea anterior a 'Cumulative Totals'
                m2 = p2.match(line)
                if m2:
                    #Cumulative total
                     cum_total = m2.groupdict()['total']
                     continue

                m3 = p3.match(line)  
                if m3:
                    #Cumulative Critical
                    cum_crit = m3.groupdict()['crit']
                    continue

                m4 = p4.match(line)  
                if m4:
                    #Current Major
                    cum_maj = m4.groupdict()['maj']
                    continue               

                m5 = p5.match(line)  
                if m5:
                    #Current total
                    cum_min = m5.groupdict()['min']
                    result_dict['Current'] = {}
                    result_dict['Current']['TOTAL'] = curr_total
                    result_dict['Current']['CRITICAL'] = curr_crit
                    result_dict['Current']['MAJOR'] = curr_maj
                    result_dict['Current']['MINOR'] = curr_min
                    result_dict['Cumulative'] = {}
                    result_dict['Cumulative']['TOTAL'] = cum_total
                    result_dict['Cumulative']['CRITICAL'] = cum_crit
                    result_dict['Cumulative']['MAJOR'] = cum_maj
                    result_dict['Cumulative']['MINOR'] = cum_min
                    i=0
                    continue 

            m1 = p1.match(line)
            if m1:
            #Empiezan valores de Current Outstanding
                i=1
                continue

            m6 = p6.match(line)
            if m6:
            #Empiezan valores de Cumulativa Totals
                i=2
                continue

            m7 = p7.match(line)    
            #Last Alarm Received    
            if m7:
                result_dict = alarm_dict.setdefault('alarms')
                last_al = m7.groupdict()['last_alm_date']
                result_dict['LAST_AL'] = last_al
                continue

            m8 = p8.match(line)
            #Lista Alarm Events
            if m8:
                if 'OA' not in alarm_dict:
                    result_dict = alarm_dict.setdefault('alarms').setdefault('OA', {})
                sev = m8.groupdict()['sev']
                card = m8.groupdict()['card']
                event = m8.groupdict()['event']
                result_dict[card] = {}
                result_dict[card]['SEV'] = sev
                result_dict[card]['EVENT'] = event
                continue    

        return alarm_dict
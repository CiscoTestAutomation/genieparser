''' show_alarm.py
IOSXE parsers for the following show commands:
    * show alarm profile
    * show alarm settings
    * show facility-alarm status
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Schema for 'show alarm profile'
# =============================================

class ShowAlarmProfileSchema(MetaParser):
    """
    Schema for show alarm profile
    """
    schema = {
                Any() : {
                     Optional('interfaces'): list,
                     Optional('alarms'): str,
                     Optional('syslog'): str,
                     Optional('notifies'): str,
                     Optional('relay_major'): str,
                },
        }
# =============================================
# Parser for 'show alarm profile'
# =============================================

class ShowAlarmProfile(ShowAlarmProfileSchema):
    """Parser for show alarm profile
    """
    cli_command = 'show alarm profile'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}
        p1= re.compile(r'alarm\sprofile\s(?P<profile>(\w+)):')
        p2 = re.compile(r'Interfaces(?P<interfaces>(\s+[\w\-\s\,\/]+)?)')
        p3 = re.compile(r'Alarms(?P<alarms>(\s+[\w\-\s\,]+)?)')
        p4 = re.compile(r'Syslog(?P<syslog>(\s+[\w\-\s\,]+)?)')
        p5 = re.compile(r'Notifies(?P<notifies>(\s+[\w\-\s\,]+)?)')
        p6 = re.compile(r'Relay Major(?P<relay_major>(\s+[\w\-\s\,]+)?)')

        profile = ''
        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({group['profile'] : {} })
                profile = group['profile']
            if profile:
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[profile].update({'interfaces': group['interfaces'].strip().split(" ")})
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[profile].update({'alarms' : group['alarms'].strip()})
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[profile].update({'syslog' : group['syslog'].strip()})
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[profile].update({'notifies' : group['notifies'].strip()})
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[profile].update({'relay_major' : group['relay_major'].strip()})
                    profile = ''

        return ret_dict

# =============================================
# Schema for 'show alarm settings'
# =============================================

class ShowAlarmSettingsSchema(MetaParser):
    """
    Schema for show alarm settings
    """
    schema = {
            'alarm_relay_mode' : str,
            'power_supply' : {
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            'temperature_primary':{
                Optional('alarm') : str,
                Optional('threshold'): {
                    Optional('max_temp'): str,
                    Optional('min_temp'): str,
                    },
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            'temperature_secondary':{
                Optional('alarm') : str,
                Optional('threshold'): {
                    Optional('max_temp'): str,
                    Optional('min_temp'): str,
                    },
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            'sd_card':{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            'input_alarm_1':{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            'input_alarm_2':{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            Optional('input_alarm_3'):{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            Optional('input_alarm_4'):{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            Optional('ptp'):{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                },
            Optional('dlr'):{
                Optional('alarm') : str,
                Optional('relay') : str,
                Optional('notifies') : str,
                Optional('syslog') : str,
                }
            }
# =============================================
# Parser for 'show alarm settings'
# =============================================

class ShowAlarmSettings(ShowAlarmSettingsSchema):
    """
    Schema for show alarm settings
    """
    cli_command = 'show alarm settings'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        pa = re.compile(r'Alarm(?P<alarm>((\s+\w+))?)')
        pb = re.compile(r'Threshold(s)?(?P<threshold>([\w\:\s\d\-\+]+)?)')
        pb1 = re.compile(r'MAX:\s+(?P<max_temp>(\+?\-?\d+C))\s+MIN:\s+(?P<min_temp>(\+?\-?\d+C))')
        pc = re.compile(r'Relay(?P<relay>((\s+\w+)?))')
        pd = re.compile(r'Notifies(?P<notifies>((\s+\w+)?))')
        pe = re.compile(r'Syslog(?P<syslog>((\s+\w+)?))')
        
        p1= re.compile(r'Alarm relay mode:\s(?P<status>(\w+))')
        p2 = re.compile(r'Power Supply')
        p3 = re.compile(r'Temperature-Primary')
        p4 = re.compile(r'Temperature-Secondary')
        p5 = re.compile(r'SD-Card')
        p6 = re.compile(r'Input-Alarm 1')
        p7 = re.compile(r'Input-Alarm 2')
        p8 = re.compile(r'Input-Alarm 3')
        p9 = re.compile(r'Input-Alarm 4')
        p10 = re.compile(r'PTP')
        p11 = re.compile(r'DLR')
        item = ''

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'alarm_relay_mode' : group['status'] })
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'power_supply' : {}})
                item = 'power_supply'
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'temperature_primary' : {}})
                item = 'temperature_primary'
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'temperature_secondary' : {}})
                item = 'temperature_secondary'
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'sd_card' : {}})
                item = 'sd_card'
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'input_alarm_1' : {}})
                item = 'input_alarm_1'
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'input_alarm_2' : {}})
                item = 'input_alarm_2'
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'input_alarm_3' : {}})
                item = 'input_alarm_3'
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'input_alarm_4' : {}})
                item = 'input_alarm_4'
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'ptp' : {}})
                item = 'ptp'
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dlr' : {}})
                item = 'dlr'
            if item:
                m = pa.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[item].update({'alarm' : group['alarm'].strip() })
                m = pb.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[item].update({'threshold' : {} })
                    if group['threshold']:
                        ret_dict[item].update({'threshold' : {} })
                        m = pb1.match(group['threshold'].strip())
                        if m:
                            group = m.groupdict()
                            ret_dict[item]['threshold'].update(group)
                m = pc.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[item].update({'relay' : group['relay'].strip() })
                m = pd.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[item].update({'notifies' : group['notifies'].strip() })
                m = pe.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict[item].update({'syslog' : group['syslog'].strip() })
                    item = ''
        return ret_dict

# =============================================
# Schema for 'show facility-alarm status'
# =============================================

class ShowFacilityAlarmStatusSchema(MetaParser):
    """
    Schema for show facility-alarm status
    """
    schema = {
                'alarms' : {
                    Any() : {
                        Optional('severity'): str,
                        Optional('description'): str,
                        Optional('relay'): str,
                        Optional('time'): str,
                        Optional('index'): int,
                        },
                    }
                }

# =============================================
#Parser for 'show facility-alarm status'
# =============================================

class ShowFacilityAlarmStatus(ShowFacilityAlarmStatusSchema):
    """Parser for show facility-alarm status
    """
    cli_command = 'show facility-alarm status'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        #Source                 Severity Description                         Relay    Time
        p1 = re.compile(r'Source\s+Severity\s+Description\s+Relay\s+Time')

        #GigabitEthernet1/8       MAJOR    1 Link Fault                        MAJ      Mar 02 2023 10:19:20
        p2 = re.compile(r'(?P<source>([\w\/\d\-\_]+))\s\s+(?P<severity>([A-Z]+))\s\s+(?P<description>([\w\s\d]+))\s\s+(?P<relay>([A-Z]+))\s\s+(?P<time>([\w\d\s\:]+))')
        
        # Source                     Time                   Severity      Description [Index]
        p3 = re.compile(r'^Source(\s+Time)\s+Severity\s+Description(\s+\[Index])$')

        # Power Supply Bay 0         Jan 23 2024 17:18:47   CRITICAL      Power Supply/FAN Module Missing [0]
        # TenGigabitEthernet0/0/0    Jan 21 2024 19:15:56   CRITICAL      Physical Port Link Down [1]
        # xcvr container 0/0/3       Jan 21 2024 19:15:56   CRITICAL      Transceiver Missing - Link Down [1]
        p4 = re.compile(r'^(?P<source>([\w\/\d\-\_ ]+))\s\s+()?(?P<time>([\w\d\s\:]+))\s\s+(?P<severity>([A-Z]+))\s\s+(?P<description>([\w\s\d\/\/\-]+))\s+(\[(?P<index>(\d+))\])$')
        
        for line in out.splitlines():
            line = line.strip()

            #Source                 Severity Description                         Relay    Time
            m = p1.match(line)
            if m:
                root_dict = ret_dict.setdefault('alarms', {})
                continue

            #GigabitEthernet1/8       MAJOR    1 Link Fault                        MAJ      Mar 02 2023 10:19:20
            m = p2.match(line)
            if m:
                group = m.groupdict()
                alarm_dict = root_dict.setdefault(group['source'] , {})
                alarm_dict.update({'severity' : group['severity'].strip() , 'description':group['description'].strip(), 'relay' : group['relay'].strip() , 'time' : group['time'].strip() })
            
            # Source                     Time                   Severity      Description [Index]
            m = p3.match(line)
            if m:
                root_dict = ret_dict.setdefault('alarms', {})
                continue

            # Power Supply Bay 0         Jan 23 2024 17:18:47   CRITICAL      Power Supply/FAN Module Missing [0]
            # TenGigabitEthernet0/0/0    Jan 21 2024 19:15:56   CRITICAL      Physical Port Link Down [1]
            # xcvr container 0/0/3       Jan 21 2024 19:15:56   CRITICAL      Transceiver Missing - Link Down [1]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                alarm_dict = root_dict.setdefault(group['source'].strip().replace(" ","_").lower() , {})
                alarm_dict.update({'severity' : group['severity'].strip() , 'description':group['description'].strip(), 'index' : int(group['index'].strip()), 'time' : group['time'].strip() })

        return ret_dict



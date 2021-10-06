# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ==============================
# Schema for 'show environment'
# ==============================
class ShowEnvironmentSchema(MetaParser):

    ''' Schema for "show environment" '''

# These are the key-value pairs to add to the parsed dictionary
    schema = {
        'power_supply': {
            Any() : {
                Optional('volt') : float,
                Optional('status') : str
            }
        },
        'fan': {
            Any() : {
                Optional('status') : str,
                Optional('running_percent_speed') : int
            }
        },
        'board_temperature' : {
            'board_temperature_status' : str,
            Any() : {
                Optional('temp_cels') : int,
                Optional('status') : str,
                Optional('warning_status') : str,
                Optional('high_threshold') : int,
                Optional('low_threshold') : int
            }
        },
        'board_temperature_alert' : {
            Any() : {        
                Optional('warning_status') : str,
                Optional('high_threshold') : int,
                Optional('low_threshold') : int
            }
        },
        'environmental_events' : {
            Any() : {
                Optional('env_event') : str,
                Optional('env_state') : str,
                Optional('env_time')  : str
            }
        },
        Optional('external_alarms') : {
            Any() : {
                Optional('alarm_assert_status') : str
            }
        }
    }

# Python (this imports the Python re module for RegEx)
import re

# ==============================
# Parser for 'show environment ASR901'
# ==============================

# The parser class inherits from the schema class
class ShowEnvironment(ShowEnvironmentSchema):

    ''' Parser for "show environment" on ASR901 Platforms
    ASR901-6Z-CALO#show environment 
        Power Supply Status:
        12AV  Supply: +12.010 V Normal
        1.5V  Supply: +1.500 V Normal
        12BV  Supply: +12.010 V Normal
        2.5V  Supply: +2.500 V Normal
        1.05V Supply: +1.090 V Normal
        1.2V  Supply: +1.200 V Normal
        1.8V  Supply: +1.800 V Normal
        0.75V Supply: +0.750 V Normal
        1V    Supply: +1.000 V Normal
        3.3V  Supply: +3.280 V Normal
        5V    Supply: +4.980 V Normal
        Fan Status:
        Fan 1 Operation: Normal, is running at 53   percent speed 

        Fan 2 Operation: Normal, is running at 53   percent speed 

        Fan 3 Operation: Normal, is running at 54   percent speed 


        Alert settings:
        Board temperature, temperature warning: Enabled
        Threshold: 90 (high) -40 (low) DegC
        Inlet temperature, temperature warning: Enabled
        Threshold: 80 (high) -40 (low) DegC
        Board Temperature: Normal
        Board temperature,  temperature = 37 (C), Normal
        Inlet temperature,  temperature = 25 (C), Normal

        Environmental monitor experienced the following events:
        SeqNum           Event              State             Time
            1  :  Environmental monitor : "started " at 03:34:30 UTC Mon Aug 24 2015.


        External Alarms :

        ALARM CONTACT 1 is asserted
        ALARM CONTACT 2 is asserted
        ALARM CONTACT 3 is asserted
        ALARM CONTACT 4 is asserted
    '''

    cli_command = 'show environment'


    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        
        # Init vars
        env_dic = {}

        #12AV  Supply: +11.970 V Normal
        p1 = re.compile(r'^\s*(?P<ps>[0-9]*\.?[0-9]*.V)+\s*Supply: +(?P<volt>[+-]?([0-9]*[.])?[0-9]+)+\sV\s+(?P<status>.*$)')

        #Fan 1 Operation: Normal, is running at 13   percent speed 
        p2 = re.compile(r'Fan\s+(?P<fan>\d)+\sOperation:\s+(?P<status>.*), is running at\s+(?P<speed>\d*)')

        #Fan 2 Operation: Failed
        p3 = re.compile(r'Fan\s+(?P<fan>\d)+\sOperation:\s+(?P<status>Failed$)')

        #Board temperature,  temperature = 41 (C), Normal
        p4 = re.compile(r'(?P<sensor>[a-zA-Z]*) temperature,  temperature = +(?P<temp>[0-9]*).*,(?P<status>.*$)')

        #Board Temperature: Normal
        p5 = re.compile(r'Board Temperature: (?P<board_temperature>[a-zA-Z]*)$')

        #Board temperature, temperature warning: Enabled        
        p6 = re.compile(r'^\s*(?P<sensor>[a-zA-Z]*) temperature, temperature warning: (?P<temperature_warning>[a-zA-Z]*)')

        #Threshold: 80 (high) -40 (low) DegC
        p7 = re.compile(r'\s*Threshold:\s(?P<high_warning>[0-9]*)\s\(high\)\s(?P<low_warning>-[0-9]*)\s\(low\) DegC$')

        # 270  :  12AV Power supply      : "failed  " at 08:53:24 CDT Thu Apr 15 2021.
        p8 = re.compile(r'^\s*(?P<SeqNum>[0-9]*)\s*:\s*(?P<event>[A-Za-z0-9\s]*)\s:\s\"(?P<state>[A-Za-z0-9\s]*)\" at (?P<time>[A-Za-z0-9\s\:]*)\.$')

        # ALARM CONTACT 1 is not asserted
        p9 = re.compile(r'^ALARM CONTACT (?P<alarm_contact>[0-9]) is (?P<alarm_assert_status>[A-Za-z\s]*)$')

        sensor_warning = ""
        temp_warning_status = ""

        for line in output.splitlines():
            line = line.strip()

            #12AV  Supply: +11.970 V Normal
            m = p1.match(line)
            if m:
                if 'PowerSupply' not in env_dic:
                    result_dict = env_dic.setdefault('power_supply',{})

                ps     = m.groupdict()['ps']
                volt   = m.groupdict()['volt']
                status = m.groupdict()['status']

                result_dict[ps] = {}

                result_dict[ps]['volt']   = float(volt)
                result_dict[ps]['status'] = status
                continue

            #Fan 1 Operation: Normal, is running at 13   percent speed
            m = p2.match(line)
            if m: 
                if 'fan' not in env_dic:
                    result_dict = env_dic.setdefault('fan',{})

                fan    = m.groupdict()['fan']
                status = m.groupdict()['status']
                speed  = m.groupdict()['speed'] 

                result_dict[fan] = {}
                result_dict[fan]['status'] = status
                result_dict[fan]['running_percent_speed']  = int(speed)
                continue

            #Fan 2 Operation: Failed
            m = p3.match(line)
            if m: 
                if 'fan' not in env_dic:
                    result_dict = env_dic.setdefault('fan',{})

                fan    = m.groupdict()['fan']
                status = m.groupdict()['status']

                result_dict[fan] = {}
                result_dict[fan]['status'] = status
                result_dict[fan]['running_percent_speed']  = 0
                continue

            #Board temperature,  temperature = 41 (C), Normal
            m = p4.match(line)
            if m:
                if 'board_temperature' not in env_dic:
                    result_dict = env_dic.setdefault('board_temperature',{})

                sensor = m.groupdict()['sensor']
                temp   = m.groupdict()['temp']
                status = m.groupdict()['status']

                result_dict[sensor] = {}

                result_dict[sensor]['temp_cels'] = int(temp)
                result_dict[sensor]['status'] = status

                continue

            #Board Temperature: Normal
            m = p5.match(line)
            if m:
                if 'board_temperature' not in env_dic:
                    result_dict = env_dic.setdefault('board_temperature',{})

                board_temperature_status = m.groupdict()['board_temperature']

                result_dict['board_temperature_status'] = board_temperature_status

                continue

            #Board temperature, temperature warning: Enabled
            #Threshold: 80 (high) -40 (low) DegC
            m = p6.match(line)
            if m:
                sensor_warning      = m.groupdict()['sensor']
                temp_warning_status = m.groupdict()['temperature_warning']
                
            #Threshold: 80 (high) -40 (low) DegC
            m = p7.match(line)
            if m:
                if 'board_temperature_alert' not in env_dic:
                    result_dict = env_dic.setdefault('board_temperature_alert',{})

                high_warning = m.groupdict()['high_warning']
                low_warning  = m.groupdict()['low_warning']
                

                result_dict[sensor_warning] = {}

                result_dict[sensor_warning]['warning_status'] = temp_warning_status
                result_dict[sensor_warning]['high_threshold'] = int(high_warning)
                result_dict[sensor_warning]['low_threshold']  = int(low_warning)

                sensor_warning      = ''
                temp_warning_status = ''

                continue
            
            #     270  :  12AV Power supply      : "failed  " at 08:53:24 CDT Thu Apr 15 2021.
            m = p8.match(line)
            if m:
                if 'environmental_events' not in env_dic:
                    result_dict = env_dic.setdefault('environmental_events',{})

                seq_num = m.groupdict()['SeqNum']
                event = m.groupdict()['event'] 
                state = m.groupdict()['state'] 
                time = m.groupdict()['time']
                
                result_dict[seq_num] = {}

                result_dict[seq_num]['env_event'] = event.strip()
                result_dict[seq_num]['env_state'] = state.strip()
                result_dict[seq_num]['env_time'] = time.strip()

                continue

            # ALARM CONTACT 1 is not asserted
            m = p9.match(line)
            if m:
                if 'external_alarms' not in env_dic:
                    result_dict = env_dic.setdefault('external_alarms',{})
                
                alarm_contact = m.groupdict()['alarm_contact']
                status        = m.groupdict()['alarm_assert_status']

                result_dict[alarm_contact] = {}

                result_dict[alarm_contact]['alarm_assert_status'] = status

                continue
            
        return env_dic


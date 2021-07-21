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
        'PowerSupply': {
            Any() : {
                Optional('volt') : str,
                Optional('status') : str
            }
        },
        'Fan': {
            Any() : {
                Optional('status') : str,
                Optional('speed') : str
            }
        },
        'Sensor' : {
            Any() : {
                Optional('temp') : str,
                Optional('status') : str
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
    R04-TA1827R-A901-01#show environment 
        Power Supply Status:
        12AV  Supply: +11.970 V Normal
        1.5V  Supply: +1.490 V Normal
        1.25V Supply: +1.210 V Normal
        12BV  Supply: +11.970 V Normal
        2.5V  Supply: +2.490 V Normal
        1.05V Supply: +1.090 V Normal
        1.2V  Supply: +1.200 V Normal
        1.8V  Supply: +1.790 V Normal
        Fan Status:
        Fan 1 Operation: Normal, is running at 13   percent speed 

        Fan 2 Operation: Normal, is running at 13   percent speed 


        Alert settings:
        Board temperature, temperature warning: Enabled
        Threshold: 80 (high) -40 (low) DegC
        Board Temperature: Normal
        Board temperature,  temperature = 41 (C), Normal

        Environmental monitor experienced the following events:
        SeqNum           Event              State             Time
            1  :  Environmental monitor : "started " at 14:48:28 CDT Tue Jul 13 2021.


        External Alarms :

    ALARM CONTACT 1 is not asserted
    ALARM CONTACT 2 is not asserted
    ALARM CONTACT 3 is not asserted
    ALARM CONTACT 4 is not asserted
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

        for line in output.splitlines():
            line = line.strip()

            #12AV  Supply: +11.970 V Normal
            m = p1.match(line)
            if m:
                if 'PowerSupply' not in env_dic:
                    result_dict = env_dic.setdefault('PowerSupply',{})

                ps     = m.groupdict()['ps']
                volt   = m.groupdict()['volt']
                status = m.groupdict()['status']

                result_dict[ps] = {}

                result_dict[ps]['volt']   = volt
                result_dict[ps]['status'] = status
                continue

            #Fan 1 Operation: Normal, is running at 13   percent speed
            m = p2.match(line)
            if m: 
                if 'Fan' not in env_dic:
                    result_dict = env_dic.setdefault('Fan',{})

                fan    = m.groupdict()['fan']
                status = m.groupdict()['status']
                speed  = m.groupdict()['speed'] 

                result_dict[f'fan{fan}'] = {}
                result_dict[f'fan{fan}']['status'] = status
                result_dict[f'fan{fan}']['speed']  = speed
                continue

            #Fan 2 Operation: Failed
            m = p3.match(line)
            if m: 
                if 'Fan' not in env_dic:
                    result_dict = env_dic.setdefault('Fan',{})

                fan    = m.groupdict()['fan']
                status = m.groupdict()['status']
                speed  = m.groupdict()['speed'] 

                result_dict[f'fan{fan}'] = {}
                result_dict[f'fan{fan}']['status'] = status
                result_dict[f'fan{fan}']['speed']  = 'N/A'
                continue

            #Board temperature,  temperature = 41 (C), Normal
            m = p4.match(line)
            if m:
                if 'Sensor' not in env_dic:
                    result_dict = env_dic.setdefault('Sensor',{})

                sensor = m.groupdict()['sensor']
                temp   = m.groupdict()['temp']
                status = m.groupdict()['status']

                result_dict[sensor] = {}

                result_dict[sensor]['temp'] = temp
                result_dict[sensor]['status'] = status

                continue

        return env_dic


"""show_ignition.py
   supported commands:
     * show ignition
     
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# Genie Libs
from genie.libs.parser.utils.common import Common

class ShowIgnitionSchema(MetaParser):
    """
    Schema for show ignition 
    """

    schema = {
        'ignition_status':{
                'ignition_mgmt':str,
                'input_volt':str,
                'pwr_state':str,
                Optional('sense'):str,
                'shutdown_time':str,
                Optional('battery_type'):str,
                'undervoltage':str,
                'overvoltage':str,
                Optional('sense_on_threshold'):str,
                Optional('sense_off_threshold'):str,
                'undervoltage_time_delay':str,
                'overvoltage_time_delay':str,
                'ignition_off_time_delay':str,
            },
        }

class ShowIgnition(ShowIgnitionSchema):
    """ Parser for show ignition """

    # Parser for 'show ignition'
    cli_command = 'show ignition'

    """
        Status:
            Ignition management: Enabled
            Input voltage:       14.080 V
            Ignition status:     Power on
            Ignition Sense:      Enabled
            Shutdown timer:      0.0 s to off [will begin power down at ~100 sec]
            Config-ed battery:   12v
        Thresholds:
            Undervoltage:        9.000 V
            Overvoltage:         37.000 V
            Sense on:            13.200 V
            Sense off:           12.800 V
            Undervoltage timer:  20.0 s
            Overvoltage timer:   1.0 s
            Ignition-Off timer:  7200.0 s
    """

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
            
        # initial variables
        status_dict = {}
        result_dict = {}

        # Status:
        p1 = re.compile(r'^Status')

        # Ignition management: Enabled
        p2 = re.compile(r'^\s*Ignition management:\s(?P<ignition_mgmt>\w*)')

        # Input voltage:       14.144 V
        p3 = re.compile(r'^\s*Input voltage:\s*(?P<input_volt>\d*\.\d*\s\w)')

        # Ignition status:     Power on
        p4 = re.compile(r'^\s*Ignition status:\s*(?P<pwr_state>[\s\S]+)')

        # Ignition Sense:      Enabled
        p5 = re.compile(r'^\s*Ignition Sense:\s*(?P<sense>\w*)')

        # Shutdown timer:      0.0 s to off [will begin power down at ~100 sec]
        p6 = re.compile(r'^\s*Shutdown timer:\s*(?P<shutdown_time>[\s\S]+)')

        # Config-ed battery:   12v
        p7 = re.compile(r'^\s*Config-ed battery:\s*(?P<battery_type>\d+\w)')

        # Undervoltage:        9.000 V
        p8 = re.compile(r'^\s*Undervoltage:\s+(?P<undervoltage>[\w\s\S]+)')

        # Overvoltage:         37.000 V
        p9 = re.compile(r'^\s*Overvoltage:\s+(?P<overvoltage>[\w\s\S]+)')

        # Sense on:            13.200 V
        p10 = re.compile(r'^\s*Sense on:\s+(?P<sense_on_threshold>[\w\s\S]+)')

        # Sense off:           12.800 V
        p11 = re.compile(r'^\s*Sense off:\s+(?P<sense_off_threshold>[\w\s\S]+)')

        # Undervoltage timer:  20.0 s
        p12 = re.compile(r'^\s*Undervoltage timer:\s+(?P<undervoltage_time_delay>[\w\s\S]+)')

        # Overvoltage timer:   1.0 s
        p13 = re.compile(r'^\s*Overvoltage timer:\s+(?P<overvoltage_time_delay>[\w\s\S]+)')

        # Ignition-Off timer:  7200.0 s
        p14 = re.compile(r'^\s*Ignition-Off timer:\s+(?P<ignition_off_time_delay>[\w\s\S]+)')
        
        for line in output.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                status_dict = result_dict.setdefault('ignition_status',{})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'ignition_mgmt' : group['ignition_mgmt']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'input_volt' : group['input_volt']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'pwr_state' : group['pwr_state']})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'sense' : group['sense']})
                continue
        
            m = p6.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'shutdown_time' : group['shutdown_time']})
                continue
            
            m = p7.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'battery_type' : group['battery_type']})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'undervoltage' : group['undervoltage']})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'overvoltage' : group['overvoltage']})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'sense_on_threshold' : group['sense_on_threshold']})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'sense_off_threshold' : group['sense_off_threshold']})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'undervoltage_time_delay' : group['undervoltage_time_delay']})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'overvoltage_time_delay' : group['overvoltage_time_delay']})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'ignition_off_time_delay' : group['ignition_off_time_delay']})
                continue

        return result_dict
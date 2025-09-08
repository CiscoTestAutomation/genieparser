"""
show_alarm.py
IOSXE parser for the following show command:
    * show facility-alarm relay major
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowFacilityAlarmRelayMajorSchema(MetaParser):
    # =============================================
    # Schema for 'show facility-alarm relay major'
    # =============================================
    schema = {
        'hardware_locations': {
            Any(): {
                Optional('source'): str,
                Optional('description'): str,
                Optional('relay'): int,
                Optional('time'): str,
            }
        }
    }
class ShowFacilityAlarmRelayMajor(ShowFacilityAlarmRelayMajorSchema):
    """
    Parser for:
        * show facility - alarm relay major 
    """
    cli_command = 'show facility-alarm relay major'

    def cli(self, output=None):
        """
        Method to parse the output of 'show facility-alarm relay major'.

        Args:
            output (str): CLI output to parse, if provided. If None, the command
                          will be executed on the device.

        Returns:
            dict: Parsed output in the form of a dictionary.
        """
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize result dictionary
        ret_dict = {} 

    
        # Power Supply 1 Description 1 2025-06-26 12:45
        p1 = re.compile(r"(?P<source>Power Supply\s+\d+)\s+(?P<description>.+?)\s+(?P<relay>\d+)\s+(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2})")

        
        # Temperature Sensor Description 2 2025-06-26 12:50
        p2 = re.compile(r"(?P<source>Temperature Sensor)\s+(?P<description>.+?)\s+(?P<relay>\d+)\s+(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2})")

    
        #Fan Tray 3 Description 3 2025-06-26 13:00
        p3 = re.compile(r"(?P<source>Fan Tray\s+\d+)\s+(?P<description>.+?)\s+(?P<relay>\d+)\s+(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2})")
        
        # Iterate through each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Match Power Supply
            #Power Supply 1     Power supply failure                1        2023-10-01 12:34
            matched_line = p1.match(line) 
            
            if matched_line:
                source = str(matched_line.group('source')).strip()
                inner_dict = ret_dict.setdefault('hardware_locations', {}).setdefault(source.lower().replace(" ", "_"), {})
                inner_dict['description'] = str(matched_line.group('description')).strip()
                inner_dict['relay'] = int(matched_line.group('relay'))
                inner_dict['time'] = str(matched_line.group('time')).strip()
                continue

            # Match Temperature Sensor
            # Temperature Sensor High temperature detected           2        2023-10-01 12:40
            matched_line = p2.match(line)
            
            if matched_line:
                source = str(matched_line.group('source')).strip()
                inner_dict = ret_dict.setdefault('hardware_locations', {}).setdefault(source.lower().replace(" ", "_"), {})
                inner_dict['description'] = str(matched_line.group('description')).strip()
                inner_dict['relay'] = int(matched_line.group('relay'))
                inner_dict['time'] = str(matched_line.group('time')).strip()
                continue

            # Match Fan Tray 
            # Fan Tray 2         Fan speed below threshold           3        2023-10-01 12:45
            matched_line = p3.match(line)
            
            if matched_line:
                source = str(matched_line.group('source')).strip()
                inner_dict = ret_dict.setdefault('hardware_locations', {}).setdefault(source.lower().replace(" ", "_"), {})
                inner_dict['description'] = str(matched_line.group('description')).strip()
                inner_dict['relay'] = int(matched_line.group('relay'))
                inner_dict['time'] = str(matched_line.group('time')).strip()
                continue

        return ret_dict

    
    
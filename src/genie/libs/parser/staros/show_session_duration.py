"""starOS implementation of show_session_duration.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
#from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSessionDurationSchema(MetaParser):
    """Schema for show session duration"""
    schema = {
        'duration' :{
            Any(): str
        }
    }

class ShowSessDur(ShowSessionDurationSchema):
    """Parser for show session duration"""
    cli_command = 'show session duration'

    """
    In-Progress Call Duration Statistics
         <1min          39644
         <2min          29938
         <5min          70274
         <15min        161509
         <1hr          416526
         <4hr          739682
         <12hr         607613
         <24hr         226358
         >24hr         129947
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial return dictionary
        duration_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        pattern = re.compile(r'^\s+(?P<duration>[<>]\d\w+)\s+(?P<calls>\d+)', re.MULTILINE)

        #For Loop to get all the values from output
        for match in out.splitlines(): #Split a string into a list where each line is a list item
            m= pattern.match(match)
            if m:
                if 'duration' not in duration_dict:
                    result_dict = duration_dict.setdefault('duration', {})
                
                #Defining a variable that contains the value of the regex
                call = m.groupdict()['calls'].strip()
                tiempo = m.groupdict()['duration'].strip()

                result_dict[tiempo] = call
        return duration_dict

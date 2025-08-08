''' show_loopdetect.py
IOSXE parsers for the following show commands:
    * show loopdetect
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# Genie testbed
from genie.testbed import load

class ShowLoopdetectSchema(MetaParser):
    """
    Schema for show loopdetect
    """
    # Define the schema structure for the command output
    schema = {
        'status': str,  # Status of Loopdetect (e.g., enabled/disabled)
        Optional('interfaces'): {  # Optional interfaces information
            Any(): {  # Interface name as a key
                'interval': int,  # Loopdetect interval in seconds
                'elapsed_time': int,  # Elapsed time since last detection
                'port_to_errdisable': str,  # Port error-disable mode (e.g., Yes/No)
                'action': str  # Action taken (e.g., Shutdown, None)
            }
        }
    }

class ShowLoopdetect(ShowLoopdetectSchema):
    """
    Parser for show loopdetect
    """

    # CLI command executed to retrieve the output
    cli_command = 'show loopdetect'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}        
        # Loopdetect is enabled         
        p1 = re.compile(r'^Loopdetect\s+is\s+enabled$')       
        # Gi1/0/1   10   180   Enabled   Shut
        p2 = re.compile(r'^(?P<interface>\S+)\s+(?P<interval>\d+)\s+(?P<elapsed_time>\d+)\s+(?P<port_to_errdisable>.*?)\s{2,}(?P<action>\S+)$')
        # Compile the interface line pattern for faster matching
        for line in output.splitlines():
            line = line.strip()
            # Check if the line indicates loop detection is enabled
            if p1.match(line):
                ret_dict['status'] = 'enabled'
                continue
            # Match the interface status line
            m = p2.match(line)
            if m:
                interface = m.group('interface')
                # Create or get the dictionary for this interface
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                # Update interface details in the dictionary
                intf_dict.update({
                    'interval': int(m.group('interval')),
                    'elapsed_time': int(m.group('elapsed_time')),
                    'port_to_errdisable': m.group('port_to_errdisable').strip(),
                    'action': m.group('action')
            })
        # Return the parsed dictionary
        return ret_dict
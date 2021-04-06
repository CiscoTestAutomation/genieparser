""" show_arm.py

IOSXR parsers for the following commands:

    * 'show arm ipv4 conflicts'

"""

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowArmIpv4ConflictsSchema(MetaParser):
    """ Schema for 'show arm ipv4 conflicts' """
    
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'forced_down': {
                            'F': {
                                Optional('down_interface'): {
                                    Any(): {
                                        'address': str,
                                        Optional('up_interface'): {
                                            Any():
                                                'address': str
                                        }
                                    }
                                }
                            }
                        },
                        Optional('unnumbered_down_interface'): {
                            Any(): {
                                'due_to': str,
                                Optional('up_interface'): {
                                    Any(): {
                                        'due_to': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
class ShowArmIpv4Conflicts(ShowArmIpv4ConflictsSchema):
    """ Parser class for 'show arm ipv4 conflicts' """
    
    cli_command = ['show arm ipv4 conflicts']
    
    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command[0])
            
        # cli 
        p0 = 'cli stuff'
        
        # F Forced down
        p1 = re.compile(r'^(?P<forced_down>\D) +Forced down')
           
        # F Lo2 10.1.1.2/24                          Lo1 10.1.1.1/24
        p2 = re.compile(r'^(?:F +(?P<down_interface>\S+) +(?P<down_address>\S+))? +(?:(?P<up_interface>\S+) +(?P<up_address>\S+))?')
        
        # tu2->tu1                       tu1->Lo1
        p3 = re.compile(r'^(?:(?P<forced_down>F) +(?P<interface>\S+) +(?P<address>\S+))?(?: +(?P<interface2>\S+) +(?P<address2>\S+)(?: +(?P<vrf>\w+))?)?$')
        
        for line in output.splitlines():
            line = line.strip()

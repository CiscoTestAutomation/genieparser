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
                            Any(): {
                                Optional('down_interface'): {
                                    Any(): {
                                        'address': str,
                                        'up_interface': {
                                            Any(): {
                                                'address': str
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        Optional('unnumbered_down_interface'): {
                            Any(): {
                                'due_to': str,
                                'up_interface': {
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
            
        # intialize vrf dictionary for parsed results
        result_dict = {}    
        
        # F Forced down
        p1 = re.compile(r'^(?P<forced_down>\D) +Forced down')
           
        # F Lo2 10.1.1.2/24                          Lo1 10.1.1.1/24
        p2 = re.compile(r'^(?:F +(?P<down_interface>\S+) +(?P<down_address>\S+))? +(?:(?P<up_interface>\S+) +(?P<up_address>\S+))?')
        
        # tu2->tu1                       tu1->Lo1
        p3 = re.compile(r'^(?:(?P<unnumbered_down_interface>\w+)->(?P<unnum_down_due>\w+))? +(?:(?P<unnumbered_up_interface>\w+)->(?P<unnum_up_due>\w+))?')
        
        for line in output.splitlines():
            line = line.strip()

            # F Forced down
            m=p1.match(line)
            if m:
                group = m.groupdict()
                                            
                forced_down_dict = result_dict.setdefault('vrf', {}). \
                                               setdefault('default', {}). \
                                               setdefault('address_family', {}). \
                                               setdefault('ipv4', {}). \
                                               setdefault('forced_down', {}). \
                                               setdefault(group['forced_down'], {})
                continue

            # F Lo2 10.1.1.2/24                          Lo1 10.1.1.1/24
            m=p2.match(line)
            if m:
                group = m.groupdict()
                
                # convert Lo2 to loopback2
                down_interface = Common.convert_intf_name(group['down_interface'])
                
                down_interface_dict = forced_down_dict.setdefault('down_interface', {}). \
                                                       setdefault(down_interface, {})
                
                down_interface_dict.update({'address': group['down_address']})
                
                # convert Lo1 to loopback1
                up_interface = Common.convert_intf_name(group['up_interface'])
                
                up_interface_dict = down_interface_dict.setdefault('up_interface', {}). \
                                                        setdefault(up_interface, {})
                up_interface_dict.update({'address': group['up_address']})
                continue


            # tu2->tu1                       tu1->Lo1
            m=p3.match(line)
            if m:
                group = m.groupdict()
                address_family_dict = result_dict.setdefault('vrf', {}). \
                                                  setdefault('default', {}). \
                                                  setdefault('address_family', {}). \
                                                  setdefault('ipv4', {})
                
                # convert tu2 to Tunnel2
                unnumbered_down_interface = Common.convert_intf_name(group['unnumbered_down_interface'])
                unnumbered_down_dict = address_family_dict.setdefault('unnumbered_down_interface', {}). \
                                                           setdefault(unnumbered_down_interface, {})
                
                # convert tu1 to Tunnel1
                unnumbered_down_due = Common.convert_intf_name(group['unnum_down_due'])
                unnumbered_down_dict.update({'due_to': unnumbered_down_due})
                
                # convert tu1 to Tunnel1
                unnumbered_up_interface = Common.convert_intf_name(group['unnumbered_up_interface'])
                unnumbered_up_dict = unnumbered_down_dict.setdefault('up_interface', {}). \
                                                          setdefault(unnumbered_up_interface, {})
                
                # convert Lo1 to Loopback1
                unnumbered_up_due = Common.convert_intf_name(group['unnum_up_due'])
                unnumbered_up_dict.update({'due_to': unnumbered_up_due})
                continue
            
        return result_dict
            
                                                    
                                                    
            

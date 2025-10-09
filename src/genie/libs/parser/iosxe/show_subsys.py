"""show_subsys.py

IOSXE parsers for the following show commands:
    * show subsys name {name}
    * show subsys name pgen
    * show subsys name ipfib
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================================
# Schema for 'show subsys name {name}'
# ======================================================
class ShowSubsysNameSchema(MetaParser):
    """Schema for show subsys name {name}"""
    
    schema = {
        'subsys': {
            Any(): {  # subsys name (e.g., ipv6fib)
                'class': str,
                'version': str
            }
        }
    }


# ======================================================
# Parser for 'show subsys name {name}'
# ======================================================
class ShowSubsysName(ShowSubsysNameSchema):
    """Parser for show subsys name {name}"""

    cli_command = 'show subsys name {name}'

    def cli(self, name="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(name=name))

        ret_dict = {}

        # Name                               Class       Version
        # ipv6fib                            Protocol    1.000.001
        p1 = re.compile(r'^(?P<subsys_name>\S+)\s+(?P<class>\S+)\s+(?P<version>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Skip header line
            if 'Name' in line and 'Class' in line and 'Version' in line:
                continue
                
            # Parse subsys entry
            m = p1.match(line)
            if m:
                subsys_name = m.group('subsys_name')
                class_name = m.group('class')
                version = m.group('version')
                
                subsys_dict = ret_dict.setdefault('subsys', {})
                subsys_entry = subsys_dict.setdefault(subsys_name, {})
                subsys_entry['class'] = class_name
                subsys_entry['version'] = version
                continue

        return ret_dict


# ======================================================
# Schema for 'show subsys name pgen'
# ======================================================
class ShowSubsysNamePgenSchema(MetaParser):
    """Schema for show subsys name pgen"""
    
    schema = {
        'subsys': {
            Any(): {  # subsys name (e.g., pgen)
                'class': str,
                'version': str
            }
        }
    }


# ======================================================
# Parser for 'show subsys name pgen'
# ======================================================
class ShowSubsysNamePgen(ShowSubsysNamePgenSchema):
    """Parser for show subsys name pgen"""

    cli_command = 'show subsys name pgen'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Name                               Class       Version
        # pgen                               Protocol    1.000.001
        p1 = re.compile(r'^(?P<subsys_name>\S+)\s+(?P<class>\S+)\s+(?P<version>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Skip header line
            if 'Name' in line and 'Class' in line and 'Version' in line:
                continue
                
            # Parse subsys entry
            m = p1.match(line)
            if m:
                subsys_name = m.group('subsys_name')
                class_name = m.group('class')
                version = m.group('version')
                
                subsys_dict = ret_dict.setdefault('subsys', {})
                subsys_entry = subsys_dict.setdefault(subsys_name, {})
                subsys_entry['class'] = class_name
                subsys_entry['version'] = version
                continue

        return ret_dict

class ShowSubsysNameIpfibSchema(MetaParser):
    """Schema for show subsys name ipfib"""
    schema = {
        'subsystems': {
            str: {  # The name of the subsystem, e.g., 'ipfib'
                'class': str,
                'version': str,
            }
        }
    }

class ShowSubsysNameIpfib(ShowSubsysNameIpfibSchema):
    """Parser for show subsys name ipfib"""

    cli_command = 'show subsys name ipfib'

    def cli(self, output=None):
        if output is None:
            # Execute the command on the device
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # ipfib                              Protocol    2.000.001
        p1 = re.compile(r'^(?P<name>\S+)\s+(?P<class>\S+)\s+(?P<version>\S+)$')

        # Process each line of the output
        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('Name'):
                # Skip empty lines and the header line
                continue

            # ipfib Protocol 2.000.001
            match = p1.match(line)
            if match:
                # Extract the matched groups
                name = match.group('name')
                class_ = match.group('class')
                version = match.group('version')

                # Use setdefault to avoid KeyError
                subsystems = parsed_dict.setdefault('subsystems', {})
                subsystems[name] = {
                    'class': class_,
                    'version': version,
                }

        return parsed_dict


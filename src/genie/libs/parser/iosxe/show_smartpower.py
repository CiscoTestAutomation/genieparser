''' show_smartpower.py

IOSXE parsers for the following show commands:
    * show smartpower version
'''

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowSmartPowerVersionSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        Optional("smartpower_mode"): str,
        Optional("ios_version"): str,
        Optional("smartpower_specification"): str,
        Optional("smartpower_version"): str,
        Optional("sdk_version"): str
    }

class ShowSmartPowerVersion(ShowSmartPowerVersionSchema):
    """Parser for show smartpower version"""

    cli_command = 'show smartpower version'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
        
        # SmartPower is Enabled
        p1 = re.compile(r'^SmartPower is (?P<smartpower_mode>\S+)$')

        # IOS Version:  17.15.20240121:114115101
        p2 = re.compile(r'^IOS Version:\s+(?P<ios_version>\S+)$')

        # SmartPower Specification:  3.5.1
        p3 = re.compile(r'^SmartPower Specification:\s+(?P<smartpower_specification>\S+)$')

        # SmartPower Version:  1.0
        p4 = re.compile(r'^SmartPower Version:  (?P<smartpower_version>\S+)$')

        # Powernet SDK Version:  4.0.1
        p5 = re.compile(r'^Powernet SDK Version:  (?P<sdk_version>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # SmartPower is Enabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'smartpower_mode': group['smartpower_mode']})
                continue 

            # IOS Version:  17.15.20240121:114115101
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'ios_version': group['ios_version']})
                continue 

            # SmartPower Specification:  3.5.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'smartpower_specification': group['smartpower_specification']})
                continue 

            # SmartPower Version:  1.0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'smartpower_version': group['smartpower_version']})
                continue 

            # Powernet SDK Version:  4.0.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'sdk_version': group['sdk_version']})
                continue

        return ret_dict


class ShowSmartPowerDomainSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        Optional("switch_name"): str,
        Optional("domain"): str,
        Optional("protocol"): str,
        Optional("ip"): str,
        Optional("port"): str
    }

class ShowSmartPowerDomain(ShowSmartPowerDomainSchema):
    """Parser for show smartpower domain"""

    cli_command = 'show smartpower domain'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
                                                      
        # Name      : switch-2  
        p1 = re.compile(r'^Name\s+:\s+(?P<switch_name>\S+)$')

        # Domain    : cisco  
        p2 = re.compile(r'^Domain\s+:\s+(?P<domain>\S+)$')

        # Protocol  : udp
        p3 = re.compile(r'^Protocol\s+:\s+(?P<protocol>\S+)$')

        # IP        : 10.10.10.1
        p4 = re.compile(r'^IP\s+:\s+(?P<ip>\S+)$')

        # Port      : 43440
        p5 = re.compile(r'^Port\s+:\s+(?P<port>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Name      : switch-2  
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'switch_name': group['switch_name']})
                continue 

            # Domain    : cisco  
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'domain': group['domain']})
                continue 

            # Protocol  : udp
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'protocol': group['protocol']})
                continue 

            # IP        : 10.10.10.1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'ip': group['ip']})
                continue 

            # Port      : 43440
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'port': group['port']})
                continue

        return ret_dict


class ShowSmartpowerCategoriesSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        "levels": {
            Any(): {
                Optional("label"): str,
                Optional("color"): str,
                Optional("feature_mapping"): str,
            },
        } 
    }

class ShowSmartpowerCategories(ShowSmartpowerCategoriesSchema):
    """Parser for show smartpower categories"""

    cli_command = 'show smartpower categories'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        # Level   Label       Color       Feature Mapping
        # -----   -----       -----       ---------------
        # 10      Full        Red         FullPwr
        # 9       High        Red         SmartLED
        # 8       Reduced     Yellow      NA
        # 7       Medium      Yellow      NA
        # 6       Frugal      Green       NA
        # 5       Low         Green       NA
        # 4       Ready       Blue        NA
        # 3       Standby     Blue        NA
        # 2       Sleep       Brown       NA
        # 1       Hibernate   Brown       NA
        # 0       Shut        Black       PwrDown

        p1 = re.compile(r'^(?P<level>\d+)+\s+(?P<label>\w+)+\s+(?P<color>\w+)\s+(?P<feature_mapping>\w+)$')
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                level = group['level']
                result_dict = ret_dict.setdefault('levels', {}).setdefault(level, {})
                result_dict['label'] = group['label']
                result_dict['color'] = group['color']
                result_dict['feature_mapping'] = group['feature_mapping']
                continue  

        return ret_dict     
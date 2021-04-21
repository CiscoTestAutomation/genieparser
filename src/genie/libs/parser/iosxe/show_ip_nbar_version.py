"""show_ip_nbar_version.py

    IOSXE parsers for the following show commands:
        * 'show ip nbar version'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================
# Schema for:
#    * 'show ip nbar version'
# ==============================

class ShowIpNbarVersionSchema(MetaParser):
    """Schema for show ip nbar version"""
    
    schema = {
        'file': str,
        'name': str,
        'publisher': str,
        'nbar_minimum_backward_compatible_version': str,
        'creation_time': str,
        'nbar_engine_version': str,
        'nbar_software_version': str,
        'state': str,
        'version': str
    }

class ShowIpNbarVersion(ShowIpNbarVersionSchema):
    """Parser for show ip nbar version"""

    cli_command = ['show ip nbar version']

    #* could add extra parameters if needed
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        # initial variables
        parsed_dict = {}
        
        # NBAR software version:    34
        p1 = re.compile('^NBAR software version:\s+(?P<nbar_software_version>.+)')
        
        # NBAR minimum backward compatible version: 41
        p2 = re.compile('^NBAR minimum backward compatible version:\s+(?P<nbar_minimum_backward_compatible_version>.+)')
        
        # Name: Advanced Protocol Pack
        p3 = re.compile('^Name:\s+(?P<name>.+)')
        
        # Version:  41.0
        p4 = re.compile('^Version:\s+(?P<version>.+)')

        # Publisher:    Cisco Systems Inc.
        p5 = re.compile('^Publisher:\s+(?P<publisher>.+)')

        # NBAR Engine Version:  31
        p6 = re.compile('^NBAR Engine Version:\s+(?P<nbar_engine_version>.+)')
        
        # Creation time:    Mon Feb 11 09:42:11 UTC 2019
        p7 = re.compile('^Creation time:\s+(?P<creation_time>.+)')
        
        # File: bootflash:sdavc/pp-adv-all-166.2-31-41.0.0.pack
        p8 = re.compile('^File:\s+(?P<file>.+)')
        
        # State:    Active
        p9 = re.compile('^State:\s+(?P<state>.+)')


        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p2.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p3.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p4.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p5.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p6.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p7.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p8.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue
            m = p9.match(line)
            if m:
                parsed_dict.update(m.groupdict())
                continue


        return parsed_dict

    
"""show_version.py

IOSXE parsers for show commands:
    * 'show version {switch} {sw_number} {route_processor} {mode}'
    * 'show version {mode}'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowVersionModeSchema(MetaParser):
    """
        Schema for * show version {switch} {sw_number} {route_processor} {mode}
                   * show version {mode}
    """
    
    schema = {
        'role':{
            Any(): {
                'package': str,
                'version': str,
                'status': str,
                Optional('file_type'): str,
                'file': str,
                'location': str,
                'built_date': str,
                'owner': str,
                'checksum': str
            }
        }
    }


class ShowVersionMode(ShowVersionModeSchema):
    """ 
        Parser for * show version {switch} {sw_number} {route_processor} {mode}
                   * show version {mode}
    """

    cli_command = ['show version {mode}',
            'show version {switch} {sw_number} {route_processor} {mode}']

    def cli(self, mode, switch=None, sw_number=None, route_processor=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, sw_number=sw_number,\
                    route_processor=route_processor, mode=mode)
            else:
                cmd = self.cli_command[0].format(mode=mode)
            
            output = self.device.execute(cmd)
        
        # Package: rpbase, version: BLD_POLARIS_DEV_LATEST_20230413_214611_V17_12_0_10, status: active
        p1 = re.compile(r'^Package: (?P<package>.+), version: (?P<version>\S+), status: (?P<status>.+)$')
        
        # Role: rp_iosd
        p2 = re.compile(r'^Role: (?P<role>.+)$')
        
        # File: consolidated:cat9k-rpbase.BLD_POLARIS_DEV_LATEST_20230413_214611_V17_12_0_10.SSA.pkg, on: RP0/0
        # File: /flash/packages.conf, on: RP0
        p3 = re.compile(r'^File: ((?P<file_type>.+):)?(?P<file>\S+), on: (?P<location>\S+)$')
        
        # Built: 2023-04-13_15.18, by: mcpre
        p4 = re.compile(r'^Built: (?P<built_date>\S+), by: (?P<owner>\S+)$')
        
        # File SHA1 checksum: 7cc7035fc0c6b8eb57b5088b86d9ae9e67e67b8b
        p5 = re.compile(r'^File SHA1 checksum: (?P<checksum>\S+)$')

        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            # Package: rpbase, version: BLD_POLARIS_DEV_LATEST_20230413_214611_V17_12_0_10, status: active
            m = p1.match(line)
            if m:
                pack_dict = m.groupdict()
                continue

            # Role: rp_iosd
            m = p2.match(line)
            if m:
                role_dict = ret_dict.setdefault('role', {}).setdefault(m.groupdict()['role'], {})
                role_dict.update(pack_dict)
                continue
            
            # File: consolidated:cat9k-rpbase.BLD_POLARIS_DEV_LATEST_20230413_214611_V17_12_0_10.SSA.pkg, on: RP0/0
            # File: /flash/packages.conf, on: RP0
            m = p3.match(line)
            if m:
                role_dict['file'] = m.groupdict()['file']
                role_dict['location'] = m.groupdict()['location']
                if m.groupdict()['file_type']:
                    role_dict['file_type'] = m.groupdict()['file_type']
                continue
            
            # Built: 2023-04-13_15.18, by: mcpre
            m = p4.match(line)
            if m:
                role_dict.update(m.groupdict())
                continue

            # File SHA1 checksum: 7cc7035fc0c6b8eb57b5088b86d9ae9e67e67b8b
            m = p5.match(line)
            if m:
                role_dict.update(m.groupdict())
                continue

        return ret_dict

''' show_bootflash.py

IOSXE parsers for the following show commands:
    * show bootflash:
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show bootflash:'
# =================

class ShowBootflashSchema(MetaParser):
    """Schema for show bootflash:."""
    schema = {
        'bytes_available': int,
        'bytes_used': int,
        'files': {
            Any(): {
                'file_length': int,
                'file_date': str,
                'file_name': str
                }
            }
    }

# =================
# Parser for:
#  * 'show bootflash:'
# =================
class ShowBootflash(ShowBootflashSchema):
    """Parser for show bootflash:"""

    cli_command = 'show bootflash:'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 13755338752 bytes available (489017344 bytes used)
        p1 = re.compile(r"(?P<bytes_available>\d+)\s+bytes available\s+\((?P<bytes_used>\d+)\s+bytes used\)")
        #12         11 Oct 12 2020 07:27:04 +00:00 /bootflash/tracelogs/timestamp
        p2 = re.compile(r"(?P<file_index>\d+)\s+(?P<file_length>\d+)\s+(?P<file_date>[a-zA-Z]+\s+\d+\s+\d+\s+[0-9:.]+\s+[0-9+:]+)\s+(?P<file_name>\S+)")

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line_strip = line.strip()
            # 13755338752 bytes available (489017344 bytes used)
            m = p1.match(line_strip)
            if m:
                group = m.groupdict()
                ret_dict.update({k:int(v) for k, v in group.items()})
                continue
            #12         11 Oct 12 2020 07:27:04 +00:00 /bootflash/tracelogs/timestamp
            m = p2.match(line_strip)
            if m:
                group=m.groupdict()
                index=int(group['file_index'])
                if 'files' not in ret_dict:
                    ret_dict['files']={}
                if index not in ret_dict['files']:
                    ret_dict['files'][index]={}
                ret_dict['files'][index]['file_length']=int(group['file_length'])
                ret_dict['files'][index]['file_date']=group['file_date']
                ret_dict['files'][index]['file_name']=group['file_name']

        return ret_dict


class ShowBootSystemSchema(MetaParser):
    """Schema for show boot system"""
    schema = {
        'boot_variable': str,
        Optional('manual_boot_variable'): str,
        Optional('is_manual_boot'): bool,
        Optional('baud'): int,
        Optional('ipxe_timeout'): Or(int, str),
        Optional('bootmode'): str,
        Optional('is_boot_mode'): bool,
        Optional('enable_break'): bool,
        Optional('config_file'): str,
    }

# ================= 
# Parser for:
#  * 'show boot system'
# =================

class ShowBootSystem(ShowBootSystemSchema):
    """Parser for show boot system"""

    cli_command = 'show boot system'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict={}

        # BOOT variable = flash:packages.conf;
        p1 = re.compile('^BOOT variable \=\s+(?P<boot>\S+)$')
        
        # MANUAL_BOOT variable = no
        p2 = re.compile('^MANUAL_BOOT variable\s+\=\s+(?P<manual>yes|no)$')

        # Manual Boot = no
        p2_1 = re.compile('^Manual\sBoot\s+\=\s+(?P<manual>yes|no)$')

        # BAUD variable = 9600
        p3 = re.compile('^BAUD variable\s+\=\s+(?P<baud>\d+)$')

        # IPXE_TIMEOUT variable = 0
        p4 = re.compile('^IPXE_TIMEOUT variable\s+\=\s+(?P<ipxe>\d+)$')

        # iPXE Timeout = 0
        p4_1 = re.compile('^iPXE\sTimeout\s+\=\s+(?P<ipxe>\d+)$')

        # BOOTMODE variable = yes
        p5 = re.compile('^BOOTMODE variable\s+\=\s+(?P<boot_mode>yes|no)$')

        # Boot Mode = DEVICE
        p5_1 = re.compile('^Boot\sMode\s+\=\s+(?P<boot_mode>\w+)$')

        # Enable Break = yes
        p6 = re.compile('^Enable Break\s+\=\s+(?P<enable>yes|no)$')

        # Config file         = flash:/config.text
        p7 = re.compile('^Config file\s+\=\s+(?P<config>\S+)$')
        
        for line in output.splitlines():
            line=line.strip()
            
            # BOOT variable = flash:packages.conf;
            m = p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('boot_variable', group['boot'])
                continue
                
            # MANUAL_BOOT variable = no
            m = p2.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('manual_boot_variable', group['manual'])
                continue

            # Manual Boot = no
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                manual = group['manual'] == 'yes'
                ret_dict.setdefault('is_manual_boot', manual)
                continue
                
            # BAUD variable = 9600
            m = p3.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('baud', int(group['baud']))
                continue
                
            # IPXE_TIMEOUT variable = 0
            m = p4.match(line) 
            if m:
                group=m.groupdict()
                ret_dict.setdefault('ipxe_timeout', int(group['ipxe']))
                continue

            # iPXE Timeout = 0
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('ipxe_timeout', int(group['ipxe']))
                continue
                
            # BOOTMODE variable = yes
            m = p5.match(line)
            if m:
                group=m.groupdict()
                is_boot_mode = group['boot_mode'] == 'yes'
                ret_dict.setdefault('is_boot_mode', is_boot_mode)
                continue

            # Boot Mode = DEVICE
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('bootmode', group['boot_mode'])
                continue
            
            # Enable Break = yes
            m = p6.match(line)
            if m:
                group=m.groupdict()
                enable = group['enable'] == 'yes'
                ret_dict.setdefault('enable_break', enable)
                continue
            
            # Config file         = flash:/config.text
            m = p7.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('config_file', group['config'])
                continue
                
        return ret_dict     
 

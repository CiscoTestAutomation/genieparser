''' show_iox.py

IOSXE parsers for the following show commands:
    * show iox:
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show iox:'
# =================

class ShowIoxSchema(MetaParser):
    """Schema for show iox:."""
    schema = {
        'caf_service': str,
        'ha_service': str,
        'ioxman_service': str,
        'sec_storage_service': str,
        'libvirtd': str,
        'dockerd': str,
        Optional('sync_status'): str,
        Optional('redundancy_status'): str,
        Optional('last_application_sync_time'): str
    }

# =================
# Parser for:
#  * 'show iox:'
# =================
class ShowIox(ShowIoxSchema):
    '''Parser for show iox    
    
    IOx Infrastructure Summary:
    ---------------------------
    IOx service (CAF)              : Running
    IOx service (HA)               : Running 
    IOx service (IOxman)           : Running 
    IOx service (Sec storage)      : Not Running 
    Libvirtd 5.5.0                 : Running
    Dockerd 18.03.0                : Running
    Redundancy Status              : Ready 
    Sync status                    : Successful
    Last application sync time     : 2021-03-23 12:21:07.529935
    '''

    cli_command = 'show iox-service'    

    def cli(self, output=None):
        #print("DEBUG: cli")
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # IOx service (CAF)              : Running
        p1 = re.compile(r"IOx service \(CAF\) +: (?P<caf_service>[\w\s]+)$")
        # IOx service (HA)              : Running
        p2 = re.compile(r"IOx service \(HA\) +: (?P<ha_service>[\w\s]+)$")
        # IOx service (IOxman)              : Running
        p3 = re.compile(r"IOx service \(IOxman\) +: (?P<ioxman_service>[\w\s]+)$")
        # IOx service (Sec storage)              : Running
        p4 = re.compile(r"IOx service \(Sec storage\) +: (?P<sec_storage_service>[\w\s]+)$")
        # Libvirtd 5.5.0                 : Running
        p5 = re.compile(r"Libvirtd.*: (?P<libvirtd>[\w\s]+)$")
        # Dockerd 18.03.0                : Running
        p6 = re.compile(r"Dockerd.*: (?P<dockerd>[\w\s]+)$")
        # Redundancy Status              : Ready
        p7 = re.compile(r"Redundancy Status +: (?P<redundancy_status>.*)$")
        # Sync status                    : Successful
        # Sync Status                    : Disabled
        p8 = re.compile(r"Sync.*: (?P<sync_status>[\w\s]+)$")
        # Last application sync time     : 2021-03-23 12:21:07.529935
        p9 = re.compile(r"Last application sync time +: (?P<last_application_sync_time>.*)$")
            
        for line in out.splitlines():
            line_strip = line.strip()
            
            # IOx service (CAF)              : Running
            m = p1.match(line)

            if m:
                ret_dict['caf_service'] = m.groupdict()['caf_service'].strip()
                
            m = p2.match(line)
            if m:
                ret_dict['ha_service'] = m.groupdict()['ha_service'].strip()
                
            m = p3.match(line)
            if m:
                ret_dict['ioxman_service'] = m.groupdict()['ioxman_service'].strip()
                
            m = p4.match(line)
            if m:
                ret_dict['sec_storage_service'] = m.groupdict()['sec_storage_service'].strip()                

            m = p5.match(line)
            if m:
                ret_dict['libvirtd'] = m.groupdict()['libvirtd'].strip()

            m = p6.match(line)
            if m:
                ret_dict['dockerd'] = m.groupdict()['dockerd'].strip()

            m = p7.match(line)
            if m:
                ret_dict['redundancy_status'] = m.groupdict()['redundancy_status'].strip()

            m = p8.match(line)
            if m:
                ret_dict['sync_status'] = m.groupdict()['sync_status'].strip()

            m = p9.match(line)
            if m:
                ret_dict['last_application_sync_time'] = m.groupdict()['last_application_sync_time'].strip()
            
        return ret_dict
# ----------------------

""" show_vtp.py

IOSXE parsers for the following show commands:
    * show vtp status
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show vtp status'
# =============================================

class ShowVtpStatusSchema(MetaParser):
    """Schema for show vtp status"""

    schema = {'vtp': {
                Optional('version_capable'): list,
                'version': str,
                Optional('domain_name'): str,
                'pruning_mode': bool,
                'traps_generation': bool,
                Optional('device_id'): str,
                'conf_last_modified_by': str,
                'conf_last_modified_time': str,
                Optional('updater_id'): str,
                Optional('updater_interface'): str,
                Optional('updater_reason'): str,
                'operating_mode': str,
                'enabled': bool,
                'maximum_vlans': int,
                'existing_vlans': int,
                'configuration_revision': int,
                'md5_digest': str,

            }
        }

class ShowVtpStatus(ShowVtpStatusSchema):
    """Parser for show vtp status """

    cli_command = 'show vtp status'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial variables
        ret_dict = {}
        digest = []

        # VTP Version capable             : 1 to 3
        p1 = re.compile(r'^VTP +Version +capable +: +(?P<val>[\w\s]+)$')

        # VTP version running             : 1
        # VTP Version                     : 2
        p2 = re.compile(r'^VTP +[Vv]ersion( +running)? +: +(?P<val>\d+)$')

        # VTP Domain Name                 : 
        p3 = re.compile(r'^VTP +Domain +Name +: +(?P<val>\S+)$')

        # VTP Pruning Mode                : Disabled
        p4 = re.compile(r'^VTP +Pruning +Mode +: +(?P<val>\w+)$')

        # VTP Traps Generation            : Disabled
        p5 = re.compile(r'^VTP +Traps +Generation +: +(?P<val>\w+)$')

        # Device ID                       : 3820.5622.a580
        p6 = re.compile(r'^Device +ID +: +(?P<val>[\w\.\:]+)$')

        # Configuration last modified by 192.168.234.1 at 12-5-17 09:35:46
        p7 = re.compile(r'^Configuration +last +modified +by +'
                         '(?P<val>[\w\.\:]+) +at +(?P<val1>[\w\.\:\-\s]+)$')

        # Local updater ID is 192.168.234.1 on interface Vl100 (lowest numbered VLAN interface found)
        p8 = re.compile(r'^Local +updater +ID +is +(?P<id>[\w\.\:]+) +on +'
                         'interface +(?P<intf>[\w\.\/\-]+) *'
                         '(\((?P<reason>[\S\s]+)\))?$')

        # Feature VLAN:
        # --------------
        # VTP Operating Mode                : Server
        p9 = re.compile(r'^VTP +Operating +Mode +: (?P<val>\S+)$')

        # Maximum VLANs supported locally   : 1005
        p10 = re.compile(r'^Maximum +VLANs +supported +locally +: (?P<val>\d+)$')

        # Number of existing VLANs          : 53
        p11 = re.compile(r'^Number +of +existing +VLANs +: (?P<val>\d+)$')

        # Configuration Revision            : 55
        p12 = re.compile(r'^Configuration +Revision +: (?P<val>\d+)$')

        # MD5 digest                        : 0x9E 0x35 0x3C 0x74 0xDD 0xE9 0x3D 0x62 
        p13 = re.compile(r'^MD5 +digest +: (?P<val>[\w\s]+)$')

        #                                     0xDE 0x2D 0x66 0x67 0x70 0x72 0x55 0x38
        p13_1 = re.compile(r'^(?P<val>[\w\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # VTP Version capable             : 1 to 3
            m = p1.match(line)
            if m:
                if 'vtp' not in ret_dict:
                    ret_dict['vtp'] = {}

                try:
                    val = m.groupdict()['val'].split('to')
                    val = list( range( int(val[0]), int(val[1]) + 1 ))
                    ret_dict['vtp']['version_capable'] = val
                except Exception:
                    pass

                continue

            # VTP version running             : 1
            # VTP Version                     : 2
            m = p2.match(line)
            if m:
                if 'vtp' not in ret_dict:
                    ret_dict['vtp'] = {}
                ret_dict['vtp']['version'] = m.groupdict()['val']
                continue

            # VTP Domain Name                 : 
            m = p3.match(line)
            if m:
                ret_dict['vtp']['domain_name'] = m.groupdict()['val']
                continue
        
            # VTP Pruning Mode                : Disabled
            m = p4.match(line)
            if m:
                ret_dict['vtp']['pruning_mode'] = False if 'disable' in \
                                                    m.groupdict()['val'].lower() else True
                continue

            # VTP Traps Generation            : Disabled
            m = p5.match(line)
            if m:
                ret_dict['vtp']['traps_generation'] = False if 'disable' in \
                                                    m.groupdict()['val'].lower() else True
                continue
            
            # Device ID                       : 3820.5622.a580
            m = p6.match(line)
            if m:
                ret_dict['vtp']['device_id'] = m.groupdict()['val']
                continue

            # Configuration last modified by 192.168.234.1 at 12-5-17 09:35:46
            m = p7.match(line)
            if m:
                ret_dict['vtp']['conf_last_modified_by'] = m.groupdict()['val']
                ret_dict['vtp']['conf_last_modified_time'] = m.groupdict()['val1']
                continue

            # Local updater ID is 192.168.234.1 on interface Vl100 (lowest numbered VLAN interface found)
            m = p8.match(line)
            if m:
                ret_dict['vtp']['updater_id'] = m.groupdict()['id']
                ret_dict['vtp']['updater_interface'] = m.groupdict()['intf']
                ret_dict['vtp']['updater_reason'] = m.groupdict()['reason']
                continue

            # Feature VLAN:
            # --------------
            # VTP Operating Mode                : Server
            m = p9.match(line)
            if m:
                status = m.groupdict()['val'].lower()
                ret_dict['vtp']['operating_mode'] = status

                if status in ['server', 'client']:
                    ret_dict['vtp']['enabled'] = True
                else:
                    ret_dict['vtp']['enabled'] = False
                continue

            # Maximum VLANs supported locally   : 1005
            m = p10.match(line)
            if m:
                ret_dict['vtp']['maximum_vlans'] = int(m.groupdict()['val'])
                continue

            # Number of existing VLANs          : 53
            m = p11.match(line)
            if m:
                ret_dict['vtp']['existing_vlans'] = int(m.groupdict()['val'])
                continue

            # Configuration Revision            : 55
            m = p12.match(line)
            if m:
                ret_dict['vtp']['configuration_revision'] = int(m.groupdict()['val'])
                continue

            # MD5 digest                        : 0x9E 0x35 0x3C 0x74 0xDD 0xE9 0x3D 0x62 
            m = p13.match(line)
            if m:
                digest = m.groupdict()['val'].split()
                ret_dict['vtp']['md5_digest'] = ' '.join(sorted(digest))
                continue
            
            #                                     0xDE 0x2D 0x66 0x67 0x70 0x72 0x55 0x38
            m = p13_1.match(line)
            if m:
                if digest:
                    digest.extend(m.groupdict()['val'].split())
                    ret_dict['vtp']['md5_digest'] = ' '.join(sorted(digest))
                    continue

        return ret_dict

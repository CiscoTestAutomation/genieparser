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
# Parser for 'show vtp password'
# =============================================

class ShowVtpPasswordSchema(MetaParser):
    """Schema for show vtp password"""

    schema = {'vtp': {
                'configured': bool,
                Optional('password'): str,
        }
    }


class ShowVtpPassword(ShowVtpPasswordSchema):
    """Parser for show vtp password"""

    cli_command = 'show vtp password'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # The VTP password is not configured.
        p1 = re.compile(r'^The +VTP +password +is +not +configured.$')

        # VTP Password: password-string
        p2 = re.compile(r'^VTP +Password: +(?P<val>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # The VTP password is not configured.
            m = p1.match(line)
            if m:
                sub_dict = ret_dict.setdefault('vtp', {})
                sub_dict['configured'] = False
                continue

            # VTP Password: password-string
            m = p2.match(line)
            if m:
                sub_dict = ret_dict.setdefault('vtp', {})
                sub_dict['configured'] = True
                sub_dict['password'] = m.groupdict()['val']
                continue

        return ret_dict


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
                Optional('conf_last_modified_by'): str,
                Optional('conf_last_modified_time'): str,
                Optional('updater_id'): str,
                Optional('updater_interface'): str,
                Optional('updater_reason'): str,
                Optional('operating_mode'): str,
                Optional('enabled'): bool,
                Optional('maximum_vlans'): int,
                Optional('existing_vlans'): int,
                Optional('configuration_revision'): int,
                Optional('md5_digest'): str,

                Optional('feature'): {
                    'vlan': {
                        'enabled': bool,
                        'operating_mode': str,
                        Optional('maximum_vlans'): int,
                        'existing_vlans': int,
                        'existing_extended_vlans': int,
                        Optional('configuration_revision'): int,
                        Optional('primary_id'): str,
                        Optional('primary_description'): str,
                        Optional('md5_digest'): str,
                    },
                    'mst': {
                        'enabled': bool,
                        'operating_mode': str,
                        Optional('configuration_revision'): int,
                        Optional('primary_id'): str,
                        Optional('primary_description'): str,
                        Optional('md5_digest'): str,
                    },
                    Optional('unknown'): {
                        'enabled': bool,
                        'operating_mode': str,
                    }
                },
            }
        }

class ShowVtpStatus(ShowVtpStatusSchema):
    """Parser for show vtp status """

    cli_command = 'show vtp status'
    exclude = ['device_id']

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
        # VTP Version : running VTP1 (VTP2 capable)
        p2 = re.compile(r'^VTP +[Vv]ersion(?: +running)? *: '
                         '(running VTP)?(?P<version>\d+)'
                         '( +\(VTP+(?P<capable>\d+) capable\))?$')

        # VTP Domain Name                 : 
        p3 = re.compile(r'^VTP +Domain +Name +: +(?P<val>\S+)$')

        # VTP Pruning Mode                : Disabled
        p4 = re.compile(r'^VTP +Pruning +Mode +: +(?P<val>\w+)$')

        # VTP Traps Generation            : Disabled
        p5 = re.compile(r'^VTP +Traps +Generation +: +(?P<val>\w+)$')

        # Device ID                       : 3820.56ff.c7a2
        p6 = re.compile(r'^Device +ID +: +(?P<val>[\w\.\:]+)$')

        # Configuration last modified by 192.168.234.1 at 12-5-17 09:35:46
        p7 = re.compile(r'^Configuration +last +modified +by +'
                         '(?P<val>[\w\.\:]+) +at +(?P<val1>[\w\.\:\-\s]+)$')

        # Local updater ID is 192.168.234.1 on interface Vl100 (lowest numbered VLAN interface found)
        p8 = re.compile(r'^Local +updater +ID +is +(?P<id>[\w\.\:]+) +on +'
                         'interface +(?P<intf>[\w\.\/\-]+) *'
                         '(\((?P<reason>[\S\s]+)\))?$')

        # Feature VLAN:
        p17 = re.compile(r'^Feature +VLAN:$')
        # --------------
        # VTP Operating Mode                : Server
        p9 = re.compile(r'^VTP +Operating +Mode +: (?P<val>\S+\s?\S*)$')

        # Maximum VLANs supported locally   : 1005
        # Maximum VLANs supported locally   :  2048
        p10 = re.compile(r'^Maximum +VLANs +supported +locally +: +(?P<val>\d+)$')

        # Number of existing VLANs          : 53
        p11 = re.compile(r'^Number +of +existing +VLANs +: (?P<val>\d+)$')

        # Number of existing extended VLANs : 0
        p14 = re.compile(r'^Number +of +existing +extended +VLANs +: (?P<val>\d+)$')

        # Configuration Revision            : 55
        p12 = re.compile(r'^Configuration +Revision +: (?P<val>\d+)$')

        # Primary ID                        : 0000.0000.0000
        p15 = re.compile(r'^Primary +ID +: (?P<val>([0-9a-f]{4}.?){3})$')

        # Primary Description               : SW2
        p16 = re.compile(r'^Primary +Description +: (?P<val>\S*)$')

        # MD5 digest                        : 0x9E 0x35 0x3C 0x74 0xDD 0xE9 0x3D 0x62 
        p13 = re.compile(r'^MD5 +digest +: (?P<val>[\w\s]+)$')

        #                                     0xDE 0x2D 0x66 0x67 0x70 0x72 0x55 0x38
        p13_1 = re.compile(r'^(?P<val>[\w\s]+)$')

        # Feature MST:
        p18 = re.compile(r'^Feature +MST:.*$')

        # Feature UNKNOWN:
        p19 = re.compile(r'^Feature +UNKNOWN:.*$')

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
            # VTP Version : running VTP1 (VTP2 capable)
            m = p2.match(line)
            if m:
                if 'vtp' not in ret_dict:
                    ret_dict['vtp'] = {}
                version = m.groupdict()['version']
                capable = m.groupdict()['capable']
                if version:
                    ret_dict['vtp']['version'] = version
                if capable:
                    ret_dict['vtp']['version_capable'] = list(capable)

                if version == '3':
                    if 'feature' not in ret_dict['vtp']:
                        ret_dict['vtp']['feature'] = {'vlan': {}, 'mst': {}}

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
            
            # Device ID                       : 3820.56ff.c7a2
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
            m = p17.match(line)
            if m:
                if version == '3':
                    feature = 'vlan'

                continue

            # VTP Operating Mode                : Server
            m = p9.match(line)
            if m:
                status = m.groupdict()['val'].lower()

                if status in ['server', 'primary server', 'client']:
                    enabled = True
                else:
                    enabled = False

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['operating_mode'] = status
                    ret_dict['vtp']['feature'][feature]['enabled'] = enabled

                else:
                    ret_dict['vtp']['operating_mode'] = status
                    ret_dict['vtp']['enabled'] = enabled

                continue

            # Maximum VLANs supported locally   : 1005
            m = p10.match(line)
            if m:
                max = int(m.groupdict()['val'])

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['maximum_vlans'] = max
                else:
                    ret_dict['vtp']['maximum_vlans'] = max

                continue

            # Number of existing VLANs          : 53
            m = p11.match(line)
            if m:
                num = int(m.groupdict()['val'])

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['existing_vlans'] = num
                else:
                    ret_dict['vtp']['existing_vlans'] = num

                continue

            # Number of existing extended VLANs : 0
            m = p14.match(line)
            if m:
                num = int(m.groupdict()['val'])

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['existing_extended_vlans'] = num

                continue

            # Configuration Revision            : 55
            m = p12.match(line)
            if m:
                num = int(m.groupdict()['val'])

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['configuration_revision'] = num
                else:
                    ret_dict['vtp']['configuration_revision'] = num

                continue

            # Primary ID                        : 0000.0000.0000
            m = p15.match(line)
            if m:
                if version == '3':
                    ret_dict['vtp']['feature'][feature]['primary_id'] = m.groupdict()['val'].lower()

                continue

            # Primary Description               : SW2
            m = p16.match(line)
            if m:
                if version == '3':
                    ret_dict['vtp']['feature'][feature]['primary_description'] = m.groupdict()['val']

                continue

            # MD5 digest                        : 0x9E 0x35 0x3C 0x74 0xDD 0xE9 0x3D 0x62 
            m = p13.match(line)
            if m:
                digest = m.groupdict()['val'].split()

                if version == '3':
                    ret_dict['vtp']['feature'][feature]['md5_digest'] = ' '.join(sorted(digest))
                else:
                    ret_dict['vtp']['md5_digest'] = ' '.join(sorted(digest))

                continue
            
            #                                     0xDE 0x2D 0x66 0x67 0x70 0x72 0x55 0x38
            m = p13_1.match(line)
            if m:
                if digest:
                    digest.extend(m.groupdict()['val'].split())

                    if version == '3':
                        ret_dict['vtp']['feature'][feature]['md5_digest'] = ' '.join(sorted(digest))
                    else:
                        ret_dict['vtp']['md5_digest'] = ' '.join(sorted(digest))

                    continue

            # Feature MST:
            # --------------
            m = p18.match(line)
            if m:
                if version == '3':
                    feature = 'mst'

                continue

            # Feature UNKNOWN:
            # --------------
            m = p19.match(line)
            if m:
                unknown_dict = {'unknown': {}}
                ret_dict['vtp']['feature'].update(unknown_dict)
                if version == '3':
                    feature = 'unknown'

                continue

        return ret_dict

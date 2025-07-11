# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any



class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {
        'os': str,
        Optional('os_flavor'): str,
        'version': str,
        Optional('build'): str,
        Optional('platform'): str,
        Optional('pid'): str,
        Optional('operating_mode'): str,
        Optional('chassis_type'): str,
    }


class ShowVersion(ShowVersionSchema):
    """Parser for show version"""

    cli_command = [
        'show version',
    ]

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}


        # ********************************************
        # *                  SONIC                   *
        # ********************************************

        # Model Number: 8201-32FH-O
        sonic_pid_pattern = re.compile(r'^Model\sNumber:\s+(?P<pid>.+)$')


        # ********************************************
        # *                  ASA                     *
        # ********************************************

        # Cisco Adaptive Security Appliance Software Version 9.8(4)10
        asa_os_version_pattern = re.compile(r'^Cisco\s+Adaptive Security Appliance Software Version (?P<version>.+)$')

        # Hardware:   ASAv, 2048 MB RAM, CPU Xeon E5 series 3491 MHz,
        # Hardware:   ASA5520, 512 MB RAM, CPU Pentium 4 Celeron 2000 MHz
        asa_platform_pattern = re.compile(r'^Hardware:\s+(?P<platform>.*), .*, .*$')

        # Model Id:   ASAv10
        asa_pid_pattern = re.compile(r'Model\s+Id\:\s+(?P<pid>.+)')


        # ********************************************
        # *                  GAIA                    *
        # ********************************************

        # Product version Check Point Gaia R80.40
        gaia_os_version_pattern = re.compile(r'^Product version Check Point Gaia (?P<version>.*)$')


        # ********************************************
        # *                  IOSXE                   *
        # ********************************************

        # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500e-UNIVERSALK9-M), Version 03.04.06.SG RELEASE SOFTWARE (fc1)
        # Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.07E RELEASE SOFTWARE (fc3)
        # Cisco IOS XE Software, Version 17.05.01a
        # Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.07E RELEASE SOFTWARE (fc3)
        # Cisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.1a, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.03.02.SG RELEASE SOFTWARE (fc1)
        # Cisco IOS Software [Bengaluru], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.5.1a, RELEASE SOFTWARE (fc3)
        iosxe_os_version_platform_pattern = re.compile(r'^Cisco IOS.*XE Software(?:.*\((?P<platform>[^\-]+).*\))?,(?: Experimental)? Version (?P<version>[\w\.\(\)\:]+).*$')

        # cisco WS-C2940-8TT-S (RC32300) processor (revision H0) with 19868K bytes of memory.
        # cisco WS-C3650-48PD (MIPS) processor with 4194304K bytes of physical memory.
        # cisco C9500-24Y4C (X86) processor with 2900319K/6147K bytes of memory.
        # cisco CSR1000V (VXE) processor (revision VXE) with 715705K/3075K bytes of memory.
        iosxe_pid_pattern = re.compile(r'^[Cc]isco (?P<pid>\S+) \(.*\).* with \S+ bytes of(?: physical)? memory.$')

        # Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
        iosxe_backup_os_pattern = re.compile(r'^[Cc]isco IOS(?: |-)XE [Ss]oftware.*$')

        # Switch Ports Model              SW Version        SW Image              Mode
        # ------ ----- -----              ----------        ----------            ----
        # *    1 41    C9300-24P          17.07.01          CAT9K_IOSXE           INSTALL
        iosxe_backup_pid_version_pattern = re.compile(r'^\*?\s*\d+\s+\d+\s+(?P<pid>[\w\-]+)\s+(?P<version>[\w\-\.]+)\s+\w+\s+\w+$')

        # Model Number                       : C9300-24P
        iosxe_backup_pid_pattern = re.compile(r'^Model\s+Number\s+\:\s+(?P<pid>.+)$')
        # Router operating mode: Controller-Managed
        iosxe_sdwan_controller_mode = re.compile(r'^Router operating mode:\s+(?P<mode>\S+)\s*$')

        # Switch 02
        iosxe_switch_number_pattern = re.compile(r'^[Ss]witch +0(?P<switch_number>\d+)$')

        # ********************************************
        # *                  IOSXR                   *
        # ********************************************

        # Cisco IOS XR Software, Version 6.1.4.10I[Default]
        # Cisco IOS XR Software, Version 6.2.1.23I[Default]
        # Cisco IOS XR Software, Version 6.3.1.15I
        # Cisco IOS XR Software, Version 6.4.2[Default]
        # Cisco IOS XR Software, Version 7.5.1.20I LNT
        iosxr_os_version_pattern = re.compile(r'^Cisco IOS XR Software, Version (?P<version>[\w\.]+)(\[.*\])?\s*(?P<os_flavor>\w+)?$')

        # cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K bytes of memory.
        # cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 4193911K bytes of memory.
        # cisco IOS-XRv 9000 () processor
        # cisco CRS-16/S-B (Intel 686 F6M14S4) processor with 12582912K bytes of memory.
        iosxr_platform_pattern = re.compile(r'^cisco (?P<platform>\S+|IOS(?: |-)XRv ?\d*)(?: Series)? \(.*\) processor.*$')

        # ASR-9001 Chassis
        # ASR 9006 4 Line Card Slot Chassis
        iosxr_pid_pattern = re.compile(r'^(?P<pid>\w+[-\s]\d+) (Chassis|4 Line Card Slot Chassis( with V\d (AC|DC) PEM)?)?$')

        # ********************************************
        # *                  IOS                     *
        # ********************************************

        # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 15.2(2)E8, RELEASE SOFTWARE (fc1)
        # IOS (tm) C2940 Software (C2940-I6K2L2Q4-M), Version 12.1(22)EA12, RELEASE SOFTWARE (fc1)
        # Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E7, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software [Bengaluru], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.5.1a, RELEASE SOFTWARE (fc3)
        ios_os_version_platform_pattern = re.compile(r'^(?!.*XE Software.*)(Cisco IOS Software|IOS \(\S+\))(?: \[(?P<os_flavor>.*?)\])?,?\s*(?P<alternate_platform>.+)?\s+Software \((?P<platform>[^\-]+).*\),(?: Experimental)? Version (?P<version>[\w\.\:\(\)]+),?.*$')

        # Cisco CISCO1941/K9 (revision 1.0) with 491520K/32768K bytes of memory.
        # cisco CW9164I-ROW ARMv8 Processor rev 4 (v8l) with 1780316/936396K bytes of memo
        ios_pid_pattern = re.compile(r'^[Cc]isco (?P<pid>\S+) .*? with \S+ bytes of(?: physical)? mem.*$')

        # ********************************************
        # *                  JUNOS                   *
        # ********************************************

        # Junos: 18.2R2-S1
        junos_os_version_pattern = re.compile(r'^Junos: (?P<version>\S+)$')

        # Model: ex4200-24p
        junos_pid_pattern = re.compile(r'^Model: (?P<pid>\S+)$')


        # ********************************************
        # *                  NXOS                    *
        # ********************************************

        # Cisco Nexus Operating System (NX-OS) Software
        nxos_os_pattern = re.compile(r'^.*Nexus Operating System.*$')

        # system:    version 6.0(2)U6(10)
        # NXOS: version 9.3(6uu)I9(1uu) [build 9.3(6)]
        nxos_version_pattern = re.compile(r'^(?:system|NXOS):\s+version (?P<version>\S+)(?: \[build (?P<build>.*)\])?$')

        # cisco Nexus 3048 Chassis ("48x1GE + 4x10G Supervisor")
        # cisco Nexus9000 C9396PX Chassis
        nxos_platform_and_pid_pattern = re.compile(r'^cisco (?P<platform>Nexus\s?[\d]+) ?(?P<pid>\S+)? Chassis.*$')


        # ********************************************
        # *                 VIPTELLA                 *
        # ********************************************

        # 15.3.3
        viptella_os_pattern = re.compile(r'^(?P<version>[\d+\.]+)$')

        # ********************************************
        # *                 Wireless                 *
        # ********************************************

        # AP Running Image : 17.12.0.78
        wireless_ap_pattern = re.compile(r'^AP Running Image\s*:\s*(?P<version>[\d+.]+)$')

        # Product/Model Number                 : AIR-AP4800-D-K9
        wireless_pid_pattern = re.compile(r'^Product/Model Number\s*:\s*(?P<pid>\S+)\s*$')


        # ********************************************
        # *                 Wireless                 *
        # ********************************************

        # AP Running Image : 17.12.0.78
        wireless_ap_pattern = re.compile(r'^AP Running Image\s*:\s*(?P<version>[\d+.]+)$')

        for line in output.splitlines():
            line = line.strip()

            # ********************************************
            # *                  ASA                     *
            # ********************************************

            # Cisco Adaptive Security Appliance Software Version 9.8(4)10
            m = asa_os_version_pattern.match(line)
            if m:
                ret_dict['os'] = 'asa'
                ret_dict['version'] = m.groupdict()['version']
                continue

            # Hardware:   ASAv, 2048 MB RAM, CPU Xeon E5 series 3491 MHz,
            # Hardware:   ASA5520, 512 MB RAM, CPU Pentium 4 Celeron 2000 MHz
            m = asa_platform_pattern.match(line)
            if m:
                ret_dict['platform'] = m.groupdict()['platform']
                continue

            # Model Id:   ASAv10
            m = asa_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid'].lower()
                continue


            # ********************************************
            # *                  GAIA                    *
            # ********************************************

            # Product version Check Point Gaia R80.40
            m = gaia_os_version_pattern.match(line)
            if m:
                ret_dict['os'] = 'gaia'
                ret_dict['version'] = m.groupdict()['version']
                continue


            # ********************************************
            # *                  IOSXE                   *
            # ********************************************

            # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.04.06.SG RELEASE SOFTWARE (fc1)
            # Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.07E RELEASE SOFTWARE (fc3)
            # Cisco IOS XE Software, Version 17.05.01a
            # Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.07E RELEASE SOFTWARE (fc3)
            # Cisco IOS Software [Amsterdam], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.3.1a, RELEASE SOFTWARE (fc3)
            m = iosxe_os_version_platform_pattern.match(line)
            if m:
                ret_dict['os'] = 'iosxe'
                group = m.groupdict()
                ret_dict['version'] = group['version']
                if group['platform']:
                    platform = group['platform'].lower()
                    if 'x86_64_linux' not in platform:
                        ret_dict['platform'] = platform
                continue

            # cisco WS-C2940-8TT-S (RC32300) processor (revision H0) with 19868K bytes of memory.
            # cisco WS-C3650-48PD (MIPS) processor with 4194304K bytes of physical memory.
            # cisco C9500-24Y4C (X86) processor with 2900319K/6147K bytes of memory.
            m = iosxe_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                continue

            # Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
            # Cisco IOS XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
            m = iosxe_backup_os_pattern.match(line)
            if m:
                ret_dict['os'] = 'iosxe'
                continue

            # *    1 41    C9300-24P          17.07.01          CAT9K_IOSXE           INSTALL
            m = iosxe_backup_pid_version_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                ret_dict['version'] = m.groupdict()['version']
                continue

            # Model Number                       : C9300-24P
            m = iosxe_backup_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                continue

            # Controller Mode
            m = iosxe_sdwan_controller_mode.match(line)
            if m:
                ret_dict['operating_mode'] = m.groupdict().get('mode')
                continue

            # Switch 02
            m = iosxe_switch_number_pattern.match(line)
            if m:
                ret_dict['chassis_type'] = 'stack'
                continue
            # ********************************************
            # *                  IOSXR                   *
            # ********************************************

            # Cisco IOS XR Software, Version 6.1.4.10I[Default]
            # Cisco IOS XR Software, Version 6.2.1.23I[Default]
            # Cisco IOS XR Software, Version 6.3.1.15I
            # Cisco IOS XR Software, Version 6.4.2[Default]
            m = iosxr_os_version_pattern.match(line)
            if m:
                group = m.groupdict()
                ret_dict['os'] = 'iosxr'
                ret_dict['version'] = group['version']
                if group['os_flavor']:
                    ret_dict['os_flavor'] = group['os_flavor']
                continue

            # cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K bytes of memory.
            # cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 4193911K bytes of memory.
            # cisco IOS-XRv 9000 () processor
            # cisco CRS-16/S-B (Intel 686 F6M14S4) processor with 12582912K bytes of memory.
            m = iosxr_platform_pattern.match(line)
            if m:
                ret_dict['platform'] = m.groupdict()['platform'].lower()
                ret_dict['platform'] = \
                    re.sub(r'\s|\-', r'', m.groupdict()['platform'].lower())
                continue

            # ASR-9001 Chassis
            # ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            m = iosxr_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid'].replace(' ', '-')
                continue

            # ********************************************
            # *                  IOS                     *
            # ********************************************

            # Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 15.2(2)E8, RELEASE SOFTWARE (fc1)
            # IOS (tm) C2940 Software (C2940-I6K2L2Q4-M), Version 12.1(22)EA12, RELEASE SOFTWARE (fc1)
            # Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E7, RELEASE SOFTWARE (fc3)
            # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
            # Cisco IOS Software [Bengaluru], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 17.5.1a, RELEASE SOFTWARE (fc3)
            m = ios_os_version_platform_pattern.match(line)
            if m:
                group = m.groupdict()
                ret_dict['version'] = group['version']
                if ret_dict.get('os', None) is None:
                    ret_dict['os'] = 'ios'

                # Clean up platform a bit before adding to ret_dict
                platform = group['platform'].lower()
                if 'x86_64_linux' in platform:
                    if group['alternate_platform']:
                        platform = group['alternate_platform'].lower()
                    else:
                        continue

                ret_dict['platform'] = \
                    re.sub(r'\_(ios).*', r'', platform)
                ret_dict['platform'] = \
                    re.sub(r'cat(\d)\d{3}', r'cat\1k', ret_dict['platform'])

                if group['os_flavor']:
                    ret_dict['os_flavor'] = group['os_flavor'].lower()
                continue

            # Cisco CISCO1941/K9 (revision 1.0) with 491520K/32768K bytes of memory.
            m = ios_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                continue


            # ********************************************
            # *                  JUNOS                   *
            # ********************************************

            # Junos: 18.2R2-S1
            m = junos_os_version_pattern.match(line)
            if m:
                ret_dict['os'] = 'junos'
                ret_dict['version'] = m.groupdict()['version']
                continue

            # Model: ex4200-24p
            m = junos_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid'].lower()
                continue


            # ********************************************
            # *                  NXOS                    *
            # ********************************************

            # Cisco Nexus Operating System (NX-OS) Software
            m = nxos_os_pattern.match(line)
            if m:
                ret_dict['os'] = 'nxos'
                continue

            # system:    version 6.0(2)U6(10)
            # NXOS: version 9.3(6uu)I9(1uu) [build 9.3(6)]
            m = nxos_version_pattern.match(line)
            if m:
                group = m.groupdict()
                if group['build']:
                    ret_dict['build'] = group['build']
                ret_dict['version'] = group['version']
                continue

            # cisco Nexus 3048 Chassis ("48x1GE + 4x10G Supervisor")
            # cisco Nexus9000 C9396PX Chassis
            m = nxos_platform_and_pid_pattern.match(line)
            if m:
                group = m.groupdict()
                ret_dict['platform'] = group['platform'].lower()
                ret_dict['platform'] = re.sub(r'nexus\s*(\d)\d{3}', r'n\1k', ret_dict['platform'])
                if group['pid']:
                    ret_dict['pid'] = group['pid']
                continue

            # ********************************************
            # *                 VIPTELLA                 *
            # ********************************************

            # 15.3.3
            m = viptella_os_pattern.match(line)
            if m:
                ret_dict['os'] = 'viptella'
                ret_dict['version'] = m.groupdict()['version']
                continue

            # ********************************************
            # *                 Wireless                 *
            # ********************************************

            # AP Running Image     : 17.14.0.21
            m = wireless_ap_pattern.match(line)
            if m:
                ret_dict['os'] = 'cheetah'
                ret_dict['platform'] = 'ap'
                ret_dict['version'] = m.groupdict()['version']
                continue

            # Product/Model Number                 : AIR-AP4800-D-K9
            m = wireless_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                continue

            # ********************************************
            # *                  SONIC                   *
            # ********************************************

            # Model Number: 8201-32FH-O
            m = sonic_pid_pattern.match(line)
            if m:
                ret_dict['pid'] = m.groupdict()['pid']
                continue

        return ret_dict


class ShowInventorySchema(MetaParser):
    """Schema for show inventory"""
    schema = {
        Optional('chassis_type'): str,
        'inventory_item_index': {
            int: {
                'name': str,
                'description':   str,
                Optional('pid'): str,
                Optional('vid'): str,
                Optional('sn'):  str,
            }
        }
    }


class ShowInventory(ShowInventorySchema):
    """Parser for show inventory
    """

    cli_command = [
        'show inventory',
    ]

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # NAME: "Chassis", DESCR: "Cisco Catalyst Series C9500X-28C8D Chassis"
        # Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
        # NAME: "Rack 0", DESCR: "Cisco 8200 1RU w/24x100G & 8x400G, XR SW & HBM"
        p1 = re.compile(r'^(?:NAME|Name):\s+\"(?P<name>.+)\",\s+DESCR: \"(?P<description>.+)\"$')

        # PID: C9500X-28C8D      , VID: V00  , SN: FDO25030SLN
        p2 = re.compile(r'^PID:\s*(?P<pid>\S+)\s*,\s+VID:\s+(?P<vid>\S+)?\s*,\s+SN:\s*(?P<sn>\S+)?$')

        item_index = 0
        rp_count = 0
        name_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # NAME: "Chassis", DESCR: "Cisco Catalyst Series C9500X-28C8D Chassis"
            # Name: "Chassis", DESCR: "ASA 5555-X with SW, 8 GE Data, 1 GE Mgmt"
            # NAME: "Rack 0", DESCR: "Cisco 8200 1RU w/24x100G & 8x400G, XR SW & HBM"
            # NAME: "c92xx Stack", DESCR: "c92xx Stack"
            # NAME: "module R0", DESCR: "Cisco ASR1000 Route Processor 3"
            # NAME: "module R1", DESCR: "Cisco ASR1000 Route Processor 3"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['name']
                description = group['description']
                if name.endswith('hassis') or \
                    name.startswith('Rack') or \
                        description.endswith('hassis') or \
                            description.endswith('Stack') or \
                                'Virtual Router' in description:
                    name_dict = ret_dict.setdefault('inventory_item_index', {})\
                                        .setdefault(item_index, {})
                    name_dict['name'] = name
                    name_dict['description'] = description
                    item_index += 1

                if re.search('stack', name, flags=re.IGNORECASE):
                    ret_dict["chassis_type"] = 'stack'

                if re.search('Route Processor', description, flags=re.IGNORECASE):
                    rp_count += 1
                    if rp_count>1:
                        ret_dict["chassis_type"] = 'dual_rp'

                continue

            # PID: C9500X-28C8D      , VID: V00  , SN: FDO25030SLN
            m = p2.match(line)
            if m and name_dict:  # Only set once the chassis/stack has been seen
                group = m.groupdict()
                # Set only if there no existing value
                name_dict.setdefault('pid', group['pid'].replace(' ',''))
                if group['vid']:
                    name_dict.setdefault('vid', group['vid'].replace(' ',''))
                if group['sn']:
                    name_dict.setdefault('sn', group['sn'])
                continue

        return ret_dict

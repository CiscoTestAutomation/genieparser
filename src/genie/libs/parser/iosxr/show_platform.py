''' show_platform.py

IOSXR parsers for the following show commands:
    * 'show version'
    * 'show sdr detail'
    * 'show platform'
    * 'show platform vm'
    * 'show install active summary'
    * 'show install inactive summary'
    * 'show install commit summary'
    * 'show inventory'
    * 'admin show diag chassis'
    * 'show redundancy summary'
    * 'show redundancy'
    * 'dir'
    * 'dir {directory}'
    * 'dir location {location}'
    * 'dir {directory} location {location}'
    * 'show processes memory detail'
    * 'show processes memory detail | include <WORD>'
'''

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value,expression))
    return match

# =========================
# Parser for 'show version'
# =========================

class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {'operating_system': str,
              'software_version': str,
              'uptime': str,
              Optional('image'): str,
              Optional('device_family'): str,
              Optional('processor'): str,
              Optional('processor_memory_bytes'): str,
              Optional('chassis_detail'): str,
              Optional('config_register'): str,
              Optional('rp_config_register'): str,
              Optional('main_mem'): str,
             }

class ShowVersion(ShowVersionSchema):
    """Parser for show version"""
    cli_command = 'show version'
    exclude = ['seconds', 'minutes', 'hours', 'uptime']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        show_version_dict = {}

        # regex patterns

        # Cisco IOS XR Software, Version 6.3.1.15I
        # Cisco IOS XR Software, Version 6.1.4.10I[Default]
        p1 = re.compile(r'\s*Cisco +IOS +XR +Software, +Version'
                        ' +(?P<software_version>[A-Z0-9\.]+)(?:\[Default\])?(\sLNT)?$')

        # System uptime is 1 week, 1 day, 5 hours, 47 minutes
        # PE1 uptime is 3 hours, 11 minutes
        p2 = re.compile(r'\s*.* +uptime +is +(?P<uptime>[a-zA-Z0-9\s\,]+)$')

        # System image file is "disk0:asr9k-os-mbi-6.1.4.10I/0x100305/mbiasr9k-rsp3.vm"
        p3 = re.compile(r'\s*System +image +file +is'
                        ' +\"(?P<image>[a-zA-Z0-9\:\/\.\-]+)\"$')

        # cisco IOS-XRv 9000 () processor
        p4 = re.compile(r'\s*cisco +(?P<device_family>[a-zA-Z0-9\-\s]+)'
                        r' +\(\) +processor$')

        # cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K bytes of memory.
        # cisco CRS-16/S-B (Intel 686 F6M14S4) processor with 12582912K bytes of memory.
        p5 = re.compile(r'^cisco +(?P<device_family>[a-zA-Z0-9\/\-\s]+)'
                        r'(?:( +Series))? +\((?P<processor>[a-zA-Z0-9\s]+)\)'
                        r' +processor +with +(?P<processor_memory_bytes>[0-9A-Z]+)'
                        r' +bytes +of +memory.$')

        # Configuration register on node 0/RSP0/CPU0 is 0x1922
        p6 = re.compile(r'\s*Configuration +register +on +node'
                        ' +(?P<node>[A-Z0-9\/]+) +is'
                        ' +(?P<config_register>[x0-9]+)$')

        # ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
        p7 = re.compile(r'\s*.*Chassis.*$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                show_version_dict['operating_system'] = 'IOSXR'
                show_version_dict['software_version'] = \
                    str(m.groupdict()['software_version'])
                continue

            m = p2.match(line)
            if m:
                show_version_dict['uptime'] = str(m.groupdict()['uptime'])
                continue

            m = p3.match(line)
            if m:
                show_version_dict['image'] = str(m.groupdict()['image'])
                continue

            m = p4.match(line)

            if m:
                show_version_dict['device_family'] = \
                    str(m.groupdict()['device_family'])
                continue

            m = p5.match(line)
            if m:
                show_version_dict['device_family'] = \
                    m.groupdict()['device_family']
                show_version_dict['processor'] = m.groupdict()['processor']
                show_version_dict['processor_memory_bytes'] = \
                    m.groupdict()['processor_memory_bytes']
                show_version_dict['main_mem'] = line
                continue

            m = p6.match(line)
            if m:
                show_version_dict['config_register'] = \
                    m.groupdict()['config_register']
                node = str(m.groupdict()['node'])
                if re.search('CPU0', node):
                    show_version_dict['rp_config_register'] = \
                        str(m.groupdict()['config_register'])
                continue

            m = p7.match(line)
            if m:
                show_version_dict['chassis_detail'] = str(line.strip())
                continue

        return show_version_dict

# ============================
# Parser for 'show sdr detail'
# ============================

class ShowSdrDetailSchema(MetaParser):
    """Schema for show sdr detail"""
    schema = {
        'sdr_id':
            {Any():
                {'sdr_name': str,
                 Optional('dsdrsc_node'): str,
                 Optional('dsdrsc_partner_node'): str,
                 'primary_node1': str,
                 'primary_node2': str,
                 Optional('mac_address'): str,
                 'membership':
                    {Any():
                        {'type': str,
                         'node_status': str,
                         Optional('red_state'): str,
                         'partner_name': str,
                        },
                    },
                },
            },
        }

class ShowSdrDetail(ShowSdrDetailSchema):
    """Parser for show sdr detail"""
    cli_command = 'show sdr detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        sdr_detail = {}

        for line in out.splitlines():
            line = line.rstrip()

            # SDR_id               : 0
            # SDR ID             : 2
            p1 = re.compile(r'\s*(SDR_id|SDR ID) *: +(?P<sdr_id>[0-9]+)$')
            m = p1.match(line)
            if m:
                if 'sdr_id' not in sdr_detail:
                    sdr_detail['sdr_id'] = {}
                sdr_id = int(m.groupdict()['sdr_id'])
                if sdr_id not in sdr_detail['sdr_id']:
                    sdr_detail['sdr_id'][sdr_id] = {}
                continue

            # SDR_name             : Owner
            # SDR name           : default-sdr
            p2 = re.compile(r'\s*(SDR_name|SDR name) *:'
                             ' +(?P<sdr_name>[a-zA-Z\-]+)$')
            m = p2.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['sdr_name'] = \
                    str(m.groupdict()['sdr_name'])
                continue

            # dSDRsc node          : 0/0/CPU0
            p3 = re.compile(r'\s*dSDRsc +node *:'
                             ' +(?P<dsdrsc_node>[a-zA-Z0-9\/]+)$')
            m = p3.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['dsdrsc_node'] \
                    = str(m.groupdict()['dsdrsc_node'])
                continue

            # dSDRsc partner node  : NONE
            p4 = re.compile(r'\s*dSDRsc +partner +node *:'
                             ' +(?P<dsdrsc_partner_node>[a-zA-Z0-9\/]+)$')
            m = p4.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['dsdrsc_partner_node'] = \
                    str(m.groupdict()['dsdrsc_partner_node'])
                continue

            # primary node1        : 0/0/CPU0
            # SDR lead (Primary) : 0x1000
            p5 = re.compile(r'\s*(primary +node1|SDR +lead +\(Primary\)) *:'
                             ' +(?P<primary_node1>[a-zA-Z0-9\/]+)$')
            m = p5.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['primary_node1'] = \
                    str(m.groupdict()['primary_node1'])
                continue

            # primary node2        : NONE
            # SDR lead (Backup)  : 0xffffffff
            p6 = re.compile(r'\s*(primary +node2|SDR +lead +\(Backup\)) *:'
                             ' +(?P<primary_node2>[a-zA-Z0-9\/]+)$')
            m = p6.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['primary_node2'] = \
                    str(m.groupdict()['primary_node2'])
                continue

            # mac addr             : 025e.eaff.fb57
            p7 = re.compile(r'\s*mac +addr *:'
                             ' +(?P<mac_address>[a-zA-Z0-9\.]+)$')
            m = p7.match(line)
            if m:
                sdr_detail['sdr_id'][sdr_id]['mac_address'] = \
                    str(m.groupdict()['mac_address'])
                continue

            # RP         0/0/CPU0      IOS XR RUN        Primary    NONE
            # RP         0/RSP0/CPU0   IOS XR RUN        Primary    0/RSP1/CPU0
            # RP         0/RSP0/CPU0   IOS XR RUN        Primary    0/RSP1/CPU0
            p8 = re.compile(r'\s*(?P<type>[a-zA-Z0-9\-]+)'
                             ' +(?P<node_name>[a-zA-Z0-9\/]+)'
                             ' +(?P<node_status>[IOS XR RUN|OPERATIONAL|POWERED_ON]+)'
                             ' +(?P<red_state>[a-zA-Z\/\-]+)?'
                             ' +(?P<partner_name>[a-zA-Z0-9\/]+)$')
            m = p8.match(line)
            if m:
                if 'membership' not in sdr_detail['sdr_id'][sdr_id]:
                    sdr_detail['sdr_id'][sdr_id]['membership'] = {}

                node_name = str(m.groupdict()['node_name']).strip()

                if node_name not in sdr_detail['sdr_id'][sdr_id]['membership']:
                    sdr_detail['sdr_id'][sdr_id]['membership'][node_name] = {}
                    sdr_detail['sdr_id'][sdr_id]['membership'][node_name]\
                        ['type'] = str(m.groupdict()['type']).strip()
                    sdr_detail['sdr_id'][sdr_id]['membership'][node_name]\
                        ['node_status'] = \
                            str(m.groupdict()['node_status']).strip()
                    sdr_detail['sdr_id'][sdr_id]['membership'][node_name]\
                        ['red_state'] = str(m.groupdict()['red_state']).strip()
                    sdr_detail['sdr_id'][sdr_id]['membership'][node_name]\
                        ['partner_name'] = \
                            str(m.groupdict()['partner_name']).strip()
                    continue

        return sdr_detail

# ==========================
# Parser for 'show platform'
# ==========================

class ShowPlatformSchema(MetaParser):
    """Schema for show platform"""
    schema = {
        'slot':
            {Any():
                {Any():
                    {'name': str,
                     'state': str,
                     'config_state': str,
                     'full_slot': str,
                     Optional('redundancy_state'): str,
                     Optional('plim'): str,
                     Optional('subslot'):
                        {Optional(Any()):
                            {Optional('name'): str,
                             Optional('state'): str,
                             Optional('config_state'): str,
                             Optional('redundancy_state'): str,
                            },
                        },
                    },
                },
            },
        }

class ShowPlatform(ShowPlatformSchema):
    """Parser for show platform"""
    cli_command = 'show platform'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # 0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
        # 0/0/CPU0        RP(Active)      N/A             IOS XR RUN      PWR,NSHUT,MON
        # 0/0/CPU0        RP(Active)      N/A             OPERATIONAL      PWR,NSHUT,MON
        # 0/0               NCS1K4-OTN-XP              POWERED_ON        NSHUT
        # 0/1               NCS1K4-1.2T-K9             OPERATIONAL       NSHUT
        # 0/0               NCS1K4-OTN-XP              POWERED_ON        NSHUT
        # 1/3/3         MSC(SPA)          OC192RPR-XFP       DISABLED        NPWR,SHUT,MON
        # 1/10/CPU0     FP-X              N/A                UNPOWERED       NPWR,NSHUT,MON
        
        p1 = re.compile(r'^\s*(?P<node>[a-zA-Z0-9\/]+)'
                            '\s+(?P<name>[a-zA-Z0-9\-\.]+)'
                            '(?:\((?P<redundancy_state>[a-zA-Z]+)\))?'
                            '(?: +(?P<plim>[a-zA-Z0-9(\/|\-| )]+))?'
                            '\s+(?P<state>(UNPOWERED|DISABLED|IOS XR RUN|OK|OPERATIONAL|POWERED_ON))'
                            '\s+(?P<config_state>[a-zA-Z\,]+)$')            

        # Init vars
        show_platform = {}
        daughtercard_dict = {}

        for line in out.splitlines():
            entry_is_daughter = False
            line = line.rstrip()


            m = p1.match(line)
            if m:
                # Parse regexp
                node = str(m.groupdict()['node']).strip()
                name = str(m.groupdict()['name']).strip()
                redundancy_state = str(m.groupdict()['redundancy_state']).strip()
                plim = str(m.groupdict()['plim']).strip()
                state = str(m.groupdict()['state']).strip()
                config_state = str(m.groupdict()['config_state']).strip()

                # Parse node for rack, slot, subslot details
                parse_node = re.compile(r'\s*(?P<rack>[0-9]+)\/(?P<slot>[0-9A-Z]+)(?:\/(?P<last_entry>[0-9A-Z]+))?$').match(node)
                rack = str(parse_node.groupdict()['rack'])
                slot = rack + '/' + str(parse_node.groupdict()['slot'])
                last_entry = str(parse_node.groupdict()['last_entry'])

                # Check if subslot/daughtercard
                # 0/3/0 
                # 1/3/0  
                parse_subslot = re.compile(r'.*(0\/[0-9]\/[0-9]+).*').match(node)
                parse_subslot2 = re.compile(r'.*(1\/[0-9]\/[0-9]+).*').match(node)
                if (parse_subslot or parse_subslot2) and last_entry.isdigit():
                    # This entry is a daughtercard/subslot
                    entry_is_daughter = True
                    subslot = last_entry

                # Determine if slot is RP/LineCard/OtherCard
                parse_rp = re.compile(r'.*(RSP|RP).*').match(slot)
                parse_lc = re.compile(r'.*(0\/)\d').match(slot)
                parse_name = re.compile(r'.*(RSP|RP).*').match(name)
                if parse_rp or parse_name:
                    slot_type = 'rp'
                elif parse_lc:
                    slot_type = 'lc'
                else:
                    slot_type = 'oc'

                # Set everything
                if 'slot' not in show_platform:
                    show_platform['slot'] = {}
                if slot_type not in show_platform['slot']:
                    show_platform['slot'][slot_type] = {}
                if slot not in show_platform['slot'][slot_type]:
                    show_platform['slot'][slot_type][slot] = {}
                    show_platform['slot'][slot_type][slot]['name'] = name
                    show_platform['slot'][slot_type][slot]['full_slot'] = node
                    show_platform['slot'][slot_type][slot]['state'] = state
                    show_platform['slot'][slot_type][slot]['config_state'] = config_state
                    if redundancy_state != 'None':
                        show_platform['slot'][slot_type][slot]['redundancy_state'] = redundancy_state
                    if plim != 'None' and plim != '':
                        show_platform['slot'][slot_type][slot]['plim'] = plim
                    # Check for daughtercards
                    if daughtercard_dict and slot in daughtercard_dict:
                        # Then merge dictionary
                        show_platform['slot'][slot_type][slot]['subslot'].update(daughtercard_dict[slot])
                        continue

                # Check for daughtercards
                if entry_is_daughter:
                    # Verify parent exists
                    if slot in show_platform['slot'][slot_type]:
                        if 'subslot' not in show_platform['slot'][slot_type][slot]:
                            show_platform['slot'][slot_type][slot]['subslot'] = {}
                        if subslot not in show_platform['slot'][slot_type][slot]['subslot']:
                            show_platform['slot'][slot_type][slot]['subslot'][subslot] = {}
                            show_platform['slot'][slot_type][slot]['subslot'][subslot]['name'] = name
                            show_platform['slot'][slot_type][slot]['subslot'][subslot]['state'] = state
                            show_platform['slot'][slot_type][slot]['subslot'][subslot]['config_state'] = config_state
                            show_platform['slot'][slot_type][slot]['subslot'][subslot]['redundancy_state'] = redundancy_state
                            continue
                    else:
                        # Store in temp dict
                        if slot not in daughtercard_dict[slot]:
                            daughtercard_dict[slot] = {}
                        if 'subslot' not in daughtercard_dict:
                            daughtercard_dict[slot]['subslot'] = {}
                        if subslot not in daughtercard_dict[slot]['subslot']:
                            daughtercard_dict[slot]['subslot'][subslot] = {}
                            daughtercard_dict[slot]['subslot'][subslot]['name'] = name
                            daughtercard_dict[slot]['subslot'][subslot]['state'] = state
                            daughtercard_dict[slot]['subslot'][subslot]['config_state'] = config_state
                            daughtercard_dict[slot]['subslot'][subslot]['redundancy_state'] = redundancy_state
                            continue

        return show_platform

# =============================
# Parser for 'show platform vm'
# =============================

class ShowPlatformVmSchema(MetaParser):
    """Schema for show platform vm"""
    schema = {
        'node':
            {Any():
                {'type': str,
                 'partner_name': str,
                 'sw_status': str,
                 'ip_address': str,
                },
            },
        }

class ShowPlatformVm(ShowPlatformVmSchema):
    """Parser for show platform vm"""

    cli_command = 'show platform vm'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        show_platform_vm = {}

        for line in out.splitlines():
            line = line.strip()

            # 0/RP0/CPU0      RP (ACTIVE)     NONE            FINAL Band      192.0.0.4
            # 0/0/CPU0        LC (ACTIVE)     NONE            FINAL Band      192.0.0.6
            # 0/RSP0/CPU0     RP(ACTIVE)     0/RSP1/CPU0     FINAL Band      192.0.0.4
            # 0/RSP1/CPU0     RP(STANDBY)    0/RSP0/CPU0     FINAL Band      192.168.166.4

            p1 = re.compile(r'^(?P<node>[\S\/]+) +(?P<type>[(RP|LC)\s*\((ACTIVE|STANDBY)\)]+)'
                             ' +(?P<partner_name>[NONE|(?:\S)]+) +(?P<sw_status>[a-zA-Z\s]+)'
                             ' +(?P<ip_address>[\S]+)$')

            m = p1.match(line)
            if m:
                if 'node' not in show_platform_vm:
                    show_platform_vm['node'] = {}

                node = str(m.groupdict()['node']).strip()
                if node not in show_platform_vm['node']:
                    show_platform_vm['node'][node] = {}
                    show_platform_vm['node'][node]['type'] = \
                        str(m.groupdict()['type']).strip()
                    show_platform_vm['node'][node]['partner_name'] = \
                        str(m.groupdict()['partner_name']).strip()
                    show_platform_vm['node'][node]['sw_status'] = \
                        str(m.groupdict()['sw_status']).strip()
                    show_platform_vm['node'][node]['ip_address'] = \
                        str(m.groupdict()['ip_address']).strip()
                continue

        return show_platform_vm

# ========================================
# Schema for 'show install active summary'
# ========================================
class ShowInstallActiveSummarySchema(MetaParser):
    """Schema for show install active summary"""
    schema = {
        'active_packages': Any(),
        Optional('num_active_packages'): int,
        Optional('sdr'): str,
        }

class ShowInstallActiveSummary(ShowInstallActiveSummarySchema):
    """Parser for show install active summary"""

    cli_command = 'show install active summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        install_active_dict = {}
        previous_line_sdr = False
        previous_line_active_packages = False

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'\s*SDRs:*$')
            m = p1.match(line)
            if m:
                previous_line_sdr = True
                continue

            if previous_line_sdr:
                previous_line_sdr = False
                install_active_dict['sdr'] = str(line).strip()
                continue


            # disk0:xrvr-full-x-6.2.1.23I
            # disk0:asr9k-mini-px-6.1.21.15I
            # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
            p2 = re.compile(r'\s*Active +Packages:'
                             ' *(?P<num_active_packages>[0-9]+)?$')
            m = p2.match(line)
            if m:
                previous_line_active_packages = True
                if 'active_packages' not in install_active_dict:
                    install_active_dict['active_packages'] = []
                if m.groupdict()['num_active_packages']:
                    install_active_dict['num_active_packages'] = \
                        int(m.groupdict()['num_active_packages'])
                continue

            if previous_line_active_packages and line is not None:
                clean_line = str(line).strip()
                if line and '/' not in line:
                    install_active_dict['active_packages'].append(clean_line)
                    continue

        return install_active_dict

# ========================================
# Schema for 'show install inactive summary'
# ========================================
class ShowInstallInactiveSummarySchema(MetaParser):
    """Schema for show install inactive summary"""
    schema = {
        'inactive_packages': Any(),
        Optional('num_inactive_packages'): int,
        Optional('sdr'): list,
        }

class ShowInstallInactiveSummary(ShowInstallInactiveSummarySchema):
    """Parser for show install inactive summary"""

    cli_command = 'show install inactive summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        install_inactive_dict = {}
        previous_line_sdr = False
        previous_line_inactive_packages = False

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'\s*SDRs:*$')
            m = p1.match(line)
            if m:
                previous_line_sdr = True
                continue

            if previous_line_sdr:
                previous_line_sdr = False
                install_inactive_dict.setdefault('sdr', []).append(str(line).strip())
                continue


            # disk0:xrvr-full-x-6.2.1.23I
            # disk0:asr9k-mini-px-6.1.21.15I
            # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
            p2 = re.compile(r'\s*Inactive +Packages:'
                             ' *(?P<num_inactive_packages>[0-9]+)?$')
            m = p2.match(line)
            if m:
                previous_line_inactive_packages = True
                if 'inactive_packages' not in install_inactive_dict:
                    install_inactive_dict['inactive_packages'] = []
                if m.groupdict()['num_inactive_packages']:
                    install_inactive_dict['num_inactive_packages'] = \
                        int(m.groupdict()['num_inactive_packages'])
                continue

            if previous_line_inactive_packages and line is not None:
                clean_line = str(line).strip()
                if line and '/' not in line:
                    install_inactive_dict['inactive_packages'].append(clean_line)
                    continue

        return install_inactive_dict

# ========================================
# Schema for 'show install commit summary'
# ========================================
class ShowInstallCommitSummarySchema(MetaParser):
    """Schema for show install commit summary"""
    schema = {
        Optional('committed_packages'): Any(),
        Optional('active_packages'): Any(),
        Optional('num_committed_packages'): int,
        Optional('sdr'): list,
        }

class ShowInstallCommitSummary(ShowInstallCommitSummarySchema):
    """Parser for show install commit summary"""

    cli_command = 'show install commit summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        install_commit_dict = {}
        previous_line_sdr = False
        previous_line_committed_packages = False
        previous_line_active_packages = False

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'\s*SDRs:*$')
            m = p1.match(line)
            if m:
                previous_line_sdr = True
                continue

            if previous_line_sdr:
                previous_line_sdr = False
                install_commit_dict.setdefault('sdr', []).append(str(line).strip())
                continue


            # disk0:xrvr-full-x-6.2.1.23I
            # disk0:asr9k-mini-px-6.1.21.15I
            # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
            p2 = re.compile(r'\s*Committed +Packages:'
                             ' *(?P<num_committed_packages>[0-9]+)?$')
            m = p2.match(line)
            if m:
                previous_line_committed_packages = True
                if 'committed_packages' not in install_commit_dict:
                    install_commit_dict['committed_packages'] = []
                if m.groupdict()['num_committed_packages']:
                    install_commit_dict['num_committed_packages'] = \
                        int(m.groupdict()['num_committed_packages'])
                continue

            if previous_line_committed_packages and line is not None:
                clean_line = str(line).strip()
                if line and '/' not in line:
                    install_commit_dict['committed_packages'].append(clean_line)
                    continue

            # disk0:xrvr-full-x-6.2.1.23I
            # disk0:asr9k-mini-px-6.1.21.15I
            # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
            p2 = re.compile(r'\s*Active +Packages:'
                            ' *(?P<num_active_packages>[0-9]+)?$')
            m = p2.match(line)
            if m:
                previous_line_active_packages = True
                if 'active_packages' not in install_commit_dict:
                    install_commit_dict['active_packages'] = []
                if m.groupdict()['num_active_packages']:
                    install_commit_dict['num_active_packages'] = \
                        int(m.groupdict()['num_active_packages'])
                continue
            if previous_line_active_packages and line is not None:
                clean_line = str(line).strip()
                if line and '/' not in line:
                    install_commit_dict['active_packages'].append(clean_line)
                    continue

        return install_commit_dict

# ===========================
# Schema for 'show inventory'
# ===========================

class ShowInventorySchema(MetaParser):
    """Schema for show inventory"""
    schema = {
        'module_name':
            {Any():
                {'descr': str,
                 'pid': str,
                 'vid': str,
                 Optional('sn'): str,
                },
            },
        }

class ShowInventory(ShowInventorySchema):
    """Parser for show inventory"""

    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        inventory_dict = {}

        # NAME: "module 0/RSP0/CPU0", DESCR: "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB"
        # NAME: "Rack 0", DESCR: "Cisco XRv9K Centralized Virtual Router"
        # NAME: "Rack 0", DESCR: "Sherman 1RU Chassis with 24x400GE QSFP56-DD & 12x100G QSFP28"
        # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
        # NAME: "TenGigE0/0/0/0", DESCR: "Cisco SFP+ 10G SR Pluggable Optics Module"
        p1 = re.compile(r'^NAME: +\"(?P<module_name>[\S\s]*)\",'
                         r' +DESCR: +\"(?P<descr>[\S\s]*)\"$')

        # PID: A9K-MPA-20X1GE, VID: V02, SN: FOC1811N49J
        # PID: SFP-1G-NIC-X      , VID: N/A, SN: N/A
        # PID: N/A, VID: N/A, SN:
        p2 = re.compile(r'^PID: *(?P<pid>[\S\s]*),'
                         r' +VID: *(?P<vid>[\S\s]*),'
                         r' SN: *(?P<sn>[\S\s]*)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
            # NAME: "TenGigE0/0/0/0", DESCR: "Cisco SFP+ 10G SR Pluggable Optics Module"
            m = p1.match(line)
            if m:
                if 'module_name' not in inventory_dict:
                    inventory_dict['module_name'] = {}
                module_name = str(m.groupdict()['module_name'])
                if module_name not in inventory_dict['module_name']:
                    inventory_dict['module_name'][module_name] = {}
                    inventory_dict['module_name'][module_name]['descr'] = \
                        str(m.groupdict()['descr']).strip()
                    continue

            # PID: A9K-MPA-20X1GE, VID: V02, SN: FOC1811N49J
            # PID: SFP-1G-NIC-X      , VID: N/A, SN: N/A
            m = p2.match(line)
            if m:
                inventory_dict['module_name'][module_name]['pid'] = \
                    str(m.groupdict()['pid']).strip()
                inventory_dict['module_name'][module_name]['vid'] = \
                    str(m.groupdict()['vid']).strip()
                inventory_dict['module_name'][module_name]['sn'] = \
                    str(m.groupdict()['sn']).strip()
                continue
        return inventory_dict

# ====================================
# Schema for 'admin show diag chassis'
# ====================================

class AdminShowDiagChassisSchema(MetaParser):
    """Schema for admin show diag chassis"""
    schema = {
        Optional('device_family'): str,
        Optional('device_series'): str,
        Optional('num_line_cards'): int,
        Optional('chassis_feature'): str,
        Optional('controller_family'): str,
        Optional('controller_type'): str,
        'rack_num': int,
        Optional('sn'): str,
        'pid': str,
        'vid': str,
        Optional('desc'): str,
        'clei': str,
        Optional('eci'): str,
        Optional('pca'): str,
        Optional('top_assy_num'): str,
        Optional('main'): {
            'board_type': str,
            'part': str,
            'dev': str,
            'serial_number': str,
        },
        Optional('part_number'): str,
        Optional('part_revision'): str,
        Optional('hw_version'): str,
        Optional('top_assembly_block'): {
            Optional('serial_number'): str,
            'part_number': str,
            Optional('part_revision'): str,
            Optional('revision'): str,
            Optional('mfg_deviation'): str,
            Optional('hw_version'): str,
            Optional('mfg_bits'): str,
        }
    }

class AdminShowDiagChassis(AdminShowDiagChassisSchema):
    """Parser for admin show diag chassis"""
    cli_command = 'admin show diag chassis'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        admin_show_diag_dict = {}
        top_assembly_flag = False
        main_flag = False

        for line in out.splitlines():
            line = line.strip()

            # Rack 0 - ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            # Rack 0 - Cisco CRS Series 16 Slots Line Card Chassis
            # Rack 0 - CRS 16 Slots Line Card Chassis for CRS-16/S-B
            p1 = re.compile(r'Rack +(?P<rack_num>\d+) +-'
                            r' +(?P<device_group>[a-zA-Z0-9\s]+)'
                            r' +(?P<num_line_cards>\d+)'
                            r' +((Line +Card +Slot +Chassis +with *)|'
                            r'Slots +Line +Card +Chassis(?:( +for))? *)'
                            r'(?P<chassis_feature>[\S ]+)?$')

            m = p1.match(line)
            if m:
                admin_show_diag_dict['rack_num'] = \
                    int(m.groupdict()['rack_num'])

                # ASR 9006
                # Cisco CRS Series
                # CRS
                device_group = m.group(2)
                split_device_group = re.split(r'\s', device_group)
                if len(split_device_group)>1:
                    admin_show_diag_dict['device_family'] = \
                        split_device_group[0]
                    device_series = ' '.join(split_device_group[1:])
                else:
                    device_series = split_device_group[0]
                admin_show_diag_dict['device_series'] = device_series

                admin_show_diag_dict['num_line_cards'] = \
                    int(m.groupdict()['num_line_cards'])
                if m.groupdict()['chassis_feature']:
                    admin_show_diag_dict['chassis_feature'] = \
                        str(m.groupdict()['chassis_feature'])

                description = line[8:]
                admin_show_diag_dict['desc'] = description
                continue

            # RACK NUM: 0
            p2 = re.compile(r'RACK NUM\: *(?P<rack_num>[0-9]+)$')
            m = p2.match(line)
            if m:
                admin_show_diag_dict['rack_num'] = \
                    int(m.groupdict()['rack_num'])
                continue


            # S/N:   FOX1810G8LR
            # Serial Number   : FOC23158L99
            # Chassis Serial Number    : FOC23158L99
            # PCB Serial Number        : CAT2311B0AK
            p3 = re.compile(r'^(S\/N|((Chassis|PCB) +)?Serial +Number)(\s+)?(\:)? +(?P<serial_number>\S+)$')
            m = p3.match(line)
            if m:
                serial_num = str(m.groupdict()['serial_number'])
                if top_assembly_flag:
                    top_assembly_dict['serial_number'] = serial_num
                elif main_flag:
                    main_dict['serial_number'] = serial_num
                else:
                    admin_show_diag_dict['sn'] = serial_num

                continue

            # PID:   ASR-9006-AC-V2
            # Product ID      : NCS-5501
            p4 = re.compile(r'(PID|Product ID)(\s+)?\: '
                            r'+(?P<pid>[a-zA-Z0-9\-]+)$')
            m = p4.match(line)
            if m:
                admin_show_diag_dict['pid'] = \
                    str(m.groupdict()['pid'])
                continue

            # VID:   V02
            # VID             : V01
            # Version Identifier       : V01
            p5 = re.compile(r'(?:VID|Version +Identifier)(\s+)?\: +(?P<vid>[a-zA-Z0-9\-]+)$')
            m = p5.match(line)
            if m:
                admin_show_diag_dict['vid'] = \
                    str(m.groupdict()['vid'])
                continue

            # Desc:  ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            # UDI Description          : Network Convergence System 1004 4 line card slots
            p6 = re.compile(r'^(Desc\:|UDI Description\s+:) *(?P<desc>[\S\s]+)$')
            m = p6.match(line)
            if m:
                admin_show_diag_dict['desc'] = \
                    str(m.groupdict()['desc'])
                continue

            # CLEI:  IPMUP00BRB
            # CLEI Code       : INM1J10ARA
            p7 = re.compile(r'CLEI( +Code\s+)?: +(?P<clei>[a-zA-Z0-9\-]+)$')
            m = p7.match(line)
            if m:
                admin_show_diag_dict['clei'] = \
                    str(m.groupdict()['clei'])
                continue

            # Top Assy. Number:   68-4235-02
            p8 = re.compile(r'Top +Assy. +Number\:'
                            r' *(?P<top_assy_num>[a-zA-Z0-9\-\s]+)$')
            m = p8.match(line)
            if m:
                admin_show_diag_dict['top_assy_num'] = \
                    str(m.groupdict()['top_assy_num'])
                continue

            # PCA:   73-7806-01 rev B0
            p9 = re.compile(r'^PCA\: +(?P<pca>[\S ]+)$')
            m = p9.match(line)
            if m:
                admin_show_diag_dict['pca'] = \
                    str(m.groupdict()['pca'])
                continue

            # ECI:   459651
            p10 = re.compile(r'^ECI\: +(?P<eci>[\S ]+)$')
            m = p10.match(line)
            if m:
                admin_show_diag_dict['eci'] = \
                    str(m.groupdict()['eci'])
                continue

            # MAIN: board type 500060
            p11 = re.compile(r'^MAIN\: +board +type +(?P<board_type>[\S ]+)$')
            m = p11.match(line)
            if m:
                main_dict = admin_show_diag_dict.setdefault('main', {})
                main_dict['board_type'] = \
                    str(m.groupdict()['board_type'])
                continue

            # 800-25021-05 rev B0
            p12 = re.compile(r'^\S+ +rev +\S+')
            m = p12.match(line)
            if m:
                main_dict = admin_show_diag_dict.setdefault('main', {})
                main_dict['part'] = line.strip()
                continue

            # dev 080366, 080181
            p13 = re.compile(r'\s*dev +(?P<dev>[\S ]+)')
            m = p13.match(line)
            if m:
                dev = m.groupdict()['dev']
                main_dict = admin_show_diag_dict.setdefault('main', {})
                main_flag = True
                main_dict['dev'] = dev
                continue

            # 0 Rack 0-IDPROM Info
            # Rack 0-IDPROM Info
            # Rack 0-Chassis IDPROM Info
            p15 = re.compile(r'^(?:[0-9]+ +)?Rack +(?P<rack_num>[0-9]+)-(Chassis )?IDPROM +Info$')
            m15 = p15.match(line)
            if m15:
                admin_show_diag_dict['rack_num'] = \
                    int(m15.groupdict()['rack_num'])
                continue

            # Top +Assembly +Block\:$
            p16 = re.compile(r'Top +Assembly +Block\:$')
            m16 = p16.match(line)
            if m16:
                top_assembly_flag = True
                top_assembly_dict = admin_show_diag_dict.setdefault('top_assembly_block', {})

                continue

            # Part Number     : 73-101057-02
            p17 = re.compile(r'^Part +(n|N)umber(\s+)?\: +(?P<part_number>\S+)$')
            m17 = p17.match(line)
            if m17:
                part_num = str(m17.groupdict()['part_number'])
                if top_assembly_flag:
                    top_assembly_dict['part_number'] = part_num
                else:
                    admin_show_diag_dict['part_number'] = part_num

                continue

            # Top Assy. Part Number    : 73-101057-02
            p17_1 = re.compile(r'^Top +Assy\. +Part +Number +: +(?P<part_number>\S+)$')
            m = p17_1.match(line)
            if m:
                part_num = str(m.groupdict()['part_number'])
                top_assembly_dict = admin_show_diag_dict.setdefault('top_assembly_block', {})
                top_assembly_dict.update({'part_number': part_num})

            # Top Assy. Revision       : A0
            p17_2 = re.compile(r'^Top +Assy\. +Revision\s+: *(?P<revision>[\S\s]+)$')
            m = p17_2.match(line)
            if m:
                revision = m.groupdict()['revision']
                top_assembly_dict = admin_show_diag_dict.setdefault('top_assembly_block', {})
                top_assembly_dict.update({'revision': revision})
                continue

            # Part Revision   : D0
            p18 = re.compile(r'^Part +(r|R)evision(\s+)?\: +(?P<part_revision>\S+)$')
            m18 = p18.match(line)
            if m18:
                part_rev = str(m18.groupdict()['part_revision'])
                if top_assembly_flag:
                    top_assembly_dict['part_revision'] = part_rev
                else:
                    admin_show_diag_dict['part_revision'] = part_rev

                continue

            # H/W Version     : 1.0
            p19 = re.compile(r'^H\/W +[v|V]ersion(\s+)?\: +(?P<hw_version>\S+)$')
            m19 = p19.match(line)
            if m19:
                hw_ver = str(m19.groupdict()['hw_version'])
                if top_assembly_flag:
                    top_assembly_dict['hw_version'] = hw_ver
                else:
                    admin_show_diag_dict['hw_version'] = hw_ver

            # Mfg Deviation   : 0
            p20 = re.compile(r'^[M|m]fg +[D|d]eviation(\s+)?\: '
                             r'+(?P<mfg_deviation>\S+)$')
            m20 = p20.match(line)
            if m20:
                mfg_dev = str(m20.groupdict()['mfg_deviation'])
                top_assembly_dict['mfg_deviation'] = mfg_dev

                continue

            # Mfg Bits        : 1
            p21 = re.compile(r'^[M|m]fg +Bits(\s+)?\: +(?P<mfg_bits>\S+)$')
            m21 = p21.match(line)

            if m21:
                mfg_bit = str(m21.groupdict()['mfg_bits'])
                top_assembly_dict['mfg_bits'] = mfg_bit
                top_assembly_flag = False
                continue

            # Controller Family        : 0009
            p22 = re.compile(r'^Controller\s+Family\s+:\s+(?P<controller_family>\S+)$')
            m = p22.match(line)
            if m:
                controller_family = m.groupdict()['controller_family']
                admin_show_diag_dict['controller_family'] = controller_family
                continue

            # Controller Type          : 09d2
            p23 = re.compile(r'^Controller\s+Type\s+:\s+(?P<controller_type>\S+)$')
            m = p23.match(line)
            if m:
                controller_type = m.groupdict()['controller_type']
                admin_show_diag_dict['controller_type'] = controller_type
                continue

        return admin_show_diag_dict

# ====================================
# Schema for 'show redundancy summary'
# ====================================

class ShowRedundancySummarySchema(MetaParser):
    """Schema for show redundancy summary"""
    schema = {
        'node':
            {Any():
                {'type': str,
                 Optional('standby_node'): str,
                 Optional('backup_node'): str,
                 Optional('node_detail'): str,
                },
            },
        Optional('redundancy_communication'): bool,
        }

class ShowRedundancySummary(ShowRedundancySummarySchema):
    """Parser for show redundancy summary"""
    cli_command = 'show redundancy summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        redundancy_summary = {}
        redundancy_communication = False

        for line in out.splitlines():
            line = line.rstrip()

            p0 = re.compile(r'\s*Active.*$')
            m = p0.match(line)
            if m:
                continue

            # 0/RSP0/CPU0(A)   0/RSP1/CPU0(S) (Node Not Ready, NSR: Not Configured)
            p1 = re.compile(r'\s*(?P<node>[a-zA-Z0-9\/\(\)]+)'
                             ' +(?P<standby_node>[a-zA-Z0-9\/\(\)]+)'
                             ' +\((?P<node_detail>[a-zA-Z\,\:\s]+)\)$')
            m = p1.match(line)
            if m:
                if 'node' not in redundancy_summary:
                    redundancy_summary['node'] = {}

                # Check if node type is active or primary
                node = str(m.groupdict()['node']).strip()
                if re.search("\(P\)", node):
                    type = 'primary'
                else:
                    type = 'active'

                # Check standby or backup node
                backup_node = None
                standby_node = str(m.groupdict()['standby_node'])
                if re.search("\(B\)", standby_node):
                    backup_node = standby_node
                elif standby_node == 'N/A':
                    continue

                # set everything
                redundancy_summary['node'][node] = {}
                redundancy_summary['node'][node]['type'] = type
                redundancy_summary['node'][node]['standby_node'] = \
                    standby_node
                redundancy_summary['node'][node]['node_detail'] = \
                    str(m.groupdict()['node_detail'])

                if re.search(r'NSR: +Ready', str(m.groupdict()['node_detail'])):
                    redundancy_communication = True
                redundancy_summary['redundancy_communication'] = redundancy_communication
                if backup_node is not None:
                    redundancy_summary['node'][node]['backup_node'] = \
                        backup_node
                    continue

            # 0/0/CPU0             N/A
            p2 = re.compile(r'\s*(?P<node>[a-zA-Z0-9\/\(\)]+)'
                             ' +(?P<standby_node>[a-zA-Z0-9\/\(\)]+)$')
            m = p2.match(line)
            if m:
                if 'node' not in redundancy_summary:
                    redundancy_summary['node'] = {}

                # Check if node type is active or primary
                node = str(m.groupdict()['node']).strip()
                if re.search("\(P\)", node):
                    type = 'primary'
                else:
                    type = 'active'

                # Check standby or backup node
                backup_node = None
                standby_node = str(m.groupdict()['standby_node'])
                if re.search("\(B\)", standby_node):
                    backup_node = standby_node

                # set everything
                redundancy_summary['node'][node] = {}
                redundancy_summary['node'][node]['type'] = type
                redundancy_summary['node'][node]['standby_node'] = \
                    standby_node
                if backup_node is not None:
                    redundancy_summary['node'][node]['backup_node'] = \
                        backup_node
                    continue

        return redundancy_summary

# ============================
# Schema for 'show redundancy'
# ============================

class ShowRedundancySchema(MetaParser):
    """Schema for show redundancy"""
    schema = {
        'node':
            {Any():
                {'role': str,
                 Optional('valid_partner'): str,
                 Optional('ready'): str,
                 Optional('group'):
                    {Any():
                        {'primary': str,
                         'backup': str,
                         'status': str,
                        },
                    },
                 Optional('primary_rmf_state'): str,
                 Optional('primary_rmf_state_reason'): str,
                 'last_reload_timestamp': str,
                 'time_since_last_reload': str,
                 'node_uptime': str,
                 'node_uptime_timestamp': str,
                 'node_uptime_in_seconds': int,
                 Optional('standby_node'): str,
                 Optional('backup_process'): str,
                 Optional('last_switchover_timepstamp'): str,
                 Optional('time_since_last_switchover'): str,
                 Optional('standby_node_timestamp'): str,
                 Optional('time_since_standby_boot'): str,
                 Optional('standby_node_not_ready'): str,
                 Optional('time_since_standby_node_not_ready'): str,
                 Optional('standby_node_ready'):str,
                 Optional('time_since_standby_node_ready'): str,
                 Optional('reload_cause'): str
                },
            },
        }

class ShowRedundancy(ShowRedundancySchema):
    """Parser for show redundancy"""
    cli_command = 'show redundancy'
    exclude = ['node_uptime', 'time_since_standby_boot',
        'time_since_last_reload', 'time_since_last_switchover',
        'time_since_standby_node_not_ready', 'time_since_standby_node_ready',
        'standby_node_not_ready', 'standby_node_ready',
        'standby_node_timestamp', 'node_uptime_in_seconds', 'iteration:']


    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        redundancy_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Redundancy information for node 0/RP0/CPU0
            p1 = re.compile(r'\s*Redundancy +information +for +node'
                             ' +(?P<node>[a-zA-Z0-9\/]+):$')
            m = p1.match(line)
            if m:
                if 'node' not in redundancy_dict:
                    redundancy_dict['node'] = {}
                node = str(m.groupdict()['node'])
                if node not in redundancy_dict['node']:
                    redundancy_dict['node'][node] = {}
                    continue

            # Node 0/RSP0/CPU0 is in ACTIVE role
            p2 = re.compile(r'\s*Node +([a-zA-Z0-9\/]+) +is +in'
                             ' +(?P<role>[a-zA-Z]+) +role$')
            m = p2.match(line)
            if m:
                redundancy_dict['node'][node]['role'] = \
                    str(m.groupdict()['role'])
                continue

            # Node Redundancy Partner (0/RSP1/CPU0) is in STANDBY role
            p3_1 =  re.compile(r'\s*Node *Redundancy *Partner'
                                ' *\((?P<node>[a-zA-Z0-9\/]+)\) *is *in'
                                ' *(?P<role>[a-zA-Z]+) *role$')
            m = p3_1.match(line)
            if m:
                if 'standby' in str(m.groupdict()['role']).lower():
                    redundancy_dict['node'][node]['standby_node'] = str(m.groupdict()['node'])
                continue
            
            # Partner node (0/RP1/CPU0) is in STANDBY role (eXR)
            p3_2 =  re.compile(r'\s*Partner *node'
                                ' *\((?P<node>[a-zA-Z0-9\/]+)\) *is *in'
                                ' *(?P<role>[a-zA-Z]+) *role$')
            m = p3_2.match(line)
            if m:
                if 'standby' in str(m.groupdict()['role']).lower():
                    redundancy_dict['node'][node]['standby_node'] = str(m.groupdict()['node'])
                continue

            # Process Redundancy Partner (0/RSP0/CPU0) is in BACKUP role
            p3_3 =  re.compile(r'\s*Process *Redundancy *Partner'
                                ' *\((?P<node>[a-zA-Z0-9\/]+)\) *is *in'
                                ' *(?P<role>[a-zA-Z]+) *role$')
            m = p3_3.match(line)
            if m:
                if 'backup' in str(m.groupdict()['role']).lower():
                    redundancy_dict['node'][node]['backup_process'] = str(m.groupdict()['node'])
                continue

            # Standby node in 0/RSP1/CPU0 is ready
            # Standby node in 0/RSP1/CPU0 is NSR-ready
            p3_2 = re.compile(r'\s*Standby *node *in *([a-zA-Z0-9\/]+)'
                               ' *is *(?P<ready>[a-zA-Z\-]+)$')
            m = p3_2.match(line)
            if m:
                redundancy_dict['node'][node]['ready'] = \
                    str(m.groupdict()['ready'])
                continue

            # Node 0/RP0/CPU0 has no valid partner
            p3 = re.compile(r'\s*Node +([a-zA-Z0-9\/]+) +has +(?P<valid_partner>\S+)'
                             ' +valid +partner$')
            m = p3.match(line)
            if m:
                redundancy_dict['node'][node]['valid_partner'] = \
                str(m.groupdict()['valid_partner'])
                continue

            # v6-routing       0/RSP0/CPU0     N/A             Not Ready
            p4 = re.compile(r'\s*(?P<group>[a-zA-Z0-9\-]+)'
                             ' +(?P<primary>[A-Z0-9\/]+)'
                             ' +(?P<backup>[A-Z0-9\/]+)'
                             ' +(?P<status>[a-zA-Z\-\s]+)$')
            m = p4.match(line)
            if m:
                if 'group' not in redundancy_dict['node'][node]:
                    redundancy_dict['node'][node]['group'] = {}

                group = str(m.groupdict()['group'])
                if group not in redundancy_dict['node'][node]['group']:
                    redundancy_dict['node'][node]['group'][group] = {}
                    redundancy_dict['node'][node]['group'][group]['primary'] = \
                        str(m.groupdict()['primary'])
                    redundancy_dict['node'][node]['group'][group]['backup'] = \
                        str(m.groupdict()['backup'])
                    redundancy_dict['node'][node]['group'][group]['status'] = \
                        str(m.groupdict()['status'])
                    continue

            # NSR not ready since Backup is not Present
            p5 = re.compile(r'\s*NSR +(?P<primary_rmf_state>[a-zA-Z\s]+) +since'
                             ' +(?P<primary_rmf_state_reason>[a-zA-Z\s]+)$')
            m = p5.match(line)
            if m:
                redundancy_dict['node'][node]['primary_rmf_state'] = \
                    str(m.groupdict()['primary_rmf_state'])
                redundancy_dict['node'][node]\
                    ['primary_rmf_state_reason'] = \
                    str(m.groupdict()['primary_rmf_state_reason'])
                continue

            # A9K-RSP440-TR reloaded Thu Apr 27 02:14:12 2017: 1 hour, 16 minutes ago
            p6 = re.compile(r'\s*(?P<node_name>[a-zA-Z0-9\-]+) +reloaded'
                             ' +(?P<last_reload_timestamp>[a-zA-Z0-9\:\s]+):'
                             ' +(?P<time_since_last_reload>[a-zA-Z0-9\,\s]+)$')
            m = p6.match(line)
            if m:
                redundancy_dict['node'][node]['last_reload_timestamp'] =\
                    str(m.groupdict()['last_reload_timestamp'])
                redundancy_dict['node'][node]['time_since_last_reload'] =\
                    str(m.groupdict()['time_since_last_reload'])
                continue

            # Active node booted Thu Apr 27 03:22:37 2017: 8 minutes ago
            # Active node booted Thu Jan 11 12:31:59 2018: 5 days, 23 hours,  ago
            # Active node booted Tue Jan  2 07:32:33 2018: 1 day, 1 hour, 6 minutes ago
            # Active node booted Thu Jan 11 12:32:03 2018: 1 week, 4 days, 20 hours, 19 minutes ago
            p7 = re.compile(r'\s*Active +node +booted'
                            ' +(?P<node_uptime_timestamp>[a-zA-Z0-9\:\s]+):'
                            ' +(?P<node_uptime>((?P<ignore>\d+ \w+, *)?((?P<week>\d+) +(week|weeks), )?'
                            '(((?P<day>\d+) +(day|days))?, )?)?(((?P<hour>\d+) +(hour|hours))?, )?'
                            '(((?P<minute>\d+) +(minute|minutes))|((?P<second>\d+) +(seconds|seconds)))?) +ago$')
            m = p7.match(line)
            if m:
                redundancy_dict['node'][node]['node_uptime_timestamp'] = \
                    str(m.groupdict()['node_uptime_timestamp'])
                redundancy_dict['node'][node]['node_uptime'] = \
                    str(m.groupdict()['node_uptime'])
                time_in_seconds = 0
                if m.groupdict()['week']:
                    time_in_seconds += int(m.groupdict()['week']) * 7 * 86400
                if m.groupdict()['day']:
                    time_in_seconds += int(m.groupdict()['day']) * 86400
                if m.groupdict()['hour']:
                    time_in_seconds += int(m.groupdict()['hour']) * 3600
                if m.groupdict()['minute']:
                    time_in_seconds += int(m.groupdict()['minute']) * 60
                if m.groupdict()['second']:
                    time_in_seconds += int(m.groupdict()['second'])
                redundancy_dict['node'][node]['node_uptime_in_seconds'] = \
                    time_in_seconds
                continue

            # Standby node boot Thu Aug 10 08:29:18 2017: 1 day, 32 minutes ago
            p7_1 = re.compile(r'\s*Standby +node +boot'
                               ' +(?P<standby_node_timestamp>[a-zA-Z0-9\:\s]+):'
                               ' +(?P<time_since_standby_boot>[a-zA-Z0-9\,\s]+)$')
            m = p7_1.match(line)
            if m:
                standby_node_timestamp = str(m.groupdict()['standby_node_timestamp'])
                time_since_standby_boot = str(m.groupdict()['time_since_standby_boot'])

                redundancy_dict['node'][node]['standby_node_timestamp'] = \
                standby_node_timestamp
                redundancy_dict['node'][node]['time_since_standby_boot'] = \
                time_since_standby_boot
                continue

            # Standby node last went not ready Fri Aug 11 07:13:26 2017: 1 hour, 48 minutes ago
            # Standby node last went ready Fri Aug 11 07:13:26 2017: 1 hour, 48 minutes ago

            p7_2 = re.compile(r'\s*Standby *node *last *went *not *ready'
                               ' *(?P<standby_node_not_ready>[a-zA-Z0-9\:\s]+):'
                               ' *(?P<time_since_standby_node_not_ready>[a-zA-Z0-9\,\s]+)$')
            m = p7_2.match(line)
            if m:
                standby_node_not_ready = str(m.groupdict()['standby_node_not_ready'])
                time_since_standby_node_not_ready = str(m.groupdict()['time_since_standby_node_not_ready'])

                redundancy_dict['node'][node]['standby_node_not_ready'] = \
                standby_node_not_ready
                redundancy_dict['node'][node]['time_since_standby_node_not_ready'] = \
                time_since_standby_node_not_ready
                continue

            p7_3 = re.compile(r'\s*Standby *node *last *went *ready'
                               ' *(?P<standby_node_ready>[a-zA-Z0-9\:\s]+):'
                               ' *(?P<time_since_standby_node_ready>[a-zA-Z0-9\,\s]+)$')
            m = p7_3.match(line)
            if m:
                standby_node_ready = str(m.groupdict()['standby_node_ready'])
                time_since_standby_node_ready = str(m.groupdict()['time_since_standby_node_ready'])

                redundancy_dict['node'][node]['standby_node_ready'] = \
                standby_node_ready
                redundancy_dict['node'][node]['time_since_standby_node_ready'] = \
                time_since_standby_node_ready
                continue

            # Last switch-over Thu Apr 27 03:29:57 2017: 1 minute ago
            p8 = re.compile(r'\s*Last +switch-over'
                        ' +(?P<last_switchover_timepstamp>[a-zA-Z0-9\:\s]+):'
                        ' +(?P<time_since_last_switchover>[a-zA-Z0-9\,\s]+)$')
            m = p8.match(line)
            if m:
                redundancy_dict['node'][node]['last_switchover_timepstamp'] = \
                    str(m.groupdict()['last_switchover_timepstamp'])
                redundancy_dict['node'][node]['time_since_last_switchover'] = \
                    str(m.groupdict()['time_since_last_switchover'])
                continue

            # Active node reload  Cause: Initiating switch-over.
            p9 = re.compile(r'\s*Active +node +reload *(?:Cause)?:'
                             ' +(?P<reload_cause>[a-zA-Z\-\s]+).$')
            m = p9.match(line)
            if m:
                redundancy_dict['node'][node]['reload_cause'] = \
                    str(m.groupdict()['reload_cause'])
                continue

        return redundancy_dict

# ================
# Schema for 'dir'
# ================
class DirSchema(MetaParser):
    """Schema for 
        * dir
        * dir {directory}
        * dir location {location}
        * dir {directory} location {location}
    """

    schema = {
        'dir': {
            'dir_name': str,
            'total_bytes': str,
            'total_free_bytes': str,
            Optional('location'): str,
            Optional('files'):
                {Any():
                    {Optional('size'): str,
                     Optional('date'): str,
                     Optional('permission'): str,
                     Optional('index'): str,
                     Optional('time'): str,
                     Optional('date'): str}
                },
            },
        }

class Dir(DirSchema):
    """Parser for
        * dir
        * dir {directory}
        * dir location {location}
        * dir {directory} location {location}
    """

    cli_command = [
        'dir', 'dir {directory}', 'dir location {location}',
        'dir {directory} location {location}'
    ]

    exclude = ['size', 'time', 'total_free_bytes', 'date', 'index']

    def cli(self, directory='', location='', output=None):
        if output is None:
            if directory and location:
                out = self.device.execute(self.cli_command[3].format(
                    directory=directory, location=location))
            elif location:
                out = self.device.execute(
                    self.cli_command[2].format(location=location))
            elif directory:
                out = self.device.execute(
                    self.cli_command[1].format(directory=directory))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        dir_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Directory of /misc/scratch
            # Directory of disk0a:/usr
            # Directory of net/node0_RSP1_CPU0/harddisk:/dumper
            p1 = re.compile(r'\s*Directory\s+of\s+(?P<dir_name>\S+)$')
            m = p1.match(line)
            if m:
                if 'dir' not in dir_dict:
                    dir_dict['dir'] = {}
                    dir_dict['dir']['dir_name'] = str(m.groupdict()['dir_name'])
                    if location:
                        dir_dict['dir']['location'] = location
                continue

            # 1012660 kbytes total (939092 kbytes free)
            # 2562719744 bytes total (1918621184 bytes free)
            p2 = re.compile(r'\s*(?P<total_bytes>[0-9]+ +(kbytes|bytes))'
                             ' +total +\((?P<total_free_bytes>[0-9]+'
                             ' +(kbytes|bytes)) +free\)$')
            m = p2.match(line)
            if m:
                dir_dict['dir']['total_bytes'] = \
                        str(m.groupdict()['total_bytes'])
                dir_dict['dir']['total_free_bytes'] = \
                    str(m.groupdict()['total_free_bytes'])
                continue

            # 20 -rw-r--r-- 1   773 May 10  2017 cvac.log
            # 15 lrwxrwxrwx 1    12 May 10  2017 config -> /misc/config
            # 11 drwx------ 2 16384 Mar 28 12:23 lost+found
            # 14 -rw-r--r--. 1 10429 Oct 26 16:17 pnet_cfg.log
            # 10541310    -rwx  6142        Mon May 18 19:16:01 2020  prod2_vxlan_config

            p3 = re.compile(r'^\s*(?P<index>[0-9]+) +(?P<permission>[a-z\-]+)(\.)?('
                            ' +(?P<unknown>[0-9]+))? +(?P<size>[0-9]+)( +(?P<date>[a-zA-Z]{3}))? '
                            '+(?P<month>[a-zA-Z]{3}) +(?P<day>[0-9]{,3})( +(?P<time>[\d\:]+))?( '
                            '+(?P<year>[0-9]{4}))? +(?P<file>[a-zA-Z0-9\.\/\_\-\+\>\s]+)$')
            m = p3.match(line)
            if m:
                file = m.groupdict()['file']
                date = m.groupdict()['month'].strip() \
                    + ' ' + m.groupdict()['day'].strip()

                if m.groupdict()['time']:
                    date = date + ' ' + m.groupdict()['time'].strip()

                if m.groupdict()['year']:
                    date = date + ' ' + m.groupdict()['year'].strip()

                if m.groupdict()['date']:
                    date = m.groupdict()['date'].strip() + ' ' + date

                if 'files' not in dir_dict['dir']:
                    dir_dict['dir']['files'] = {}
                dir_dict['dir']['files'][file] = {}
                dir_dict['dir']['files'][file]['size'] = m.groupdict()['size']
                dir_dict['dir']['files'][file]['permission'] = \
                    m.groupdict()['permission']
                dir_dict['dir']['files'][file]['index'] = m.groupdict()['index']
                dir_dict['dir']['files'][file]['date'] = date
                continue

        return dir_dict


class ShowProcessesMemorySchema(MetaParser):
    """Schema for show processes memory
                  show processes memory | include <WORD>
    """

    schema = {
        'jid': {
            Any(): {
                'index':{
                    Any():{
                        'jid': int,
                        'text': int,
                        'data': int,
                        'stack': int,
                        'dynamic': int,
                        'process': str,
                    }
                }
            }
        }
    }


class ShowProcessesMemory(ShowProcessesMemorySchema):
    """Schema for show processes memory
                  show processes memory | include <WORD>
    """

    cli_command = [
        'show processes memory', 'show processes memory | include {include}'
    ]

    def cli(self, include=None, output=None):

        ret_dict = {}
        jid_index = {}

        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        #  8178  45387776  4294967295  1029939200  ffc31360/ffc311a0  bgp
        p1 = re.compile(
            r'^(\s+)?(?P<jid>\d+)\s+(?P<text>\d+)\s+(?P<data>\d+)\s+(?P<stack>\d+)\s+(?P<dynamic>\S+)\s+(?P<process>\S+)'
        )

        for line in out.splitlines():
            line = line.strip()

            #  8178  45387776  4294967295  1029939200  ffc31360/ffc311a0  bgp
            m = p1.match(line)
            if m:
                group = m.groupdict()
                jid = int(group['jid'])
                index = jid_index.get(jid, 0) + 1
                jid_dict = ret_dict.setdefault('jid', {}). \
                    setdefault(jid, {}). \
                    setdefault('index', {}). \
                    setdefault(index, {})

                jid_index.update({jid: index})

                jid_dict.update({
                    k: int(v) if v.isdigit() else v
                    for k, v in group.items() if v is not None
                })

        return ret_dict


class ShowProcessesMemoryDetailSchema(MetaParser):
    """Schema for show processes memory detail
                  show processes memory detail | include <WORD>
    """

    schema = {
        'jid': {
            int: {
                'index': {
                    int: {
                        'jid': int,
                        'text': str,
                        'data': str,
                        'stack': str,
                        'dynamic': str,
                        'dyn_limit': str,
                        'shm_tot': str,
                        'phy_tot': str,
                        'process': str,
                    }
                }
            }
        }
    }


class ShowProcessesMemoryDetail(ShowProcessesMemoryDetailSchema):
    """Schema for show processes memory detail
                  show processes memory detail | include <WORD>
    """

    cli_command = [
        'show processes memory detail',
        'show processes memory detail | include {include}'
    ]

    def cli(self, include=None, output=None):

        ret_dict = {}
        jid_index = {}

        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        #  1078           2M      1021M       136K        39M     14894M        23M        62M bgp
        #  1257          60K       261M       136K         1M  unlimited         6M         9M bgp_epe
        p1 = re.compile(
            r'^(\s+)?(?P<jid>\d+)\s+(?P<text>\S+)\s+(?P<data>\S+)\s+(?P<stack>\S+)\s+(?P<dynamic>\S+)\s+(?P<dyn_limit>\S+)\s+(?P<shm_tot>\S+)\s+(?P<phy_tot>\S+)\s+(?P<process>\S+)'
        )

        for line in out.splitlines():
            line = line.strip()

            #  1078           2M      1021M       136K        39M     14894M        23M        62M bgp
            #  1257          60K       261M       136K         1M  unlimited         6M         9M bgp_epe
            m = p1.match(line)
            if m:
                group = m.groupdict()
                jid = int(group['jid'])
                index = jid_index.get(jid, 0) + 1
                jid_index.update({jid: index})
                jid_dict = ret_dict.setdefault('jid', {}). \
                    setdefault(jid, {}). \
                    setdefault('index', {}). \
                    setdefault(index, {})

                jid_dict.update({
                    k: int(v) if v.isdigit() else v
                    for k, v in group.items()
                })

        return ret_dict

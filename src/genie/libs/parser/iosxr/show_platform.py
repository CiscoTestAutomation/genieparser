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
    * 'show diag details'
    * 'show redundancy summary'
    * 'show redundancy'
    * 'dir'
    * 'dir {directory}'
    * 'dir location {location}'
    * 'dir {directory} location {location}'
    * 'show processes memory detail'
    * 'show processes memory detail | include <WORD>'
    * 'show filesystem location all'
'''

# Python
import re
import xmltodict
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


logger = logging.getLogger(__name__)


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
              Optional('built_by'): str,
              Optional('built_on'): str,
              Optional('built_host'): str,
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

        # cisco 8201-32FH (Intel(R) Xeon(R) CPU D-1530 @ 2.40GHz) processor with 32GB of memory
        # cisco 8202-32FH-M (Intel(R) Xeon(R) CPU D-1530 @ 2.40GHz) processor with 64GB of memory
        p5_1 = re.compile(r'^cisco +(?P<pid>[a-zA-Z0-9\/\-\s]+)'
                          r' +\((?P<processor>.+)\)'
                          r' +processor +with +(?P<processor_memory_bytes>[0-9A-Z]+)'
                          r' +of +memory$')

        # Configuration register on node 0/RSP0/CPU0 is 0x1922
        p6 = re.compile(r'\s*Configuration +register +on +node'
                        ' +(?P<node>[A-Z0-9\/]+) +is'
                        ' +(?P<config_register>[x0-9]+)$')

        # ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
        p7 = re.compile(r'\s*.*Chassis.*$')

        # Built By     : xyz
        p8 = re.compile(r'^Built\s+By\s*:\s+(?P<built_by>\S+)$')

        # Built On     : Fri Dec 13 16:42:11 PST 2019
        p9 = re.compile(r'^Built\s+On\s*:\s+(?P<built_on>[a-zA-Z0-9\:\/\.\-\s]+)$')

        # Built Host   : iox-abc-123
        p10 = re.compile(r'^Built\s+Host\s*:\s*(?P<built_host>\S+)$')

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

            m = p5_1.match(line)
            if m:
                show_version_dict['chassis_detail'] = \
                    m.groupdict()['pid']
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
                show_version_dict.setdefault('chassis_detail', str(line.strip()))
                continue

            m = p8.match(line)
            if m:
                show_version_dict['built_by'] = m.groupdict()['built_by']
                continue

            m = p9.match(line)
            if m:
                show_version_dict['built_on'] = m.groupdict()['built_on']
                continue

            m = p10.match(line)
            if m:
                show_version_dict['built_host'] = m.groupdict()['built_host']
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
                parse_node = re.compile(r'\s*(?P<rack>[A-Z0-9]+)\/(?P<slot>[0-9A-Z]+)(?:\/(?P<last_entry>[0-9A-Z]+))?$').match(node)
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
        Optional('active_packages'): Any(),
        Optional('num_active_packages'): int,
        Optional('sdr'): str,
        Optional('label'): str,
        Optional('software_hash'): str,
        Optional('optional_packages'): {str: str},
        Optional('mandatory_packages'): {str: str},
        Optional('active_fixes'): {str: str},
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
        #   SDRs:
        p1 = re.compile(r'\s*SDRs:*$')

        # disk0:xrvr-full-x-6.2.1.23I
        # disk0:asr9k-mini-px-6.1.21.15I
        # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
        p2 = re.compile(r'\s*Active +Packages:'
                                ' *(?P<num_active_packages>[0-9]+)?$')

        # Active Packages: XR: 201    All: 1532
        p3 = re.compile(r'^Active +Packages: +XR: +(?P<xr>[\d]+)\s+All: +(?P<all>[\d]+)$')

        # Label:              7.10.2-meta_7102_fcs_01_25_2024
        p4 = re.compile(r'^Label:\s+(?P<label>[\w\.\-]+)$')

        # Software Hash:      454175afbe3ad586c3b39a79db238b53844fe794723ea99fa00ac1acd5442359
        p5 = re.compile(r'^Software +Hash:\s+(?P<sh>[\w]+)$')

        # Optional Packages                                                        Version
        # ---------------------------------------------------- ---------------------------
        # xr-8000-netflow                                                   7.10.2v1.0.0-1
        # xr-bgp                                                            7.10.2v1.0.0-1
        p6 = re.compile(r'^(?P<optional_packages>[\w\-]+)\s+(?P<version>[\w\.\-]+)$')

        # Mandatory Packages with Committed Bugfixes                               Version
        # xr-8000-core                                                      7.10.2v1.0.1-1
        # xr-8000-cpa-npu                                                   7.10.2v1.0.2-1
        p7 = re.compile(r'^(?P<mandatory_packages>[\w\-]+)\s+(?P<version>[\w\.\-]+)$')

        # Active Fixes (count: 6):
        p8 = re.compile(r"Active Fixes \(count: (?P<count>\d+)\):")

        # CSCwh02785: xr-fib
        # CSCwh80170: xr-8000-cpa-npu
        # CSCwi62344: xr-8000-core, xr-8000-cpa-npu, xr-8000-leabaofa, xr-networkboot
        p9 = re.compile(r'^\s*(?P<bug_id>CSC\w+): (?P<package_name>[\w\-\,\ ]+)$')

        for line in out.splitlines():
            line = line.rstrip()
            if line.startswith('-'):
                continue

            m = p1.match(line)
            if m:
                previous_line_sdr = True
                continue

            if previous_line_sdr:
                previous_line_sdr = False
                install_active_dict['sdr'] = str(line).strip()
                continue

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

            m = p3.match(line)
            if m:
                group = m.groupdict()
                active_dict = install_active_dict.setdefault('active_packages', {})
                active_dict.update({'XR': group.get('xr')})
                active_dict.update({'All': group.get('all')})

            m = p4.match(line)
            if m:
                group = m.groupdict()
                install_active_dict.update({'label': group['label']})

            m = p5.match(line)
            if m:
                group = m.groupdict()
                install_active_dict.update({'software_hash': group['sh']})

            m = p6.match(line)
            if m:
                group = m.groupdict()
                active_dict = install_active_dict.setdefault('optional_packages', {})
                active_dict.update({group['optional_packages']: group['version']})

            m = p7.match(line)
            if m:
                group = m.groupdict()
                active_dict = install_active_dict.setdefault('mandatory_packages', {})
                active_dict.update({group['mandatory_packages']: group['version']})

            m = p8.match(line)
            if m:
                group = m.groupdict()
                active_dict = install_active_dict.setdefault('active_fixes', {})
                active_dict.update({'count': group['count']})

            m = p9.match(line)
            if m:
                group = m.groupdict()
                active_dict = install_active_dict.setdefault('active_fixes', {})
                active_dict.update({group['bug_id']: group['package_name']})

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
        Optional('label'): str,
        Optional('software_hash'): str,
        Optional('optional_packages'): {str: str},
        Optional('mandatory_packages'): {str: str},
        Optional('committed_fixes'): {str: str},
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
        sdr = False
        previous_line_sdr = False
        previous_line_committed_packages = False
        previous_line_active_packages = False

        #SDRs:
        p1 = re.compile(r'\s*SDRs:*$')

        # disk0:xrvr-full-x-6.2.1.23I
        # disk0:asr9k-mini-px-6.1.21.15I
        # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
        p2 = re.compile(r'\s*Committed +Packages:'
                        ' *(?P<num_committed_packages>[0-9]+)?$')
        
        # disk0:xrvr-full-x-6.2.1.23I
        # disk0:asr9k-mini-px-6.1.21.15I
        # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
        p3 = re.compile(r'\s*Active +Packages:'
                        ' *(?P<num_active_packages>[0-9]+)?$')
        
        # Committed Packages: XR: 201    All: 1532
        p4 = re.compile(r'^Committed +Packages: +XR: +(?P<xr>[\d]+)\s+All: +(?P<all>[\d]+)$')

        # Label:              7.10.2-meta_7102_fcs_01_25_2024
        p5 = re.compile(r'^Label:\s+(?P<label>[\w\.\-]+)$')

        # Software Hash:      454175afbe3ad586c3b39a79db238b53844fe794723ea99fa00ac1acd5442359
        p6 = re.compile(r'^Software +Hash:\s+(?P<sh>[\w]+)$')

        # Optional Packages                                                        Version
        # ---------------------------------------------------- ---------------------------
        # xr-8000-netflow                                                   7.10.2v1.0.0-1
        # xr-bgp                                                            7.10.2v1.0.0-1
        p7 = re.compile(r'^(?P<optionalpackages>[\w\-]+)\s+(?P<version>[\w\.\-]+)$')

        # Mandatory Packages with Committed Bugfixes                               Version
        # xr-8000-core                                                      7.10.2v1.0.1-1
        # xr-8000-cpa-npu                                                   7.10.2v1.0.2-1
        p8 = re.compile(r'^(?P<mandatory_packages>[\w\-]+)\s+(?P<version>[\w\.\-]+)$')

        # Committed Fixes (count: 6):
        p9 = re.compile(r"Committed Fixes \(count: (?P<count>\d+)\):")

        # CSCwh02785: xr-fib
        # CSCwh80170: xr-8000-cpa-npu
        # CSCwi62344: xr-8000-core, xr-8000-cpa-npu, xr-8000-leabaofa, xr-networkboot
        p10 = re.compile(r'^\s*(?P<bug_id>CSC\w+): (?P<package_name>[\w\-\,\ ]+)$')

        for line in out.splitlines():
            line = line.rstrip()
            if line.startswith('-'):
                continue

            #SDRs:
            m = p1.match(line)
            if m:
                previous_line_sdr = True
                sdr = True
                continue

            if previous_line_sdr:
                previous_line_sdr = False
                install_commit_dict.setdefault('sdr', []).append(str(line).strip())
                continue

            if sdr:

                # disk0:xrvr-full-x-6.2.1.23I
                # disk0:asr9k-mini-px-6.1.21.15I
                # xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
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
                m = p3.match(line)
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
            else :

                # Committed Packages: XR: 201    All: 1532
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    commit_dict = install_commit_dict.setdefault('committed_packages', {})
                    commit_dict.update({'XR': group['xr']})
                    commit_dict.update({'All': group['all']})

                # Label:              7.10.2-meta_7102_fcs_01_25_2024
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    install_commit_dict.update({'label': group['label']})
    
                # Software Hash:      454175afbe3ad586c3b39a79db238b53844fe794723ea99fa00ac1acd5442359
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    install_commit_dict.update({'software_hash': group['sh']})
                
                # Optional Packages                                                        Version
                # ---------------------------------------------------- ---------------------------
                # xr-8000-netflow                                                   7.10.2v1.0.0-1
                # xr-bgp                                                            7.10.2v1.0.0-1
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    commit_dict = install_commit_dict.setdefault('optional_packages', {})
                    commit_dict.update({group['optionalpackages']: group['version']})

                # Mandatory Packages with Committed Bugfixes                               Version
                # xr-8000-core                                                      7.10.2v1.0.1-1
                # xr-8000-cpa-npu                                                   7.10.2v1.0.2-1
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    commit_dict = install_commit_dict.setdefault('mandatory_packages', {})
                    commit_dict.update({group['mandatory_packages']: group['version']})   
                
                # Committed Fixes (count: 6):
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    commit_dict = install_commit_dict.setdefault('committed_fixes', {})
                    commit_dict.update({'count': group['count']})

                # CSCwh02785: xr-fib
                # CSCwh80170: xr-8000-cpa-npu
                # CSCwi62344: xr-8000-core, xr-8000-cpa-npu, xr-8000-leabaofa, xr-networkboot
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    commit_dict = install_commit_dict.setdefault('committed_fixes', {})
                    commit_dict.update({group['bug_id']: group['package_name']})

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



class ShowDiagDetailsSchema(MetaParser):

    schema = {
        'item': {
            Any(description="Placeholder for item names"): {
                'description': str,
                Optional('pid'): str,
                Optional('serial_number'): str,
                Optional('chassis_serial_number'): str,
                Optional('udi_description'): str,
                Optional('controller_family'): str,
                Optional('controller_type'): str,
                Optional('vid'): str,
                Optional('udi_description'): str,
                Optional('chassis_serial_number'): str,
                Optional('top_assy_part_number'): str,
                Optional('top_assy_revision'): str,
                Optional('pcb_serial_number'): str,
                Optional('pca_number'): str,
                Optional('pca_revision'): str,
                Optional('clei_code'): str,
                Optional('eci_number'): str,
                Optional('deviation_number'): {
                    Any(): str
                },
                Optional('manufacturing_number'): str,
                Optional('calibration_data'): str,
                Optional('chassis_mac_address'): str,
                Optional('mac_address_block_size'): str,
                Optional('hardware_revision'): str,
                Optional('device_value_1'): str,
                Optional('power_supply_type'): str,
                Optional('power_consumption'): str,
                Optional('asset_id'): str,
                Optional('asset_alias'): str,
                Optional('eci_number'): str,
                Optional('idprom_format_revision'): str,
                Optional('main_board_type'): str,
                Optional('sn'): str,
                Optional('hwrev_udi_vid'): str,
                Optional('top_assy_number'): str,
                Optional('chip_hwrev'): str,
                Optional('new_deviation_num'): int,
                Optional('clei'): str,
                Optional('board_state'): str,
                Optional('pld'): {
                    Optional('motherboard'): str,
                    Optional('processor_version'): str,
                    Optional('rev'): str,
                    Optional('power'): str,
                },
                Optional('monltb'): str,
                Optional('rommon_version'): str,
                Optional('cpu0'): str,
                Optional('base_mac_address'): str,
                Optional('capabilities'): str,
                Optional('envmon_information'): str,
                Optional('rma_test_history'): str,
                Optional('rma_number'): str,
                Optional('rma_history'): str,
                Optional('device_values'): str,
                Optional(Any(description='Placeholder for blocks')): {
                    Optional('block_signature'): str,
                    Optional('block_version'): int,
                    Optional('block_length'): int,
                    Optional('block_checksum'): str,
                    Optional('eeprom_size'): int,
                    Optional('block_count'): int,
                    Optional('fru_major_type'): str,
                    Optional('fru_minor_type'): str,
                    Optional('oem_string'): str,
                    Optional('pid'): str,
                    Optional('serial_number'): str,
                    Optional('part_number'): str,
                    Optional('part_revision'): str,
                    Optional('mfg_deviation'): str,
                    Optional('hw_version'): str,
                    Optional('mfg_bits'): int,
                    Optional('engineer_use'): int,
                    Optional('snmpoid'): str,
                    Optional('power_consumption'): str,
                    Optional('rma_code'): str,
                    Optional('clei_code'): str,
                    Optional('vid'): str,
                    Optional('feature_bits'): str,
                    Optional('hw_change_bit'): str,
                    Optional('card_index'): int,
                    Optional('mac_address'): str,
                    Optional('num_of_macs'): int,
                    Optional('num_eobc_links'): int,
                    Optional('num_epld'): int,
                    Optional('epld_a'): str,
                    Optional('epld_b'): str,
                    Optional('port_type_num'): str,
                    Optional('sram_size'): int,
                    Optional('sensor'): {
                        Any(): str
                    },
                    Optional('max_connector_power'): str,
                    Optional('cooling_requirement'): int,
                    Optional('ambient_temperature'): int,
                    Optional('no_of_valid_sensor'): int,
                    Optional('fabswitch0'): str,
                    Optional('fabswitch1'): str,
                    Optional('fabarbiter'): str,
                    Optional('fia'): str,
                    Optional('intctrl'): str,
                    Optional('clkctrl'): str,
                    Optional('10gpuntfpga'): str,
                    Optional('hd'): str,
                    Optional('usb0'): str,
                    Optional('usb1'): str,
                    Optional('cpuctrl'): str,
                    Optional('ydti'): str,
                    Optional('liu'): str,
                    Optional('mlanswitch'): str,
                    Optional('eobcswitch'): str,
                    Optional('eobcswitch'): str,
                    Optional('hostinftctrl'): str,
                    Optional('phy'): str,
                    Optional('offload10ge'): str,
                    Optional('e10gedualmac0'): str,
                    Optional('e10gedualmac1'): str,
                    Optional('egedualmac0'): str,
                    Optional('egedualmac1'): str,
                    Optional('cbc_active_partition'): str,
                    Optional('cbc_inactive_partition'): str,
                    Optional('np0'): str,
                    Optional('np1'): str,
                    Optional('np2'): str,
                    Optional('np3'): str,
                    Optional('np4'): str,
                    Optional('np5'): str,
                    Optional('np6'): str,
                    Optional('np7'): str,
                    Optional('fia0'): str,
                    Optional('fia1'): str,
                    Optional('fia2'): str,
                    Optional('fia3'): str,
                    Optional('fia4'): str,
                    Optional('fia5'): str,
                    Optional('xbar'): str,
                    Optional('arbiter'): str,
                    Optional('portctrl'): str,
                    Optional('phyctrl'): str,
                    Optional('usb'): str,
                    Optional(Any(description='Placeholder for PHY')): {
                        Optional('hwrev'): str,
                        Optional('fwrev'): str,
                        Optional('swrev'): str
                    }
                }
            }
        }
    }


class ShowDiagDetails(ShowDiagDetailsSchema):

    cli_command = "show diag details"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Rack 0-Chassis IDPROM - Cisco 8000 Series 32x400G QSFPDD 1RU Fixed System w/HBM
        # 0/0-DB-IDPROM - 400G Modular Linecard, Service Edge Optimized
        p0 = re.compile(r'(?P<item>.+?)[\s-]IDPROM\s+\-\s+(?P<description>.+?)\s*$')

        # Controller Family          : 0045
        p1 = re.compile(r'^Controller Family\s+:\s+(?P<controller_family>\w+)$')

        # Controller Type            : 06b1
        p2 = re.compile(r'^Controller Type\s+:\s+(?P<controller_type>\w+)$')

        # PID                        : 8201-32FH
        p3 = re.compile(r'^(PID|Product ID)\s+:\s+(?P<pid>[\w-]+)$')

        # Version Identifier         : V03
        p4 = re.compile(r'^(VID|Version Identifier)\s+:\s+(?P<version_identifier>.+?)$')

        # UDI Description            : Cisco 8000 Series 32x400G QSFPDD 1RU Fixed System w/HBM
        p5 = re.compile(r'^UDI Description\s+:\s+(?P<udi_description>.+?)$')

        # Chassis Serial Number      : FLM263401XF
        p6 = re.compile(r'^Chassis Serial\s+Number\s+:\s+(?P<serial_number>\w+)$')

        # Top Assy. Part Number      : 68-7325-05
        p7 = re.compile(r'^Top Assy. Part Number\s+:\s+(?P<part_number>[\w-]+)$')

        # Top Assy. Revision         : B0
        p8 = re.compile(r'^Top Assy. Revision\s+:\s+(?P<revision>[\w-]+)$')

        # PCB Serial Number          : FLM263303GJ
        p9 = re.compile(r'^PCB Serial Number\s+:\s+(?P<serial_number>.+?)$')

        # PCA Number                 : 73-20364-02
        p10 = re.compile(r'^PCA Number\s+:\s+(?P<serial_number>.+?)$')

        # PCA Revision               : E0
        p11 = re.compile(r'^PCA Revision\s+:\s+(?P<serial_number>.+?)$')

        # CLEI Code                  : CMM6210ARC
        p12 = re.compile(r'^CLEI Code\s+:\s+(?P<clei_code>\w+)$')

        # ECI Number                 : 477690
        p13 = re.compile(r'^ECI Number\s+:\s+(?P<eci_num>\w+)$')

        # Deviation Number # 1       : 0
        p14 = re.compile(r'^Deviation Number # (?P<num>\d)\s+:\s+(?P<deviation_num>\w+)$')

        # Manufacturing Test Data    : 00 00 00 00 00 00 00 00
        p15 = re.compile(r'^Manufacturing Test Data\s+:\s+(?P<manufacturing_num>[\w\s]+)$')

        # Calibration Data           : 00000000
        p16 = re.compile(r'^Calibration Data\s+:\s+(?P<calibration_data>\d+)$')

        # Chassis MAC Address        : 3c26.e4b6.8c00
        p17 = re.compile(r'^Chassis MAC Address\s+:\s+(?P<chassis_mac_addr>[\w.]+)$')

        # MAC Addr. Block Size       : 512
        p18 = re.compile(r'^MAC Addr. Block Size\s+:\s+(?P<mac_addr>\d+)$')

        # Hardware Revision          : 1.0
        p19 = re.compile(r'^Hardware Revision\s+:\s+(?P<hardware_revision>[\w.]+)$')

        # Device values # 1          : 42 e0 00 08 28 00 00 00
        p20 = re.compile(r'^Device values # 1\s+:\s+(?P<device_value>[\w\s]+)$')

        # Power Supply Type          : AC
        p21 = re.compile(r'^Power Supply Type\s+:\s+(?P<power_supply>\w+)$')

        # Power Consumption          : 2000 Watts (Maximum)
        # Power Consump   : 0 W
        p22 = re.compile(r'^Power (Consumption|Consump)\s+:\s+(?P<power_consump>.+?)$')

        # Asset ID                 :
        p23 = re.compile(r'^Asset ID\s+:\s+(?P<asset_id>.+?)$')

        # Asset Alias              :
        p24 = re.compile(r'^Asset Alias\s+:\s+(?P<asset_alias>.+?)$')

        # ECI Number               :
        p25 = re.compile(r'^ECI Number\s+:\s+(?P<eci_number>.+?)$')

        # IDPROM Format Revision   : A
        p26 = re.compile(r'^IDPROM Format Revision\s+:\s+(?P<idprom_format_revision>\w+)$')

        # Common Blocks:
        p27 = re.compile(r'^Common Blocks:$')

        # Block Signature : 0xabab
        p28 = re.compile('^Block Signature\s+:\s+(?P<block_signature>\w+)$')

        # Block Version   : 3
        p29 = re.compile('^Block Version\s+:\s+(?P<block_version>\d+)$')

        # Block Length    : 160
        p30 = re.compile('^Block Length\s+:\s+(?P<block_length>\d+)$')

        # Block Checksum  : 0x1b10
        p31 = re.compile('^Block Checksum\s+:\s+(?P<block_checksum>.+?)$')

        # EEPROM Size     : 65535
        p32 = re.compile('^EEPROM Size\s+:\s+(?P<eeprom_size>\d+)$')

        # Block Count     : 4
        p33 = re.compile('^Block Count\s+:\s+(?P<block_count>\d+)$')

        # FRU Major Type  : 0x6003
        p34 = re.compile('^FRU Major Type\s+:\s+(?P<fru_major_type>\w+)$')

        # FRU Minor Type  : 0x0
        p35 = re.compile('^FRU Minor Type\s+:\s+(?P<fru_minor_type>\w+)$')

        # OEM String      : Cisco Systems, Inc.
        p36 = re.compile('^OEM String\s+:\s+(?P<oem_string>.+?)$')

        # Serial Number   : JAE24480QCT
        p37 = re.compile('^Serial Number\s+:\s+(?P<serial_number>\w+)$')

        # Part Number     : 73-102072-04
        p38 = re.compile('^Part Number\s+:\s+(?P<part_number>.+?)$')

        # Part Revision   : 05
        p39 = re.compile('^Part Revision\s+:\s+(?P<part_revision>\w+)$')

        # Mfg Deviation   : 000000000
        p40 = re.compile('^Mfg Deviation\s+:\s+(?P<mfg_deviation>\w+)$')

        # H/W Version     : 0.300
        p41 = re.compile('^H/W Version\s+:\s+(?P<hw_version>.+?)$')

        # Mfg Bits        : 0
        p42 = re.compile('^Mfg Bits\s+:\s+(?P<mfg_bits>\w+)$')

        # Engineer Use    : 0
        p43 = re.compile('^Engineer Use\s+:\s+(?P<engineer_use>\w+)$')

        # snmpOID         : 9.12.3.1.9.2.708.0
        p44 = re.compile('^snmpOID\s+:\s+(?P<snmpoid>.+?)$')

        # RMA Code        : 0-0-0-0
        p45 = re.compile('^RMA Code\s+:\s+(?P<rma_code>.+?)$')

        # Card Specific Block:
        p46 = re.compile('^Card Specific Block:$')

        # Feature Bits    : 0x0
        p47 = re.compile(r'^Feature Bits\s+:\s+(?P<feature_bits>\w+)$')

        # HW Changes Bits : 0x77ce
        p48 = re.compile(r'^HW Changes Bits\s+:\s+(?P<hw_change_bit>\w+)$')

        # Card Index      : 27061
        p49 = re.compile(r'^Card Index\s+:\s+(?P<card_index>\d+)$')

        # MAC Addresses   : 90-77-ee-75-70-f2
        p50 = re.compile(r'^MAC Addresses\s+:\s+(?P<mac_address>.+?)$')

        # Number of MACs  : 18
        p51 = re.compile(r'^Number of MACs\s+:\s+(?P<num_macs>\d+)$')

        # Number of EOBC links : 2
        p52 = re.compile(r'^Number of EOBC links\s+:\s+(?P<num_eobc_links>\d+)$')

        # Number of EPLD  : 2
        p53 = re.compile(r'^Number of EPLD\s+:\s+(?P<num_epld>\d+)$')

        # EPLD A          : 0x0
        p54 = re.compile(r'^EPLD A\s+:\s+(?P<epld_a>.+?)$')

        # EPLD B          : 0x0
        p55 = re.compile(r'^EPLD B\s+:\s+(?P<epld_b>.+?)$')

        # Port Type-Num   : 0-0
        p56 = re.compile(r'^Port Type-Num\s+:\s+(?P<port_type_num>.+?)$')

        # SRAM size       : 0
        p57 = re.compile(r'^SRAM size\s+:\s+(?P<sram_size>\d+)$')

        # Sensor #1       : 115,105
        p58 = re.compile(r'^Sensor #(?P<num>\d)\s+:\s+(?P<sensor>.+?)$')

        # Max Connector Power: 1800 W
        p59 = re.compile(r'^Max Connector Power:\s+(?P<max_connector_power>.+?)$')

        # Cooling Requirement: 75
        p60 = re.compile(r'^Cooling Requirement:\s+(?P<cooling_req>\d+)$')

        # Ambient Temperature: 55
        p61 = re.compile(r'^Ambient Temperature:\s+(?P<ambient_temp>\d+)$')

        # Temperature Sensor Block:
        p62 = re.compile(r'^Temperature Sensor Block:$')

        # Number of Valid Sensors : 0
        p63 = re.compile(r'^Number of Valid Sensors\s+:\s+(?P<valid_sensor>\d+)$')

        # Hardware Configuration Block:
        p64 = re.compile(r'^Hardware Configuration Block:$')

        # NODE module 0/RSP0/CPU0  ASR9K Route Switch Processor with 440G/slot Fabric and 12GB
        p65 = re.compile(r'^NODE module (?P<item>.+?)\s+(?P<description>.+)$')

        # MAIN:  board type 0x100307
        p66 = re.compile(r'^MAIN:\s+board type (?P<board_type>.+?)$')

        # S/N:   FOC1910NMC0
        p67 = re.compile(r'^S\/N:\s+(?P<sn>.+)$')

        # Top Assy. Number:   68-3661-04
        p68 = re.compile(r'^Top Assy. Number:\s+(?P<top_assy_num>.+)$')

        # HwRev (UDI_VID):   V06
        p69 = re.compile(r'^HwRev \(UDI_VID\):\s+(?P<hwrev>.+)$')

        # Chip HwRev: V1.0
        p70 = re.compile(r'^Chip HwRev:\s+(?P<chip_hwrev>.+)$')

        # New Deviation Number: 0
        p71 = re.compile(r'^New Deviation Number:\s+(?P<new_deviation_num>\d+)$')

        # CLEI:  IPUCBB4BTD
        p72 = re.compile(r'^CLEI:\s+(?P<clei>.+)$')

        # Board State : IOS XR RUN
        p73 = re.compile(r'^Board State\s+:\s+(?P<board_state>.+)$')

        # PLD:    Motherboard: N/A, Processor version: 0x0 (rev: 2.174), Power: N/A
        p74 = re.compile(r'^PLD:\s+Motherboard:\s+(?P<motherboard>[\w\/]+),'
                           r'\s+Processor version:\s+(?P<processor_version>\w+)\s+'
                           r'\(rev:\s+(?P<rev>[\d.]+)\),\s+Power:\s+(?P<power>[\w\/]+)$')

        # MONLIB:
        p75 = re.compile(r'^MONLTB:(?P<monltb>.+)$')

        # ROMMON: Version 0.76 [ASR9K x86 ROMMON],
        p76 = re.compile(r'^ROMMON:\s+Version\s+(?P<rommon_version>.+)$')

        # CPU0: Intel 686 F6M14S4
        p77 = re.compile(r'^CPU0:\s+(?P<cpu>.+)$')

        # Board FPGA/CPLD/ASIC Hardware Revision:
        p78 = re.compile(r'^Board FPGA/CPLD/ASIC Hardware Revision:$')

        # FabSwitch0  : V1.5
        p79 = re.compile(r'^FabSwitch0\s+:\s+(?P<fabswitch0>.+)$')

        # FabSwitch1  : V1.5
        p80 = re.compile(r'^FabSwitch1\s+:\s+(?P<fabswitch1>.+)$')

        # FabArbiter  : V0.1
        p81 = re.compile(r'^FabArbiter\s+:\s+(?P<fabarbiter>.+)$')

        # FIA  : V0.2
        p82 = re.compile(r'^FIA\s+:\s+(?P<fia>.+)$')

        # IntCtrl  : V0.11
        p83 = re.compile(r'^IntCtrl\s+:\s+(?P<intctrl>.+)$')

        # ClkCtrl  : V2.10
        p84 = re.compile(r'^ClkCtrl\s+:\s+(?P<clkctrl>.+)$')

        # 10GPuntFPGA  : V1.10
        p85 = re.compile(r'^10GPuntFPGA\s+:\s+(?P<puntfpga>.+)$')

        # HD  : V2.16
        p86 = re.compile(r'^HD\s+:\s+(?P<hd>.+)$')

        # USB0  : V2.16
        p87 = re.compile(r'^USB0\s+:\s+(?P<usb0>.+)$')

        # USB1  : V0.0
        p88 = re.compile(r'^USB1\s+:\s+(?P<usb1>.+)$')

        # CpuCtrl  : V0.11
        p89 = re.compile(r'^CpuCtrl\s+:\s+(?P<cpuctrl>.+)$')

        # YDTI  : V4.9
        p90 = re.compile(r'^YDTI\s+:\s+(?P<ydti>.+)$')

        # LIU  : V0.0
        p91 = re.compile(r'^LIU\s+:\s+(?P<liu>.+)$')

        # MLANSwitch  : V0.0
        p92 = re.compile(r'^MLANSwitch\s+:\s+(?P<mlanswitch>.+)$')

        # EOBCSwitch  : V0.0
        p93 = re.compile(r'^EOBCSwitch\s+:\s+(?P<eobcswitch>.+)$')

        # HostInftCtrl  : V0.0
        p94 = re.compile(r'^HostInftCtrl\s+:\s+(?P<hostinftctrl>.+)$')

        # PHY  : V0.0
        p95 = re.compile(r'^PHY\s+:\s+(?P<phy>.+)$')

        # Offload10GE  : V0.0
        p96 = re.compile(r'^Offload10GE\s+:\s+(?P<offload10ge>.+)$')

        # E10GEDualMAC0  : V0.0
        p97 = re.compile(r'^E10GEDualMAC0\s+:\s+(?P<e10gedualmac0>.+)$')

        # E10GEDualMAC1  : V0.0
        p98 = re.compile(r'^E10GEDualMAC1\s+:\s+(?P<e10gedualmac1>.+)$')

        # EGEDualMAC0  : V0.0
        p99 = re.compile(r'^EGEDualMAC0\s+:\s+(?P<egedualmac0>.+)$')

        # EGEDualMAC1  : V0.0
        p100 = re.compile(r'^EGEDualMAC1\s+:\s+(?P<egedualmac1>.+)$')

        # CBC (active partition)  : v16.117
        p101 = re.compile(r'^CBC \(active partition\)\s+:\s+(?P<cbc_active_partition>.+)$')

        # CBC (inactive partition)  : v16.116
        p102 = re.compile(r'^CBC \(inactive partition\)\s+:\s+(?P<cbc_inactive_partition>.+)$')

        # NP0  : V4.194
        p103 = re.compile(r'^NP(?P<np>\d+)\s+:\s+(?P<np0>.+)$')

        # FIA0  : V0.2
        p104 = re.compile(r'^FIA(?P<fia>\d+)\s+:\s+(?P<fia0>.+)$')

        # X-Bar  : V1.5
        p105 = re.compile(r'^X-Bar\s+:\s+(?P<xbar>.+)$')

        # Arbiter  : V0.2
        p106 = re.compile(r'^Arbiter\s+:\s+(?P<arbiter>.+)$')

        # PortCtrl  : V1.0
        p107 = re.compile(r'^PortCtrl\s+:\s+(?P<portctrl>.+)$')

        # PHYCtrl  : V1.1
        p108 = re.compile(r'^PHYCtrl\s+:\s+(?P<phyctrl>.+)$')

        # USB  : V17.0
        p109 = re.compile(r'^USB\s+:\s+(?P<usb>.+)$')

        # PHY0  : V0.4(HwRev)	V0.0(FwRev)	V8.0(SwRev)
        p110 = re.compile(r'^(?P<phy>\w+)\s+:\s+(?P<hwrev>.+)\(HwRev\)\s+(?P<fwrev>.+)\(FwRev\)\s+(?P<swrev>.+)\(SwRev\)$')

        # Base MAC Address         : 00a7.428b.f4b0
        p111 = re.compile(r'^Base MAC Address\s+:\s+(?P<base_mac_address>.+)$')

        # Capabilities             : 00
        p112 = re.compile(r'^Capabilities\s+:\s+(?P<capabilities>.+)$')

        # ENVMON Information       : 2 86 0 0 0 0 0 0
        # 	                         0 0 0 0 0 0 0 0
        # 	                         0 0 0 0 0 0 0 0
        # 	                         0 0 0 0 0 0 0 0
        p113 = re.compile(r'ENVMON Information\s+:\s+(?P<envmon_information>.+)')

        # 0 0 0 0 0 0 0 0
        p113_1 = re.compile(r'^(?P<env_info>[\d\s]{15})$')

        # RMA Test History         : 00
        p114 = re.compile(r'^RMA Test History\s+:\s+(?P<rma_test_history>.+)$')

        # RMA Number               : 0-0-0-0
        p115 = re.compile(r'^RMA Number\s:\s+(?P<rma_number>.+)$')

        # RMA History              : 00
        p116 = re.compile(r'^RMA History\s:\s(?P<rma_history>.+)$')

        # Device values            : 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0
        p117 = re.compile(r'^Device values\s+:\s+(?P<device_values>.+)$')

        pointer_block = {}

        for line in output.splitlines():
            line = line.strip()

            # Rack 0-Chassis IDPROM - Cisco 8000 Series 32x400G QSFPDD 1RU Fixed System w/HBM
            m = p0.match(line) or p65.match(line)
            if m:
                match_dict = m.groupdict()
                item_dict = ret_dict.setdefault('item', {}).setdefault(match_dict['item'], {})
                item_dict['description'] = match_dict['description']
                pointer_block = item_dict
                continue

            # Controller Family          : 0045
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['controller_family'] = match_dict['controller_family']
                continue

            # Controller Type            : 06b1
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['controller_type'] = match_dict['controller_type']
                continue

            # PID                        : 8201-32FH
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pid'] = match_dict['pid']
                continue

            # Version Identifier         : V03
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['vid'] = match_dict['version_identifier']
                continue

            # UDI Description            : Cisco 8000 Series 32x400G QSFPDD 1RU Fixed System w/HBM
            m = p5.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['udi_description'] = match_dict['udi_description']
                continue

            # Chassis Serial Number      : FLM263401XF
            m = p6.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['chassis_serial_number'] = match_dict['serial_number']
                continue

            # Top Assy. Part Number      : 68-7325-05
            m = p7.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['top_assy_part_number'] = match_dict['part_number']
                continue

            # Top Assy. Revision         : B0
            m = p8.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['top_assy_revision'] = match_dict['revision']
                continue

            # PCB Serial Number          : FLM263303GJ
            m = p9.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pcb_serial_number'] = match_dict['serial_number']
                continue

            # PCA Number                 : 73-20364-02
            m = p10.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pca_number'] = match_dict['serial_number']
                continue

            # PCA Revision               : E0
            m = p11.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pca_revision'] = match_dict['serial_number']
                continue

            # CLEI Code                  : CMM6210ARC
            m = p12.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['clei_code'] = match_dict['clei_code']
                continue

            # ECI Number                 : 477690
            m = p13.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['eci_number'] = match_dict['eci_num']
                continue

            # Deviation Number # 1       : 0
            m = p14.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block.setdefault('deviation_number', {}).setdefault(
                    match_dict['num'], match_dict['deviation_num'])
                continue

            # Manufacturing Test Data    : 00 00 00 00 00 00 00 00
            m = p15.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['manufacturing_number'] = match_dict['manufacturing_num']
                continue

            # Calibration Data           : 00000000
            m = p16.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['calibration_data'] = match_dict['calibration_data']
                continue

            # Chassis MAC Address        : 3c26.e4b6.8c00
            m = p17.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['chassis_mac_address'] = match_dict['chassis_mac_addr']
                continue

            # MAC Addr. Block Size       : 512
            m = p18.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['mac_address_block_size'] = match_dict['mac_addr']
                continue

            # Hardware Revision          : 1.0
            m = p19.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hardware_revision'] = match_dict['hardware_revision']
                continue

            # Device values # 1          : 42 e0 00 08 28 00 00 00
            m = p20.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['device_value_1'] = match_dict['device_value']
                continue

            # Power Supply Type          : AC
            m = p21.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['power_supply_type'] = match_dict['power_supply']
                continue

            # Power Consumption          : 2000 Watts (Maximum)
            m = p22.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['power_consumption'] = match_dict['power_consump']
                continue

            # Asset ID                 :
            m = p23.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['asset_id'] = match_dict['asset_id']
                continue

            # Asset Alias              :
            m = p24.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['asset_alias'] = match_dict['asset_alias']
                continue

            # ECI Number               :
            m = p25.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['eci_number'] = match_dict['eci_num']
                continue

            # IDPROM Format Revision   : A
            m = p26.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['idprom_format_revision'] = match_dict['idprom_format_revision']
                continue

            # Common Blocks:
            m = p27.match(line)
            if m:
                common_blocks = pointer_block.setdefault('common_blocks', {})
                pointer_block = common_blocks
                continue

            # Block Signature : 0xabab
            m = p28.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['block_signature'] = match_dict['block_signature']
                continue

            # Block Version   : 3
            m = p29.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['block_version'] = int(match_dict['block_version'])
                continue

            # Block Length    : 160
            m = p30.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['block_length'] = int(match_dict['block_length'])
                continue

            # Block Checksum  : 0x1b10
            m = p31.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['block_checksum'] = match_dict['block_checksum']
                continue

            # EEPROM Size     : 65535
            m = p32.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['eeprom_size'] = int(match_dict['eeprom_size'])
                continue

            # Block Count     : 4
            m = p33.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['block_count'] = int(match_dict['block_count'])
                continue

            # FRU Major Type  : 0x6003
            m = p34.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fru_major_type'] = match_dict['fru_major_type']
                continue

            # FRU Minor Type  : 0x0
            m = p35.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fru_minor_type'] = match_dict['fru_minor_type']
                continue

            # OEM String      : Cisco Systems, Inc.
            m = p36.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['oem_string'] = match_dict['oem_string']
                continue

            # Serial Number   : JAE24480QCT
            m = p37.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['serial_number'] = match_dict['serial_number']
                continue

            # Part Number     : 73-102072-04
            m = p38.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['part_number'] = match_dict['part_number']
                continue

            # Part Revision   : 05
            m = p39.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['part_revision'] = match_dict['part_revision']
                continue

            # Mfg Deviation   : 000000000
            m = p40.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['mfg_deviation'] = match_dict['mfg_deviation']
                continue

            # H/W Version     : 0.300
            m = p41.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hw_version'] = match_dict['hw_version']
                continue

            # Mfg Bits        : 0
            m = p42.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['mfg_bits'] = int(match_dict['mfg_bits'])
                continue

            # Engineer Use    : 0
            m = p43.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['engineer_use'] = int(match_dict['engineer_use'])
                continue

            # snmpOID         : 9.12.3.1.9.2.708.0
            m = p44.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['snmpoid'] = match_dict['snmpoid']
                continue

            # RMA Code        : 0-0-0-0
            m = p45.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['rma_code'] = match_dict['rma_code']
                continue

            # Card Specific Block:
            m = p46.match(line)
            if m:
                card_specific_block = item_dict.setdefault('card_specific_block', {})
                pointer_block = card_specific_block
                continue

            # Feature Bits    : 0x0
            m = p47.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['feature_bits'] = match_dict['feature_bits']
                continue

            # HW Changes Bits : 0x77ce
            m = p48.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hw_change_bit'] = match_dict['hw_change_bit']
                continue

            # Card Index      : 27061
            m = p49.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['card_index'] = int(match_dict['card_index'])
                continue

            # MAC Addresses   : 90-77-ee-75-70-f2
            m = p50.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['mac_address'] = match_dict['mac_address']
                continue

            # Number of MACs  : 18
            m = p51.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['num_of_macs'] = int(match_dict['num_macs'])
                continue

            # Number of EOBC links : 2
            m = p52.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['num_eobc_links'] = int(match_dict['num_eobc_links'])
                continue

            # Number of EPLD  : 2
            m = p53.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['num_epld'] = int(match_dict['num_epld'])
                continue

            # EPLD A          : 0x0
            m = p54.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['epld_a'] = match_dict['epld_a']
                continue

            # EPLD B          : 0x0
            m = p55.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['epld_b'] = match_dict['epld_b']
                continue

            # Port Type-Num   : 0-0
            m = p56.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['port_type_num'] = match_dict['port_type_num']
                continue

            # SRAM size       : 0
            m = p57.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['sram_size'] = int(match_dict['sram_size'])
                continue

            # Sensor #1       : 115,105
            m = p58.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block.setdefault('sensor', {}).setdefault(match_dict['num'], match_dict['sensor'])
                continue

            # Max Connector Power: 1800 W
            m = p59.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['max_connector_power'] = match_dict['max_connector_power']
                continue

            # Cooling Requirement: 75
            m = p60.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cooling_requirement'] = int(match_dict['cooling_req'])
                continue

            # Ambient Temperature: 55
            m = p61.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['ambient_temperature'] = int(match_dict['ambient_temp'])
                continue

            # Temperature Sensor Block:
            m = p62.match(line)
            if m:
                temperature_sensor_block = item_dict.setdefault('temperature_sensor_block', {})
                pointer_block = temperature_sensor_block
                continue

            # Number of Valid Sensors : 0
            m = p63.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['no_of_valid_sensor'] = int(match_dict['valid_sensor'])
                continue

            # Hardware Configuration Block:
            m = p64.match(line)
            if m:
                hardware_configuration_block = item_dict.setdefault('hardware_configuration_block', {})
                pointer_block = hardware_configuration_block
                continue

            # MAIN:  board type 0x100307
            m = p66.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['main_board_type'] = match_dict['board_type']

            # S/N:   FOC1910NMC0
            m = p67.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['sn'] = match_dict['sn']

            # Top Assy. Number:   68-3661-04
            m = p68.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['top_assy_number'] = match_dict['top_assy_num']

            # HwRev (UDI_VID):   V06
            m = p69.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hwrev_udi_vid'] = match_dict['hwrev']

            # Chip HwRev: V1.0
            m = p70.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['chip_hwrev'] = match_dict['chip_hwrev']

            # New Deviation Number: 0
            m = p71.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['new_deviation_num'] = int(match_dict['new_deviation_num'])

            # CLEI:  IPUCBB4BTD
            m = p72.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['clei'] = match_dict['clei']

            # Board State : IOS XR RUN
            m = p73.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['board_state'] = match_dict['board_state']

            # PLD:    Motherboard: N/A, Processor version: 0x0 (rev: 2.174), Power: N/A
            m = p74.match(line)
            if m:
                match_dict = m.groupdict()
                pld = pointer_block.setdefault('pld', {})
                pld['motherboard'] = match_dict['motherboard']
                pld['processor_version'] = match_dict['processor_version']
                pld['rev'] = match_dict['rev']
                pld['power'] =match_dict['power']

            # MONLIB:
            m = p75.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['monltb'] = match_dict['monltb']

            # ROMMON: Version 0.76 [ASR9K x86 ROMMON],
            m = p76.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['rommon_version'] = match_dict['rommon_version']

            # CPU0: Intel 686 F6M14S4
            m = p77.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cpu0'] = match_dict['cpu']

            # Board FPGA/CPLD/ASIC Hardware Revision:
            m = p78.match(line)
            if m:
                board_hw_revision = item_dict.setdefault('FPGA/CPLD/ASIC', {})
                pointer_block = board_hw_revision

            # FabSwitch0  : V1.5
            m = p79.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fabswitch0'] = match_dict['fabswitch0']

            # FabSwitch1  : V1.5
            m = p80.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fabswitch1'] = match_dict['fabswitch1']

            # FabArbiter  : V0.1
            m = p81.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fabarbiter'] = match_dict['fabarbiter']

            # FIA  : V0.2
            m = p82.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['fia'] = match_dict['fia']

            # IntCtrl  : V0.11
            m = p83.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['intctrl'] = match_dict['intctrl']

            # ClkCtrl  : V2.10
            m = p84.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['clkctrl'] = match_dict['clkctrl']

            # 10GPuntFPGA  : V1.10
            m = p85.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['10gpuntfpga'] = match_dict['puntfpga']

            # HD  : V2.16
            m = p86.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hd'] = match_dict['hd']

            # USB0  : V2.16
            m = p87.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['usb0'] = match_dict['usb0']

            # USB1  : V0.0
            m = p88.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['usb1'] = match_dict['usb1']

            # CpuCtrl  : V0.11
            m = p89.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cpuctrl'] = match_dict['cpuctrl']

            # YDTI  : V4.9
            m = p90.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['ydti'] = match_dict['ydti']

            # LIU  : V0.0
            m = p91.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['liu'] = match_dict['liu']

            # MLANSwitch  : V0.0
            m = p92.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['mlanswitch'] = match_dict['mlanswitch']

            # EOBCSwitch  : V0.0
            m = p93.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['eobcswitch'] = match_dict['eobcswitch']

            # HostInftCtrl  : V0.0
            m = p94.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['hostinftctrl'] = match_dict['hostinftctrl']

            # PHY  : V0.0
            m = p95.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['phy'] = match_dict['phy']

            # Offload10GE  : V0.0
            m = p96.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['offload10ge'] = match_dict['offload10ge']

            # E10GEDualMAC0  : V0.0
            m = p97.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['e10gedualmac0'] = match_dict['e10gedualmac0']

            # E10GEDualMAC1  : V0.0
            m = p98.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['e10gedualmac1'] = match_dict['e10gedualmac1']

            # EGEDualMAC0  : V0.0
            m = p99.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['egedualmac0'] = match_dict['egedualmac0']

            # EGEDualMAC1  : V0.0
            m = p100.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['egedualmac1'] = match_dict['egedualmac1']

            # CBC (active partition)  : v16.117
            m = p101.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cbc_active_partition'] = match_dict['cbc_active_partition']

            # CBC (inactive partition)  : v16.116
            m = p102.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cbc_inactive_partition'] = match_dict['cbc_inactive_partition']

            # NP0  : V4.194
            m = p103.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block["np"+ match_dict['np']] = match_dict['np0']

            # FIA0  : V0.2
            m = p104.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block["fia"+ match_dict['fia']] = match_dict['fia0']

            # X-Bar  : V1.5
            m = p105.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['xbar'] = match_dict['xbar']

            # Arbiter  : V0.2
            m = p106.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['arbiter'] = match_dict['arbiter']

            # PortCtrl  : V1.0
            m = p107.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['portctrl'] = match_dict['portctrl']

            # PHYCtrl  : V1.1
            m = p108.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['phyctrl'] = match_dict['phyctrl']

            # USB  : V17.0
            m = p109.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['usb'] = match_dict['usb']

            # PHY0  : V0.4(HwRev)	V0.0(FwRev)	V8.0(SwRev)
            m = p110.match(line)
            if m:
                match_dict = m.groupdict()
                ph = match_dict['phy'].lower()
                phy = pointer_block.setdefault(ph, {})
                phy['hwrev'] = match_dict['hwrev']
                phy['fwrev'] = match_dict['fwrev']
                phy['swrev'] = match_dict['swrev']

            # Base MAC Address         : 00a7.428b.f4b0
            m = p111.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['base_mac_address'] = match_dict['base_mac_address']

            # Capabilities             : 00
            m = p112.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['capabilities'] = match_dict['capabilities']

            # ENVMON Information       : 2 86 0 0 0 0 0 0
            m = p113.match(line)
            if m:
                match_dict = m.groupdict()
                envmon_information = match_dict['envmon_information']

            # 0 0 0 0 0 0 0 0
            m = p113_1.match(line)
            if m:
                match_dict = m.groupdict()
                envmon_information = envmon_information + match_dict['env_info']
                pointer_block['envmon_information'] = envmon_information

            # RMA Test History         : 00
            m = p114.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['rma_test_history'] = match_dict['rma_test_history']

            # RMA Number               : 0-0-0-0
            m = p115.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['rma_number'] = match_dict['rma_number']

            # RMA History              : 00
            m = p116.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['rma_history'] = match_dict['rma_history']

            # Device values            : 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0
            m = p117.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['device_values'] = match_dict['device_values']

        return ret_dict


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

# ==============================================
# Parser for 'show filesystem location all'
# ==============================================

class ShowFilesystemLocationAllSchema(MetaParser):
    """Schema for show filesystem location all"""

    schema = {
        'node': {
            Any(): {
                'file_systems': {
                    Any(): {
                    'total_size': int,
                    'free_size': int,
                    'type': str,
                    'flags': str,
                    'prefixes': str,
                    }
                }
            }
        }
    }

class ShowFilesystemLocationAll(ShowFilesystemLocationAllSchema):

    cli_command = ['show filesystem location all']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        # node:  node0_RP0_CPU0
        p1 = re.compile(r'^node:\s+(?P<node>\S+)$')

        # 3962216448   3926405120  flash-disk     rw  apphost:
        p2 = re.compile(r'^(?P<total_size>\d+)\s*(?P<free_size>\d+)\s*(?P<type>\S*)\s*(?P<flags>\S*)\s*(?P<prefixes>[\S\s]+)$')

        # initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # node:  node0_RP0_CPU0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node_dict = ret_dict.setdefault('node', {}).setdefault(group['node'], {})
                index = 0
                continue

            # 3962216448   3926405120  flash-disk     rw  apphost:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                file_systems_dict = node_dict.setdefault('file_systems', {}).setdefault(index, {})
                file_systems_dict.update({
                    'total_size': int(group['total_size']),
                    'free_size': int(group['free_size']),
                    'type': group['type'],
                    'flags': group['flags'],
                    'prefixes': group['prefixes'],
                    })
                continue

        return ret_dict

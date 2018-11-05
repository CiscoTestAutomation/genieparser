''' show_paltform.py

IOSXR parsers for the following show commands:
    * 'show version'
    * 'show sdr detail'
    * 'show platform'
    * 'show platform vm'
    * 'show install active summary'
    * 'show inventory'
    * 'admin show diag chassis'
    * 'show redundancy summary'
    * 'show redundancy'
    * 'dir'
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
              'device_family': str,
              Optional('processor'): str,
              Optional('processor_memory_bytes'): str,
              Optional('chassis_detail'): str,
              Optional('config_register'): str,
              Optional('rp_config_register'): str,
              Optional('main_mem'): str,
             }

class ShowVersion(ShowVersionSchema):
    """Parser for show version"""
    def cli(self):
        cmd = 'show version'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        show_version_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # Cisco IOS XR Software, Version 6.3.1.15I
            # Cisco IOS XR Software, Version 6.1.4.10I[Default]
            p1 = re.compile(r'\s*Cisco +IOS +XR +Software, +Version'
                             ' +(?P<software_version>[A-Z0-9\.]+)(?:\[Default\])?$')
            m = p1.match(line)
            if m:
                show_version_dict['operating_system'] = 'IOSXR'
                show_version_dict['software_version'] = \
                    str(m.groupdict()['software_version'])
                continue

            # System uptime is 1 week, 1 day, 5 hours, 47 minutes
            # PE1 uptime is 3 hours, 11 minutes
            p2 = re.compile(r'\s*.* +uptime +is +(?P<uptime>[a-zA-Z0-9\s\,]+)$')
            m = p2.match(line)
            if m:
                show_version_dict['uptime'] = str(m.groupdict()['uptime'])
                continue

            # System image file is "disk0:asr9k-os-mbi-6.1.4.10I/0x100305/mbiasr9k-rsp3.vm"
            p3 = re.compile(r'\s*System +image +file +is'
                             ' +\"(?P<image>[a-zA-Z0-9\:\/\.\-]+)\"$')
            m = p3.match(line)
            if m:
                show_version_dict['image'] = str(m.groupdict()['image'])
                continue

            # cisco IOS-XRv 9000 () processor
            p4 = re.compile(r'\s*cisco +(?P<device_family>[a-zA-Z0-9\-\s]+)'
                               ' +\(\) +processor$')
            m = p4.match(line)
            if m:
                show_version_dict['device_family'] = \
                    str(m.groupdict()['device_family'])
                continue

            # cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K bytes of memory.
            p5 = re.compile(r'\s*cisco +(?P<device_family>[a-zA-Z0-9\s]+)'
                               ' +Series +\((?P<processor>[a-zA-Z0-9\s]+)\)'
                               ' +processor +with'
                               ' +(?P<processor_memory_bytes>[0-9A-Z]+) +bytes'
                               ' +of +memory.$')
            m = p5.match(line)
            if m:
                show_version_dict['device_family'] = \
                    str(m.groupdict()['device_family'])
                show_version_dict['processor'] = str(m.groupdict()['processor'])
                show_version_dict['processor_memory_bytes'] = \
                    str(m.groupdict()['processor_memory_bytes'])
                show_version_dict['main_mem'] = str(line).strip()
                continue

            # Configuration register on node 0/RSP0/CPU0 is 0x1922
            p6 = re.compile(r'\s*Configuration +register +on +node'
                             ' +(?P<node>[A-Z0-9\/]+) +is'
                             ' +(?P<config_register>[x0-9]+)$')
            m = p6.match(line)
            if m:
                show_version_dict['config_register'] = \
                    m.groupdict()['config_register']
                node = str(m.groupdict()['node'])
                if re.search('CPU0', node):
                    show_version_dict['rp_config_register'] = \
                        str(m.groupdict()['config_register'])
                continue

            # ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            p7 = re.compile(r'\s*.*Chassis.*$')
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
    def cli(self):
        cmd = 'show sdr detail'.format()
        out = self.device.execute(cmd)
        
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

            # mac addr             : 025e.ea57.a400
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
                             ' +(?P<node_status>[IOS XR RUN|OPERATIONAL]+)'
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
    def cli(self):
        cmd = 'show platform'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        show_platform = {}
        daughtercard_dict = {}

        for line in out.splitlines():
            entry_is_daughter = False
            line = line.rstrip()

            # 0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
            # 0/0/CPU0        RP(Active)      N/A             IOS XR RUN      PWR,NSHUT,MON
            p1 = re.compile(r'\s*(?P<node>[a-zA-Z0-9\/]+)'
                             ' +(?P<name>[a-zA-Z0-9\-]+)'
                             '(?:\((?P<redundancy_state>[a-zA-Z]+)\))?'
                             '(?: +(?P<plim>[a-zA-Z\/]+))?'
                             ' +(?P<state>(IOS XR RUN|OK)+)'
                             ' +(?P<config_state>[a-zA-Z\,]+)$')
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
                parse_node = re.compile(r'\s*(?P<rack>[0-9]+)'
                                         '\/(?P<slot>[0-9A-Z]+)'
                                         '\/(?P<last_entry>[0-9A-Z]+)'
                                         '$').match(node)
                rack = str(parse_node.groupdict()['rack'])
                slot = rack + '/' + str(parse_node.groupdict()['slot'])
                last_entry = str(parse_node.groupdict()['last_entry'])

                # Check if subslot/daughtercard
                parse_subslot = re.compile(r'.*(0\/0\/[0-9]+).*').match(node)
                if parse_subslot and last_entry.isdigit():
                    # This entry is a daughtercard/subslot
                    entry_is_daughter = True
                    subslot = last_entry
                
                # Determine if slot is RP/LineCard/OtherCard
                parse_rp = re.compile(r'.*(RSP|RP).*').match(slot)
                parse_lc = re.compile(r'.*(0\/0).*').match(slot)
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
                    if plim != 'None':
                        show_platform['slot'][slot_type][slot]['plim'] = plim
                    # Check for daughtercards
                    if daughtercard_dict and slot in daughtercard_dict:
                        # Then merge dictionary
                        show_platform['slot'][slot_type][slot]['subslot'].update(daughter_temp[slot])
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
    def cli(self):
        cmd = 'show platform vm'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        show_platform_vm = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # 0/RP0/CPU0      RP (ACTIVE)     NONE            FINAL Band      192.0.0.4
            # 0/0/CPU0        LC (ACTIVE)     NONE            FINAL Band      192.0.0.6
            p1 = re.compile(r'\s*(?P<node>[a-zA-Z0-9\/]+)'
                             ' +(?P<type>[a-zA-Z0-9\(\)\s]+)'
                             ' +(?P<partner_name>[NONE]+)'
                             ' +(?P<sw_status>[a-zA-Z\s]+)'
                             ' +(?P<ip_address>[0-9\.]+)$')
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
    def cli(self):
        cmd = 'show install active summary'.format()
        out = self.device.execute(cmd)
        
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
                 'sn': str,
                },
            },
        }

class ShowInventory(ShowInventorySchema):
    """Parser for show inventory"""
    def cli(self):
        cmd = 'show inventory'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        inventory_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # NAME: "module 0/RSP0/CPU0", DESCR: "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB"
            # NAME: "Rack 0", DESCR: "Cisco XRv9K Centralized Virtual Router"
            # NAME: "Rack 0", DESCR: "Sherman 1RU Chassis with 24x400GE QSFP56-DD & 12x100G QSFP28"
            # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
            p1 = re.compile(r'\s*NAME: +\"(?P<module_name>[a-zA-Z0-9\/\s]+)\",'
                             ' +DESCR: +\"(?P<descr>[\w\-\.\:\/\s,&]+)\"$')
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
            p2 = re.compile(r'\s*PID: +(?P<pid>[a-zA-Z0-9\/\-\s]+),'
                             ' +VID: +(?P<vid>[a-zA-Z0-9\/\s]+),'
                             ' +SN: +(?P<sn>[a-zA-Z0-9\/\s]+)$')
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
        'device_family': str,
        'device_series': int,
        'num_line_cards': int,
        'chassis_feature': str,
        'rack_num': int,
        'sn': str,
        'pid': str,
        'vid': str,
        'desc': str,
        'clei': str,
        'top_assy_num': str,
        }

class AdminShowDiagChassis(AdminShowDiagChassisSchema):
    """Parser for admin show diag chassis"""
    def cli(self):
        cmd = 'admin show diag chassis'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        admin_show_diag_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # Rack 0 - ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            p1 = re.compile(r'\s*Rack +(?P<rack_num>[0-9]+)'
                            ' +\- +(?P<device_family>[a-zA-Z]+)'
                            ' +(?P<device_series>[0-9]+)'
                            ' +(?P<num_line_cards>[0-9]+)'
                            ' +Line +Card +Slot +Chassis +with'
                            ' +(?P<chassis_feature>[a-zA-Z0-9\s]+)$')
            m = p1.match(line)
            if m:
                admin_show_diag_dict['rack_num'] = \
                    int(m.groupdict()['rack_num'])
                admin_show_diag_dict['device_family'] = \
                    str(m.groupdict()['device_family'])
                admin_show_diag_dict['device_series'] = \
                    int(m.groupdict()['device_series'])
                admin_show_diag_dict['num_line_cards'] = \
                    int(m.groupdict()['num_line_cards'])
                admin_show_diag_dict['chassis_feature'] = \
                    str(m.groupdict()['chassis_feature'])
                continue

            # RACK NUM: 0
            p2 = re.compile(r'\s*RACK NUM: *(?P<rack_num>[0-9]+)$')
            m = p2.match(line)
            if m:
                admin_show_diag_dict['rack_num'] = \
                    int(m.groupdict()['rack_num'])
                continue

            
            # S/N:   FOX1810G8LR
            p3 = re.compile(r'\s*S\/N: *(?P<sn>[a-zA-Z0-9]+)$')
            m = p3.match(line)
            if m:
                admin_show_diag_dict['sn'] = \
                    str(m.groupdict()['sn'])
                continue
            
            # PID:   ASR-9006-AC-V2
            p4 = re.compile(r'\s*PID: *(?P<pid>[a-zA-Z0-9\-]+)$')
            m = p4.match(line)
            if m:
                admin_show_diag_dict['pid'] = \
                    str(m.groupdict()['pid'])
                continue
            
            # VID:   V02
            p5 = re.compile(r'\s*VID: *(?P<vid>[a-zA-Z0-9\-]+)$')
            m = p5.match(line)
            if m:
                admin_show_diag_dict['vid'] = \
                    str(m.groupdict()['vid'])
                continue

            # Desc:  ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
            p6 = re.compile(r'\s*Desc: *(?P<desc>[a-zA-Z0-9\-\s]+)$')
            m = p6.match(line)
            if m:
                admin_show_diag_dict['desc'] = \
                    str(m.groupdict()['desc'])
                continue
            
            # CLEI:  IPMUP00BRB
            p7 = re.compile(r'\s*CLEI: *(?P<clei>[a-zA-Z0-9\-]+)$')
            m = p7.match(line)
            if m:
                admin_show_diag_dict['clei'] = \
                    str(m.groupdict()['clei'])
                continue
            
            # Top Assy. Number:   68-4235-02
            p8 = re.compile(r'\s*Top +Assy. +Number:'
                             ' *(?P<top_assy_num>[a-zA-Z0-9\-\s]+)$')
            m = p8.match(line)
            if m:
                admin_show_diag_dict['top_assy_num'] = \
                    str(m.groupdict()['top_assy_num'])
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
    def cli(self):
        cmd = 'show redundancy summary'.format()
        out = self.device.execute(cmd)
        
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
    def cli(self):
        cmd = 'show redundancy'.format()
        out = self.device.execute(cmd)
        
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
    """Schema for dir"""
    schema = {
        'dir': {
            'dir_name': str,
            'total_bytes': str,
            'total_free_bytes': str,
            Optional('files'):
                {Any():
                    {Optional('size'): str,
                     Optional('date'): str,
                     Optional('permission'): str,
                     Optional('index'): str,
                     Optional('time'): str}
                },
            },
        }

class Dir(DirSchema):
    """Parser for dir"""
    def cli(self):
        cmd = 'dir'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        dir_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # Directory of /misc/scratch
            # Directory of disk0a:/usr
            p1 = re.compile(r'\s*Directory +of'
                             ' +(?P<dir_name>[a-zA-Z0-9\:\/]+)$')
            m = p1.match(line)
            if m:
                if 'dir' not in dir_dict:
                    dir_dict['dir'] = {}
                    dir_dict['dir']['dir_name'] = str(m.groupdict()['dir_name'])
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
            p3 = re.compile(r'^\s*(?P<index>[0-9]+) +(?P<permission>[a-z\-]+)(\.)? '
                '+(?P<unknown>[0-9]+) +(?P<size>[0-9]+) +(?P<month>[a-zA-Z]+) '
                '+(?P<day>[0-9]+) +(?P<year>[0-9\:]+) '
                '+(?P<file>[a-zA-Z0-9\.\/\_\-\+\>\s]+)$')
            m = p3.match(line)
            if m:
                file = m.groupdict()['file']
                date = m.groupdict()['month'].strip() \
                    + ' ' + m.groupdict()['day'].strip() + ' ' \
                    + m.groupdict()['year'].strip()
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

# vim: ft=python et sw=4

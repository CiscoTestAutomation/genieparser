''' show_platform.py

IOSXR parsers for the following show commands:
    * 'show diag details'
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
                Optional('clei'): str,
                Optional('sn'): str,
                Optional('hwrev_udi_vid'): str,
                Optional('top_assy_number'): str,
                Optional('chip_hwrev'): str,
                Optional('new_deviation_num'): int,
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
                    Optional('main_board_type'): str,
                    Optional('board_state'): str,
                    Optional('clei'): str,
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
                    Optional('stackmib_oid'): int,
                    Optional('cooling_capacity'): int,
                    Optional('sensor'): {
                        Any(): str
                    },
                    Optional('current_volt'): {
                        Any(): str
                    },
                    Optional('current_mode'): {
                        Any(): str
                    },
                    Optional('max_float_current_mode'): {
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
        p3 = re.compile(r'^(PID|Product ID)\s*:\s+(?P<pid>[\w\.-]+)$')

        # Version Identifier         : V03
        p4 = re.compile(r'^(VID|Version Identifier)\s*:\s+(?P<version_identifier>.+?)$')

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

        # PCA:   73-17858-02 rev N/A
        p10_1 = re.compile(r'^PCA:\s+(?P<serial_number>[\w-]+)(\s+rev +(?P<pca_rev>\S+))*$')
        
        # PCA Revision               : E0
        p11 = re.compile(r'^PCA Revision\s+:\s+(?P<pca_rev>.+?)$')

        # CLEI Code                  : CMM6210ARC
        p12 = re.compile(r'^CLEI Code\s*:\s+(?P<clei_code>\w+)$')

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
        p28 = re.compile(r'^Block Signature\s+:\s+(?P<block_signature>\w+)$')

        # Block Version   : 3
        p29 = re.compile(r'^Block Version\s+:\s+(?P<block_version>\d+)$')

        # Block Length    : 160
        p30 = re.compile(r'^Block Length\s+:\s+(?P<block_length>\d+)$')

        # Block Checksum  : 0x1b10
        p31 = re.compile(r'^Block Checksum\s+:\s+(?P<block_checksum>.+?)$')

        # EEPROM Size     : 65535
        p32 = re.compile(r'^EEPROM Size\s+:\s+(?P<eeprom_size>\d+)$')

        # Block Count     : 4
        p33 = re.compile(r'^Block Count\s+:\s+(?P<block_count>\d+)$')

        # FRU Major Type  : 0x6003
        p34 = re.compile(r'^FRU Major Type\s+:\s+(?P<fru_major_type>\w+)$')

        # FRU Minor Type  : 0x0
        p35 = re.compile(r'^FRU Minor Type\s+:\s+(?P<fru_minor_type>\w+)$')

        # OEM String      : Cisco Systems, Inc.
        p36 = re.compile(r'^OEM String\s+:\s+(?P<oem_string>.+?)$')

        # Serial Number   : JAE24480QCT
        p37 = re.compile(r'^Serial Number\s+:\s+(?P<serial_number>\w+)$')

        # Part Number     : 73-102072-04
        p38 = re.compile(r'^Part Number\s+:\s+(?P<part_number>.+?)$')

        # Part Revision   : 05
        p39 = re.compile(r'^Part Revision\s+:\s+(?P<part_revision>\w+)$')

        # Mfg Deviation   : 000000000
        p40 = re.compile(r'^Mfg Deviation\s+:\s+(?P<mfg_deviation>\w+)$')

        # H/W Version     : 0.300
        p41 = re.compile(r'^H/W Version\s+:\s+(?P<hw_version>.+?)$')

        # Mfg Bits        : 0
        p42 = re.compile(r'^Mfg Bits\s+:\s+(?P<mfg_bits>\w+)$')

        # Engineer Use    : 0
        p43 = re.compile(r'^Engineer Use\s+:\s+(?P<engineer_use>\w+)$')

        # snmpOID         : 9.12.3.1.9.2.708.0
        p44 = re.compile(r'^snmpOID\s+:\s+(?P<snmpoid>.+?)$')

        # RMA Code        : 0-0-0-0
        p45 = re.compile(r'^RMA Code\s+:\s+(?P<rma_code>.+?)$')

        # Card Specific Block:
        p46 = re.compile(r'^Card Specific Block:$')

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
        p61 = re.compile(r'^Ambient Temperature\s*:\s+(?P<ambient_temp>\d+)$')

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
        p67 = re.compile(r'^S\/N:?\s+(?P<sn>.+)$')

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

        # MPA 0/0/1 : ASR 9000 20-port 1GE Modular Port Adapter
        p118 = re.compile(r'^MPA+\s+(?P<item>.+?)\s+:+\s+(?P<description>.+?)$')

        # RP Module Specific Block:
        p119 = re.compile(r'^RP Module Specific Block+\:$')

        # Chassis Specific Block:
        p120 = re.compile(r'^Chassis Specific Block+\:$')

        # Second Serial Number Specific Block:
        p121 = re.compile(r'^Second Serial Number Specific Block+\:$')

        # Top Assembly Block
        p122 = re.compile(r'^Top Assembly Block+\:$')

        # Power Supply Specific Block:
        p123 = re.compile(r'^Power Supply Specific Block+\:$')

        # Fan Module Specific Block:
        p124 = re.compile(r'^Fan Module Specific Block+\:$')
        
        # Stackmib OID    : 0
        p125 = re.compile(r'^Stackmib OID\s+:\s+(?P<stackmib_oid>\d+)$')

        # Cooling Capacity    : 0
        p126 = re.compile(r'^Cooling Capacity\s+:\s+(?P<cooling_capacity>\d+)$')

        # Current 110v    : 8300
        p127 = re.compile(r'^Current+\s(?P<volt>\d+v)\s+:+\s+(?P<current>\d+)$')

        # Current mode1   : 0
        p128 = re.compile(r'^Current+\s(?P<mode>\S+)\s+:+\s+(?P<current_mode>\d+)$')

        # Max Float Current mode1: 0
        p129 = re.compile(r'^Max Float Current +(?P<mode>\S+):+\s+(?P<max_float>\d+)$')

        pointer_block = {}
        item = None

        for line in output.splitlines():
            line = line.strip()

            # p0
            # Rack 0-Chassis IDPROM - Cisco 8000 Series 32x400G QSFPDD 1RU Fixed System w/HBM
            # 0/0-DB-IDPROM - 400G Modular Linecard, Service Edge Optimized

            # p65
            # NODE module 0/RSP0/CPU0  ASR9K Route Switch Processor with 440G/slot Fabric and 12GB
            m = p0.match(line) or p65.match(line) or p118.match(line)
            if m:
                match_dict = m.groupdict()
                item = match_dict['item']
                item_dict = ret_dict.setdefault('item', {}).setdefault(item, {})
                item_dict['description'] = match_dict['description']

                pointer_block = item_dict

                # If description is of parent is N/A, override it
                if item and '-DB' in item:
                    item_ = item.replace('-DB', '')
                    if ret_dict.get('item', {}).get(item_, {}).get('description') == 'N/A':
                        item_dict = ret_dict.setdefault('item', {}).setdefault(item_, {})
                        item_dict['description'] = match_dict['description']
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

                # if this is a daughter board and PID not set for parent module, update it
                if item and '-DB' in item:
                    item = item.replace('-DB', '')
                    item_dict.setdefault('pid', match_dict['pid'])
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
            # PCA:   73-13152-04 rev N/A 
            m = p10.match(line) or p10_1.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pca_number'] = match_dict['serial_number']
                if 'rev' in line:
                    pointer_block['pca_revision'] = match_dict['pca_rev']
                continue

            # PCA Revision               : E0
            m = p11.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['pca_revision'] = match_dict['pca_rev']
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
                pointer_block['eci_number'] = match_dict['eci_number']
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

            # RP Module Specific Block:
            m = p119.match(line)
            if m:
                rp_module_specifc_blocks = item_dict.setdefault('rp_module_specifc_blocks', {})
                pointer_block = rp_module_specifc_blocks
                continue

            # Chassis Specific Block:
            m = p120.match(line)
            if m:
                chassis_specific_blocks = item_dict.setdefault('chassis_specific_blocks', {})
                pointer_block = chassis_specific_blocks
                continue

            # Second Serial Number Specific Block:
            m = p121.match(line)
            if m:
                second_serial_no_specific_blocks = item_dict.setdefault('second_serial_no_specific_blocks', {})
                pointer_block = second_serial_no_specific_blocks
                continue
            
            # Top Assembly Block
            m = p122.match(line)
            if m:
                top_assesmbly_blocks = item_dict.setdefault('top_assesmbly_blocks', {})
                pointer_block = top_assesmbly_blocks
                continue
            
            # Power Supply Specific Block:
            m = p123.match(line)
            if m:
                power_supply_specific_blocks = item_dict.setdefault('power_supply_specific_blocks', {})
                pointer_block = power_supply_specific_blocks
                continue

            # Fan Module Specific Block:
            m = p124.match(line)
            if m:
                fan_module_specific_blocks = item_dict.setdefault('fan_module_specific_blocks', {})
                pointer_block = fan_module_specific_blocks
                continue

            # Stackmib OID    : 0
            m = p125.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['stackmib_oid'] = int(match_dict['stackmib_oid'])
                continue
            
            # Cooling Capacity    : 0
            m = p126.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block['cooling_capacity'] = int(match_dict['cooling_capacity'])
                continue

            # Current 110v    : 8300
            m = p127.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block.setdefault('current_volt', {}).setdefault(match_dict['volt'], match_dict['current'])
                continue

            # Current 110v    : 8300
            m = p128.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block.setdefault('current_mode', {}).setdefault(match_dict['mode'], match_dict['current_mode'])
                continue

            # Current 110v    : 8300
            m = p129.match(line)
            if m:
                match_dict = m.groupdict()
                pointer_block.setdefault('max_float_current_mode', {}).setdefault(match_dict['mode'], match_dict['max_float'])
                continue

        return ret_dict


import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ================
# Schema for:
#  * 'show romvar'
# ================
class ShowRomvarSchema(MetaParser):
    """Schema for show romvar."""

    schema = {
        "rommon_variables" : {
            Optional("ps1"): str,
            Optional("switch_number"): int,
            Optional("mcp_startup_traceflags"): str,
            Optional("license_active_level"): str,
            Optional("license_boot_level"): str,
            Optional("stack"): str,
            "boot": list,
            Optional("switch_priority"): int,
            Optional("chassis_ha_local_ip"): str,
            Optional("chassis_ha_remote_ip"): str,
            Optional("chassis_ha_local_mask"): str,
            Optional("ret_2_rts"): str,
            Optional("rmi_interface"): str,
            Optional("rmi_local_ip"): str,
            Optional("rmi_remote_ip"): str,
            "bsi": int,
            Optional("ret_2_rcalts"): str,
            "random_num": int,
            Optional("thrput"): str,
            Optional("config_file"): str,
            Optional("bootldr"): str,
            Optional("crashinfo"): str,
            Optional("no_console"): int,
            Optional("boot_device_mode"): str,
            Optional("boardid"): int,
            Optional("mac_addr"): str,
            Optional("manual_boot"): str,
            Optional("model_num"): str,
            Optional("model_revision_num"): str,
            Optional("motherboard_assembly_num"): str,
            Optional("motherboard_revision_num"): str,
            Optional("motherboard_serial_num"): str,
            Optional("rommon_autoboot_attempt"): int,
            Optional("system_serial_num"): str,
            Optional("version_id"): str,
            Optional("device_managed_mode"): str,
            Optional("default_gateway"): str,
            Optional("ip_address"): str,
            Optional("crashinfo"): str,
            Optional("subnet_mask"): str,
            Optional("abnormal_reset_count"): int
        }
    }


# ================
# Parser for:
#  * 'show romvar'
# ================
class ShowRomvar(ShowRomvarSchema):
    """Parser for show romvar"""

    cli_command = "show romvar"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        # ROMMON variables:
        #
        # PS1 = rommon ! >
        #
        # ? = 0
        #
        # SWITCH_NUMBER = 1
        #
        # THRPUT =
        #
        # MCP_STARTUP_TRACEFLAGS = 00000000:00000000
        #
        # LICENSE_ACTIVE_LEVEL = adventerprise,all:c980080k9;
        #
        # LICENSE_BOOT_LEVEL = adventerprise,all:c980080k9;
        #
        # CONFIG_FILE =
        #
        # BOOTLDR =
        #
        # STACK_1_1 = 0_0
        #
        # BOOT = bootflash:packages.conf,12;
        #
        # SWITCH_PRIORITY = 2
        #
        # CHASSIS_HA_LOCAL_IP = 10.10.30.6
        #
        # CHASSIS_HA_REMOTE_IP = 10.10.30.7
        #
        # CHASSIS_HA_LOCAL_MASK = 255.255.255.0
        #
        # RET_2_RTS = 15:45:35 UTC Wed Jul 29 2020
        #
        # RMI_INTERFACE_NAME = Vlan10
        #
        # RMI_CHASSIS_LOCAL_IP = 10.10.30.6
        #
        # RMI_CHASSIS_REMOTE_IP = 10.10.30.7
        #
        # BSI = 0
        #
        # RET_2_RCALTS =
        #
        # RANDOM_NUM = 2143851718
        #
        # NO_CONSOLE=1
        #
        # BOOT_DEVICE_MODE=meraki
        #
        # BOARDID=28755
        #
        # MAC_ADDR=6C:13:D5:1B:5C:80
        #
        # MANUAL_BOOT=no
        #
        # MODEL_NUM=C9300-48U
        #
        # MODEL_REVISION_NUM=A0
        #
        # MOTHERBOARD_ASSEMBLY_NUM=73-19919-04
        #
        # MOTHERBOARD_REVISION_NUM=A0
        #
        # MOTHERBOARD_SERIAL_NUM=FOC25124Q2U
        #
        # ROMMON_AUTOBOOT_ATTEMPT=0
        #
        # SYSTEM_SERIAL_NUM=FOC2514L1HE
        #
        # VERSION_ID=V05
        #
        # ABNORMAL_RESET_COUNT=0


        # ROMMON variables:
        p_variables = re.compile(r"^ROMMON\s+variables.*$")

        # PS1 = rommon ! >
        p_ps1 = re.compile(r"^PS1\s*=\s*(?P<ps1>.*)$")

        # THRPUT =
        p_thrput = re.compile(r".*(THRPUT|THPUT)\s*=\s*(?P<thrput>.*)$")

        # SR_MGMT_VRF = 0
        p_mgmt_vrf = re.compile(r"^SR_MGMT_VRF\s*=\s*(?P<mgmt_vrf>.*)$")

        # REAL_MGMTE_DEV =
        p_mgmte_dev = re.compile(r"^REAL_MGMTE_DEV\s*=\s*(?P<mgmte_dev>.*)$")

        # IP_ADDRESS = 10.19.92.165
        p_ip = re.compile(r"^IP_ADDRESS\s*=\s*(?P<ip_address>\S+)$")

        # DEFAULT_GATEWAY = 10.19.92.1
        p_gateway = re.compile(r"^DEFAULT_GATEWAY\s*=\s*(?P<gateway>\S+)$")

        # IP_SUBNET_MASK = 255.255.255.0
        p_mask = re.compile(r"^IP_SUBNET_MASK\s*=\s*(?P<ip_mask>\S+)$")

        # DEV_MODE0 = FM5R95WUO0WUATJTQX5I5ZQHLWIT6CWKD513RVT9Q5UQKJVKPDSNU7NR1EDU4QWO
        p_dev_mode_0 = re.compile(r"^DEV_MODE0\s*=\s*(?P<mode_0>\S+)$")

        # DEV_MODE1 = ICQWTUNIEAVS6DH4X7GBV3917N3M1YNMQC5JDW4GM9OLFOZ0B4XCPXGXE596Z71C
        p_dev_mode_1 = re.compile(r"^DEV_MODE1\s*=\s*(?P<mode_1>\S+)$")

        # DEV_MODE2 = 93URXAFOPS1F74TR7LAT9BCAQ5O0LX73WHFMWKRQKZDYFIUCHTPK0SBVEYFZXSAQ
        p_dev_mode_2 = re.compile(r"^DEV_MODE2\s*=\s*(?P<mode_2>\S+)$")

        # DEV_MODE3 = 6LQB4NEFCJ1DYOV929FGLMX3XK710QERFA2SWWCE8C08D5WYLS2X6CXDVQY0CFIO
        p_dev_mode_3 = re.compile(r"^DEV_MODE3\s*=\s*(?P<mode_3>\S+)$")

        # DEV_MODE4 = 1DY4J4L14FCUYC22JDK8YLQQVF0ZPC9BVT7HM75LF4Z319VKS2WE8XWAUV1PEF27
        p_dev_mode_4 = re.compile(r"^DEV_MODE4\s*=\s*(?P<mode_4>\S+)$")

        # DEV_MODE5 = 7YMXKN3FA6X5OEGHUZISA16KC0VAZ51S12JGPMUD3NZCCSTTGZ7O9G58NRUZIKBG
        p_dev_mode_5 = re.compile(r"^DEV_MODE5\s*=\s*(?P<mode_5>\S+)$")

        # DEV_MODE6 = AR1PHFLWRD9ZGDSC0BKKIGWQBUJXX0FGJT3EEU8A7MMUVPLS73FP4WBUIZUS3X76
        p_dev_mode_6 = re.compile(r"^DEV_MODE6\s*=\s*(?P<mode_6>\S+)$")

        # DEV_MODE7 = H5LF3EG7Y2S45ZFEB3GTDSK5M9XLDH4FUU7BQFZ9JI7PRWAHA3HS27JCU4A7PBN1
        p_dev_mode_7 = re.compile(r"^DEV_MODE7\s*=\s*(?P<mode_7>\S+)$")

        # ? = 1
        p_question = re.compile(r"^/?=1$")

        # MCP_STARTUP_TRACEFLAGS = 00000000:00000000
        p_mcp = re.compile(r"^MCP_STARTUP_TRACEFLAGS\s*=\s*(?P<tflag>.*)$")

        # RET_2_RTS = 23:48:46 Pacific Fri Dec 13 2019
        p_ret_rts = re.compile(r"^RET_2_RTS\s*=\s*(?P<ret_date>.*)$")

        # CHASSIS_HA_LOCAL_IP = 10.10.68.54
        p_chassis_ha_ip = re.compile(r"^CHASSIS_HA_LOCAL_IP\s*=\s*(?P<ha_ip>\S+)$")

        # CHASSIS_HA_REMOTE_IP = 10.10.68.52
        p_chassis_ha_remote_ip = re.compile(r"CHASSIS_HA_REMOTE_IP\s*=\s*(?P<remote_ha_ip>\S+)$")

        # CHASSIS_HA_LOCAL_MASK = 255.255.255.240
        p_chassis_ha_mask = re.compile(r"^CHASSIS_HA_LOCAL_MASK\s*=\s*(?P<ha_mask>\S+)$")

        # SWITCH_PRIORITY = 1
        p_switch_priority = re.compile(r"^SWITCH_PRIORITY\s*=\s*(?P<priority>\d+)$")

        # SWITCH_NUMBER = 2
        p_switch_number = re.compile(r"^SWITCH_NUMBER\s*=\s*(?P<number>\d+)$")

        # LICENSE_ACTIVE_LEVEL = adventerprise,all:c9800lk9;
        p_lic_active = re.compile(r"^LICENSE_ACTIVE_LEVEL\s*=\s*(?P<lic_active>.*)$")

        # LICENSE_BOOT_LEVEL = adventerprise,all:c980080k9;
        p_lic_boot = re.compile(r"^LICENSE_BOOT_LEVEL\s*=\s*(?P<lic_boot>.*)$")

        # CONFIG_FILE =
        p_config_file = re.compile(r"^CONFIG_FILE\s*=\s*(?P<config_file>.*)$")

        # BOOTLDR =
        p_bootldr = re.compile(r"^BOOTLDR\s*=\s*(?P<bootldr>.*)$")

        # BOOT = bootflash:packages.conf,12;bootflash:C9800-L-universalk9_wlc.BLD_V173_THROTTLE_LATEST_20200707_003212_2.SSA.bin,12;
        p_boot = re.compile(r"^BOOT\s*=\s*(?P<boot>.*)$")

        # BSI = 0
        p_bsi = re.compile(r"^BSI\s*=\s*(?P<bsi>\d+)$")

        # RET_2_RCALTS =
        p_rcalts = re.compile(r"^RET_2_RCALTS\s*=\s*(?P<rcalts>.*)")

        # RANDOM_NUM = 25654861
        p_random = re.compile(r"^RANDOM_NUM\s*=\s*(?P<random>\d+)$")

        # STACK_1_1 = 0_0
        p_stack = re.compile(r"^STACK_1_1\s*=\s*(?P<stack>.*)$")

        # RMI_INTERFACE_NAME = Vlan10
        p_rmi_int = re.compile(r"^RMI_INTERFACE_NAME\s*=\s*(?P<rmi_int>\S+)$")

        # RMI_CHASSIS_LOCAL_IP = 10.10.30.6
        p_rmi_ip = re.compile(r"^RMI_CHASSIS_LOCAL_IP\s*=\s*(?P<rmi_ip>\S+)$")

        # RMI_CHASSIS_REMOTE_IP = 10.10.30.7
        p_rmi_ip_remote = re.compile(r"^RMI_CHASSIS_REMOTE_IP\s*=\s*(?P<rmi_remote_ip>\S+)$")

        # CRASHINFO = bootflash:crashinfo_RP_00_00_20200428-005338-IST
        p_crash = re.compile(r"^CRASHINFO\s*=\s*(?P<crash>.*)$")

        # NO_CONSOLE = 1
        p_no_console = re.compile(r"^NO_CONSOLE\s*=\s*(?P<number>\d*)$")

        # BOOT_DEVICE_MODE = meraki
        p_boot_device_mode= re.compile(r"^BOOT_DEVICE_MODE\s*=\s*(?P<boot_device_mode>.*)$")

        # BOARDID = 28755
        p_boardid = re.compile(r"^BOARDID\s*=\s*(?P<boardid>\d*)$")

        # MAC_ADDR = 6C:13:D5:1B:5C:80
        p_mac_addr = re.compile(r"^MAC_ADDR\s*=\s*(?P<mac_addr>\S+)$")

        # MANUAL_BOOT = no
        p_manual_boot = re.compile(r"^MANUAL_BOOT\s*=\s*(?P<manual_boot>\S+)$")

        # MODEL_NUM = C9300-48U
        p_model_num = re.compile(r"^MODEL_NUM\s*=\s*(?P<model_num>\S+)$")

        # MODEL_REVISION_NUM = A0
        p_model_revision_num = re.compile(r"^MODEL_REVISION_NUM\s*=\s*(?P<model_revision_num>\S+)$")

        # MOTHERBOARD_ASSEMBLY_NUM = 73-19919-04
        p_motherboard_assembly_num = re.compile(r"^MOTHERBOARD_ASSEMBLY_NUM\s*=\s*(?P<motherboard_assembly_num>\S+)$")

        # MOTHERBOARD_REVISION_NUM = A0
        p_motherboard_revision_num = re.compile(r"^MOTHERBOARD_REVISION_NUM\s*=\s*(?P<motherboard_revision_num>\S+)$")

        # MOTHERBOARD_SERIAL_NUM = FOC25124Q2U
        p_motherboard_serial_num = re.compile(r"^MOTHERBOARD_SERIAL_NUM\s*=\s*(?P<motherboard_serial_num>\S+)$")

        # ROMMON_AUTOBOOT_ATTEMPT = 0
        p_rommon_autoboot_attempt = re.compile(r"^ROMMON_AUTOBOOT_ATTEMPT\s*=\s*(?P<rommon_autoboot_attempt>\S+)$")

        # SYSTEM_SERIAL_NUM = FOC2514L1HE
        p_system_serial_num = re.compile(r"^SYSTEM_SERIAL_NUM\s*=\s*(?P<system_serial_num>\S+)$")

        # VERSION_ID = V05
        p_version_id = re.compile(r"^VERSION_ID\s*=\s*(?P<version_id>\S+)$")

        # DEVICE_MANAGED_MODE = controller
        p_device_managed_mode = re.compile(r"^\s*DEVICE_MANAGED_MODE\s*=\s+(?P<mode>\S+)$")

        # ABNORMAL_RESET_COUNT=0
        p_abnormal_reset_count = re.compile(r"^ABNORMAL_RESET_COUNT\s*=\s*(?P<abnormal_reset_count>\d+)$")

        romvar_dict = {}

        for line in output.splitlines():
            line = line.strip()
            line = line.replace('"', "")

            # ROMMON variables
            if p_variables.match(line):
                if not romvar_dict.get("rommon_variables"):
                    romvar_dict.update({ "rommon_variables" : {} })
                continue
            # PS1 = rommon ! >
            if p_ps1.match(line):
                match = p_ps1.match(line)
                romvar_dict["rommon_variables"]["ps1"] = match.group("ps1")
            # THRPUT =
            if p_thrput.match(line):
                match = p_thrput.match(line)
                if len(match.group("thrput")):
                    romvar_dict["rommon_variables"]["thrput"] = match.group("thrput")
                continue
            # SR_MGMT_VRF = 0
            if p_mgmt_vrf.match(line):
                match = p_mgmt_vrf.match(line)
                romvar_dict["rommon_variables"]["sr_mgmt_vrf"] = match.group("mgmt_vrf")
                continue
            # REAL_MGMTE_DEV =
            if p_mgmte_dev.match(line):
                match = p_mgmte_dev.match(line)
                romvar_dict["rommon_variables"]["real_mgmte_dev"] = match.group("mgmte_dev")
                continue
            # IP_ADDRESS = 10.19.92.165
            if p_ip.match(line):
                match = p_ip.match(line)
                romvar_dict["rommon_variables"]["ip_address"] = match.group("ip_address")
                continue
            # DEFAULT_GATEWAY = 10.19.92.1
            if p_gateway.match(line):
                match = p_gateway.match(line)
                romvar_dict["rommon_variables"]["default_gateway"] = match.group("gateway")
                continue
            # DEFAULT_GATEWAY = 10.19.92.1
            if p_mask.match(line):
                match = p_mask.match(line)
                romvar_dict["rommon_variables"]["subnet_mask"] = match.group("ip_mask")
                continue
            # DEV_MODE0 = FM5R95WUO0WUATJTQX5I5ZQHLWIT6CWKD513RVT9Q5UQKJVKPDSNU7NR1EDU4QWO
            if p_dev_mode_0.match(line):
                match = p_dev_mode_0.match(line)
                romvar_dict["rommon_variables"]["dev_mode0"] = match.group("mode_0")
                continue
            # DEV_MODE1 = ICQWTUNIEAVS6DH4X7GBV3917N3M1YNMQC5JDW4GM9OLFOZ0B4XCPXGXE596Z71C
            if p_dev_mode_1.match(line):
                match = p_dev_mode_1.match(line)
                romvar_dict["rommon_variables"]["dev_mode1"] = match.group("mode_1")
                continue
            # DEV_MODE2 = 93URXAFOPS1F74TR7LAT9BCAQ5O0LX73WHFMWKRQKZDYFIUCHTPK0SBVEYFZXSAQ
            if p_dev_mode_2.match(line):
                match = p_dev_mode_2.match(line)
                romvar_dict["rommon_variables"]["dev_mode2"] = match.group("mode_2")
                continue
            # DEV_MODE3 = 6LQB4NEFCJ1DYOV929FGLMX3XK710QERFA2SWWCE8C08D5WYLS2X6CXDVQY0CFIO
            if p_dev_mode_3.match(line):
                match = p_dev_mode_3.match(line)
                romvar_dict["rommon_variables"]["dev_mode3"] = match.group("mode_3")
                continue
            # DEV_MODE4 = 1DY4J4L14FCUYC22JDK8YLQQVF0ZPC9BVT7HM75LF4Z319VKS2WE8XWAUV1PEF27
            if p_dev_mode_4.match(line):
                match = p_dev_mode_4.match(line)
                romvar_dict["rommon_variables"]["dev_mode4"] = match.group("mode_4")
                continue
            # DEV_MODE5 = 7YMXKN3FA6X5OEGHUZISA16KC0VAZ51S12JGPMUD3NZCCSTTGZ7O9G58NRUZIKBG
            if p_dev_mode_5.match(line):
                match = p_dev_mode_5.match(line)
                romvar_dict["rommon_variables"]["dev_mode5"] = match.group("mode_5")
                continue
            # DEV_MODE6 = AR1PHFLWRD9ZGDSC0BKKIGWQBUJXX0FGJT3EEU8A7MMUVPLS73FP4WBUIZUS3X76
            if p_dev_mode_6.match(line):
                match = p_dev_mode_6.match(line)
                romvar_dict["rommon_variables"]["dev_mode6"] = match.group("mode_6")
                continue
            # DEV_MODE7 = H5LF3EG7Y2S45ZFEB3GTDSK5M9XLDH4FUU7BQFZ9JI7PRWAHA3HS27JCU4A7PBN1
            if p_dev_mode_7.match(line):
                match = p_dev_mode_7.match(line)
                romvar_dict["rommon_variables"]["dev_mode7"] = match.group("mode_7")
                continue
            # ?=1
            if p_question.match(line):
                continue
            # MCP_STARTUP_TRACEFLAGS = 00000000:00000000
            if p_mcp.match(line):
                match = p_mcp.match(line)
                romvar_dict["rommon_variables"]["mcp_startup_traceflags"] = match.group("tflag")
                continue
            # RET_2_RTS = 23:48:46 Pacific Fri Dec 13 2019
            if p_ret_rts.match(line):
                match = p_ret_rts.match(line)
                if len(match.group("ret_date")):
                    romvar_dict["rommon_variables"]["ret_2_rts"] = match.group("ret_date")
                continue
            # CHASSIS_HA_LOCAL_IP = 10.10.68.54
            if p_chassis_ha_ip.match(line):
                match = p_chassis_ha_ip.match(line)
                romvar_dict["rommon_variables"]["chassis_ha_local_ip"] = match.group("ha_ip")
                continue
            # CHASSIS_HA_REMOTE_IP = 10.10.68.52
            if p_chassis_ha_remote_ip.match(line):
                match = p_chassis_ha_remote_ip.match(line)
                romvar_dict["rommon_variables"]["chassis_ha_remote_ip"] = match.group("remote_ha_ip")
                continue
            # CHASSIS_HA_LOCAL_MASK = 255.255.255.240
            if p_chassis_ha_mask.match(line):
                match = p_chassis_ha_mask.match(line)
                romvar_dict["rommon_variables"]["chassis_ha_local_mask"] = match.group("ha_mask")
                continue
            # SWITCH_PRIORITY = 1
            if p_switch_priority.match(line):
                match = p_switch_priority.match(line)
                romvar_dict["rommon_variables"]["switch_priority"] = int(match.group("priority"))
                continue
            # SWITCH_NUMBER = 2
            if p_switch_number.match(line):
                match = p_switch_number.match(line)
                romvar_dict["rommon_variables"]["switch_number"] = int(match.group("number"))
                continue
            # LICENSE_ACTIVE_LEVEL = adventerprise,all:c9800lk9;
            if p_lic_active.match(line):
                match = p_lic_active.match(line)
                romvar_dict["rommon_variables"]["license_active_level"] = match.group("lic_active")
                continue
            # CONFIG_FILE =
            if p_config_file.match(line):
                match = p_config_file.match(line)
                if len(match.group("config_file")):
                    romvar_dict["rommon_variables"]["config_file"] = match.group("config_file")
                continue
            # BOOTLDR =
            if p_bootldr.match(line):
                match = p_bootldr.match(line)
                if len(match.group("bootldr")):
                    romvar_dict["rommon_variables"]["bootldr"] = match.group("bootldr")
                continue
            # LICENSE_BOOT_LEVEL =
            if p_lic_boot.match(line):
                match = p_lic_boot.match(line)
                if len(match.group("lic_boot")):
                    romvar_dict["rommon_variables"]["license_boot_level"] = match.group("lic_boot")
                continue
            # BOOT = bootflash:packages.conf,12;bootflash:C9800-L-universalk9_wlc.BLD_V173_THROTTLE_LATEST_20200707_003212_2.SSA.bin,12;
            if p_boot.match(line):
                boot_list = []
                match = p_boot.match(line)
                boot_variables = match.group("boot")
                boot_list = filter(None, boot_variables.split(';'))
                romvar_dict["rommon_variables"]["boot"] = list(boot_list)
                continue
            # BSI = 0
            if p_bsi.match(line):
                match = p_bsi.match(line)
                romvar_dict["rommon_variables"]["bsi"] = int(match.group("bsi"))
                continue
            # RET_2_RCALTS =
            if p_rcalts.match(line):
                match = p_rcalts.match(line)
                if len(match.group("rcalts")):
                    romvar_dict["rommon_variables"]["ret_2_rcalts"] = match.group("rcalts")
                continue
            # RANDOM_NUM = 25654861
            if p_random.match(line):
                match = p_random.match(line)
                romvar_dict["rommon_variables"]["random_num"] = int(match.group("random"))
                continue
            # STACK_1_1 = 0_0
            if p_stack.match(line):
                match = p_stack.match(line)
                romvar_dict["rommon_variables"]["stack"] = match.group("stack")
                continue
            # RMI_INTERFACE_NAME = Vlan10
            if p_rmi_int.match(line):
                match = p_rmi_int.match(line)
                romvar_dict["rommon_variables"]["rmi_interface"] = match.group("rmi_int")
                continue
            # RMI_CHASSIS_LOCAL_IP = 10.10.30.6
            if p_rmi_ip.match(line):
                match = p_rmi_ip.match(line)
                romvar_dict["rommon_variables"]["rmi_local_ip"] = match.group("rmi_ip")
                continue
            # RMI_CHASSIS_REMOTE_IP = 10.10.30.7
            if p_rmi_ip_remote.match(line):
                match = p_rmi_ip_remote.match(line)
                romvar_dict["rommon_variables"]["rmi_remote_ip"] = match.group("rmi_remote_ip")
                continue
            # CRASHINFO = bootflash:crashinfo_RP_00_00_20200428-005338-IST
            if p_crash.match(line):
                match = p_crash.match(line)
                romvar_dict["rommon_variables"]["crashinfo"] = match.group("crash")
                continue
            # NO_CONSOLE = 1
            if p_no_console.match(line):
                match = p_no_console.match(line)
                romvar_dict["rommon_variables"]["no_console"] = int(match.group("number"))
                continue
            # BOOT_DEVICE_MODE = meraki
            if p_boot_device_mode.match(line):
                match = p_boot_device_mode.match(line)
                romvar_dict["rommon_variables"]["boot_device_mode"] = match.group("boot_device_mode")
                continue
            # BOARDID = 28755
            if p_boardid.match(line):
                match = p_boardid.match(line)
                romvar_dict["rommon_variables"]["boardid"] = int(match.group("boardid"))
                continue
            # MAC_ADDR = 6C:13:D5:1B:5C:80
            if p_mac_addr.match(line):
                match = p_mac_addr.match(line)
                romvar_dict["rommon_variables"]["mac_addr"] = match.group("mac_addr")
                continue
            # MANUAL_BOOT = no
            if p_manual_boot.match(line):
                match = p_manual_boot.match(line)
                romvar_dict["rommon_variables"]["manual_boot"] = match.group("manual_boot")
                continue
           # MODEL_NUM = C9300-48U
            if p_model_num.match(line):
                match = p_model_num.match(line)
                romvar_dict["rommon_variables"]["model_num"] = match.group("model_num")
                continue
            # MODEL_REVISION_NUM = A0
            if p_model_revision_num.match(line):
                match = p_model_revision_num.match(line)
                romvar_dict["rommon_variables"]["model_revision_num"] = match.group("model_revision_num")
                continue
           # MOTHERBOARD_ASSEMBLY_NUM = 73-19919-04
            if p_motherboard_assembly_num.match(line):
                match = p_motherboard_assembly_num.match(line)
                romvar_dict["rommon_variables"]["motherboard_assembly_num"] = match.group("motherboard_assembly_num")
                continue
            # MOTHERBOARD_REVISION_NUM = A0
            if p_motherboard_revision_num.match(line):
                match = p_motherboard_revision_num.match(line)
                romvar_dict["rommon_variables"]["motherboard_revision_num"] = match.group("motherboard_revision_num")
                continue
            # MOTHERBOARD_SERIAL_NUM = FOC25124Q2U
            if p_motherboard_serial_num.match(line):
                match = p_motherboard_serial_num.match(line)
                romvar_dict["rommon_variables"]["motherboard_serial_num"] = match.group("motherboard_serial_num")
                continue
           # ROMMON_AUTOBOOT_ATTEMPT = 0
            if p_rommon_autoboot_attempt.match(line):
                match = p_rommon_autoboot_attempt.match(line)
                romvar_dict["rommon_variables"]["rommon_autoboot_attempt"] = int(match.group("rommon_autoboot_attempt"))
                continue
            # SYSTEM_SERIAL_NUM = FOC2514L1HE
            if p_system_serial_num.match(line):
                match = p_system_serial_num.match(line)
                romvar_dict["rommon_variables"]["system_serial_num"] = match.group("system_serial_num")
                continue
            # VERSION_ID = V05
            if p_version_id.match(line):
                match = p_version_id.match(line)
                romvar_dict["rommon_variables"]["version_id"] = match.group("version_id")
                continue
            # DEVICE_MANAGED_MODE = controller
            if p_device_managed_mode.match(line):
                match = p_device_managed_mode.match(line)
                romvar_dict["rommon_variables"]["device_managed_mode"] = match.group("mode")
                continue

            if p_abnormal_reset_count.match(line):
                match = p_abnormal_reset_count.match(line)
                romvar_dict["rommon_variables"]["abnormal_reset_count"] = int(match.group("abnormal_reset_count"))
                continue

        return romvar_dict

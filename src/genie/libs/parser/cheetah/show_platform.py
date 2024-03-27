"""
CHEETAH parsers for the following show commands:

    * show version

"""
# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowVersionSchema(MetaParser):

    """
    Schema for
        * show version
    """

    schema = {
        'version': {
            'model_number': str,
            'top_assembly_serial_number': str,
            Optional('radio_driver_version'): str,
            'radio_fw_version': str,
            'ap_running_image': str,
            'primary_boot_image': str,
            'backup_boot_image': str,
            'chassis': str,
            'main_mem': str,
            'os': str,
            'processor_type': str,
            Optional('bootloader_version'): str,
            Optional('bootloader_timestamp'): str,
            'multigigabit_eth_intf': int,
            Optional('gigabit_eth_intf'): int,
            '80211_radios': int,
            Optional('uptime'): str,
            Optional('last_reload_time'): str,
            Optional('last_reload_reason'): str,
            'nss_fw_version': str,
            'primary_boot_image_hash': str,
            'backup_boot_image_hash': str,
            'base_ethernet_mac': str,
            'part_number': str,
            'pcb_serial_number': str,
            'top_assembly_part_number': str,
            'top_revision_number': str,
            'processor_board_id': str
        }
    }

# ====================
# Parser for:
#  * 'show version'
# ====================
class ShowVersion(ShowVersionSchema):

    """
    Parser for
        * show version
    """

    cli_command = "show version"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # Cisco AP Software, (ap3g3), [lnx15:/6885/label/ci_barbados]
        p0 = re.compile(r'Cisco AP Software.*?')
        # BOOTLDR: U-Boot boot loader Version 2013.01-ge1c49d93a (Jul 28 2023 - 09:08:14)
        p1 = re.compile(r'BOOTLDR:\s+U\-Boot\s+boot\s+loader\s+Version\s+(?P<bootloader_version>\S+)\s+\((?P<bootloader_timestamp>.*?)\)$')
        # AP5C5A.C752.01DC uptime is 0 days, 8 hours, 24 minutes
        p1_1 = re.compile(r'.*?\s+uptime\s+is\s+(?P<uptime>.*?)$')
        # Last reload time   : Tue Jan 23 19:26:02 UTC 2024
        p1_2 = re.compile(r'Last\s+reload\s+time\s+:\s+(?P<last_reload_time>.*?)$')
        # Last reload reason : Image Upgrade
        p1_3 = re.compile(r'Last\s+reload\s+reason\s+:\s+(?P<last_reload_reason>.*?)$')
        # cisco AIR-AP4800-D-K9 ARMv7 Processor rev 1 (v7l) with 1028320/528608K bytes of memory.
        p1_4 = re.compile(r'^(C|c)isco +(?P<chassis>[a-zA-Z0-9\-\/\+]+) +(?P<processor_type>\w+) +(.*?)with +(?P<main_mem>[0-9]+)\/[0-9]+[kK]')
        # Processor board ID FGL2325A4YP
        p1_5 = re.compile(r'Processor\s+board\s+ID\s+(?P<processor_board_id>\S+)$')
        # AP Running Image     : 17.15.0.10
        p1_6 = re.compile(r'AP\s+Running\s+Image\s+:\s+(?P<ap_running_image>\S+)$')
        # Primary Boot Image   : 17.15.0.10
        p1_7 = re.compile(r'Primary\s+Boot\s+Image\s+:\s+(?P<primary_boot_image>\S+)$')
        # Backup Boot Image    : 17.15.0.8
        p1_8 = re.compile(r'Backup\s+Boot\s+Image\s+:\s+(?P<backup_boot_image>\S+)$')
        # Primary Boot Image Hash: 8084019f7d71c36ca841f23b8089b7f3e3008cf360da0b49c30c1b468b7e090fef649c1ac7f7dff564f023a795f47ede202024fe7e2a1ae229d69e9ece865ddc
        p1_9 = re.compile(r'Primary\s+Boot\s+Image\s+Hash:\s+(?P<primary_boot_image_hash>\S+)$')
        # Backup  Boot Image Hash: 6b563a9e688f24196d72661309291367bb52e49683e3f6b98feba06ccf22ea03a2ec0b194c5e41f7166138bc3a0fe0d7a9aa1d005295fb29669253eea08a64ba
        p1_10 = re.compile(r'Backup\s+Boot\s+Image\s+Hash:\s+(?P<backup_boot_image_hash>\S+)$')
        # 1 Multigigabit Ethernet interfaces
        # 1 Gigabit Ethernet interfaces
        p1_11 = re.compile(r'^(?P<number_of_ports>\d+) (?P<interface>.+) Ethernet interfaces$')
        # 3 802.11 Radios
        p1_12 = re.compile(r'(?P<number_of_ports>\d+) 802.11 Radios$')
        # Radio Driver version : 9.0.5.5-W8964
        p1_13 = re.compile(r'Radio\s+Driver\s+version\s+:\s+(?P<radio_driver_version>.+)$')
        # Radio FW version : 9.1.8.1
        p1_14 = re.compile(r'Radio\s+FW\s+version\s+:\s+(?P<radio_fw_version>.+)$')
        # NSS FW version : 2.4.32
        p1_15 = re.compile(r'NSS\s+FW\s+version\s+:\s+(?P<nss_fw_version>.+)$')
        # Base ethernet MAC Address            : 5C:5A:C7:52:01:DC
        p1_16 = re.compile(r'Base\s+ethernet\s+MAC\s+Address\s+:\s+(?P<base_ethernet_mac>\S+)$')
        # Part Number                          : 73-018776-02
        p1_17 = re.compile(r'Part\s+Number\s+:\s+(?P<part_number>\S+)$')
        # PCB Serial Number                    : FOC23206BHY
        p1_18 = re.compile(r'PCB\s+Serial\s+Number\s+:\s+(?P<pcb_serial_number>\S+)$')
        # Top Assembly Part Number             : 068-100533-01
        p1_19 = re.compile(r'Top\s+Assembly\s+Part\s+Number\s+:\s+(?P<top_assembly_part_number>\S+)$')
        # Top Assembly Serial Number           : FGL2325A4YP
        p1_20 = re.compile(r'Top\s+Assembly\s+Serial\s+Number\s+:\s+(?P<top_assembly_serial_number>\S+)$')
        # Top Revision Number                  : A0
        p1_21 = re.compile(r'Top\s+Revision\s+Number\s+:\s+(?P<top_revision_number>\S+)$')
        # Product/Model Number                 : AIR-AP4800-D-K9
        p1_22 = re.compile(r'Product/Model\s+Number\s+:\s+(?P<model_number>\S+)\s*$')

        for line in output.splitlines():
            line = line.strip()

            # Cisco AP Software, (ap3g3), [lnx15:/6885/label/ci_barbados]
            m = p0.match(line)
            if m:
                ret_dict['os'] = 'cheetah'
                continue

            # BOOTLDR: U-Boot boot loader Version 2013.01-ge1c49d93a (Jul 28 2023 - 09:08:14)
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['bootloader_version'] = match_dict['bootloader_version']
                ret_dict['bootloader_timestamp'] = match_dict['bootloader_timestamp']
                continue

            # AP5C5A.C752.01DC uptime is 0 days, 8 hours, 24 minutes
            m = p1_1.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['uptime'] = match_dict['uptime']
                continue

            # Last reload time   : Tue Jan 23 19:26:02 UTC 2024
            m = p1_2.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['last_reload_time'] = match_dict['last_reload_time']
                continue

            # Last reload reason : Image Upgrade
            m = p1_3.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['last_reload_reason'] = match_dict['last_reload_reason']
                continue

            # cisco AIR-AP4800-D-K9 ARMv7 Processor rev 1 (v7l) with 1028320/528608K bytes of memory.
            m = p1_4.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['chassis'] = match_dict['chassis']
                ret_dict['processor_type'] = match_dict['processor_type']
                ret_dict['main_mem'] = match_dict['main_mem']
                continue

            # Processor board ID FGL2325A4YP
            m = p1_5.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['processor_board_id'] = match_dict['processor_board_id']
                continue

            # AP Running Image     : 17.15.0.10
            m = p1_6.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['ap_running_image'] = match_dict['ap_running_image']
                continue

            # Primary Boot Image   : 17.15.0.10
            m = p1_7.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['primary_boot_image'] = match_dict['primary_boot_image']
                continue

            # Backup Boot Image    : 17.15.0.8
            m = p1_8.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['backup_boot_image'] = match_dict['backup_boot_image']
                continue

            # Primary Boot Image Hash: 8084019f7d71c36ca841f23b8089b7f3e3008cf360da0b49c30c1b468b7e090fef649c1ac7f7dff564f023a795f47ede202024fe7e2a1ae229d69e9ece865ddc
            m = p1_9.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['primary_boot_image_hash'] = match_dict['primary_boot_image_hash']
                continue

            # Backup  Boot Image Hash: 6b563a9e688f24196d72661309291367bb52e49683e3f6b98feba06ccf22ea03a2ec0b194c5e41f7166138bc3a0fe0d7a9aa1d005295fb29669253eea08a64ba
            m = p1_10.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['backup_boot_image_hash'] = match_dict['backup_boot_image_hash']
                continue

            # 1 Multigigabit Ethernet interfaces
            # 1 Gigabit Ethernet interfaces
            m = p1_11.match(line)
            if m:
                interface = m.groupdict()['interface'].lower() + '_eth_intf'
                ret_dict[interface] = int(m.groupdict()['number_of_ports'])
                continue

            # 3 802.11 Radios
            m = p1_12.match(line)
            if m:
                ret_dict["80211_radios"] = int(m.groupdict()['number_of_ports'])
                continue

            # Radio Driver version : 9.0.5.5-W8964
            m = p1_13.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['radio_driver_version'] = match_dict['radio_driver_version']
                continue

            # Radio FW version : 9.1.8.1
            m = p1_14.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['radio_fw_version'] = match_dict['radio_fw_version']
                continue

            # NSS FW version : 2.4.32
            m = p1_15.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['nss_fw_version'] = match_dict['nss_fw_version']
                continue

            # Base ethernet MAC Address            : 5C:5A:C7:52:01:DC
            m = p1_16.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['base_ethernet_mac'] = match_dict['base_ethernet_mac']
                continue

            # Part Number                          : 73-018776-02
            m = p1_17.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['part_number'] = match_dict['part_number']
                continue

            # PCB Serial Number                    : FOC23206BHY
            m = p1_18.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['pcb_serial_number'] = match_dict['pcb_serial_number']
                continue

            # Top Assembly Part Number             : 068-100533-01
            m = p1_19.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['top_assembly_part_number'] = match_dict['top_assembly_part_number']
                continue

            # Top Assembly Serial Number           : FGL2325A4YP
            m = p1_20.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['top_assembly_serial_number'] = match_dict['top_assembly_serial_number']
                continue

            # Top Revision Number                  : A0
            m = p1_21.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['top_revision_number'] = match_dict['top_revision_number']
                continue

            # Product/Model Number                 : AIR-AP4800-D-K9
            m = p1_22.match(line)
            if m:
                match_dict = m.groupdict()
                ret_dict['model_number'] = match_dict['model_number']
                continue

        return {'version': ret_dict}
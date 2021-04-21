""" Parsers for NXOS ACI """

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowFirmwareUpgradeStatusSchema(MetaParser):
    """ Schema for
        * 'show firmware upgrade status'
        * 'show firmware upgrade status switch-group {switch_group}'
        * 'show firmware upgrade status controller-group'
    """

    schema = {
        'node': {
            Any(): {
                'pod': int,
                'current_firmware': str,
                Optional('target_firmware'): str,
                'status': str,
                Optional('upgrade_progress_percentage'): int,
                Optional('download_status'): str,
                Optional('download_progress_percentage'): int,
                Optional('last_firmware_install_date'): str
            }
        }
    }


class ShowFirmwareUpgradeStatus(ShowFirmwareUpgradeStatusSchema):
    """ Parser class for:
        * 'show firmware upgrade status'
        * 'show firmware upgrade status switch-group {switch_group}'
    """

    cli_command = [
        'show firmware upgrade status',
        'show firmware upgrade status switch-group {switch_group}'
    ]

    def cli(self, switch_group=None, output=None):
        if output is None:
            if switch_group:
                cmd = self.cli_command[1].format(switch_group=switch_group)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)
        # ----------  ----------  --------------------  --------------------  -------------------------  --------------------

        # 1           1           apic-4.2(4o)                                success                    100
        # 1           101         unknown               unknown               node unreachable           -
        # 1           102         n9000-14.2(4q)                              not scheduled              0
        # 1           201         unknown               unknown               node unreachable           -

        #  Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)   Download-Status            Download-Progress(%)
        #  ----------  ----------  --------------------  --------------------  -------------------------  --------------------  -------------------------  --------------------

        #  1           101         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
        #  1           107         n9000-15.0(0.138)     n9000-15.0(0.144)     waiting in queue           0                     downloaded                 100                 
        #  1           108         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
        #  1           112         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
        #  1           113         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded       

        p1 = re.compile(r"^\s*(?P<pod>\d+)  +(?P<node>\d+)  +(?P<current_firmware>\S+)  +(?:(?P<target_firmware>\S+)?  +)?(?P<status>\w+(?: \w+)*\w)  +(?P<upgrade_progress_percentage>\d+|-)(?: *(?:(?P<download_status>\S+) *(?P<download_progress_percentage>\d+)?)?)")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()

                node_dict = ret_dict.setdefault('node', {}).setdefault(int(groups['node']), {})
                node_dict.update({'pod': int(groups['pod'])})
                node_dict.update({'current_firmware': groups['current_firmware']})
                node_dict.update({'status': groups['status']})

                if 'target_firmware' in groups and groups['target_firmware']:
                    node_dict.update({'target_firmware': groups['target_firmware']})

                if groups['upgrade_progress_percentage'] != '-':
                    node_dict.update({'upgrade_progress_percentage': int(groups['upgrade_progress_percentage'])})

                if 'download_status' in groups and groups['download_status']:
                    node_dict.update({'download_status': groups['download_status']})

                if 'download_progress_percentage' in groups and groups['download_progress_percentage']:
                    node_dict.update({'download_progress_percentage': int(groups['download_progress_percentage'])})

                if 'last_firmware_install_date' in groups and groups['last_firmware_install_date']:
                    node_dict.update({'last_firmware_install_date': groups['last_firmware_install_date']})

        return ret_dict


class ShowFirmwareUpgradeStatusControllerGroup(ShowFirmwareUpgradeStatusSchema):
    """ Parser class for
        * 'show firmware upgrade status controller-group'
    """

    cli_command = ['show firmware upgrade status controller-group']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)     Last-Firmware-Install-Date
        # ----------  ----------  --------------------  --------------------  -------------------------  --------------------  ------------------------------

        # 1           1           apic-5.0(1k)          apic-5.0(1k)          success                    100                   2020-11-17T18:43:57.000+00:00
        p1 = re.compile(r"^(?P<pod>\d+)  +(?P<node>\d+)  +(?P<current_firmware>\S+)  +(?:(?P<target_firmware>\S+)  +)?(?P<status>\w+(?: \w+)*\w)  +(?P<upgrade_progress_percentage>\d+|-)  +(?P<last_firmware_install_date>\S+)")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)     Last-Firmware-Install-Date
            # ----------  ----------  --------------------  --------------------  -------------------------  --------------------  ------------------------------

            # 1           1           apic-5.0(1k)          apic-5.0(1k)          success                    100                   2020-11-17T18:43:57.000+00:00
            m = p1.match(line)
            if m:
                groups = m.groupdict()

                node_dict = ret_dict.setdefault('node', {}).setdefault(int(groups['node']), {})
                node_dict.update({'pod': int(groups['pod'])})
                node_dict.update({'current_firmware': groups['current_firmware']})
                node_dict.update({'status': groups['status']})

                if 'target_firmware' in groups and groups['target_firmware']:
                    node_dict.update({'target_firmware': groups['target_firmware']})

                if groups['upgrade_progress_percentage'] != '-':
                    node_dict.update({'upgrade_progress_percentage': int(groups['upgrade_progress_percentage'])})

                if 'last_firmware_install_date' in groups and groups['last_firmware_install_date']:
                    node_dict.update({'last_firmware_install_date': groups['last_firmware_install_date']})

        return ret_dict


class ShowFirmwareRepositorySchema(MetaParser):
    """ Schema for
        * 'show firmware repository'
    """

    schema = {
        'name': {
            Any(): {
                'version': {
                    Any(): {
                        'type': str,
                        'size': float
                    }
                }
            }
        }
    }


class ShowFirmwareRepository(ShowFirmwareRepositorySchema):
    """ Parser class for
        * 'show firmware repository'
    """

    cli_command = ['show firmware repository']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        #  aci-catalog-dk10.121.8.2.bin                catalog     70.8(2)        0.129
        #  aci-apic-dk9.5.0.1k.bin                   controller  5.0(1k)        6266.102
        #  aci-catalog-dk10.121.7.4.bin                catalog     70.7(4)        0.128
        p1 = re.compile(r"^(?P<name>\S+) +(?P<type>\S+) +(?P<version>\S+) +(?P<size>[\d\.]+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()

                version_dict = ret_dict.setdefault('name', {}).\
                    setdefault(groups['name'], {}).setdefault('version', {}).\
                    setdefault(groups['version'], {})

                version_dict.update({'type': groups['type']})
                version_dict.update({'size': float(groups['size'])})

        return ret_dict

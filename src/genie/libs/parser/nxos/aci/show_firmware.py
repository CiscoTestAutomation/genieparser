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

        # 1           1           apic-4.2(4o)                                success                    100                downloaded       100
        # 1           101         unknown               unknown               node unreachable           -                  downloaded     100
        # 1           101         unknown               unknown               node unreachable           -
        p1 = re.compile(r"^(?P<pod>\d+)  +(?P<node>\d+)  +(?P<current_firmware>\S+)  +(?:(?P<target_firmware>\S+)  +)?(?P<status>\w+(?: \w+)*\w)  +(?P<upgrade_progress_percentage>\d+|-)(?:  +(?:(?P<download_status>\S+)  +(?P<download_progress_percentage>\d+)|(?P<last_firmware_install_date>\S+)))?")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 1           1           apic-4.2(4o)                                success                    100                downloaded       100
            # 1           101         unknown               unknown               node unreachable           -                  downloaded     100
            # 1           101         unknown               unknown               node unreachable           -
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


class ShowFirmwareUpgradeStatusControllerGroup(ShowFirmwareUpgradeStatus):
    """ Parser class for
        * 'show firmware upgrade status controller-group'
    """

    cli_command = ['show firmware upgrade status controller-group']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        return super().cli(output=output)


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

        #  aci-catalog-dk9.70.8.2.bin                catalog     70.8(2)        0.129
        #  aci-apic-dk9.5.0.1k.bin                   controller  5.0(1k)        6266.102
        #  aci-catalog-dk9.70.7.4.bin                catalog     70.7(4)        0.128
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

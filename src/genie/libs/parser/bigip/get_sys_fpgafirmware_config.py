# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/fpga/firmware-config' resources
# =============================================


class SysFpgaFirmwareconfigSchema(MetaParser):

    schema = {}


class SysFpgaFirmwareconfig(SysFpgaFirmwareconfigSchema):
    """ To F5 resource for /mgmt/tm/sys/fpga/firmware-config
    """

    cli_command = "/mgmt/tm/sys/fpga/firmware-config"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

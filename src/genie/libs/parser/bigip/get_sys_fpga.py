# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/fpga' resources
# =============================================


class SysFpgaSchema(MetaParser):

    schema = {}


class SysFpga(SysFpgaSchema):
    """ To F5 resource for /mgmt/tm/sys/fpga
    """

    cli_command = "/mgmt/tm/sys/fpga"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

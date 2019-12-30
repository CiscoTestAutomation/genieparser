# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/cpu' resources
# =============================================


class SysCpuSchema(MetaParser):

    schema = {}


class SysCpu(SysCpuSchema):
    """ To F5 resource for /mgmt/tm/sys/cpu
    """

    cli_command = "/mgmt/tm/sys/cpu"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

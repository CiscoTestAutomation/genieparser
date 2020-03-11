# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/raid/bay' resources
# =============================================


class SysRaidBaySchema(MetaParser):

    schema = {}


class SysRaidBay(SysRaidBaySchema):
    """ To F5 resource for /mgmt/tm/sys/raid/bay
    """

    cli_command = "/mgmt/tm/sys/raid/bay"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

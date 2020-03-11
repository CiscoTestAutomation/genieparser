# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/raid/disk' resources
# =============================================


class SysRaidDiskSchema(MetaParser):

    schema = {}


class SysRaidDisk(SysRaidDiskSchema):
    """ To F5 resource for /mgmt/tm/sys/raid/disk
    """

    cli_command = "/mgmt/tm/sys/raid/disk"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

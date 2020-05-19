# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/disk/logical-disk' resources
# =============================================


class SysDiskLogicaldiskSchema(MetaParser):

    schema = {}


class SysDiskLogicaldisk(SysDiskLogicaldiskSchema):
    """ To F5 resource for /mgmt/tm/sys/disk/logical-disk
    """

    cli_command = "/mgmt/tm/sys/disk/logical-disk"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

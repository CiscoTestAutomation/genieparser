# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/dynad/key' resources
# =============================================


class SysDynadKeySchema(MetaParser):

    schema = {}


class SysDynadKey(SysDynadKeySchema):
    """ To F5 resource for /mgmt/tm/sys/dynad/key
    """

    cli_command = "/mgmt/tm/sys/dynad/key"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

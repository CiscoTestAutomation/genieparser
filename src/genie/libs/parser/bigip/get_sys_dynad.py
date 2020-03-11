# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/dynad' resources
# =============================================


class SysDynadSchema(MetaParser):

    schema = {}


class SysDynad(SysDynadSchema):
    """ To F5 resource for /mgmt/tm/sys/dynad
    """

    cli_command = "/mgmt/tm/sys/dynad"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

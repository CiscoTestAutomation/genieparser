# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/dynad/settings' resources
# =============================================


class SysDynadSettingsSchema(MetaParser):

    schema = {}


class SysDynadSettings(SysDynadSettingsSchema):
    """ To F5 resource for /mgmt/tm/sys/dynad/settings
    """

    cli_command = "/mgmt/tm/sys/dynad/settings"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

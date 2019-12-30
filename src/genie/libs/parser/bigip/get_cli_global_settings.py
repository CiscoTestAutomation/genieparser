# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/global-settings' resources
# =============================================


class CliGlobalsettingsSchema(MetaParser):

    schema = {}


class CliGlobalsettings(CliGlobalsettingsSchema):
    """ To F5 resource for /mgmt/tm/cli/global-settings
    """

    cli_command = "/mgmt/tm/cli/global-settings"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

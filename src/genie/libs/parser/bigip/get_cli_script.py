# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/script' resources
# =============================================


class CliScriptSchema(MetaParser):

    schema = {}


class CliScript(CliScriptSchema):
    """ To F5 resource for /mgmt/tm/cli/script
    """

    cli_command = "/mgmt/tm/cli/script"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

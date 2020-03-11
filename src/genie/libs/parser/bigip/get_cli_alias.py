# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/alias' resources
# =============================================


class CliAliasSchema(MetaParser):

    schema = {}


class CliAlias(CliAliasSchema):
    """ To F5 resource for /mgmt/tm/cli/alias
    """

    cli_command = "/mgmt/tm/cli/alias"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

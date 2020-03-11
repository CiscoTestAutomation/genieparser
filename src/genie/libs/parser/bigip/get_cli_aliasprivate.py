# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/alias/private' resources
# =============================================


class CliAliasPrivateSchema(MetaParser):

    schema = {}


class CliAliasPrivate(CliAliasPrivateSchema):
    """ To F5 resource for /mgmt/tm/cli/alias/private
    """

    cli_command = "/mgmt/tm/cli/alias/private"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

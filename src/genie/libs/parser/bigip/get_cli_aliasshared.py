# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/alias/shared' resources
# =============================================


class CliAliasSharedSchema(MetaParser):

    schema = {}


class CliAliasShared(CliAliasSharedSchema):
    """ To F5 resource for /mgmt/tm/cli/alias/shared
    """

    cli_command = "/mgmt/tm/cli/alias/shared"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

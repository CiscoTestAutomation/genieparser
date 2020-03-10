# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/version' resources
# =============================================


class CliVersionSchema(MetaParser):

    schema = {}


class CliVersion(CliVersionSchema):
    """ To F5 resource for /mgmt/tm/cli/version
    """

    cli_command = "/mgmt/tm/cli/version"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

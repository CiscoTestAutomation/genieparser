# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/history' resources
# =============================================


class CliHistorySchema(MetaParser):

    schema = {}


class CliHistory(CliHistorySchema):
    """ To F5 resource for /mgmt/tm/cli/history
    """

    cli_command = "/mgmt/tm/cli/history"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cli/preference' resources
# =============================================


class CliPreferenceSchema(MetaParser):

    schema = {}


class CliPreference(CliPreferenceSchema):
    """ To F5 resource for /mgmt/tm/cli/preference
    """

    cli_command = "/mgmt/tm/cli/preference"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

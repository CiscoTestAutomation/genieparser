# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/bot-signatures/installations' resources
# =============================================


class Live_updateBotsignaturesInstallationsSchema(MetaParser):

    schema = {}


class Live_updateBotsignaturesInstallations(
    Live_updateBotsignaturesInstallationsSchema
):
    """ To F5 resource for /mgmt/tm/live-update/bot-signatures/installations
    """

    cli_command = "/mgmt/tm/live-update/bot-signatures/installations"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

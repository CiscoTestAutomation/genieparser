# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/bot-signatures/update-files' resources
# =============================================


class Live_updateBotsignaturesUpdatefilesSchema(MetaParser):

    schema = {}


class Live_updateBotsignaturesUpdatefiles(
    Live_updateBotsignaturesUpdatefilesSchema
):
    """ To F5 resource for /mgmt/tm/live-update/bot-signatures/update-files
    """

    cli_command = "/mgmt/tm/live-update/bot-signatures/update-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

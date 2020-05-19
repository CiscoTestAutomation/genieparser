# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/browser-challenges/update-files' resources
# =============================================


class Live_updateBrowserchallengesUpdatefilesSchema(MetaParser):

    schema = {}


class Live_updateBrowserchallengesUpdatefiles(
    Live_updateBrowserchallengesUpdatefilesSchema
):
    """ To F5 resource for /mgmt/tm/live-update/browser-challenges/update-files
    """

    cli_command = "/mgmt/tm/live-update/browser-challenges/update-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

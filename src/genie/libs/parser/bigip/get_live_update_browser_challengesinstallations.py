# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/browser-challenges/installations' resources
# =============================================


class Live_updateBrowserchallengesInstallationsSchema(MetaParser):

    schema = {}


class Live_updateBrowserchallengesInstallations(
    Live_updateBrowserchallengesInstallationsSchema
):
    """ To F5 resource for /mgmt/tm/live-update/browser-challenges/installations
    """

    cli_command = "/mgmt/tm/live-update/browser-challenges/installations"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

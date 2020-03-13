# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/browser-challenges' resources
# =============================================


class Live_updateBrowserchallengesSchema(MetaParser):

    schema = {}


class Live_updateBrowserchallenges(Live_updateBrowserchallengesSchema):
    """ To F5 resource for /mgmt/tm/live-update/browser-challenges
    """

    cli_command = "/mgmt/tm/live-update/browser-challenges"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

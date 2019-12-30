# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/browser-challenges/availability' resources
# =============================================


class Live_updateBrowserchallengesAvailabilitySchema(MetaParser):

    schema = {}


class Live_updateBrowserchallengesAvailability(
    Live_updateBrowserchallengesAvailabilitySchema
):
    """ To F5 resource for /mgmt/tm/live-update/browser-challenges/availability
    """

    cli_command = "/mgmt/tm/live-update/browser-challenges/availability"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

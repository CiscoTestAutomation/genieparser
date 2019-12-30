# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/bot-signatures/availability' resources
# =============================================


class Live_updateBotsignaturesAvailabilitySchema(MetaParser):

    schema = {}


class Live_updateBotsignaturesAvailability(
    Live_updateBotsignaturesAvailabilitySchema
):
    """ To F5 resource for /mgmt/tm/live-update/bot-signatures/availability
    """

    cli_command = "/mgmt/tm/live-update/bot-signatures/availability"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

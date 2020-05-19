# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/server-technologies/availability' resources
# =============================================


class Live_updateServertechnologiesAvailabilitySchema(MetaParser):

    schema = {}


class Live_updateServertechnologiesAvailability(
    Live_updateServertechnologiesAvailabilitySchema
):
    """ To F5 resource for /mgmt/tm/live-update/server-technologies/availability
    """

    cli_command = "/mgmt/tm/live-update/server-technologies/availability"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

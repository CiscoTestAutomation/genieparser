# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/threat-campaigns/availability' resources
# =============================================


class Live_updateThreatcampaignsAvailabilitySchema(MetaParser):

    schema = {}


class Live_updateThreatcampaignsAvailability(
    Live_updateThreatcampaignsAvailabilitySchema
):
    """ To F5 resource for /mgmt/tm/live-update/threat-campaigns/availability
    """

    cli_command = "/mgmt/tm/live-update/threat-campaigns/availability"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

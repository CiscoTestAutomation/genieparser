# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/threat-campaigns' resources
# =============================================


class Live_updateThreatcampaignsSchema(MetaParser):

    schema = {}


class Live_updateThreatcampaigns(Live_updateThreatcampaignsSchema):
    """ To F5 resource for /mgmt/tm/live-update/threat-campaigns
    """

    cli_command = "/mgmt/tm/live-update/threat-campaigns"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

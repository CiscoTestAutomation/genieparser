# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/threat-campaigns/installations' resources
# =============================================


class Live_updateThreatcampaignsInstallationsSchema(MetaParser):

    schema = {}


class Live_updateThreatcampaignsInstallations(
    Live_updateThreatcampaignsInstallationsSchema
):
    """ To F5 resource for /mgmt/tm/live-update/threat-campaigns/installations
    """

    cli_command = "/mgmt/tm/live-update/threat-campaigns/installations"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

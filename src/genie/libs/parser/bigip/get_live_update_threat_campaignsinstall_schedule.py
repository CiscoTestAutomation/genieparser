# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/threat-campaigns/install-schedule' resources
# =============================================


class Live_updateThreatcampaignsInstallscheduleSchema(MetaParser):

    schema = {}


class Live_updateThreatcampaignsInstallschedule(
    Live_updateThreatcampaignsInstallscheduleSchema
):
    """ To F5 resource for /mgmt/tm/live-update/threat-campaigns/install-schedule
    """

    cli_command = "/mgmt/tm/live-update/threat-campaigns/install-schedule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/server-technologies/install-schedule' resources
# =============================================


class Live_updateServertechnologiesInstallscheduleSchema(MetaParser):

    schema = {}


class Live_updateServertechnologiesInstallschedule(
    Live_updateServertechnologiesInstallscheduleSchema
):
    """ To F5 resource for /mgmt/tm/live-update/server-technologies/install-schedule
    """

    cli_command = "/mgmt/tm/live-update/server-technologies/install-schedule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

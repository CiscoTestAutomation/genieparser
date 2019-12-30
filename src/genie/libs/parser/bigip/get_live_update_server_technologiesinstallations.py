# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/server-technologies/installations' resources
# =============================================


class Live_updateServertechnologiesInstallationsSchema(MetaParser):

    schema = {}


class Live_updateServertechnologiesInstallations(
    Live_updateServertechnologiesInstallationsSchema
):
    """ To F5 resource for /mgmt/tm/live-update/server-technologies/installations
    """

    cli_command = "/mgmt/tm/live-update/server-technologies/installations"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

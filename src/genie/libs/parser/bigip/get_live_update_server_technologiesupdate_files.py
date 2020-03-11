# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/server-technologies/update-files' resources
# =============================================


class Live_updateServertechnologiesUpdatefilesSchema(MetaParser):

    schema = {}


class Live_updateServertechnologiesUpdatefiles(
    Live_updateServertechnologiesUpdatefilesSchema
):
    """ To F5 resource for /mgmt/tm/live-update/server-technologies/update-files
    """

    cli_command = "/mgmt/tm/live-update/server-technologies/update-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

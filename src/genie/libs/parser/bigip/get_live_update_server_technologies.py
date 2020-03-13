# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/server-technologies' resources
# =============================================


class Live_updateServertechnologiesSchema(MetaParser):

    schema = {}


class Live_updateServertechnologies(Live_updateServertechnologiesSchema):
    """ To F5 resource for /mgmt/tm/live-update/server-technologies
    """

    cli_command = "/mgmt/tm/live-update/server-technologies"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

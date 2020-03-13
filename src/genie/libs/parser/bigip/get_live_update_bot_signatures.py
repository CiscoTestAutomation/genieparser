# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/bot-signatures' resources
# =============================================


class Live_updateBotsignaturesSchema(MetaParser):

    schema = {}


class Live_updateBotsignatures(Live_updateBotsignaturesSchema):
    """ To F5 resource for /mgmt/tm/live-update/bot-signatures
    """

    cli_command = "/mgmt/tm/live-update/bot-signatures"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

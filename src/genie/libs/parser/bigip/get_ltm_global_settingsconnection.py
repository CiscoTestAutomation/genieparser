# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/global-settings/connection' resources
# =============================================


class LtmGlobalsettingsConnectionSchema(MetaParser):

    schema = {}


class LtmGlobalsettingsConnection(LtmGlobalsettingsConnectionSchema):
    """ To F5 resource for /mgmt/tm/ltm/global-settings/connection
    """

    cli_command = "/mgmt/tm/ltm/global-settings/connection"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

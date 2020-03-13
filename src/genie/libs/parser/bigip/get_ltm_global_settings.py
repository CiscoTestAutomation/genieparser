# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/global-settings' resources
# =============================================


class LtmGlobalsettingsSchema(MetaParser):

    schema = {}


class LtmGlobalsettings(LtmGlobalsettingsSchema):
    """ To F5 resource for /mgmt/tm/ltm/global-settings
    """

    cli_command = "/mgmt/tm/ltm/global-settings"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

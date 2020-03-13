# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/global-settings' resources
# =============================================


class GtmGlobalsettingsSchema(MetaParser):

    schema = {}


class GtmGlobalsettings(GtmGlobalsettingsSchema):
    """ To F5 resource for /mgmt/tm/gtm/global-settings
    """

    cli_command = "/mgmt/tm/gtm/global-settings"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

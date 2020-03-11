# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/global-settings/general' resources
# =============================================


class GtmGlobalsettingsGeneralSchema(MetaParser):

    schema = {}


class GtmGlobalsettingsGeneral(GtmGlobalsettingsGeneralSchema):
    """ To F5 resource for /mgmt/tm/gtm/global-settings/general
    """

    cli_command = "/mgmt/tm/gtm/global-settings/general"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

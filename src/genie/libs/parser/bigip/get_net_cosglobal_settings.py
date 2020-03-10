# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cos/global-settings' resources
# =============================================


class NetCosGlobalsettingsSchema(MetaParser):

    schema = {}


class NetCosGlobalsettings(NetCosGlobalsettingsSchema):
    """ To F5 resource for /mgmt/tm/net/cos/global-settings
    """

    cli_command = "/mgmt/tm/net/cos/global-settings"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

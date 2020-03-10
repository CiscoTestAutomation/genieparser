# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/server' resources
# =============================================


class GtmServerSchema(MetaParser):

    schema = {}


class GtmServer(GtmServerSchema):
    """ To F5 resource for /mgmt/tm/gtm/server
    """

    cli_command = "/mgmt/tm/gtm/server"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

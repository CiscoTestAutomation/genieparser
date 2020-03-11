# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/route' resources
# =============================================


class NetRouteSchema(MetaParser):

    schema = {}


class NetRoute(NetRouteSchema):
    """ To F5 resource for /mgmt/tm/net/route
    """

    cli_command = "/mgmt/tm/net/route"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

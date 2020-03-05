# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/routing/route-map' resources
# =============================================


class NetRoutingRoutemapSchema(MetaParser):

    schema = {}


class NetRoutingRoutemap(NetRoutingRoutemapSchema):
    """ To F5 resource for /mgmt/tm/net/routing/route-map
    """

    cli_command = "/mgmt/tm/net/routing/route-map"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

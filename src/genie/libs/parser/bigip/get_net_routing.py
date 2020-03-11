# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/routing' resources
# =============================================


class NetRoutingSchema(MetaParser):

    schema = {}


class NetRouting(NetRoutingSchema):
    """ To F5 resource for /mgmt/tm/net/routing
    """

    cli_command = "/mgmt/tm/net/routing"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

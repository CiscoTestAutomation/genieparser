# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/routing/debug' resources
# =============================================


class NetRoutingDebugSchema(MetaParser):

    schema = {}


class NetRoutingDebug(NetRoutingDebugSchema):
    """ To F5 resource for /mgmt/tm/net/routing/debug
    """

    cli_command = "/mgmt/tm/net/routing/debug"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

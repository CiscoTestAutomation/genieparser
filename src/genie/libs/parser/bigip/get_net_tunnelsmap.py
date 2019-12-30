# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/map' resources
# =============================================


class NetTunnelsMapSchema(MetaParser):

    schema = {}


class NetTunnelsMap(NetTunnelsMapSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/map
    """

    cli_command = "/mgmt/tm/net/tunnels/map"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/lw4o6' resources
# =============================================


class NetTunnelsLw4o6Schema(MetaParser):

    schema = {}


class NetTunnelsLw4o6(NetTunnelsLw4o6Schema):
    """ To F5 resource for /mgmt/tm/net/tunnels/lw4o6
    """

    cli_command = "/mgmt/tm/net/tunnels/lw4o6"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

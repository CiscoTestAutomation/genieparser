# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/v6rd' resources
# =============================================


class NetTunnelsV6rdSchema(MetaParser):

    schema = {}


class NetTunnelsV6rd(NetTunnelsV6rdSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/v6rd
    """

    cli_command = "/mgmt/tm/net/tunnels/v6rd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json

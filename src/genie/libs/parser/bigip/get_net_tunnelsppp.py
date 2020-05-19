# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/tunnels/ppp' resources
# =============================================


class NetTunnelsPppSchema(MetaParser):

    schema = {}


class NetTunnelsPpp(NetTunnelsPppSchema):
    """ To F5 resource for /mgmt/tm/net/tunnels/ppp
    """

    cli_command = "/mgmt/tm/net/tunnels/ppp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
